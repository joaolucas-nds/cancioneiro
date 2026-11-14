"""Formulas de referencia (0.20.0, DEC-037; criterios da spec meta/specs/261111-formulas.md).
Formulas e acervos sinteticos, feitos a partir do data/demo.json."""
import copy
import json
import os
import subprocess
import sys

from conftest import DEMO, ROOT, changes, import_demo, write_tmp_collection

REFS = [
    {"id": "f-um", "label": "Fórmula um", "source": "Guia A",
     "style": "dream pop, soft female vocal, warm synths, 92 bpm", "notes": "Funciona pela voz na frente."},
    {"id": "f-dois", "label": "Fórmula dois", "source": "Guia B",
     "style": "synthwave, male vocal, analog bass, 95 BPM building to 115 BPM"},
    {"id": "f-tres", "label": "Fórmula três", "source": "Guia A",
     "style": "lo-fi hip hop, mellow piano, vinyl crackle, rain ambience, jazzy chords, "
              "soft drums, tape hiss, warm bass, late night, cozy, chill, nostalgic"},
]


def coll_with(refs, albums=True):
    """O demo com estas formulas; sem `albums`, so as formulas (albums: [])."""
    coll = copy.deepcopy(DEMO)
    if not albums:
        coll["albums"] = []
    coll["styleReferences"] = copy.deepcopy(refs)
    return coll


def open_refs(open_app, refs=REFS, **kw):
    page = open_app(**kw)
    import_demo(page, write_tmp_collection(coll_with(refs)))
    return page


def ref_ids(page):
    return page.evaluate("(App.collection.styleReferences || []).map(r => r.id)")


def open_dialog_by_side(page):
    page.click("#side-formulas-btn")
    page.wait_for_selector("#formulas-dialog[open]")


def test_c1_entradas_so_com_formulas(open_app):
    page = open_refs(open_app)
    assert page.is_visible("#side-formulas-btn")
    assert page.text_content("#side-formulas-btn .t") == "Fórmulas"
    assert page.text_content("#side-formulas-btn .n") == "3"
    # acima de «Todas as faixas»
    top_f = page.eval_on_selector("#side-formulas-btn", "e => e.getBoundingClientRect().top")
    top_all = page.eval_on_selector("#side-albums .side-item", "e => e.getBoundingClientRect().top")
    assert top_f < top_all
    page.click("#more-btn")
    assert page.is_visible("#menu-formulas")
    assert page.text_content("#menu-formulas") == "Fórmulas (3)"
    page.click("#menu-formulas")
    page.wait_for_selector("#formulas-dialog[open]")
    assert page.eval_on_selector_all("#formulas-body .formula", "e => e.length") == 3


def test_c1_sem_formulas_nada_aparece(open_app):
    page = open_app()
    import_demo(page)
    assert page.is_hidden("#side-formulas-btn")
    page.click("#more-btn")
    assert page.is_hidden("#menu-formulas")


def test_c2_janela_agrupa_copia_e_qualidade(open_app):
    page = open_refs(open_app)
    open_dialog_by_side(page)
    groups = page.eval_on_selector_all("#formulas-body .fgroup",
                                       "e => e.map(g => [g.querySelector('h3').textContent,"
                                       " [...g.querySelectorAll('.formula')].map(f => f.dataset.id)])")
    assert groups == [["Guia A", ["f-um", "f-tres"]], ["Guia B", ["f-dois"]]]
    # notas recolhidas; a formula sem notas nao tem o bloco
    assert page.eval_on_selector_all("#formulas-body details.formula-notes", "e => e.map(d => d.open)") == [False]
    for r in REFS:
        sel = f'#formulas-body .formula[data-id="{r["id"]}"]'
        page.click(sel + " .formula-copy")
        assert page.evaluate("navigator.clipboard.readText()") == r["style"]   # byte a byte, sem label nem notes
        got = page.text_content(sel + " .quality")
        want = page.evaluate("s => styleQuality(s, '').textContent", r["style"])
        assert got == want
    # a rampa avisa; a de 12 tags avisa em ambar
    assert "rampa de BPM" in page.text_content('.formula[data-id="f-dois"] .quality')
    assert page.eval_on_selector_all('.formula[data-id="f-tres"] .quality .q.warn', "e => e.length") >= 1


