"""Começar vazio, esquecer todos e a janela de importar por grupo (0.21.0; i-058, i-059, i-053;
spec meta/specs/261116-importar-e-comecar-vazio.md). Dados sinteticos."""
import copy

from conftest import DEMO, changes, import_demo, make_collection, write_tmp_collection

REFS = [
    {"id": "f-a1", "label": "A um", "source": "Guia A", "style": "pop, synth, 100 bpm"},
    {"id": "f-b1", "label": "B um", "source": "Guia B", "style": "rock, guitar, 120 bpm"},
    {"id": "f-a2", "label": "A dois", "source": "Guia A", "style": "jazz, piano, 90 bpm"},
]


def refs_only():
    coll = copy.deepcopy(DEMO)
    coll["albums"] = []
    coll["styleReferences"] = copy.deepcopy(REFS)
    return coll


def open_import(page, coll):
    page.set_input_files("#tracks-input", write_tmp_collection(coll))
    page.wait_for_selector("#import-dialog[open]")


def test_v1_abre_vazio_sem_buscar_o_exemplo(open_app):
    """C1: em http:// o app abre vazio e nao pede o data/demo.json (i-058)."""
    asked = []
    page = open_app(init="")
    page.on("request", lambda r: asked.append(r.url))
    page.reload()
    page.evaluate("bootDone")
    page.wait_for_timeout(300)
    assert page.evaluate("App.collection") is None
    assert page.is_visible("#empty")
    assert not [u for u in asked if u.endswith("demo.json")]


def test_v2_esquecer_todos(open_app):
    """C2: com dois acervos guardados, «Esquecer todos» avisa as alteracoes, apaga as copias e volta ao vazio;
    as marcas «usei» ficam (i-059)."""
    page = open_app()
    import_demo(page, write_tmp_collection(make_collection(3, 1)))
    import_demo(page)                                         # o segundo, aberto
    page.wait_for_function("App.source === 'demo.json' && Store.count === 2")
    page.click("#main li.row .row-used")                      # uma marca «usei»
    page.evaluate("async () => { App.changes = 0; beginEdit(); App.collection.albums[0].title += ' x'; await afterEdit('t'); }")
    page.click("#acervo-btn")
    page.wait_for_selector("#forget-all-btn", state="visible")   # a lista se desenha depois de abrir
    page.click("#forget-all-btn")
    page.wait_for_selector("#confirm-dialog[open]")
    text = page.text_content("#confirm-text")
    assert "os 2 acervos guardados" in text and "1 alteração não salva se perde" in text
    page.click("#confirm-ok-btn")
    page.wait_for_function("App.collection === null && Store.count === 0")
    assert page.is_visible("#empty")
    assert page.evaluate("dbAll().then(r => r.length)") == 0
    assert page.evaluate("Object.keys((App.ui.usedBy || {})['demo.json'] || {}).length") == 1
    page.reload()
    page.evaluate("bootDone")
    assert page.evaluate("App.collection") is None


def test_v2_falso_positivo_um_acervo_so(open_app):
    """C2: com um acervo so, «Esquecer todos» nao aparece; cancelar nao apaga nada."""
    page = open_app()
    import_demo(page)
    page.click("#acervo-btn")
    page.wait_for_function("document.querySelectorAll('#acervos-list li[data-source]').length === 1")
    assert page.is_hidden("#forget-all-btn")
    page.keyboard.press("Escape")                              # fecha o menu antes de reabrir
    import_demo(page, write_tmp_collection(make_collection(3, 1)))
    page.wait_for_function("App.source !== 'demo.json' && Store.count === 2")
    page.click("#acervo-btn")
    page.wait_for_selector("#forget-all-btn", state="visible")
    page.click("#forget-all-btn")
    page.click("#confirm-cancel-btn")
    assert page.evaluate("dbAll().then(r => r.length)") == 2 and page.evaluate("App.collection") is not None


def test_v3_grupo_de_album_marca_e_desmarca(open_app):
    """C3: na importacao de faixas, a caixa do album marca e desmarca as faixas dele; meio marcada com parte (i-053)."""
    page = open_app()
    import_demo(page)
    src = make_collection(4, 2)                                # 2 albuns de 2 faixas
    open_import(page, src)
    groups = page.query_selector_all("#import-list label.grp input")
    assert len(groups) == 2 and all(g.is_checked() for g in groups)
    groups[0].click()                                          # desmarca o primeiro album
    keys = page.eval_on_selector_all("#import-list input[data-key]", "e => e.map(c => [c.dataset.key, c.checked])")
    assert keys == [["0:0", False], ["0:1", False], ["1:0", True], ["1:1", True]]
    page.click('#import-list input[data-key="1:0"]')          # parte do segundo
    assert page.eval_on_selector_all("#import-list label.grp input", "e => e.map(c => c.indeterminate)") == [False, True]
    page.click("#import-ok-btn")
    page.wait_for_function("document.getElementById('toast').textContent.includes('faixa importada')")
    assert page.text_content("#toast").startswith("1 faixa importada")


def test_v4_formulas_por_origem_e_o_texto(open_app):
    """C4: as formulas vem agrupadas por origem, com a caixa do grupo; o texto diz «Fórmula idêntica» (i-053)."""
    page = open_app()
    import_demo(page)
    open_import(page, refs_only())
    assert page.text_content("#import-what") == "Fórmula idêntica a uma"
    got = page.eval_on_selector_all("#import-formula-list > li", "e => e.map(li => [li.querySelector('label.grp').textContent.trim(),"
                                    " [...li.querySelectorAll('input[data-ref]')].map(c => Number(c.dataset.ref))])")
    assert got == [["Guia A", [0, 2]], ["Guia B", [1]]]
    page.click("#import-formula-list > li:first-child label.grp input")   # sem o Guia A
    page.click("#import-ok-btn")
    page.wait_for_function("document.getElementById('toast').textContent.includes('fórmula importada')")
    assert page.evaluate("App.collection.styleReferences.map(r => r.id)") == ["f-b1"]


def test_v4_texto_misto_e_so_faixas(open_app):
    """C4: com faixas e formulas, «Faixa ou fórmula idêntica»; so faixas, o texto de antes."""
    page = open_app()
    import_demo(page)
    mixed = make_collection(2, 1)
    mixed["styleReferences"] = copy.deepcopy(REFS[:1])
    open_import(page, mixed)
    assert page.text_content("#import-what") == "Faixa ou fórmula idêntica a uma"
    page.click("#import-cancel-btn")
    open_import(page, make_collection(2, 1))
    assert page.text_content("#import-what") == "Faixa idêntica a uma"
    assert changes(page) == 0
