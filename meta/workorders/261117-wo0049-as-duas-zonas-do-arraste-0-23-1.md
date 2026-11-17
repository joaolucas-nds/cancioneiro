# WO 0049 — As duas zonas do arraste juntas (0.23.1)

## Cabecalho

> **Tipo:** correcao 0.23.1 — app, dois testes ajustados e meta; a Conversa 2 do log ja gravada pelo chat.
> **Config sugerida:** Sonnet · `/effort low` (aplicacao literal por script; 12 edicoes).
> **Pre-requisito:** commit `c04bd78`, branch `main`, sincronizada com `origin/main`. O `git status --short` mostra exatamente: ` M logs/2026-11-17.md` e `?? meta/workorders/261117-wo0049-as-duas-zonas-do-arraste-0-23-1.md`.
> **Base:** o pedido do dono de 2026-11-17 18:19 (as duas areas tracejadas juntas no arraste, `[relatado pelo dono]`). O chat implementou e mediu num clone (log de 2026-11-17, Conversa 2).
> **Depende de:** `c04bd78` (WO 0048).
>
> | arquivo | partida (sha1) | chegada (sha1) |
> |---|---|---|
> | `app/index.html` | `89cc791dd170b25197d5ebcf7a0bfb3695517f44` | `2566209811cb0221cb469aab91a44360ec958ad3` |
> | `tests/test_varios_json.py` | `aeb5aec4bfe1518c715eb58e63ef202aed7ccc40` | `7d0c3421184e4270d0b7545a84c26a7672e73a98` |
> | `tests/test_lateral_e_menus.py` | `a4444a68f418a5c726668c6e95f2642b3e23d4cc` | `fe6d3f75ce7ede22959ca9b2bf4eb05d8f2e705e` |
> | `README.md` | `97bb0e3aec45c1f4e1eb1f879939c49bf654f450` | `2711344a7960217331a4a3422986947533a9c265` |
> | `meta/CHANGELOG.md` | `1d2deb8b727367d2a8c4dca6e2a9ea9ac290650a` | `e7601c077759375249c8cda4f5bcee3b05389498` |
> | `meta/STATUS.md` | `3fc328fd3ad3093caf7c32a1bb8434e1f431f268` | `564a7caaea217731148a91bf5e8f23ff76167550` |
> | `meta/IDEAS.md` | `57aeff225c9fcb779372a53be44406b2b057db3d` | `cf43bfec59e253910a2b0036c261f1cb4f831ba8` |
> | `logs/2026-11-17.md` | `4675b955849793764b2c2f49087795d981fdf269` | o mesmo (gravado pelo chat; so versionar) |
>
> **Ancora semantica:** se um trecho-ancora nao bater EXATAMENTE, PARE e reporte.
> **Idempotencia:** antes de cada edicao, procure o texto NOVO INTEIRO; se ja estiver la, PULE e diga no relatorio.
> **Ancoras:** linhas inteiras (uma linha ou um bloco de linhas inteiras), cada uma 1 vez no arquivo no momento da edicao, na ordem abaixo. Toda edicao «substitui a ancora inteira».
> **Âncoras lidas em** (lidas pelo chat NESTE turno, de `c04bd78` clonado do GitHub e conferido contra o disco do dono — a lista dos versionados com o mesmo sha1; aplicadas em ordem num clone, por um extrator que le so esta WO, com a chegada medida byte a byte):
> - E01 (`app/index.html`, CSS: as duas zonas do arraste juntas): bloco de 6 linhas, começando por `  /* Sobre a lateral: so ela se destaca, com o proprio aviso; o da pagina some. */`
> - E02 (`app/index.html`, versão 0.23.1): linha `    <span class="version" data-role="app-version">v0.23.0</span>`
> - E03 (`app/index.html`, o aviso da pagina e o da lateral): bloco de 8 linhas, começando por `  const hint = document.querySelector(".drop-hint span"), text = dropHintText(zone, n…`
> - E04 (`tests/test_varios_json.py`, o aviso da lateral e o da propria lateral): linha `    assert page.evaluate(HOVER_JS, ["#side .side-head", 2]) == "Solte aqui: cada arqu…`
> - E05 (`tests/test_lateral_e_menus.py`, W1: as duas zonas juntas, e somem no fim): bloco de 17 linhas, começando por `def test_w1_o_aviso_da_pagina_nao_cobre_a_lateral(open_app):`
> - E06 (`README.md`, estado v0.23.1): linha `> **Estado:** v0.23.0 — ferramenta em uso. Lê, guarda e edita vários acervos (importa…`
> - E07 (`meta/CHANGELOG.md`, entrada [0.23.1]): bloco de 2 linhas, começando por `> Histórico de versões entregues. SemVer + Keep a Changelog. Cresce no topo.`
> - E08 (`meta/STATUS.md`, versão): linha `**Versão atual:** 0.23.0 · **Fase:** 3a, 3a.2, o BPM da 3b, o prompt-modelo e as conv…`
> - E09 (`meta/STATUS.md`, ultima conversa: a 0.23.0 aplicada e a 0.23.1): bloco de 2 linhas, começando por `- **0.23.0 implementada pelo chat num clone** (DEC-041): o aviso do arraste fora da l…`
> - E10 (`meta/STATUS.md`, 92 testes): linha `- **Testes do navegador no CI** (DEC-034): 'tests/' (pytest e Playwright, 91 testes d…`
> - E11 (`meta/STATUS.md`, backlog: conferir a 0.23.1): linha `1. **Conferir a 0.23.0 na tela** (dono): o roteiro do log de 2026-11-17. Depois dela,…`
> - E12 (`meta/IDEAS.md`, i-063 corrigida na 0.23.1): linha `'[relatado pelo dono, 2026-11-17, no roteiro da 0.22.0]' O desenho vermelho do arrast…`
> **Canal dos meta neste ciclo = CODE:** STATUS, DECISIONS, IDEAS e CHANGELOG pelo Code (DEC-010); o log do dia ja esta gravado pelo chat.

