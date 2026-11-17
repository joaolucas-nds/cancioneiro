"""A lateral e os menus (0.23.0): o aviso do arraste fora da lateral (i-063), os botoes de opcao na janela
de varios (i-061), o clique direito que abre o «⋯» (i-062) e a lateral com duas areas que rolam (i-064).
Dados so sinteticos."""
from conftest import import_demo, make_collection, write_tmp_collection

HOVER_JS = """([sel, n]) => {
  const dt = new DataTransfer();
  for (let i = 0; i < n; i++) dt.items.add(new File(['{}'], 'x' + i + '.json', { type: 'application/json' }));
  const el = document.querySelector(sel);
  for (const type of ['dragenter', 'dragover'])
    el.dispatchEvent(new DragEvent(type, { bubbles: true, cancelable: true, dataTransfer: dt }));
}"""
# Clique direito sintetico: devolve se o app tomou o evento (o menu do navegador some).
CTX_JS = """([sel, shift]) => {
  const el = document.querySelector(sel), r = el.getBoundingClientRect();
  const ev = new MouseEvent('contextmenu', { bubbles: true, cancelable: true, button: 2, shiftKey: !!shift,
    clientX: Math.round(r.left + 10), clientY: Math.round(r.top + r.height / 2) });
  el.dispatchEvent(ev);
  return [ev.defaultPrevented, ev.clientX, ev.clientY];
}"""


def ctx(page, sel, shift=False):
    return page.evaluate(CTX_JS, [sel, shift])


def visible_pop(page):
    """Qual menu esta aberto, com o titulo e o canto superior esquerdo."""
    return page.evaluate("""(() => {
      // store-pop nao existe antes da 0.23.0: os falsos positivos rodam nas duas versoes
      const p = ['track-pop', 'album-pop', 'store-pop'].map(k => document.getElementById(k)).find(x => x && !x.hidden);
      if (!p) return null;
      const r = p.getBoundingClientRect();
      return [p.id, p.querySelector('.pop-head').textContent, Math.round(r.left), Math.round(r.top)];
    })()""")


def store(page, n):
    """Guarda n acervos sinteticos no navegador, sem abrir nenhum, e redesenha a lateral."""
    page.evaluate("""async n => {
      for (let i = 0; i < n; i++) {
        const c = JSON.parse(JSON.stringify(App.collection));
        c.title = 'Guardado ' + i;
        await saveAcervo(c, 'g' + String(i).padStart(2, '0') + '.json', null);
      }
      setOrigin();
    }""", n)
    page.wait_for_function("n => document.querySelectorAll('#side-acervos li').length === n + 1", arg=n)


# ---------------------------------------------------------------- i-063: o aviso do arraste
SIDE_LABEL = '"Solte aqui: cada arquivo vira um acervo guardado"'
ZONES_JS = """(() => {
  const h = document.querySelector('.drop-hint'), side = document.getElementById('side');
  return { hint: getComputedStyle(h).display, hintText: h.textContent, hintLeft: h.getBoundingClientRect().left,
           sideRight: side.getBoundingClientRect().right,
           sideFrame: getComputedStyle(side, '::before').borderTopStyle, sideLabel: getComputedStyle(side, '::after').content,
           sideStrong: getComputedStyle(side, '::before').opacity === '1' };
})()"""


def test_w1_as_duas_zonas_aparecem_juntas(open_app):
    """W1 (0.23.1): durante o arraste, as DUAS zonas se desenham, cada uma com o seu tracejado e o seu aviso:
    a pagina (fora da lateral) e a lateral; a que esta sob o ponteiro fica forte."""
    page = open_app()
    import_demo(page)
    page.evaluate(HOVER_JS, ["#main", 1])
    z = page.evaluate(ZONES_JS)
    assert z["hint"] == "flex" and z["hintText"] == "Solte para importar" and z["hintLeft"] >= z["sideRight"]
    assert z["sideFrame"] == "dashed" and z["sideLabel"] == SIDE_LABEL and not z["sideStrong"]
    page.evaluate(HOVER_JS, ["#side .side-head", 2])
    z = page.evaluate(ZONES_JS)
    assert z["hint"] == "flex" and z["hintText"] == "Solte para escolher o que cada um vira"
    assert z["sideFrame"] == "dashed" and z["sideLabel"] == SIDE_LABEL and z["sideStrong"]
    alb = page.evaluate("App.collection.albums[0].id")
    page.evaluate(HOVER_JS, [f'#main section.album[data-album="{alb}"] .album-head', 1])
    assert page.evaluate("getComputedStyle(document.querySelector('.drop-hint')).backgroundColor") == "rgba(0, 0, 0, 0)"
    assert page.evaluate(ZONES_JS)["sideFrame"] == "dashed"


