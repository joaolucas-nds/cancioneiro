"""Ler, buscar, filtrar, copiar e exportar (fase 2, I1 e I2). Dados: data/demo.json."""
import json
import re

from conftest import DEMO, DEMO_TEXT, changelog_version, import_demo, rows

TITLES = [s["title"] for a in DEMO["albums"] for s in a["songs"]]
IDS = [s["id"] for a in DEMO["albums"] for s in a["songs"]]


def test_versao_na_tela_e_igual_ao_changelog(open_app):
    page = open_app()
    assert page.text_content('[data-role="app-version"]') == "v" + changelog_version()


def test_importar_mostra_lista_e_lateral(open_app):
    page = open_app()
    import_demo(page)
    assert rows(page) == IDS
    side = page.eval_on_selector_all("#side-albums .side-item:not(.side-new)", "e => e.length")
    assert side == len(DEMO["albums"]) + 1  # «Todas as faixas» e os álbuns


def test_busca_filtra_e_limpa(open_app):
    page = open_app()
    import_demo(page)
    alvo = TITLES[1]
    page.fill("#search", alvo)
    page.wait_for_timeout(300)
    assert rows(page) == [IDS[1]]
    page.fill("#search", "")
    page.wait_for_timeout(300)
    assert rows(page) == IDS


def test_detalhe_abre_com_endereco_e_navega(open_app):
    page = open_app()
    import_demo(page)
    page.click(f'#main li.row[data-id="{IDS[0]}"] .row-open')
    assert page.is_visible("#detail")
    assert page.evaluate("location.hash") == "#faixa=" + IDS[0]
    page.click("#detail-next")
    assert page.evaluate("App.detailId") == IDS[1]


def test_copiar_style_da_linha_sem_rotulo(open_app):
    page = open_app()
    import_demo(page)
    song = DEMO["albums"][0]["songs"][0]
    page.click(f'#main li.row[data-id="{song["id"]}"] [data-role="row-style"]')
    page.wait_for_timeout(200)
    got = page.evaluate("navigator.clipboard.readText()")
    assert got.startswith(song["style"].split(",")[0])
    assert not re.search(r"estilo suno|style:|\[letra\]", got, re.I)


def test_usei_sobrevive_a_recarregar(open_app):
    page = open_app()
    import_demo(page)
    page.click(f'#main li.row[data-id="{IDS[0]}"] .row-used')
    page.reload()
    page.evaluate("bootDone")
    assert page.get_attribute(f'#main li.row[data-id="{IDS[0]}"] .row-used', "aria-pressed") == "true"


def test_cartoes_mostram_todas_as_faixas(open_app):
    page = open_app()
    import_demo(page)
    page.click("#view-cards")
    assert page.eval_on_selector_all("#main .card", "e => e.length") == len(IDS)


def test_exportar_md_da_faixa_deixa_rotulo_fora_do_bloco(open_app):
    page = open_app()
    import_demo(page)
    song = DEMO["albums"][0]["songs"][0]
    page.click(f'#main li.row[data-id="{song["id"]}"] .row-more')
    with page.expect_download() as d:
        page.click("#tm-md")
    md = open(d.value.path(), encoding="utf-8").read()
    blocks = re.findall(r"```[^\n]*\n(.*?)```", md, re.S)
    assert any(song["style"].split(",")[0] in b for b in blocks)
    for b in blocks:
        assert not re.search(r"estilo suno|^style:|^lyrics:", b, re.I | re.M), b


def test_baixar_json_sem_chaves_internas(open_app):
    page = open_app()
    import_demo(page)
    page.click("#more-btn")
    with page.expect_download() as d:
        page.click("#download-btn")
    out = json.load(open(d.value.path(), encoding="utf-8"))
    assert out == json.loads(DEMO_TEXT)