def test_c3_celular_tela_cheia_e_alvos(open_app):
    page = open_refs(open_app, width=390, height=844, mobile=True)
    page.click("#more-btn")
    page.click("#menu-formulas")
    page.wait_for_selector("#formulas-dialog[open]")
    box = page.eval_on_selector("#formulas-dialog", "e => { const r = e.getBoundingClientRect();"
                                " return [r.left, r.top, r.width, r.height]; }")
    assert box[0] == 0 and box[1] == 0 and box[2] == 390 and box[3] == 844
    small = page.eval_on_selector_all(
        "#formulas-dialog button, #formulas-dialog summary",
        "e => e.filter(x => x.offsetParent !== null && x.getBoundingClientRect().height < 44).map(x => x.className)")
    assert small == []
    assert page.evaluate("document.documentElement.scrollWidth") <= 390
    assert page.eval_on_selector("#formulas-body", "e => e.scrollWidth <= e.clientWidth")


def test_c4_excluir_e_desfazer(open_app):
    page = open_refs(open_app)
    open_dialog_by_side(page)
    page.click('.formula[data-id="f-dois"] .formula-del')
    page.click("#confirm-ok-btn")
    page.wait_for_selector("#formulas-status .formula-undo")   # a janela ja foi redesenhada
    assert ref_ids(page) == ["f-um", "f-tres"]
    assert changes(page) == 1
    assert page.is_hidden('.formula[data-id="f-dois"]')
    assert page.text_content("#side-formulas-btn .n") == "2"
    page.click("#formulas-status .formula-undo")
    page.wait_for_function("document.getElementById('formulas-status').textContent.startsWith('Desfeito')")
    assert ref_ids(page) == ["f-um", "f-dois", "f-tres"]   # na mesma posicao
    assert changes(page) == 0
    assert page.is_visible('.formula[data-id="f-dois"]')


def test_c4_excluir_a_ultima_tira_o_campo(open_app):
    page = open_refs(open_app, refs=REFS[:1])
    open_dialog_by_side(page)
    page.click('.formula[data-id="f-um"] .formula-del')
    page.click("#confirm-ok-btn")
    page.wait_for_selector("#formulas-status .formula-undo")
    assert "styleReferences" not in page.evaluate("Object.keys(App.collection)")
    page.click("#formulas-close-btn")
    assert page.is_hidden("#side-formulas-btn")


def test_c5_importar_so_formulas(open_app):
    page = open_refs(open_app, refs=REFS[:2])
    changed = dict(REFS[1], style=REFS[1]["style"] + ", glossy")
    novo = {"id": "f-nova", "label": "Nova", "style": "bossa nova, nylon guitar, brushed drums"}
    src = write_tmp_collection(coll_with([REFS[0], changed, novo], albums=False))
    page.set_input_files("#tracks-input", src)
    page.wait_for_selector("#import-dialog[open]")
    assert page.is_visible("#import-formulas")
    assert page.is_hidden("#import-dest")              # o destino vale so para as faixas
    assert page.text_content("#import-dialog-title") == "Importar fórmulas"
    assert page.eval_on_selector_all("#import-formula-list input", "e => e.map(c => c.checked)") == [True] * 3
    page.click("#import-ok-btn")
    # o aviso NOVO: o «Acervo importado» deixado pelo import_demo tambem tem «importad»
    page.wait_for_function("document.getElementById('toast').textContent.includes('fórmulas importadas')")
    assert ref_ids(page) == ["f-um", "f-dois", "f-dois-2", "f-nova"]
    assert page.evaluate("App.collection.styleReferences[2].style") == changed["style"]
    toast = page.text_content("#toast")
    assert toast.startswith("2 fórmulas importadas · 1 fórmula já estava · 1 fórmula renomeada (id repetido)")
    assert changes(page) == 1
    page.click("#toast .toast-btn")                    # «Desfazer»
    page.wait_for_function("App.collection.styleReferences.length === 2")