def test_w1_o_arraste_acaba_e_as_zonas_somem(open_app):
    """W1 (0.23.1): ao soltar fora ou sair da janela, nenhuma das duas molduras fica para tras."""
    page = open_app()
    import_demo(page)
    page.evaluate(HOVER_JS, ["#main", 1])
    page.evaluate("""(() => { const dt = new DataTransfer(); dt.items.add(new File(['{}'], 'x.json'));
      document.querySelector('#main').dispatchEvent(new DragEvent('dragleave', { bubbles: true, cancelable: true, dataTransfer: dt })); })()""")
    z = page.evaluate(ZONES_JS)
    assert z["hint"] == "none" and z["sideFrame"] == "none" and z["sideLabel"] == "none"


def test_w1_sem_lateral_o_aviso_cobre_a_tela(open_app):
    """W1 (falso positivo): abaixo de 1280 px nao ha lateral, e o aviso continua ocupando a tela."""
    page = open_app(width=1100)
    import_demo(page)
    page.evaluate(HOVER_JS, ["#main", 1])
    assert page.evaluate("document.querySelector('.drop-hint').getBoundingClientRect().left") == 12


# ---------------------------------------------------------------- i-061: botoes de opcao
def test_w2_botoes_de_opcao_na_janela_de_varios(open_app):
    """W2: cada linha tem tres botoes de opcao (Acervo novo, Faixas no aberto, Pular), um marcado;
    clicar troca a escolha e o destino aparece com «Faixas»."""
    page = open_app()
    import_demo(page)
    paths = [write_tmp_collection(make_collection(2, 1)), write_tmp_collection(make_collection(3, 1))]
    page.set_input_files("#file-input", paths)
    page.wait_for_selector("#multi-dialog[open]")
    labels = page.eval_on_selector_all("#multi-list > li:first-child .seg span", "e => e.map(x => x.textContent)")
    assert labels == ["Acervo novo", "Faixas no aberto", "Pular"]
    assert page.evaluate("document.querySelectorAll('#multi-list select').length") == 0
    assert page.is_hidden("#multi-dest")
    page.click("#multi-list > li:first-child .seg label:has(input[value=tracks])")
    assert page.evaluate("document.querySelector('#multi-list > li:first-child .seg input:checked').value") == "tracks"
    assert page.is_visible("#multi-dest")
    page.click("#multi-list > li:first-child .seg label:has(input[value=skip])")
    assert page.is_hidden("#multi-dest")


# ---------------------------------------------------------------- i-062: clique direito
def test_w3_clique_direito_na_faixa_abre_o_menu_no_ponto(open_app):
    """W3: clique direito numa linha abre o «⋯» da faixa no ponto do clique, e o do navegador nao aparece."""
    page = open_app()
    import_demo(page)
    sid = page.evaluate("App.collection.albums[0].songs[0].id")
    title = page.evaluate("App.collection.albums[0].songs[0].title")
    taken, x, y = ctx(page, f'#main li.row[data-id="{sid}"] .row-open')
    assert taken
    assert visible_pop(page) == ["track-pop", title, x, y]
    page.keyboard.press("Escape")
    assert visible_pop(page) is None


def test_w3_clique_direito_real_no_cartao_e_no_detalhe(open_app):
    """W3: o botao direito de verdade (Playwright) no cartao e no detalhe abre o menu da faixa."""
    page = open_app()
    import_demo(page)
    sid = page.evaluate("App.collection.albums[0].songs[0].id")
    page.click(f'#main li.row[data-id="{sid}"] .row-open')            # o detalhe ao lado
    page.wait_for_selector("#detail:not([hidden])")
    page.click("#detail h2, #detail .card-title, #detail", button="right", position={"x": 40, "y": 60})
    assert visible_pop(page)[0] == "track-pop"
    page.keyboard.press("Escape")
    page.click("#view-cards")
    page.wait_for_selector("#main .card")
    page.click("#main .card", button="right", position={"x": 30, "y": 20})
    assert visible_pop(page)[0] == "track-pop"


