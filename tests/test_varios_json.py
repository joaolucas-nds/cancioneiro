"""Importar varios .json de uma vez (0.22.0; i-057, DEC-040; spec meta/specs/261116-varios-json.md).

O arraste e simulado com um DataTransfer montado na pagina: dragenter, dragover e drop
despachados no elemento-alvo. Dados so sinteticos."""
import copy
import json

from conftest import DEMO, changes, import_demo, make_collection, write_tmp_collection

# A pagina guarda cada arquivo pelo NOME: os testes dao nomes fixos aos sinteticos.
DROP_JS = """([sel, files]) => {
  const dt = new DataTransfer();
  files.forEach(([n, t]) => dt.items.add(new File([t], n, { type: 'application/json' })));
  const el = document.querySelector(sel);
  for (const type of ['dragenter', 'dragover', 'drop'])
    el.dispatchEvent(new DragEvent(type, { bubbles: true, cancelable: true, dataTransfer: dt }));
}"""
HOVER_JS = """([sel, n]) => {
  const dt = new DataTransfer();
  for (let i = 0; i < n; i++) dt.items.add(new File(['{}'], 'x' + i + '.json', { type: 'application/json' }));
  const el = document.querySelector(sel);
  for (const type of ['dragenter', 'dragover'])
    el.dispatchEvent(new DragEvent(type, { bubbles: true, cancelable: true, dataTransfer: dt }));
  return document.querySelector('.drop-hint').textContent;
}"""


def coll(n_tracks, n_albums, title, prefix):
    """Acervo sintetico com ids proprios (nao colidem com o demo)."""
    c = make_collection(n_tracks, n_albums)
    c["title"] = title
    for a in c["albums"]:
        a["id"] = prefix + "-" + a["id"]
        for s in a["songs"]:
            s["id"] = prefix + "-" + s["id"]
    return c


def track_export(song_id="solo-1", title="Faixa solta", style="pop, synth, 100 bpm"):
    """A forma do «Exportar faixa»: um album com uma faixa."""
    c = copy.deepcopy(DEMO)
    s = copy.deepcopy(DEMO["albums"][0]["songs"][0])
    s["id"], s["title"], s["style"] = song_id, title, style
    c["albums"] = [{"id": "alb-solo", "title": "Álbum solto", "songs": [s]}]
    c["title"] = "Exportada"
    return c


def text(c):
    return json.dumps(c, ensure_ascii=False)


def drop(page, sel, files):
    page.evaluate(DROP_JS, [sel, [[n, t if isinstance(t, str) else text(t)] for n, t in files]])


def stored(page):
    return sorted(page.evaluate("dbAll().then(r => r.map(x => x.source))"))


def wait_toast(page, piece):
    page.wait_for_function("p => document.getElementById('toast').textContent.includes(p)", arg=piece)
    return page.text_content("#toast")


def multi_open(page):
    """A janela de varios esta aberta? (Falso na 0.21.0, onde ela nem existe: os testes de V1 rodam nas duas.)"""
    return page.evaluate("!!(document.getElementById('multi-dialog') || {}).open")


def multi_rows(page):
    # 0.23 (i-061): a escolha e um grupo de botoes de opcao; «desligada» = os tres desligados
    return page.eval_on_selector_all(
        "#multi-list > li", "e => e.map(li => [li.querySelector('.multi-name').textContent,"
        " li.querySelector('.multi-info').textContent, (li.querySelector('.seg input:checked') || {}).value,"
        " [...li.querySelectorAll('.seg input')].every(r => r.disabled)])")


# ---------------------------------------------------------------- V1: um arquivo, nada muda
def test_v1_um_arquivo_na_pagina_importa_e_abre(open_app):
    """V1 (falso positivo): um arquivo solto na pagina vira o acervo aberto, como na 0.21.0; sem a janela nova."""
    page = open_app()
    import_demo(page)
    drop(page, "#main", [("um.json", coll(3, 1, "Um", "um"))])
    page.wait_for_function("App.source === 'um.json'")
    # O texto NOVO inteiro: o aviso do import_demo («Acervo importado: Acervo de demonstracao») ainda pode estar na tela
    assert wait_toast(page, "Acervo importado: Um").startswith("Acervo importado: Um")
    assert not multi_open(page)
    assert stored(page) == ["demo.json", "um.json"]