---

## 1. Por que

Na 0.23.0, o arraste desenhava so a zona sob o ponteiro: a lateral so aparecia com o arquivo em cima dela, e o aviso da pagina sumia. O dono pediu as duas molduras juntas, cada uma com o seu aviso. O chat implementou num clone de `c04bd78`: 92 testes verdes duas vezes; o teste novo das duas zonas reprova na 0.23.0, e o de «as molduras somem no fim» passa nas duas.

## Edicao 0 — Conferencia de hash e de arvore

```
sha1sum app/index.html tests/test_varios_json.py tests/test_lateral_e_menus.py README.md meta/CHANGELOG.md meta/STATUS.md meta/IDEAS.md logs/2026-11-17.md
GIT_OPTIONAL_LOCKS=0 git status --short
```

Todos batem com **partida** (o log, com a Conversa 2 gravada pelo chat); o `git status` mostra exatamente as duas linhas do Pre-requisito. Qualquer outra coisa: **PARE e reporte**.

## Edicoes E01 a E12

Na ordem. Copie o que esta ENTRE as linhas de quatro crases, sem elas. Aplique por script, extraindo os blocos da WO; grave em UTF-8 com LF.

### E01 — CSS: as duas zonas do arraste juntas

**Arquivo:** `app/index.html`

**Ancora:**

````
  /* Sobre a lateral: so ela se destaca, com o proprio aviso; o da pagina some. */
  body.drop-zone-side .drop-hint { display: none; }
  #side.file-target { position: sticky; }
  #side.file-target::after { content: attr(data-drop-label); position: absolute; left: 8px; right: 8px; bottom: 12px;
    padding: 10px; border-radius: 8px; background: var(--paper); color: var(--ember); border: 2px dashed var(--ember);
    font-family: var(--serif); font-size: 15px; text-align: center; }
````

**Texto novo (substitui a ancora inteira):**

