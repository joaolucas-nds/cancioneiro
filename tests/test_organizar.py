"""Organizar (I3, DEC-032): «⋯», arrastar, lote, excluir, mover e «Desfazer»."""
from conftest import DEMO, album_ids, changes, import_demo, rows

A0 = [s["id"] for s in DEMO["albums"][0]["songs"]]


def menu(page, song_id):
    page.click(f'#main li.row[data-id="{song_id}"] .row-more')


def test_descer_pelo_menu_e_desfazer(open_app):
    page = open_app()
    import_demo(page)
    menu(page, A0[0])
    page.click("#tm-down")
    assert album_ids(page)[:2] == [A0[1], A0[0]] and changes(page) == 1
    page.click("#toast button")  # «Desfazer»
    assert album_ids(page) == A0 and changes(page) == 0


def test_arrastar_pela_alca_muda_a_ordem(open_app):
    page = open_app()
    import_demo(page)
    src = page.locator(f'#main li.row[data-id="{A0[0]}"] .row-grip')
    dst = page.locator(f'#main li.row[data-id="{A0[1]}"]')
    src.evaluate("e => e.scrollIntoView({block: 'center'})")
    a, b = src.bounding_box(), dst.bounding_box()
    page.mouse.move(a["x"] + a["width"] / 2, a["y"] + a["height"] / 2)
    page.mouse.down()
    for k in range(1, 11):
        page.mouse.move(a["x"] + a["width"] / 2, b["y"] + b["height"] * (0.2 + 0.07 * k))
        page.wait_for_timeout(30)
    page.mouse.up()
    page.wait_for_timeout(300)
    assert album_ids(page)[:2] == [A0[1], A0[0]] and changes(page) == 1


def test_soltar_no_mesmo_lugar_nao_conta(open_app):
    page = open_app()
    import_demo(page)
    src = page.locator(f'#main li.row[data-id="{A0[0]}"] .row-grip')
    a = src.bounding_box()
    page.mouse.move(a["x"] + 5, a["y"] + 5)
    page.mouse.down()
    page.mouse.move(a["x"] + 8, a["y"] + 9)
    page.mouse.move(a["x"] + 5, a["y"] + 5)
    page.mouse.up()
    page.wait_for_timeout(300)
    assert album_ids(page) == A0 and changes(page) == 0


def test_lote_seleciona_e_esc_limpa(open_app):
    page = open_app()
    import_demo(page)
    for i in A0[:2]:
        page.click(f'#main li.row[data-id="{i}"] .row-sel input')
    assert "2 faixas selecionadas" in page.text_content("#batch-count")
    page.keyboard.press("Escape")
    assert page.is_hidden("#batch")


def test_excluir_confirma_e_ctrl_z_volta(open_app):
    page = open_app()
    import_demo(page)
    menu(page, A0[0])
    page.click("#tm-delete")
    page.click("#confirm-ok-btn")
    assert A0[0] not in rows(page) and changes(page) == 1
    page.click("body", position={"x": 5, "y": 400})
    page.keyboard.press("Control+z")
    page.wait_for_timeout(200)
    assert A0[0] in rows(page) and changes(page) == 0


def test_ctrl_z_na_busca_nao_mexe_no_acervo(open_app):
    page = open_app()
    import_demo(page)
    menu(page, A0[0])
    page.click("#tm-down")
    page.fill("#search", "x")
    page.focus("#search")
    page.keyboard.press("Control+z")
    page.wait_for_timeout(200)
    assert changes(page) == 1


def test_mover_para_outro_album(open_app):
    page = open_app()
    import_demo(page)
    alvo = DEMO["albums"][1]
    menu(page, A0[0])
    page.click("#tm-move")
    page.select_option("#move-target", alvo["id"])
    page.click("#move-ok-btn")
    assert page.evaluate("App.collection.albums[1].songs.map(s => s.id)")[-1] == A0[0]


def test_sem_copia_guardada_nao_ha_alca(open_app):
    """O exemplo que o Pages carrega sozinho nao tem rascunho (C9 da I3)."""
    page = open_app()
    page.wait_for_function("App.collection && App.collection.albums")   # o exemplo carregado sozinho (http://)
    page.evaluate("d => { setCollection(d); App.saved = false; render(); }", DEMO)
    assert page.eval_on_selector_all("#main .row-grip", "e => e.length") == 0