def test_v1_um_arquivo_no_album_abre_importar_faixas(open_app):
    """V1 (falso positivo): um arquivo solto sobre um album abre «Importar faixas» para ele, como antes."""
    page = open_app()
    import_demo(page)
    alb = page.evaluate("App.collection.albums[1].id")
    drop(page, f'#main section.album[data-album="{alb}"] .album-head', [("f.json", coll(2, 1, "F", "f"))])
    page.wait_for_selector("#import-dialog[open]")
    assert page.input_value("#import-target") == alb
    assert not multi_open(page)


# ---------------------------------------------------------------- V2: a janela lista os arquivos
def test_v2_tres_na_pagina_listam_na_ordem_e_o_invalido_vem_desligado(open_app):
    """V2: tres arquivos soltos na pagina abrem «Importar 3 arquivos», na ordem, com o que cada um tem;
    o invalido vem desligado e nao trava os outros."""
    page = open_app()
    import_demo(page)
    a = coll(4, 2, "A", "a")
    a["styleReferences"] = [{"id": "r1", "label": "R", "source": "G", "style": "jazz, piano, 90 bpm"}]
    drop(page, "#main", [("a.json", a), ("lixo.json", "isto nao e json"), ("b.json", coll(3, 1, "B", "b"))])
    page.wait_for_selector("#multi-dialog[open]")
    assert page.text_content("#multi-dialog-title") == "Importar 3 arquivos"
    assert multi_rows(page) == [
        ["a.json", "2 álbuns · 4 faixas · 1 fórmula", "new", False],
        ["lixo.json", "não é um JSON válido", "skip", True],
        ["b.json", "1 álbum · 3 faixas", "new", False],
    ]
    page.click("#multi-ok-btn")
    wait_toast(page, "2 acervos guardados")
    assert stored(page) == ["a.json", "b.json", "demo.json"]


# ---------------------------------------------------------------- V3: acervo novo + faixas, um «Desfazer»
def test_v3_dois_acervos_novos_e_uma_faixa_sem_trocar_o_aberto(open_app):
    """V3: dois em «Acervo novo» e a faixa exportada em «Faixas» (o padrao pela forma, DEC-040 1a):
    os dois ficam guardados sem trocar o aberto; a faixa entra no aberto; o aviso soma; um «Desfazer»
    devolve o aberto como estava."""
    page = open_app()
    import_demo(page)
    before = page.evaluate("JSON.stringify(App.collection)")
    drop(page, "#main", [("a.json", coll(4, 2, "A", "a")), ("b.json", coll(3, 1, "B", "b")),
                         ("solo.json", track_export())])
    page.wait_for_selector("#multi-dialog[open]")
    assert [r[2] for r in multi_rows(page)] == ["new", "new", "tracks"]
    assert page.is_visible("#multi-target")                     # com «Faixas», o destino aparece
    page.click("#multi-ok-btn")
    msg = wait_toast(page, "acervos guardados")
    assert msg.startswith("1 faixa importada") and "2 acervos guardados: a.json, b.json" in msg
    assert page.evaluate("App.source") == "demo.json"
    assert stored(page) == ["a.json", "b.json", "demo.json"]
    assert "solo-1" in page.evaluate("App.collection.albums.flatMap(a => a.songs.map(s => s.id))")
    assert changes(page) == 1
    page.click("#toast .toast-btn")                              # «Desfazer»
    wait_toast(page, "Desfeito: 1 faixa importada")
    assert page.evaluate("JSON.stringify(App.collection)") == before
    assert stored(page) == ["a.json", "b.json", "demo.json"]   # o «Desfazer» nao apaga os guardados


def test_v3_sem_faixas_o_destino_some(open_app):
    """V3: o destino so aparece quando alguma linha esta em «Faixas»."""
    page = open_app()
    import_demo(page)
    drop(page, "#main", [("a.json", coll(2, 1, "A", "a")), ("b.json", coll(2, 1, "B", "b"))])
    page.wait_for_selector("#multi-dialog[open]")
    assert page.is_hidden("#multi-dest")
    page.click("#multi-list > li:first-child .seg label:has(input[value=tracks])")
    assert page.is_visible("#multi-dest")


