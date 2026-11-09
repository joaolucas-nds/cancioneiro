"""Salvar no arquivo (I4, DEC-033; criterios da spec meta/specs/261106-salvar-no-arquivo.md).
As janelas do sistema sao arquivos da pasta privada do navegador (FS_STUB no conftest)."""
import json

from conftest import DEMO_TEXT, changes, import_demo


def opfs_write(page, name, text):
    page.evaluate("""async ([n, t]) => { const d = await navigator.storage.getDirectory();
      const h = await d.getFileHandle(n, { create: true }); const w = await h.createWritable();
      await w.write(t); await w.close(); }""", [name, text])


def opfs_read(page, name):
    return page.evaluate("""async n => { const d = await navigator.storage.getDirectory();
      try { return await (await (await d.getFileHandle(n)).getFile()).text(); } catch (e) { return null; } }""", name)


def record(page, src="demo-acervo.json"):
    return page.evaluate("""async s => { const r = await dbGet(s); return r ? { link: !!r.fileHandle,
      name: r.fileHandle && r.fileHandle.name } : null; }""", src)


def calls(page):
    return page.evaluate("__fs.calls.splice(0)")


def change(page):
    page.evaluate("moveSongBy(App.collection.albums[0].songs[0].id, 1)")
    page.wait_for_timeout(150)


def import_by_picker(page, text=DEMO_TEXT):
    opfs_write(page, "demo-acervo.json", text)
    page.click("#more-btn")
    page.click("#menu-import")
    page.wait_for_function("App.source === 'demo-acervo.json' && App.saved")


def save(page):
    page.click("#draft-save")
    page.wait_for_timeout(300)


def collection_text(page):
    return page.evaluate("JSON.stringify(App.collection, null, 2)") + "\n"


def test_c1_sem_api_baixa_como_antes(open_app):
    page = open_app(fs_api=False)
    import_demo(page)
    change(page)
    assert page.text_content("#draft-save") == "Salvar .json" and page.is_hidden("#save-wrap")
    with page.expect_download() as d:
        page.click("#draft-save")
    assert d.value.suggested_filename == "demo.json"
    page.wait_for_timeout(200)
    assert changes(page) == 0


def test_c1_c5_c3_importar_vincula_e_salvar_grava_sem_janela(open_app):
    page = open_app()
    import_by_picker(page)
    assert record(page) == {"link": True, "name": "demo-acervo.json"}
    change(page)
    assert page.text_content("#draft-save") == "Salvar" and page.is_visible("#save-wrap")
    calls(page)
    save(page)
    assert calls(page) == ["query"] and changes(page) == 0
    assert opfs_read(page, "demo-acervo.json") == collection_text(page)
    assert page.text_content("#draft-text").startswith("✓ Salvo no arquivo às")


def test_c2_sem_vinculo_pede_janela_e_cancelar_nao_grava(open_app):
    page = open_app()
    import_demo(page)  # pelo <input>: sem vinculo
    change(page)
    page.evaluate("__fs.cancel = true")
    calls(page)
    save(page)
    assert calls(page) == ["save:demo.json"] and changes(page) == 1 and record(page, "demo.json")["link"] is False
    page.evaluate("__fs.cancel = false")
    save(page)
    assert changes(page) == 0 and record(page, "demo.json")["link"] is True
    assert opfs_read(page, "demo.json") == collection_text(page)


def test_c4_reabrir_pede_permissao(open_app):
    page = open_app()
    import_by_picker(page)
    page.reload()
    page.evaluate("bootDone")
    assert page.evaluate("App.link && App.link.handle.name") == "demo-acervo.json"
    change(page)
    page.evaluate("__fs.perm = 'prompt'; __fs.req = 'denied'")
    calls(page)
    save(page)
    assert calls(page) == ["query", "request"] and changes(page) == 1
    page.evaluate("__fs.req = 'granted'")
    save(page)
    assert changes(page) == 0


def test_c6_arquivo_mudado_fora_pergunta(open_app):
    page = open_app()
    import_by_picker(page)
    change(page)
    save(page)
    change(page)
    save(page)  # falso positivo: duas gravacoes seguidas pelo app nao perguntam
    assert not page.evaluate("document.getElementById('choice-dialog').open") and changes(page) == 0
    change(page)
    page.wait_for_timeout(1100)
    opfs_write(page, "demo-acervo.json", DEMO_TEXT.replace('"title"', '"title" ', 1))
    page.click("#draft-save")
    page.wait_for_selector("#choice-dialog[open]")
    assert page.eval_on_selector_all("#choice-actions button", "e => e.map(x => x.dataset.value)") == ["cancel", "other", "replace"]
    page.click('#choice-actions [data-value="cancel"]')
    page.wait_for_timeout(200)
    assert changes(page) == 1
    page.click("#draft-save")
    page.wait_for_selector("#choice-dialog[open]")
    page.click('#choice-actions [data-value="replace"]')
    page.wait_for_timeout(300)
    assert changes(page) == 0 and opfs_read(page, "demo-acervo.json") == collection_text(page)


def test_c7_arquivo_sumiu(open_app):
    page = open_app()
    import_by_picker(page)
    change(page)
    page.evaluate("async () => (await navigator.storage.getDirectory()).removeEntry('demo-acervo.json')")
    page.click("#draft-save")
    page.wait_for_selector("#choice-dialog[open]")
    assert "não foi encontrado" in page.text_content("#choice-text")
    page.click('#choice-actions [data-value="cancel"]')
    assert changes(page) == 1


def test_c8_baixar_com_vinculo_nao_zera(open_app):
    page = open_app()
    import_by_picker(page)
    change(page)
    page.click("#draft-more")
    with page.expect_download():
        page.click("#save-download")
    page.wait_for_timeout(200)
    assert changes(page) == 1 and json.loads(opfs_read(page, "demo-acervo.json")) == json.loads(DEMO_TEXT)


def test_c9_ctrl_s_na_busca_salva(open_app):
    page = open_app()
    import_by_picker(page)
    change(page)
    page.focus("#search")
    page.evaluate("__keys = []")
    page.keyboard.press("Control+s")
    page.wait_for_timeout(400)
    assert changes(page) == 0 and page.evaluate("__keys.some(e => e.key === 's' && e.defaultPrevented)")


def test_c10_desfazer_depois_de_salvar(open_app):
    page = open_app()
    import_by_picker(page)
    change(page)
    save(page)
    page.click("body", position={"x": 5, "y": 400})
    page.keyboard.press("Control+z")
    page.wait_for_timeout(200)
    assert changes(page) == 1 and page.text_content("#draft-text") == "1 alteração não salva"


def test_c11_desvincular_e_esquecer(open_app):
    page = open_app()
    import_by_picker(page)
    page.click("#acervo-btn")
    assert "Vinculado a demo-acervo.json" in page.text_content("#link-note")
    page.click("#unlink-btn")
    page.wait_for_timeout(200)
    assert record(page)["link"] is False
    page.evaluate("forgetAcervo('demo-acervo.json')")
    page.wait_for_timeout(200)
    assert record(page) is None


def test_c12_celular_baixa(open_app):
    page = open_app(width=390, height=844, mobile=True)
    import_demo(page)
    change(page)
    assert page.text_content("#draft-save") == "Salvar .json" and page.is_hidden("#save-wrap")
    calls(page)
    with page.expect_download():
        page.click("#draft-save")
    assert calls(page) == []
