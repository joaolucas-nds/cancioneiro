"""Organizar os albuns (0.18.0, i-049, DEC-035; criterios da spec
meta/specs/261109-organizar-os-albuns.md). Acervo sintetico de 4 albuns."""
import json
import os
import tempfile

from conftest import changes, import_demo, make_collection, write_tmp_collection

COLL = make_collection(12, 4)   # 4 albuns de 3 faixas: al-00 .. al-03


def open4(open_app, **kw):
    page = open_app(**kw)
    import_demo(page, write_tmp_collection(COLL))
    return page


def album_order(page):
    return page.evaluate("App.collection.albums.map(a => a.id)")


def head_menu(page, album_id):
    page.click(f'#main section.album[data-album="{album_id}"] .album-more')


def items(page):
    return page.eval_on_selector_all("#album-pop [role=menuitem]",
                                     "e => e.filter(x => x.offsetParent !== null).map(x => [x.id, x.disabled])")


def undo(page):
    page.click("body", position={"x": 600, "y": 5})
    page.keyboard.press("Control+z")
    page.wait_for_timeout(200)


def test_c1_menu_no_cabecalho_e_na_lateral(open_app):
    page = open4(open_app)
    head_menu(page, "al-00")
    got = dict(items(page))
    assert list(got) == ["am-rename", "am-up", "am-down", "am-merge", "am-md", "am-json", "am-delete"]
    assert got["am-up"] is True and got["am-down"] is False   # Subir desligado no primeiro
    page.keyboard.press("Escape")
    assert page.is_hidden("#album-pop")
    page.click('#side .side-album[data-album="al-03"] .side-more')
    got = dict(items(page))
    assert got["am-down"] is True and got["am-up"] is False


def test_c1_sem_copia_guardada_so_exporta(open_app):
    page = open_app()
    # Em http://, o app carrega sozinho o exemplo do repositorio (DEC-006); espera ele
    # chegar, senao ele chega depois e cobre este acervo.
    page.wait_for_function("App.collection && App.collection.albums")
    page.evaluate("d => { setCollection(d); App.saved = false; render(); }", COLL)
    head_menu(page, "al-00")
    got = dict(items(page))
    assert got["am-md"] is False and got["am-json"] is False
    assert all(got[k] for k in ("am-rename", "am-up", "am-down", "am-merge", "am-delete"))
    assert page.is_visible("#am-note")
    assert page.eval_on_selector_all("#side .side-grip", "e => e.length") == 0


def test_c2_renomear_titulo_e_descricao(open_app):
    page = open4(open_app)
    head_menu(page, "al-01")
    page.click("#am-rename")
    page.fill("#album-title-input", "")
    assert page.is_disabled("#album-ok-btn")   # titulo vazio nao renomeia
    page.fill("#album-title-input", "Álbum 1")   # nome de outro album: avisa, mas deixa
    assert page.is_visible("#album-dup-note")
    page.fill("#album-title-input", "Manhãs lentas")
    page.fill("#album-desc-input", "violão e voz")
    page.click("#album-ok-btn")
    page.wait_for_timeout(200)
    a = page.evaluate("App.collection.albums[1]")
    assert a["id"] == "al-01" and a["title"] == "Manhãs lentas" and a["description"] == "violão e voz"
    assert changes(page) == 1
    assert "Manhãs lentas" in page.text_content('#side .side-item[data-album="al-01"]')
    assert page.text_content('#main section.album[data-album="al-01"] .album-desc') == "violão e voz"
    undo(page)
    assert page.evaluate("App.collection.albums[1].title") == "Álbum 2" and changes(page) == 0


def test_c2_renomear_sem_mudanca_nao_conta(open_app):
    page = open4(open_app)
    head_menu(page, "al-01")
    page.click("#am-rename")
    page.click("#album-ok-btn")
    page.wait_for_timeout(200)
    assert changes(page) == 0


def test_c3_subir_descer_e_alt_setas(open_app):
    page = open4(open_app)
    head_menu(page, "al-00")
    page.click("#am-down")
    assert album_order(page) == ["al-01", "al-00", "al-02", "al-03"] and changes(page) == 1
    sec = page.eval_on_selector_all("#main section.album", "e => e.map(x => x.dataset.album)")
    assert sec[:2] == ["al-01", "al-00"]
    page.focus('#side .side-item[data-album="al-03"]')
    page.keyboard.press("Alt+ArrowUp")
    page.wait_for_timeout(200)
    assert album_order(page) == ["al-01", "al-00", "al-03", "al-02"] and changes(page) == 2


def drag(page, src, dst_box, frac):
    s = src.bounding_box()
    page.mouse.move(s["x"] + s["width"] / 2, s["y"] + s["height"] / 2)
    page.mouse.down()
    for k in range(1, 13):
        page.mouse.move(s["x"] + s["width"] / 2, s["y"] + (dst_box["y"] + dst_box["height"] * frac - s["y"]) * k / 12)
        page.wait_for_timeout(30)
    page.mouse.up()
    page.wait_for_timeout(300)