# ---------------------------------------------------------------- V4: a regra de id entre arquivos
def test_v4_mesmo_id_entre_arquivos_ganha_sufixo_e_identica_pula(open_app):
    """V4: pelo «Importar faixas…» com dois arquivos, tudo vem em «Faixas»; a faixa do segundo com o
    mesmo id e conteudo diferente entra com -2; a identica a uma do aberto pula."""
    page = open_app()
    import_demo(page)
    same = copy.deepcopy(DEMO)                                    # uma faixa identica a do demo
    same["albums"] = [copy.deepcopy(DEMO["albums"][0])]
    same["albums"][0]["songs"] = same["albums"][0]["songs"][:1]
    p1, p2 = write_tmp_collection(track_export("x-1", "X um", "pop")), write_tmp_collection(track_export("x-1", "X dois", "rock"))
    page.set_input_files("#tracks-input", [p1, p2, write_tmp_collection(same)])
    page.wait_for_selector("#multi-dialog[open]")
    assert [r[2] for r in multi_rows(page)] == ["tracks", "tracks", "tracks"]
    page.click("#multi-ok-btn")
    msg = wait_toast(page, "arquivos:")
    assert msg.startswith("3 arquivos: 2 faixas importadas · 1 já estava · 1 renomeada (id repetido)")
    ids = page.evaluate("App.collection.albums.flatMap(a => a.songs.map(s => s.id))")
    assert "x-1" in ids and "x-1-2" in ids


# ---------------------------------------------------------------- V5: a lateral guarda direto
def test_v5_dois_na_lateral_viram_acervos_sem_janela(open_app):
    """V5: dois arquivos soltos na lateral, fora de um album: dois acervos guardados, sem janela,
    e o aberto nao muda (DEC-040, 3a)."""
    page = open_app()
    import_demo(page)
    drop(page, "#side .side-head", [("a.json", coll(2, 1, "A", "a")), ("b.json", coll(2, 1, "B", "b"))])
    assert wait_toast(page, "acervos guardados").startswith("2 acervos guardados: a.json, b.json")
    assert not multi_open(page)
    assert page.evaluate("App.source") == "demo.json"
    assert stored(page) == ["a.json", "b.json", "demo.json"]
    page.wait_for_function("document.querySelectorAll('#side-acervos li').length === 3")


def test_v5_um_na_lateral_tambem_guarda_sem_abrir(open_app):
    """V5 (DEC-040, 4a): um arquivo so, na lateral, tambem vira acervo guardado sem trocar o aberto."""
    page = open_app()
    import_demo(page)
    drop(page, "#side .side-head", [("a.json", coll(2, 1, "A", "a"))])
    assert wait_toast(page, "acervo guardado").startswith("1 acervo guardado: a.json")
    assert page.evaluate("App.source") == "demo.json"


def test_v5_mesmo_nome_com_alteracoes_confirma_so_esse(open_app):
    """V5: com o mesmo nome de um guardado com alteracoes, a confirmacao aparece so para ele."""
    page = open_app()
    import_demo(page, write_tmp_collection(coll(2, 1, "P", "p")))
    p_name = page.evaluate("App.source")
    page.evaluate("async () => { beginEdit(); App.collection.albums[0].title += ' x'; await afterEdit('t'); }")
    import_demo(page)                                             # o demo fica aberto; P guardado com 1 alteracao
    page.wait_for_function("App.source === 'demo.json'")
    drop(page, "#side .side-head", [(p_name, coll(3, 1, "P novo", "p")), ("q.json", coll(2, 1, "Q", "q"))])
    page.wait_for_selector("#confirm-dialog[open]")
    t = page.text_content("#confirm-text")
    assert p_name in t and "q.json" not in t and "1 alteração não salva se perde" in t
    page.click("#confirm-ok-btn")
    msg = wait_toast(page, "acervos guardados")
    assert msg.startswith("2 acervos guardados: " + p_name + ", q.json")
    assert not page.evaluate("document.getElementById('confirm-dialog').open")
    assert page.evaluate(f"dbGet({json.dumps(p_name)}).then(r => [r.json.title, r.changes || 0])") == ["P novo", 0]
    assert page.evaluate("App.source") == "demo.json"


def test_v5_sobre_album_da_lateral_continua_faixas(open_app):
    """V5 (falso positivo): sobre um album da lateral, um arquivo continua «Importar faixas» naquele album;
    dois abrem a janela com «Faixas» e o album ja escolhidos."""
    page = open_app()
    import_demo(page)
    alb = page.evaluate("App.collection.albums[0].id")
    drop(page, f'#side .side-item[data-album="{alb}"]', [("a.json", coll(2, 1, "A", "a"))])
    page.wait_for_selector("#import-dialog[open]")
    assert page.input_value("#import-target") == alb
    page.click("#import-cancel-btn")
    drop(page, f'#side .side-item[data-album="{alb}"]', [("a.json", coll(2, 1, "A", "a")), ("b.json", coll(2, 1, "B", "b"))])
    page.wait_for_selector("#multi-dialog[open]")
    assert [r[2] for r in multi_rows(page)] == ["tracks", "tracks"]
    assert page.input_value("#multi-target") == alb