````
  /* 0.23.1 (i-063): as DUAS zonas desenhadas o arraste inteiro, cada uma com o seu
     tracejado e o seu aviso: a lateral (acervo novo) e o resto da tela (importar).
     A que esta sob o ponteiro fica forte; a outra, esmaecida, mas a vista. */
  body.side-drop #side::before { content: ""; position: absolute; inset: 4px; z-index: 49; pointer-events: none;
    border: 3px dashed var(--ember); border-radius: var(--radius); opacity: .55; }
  body.side-drop #side::after { content: attr(data-drop-label); position: absolute; left: 12px; right: 12px; bottom: 16px;
    z-index: 49; pointer-events: none; padding: 10px; border-radius: 8px; background: var(--paper); color: var(--ember);
    font-family: var(--serif); font-size: 15px; text-align: center; box-shadow: 0 0 0 1px var(--line); }
  /* Esmaecida, so a cor do texto: o fundo do aviso fica opaco, para nao misturar com a lista */
  body.side-drop:not(.drop-zone-side) #side::after { color: color-mix(in srgb, var(--ember) 65%, var(--paper)); }
  body.side-drop.drop-zone-side #side::before { opacity: 1; }
  body.drop-zone-side .drop-hint { background: rgba(244, 239, 230, .45); border-color: color-mix(in srgb, var(--ember) 50%, transparent); }
  body.drop-zone-side .drop-hint span { opacity: .6; }
````

### E02 — versão 0.23.1

**Arquivo:** `app/index.html`

**Ancora:**

````
    <span class="version" data-role="app-version">v0.23.0</span>
````

**Texto novo (substitui a ancora inteira):**

````
    <span class="version" data-role="app-version">v0.23.1</span>
````

### E03 — o aviso da pagina e o da lateral

**Arquivo:** `app/index.html`

**Ancora:**

````
  const hint = document.querySelector(".drop-hint span"), text = dropHintText(zone, n);
  if (hint.textContent !== text) hint.textContent = text;
  // 0.23: na lateral, o aviso e dela (o CSS o desenha no pe da lateral)
  if (zone.kind === "side" && zone.el.dataset.dropLabel !== text) zone.el.dataset.dropLabel = text;
});
/** A zona do arraste no <body> (0.23): o CSS decide o que desenhar em cada uma. */
function setDropZone(kind) {
  ["page", "album", "side"].forEach(k => document.body.classList.toggle("drop-zone-" + k, k === kind));
````

**Texto novo (substitui a ancora inteira):**

````
  // 0.23.1: o aviso da pagina e sempre o da pagina (ou o do album); a lateral tem o seu
  const hint = document.querySelector(".drop-hint span"), text = dropHintText(zone.kind === "side" ? { kind: "page" } : zone, n);
  if (hint.textContent !== text) hint.textContent = text;
});
/** A zona do arraste no <body> (0.23): o CSS decide o que desenhar em cada uma. Com
    o arraste em curso e IndexedDB (a lateral e zona), a lateral se desenha sempre
    (`side-drop`, 0.23.1); `null` encerra o arraste. */