def test_c4_arrastar_album_na_lateral(open_app):
    page = open4(open_app)
    grip = page.locator('#side .side-album[data-album="al-00"] .side-grip')
    dst = page.locator('#side .side-album[data-album="al-02"]').bounding_box()
    drag(page, grip, dst, 0.8)
    assert album_order(page)[:3] == ["al-01", "al-02", "al-00"] and changes(page) == 1


def test_c4_soltar_no_mesmo_lugar_nao_conta(open_app):
    page = open4(open_app)
    grip = page.locator('#side .side-album[data-album="al-01"] .side-grip')
    b = grip.bounding_box()
    page.mouse.move(b["x"] + 5, b["y"] + 5)
    page.mouse.down()
    page.mouse.move(b["x"] + 7, b["y"] + 9)
    page.mouse.move(b["x"] + 5, b["y"] + 5)
    page.mouse.up()
    page.wait_for_timeout(300)
    assert album_order(page) == ["al-00", "al-01", "al-02", "al-03"] and changes(page) == 0


def test_c4_faixa_sobre_album_da_lateral_continua(open_app):
    """Regressao da I3: arrastar uma faixa sobre um album da lateral leva ao fim dele."""
    page = open4(open_app)
    grip = page.locator('#main li.row[data-id="f-000"] .row-grip')
    grip.evaluate("e => e.scrollIntoView({block: 'center'})")
    dst = page.locator('#side .side-item[data-album="al-02"]').bounding_box()
    s = grip.bounding_box()
    page.mouse.move(s["x"] + s["width"] / 2, s["y"] + s["height"] / 2)
    page.mouse.down()
    for k in range(1, 16):
        page.mouse.move(s["x"] + (dst["x"] + dst["width"] / 2 - s["x"]) * k / 15, s["y"] + (dst["y"] + dst["height"] / 2 - s["y"]) * k / 15)
        page.wait_for_timeout(30)
    page.mouse.up()
    page.wait_for_timeout(400)
    assert page.evaluate("App.collection.albums.find(a => a.id === 'al-02').songs.map(s => s.id)")[-1] == "f-000"
    assert album_order(page) == ["al-00", "al-01", "al-02", "al-03"]


def test_c5_juntar(open_app):
    page = open4(open_app)
    page.click('#side .side-item[data-album="al-01"]')   # filtra pelo album, como na lateral
    head_menu(page, "al-01")
    page.click("#am-merge")
    page.select_option("#merge-target", "al-03")
    assert "vão para o fim de «Álbum 4»" in page.text_content("#merge-text")
    page.click("#merge-ok-btn")
    page.wait_for_timeout(200)
    assert album_order(page) == ["al-00", "al-02", "al-03"] and changes(page) == 1
    assert page.evaluate("App.collection.albums[2].songs.map(s => s.id)") == ["f-009", "f-010", "f-011", "f-003", "f-004", "f-005"]
    assert page.evaluate("App.collection.albums[2].title") == "Álbum 4"
    assert page.input_value("#filter-album") == "al-03"
    undo(page)
    assert album_order(page) == ["al-00", "al-01", "al-02", "al-03"] and changes(page) == 0


def test_c6_excluir_album(open_app):
    page = open4(open_app)
    page.click('#main li.row[data-id="f-003"] .row-used')
    head_menu(page, "al-01")
    page.click("#am-delete")
    assert "3 faixas" in page.text_content("#confirm-ok-btn")
    page.click("#confirm-cancel-btn")   # falso positivo: cancelar nao muda nada
    assert album_order(page) == ["al-00", "al-01", "al-02", "al-03"] and changes(page) == 0
    head_menu(page, "al-01")
    page.click("#am-delete")
    page.click("#confirm-ok-btn")
    page.wait_for_timeout(200)
    assert album_order(page) == ["al-00", "al-02", "al-03"] and changes(page) == 1
    assert not page.evaluate("isUsed('f-003')")
    undo(page)
    assert album_order(page) == ["al-00", "al-01", "al-02", "al-03"] and page.evaluate("isUsed('f-003')")


def test_c7_exportar_album_json(open_app):
    page = open4(open_app)
    head_menu(page, "al-02")
    with page.expect_download() as d:
        page.click("#am-json")
    out = json.load(open(d.value.path(), encoding="utf-8"))
    assert d.value.suggested_filename == "al-02.json"
    assert [a["id"] for a in out["albums"]] == ["al-02"] and len(out["albums"][0]["songs"]) == 3
    cited = {m for s in out["albums"][0]["songs"] for m in s.get("styleModules", [])}
    assert {m["id"] for m in out.get("styleModules", [])} == cited
    path = os.path.join(tempfile.mkdtemp(), "al-02.json")
    d.value.save_as(path)
    page.set_input_files("#file-input", path)
    page.wait_for_function("App.source === 'al-02.json'")


def test_c8_celular_folha_do_album(open_app):
    page = open4(open_app, width=390, height=844, mobile=True)
    head_menu(page, "al-00")
    assert page.is_visible("#am-cancel")
    page.click("#am-down")
    page.wait_for_timeout(200)
    assert album_order(page)[:2] == ["al-01", "al-00"]