def test_v5_o_aviso_do_arraste_diz_a_zona(open_app):
    """Item 4 da spec: o aviso do arraste muda com a zona e com o numero de arquivos."""
    page = open_app()
    import_demo(page)
    alb = page.evaluate("App.collection.albums[0].id")
    # 0.23.1: sobre a lateral, o aviso dela e o da propria lateral (o da pagina continua o da pagina)
    assert page.evaluate(HOVER_JS, ["#side .side-head", 2]) == "Solte para escolher o que cada um vira"
    assert page.evaluate("getComputedStyle(document.getElementById('side'), '::after').content") \
        == '"Solte aqui: cada arquivo vira um acervo guardado"'
    assert page.evaluate(HOVER_JS, [f'#side .side-item[data-album="{alb}"]', 1]) == "Solte aqui: as faixas vão para este álbum"
    assert page.evaluate(HOVER_JS, ["#main", 1]) == "Solte para importar"
    assert page.evaluate(HOVER_JS, ["#main", 3]) == "Solte para escolher o que cada um vira"


def test_v5_todos_os_vinculos_sao_pegos_durante_o_drop(open_app):
    """Risco da spec (DEC-033): o vinculo de cada arquivo so existe durante o drop. Os pedidos tem de sair
    TODOS antes de o drop terminar, e cada acervo novo fica vinculado ao seu arquivo."""
    stub = """
    window.__hcalls = 0;
    DataTransferItem.prototype.getAsFileSystemHandle = function () {
      window.__hcalls++;
      const f = this.getAsFile();
      return navigator.storage.getDirectory().then(d => d.getFileHandle(f.name, { create: true }));
    };"""
    page = open_app(init=stub)
    import_demo(page)
    files = [["a.json", text(coll(2, 1, "A", "a"))], ["b.json", text(coll(2, 1, "B", "b"))]]
    calls = page.evaluate("args => { (" + DROP_JS + ")(args); return window.__hcalls; }", ["#side .side-head", files])
    assert calls == 2                                             # os dois pedidos, ainda dentro do drop
    wait_toast(page, "acervos guardados")
    assert page.evaluate("dbAll().then(r => r.filter(x => x.fileHandle).map(x => x.fileHandle.name).sort())") == ["a.json", "b.json"]


# ---------------------------------------------------------------- V6: sem acervo aberto
def test_v6_sem_acervo_aberto_tudo_vira_acervo_novo(open_app):
    """V6: sem acervo aberto, «Faixas» vem desligada, tudo e «Acervo novo», e abre o primeiro (DEC-040, 2a)."""
    page = open_app()
    drop(page, "#main", [("a.json", coll(2, 1, "A", "a")), ("solo.json", track_export())])
    page.wait_for_selector("#multi-dialog[open]")
    assert [r[2] for r in multi_rows(page)] == ["new", "new"]
    assert page.eval_on_selector_all("#multi-list input[value=tracks]", "e => e.map(o => o.disabled)") == [True, True]
    page.click("#multi-ok-btn")
    msg = wait_toast(page, "acervos guardados")
    assert msg.startswith("2 acervos guardados: a.json, solo.json · aberto: A")
    assert page.evaluate("App.source") == "a.json"
    assert stored(page) == ["a.json", "solo.json"]


# ---------------------------------------------------------------- V7: no celular
def test_v7_celular_a_janela_ocupa_a_tela(open_app):
    """V7: a 390 px a janela ocupa a tela, os alvos tem 44 px ou mais e nada rola para os lados."""
    page = open_app(width=390, height=844, mobile=True)
    import_demo(page)
    long_name = "um-nome-de-arquivo-bem-comprido-que-nao-quebra-sozinho-" + "x" * 40 + ".json"
    paths = [write_tmp_collection(coll(2, 1, "A", "a")), write_tmp_collection(coll(2, 1, "B", "b"))]
    page.set_input_files("#file-input", paths)
    page.wait_for_selector("#multi-dialog[open]")
    page.evaluate("n => { document.querySelector('#multi-list .multi-name').textContent = n; }", long_name)
    box = page.evaluate("(() => { const r = document.getElementById('multi-dialog').getBoundingClientRect();"
                        " return [r.left, r.width]; })()")
    assert box == [0, 390]
    small = page.eval_on_selector_all("#multi-dialog select, #multi-dialog button, #multi-dialog .seg span",
                                      "e => e.filter(x => x.offsetParent && x.getBoundingClientRect().height < 44).length")
    assert small == 0
    assert page.evaluate("(() => { const d = document.getElementById('multi-dialog');"
                         " return d.scrollWidth <= d.clientWidth && document.documentElement.scrollWidth <= 390; })()")