def test_c5_importar_faixas_e_formulas_soma(open_app):
    page = open_app()
    import_demo(page)
    src_coll = copy.deepcopy(DEMO)
    src_coll["albums"] = [{"id": "outro", "title": "Outro", "songs": [dict(DEMO["albums"][0]["songs"][0], id="nova-faixa")]}]
    src_coll["styleReferences"] = [REFS[0]]
    page.set_input_files("#tracks-input", write_tmp_collection(src_coll))
    page.wait_for_selector("#import-dialog[open]")
    assert page.text_content("#import-dialog-title") == "Importar faixas e fórmulas"
    assert page.is_visible("#import-dest")
    page.click("#import-ok-btn")
    page.wait_for_function("document.getElementById('toast').textContent.includes('fórmula importada')")
    assert page.text_content("#toast").startswith("1 faixa e 1 fórmula importadas")


def test_c6_baixar_leva_exportar_nao(open_app, tmp_path):
    page = open_refs(open_app)
    page.click("#more-btn")
    with page.expect_download() as d:
        page.click("#download-btn")
    path = tmp_path / "acervo.json"
    d.value.save_as(path)
    assert json.loads(path.read_text(encoding="utf-8"))["styleReferences"] == REFS
    for expr in ("exportSongJson(App.collection.albums[0].songs[0])", "exportAlbumJson(App.collection.albums[0])"):
        with page.expect_download() as d:
            page.evaluate(expr)
        p = tmp_path / "saida.json"
        d.value.save_as(p)
        assert "styleReferences" not in json.loads(p.read_text(encoding="utf-8"))
    md = page.evaluate("songToMarkdown(App.collection.albums[0].songs[0], true) + albumToMarkdown(App.collection.albums[0])")
    assert all(r["style"] not in md and r["label"] not in md for r in REFS)


def run_validate(path):
    return subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "validate.py"), str(path)],
                          capture_output=True, text=True)


def test_c7_validate_formulas(tmp_path):
    ok = tmp_path / "ok.json"
    ok.write_text(json.dumps(coll_with(REFS), ensure_ascii=False), encoding="utf-8")
    r = run_validate(ok)
    assert r.returncode == 0, r.stdout
    assert "3 fórmulas" in r.stdout
    bad_refs = copy.deepcopy(REFS)
    bad_refs[2]["id"] = "f-um"                                   # id repetido
    bad_refs[1]["style"] = ""                                    # style vazio
    bad_refs.append({"id": "f-quatro", "label": "Q", "style": "epic, choir, [SILENCE - 4 beats]"})
    bad = tmp_path / "bad.json"
    bad.write_text(json.dumps(coll_with(bad_refs), ensure_ascii=False), encoding="utf-8")
    r = run_validate(bad)
    assert r.returncode == 1
    assert "styleReferences[2].id: 'f-um' repetido" in r.stdout
    assert "styleReferences[1].style: vazio" in r.stdout
    assert "styleReferences[3].style: tem colchete" in r.stdout
    extra = copy.deepcopy(REFS)
    extra[0]["bpm"] = 92                                         # campo a mais: o esquema recusa
    ex = tmp_path / "extra.json"
    ex.write_text(json.dumps(coll_with(extra), ensure_ascii=False), encoding="utf-8")
    r = run_validate(ex)
    if "ESQUEMA NAO CONFERIDO" not in r.stdout:                  # sem jsonschema o esquema nao roda
        assert r.returncode == 1 and "ERRO de schema" in r.stdout


def test_c8_falso_positivo_importar_sem_formulas(open_app):
    page = open_app()
    import_demo(page)
    page.set_input_files("#tracks-input", write_tmp_collection(DEMO))
    page.wait_for_selector("#import-dialog[open]")
    assert page.is_hidden("#import-formulas")
    assert page.is_visible("#import-dest")
    assert page.text_content("#import-dialog-title") == "Importar faixas"
    assert "fórmula" not in page.inner_text("#import-dialog").lower()   # o que se ve
    page.click("#import-ok-btn")
    assert "styleReferences" not in page.evaluate("Object.keys(App.collection)")
    assert page.is_hidden("#side-formulas-btn")
