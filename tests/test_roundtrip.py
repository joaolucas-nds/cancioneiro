"""Ida e volta do acervo (i-025): baixar e reimportar devolve o mesmo acervo,
antes e depois de organizar. Acervo sintetico de 205 faixas."""
import json

from conftest import import_demo, make_collection, rows, write_tmp_collection


def download_json(page):
    page.click("#more-btn")
    with page.expect_download() as d:
        page.click("#download-btn")
    return d.value.path()


def test_baixar_e_reimportar_e_identico(open_app):
    coll = make_collection(205)
    path = write_tmp_collection(coll)
    page = open_app()
    import_demo(page, path)
    assert len(rows(page)) == 205
    out = download_json(page)
    assert json.load(open(out, encoding="utf-8")) == coll


def test_organizado_volta_igual_ao_baixado(open_app):
    page = open_app()
    import_demo(page, write_tmp_collection(make_collection(30, 3)))
    page.evaluate("moveSongBy(App.collection.albums[0].songs[0].id, 2)")
    page.wait_for_timeout(150)
    out = download_json(page)
    first = json.load(open(out, encoding="utf-8"))
    page.evaluate("App.changes = 0")  # o baixar zerou; reimportar nao pede confirmacao
    page.set_input_files("#file-input", out)
    page.wait_for_timeout(500)
    assert page.evaluate("App.collection") == first
