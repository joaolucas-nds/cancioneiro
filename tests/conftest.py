"""Infraestrutura dos testes do navegador (i-051, DEC-034).

O app e aberto no Chromium sem tela, servido por um http.server local em
127.0.0.1 (a pasta privada do navegador, que os testes da I4 usam no lugar das
janelas do sistema, e recusada no file://). Dados SO sinteticos: o
data/demo.json, que ja e publico, e acervos gerados por make_collection().
Nenhum acervo do dono entra aqui.

Rodar: python -m pytest tests  (precisa de: pip install -r tests/requirements.txt
e python -m playwright install chromium).
"""
import copy
import functools
import http.server
import json
import os
import re
import socketserver
import tempfile
import threading

import pytest
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEMO_PATH = os.path.join(ROOT, "data", "demo.json")
with open(DEMO_PATH, encoding="utf-8") as fh:
    DEMO_TEXT = fh.read()
DEMO = json.loads(DEMO_TEXT)


def changelog_version():
    """A versao do topo do CHANGELOG, a mesma fonte do validate.py."""
    with open(os.path.join(ROOT, "meta", "CHANGELOG.md"), encoding="utf-8") as fh:
        return re.search(r"^## \[(\d+\.\d+\.\d+)\]", fh.read(), re.M).group(1)


def make_collection(n_tracks, n_albums=12):
    """Acervo sintetico com n_tracks faixas, copiadas das tres do demo."""
    songs = [s for a in DEMO["albums"] for s in a["songs"]]
    coll = copy.deepcopy(DEMO)
    coll["albums"] = []
    per = -(-n_tracks // n_albums)
    for k in range(n_albums):
        album = {"id": f"al-{k:02d}", "title": f"Álbum {k + 1}", "songs": []}
        for _ in range(per):
            i = sum(len(a["songs"]) for a in coll["albums"]) + len(album["songs"])
            if i >= n_tracks:
                break
            s = copy.deepcopy(songs[i % len(songs)])
            s["id"], s["title"] = f"f-{i:03d}", f"Faixa {i + 1}"
            album["songs"].append(s)
        if album["songs"]:
            coll["albums"].append(album)
    return coll


class _Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


@pytest.fixture(scope="session")
def base_url():
    """Serve a raiz do repositorio numa porta livre, durante a sessao de testes."""
    handler = functools.partial(_Quiet, directory=ROOT)
    httpd = socketserver.ThreadingTCPServer(("127.0.0.1", 0), handler)
    httpd.daemon_threads = True
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    yield f"http://127.0.0.1:{httpd.server_address[1]}"
    httpd.shutdown()


@pytest.fixture(scope="session")
def pw():
    with sync_playwright() as p:
        yield p


# As janelas do sistema da I4 sao trocadas por arquivos da pasta privada do
# navegador (OPFS); a permissao de gravar, por __fs.perm / __fs.req.
FS_STUB = """
window.__fs = { cancel: false, openName: 'demo-acervo.json', saveName: null, perm: null, req: 'granted', calls: [] };
const P = FileSystemHandle.prototype;
P.queryPermission = async function () { __fs.calls.push('query'); return __fs.perm || 'granted'; };
P.requestPermission = async function () { __fs.calls.push('request'); return __fs.req; };
window.showSaveFilePicker = async o => { __fs.calls.push('save:' + (o && o.suggestedName));
  if (__fs.cancel) throw new DOMException('aborted', 'AbortError');
  const d = await navigator.storage.getDirectory(); return d.getFileHandle(__fs.saveName || o.suggestedName, { create: true }); };
window.showOpenFilePicker = async () => { __fs.calls.push('open');
  if (__fs.cancel) throw new DOMException('aborted', 'AbortError');
  const d = await navigator.storage.getDirectory(); return [await d.getFileHandle(__fs.openName)]; };
window.__keys = []; window.addEventListener('keydown', e => window.__keys.push(e), true);
"""
NO_FS_API = "delete window.showSaveFilePicker; delete window.showOpenFilePicker;"


@pytest.fixture
def open_app(pw, base_url):
    """Abre o app num perfil novo e persistente (no contexto anonimo, ler do
    IndexedDB um handle guardado derruba a aba: medido na I4). Devolve a pagina;
    page.errors guarda os erros de pagina, conferidos no fim de cada teste."""
    opened = []

    def _open(width=1366, height=800, mobile=False, init="", fs_api=True):
        kw = dict(viewport={"width": width, "height": height}, accept_downloads=True)
        if mobile:
            kw.update(is_mobile=True, has_touch=True)
        ctx = pw.chromium.launch_persistent_context(tempfile.mkdtemp(prefix="canc-"), **kw)
        ctx.grant_permissions(["clipboard-read", "clipboard-write"], origin=base_url)
        page = ctx.new_page()
        page.errors = []
        page.on("pageerror", lambda e: page.errors.append(str(e)))
        page.add_init_script(FS_STUB + ("" if fs_api else NO_FS_API) + init)
        page.goto(base_url + "/app/index.html")
        page.evaluate("bootDone")
        opened.append(page)
        return page

    yield _open
    for page in opened:
        errs = list(page.errors)
        page.context.close()
        assert not errs, f"erro de pagina: {errs}"


def import_demo(page, path=DEMO_PATH):
    """Importa um acervo pelo <input type=file> (o caminho de sempre)."""
    page.set_input_files("#file-input", path)
    page.wait_for_function("App.saved && App.collection")


def write_tmp_collection(coll):
    fd, path = tempfile.mkstemp(suffix=".json", prefix="acervo-")
    with os.fdopen(fd, "w", encoding="utf-8") as fh:
        json.dump(coll, fh, ensure_ascii=False, indent=2)
    return path


def rows(page):
    return page.eval_on_selector_all("#main li.row", "e => e.map(x => x.dataset.id)")


def album_ids(page, k=0):
    return page.evaluate(f"App.collection.albums[{k}].songs.map(s => s.id)")


def changes(page):
    return page.evaluate("App.changes")