function setDropZone(kind) {
  ["page", "album", "side"].forEach(k => document.body.classList.toggle("drop-zone-" + k, k === kind));
  const side = document.getElementById("side");
  document.body.classList.toggle("side-drop", !!kind && !!Store.db && !!side && !side.hidden);
  if (side) side.dataset.dropLabel = dropHintText({ kind: "side" }, 1);
````

### E04 — o aviso da lateral e o da propria lateral

**Arquivo:** `tests/test_varios_json.py`

**Ancora:**

````
    assert page.evaluate(HOVER_JS, ["#side .side-head", 2]) == "Solte aqui: cada arquivo vira um acervo guardado"
````

**Texto novo (substitui a ancora inteira):**

````
    # 0.23.1: sobre a lateral, o aviso dela e o da propria lateral (o da pagina continua o da pagina)
    assert page.evaluate(HOVER_JS, ["#side .side-head", 2]) == "Solte para escolher o que cada um vira"
    assert page.evaluate("getComputedStyle(document.getElementById('side'), '::after').content") \
        == '"Solte aqui: cada arquivo vira um acervo guardado"'
````

### E05 — W1: as duas zonas juntas, e somem no fim

**Arquivo:** `tests/test_lateral_e_menus.py`

**Ancora:**

````
def test_w1_o_aviso_da_pagina_nao_cobre_a_lateral(open_app):
    """W1: com a lateral a vista, o aviso da pagina comeca depois dela; sobre a lateral, o aviso da pagina
    some e a lateral mostra o proprio; sobre um album, o aviso perde o fundo."""
    page = open_app()
    import_demo(page)
    page.evaluate(HOVER_JS, ["#main", 1])
    side_right = page.evaluate("document.getElementById('side').getBoundingClientRect().right")
    hint = page.evaluate("(() => { const r = document.querySelector('.drop-hint').getBoundingClientRect(); return [r.left, r.width]; })()")
    assert hint[0] >= side_right and hint[1] > 0
    page.evaluate(HOVER_JS, ["#side .side-head", 2])
    assert page.evaluate("getComputedStyle(document.querySelector('.drop-hint')).display") == "none"
    label = page.evaluate("getComputedStyle(document.getElementById('side'), '::after').content")
    assert label == '"Solte aqui: cada arquivo vira um acervo guardado"'
    alb = page.evaluate("App.collection.albums[0].id")
    page.evaluate(HOVER_JS, [f'#main section.album[data-album="{alb}"] .album-head', 1])
    assert page.evaluate("getComputedStyle(document.querySelector('.drop-hint')).backgroundColor") == "rgba(0, 0, 0, 0)"
    assert page.evaluate("getComputedStyle(document.getElementById('side'), '::after').content") == "none"
````

**Texto novo (substitui a ancora inteira):**

````
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
````

### E06 — estado v0.23.1

**Arquivo:** `README.md`

**Ancora:**

````
> **Estado:** v0.23.0 — ferramenta em uso. Lê, guarda e edita vários acervos (importa vários `.json` de uma vez), grava direto no arquivo do acervo (Chrome e Edge), copia por campo, troca módulos de estilo, ajusta o BPM, **mede cada prompt contra os limites do Suno**, guarda as **fórmulas de referência** dos guias para copiar inteiras, exporta Markdown, exporta uma faixa como `.json` e **entrega o prompt para chats gerarem canções no esquema**. Publicada no GitHub Pages. Ver `meta/ROADMAP.md`.
````

**Texto novo (substitui a ancora inteira):**

````
> **Estado:** v0.23.1 — ferramenta em uso. Lê, guarda e edita vários acervos (importa vários `.json` de uma vez), grava direto no arquivo do acervo (Chrome e Edge), copia por campo, troca módulos de estilo, ajusta o BPM, **mede cada prompt contra os limites do Suno**, guarda as **fórmulas de referência** dos guias para copiar inteiras, exporta Markdown, exporta uma faixa como `.json` e **entrega o prompt para chats gerarem canções no esquema**. Publicada no GitHub Pages. Ver `meta/ROADMAP.md`.
````

### E07 — entrada [0.23.1]

**Arquivo:** `meta/CHANGELOG.md`

**Ancora:**

````
> Histórico de versões entregues. SemVer + Keep a Changelog. Cresce no topo.

````

**Texto novo (substitui a ancora inteira):**

````
> Histórico de versões entregues. SemVer + Keep a Changelog. Cresce no topo.

---

## [0.23.1] — 2026-11-17

As duas zonas do arraste aparecem juntas (i-063).

### Fixed
- **Durante o arraste, a lateral e o resto da tela se desenham ao mesmo tempo**, cada um com o seu tracejado e o seu aviso: a lateral («Solte aqui: cada arquivo vira um acervo guardado») e o resto («Solte para importar» ou «Solte para escolher o que cada um vira»). A zona sob o ponteiro fica forte; a outra, esmaecida, mas à vista. Na 0.23.0 só a zona sob o ponteiro aparecia, e a lateral só se mostrava quando o arquivo já estava em cima dela `[relatado pelo dono]`.

Os testes do aviso (`tests/test_lateral_e_menus.py`) passam a conferir as duas zonas juntas e que nenhuma fica para trás quando o arraste acaba (92 no total).

````

### E08 — versão

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
**Versão atual:** 0.23.0 · **Fase:** 3a, 3a.2, o BPM da 3b, o prompt-modelo e as conveniências de uso concluídos e conferidos · os álbuns antigos convertidos (i-008, fora do repo) · curadoria no app concluída nas três entregas (DEC-028, DEC-029) · frente de interface concluída e conferida nas quatro entregas (DEC-030 a DEC-033) · organizar os álbuns (0.18.0, DEC-035) conferido · rampa de BPM (0.19.0, DEC-036) conferida · fórmulas de referência (0.20.0, DEC-037) conferidas na tela · importar vários `.json` (0.22.0, DEC-040) conferido na tela · clique direito e lateral em duas áreas (0.23.0, DEC-041) à espera da conferência na tela · a Fase 3 concluída · kit de música lido pelo KCM, à espera da resposta (i-039)
````

**Texto novo (substitui a ancora inteira):**

````
**Versão atual:** 0.23.1 · **Fase:** 3a, 3a.2, o BPM da 3b, o prompt-modelo e as conveniências de uso concluídos e conferidos · os álbuns antigos convertidos (i-008, fora do repo) · curadoria no app concluída nas três entregas (DEC-028, DEC-029) · frente de interface concluída e conferida nas quatro entregas (DEC-030 a DEC-033) · organizar os álbuns (0.18.0, DEC-035) conferido · rampa de BPM (0.19.0, DEC-036) conferida · fórmulas de referência (0.20.0, DEC-037) conferidas na tela · importar vários `.json` (0.22.0, DEC-040) conferido na tela · clique direito e lateral em duas áreas (0.23.0, DEC-041) e as duas zonas do arraste juntas (0.23.1) à espera da conferência na tela · a Fase 3 concluída · kit de música lido pelo KCM, à espera da resposta (i-039)
````

### E09 — ultima conversa: a 0.23.0 aplicada e a 0.23.1

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
- **0.23.0 implementada pelo chat num clone** (DEC-041): o aviso do arraste fora da lateral (i-063), os botões de opção na janela de vários (i-061), o clique direito (i-062) e a lateral em duas áreas (i-064). 91 testes, duas rodadas; os 7 de comportamento novo reprovam na 0.22.0 e os 3 de falso positivo passam nas duas `[medido pelo chat, no clone]`. Falta o CI e a conferência na tela (roteiro no log de 2026-11-17).
- **Este bloco substitui o anterior** (a 0.22.0 no clone). O que ele dizia está em `logs/2026-11-16.md`, Conversa 6.
````

**Texto novo (substitui a ancora inteira):**

````
- **0.23.0 implementada pelo chat num clone** (DEC-041): o aviso do arraste fora da lateral (i-063), os botões de opção na janela de vários (i-061), o clique direito (i-062) e a lateral em duas áreas (i-064). 91 testes, duas rodadas; os 7 de comportamento novo reprovam na 0.22.0 e os 3 de falso positivo passam nas duas `[medido pelo chat, no clone]`. Falta o CI e a conferência na tela (roteiro no log de 2026-11-17).
- **0.23.0 aplicada** (`c04bd78`, CI verde, run `44090505271`, `[medido pelo Code]`). O dono apontou, sem o roteiro, que as duas zonas do arraste deviam aparecer juntas `[relatado pelo dono, 2026-11-17]`; a 0.23.1 corrige (WO 0049). O roteiro da 0.23.0 não foi feito; vale o da 0.23.1, no log de 2026-11-17.
- **Este bloco substitui o anterior** (a 0.22.0 no clone). O que ele dizia está em `logs/2026-11-16.md`, Conversa 6.
````

### E10 — 92 testes

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
- **Testes do navegador no CI** (DEC-034): `tests/` (pytest e Playwright, 91 testes desde a 0.23.0, dados só sintéticos) e `.github/workflows/testes.yml`, que roda o `validate.py` com esquema, os testes dos conversores e o `pytest tests` a cada push na `main`. O resultado é o ✓ ou ✗ no commit e a aba Actions.
````

**Texto novo (substitui a ancora inteira):**

````
- **Testes do navegador no CI** (DEC-034): `tests/` (pytest e Playwright, 92 testes desde a 0.23.1, dados só sintéticos) e `.github/workflows/testes.yml`, que roda o `validate.py` com esquema, os testes dos conversores e o `pytest tests` a cada push na `main`. O resultado é o ✓ ou ✗ no commit e a aba Actions.
````

### E11 — backlog: conferir a 0.23.1

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
1. **Conferir a 0.23.0 na tela** (dono): o roteiro do log de 2026-11-17. Depois dela, o recesso decidido pelo dono.
````

**Texto novo (substitui a ancora inteira):**

````
1. **Conferir a 0.23.1 na tela** (dono): o roteiro do log de 2026-11-17, Conversa 2 (com `Ctrl+F5` antes, para o navegador largar a versão em cache). Depois dela, o recesso decidido pelo dono.
````

### E12 — i-063 corrigida na 0.23.1

**Arquivo:** `meta/IDEAS.md`

**Ancora:**

````
`[relatado pelo dono, 2026-11-17, no roteiro da 0.22.0]` O desenho vermelho do arraste ainda cobria a tela inteira, por cima da lateral, que desde a 0.22.0 é outra zona (acervo novo direto): confuso. Pediu também tirar qualquer outra colisão da função antiga. **Entregue (0.23.0, 2026-11-17):** o aviso da página começa depois da lateral; sobre a lateral, só ela se destaca, com o aviso no pé; sobre um álbum, sem a moldura da página.
````

**Texto novo (substitui a ancora inteira):**

````
`[relatado pelo dono, 2026-11-17, no roteiro da 0.22.0]` O desenho vermelho do arraste ainda cobria a tela inteira, por cima da lateral, que desde a 0.22.0 é outra zona (acervo novo direto): confuso. Pediu também tirar qualquer outra colisão da função antiga. **Entregue (0.23.0, 2026-11-17):** o aviso da página começa depois da lateral; sobre a lateral, só ela se destaca, com o aviso no pé; sobre um álbum, sem a moldura da página. **Corrigido (0.23.1, 2026-11-17)** `[relatado pelo dono]`: o pedido era ver as DUAS zonas ao mesmo tempo, cada uma com o seu tracejado; agora as duas se desenham o arraste inteiro, e a que está sob o ponteiro fica forte.
````

## Depois de aplicar — conferencia antes do commit

| # | Checagem | Comando | Esperado |
|---|---|---|---|
| 1 | Os arquivos sao os previstos | `sha1sum app/index.html tests/test_varios_json.py tests/test_lateral_e_menus.py README.md meta/CHANGELOG.md meta/STATUS.md meta/IDEAS.md logs/2026-11-17.md` | a coluna **chegada** |
| 2 | Versao | `grep -c 'data-role="app-version">v0.23.1<' app/index.html` | `1` |
| 3 | A lateral se desenha no arraste | `grep -c 'body.side-drop #side::before' app/index.html` | `1` |
| 4 | Validacao | `python scripts/validate.py; echo "exit=$?"` | `exit=0`, versao 0.23.1 |
| 5 | Nada alem do previsto | `GIT_OPTIONAL_LOCKS=0 git status --short --untracked-files=all` | os 8 arquivos da tabela e esta WO |
| 6 | Depois do push: o CI | `gh run list --limit 1`, em laco com `gh run view <id> --json status,conclusion` ate `completed` | `success`; se vermelho, o passo e as ultimas 30 linhas de `gh run view <id> --log-failed` |

As checagens 2 a 4 rodaram no clone do chat; no Git Bash, **nao testado**. O chat rodou os 92 testes duas vezes no clone (cerca de 58 s). O pytest local do Code nao roda: o veredito e o CI (checagem 6).
**Esta e qual pergunta?** A 1 responde «esta la?»; a 6, «os testes passam no CI?». Nenhuma responde «funciona na tela?»: isso e o roteiro do dono (log de 2026-11-17, Conversa 2).

## Relatorio de aplicacao

Grave em `../AAMMDD-HHMM-code-cancioneiro-apply-wo0049.txt`, com o carimbo de `date +%y%m%d-%H%M` rodado na hora. Checagem 1 em primeiro lugar e o estado final do CI. **Sem `/wrap` depois desta WO**, e sem secao sua no log, salvo se algo fugir do literal.

## Commit

```
git add app/index.html tests/test_varios_json.py tests/test_lateral_e_menus.py README.md meta/CHANGELOG.md meta/STATUS.md meta/IDEAS.md logs/2026-11-17.md meta/workorders/261117-wo0049-as-duas-zonas-do-arraste-0-23-1.md
```

```
git commit -m "fix: as duas zonas do arraste aparecem juntas (0.23.1)" -m "Durante o arraste, a lateral (acervo novo) e o resto da tela (importar) se desenham ao mesmo tempo, cada uma com o seu tracejado e o seu aviso; a zona sob o ponteiro fica forte. Dois testes ajustados."
```

```
git push
```
