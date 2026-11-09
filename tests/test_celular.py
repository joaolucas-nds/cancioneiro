"""Celular, 390x844 (I2 e I3): detalhe em tela propria, folha do «⋯», selecionar varias."""
from conftest import DEMO, import_demo

ID0 = DEMO["albums"][0]["songs"][0]["id"]


def test_detalhe_em_tela_propria_e_voltar(open_app):
    page = open_app(width=390, height=844, mobile=True)
    import_demo(page)
    page.click(f'#main li.row[data-id="{ID0}"] .row-open')
    assert page.is_visible("#detail-back")
    page.click("#detail-back")
    assert page.is_visible(f'#main li.row[data-id="{ID0}"]')


def test_selecionar_varias_pelo_menu_do_detalhe(open_app):
    page = open_app(width=390, height=844, mobile=True)
    import_demo(page)
    page.click(f'#main li.row[data-id="{ID0}"] .row-open')
    page.click("#detail-more")
    page.click("#tm-select")
    page.wait_for_timeout(200)
    assert page.evaluate("[...App.selection]") == [ID0]
    assert page.is_visible("#batch")