def test_w3_clique_direito_no_album_e_no_acervo(open_app):
    """W3: no cabecalho do album e no album da lateral, o «⋯» do album; num acervo da lateral, o menu novo
    do acervo, com «Abrir» so para os que nao estao abertos; «Abrir» abre."""
    page = open_app()
    import_demo(page)
    alb = page.evaluate("App.collection.albums[0]")
    assert ctx(page, f'#main section.album[data-album="{alb["id"]}"] .album-head h2')[0]
    assert visible_pop(page)[:2] == ["album-pop", alb["title"]]
    page.keyboard.press("Escape")
    assert ctx(page, f'#side .side-item[data-album="{alb["id"]}"]')[0]
    assert visible_pop(page)[:2] == ["album-pop", alb["title"]]
    page.keyboard.press("Escape")
    store(page, 1)
    assert ctx(page, '#side-acervos .side-item[data-source="demo.json"]')[0]
    assert visible_pop(page)[0] == "store-pop"
    assert page.is_hidden("#cm-open") and page.is_visible("#cm-forget")
    page.keyboard.press("Escape")
    assert ctx(page, '#side-acervos .side-item[data-source="g00.json"]')[0]
    assert visible_pop(page)[:2] == ["store-pop", "Guardado 0"]
    page.click("#cm-open")
    page.wait_for_function("App.source === 'g00.json'")
    assert visible_pop(page) is None


def test_w3_o_menu_do_navegador_continua_onde_deve(open_app):
    """W3 (falso positivo): com Shift, num campo de texto, com texto selecionado e fora de faixa, album
    ou acervo, o app nao toma o clique direito."""
    page = open_app()
    import_demo(page)
    sid = page.evaluate("App.collection.albums[0].songs[0].id")
    assert ctx(page, f'#main li.row[data-id="{sid}"] .row-open', shift=True)[0] is False
    assert ctx(page, "#search")[0] is False
    assert ctx(page, "#bar")[0] is False
    page.evaluate(f"""(() => {{ const el = document.querySelector('#main li.row[data-id="{sid}"] .row-open');
      const r = document.createRange(); r.selectNodeContents(el);
      const s = getSelection(); s.removeAllRanges(); s.addRange(r); }})()""")
    assert ctx(page, f'#main li.row[data-id="{sid}"] .row-open')[0] is False
    assert visible_pop(page) is None


def test_w3_celular_nao_toma_o_clique_direito(open_app):
    """W3 (falso positivo): no celular o toque longo segue com o navegador (o «⋯» esta a mao)."""
    page = open_app(width=390, height=844, mobile=True)
    import_demo(page)
    sid = page.evaluate("App.collection.albums[0].songs[0].id")
    assert ctx(page, f'#main li.row[data-id="{sid}"] .row-open')[0] is False


# ---------------------------------------------------------------- i-064: a lateral em duas areas
def test_w4_lateral_com_duas_areas_que_rolam(open_app):
    """W4: com muitos albuns e muitos acervos, a lateral nao rola inteira: os albuns rolam na area de cima,
    os acervos na de baixo (com teto menor), e os acervos ficam presos no pe da lateral."""
    page = open_app(height=768)
    import_demo(page, write_tmp_collection(make_collection(40, 40)))
    store(page, 14)
    m = page.evaluate("""(() => {
      const side = document.getElementById('side'), a = document.getElementById('side-albums'),
            c = document.getElementById('side-acervos'), sec = document.querySelector('.side-sec-acervos');
      const sr = side.getBoundingClientRect(), cr = sec.getBoundingClientRect();
      return { sideScrolls: side.scrollHeight > side.clientHeight + 1,
               albumsScroll: a.scrollHeight > a.clientHeight, acervosScroll: c.scrollHeight > c.clientHeight,
               acervosShare: cr.height / sr.height, gapBottom: Math.round(sr.bottom - cr.bottom),
               albumsBigger: a.clientHeight > c.clientHeight };
    })()""")
    assert not m["sideScrolls"] and m["albumsScroll"] and m["acervosScroll"] and m["albumsBigger"]
    assert m["acervosShare"] <= 0.35 and 0 <= m["gapBottom"] <= 14


def test_w4_poucos_albuns_os_acervos_continuam_no_pe(open_app):
    """W4: com poucos albuns e um acervo, nada rola, e os acervos ficam no pe da lateral (nao logo abaixo dos albuns)."""
    page = open_app(height=768)
    import_demo(page)
    m = page.evaluate("""(() => {
      const side = document.getElementById('side'), a = document.getElementById('side-albums'),
            c = document.getElementById('side-acervos'), sec = document.querySelector('.side-sec-acervos');
      return [a.scrollHeight > a.clientHeight, c.scrollHeight > c.clientHeight,
              Math.round(side.getBoundingClientRect().bottom - sec.getBoundingClientRect().bottom)];
    })()""")
    assert m[0] is False and m[1] is False and 0 <= m[2] <= 14
