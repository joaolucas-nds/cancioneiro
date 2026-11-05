# WO 0025 — Barra unica (frente de interface, I1), DEC-030 e versao 0.14.0

## Cabecalho

> **Tipo:** mista — CODIGO (`app/index.html`) e registro (CHANGELOG, README, DECISIONS, IDEAS, ROADMAP, STATUS inteiro).
> **Config sugerida:** Sonnet · `/effort medium`. 36 edicoes literais e o STATUS inteiro, aplicados e testados pelo chat num clone de `26e7537`; cada arquivo tem hash de chegada.
> **Pre-requisito:** commit `26e7537`, branch `main`, sincronizada com `origin/main`. O `git status` mostra **so** o que o chat gravou: `M logs/2026-11-05.md`, `M meta/CONTEXT.md`, `M meta/specs/261105-barra-unica.md` e esta WO (`?? meta/workorders/...wo0025...`).
> **Base:** spec `meta/specs/261105-barra-unica.md`; analise `meta/analises/261105-ANALISE-frente-de-interface.md`, decidida pelo dono em 2026-11-05 (vira a DEC-030 nesta WO).
> **Depende de:** WO 0024, ja aplicada (`f695f81`, wrap `240612b`).
>
> **Arquivos — partida e chegada, os dois medidos pelo chat** (em LF; chegada = aplicar literalmente as edicoes abaixo):
>
> | arquivo | partida (sha1) | chegada (sha1) |
> |---|---|---|
> | `app/index.html` | `445190eba9c0a4b8b49c8a8ac0262c8767890ab8` | `04f9484721e0aa8ca5b6a5ddfd64652acee94548` |
> | `README.md` | `63289284db96b1a0de0cb7ca58b6981e3c95eca7` | `f047d3dff285aeeb8cbfa351ad3fc1dcd7fcce3d` |
> | `meta/CHANGELOG.md` | `1b1fef576220d70354fcc01f3c2592efc3b161a0` | `957d0d54f71a55629d41fd97dca862325e54fcbd` |
> | `meta/DECISIONS.md` | `89d1a07c5f64f58ca6cd05d2b57518de353b3d31` | `be49dcecfcdf85c87a2cbbefd3dae5cc9cb57fff` |
> | `meta/IDEAS.md` | `fec7015b5d57328b4f73b04229ae185e9a02dcfb` | `e5504c028eaabbdb2893fd52eb189c76735ffcc8` |
> | `meta/ROADMAP.md` | `bad164421321dc3d6d629165fce209420bb519ca` | `0d097d6a07184c1cabe1bdc9cc21994054e42c6d` |
> | `meta/STATUS.md` | `e0cf0672ca3112f9085d893957280277a6494bb1` | `12275f2ad23e4d62f5cd71eb28299dfac7851e3a` |
> | `meta/specs/261105-barra-unica.md` | `4a90758e120aa5f6851bb9d5a405b904cf8a67f2` | `4a90758e120aa5f6851bb9d5a405b904cf8a67f2` (gravado pelo chat; só versiona) |
> | `meta/CONTEXT.md` | `8e6e6a4b1d1ae5407de87451381bc2f5069633f9` | `8e6e6a4b1d1ae5407de87451381bc2f5069633f9` (gravado pelo chat; só versiona) |
> | `logs/2026-11-05.md` | `de4aa381e11e53dd3d41ec933120bdd1c1b41bf7` | `de4aa381e11e53dd3d41ec933120bdd1c1b41bf7` (gravado pelo chat; só versiona) |
>
> **Ancora semantica:** se um trecho-ancora nao bater EXATAMENTE, PARE e reporte.
> **Idempotencia:** antes de cada edicao, procure o texto NOVO INTEIRO; se ja estiver la, PULE e diga no relatorio. Arquivo inteiro (E37): se o hash ja for o de chegada, PULE.
> **Ancoras lidas em:** cada ancora foi recortada pelo chat do arquivo de partida (`git show 26e7537:<arquivo>`; os tres do chat, depois de gravados) e conferida como ocorrendo **exatamente 1 vez** no estado em que a edicao e aplicada, na ordem abaixo. Ancora sempre de linha inteira. As edicoes que **removem** um trecho levam junto a linha anterior e a seguinte (ou as seguintes, ate uma com texto), que aparecem iguais no texto novo: assim o bloco novo nao fica vazio, e so existe depois da remocao.
> **Canal dos meta neste ciclo = CODE:** esta WO e o registro. A spec, o CONTEXT e o log ja estao gravados pelo chat (DEC-010); a WO so os versiona.

---

## 1. Por que

Primeira entrega da frente de interface (i-044 a i-048), pela spec da I1:

- **Barra unica**, fixa, de 48 px (no celular, 51), no lugar do cabecalho, da barra de filtros e da linha de origem: nome e versao, **seletor de acervo** (menu com os guardados, importar, esquecer, origem), **busca** com a tecla `/`, **Filtros** num painel, o **rascunho** com «Salvar .json», **editar** (ate a I3) e o **«⋯»** com os seis botoes do antigo cabecalho.
- **Etiquetas de filtro** removiveis, com «N de M faixas» e «Limpar tudo»; a regra `[hidden]` vale para o app todo (i-044).
- **Celular:** botoes de 44 px, a busca numa linha propria, o rascunho no pe; o topo passou de 469 px de controles para 95.
- **O cartao nao muda.** **DEC-030** registra a frente inteira: B, SortableJS 1.15.7 embutido, sem o interruptor «editar», I1 → I2 → I3 → I4.

O app de chegada foi executado pelo chat no Chromium headless (`file://`): **14 de 14** conferencias dos 13 criterios; os testes das entregas 1 a 3 seguem em **15 de 15**, **25 de 25** e **19 de 19** (com os seletores dos botoes que mudaram de lugar); prova de vida no app de partida (reprova). `validate.py` exit=0 (com `jsonschema`, `Tudo conforme ao esquema.`), `test_convert_br.py` e `test_convert_guides.py` OK. O chat tambem olhou a tela (capturas a 1366×720 e 390×844) e corrigiu o que so ela mostrava.

**Versao 0.14.0 nesta WO.** A conferencia de tela e do dono, depois do push.

## Edicao 0 — Conferencia de hash e de arvore

```
sha1sum app/index.html README.md meta/CHANGELOG.md meta/DECISIONS.md meta/IDEAS.md meta/ROADMAP.md meta/STATUS.md meta/specs/261105-barra-unica.md meta/CONTEXT.md logs/2026-11-05.md
GIT_OPTIONAL_LOCKS=0 git status --short
```

Os dez batem com a coluna **partida**; o `git status` mostra exatamente as quatro linhas do Pre-requisito. Qualquer outra coisa: **PARE e reporte**.

## Edicoes E01 a E37

Na ordem. **Todas as secoes de edicao tem o mesmo titulo, `### Exx — ...`**, inclusive a de arquivo inteiro.
Copie o que esta ENTRE as linhas de quatro crases, sem elas. **O bloco termina na linha de quatro crases, nunca
num titulo:** o CHANGELOG, a DECISIONS, a IDEAS e o STATUS trazem `## ` e `### ` dentro do bloco.

### E01 — app: o CSS do cabecalho vira o da barra unica — `app/index.html`

**Ancora, literal:**

````
  /* ---- Cabecalho ---- */
  header {
    padding: 20px 24px; border-bottom: 1px solid var(--line);
    display: flex; flex-wrap: wrap; align-items: center; gap: 16px;
    position: sticky; top: 0; background: var(--paper); z-index: 10;
  }
  /* Nome com a versao pequena embaixo; ao lado, as ferramentas (prompt, exemplo,
     estrutura); na direita, o que mexe no arquivo (importar, baixar, exportar). */
  .brand { display: flex; flex-direction: column; gap: 2px; }
  .brand h1 {
    font-family: var(--serif); font-weight: 600; font-size: 26px;
    margin: 0; letter-spacing: -0.01em; line-height: 1;
  }
  .brand .version { color: var(--ink-soft); font-size: 11px; }
  .tools { display: flex; gap: 8px; flex-wrap: wrap; }
  .actions { display: flex; gap: 8px; flex-wrap: wrap; margin-left: auto; }
  .ico { display: inline-flex; align-items: center; gap: 6px; }
  .ico svg { width: 14px; height: 14px; flex: none; }
  @media (max-width: 600px) { .actions { margin-left: 0; } }
````

**Texto novo, literal:**

````
  /* ---- Barra unica (I1, DEC-030) ----
     Uma linha fixa: nome, seletor de acervo, busca, filtros, rascunho, editar
     e «⋯». A fileira de etiquetas (filtros aplicados) e o aviso de primeira
     abertura moram juntos dela, dentro de .top, que e o que fica fixo. */
  [hidden] { display: none !important; }   /* i-044: o que tem hidden some de fato */
  .top { position: sticky; top: 0; z-index: 10; background: var(--paper); }
  .bar {
    height: 48px; box-sizing: border-box; padding: 0 14px; border-bottom: 1px solid var(--line);
    display: flex; flex-wrap: nowrap; align-items: center; gap: 8px; background: var(--paper);
  }
  .bar button { height: 32px; padding: 0 10px; }
  .brand { display: flex; align-items: baseline; gap: 6px; flex-shrink: 0; margin-right: 2px; }
  .brand h1 {
    font-family: var(--serif); font-weight: 600; font-size: 19px;
    margin: 0; letter-spacing: -0.01em; line-height: 1;
  }
  .brand .version { color: var(--ink-soft); font-size: 11px; }
  .ico { display: inline-flex; align-items: center; gap: 6px; }
  .ico svg, .icon-btn svg, .search-wrap svg { width: 14px; height: 14px; flex: none;
    fill: none; stroke: currentColor; stroke-width: 1.6; stroke-linecap: round; }
  .pop-wrap { position: relative; flex-shrink: 0; min-width: 0; }
  /* O seletor encolhe antes da busca; sem min-width:0 o botao vaza por cima dela. */
  #acervo-wrap { flex: 0 1 auto; max-width: 420px; }
  .acervo-btn { display: inline-flex; align-items: center; gap: 8px; max-width: 100%; min-width: 0; overflow: hidden; }
  /* O nome do acervo encolhe por ultimo; o arquivo e a contagem cedem antes. */
  .acervo-title { font-weight: 600; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; flex: 0 1 auto; max-width: 220px; }
  .acervo-sub { flex: 1 1 0; }
  .acervo-sub { color: var(--ink-soft); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-width: 0; }
  .chev { width: 12px; height: 12px; flex: none; fill: none; stroke: currentColor; stroke-width: 1.5; stroke-linecap: round; }
  .search-wrap {
    flex: 1 1 460px; max-width: 460px; min-width: 160px; height: 32px; box-sizing: border-box;
    display: flex; align-items: center; gap: 8px; padding: 0 10px;
    border: 1px solid var(--line); border-radius: 8px; background: var(--paper);
  }
  /* Mais especifico que o input[type="search"] geral, que vem depois no arquivo. */
  .search-wrap input[type="search"] { border: 0; border-radius: 0; height: 100%; outline: 0; padding: 0; background: transparent; flex: 1; min-width: 0; }
  .search-wrap:focus-within { outline: 2px solid var(--ember); outline-offset: 1px; }
  .search-wrap kbd { font: 11px var(--sans); color: var(--ink-soft); border: 1px solid var(--line); border-radius: 4px; padding: 0 5px; }
  /* .count-badge, nao .badge: .badge ja e a etiqueta de estado do cartao. */
  .count-badge { background: var(--ember); color: #fff; border-radius: 9px; padding: 0 6px; font-size: 11px; line-height: 16px; }
  .bar-space { flex: 1 1 0; min-width: 0; }
  .bar-draft { display: flex; align-items: center; gap: 8px; height: 32px; padding: 0 4px 0 10px;
    border-radius: 8px; background: var(--ember-soft); flex-shrink: 0; white-space: nowrap; }
  .bar-draft .dot { width: 8px; height: 8px; border-radius: 4px; background: var(--ember); }
  .bar-draft button { height: 26px; }
  .bar-edit { display: flex; gap: 6px; flex-shrink: 0; }
  .icon-btn { width: 32px; padding: 0 !important; display: inline-flex; align-items: center; justify-content: center; font-size: 16px; }
  .mobile-only { display: none; }
  .pop {
    position: absolute; top: calc(100% + 6px); left: 0; z-index: 20; min-width: 220px; max-width: 440px;
    background: var(--paper); border: 1px solid var(--line); border-radius: 10px;
    box-shadow: 0 12px 32px rgba(35,32,27,.18); padding: 6px; display: flex; flex-direction: column;
  }
  .pop-right { left: auto; right: 0; }
  .pop [role="menuitem"] { text-align: left; border: 0; background: transparent; height: auto; padding: 9px 10px; border-radius: 8px; }
  .pop [role="menuitem"]:hover, .pop [role="menuitem"]:focus-visible { background: var(--paper-2); color: var(--ink); }
  .pop .danger { color: var(--ember); }
  .pop-head { font-size: 11px; letter-spacing: .06em; text-transform: uppercase; color: var(--ink-soft); padding: 6px 10px; }
  .pop-sep { border-top: 1px solid var(--line); margin: 6px 0; }
  .pop-note { margin: 0; padding: 4px 10px; font-size: 12px; color: var(--ink-soft); }
  #acervo-pop { width: 440px; }
  #filters-pop { width: 280px; padding: 12px; gap: 4px; }
  #filters-pop label { color: var(--ink-soft); font-size: 12px; margin-top: 6px; }
  #filters-pop select { width: 100%; }
  .pop-actions { display: flex; justify-content: space-between; align-items: center; margin-top: 10px; }
  .link { border: 0 !important; background: transparent !important; color: var(--ember); padding: 0 4px; height: auto; }
  .btn-dark { background: var(--ink); color: var(--paper); border-color: var(--ink); }
  .btn-dark:hover { color: var(--paper); filter: brightness(1.2); }
  .chips { height: 36px; box-sizing: border-box; display: flex; align-items: center; gap: 8px; padding: 0 14px;
    border-bottom: 1px solid var(--line); font-size: 13px; white-space: nowrap; overflow-x: auto; }
  .chips-count { color: var(--ink-soft); }
  .chips-list { display: flex; gap: 8px; }
  .fchip { display: inline-flex; align-items: center; gap: 4px; height: 24px; padding: 0 2px 0 10px;
    border-radius: 12px; background: var(--paper-2); border: 1px solid var(--line); }
  .fchip .k { color: var(--ink-soft); }
  .fchip button { border: 0; background: transparent; padding: 0 6px; height: 22px; color: var(--ink-soft); font-size: 14px; }
  .tour { display: flex; align-items: center; gap: 8px; padding: 6px 14px; font-size: 12px;
    background: var(--ember-soft); border-bottom: 1px solid var(--line); }
  @media (max-width: 1279px) { .acervo-source { display: none; } }
  @media (max-width: 1150px) { #draft-text { display: none; } }
  /* Celular: uma linha de 52 px; busca e editar saem da linha; rascunho vai ao pe. */
  @media (max-width: 719px) {
    .bar { height: auto; min-height: 51px; padding: 3px 4px 3px 6px; gap: 2px; flex-wrap: wrap; }
    .bar button { height: 44px; }
    .brand, .bar-space, .bar-edit, .search-wrap kbd, .btn-label { display: none; }
    #acervo-wrap { flex: 1 1 0; max-width: none; }
    .acervo-btn { max-width: none; width: 100%; border-color: transparent; background: transparent; }
    .acervo-sub { font-size: 12px; }
    .icon-btn, #filters-btn { width: 44px; padding: 0 !important; justify-content: center; border-color: transparent; background: transparent; }
    #filters-btn { position: relative; }
    #filters-btn .count-badge { position: absolute; top: 3px; right: 1px; padding: 0 5px; }
    .mobile-only { display: inline-flex; }
    .pop .mobile-only { display: block; }
    .search-wrap { display: none; }
    .top.search-open .search-wrap { display: flex; order: 99; flex: 1 1 100%; max-width: none; height: 44px; margin: 4px 6px; }
    .pop { position: fixed; left: 8px; right: 8px; top: 56px; max-width: none; width: auto !important; }
    .chips { height: 44px; padding: 0 12px; }
    .bar-draft { position: fixed; left: 12px; right: 12px; bottom: 16px; height: auto; padding: 8px 8px 8px 14px; z-index: 15;
      background: var(--ink); color: var(--paper); border-radius: 12px; }
    .bar-draft #draft-text { display: inline; flex: 1; }
    .bar-draft button { height: 40px; }
    body.has-draft main { padding-bottom: 88px; }
    body.has-draft .toast { bottom: 84px; }
  }
````

### E02 — app: sai o CSS da barra de controles — `app/index.html`

**Ancora, literal:**

````
  .btn-primary:hover { filter: brightness(1.08); color: #fff; }

  /* ---- Barra de controles ---- */
  .controls {
    padding: 14px 24px; border-bottom: 1px solid var(--line);
    display: flex; gap: 14px; flex-wrap: wrap; align-items: center;
    font-size: 13px;
  }
  .controls label { color: var(--ink-soft); margin-right: 4px; }
  select, input[type="search"] {
````

**Texto novo, literal:**

````
  .btn-primary:hover { filter: brightness(1.08); color: #fff; }

  select, input[type="search"] {
````

### E03 — app: a busca encolhe dentro da barra — `app/index.html`

**Ancora, literal:**

````
  input[type="search"] { min-width: 200px; }
````

**Texto novo, literal:**

````
  input[type="search"] { min-width: 0; }
````

### E04 — app: a origem vai para o menu do acervo — `app/index.html`

**Ancora, literal:**

````
  /* Origem do acervo (DEC-022): de onde veio o que esta na tela */
  .origin { font-size: 12px; color: var(--ink-soft); display: flex; gap: 8px; align-items: center; }
  .origin button { font-size: 12px; padding: 3px 8px; }
````

**Texto novo, literal:**

````
  /* Origem do acervo (DEC-022): de onde veio o que esta na tela. Na I1, mora no
     pe do menu do seletor de acervo (#origin, .pop-note). */
````

### E05 — app: a lista de acervos vira menu — `app/index.html`

**Ancora, literal:**

````
  /* Janela «acervos» (DEC-028): um acervo guardado por linha. */
  .acervos-list { list-style: none; padding: 0; margin: 8px 0 0; display: flex; flex-direction: column; gap: 6px; }
  .acervos-list li { display: flex; gap: 10px; align-items: center; padding: 8px 10px;
    background: var(--paper-2); border-radius: 6px; font-size: 13px; }
````

**Texto novo, literal:**

````
  /* Lista de acervos (DEC-028), no menu do seletor de acervo (I1). */
  .acervos-list { list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 2px; max-height: 50vh; overflow: auto; }
  .acervos-list li { display: flex; gap: 10px; align-items: center; padding: 8px 10px;
    border-radius: 8px; font-size: 13px; }
  .acervos-list li.is-open { background: var(--paper-2); }
  .acervos-list .acervo-actions button { height: 28px; padding: 0 8px; }
````

### E06 — app: o editar ligado, fora da linha de origem — `app/index.html`

**Ancora, literal:**

````
  .origin [data-role="edit-btn"][aria-pressed="true"] { background: var(--ink); color: var(--paper); border-color: var(--ink); }
````

**Texto novo, literal:**

````
  [data-role="edit-btn"][aria-pressed="true"] { background: var(--ink); color: var(--paper); border-color: var(--ink); }
````

### E07 — app: sai o estilo da marca antiga — `app/index.html`

**Ancora, literal:**

````
  [data-role="edit-btn"][aria-pressed="true"] { background: var(--ink); color: var(--paper); border-color: var(--ink); }
  .origin .dirty { color: var(--ember); font-weight: 600; }
  .import-list { list-style: none; padding: 0; margin: 8px 0 12px; max-height: 45vh; overflow: auto;
````

**Texto novo, literal:**

````
  [data-role="edit-btn"][aria-pressed="true"] { background: var(--ink); color: var(--paper); border-color: var(--ink); }
  .import-list { list-style: none; padding: 0; margin: 8px 0 12px; max-height: 45vh; overflow: auto;
````

### E08 — app: o cabecalho e a barra de filtros viram a barra unica — `app/index.html`

**Ancora, literal:**

````
<header>
  <div class="brand">
    <h1>Cancioneiro</h1>
    <!-- Versao: a mesma do topo do meta/CHANGELOG.md. O scripts/validate.py confere
         que app, CHANGELOG, README e STATUS dizem a mesma (i-027). -->
    <span class="version" data-role="app-version">v0.13.0</span>
  </div>
  <div class="tools">
    <button id="prompt-btn" title="Copiar o prompt-modelo, com o seu pedido, para um chat">Prompt</button>
    <button id="example-btn" class="ico" title="Baixar um acervo de exemplo (.json)"><svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M8 2v8M4.5 7 8 10.5 11.5 7M3 13.5h10"/></svg>Exemplo</button>
    <button id="layout-btn" class="ico" title="Estrutura do cartão: ordem e blocos visíveis"><svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" aria-hidden="true"><path d="M3 4h10M3 8h10M3 12h10"/></svg>Estrutura</button>
  </div>
  <div class="actions">
    <button id="import-btn">Importar .json</button>
    <button id="download-btn">Baixar .json</button>
    <button id="export-md-btn">Exportar .md</button>
    <input type="file" id="file-input" accept=".json,application/json" hidden>
  </div>
</header>

<div class="controls" id="controls" hidden>
  <div><label for="filter-album">Álbum</label>
    <select id="filter-album"><option value="">todos</option></select></div>
  <div><label for="filter-state">Estado</label>
    <select id="filter-state">
      <option value="">todos</option>
      <option value="ideia">ideia</option>
      <option value="gerada">gerada</option>
      <option value="editada">editada</option>
      <option value="loop-pronto">loop-pronto</option>
      <option value="aprovada">aprovada</option>
    </select></div>
  <div><label for="filter-used">Uso</label>
    <select id="filter-used">
      <option value="">todos</option>
      <option value="used">só usados</option>
      <option value="unused">só não usados</option>
    </select></div>
  <input type="search" id="search" placeholder="buscar título, estilo, tag…">
  <span class="note" id="stats"></span>
  <span class="origin" id="origin"></span>
</div>
````

**Texto novo, literal:**

````
<!-- Barra unica (I1, DEC-030 — spec meta/specs/261105-barra-unica.md): o topo
     inteiro numa linha fixa. Os botoes que eram do cabecalho moram no «⋯» com
     os MESMOS ids, entao os ouvintes de sempre continuam valendo. -->
<div class="top" id="top">
<header class="bar" id="bar">
  <div class="brand">
    <h1>Cancioneiro</h1>
    <!-- Versao: a mesma do topo do meta/CHANGELOG.md. O scripts/validate.py confere
         que app, CHANGELOG, README e STATUS dizem a mesma (i-027). -->
    <span class="version" data-role="app-version">v0.14.0</span>
  </div>
  <div class="pop-wrap" id="acervo-wrap">
    <button type="button" id="acervo-btn" class="acervo-btn" aria-haspopup="menu" aria-expanded="false" aria-controls="acervo-pop" title="Os acervos guardados neste navegador">
      <span class="acervo-title" id="acervo-title">Abrir um acervo</span>
      <span class="acervo-sub"><span class="acervo-source" id="acervo-source"></span><span id="stats"></span></span>
      <svg class="chev" viewBox="0 0 12 12" aria-hidden="true"><path d="M3 4.5 6 7.5 9 4.5"/></svg>
    </button>
    <div class="pop" id="acervo-pop" role="menu" aria-label="Acervos" hidden>
      <div class="pop-head">Neste navegador</div>
      <ul class="acervos-list" id="acervos-list"></ul>
      <div class="pop-sep"></div>
      <button type="button" role="menuitem" id="import-btn">Importar outro .json…</button>
      <button type="button" role="menuitem" id="forget-btn" class="danger" hidden>Esquecer este acervo</button>
      <p class="pop-note" id="origin"></p>
      <p class="pop-note" id="acervos-persist"></p>
    </div>
  </div>
  <label class="search-wrap" id="search-wrap">
    <svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="7" cy="7" r="4.5"/><path d="M10.5 10.5 14 14"/></svg>
    <input type="search" id="search" placeholder="Buscar título, estilo, tag…" aria-label="Buscar">
    <kbd aria-hidden="true">/</kbd>
  </label>
  <button type="button" class="icon-btn mobile-only" id="search-toggle" aria-label="Buscar" aria-expanded="false" aria-controls="search-wrap"><svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="7" cy="7" r="4.5"/><path d="M10.5 10.5 14 14"/></svg></button>
  <div class="pop-wrap">
    <button type="button" id="filters-btn" class="ico" aria-haspopup="dialog" aria-expanded="false" aria-controls="filters-pop"><svg viewBox="0 0 16 16" aria-hidden="true"><path d="M2 4h12M4.5 8h7M7 12h2"/></svg><span class="btn-label">Filtros</span><span class="count-badge" id="filters-count" hidden></span></button>
    <div class="pop" id="filters-pop" role="dialog" aria-label="Filtros" hidden>
      <label for="filter-album">Álbum</label>
      <select id="filter-album"><option value="">todos</option></select>
      <label for="filter-state">Estado</label>
      <select id="filter-state">
        <option value="">todos</option>
        <option value="ideia">ideia</option>
        <option value="gerada">gerada</option>
        <option value="editada">editada</option>
        <option value="loop-pronto">loop-pronto</option>
        <option value="aprovada">aprovada</option>
      </select>
      <label for="filter-used">Uso</label>
      <select id="filter-used">
        <option value="">todos</option>
        <option value="used">só usados</option>
        <option value="unused">só não usados</option>
      </select>
      <div class="pop-actions">
        <button type="button" class="link" id="filters-clear">Limpar tudo</button>
        <button type="button" class="btn-dark" id="filters-done">Pronto</button>
      </div>
    </div>
  </div>
  <div class="bar-space"></div>
  <div class="bar-draft" id="bar-draft" hidden>
    <span class="dot" aria-hidden="true"></span>
    <span id="draft-text" data-role="dirty"></span>
    <button type="button" class="btn-primary" id="draft-save" data-role="dirty-download" title="Baixa o acervo com as alterações, com o nome do arquivo de origem.">Salvar .json</button>
  </div>
  <div class="bar-edit" id="bar-edit"></div>
  <div class="pop-wrap">
    <button type="button" class="icon-btn" id="more-btn" aria-label="Mais ações" aria-haspopup="menu" aria-expanded="false" aria-controls="more-pop">⋯</button>
    <div class="pop pop-right" id="more-pop" role="menu" aria-label="Mais ações" hidden>
      <div class="pop-head mobile-only" id="more-brand">Cancioneiro</div>
      <button type="button" role="menuitem" id="menu-import">Importar .json…</button>
      <button type="button" role="menuitem" id="download-btn">Baixar .json</button>
      <button type="button" role="menuitem" id="export-md-btn">Exportar .md</button>
      <div class="pop-sep"></div>
      <button type="button" role="menuitem" id="prompt-btn" title="Copiar o prompt-modelo, com o seu pedido, para um chat">Prompt para chats</button>
      <button type="button" role="menuitem" id="example-btn" title="Baixar um acervo de exemplo (.json)">Baixar exemplo</button>
      <div class="pop-sep"></div>
      <button type="button" role="menuitem" id="layout-btn" title="Estrutura do cartão: ordem e blocos visíveis">Estrutura do cartão</button>
      <button type="button" role="menuitem" class="mobile-only" id="menu-edit" hidden>Ligar editar</button>
      <button type="button" role="menuitem" class="mobile-only" id="menu-import-tracks" hidden>Importar faixas…</button>
    </div>
  </div>
  <input type="file" id="file-input" accept=".json,application/json" hidden>
</header>
<div class="chips" id="chips" hidden>
  <span class="chips-count" id="chips-count"></span>
  <span class="chips-list" id="chips-list"></span>
  <button type="button" class="link" id="chips-clear">Limpar tudo</button>
</div>
<div class="tour" id="tour" role="status" hidden>Prompt, Exemplo, Importar, Baixar e Exportar agora ficam em <b>⋯</b>, no canto direito da barra. <button type="button" class="link" id="tour-ok">entendi</button></div>
</div>
````

### E09 — app: o estado vazio aponta para o seletor — `app/index.html`

**Ancora, literal:**

````
    <p>Clique em <strong>Importar .json</strong> ou <strong>arraste o arquivo para esta tela</strong><br>
    (ex.: <code>data/demo.json</code>). O último acervo importado fica guardado neste navegador.</p>
````

**Texto novo, literal:**

````
    <p>Clique em <strong>Abrir um acervo</strong>, no topo, ou <strong>arraste o arquivo para esta tela</strong><br>
    (ex.: <code>data/demo.json</code>). Cada acervo importado fica guardado neste navegador.</p>
````

### E10 — app: sai a janela de acervos (o menu faz o mesmo) — `app/index.html`

**Ancora, literal:**

````
    <button type="button" id="layout-close-btn" class="spacer">Fechar</button>
  </div>
</dialog>

<dialog class="prompt-dialog" id="acervos-dialog" aria-labelledby="acervos-dialog-title">
  <h2 id="acervos-dialog-title">Acervos neste navegador</h2>
  <p>Cada arquivo importado fica guardado aqui, pelo nome. Importar de novo o mesmo arquivo substitui a cópia.
  O arquivo no seu computador continua sendo a fonte; esquecer não o toca.</p>
  <ul class="acervos-list" id="acervos-list"></ul>
  <p id="acervos-persist"></p>
  <div class="dialog-actions">
    <button type="button" id="acervos-close-btn" class="spacer">Fechar</button>
  </div>
</dialog>

<dialog class="prompt-dialog" id="confirm-dialog" aria-labelledby="confirm-text">
````

**Texto novo, literal:**

````
    <button type="button" id="layout-close-btn" class="spacer">Fechar</button>
  </div>
</dialog>

<dialog class="prompt-dialog" id="confirm-dialog" aria-labelledby="confirm-text">
````

### E11 — app: render sem a barra de controles — `app/index.html`

**Ancora, literal:**

````
  const controls = document.getElementById("controls");
  if (!App.collection) { controls.hidden = true; return; }
  controls.hidden = false;
````

**Texto novo, literal:**

````
  if (!App.collection) { document.getElementById("chips").hidden = true; updateBar(); return; }
````

### E12 — app: o total no seletor e o N de M nas etiquetas — `app/index.html`

**Ancora, literal:**

````
  document.getElementById("stats").textContent =
    App.collection.title + " · " + shown + "/" + total + " faixas";
````

**Texto novo, literal:**

````
  // I1 (DEC-030): o total vai no seletor de acervo; o «N de M», na fileira de etiquetas.
  // O total e o do acervo inteiro: `total` acima conta so os albuns que passam no filtro.
  const all = (App.collection.albums || []).reduce((n, a) => n + (a.songs || []).length, 0);
  document.getElementById("stats").textContent = nPlural(all, "faixa", "faixas");
  renderChips(f, shown, all);
  updateBar();
````

### E13 — app: setOrigin guarda o texto e redesenha a barra — `app/index.html`

**Ancora, literal:**

````
/** A linha de origem na barra de controles, redesenhada a partir do estado.
    Chamada com texto, guarda o texto; sem argumentos, so redesenha (curadoria).
    Ordem: o texto · a marca de rascunho com «Baixar .json» · «editar» ·
    «importar faixas…» (no modo editar) · «acervos (N)» · «esquecer». */
function setOrigin(text, forgettable) {
  if (text !== undefined) { App.originText = text; App.originForget = !!forgettable; }
  const el = document.getElementById("origin");
  el.textContent = "";
  if (!App.originText) return;
  const btn = (label, role, title, fn) => {
    const b = document.createElement("button"); b.type = "button"; b.textContent = label;
    if (role) b.dataset.role = role;
    b.title = title; b.addEventListener("click", fn); el.appendChild(b); return b;
  };
  const t = document.createElement("span"); t.textContent = "Acervo " + App.originText; el.appendChild(t);
  if (App.saved && App.changes > 0) {
    const d = document.createElement("span"); d.className = "dirty"; d.dataset.role = "dirty";
    d.textContent = "alterado: " + nPlural(App.changes, "alteração não baixada", "alterações não baixadas");
    el.appendChild(d);
    btn("Baixar .json", "dirty-download", "Baixa o acervo com as alterações, com o nome do arquivo de origem.", downloadCollection);
  }
  if (App.saved) {
    const e = btn("editar", "edit-btn", "Liga a curadoria: mudar a ordem, mover, excluir e importar faixas.", toggleEditing);
    e.setAttribute("aria-pressed", App.editing ? "true" : "false");
    if (App.editing) btn("importar faixas…", "import-tracks-btn", "Traz faixas de outro .json para este acervo.", pickTracksFile);
  }
  if (Store.db && Store.count > 0) {
    btn("acervos (" + Store.count + ")", "acervos-btn", "Os acervos guardados neste navegador: abrir outro ou esquecer.", openAcervosDialog);
  }
  if (App.originForget) {
    btn("esquecer", "", "Apaga a cópia deste acervo guardada neste navegador. O arquivo no seu computador não é tocado.",
        () => forgetAcervo(App.source));
  }
}
````

**Texto novo, literal:**

````
/** Guarda o texto de origem (mostrado no menu do seletor de acervo) e se o
    acervo aberto pode ser esquecido; sem argumentos, so redesenha a barra.
    Na I1 (DEC-030) a linha de origem acabou: as pecas dela moram na barra. */
function setOrigin(text, forgettable) {
  if (text !== undefined) { App.originText = text; App.originForget = !!forgettable; }
  updateBar();
}
````

### E14 — app: o aberto marcado na lista — `app/index.html`

**Ancora, literal:**

````
    if (r.source === App.source) {
      const s = document.createElement("span"); s.className = "acervo-open"; s.textContent = "aberto";
````

**Texto novo, literal:**

````
    if (r.source === App.source) {
      li.classList.add("is-open");
      const s = document.createElement("span"); s.className = "acervo-open"; s.textContent = "aberto";
````

### E15 — app: abrir um acervo fecha o menu — `app/index.html`

**Ancora, literal:**

````
        document.getElementById("acervos-dialog").close();
````

**Texto novo, literal:**

````
        closePopovers(false);
````

### E16 — app: esquecer na lista vira × — `app/index.html`

**Ancora, literal:**

````
    const f = document.createElement("button"); f.type = "button"; f.textContent = "esquecer";
````

**Texto novo, literal:**

````
    const f = document.createElement("button"); f.type = "button"; f.textContent = "×";
    f.setAttribute("aria-label", "Esquecer " + (r.title || r.source));
    f.title = "Apaga a cópia guardada neste navegador. O arquivo no seu computador não é tocado.";
````

### E17 — app: abrir a lista de acervos abre o menu — `app/index.html`

**Ancora, literal:**

````
async function openAcervosDialog() {
  await renderAcervosDialog();
  document.getElementById("acervos-dialog").showModal();
}
````

**Texto novo, literal:**

````
/** Abre o menu do seletor de acervo com a lista atualizada (era uma janela, ate a 0.13.0). */
async function openAcervosDialog() {
  await renderAcervosDialog();
  openPopover("acervo");
}
````

### E18 — app: sai o fechar da janela de acervos e entra o bloco da barra unica — `app/index.html`

**Ancora, literal:**

````
document.getElementById("acervos-close-btn").addEventListener("click", () =>
  document.getElementById("acervos-dialog").close());

// A abertura e assincrona (IndexedDB); a importacao espera por ela.
````

**Texto novo, literal:**

````

/* ===================================================================
   Barra unica (I1, DEC-030 — spec meta/specs/261105-barra-unica.md)
   Tres paineis ancorados (seletor de acervo, Filtros, «⋯»): so um aberto por
   vez; Esc e clique fora fecham, e o foco volta ao botao que abriu. A fileira
   de etiquetas mostra os filtros aplicados (Baymard: remover direto no resumo).
   =================================================================== */
const POPS = {
  acervo: ["acervo-btn", "acervo-pop"],
  filtros: ["filters-btn", "filters-pop"],
  mais: ["more-btn", "more-pop"],
};
let openPop = null;
const isMobile = () => window.matchMedia("(max-width: 719px)").matches;

function openPopover(name) {
  closePopovers(false);
  const [b, p] = POPS[name].map(id => document.getElementById(id));
  p.hidden = false;
  b.setAttribute("aria-expanded", "true");
  openPop = name;
  const first = p.querySelector("button:not([hidden]), select, input");
  if (first) first.focus();
}
/** Fecha o painel aberto; com `restoreFocus`, devolve o foco ao botao dele. */
function closePopovers(restoreFocus) {
  if (!openPop) return;
  const [b, p] = POPS[openPop].map(id => document.getElementById(id));
  p.hidden = true;
  b.setAttribute("aria-expanded", "false");
  openPop = null;
  if (restoreFocus) b.focus();
}
function togglePopover(name) {
  if (openPop === name) closePopovers(true); else openPopover(name);
}

/** Redesenha as pecas da barra a partir do estado (chamada por setOrigin e render). */
function updateBar() {
  const has = !!App.collection;
  document.getElementById("acervo-title").textContent =
    has ? (App.collection.title || App.source || "Acervo") : "Abrir um acervo";
  document.getElementById("acervo-source").textContent = has && App.source ? App.source + " · " : "";
  if (!has) document.getElementById("stats").textContent = "";
  // Sem acervo aberto, «outro» nao faz sentido.
  document.getElementById("import-btn").textContent = has ? "Importar outro .json…" : "Importar .json…";
  document.getElementById("origin").textContent = App.originText ? "Acervo " + App.originText : "";
  // Sem acervo aberto nao ha o que esquecer, mesmo que a origem antiga ainda diga que sim.
  document.getElementById("forget-btn").hidden = !(has && App.originForget);
  const dirty = App.saved && App.changes > 0;
  document.getElementById("bar-draft").hidden = !dirty;
  document.body.classList.toggle("has-draft", dirty);
  document.getElementById("draft-text").textContent =
    dirty ? nPlural(App.changes, "alteração não salva", "alterações não salvas") : "";
  const be = document.getElementById("bar-edit");
  be.textContent = "";
  if (App.saved) {
    const mk = (label, role, title, fn) => {
      const b = document.createElement("button");
      b.type = "button"; b.textContent = label; b.dataset.role = role; b.title = title;
      b.addEventListener("click", fn); be.appendChild(b); return b;
    };
    const e = mk("editar", "edit-btn", "Liga a curadoria: mudar a ordem, mover, excluir e importar faixas.", toggleEditing);
    e.setAttribute("aria-pressed", App.editing ? "true" : "false");
    if (App.editing) mk("importar faixas…", "import-tracks-btn", "Traz faixas de outro .json para este acervo.", pickTracksFile);
  }
  const me = document.getElementById("menu-edit");
  me.hidden = !App.saved;
  me.textContent = App.editing ? "Desligar editar" : "Ligar editar";
  document.getElementById("menu-import-tracks").hidden = !(App.saved && App.editing);
}

/** As etiquetas dos filtros aplicados, a contagem «N de M» e o numero no botao. */
function renderChips(f, shown, total) {
  const list = document.getElementById("chips-list");
  list.textContent = "";
  const chip = (kind, value, clear) => {
    const c = document.createElement("span"); c.className = "fchip";
    const k = document.createElement("span"); k.className = "k"; k.textContent = kind;
    c.appendChild(k); c.appendChild(document.createTextNode(" " + value + " "));
    const x = document.createElement("button"); x.type = "button"; x.textContent = "×";
    x.setAttribute("aria-label", "Tirar o filtro " + kind);
    x.addEventListener("click", () => { clear(); render(); });
    c.appendChild(x); list.appendChild(c);
  };
  const alb = document.getElementById("filter-album");
  if (f.album) chip("Álbum", alb.options[alb.selectedIndex].text, () => { alb.value = ""; });
  if (f.state) chip("Estado", f.state, () => { document.getElementById("filter-state").value = ""; });
  if (f.used) chip("Uso", f.used === "used" ? "só usadas" : "não usadas", () => { document.getElementById("filter-used").value = ""; });
  const q = document.getElementById("search").value.trim();
  if (q) chip("Busca", "«" + q + "»", () => { document.getElementById("search").value = ""; });
  const n = (f.album ? 1 : 0) + (f.state ? 1 : 0) + (f.used ? 1 : 0);
  const badge = document.getElementById("filters-count");
  badge.hidden = !n; badge.textContent = n ? String(n) : "";
  document.getElementById("filters-btn").setAttribute("aria-label", n ? "Filtros, " + n + (n === 1 ? " ligado" : " ligados") : "Filtros");
  document.getElementById("chips-count").textContent = shown + " de " + nPlural(total, "faixa", "faixas");
  document.getElementById("chips").hidden = !(n || q);
}
function clearAllFilters() {
  ["filter-album", "filter-state", "filter-used", "search"].forEach(id => { document.getElementById(id).value = ""; });
  render();
}

function setSearchOpen(open) {
  document.getElementById("top").classList.toggle("search-open", open);
  document.getElementById("search-toggle").setAttribute("aria-expanded", open ? "true" : "false");
  if (open) document.getElementById("search").focus();
}

document.getElementById("acervo-btn").addEventListener("click", () => {
  if (openPop === "acervo") { closePopovers(true); return; }
  openAcervosDialog();
});
document.getElementById("filters-btn").addEventListener("click", () => togglePopover("filtros"));
document.getElementById("more-btn").addEventListener("click", () => { dismissTour(); togglePopover("mais"); });
// Item de menu escolhido fecha o painel (a acao do item ja rodou: o ouvinte
// dele dispara antes, no proprio botao).
["acervo-pop", "more-pop"].forEach(id => document.getElementById(id).addEventListener("click", e => {
  if (e.target.closest('[role="menuitem"]')) closePopovers(false);
}));
document.addEventListener("pointerdown", e => {
  if (!openPop) return;
  const wrap = document.getElementById(POPS[openPop][1]).parentElement;
  if (!wrap.contains(e.target)) closePopovers(false);
});
document.addEventListener("keydown", e => {
  if (e.key === "Escape" && openPop) { e.preventDefault(); closePopovers(true); return; }
  if (e.key === "Escape" && e.target && e.target.id === "search" && isMobile()) { setSearchOpen(false); document.getElementById("search-toggle").focus(); return; }
  if (e.key !== "/" || e.ctrlKey || e.metaKey || e.altKey) return;
  const t = e.target, tag = t && t.tagName;
  // Falso positivo que nao pode acontecer: digitar «/» dentro de um campo.
  if (tag === "INPUT" || tag === "TEXTAREA" || tag === "SELECT" || (t && t.isContentEditable)) return;
  if (document.querySelector("dialog[open]")) return;
  e.preventDefault();
  if (isMobile()) setSearchOpen(true); else document.getElementById("search").focus();
});
document.getElementById("search-toggle").addEventListener("click", () =>
  setSearchOpen(!document.getElementById("top").classList.contains("search-open")));
document.getElementById("filters-clear").addEventListener("click", clearAllFilters);
document.getElementById("chips-clear").addEventListener("click", clearAllFilters);
document.getElementById("filters-done").addEventListener("click", () => closePopovers(true));
document.getElementById("draft-save").addEventListener("click", () => downloadCollection());
document.getElementById("forget-btn").addEventListener("click", () => forgetAcervo(App.source));
document.getElementById("menu-import").addEventListener("click", () => document.getElementById("file-input").click());
document.getElementById("menu-edit").addEventListener("click", toggleEditing);
document.getElementById("menu-import-tracks").addEventListener("click", pickTracksFile);
document.getElementById("more-brand").textContent =
  "Cancioneiro " + document.querySelector('[data-role="app-version"]').textContent;

/* Aviso de primeira abertura da 0.14.0: os botoes do cabecalho foram para o «⋯».
   Some ao clicar em «entendi» ou ao abrir o «⋯», e nao volta (App.ui.tour14). */
function dismissTour() {
  if (App.ui.tour14) return;
  App.ui.tour14 = true;
  saveUiState();
  document.getElementById("tour").hidden = true;
}
document.getElementById("tour").hidden = !!App.ui.tour14;
document.getElementById("tour-ok").addEventListener("click", dismissTour);

// A abertura e assincrona (IndexedDB); a importacao espera por ela.
````

### E19 — CHANGELOG: 0.14.0 — `meta/CHANGELOG.md`

**Ancora, literal:**

````
## [0.13.0] — 2026-11-05
````

**Texto novo, literal:**

````
## [0.14.0] — 2026-11-05

Primeira entrega da frente de interface (I1, DEC-030): uma barra única no topo. O cartão não muda.

### Added
- **Barra única**, fixa no topo, de 48 px (no celular, 51): o nome e a versão, o seletor de acervo, a busca, «Filtros», o rascunho, «editar» e o «⋯».
- **Seletor de acervo:** mostra o título, o arquivo e a contagem do acervo aberto. Abre um menu com os acervos guardados (abrir; × para esquecer), «Importar outro .json…», «Esquecer este acervo», a origem da cópia e o estado do armazenamento. Substitui «acervos (N)», a janela de acervos e a linha de origem.
- **Filtros num painel** (Álbum, Estado, Uso), com o número de filtros ligados no botão, e uma fileira de etiquetas removíveis com «N de M faixas» e «Limpar tudo». A tecla `/` leva à busca (fora de um campo de texto).
- **«⋯»:** Importar .json…, Baixar .json, Exportar .md, Prompt para chats, Baixar exemplo e Estrutura do cartão. Na primeira abertura, um aviso de uma linha diz para onde eles foram; some em «entendi» e fica guardado no navegador (`tour14`).
- **Celular:** botões de 44 px; a busca abre numa linha própria; o rascunho fica no pé da tela. O topo, com um filtro ligado, passou de 469 px de controles para 95 px.

### Changed
- O rascunho aparece na barra como «● N alterações não salvas», com **Salvar .json**: o mesmo «Baixar .json» da DEC-028, com o nome de origem.
- Os seis botões do cabeçalho foram para o «⋯»; «editar» e «importar faixas…» foram da linha de origem para a barra.

### Fixed
- Sem acervo, a barra de filtros não fica mais na tela: a regra `[hidden]` vale para o app todo (i-044).

Spec `meta/specs/261105-barra-unica.md`: 14 de 14 conferências dos 13 critérios no Chromium headless, com prova de vida no app da 0.13.0; os testes das entregas 1 a 3 seguem em 15 de 15, 25 de 25 e 19 de 19, com os seletores dos botões que mudaram de lugar.

---

## [0.13.0] — 2026-11-05
````

### E20 — README: versao — `README.md`

**Ancora, literal:**

````
> **Estado:** v0.13.0 — ferramenta em uso. Lê, guarda e edita vários acervos, copia por campo, troca módulos de estilo, ajusta o BPM, **mede cada prompt contra os limites do Suno**, exporta Markdown, exporta uma faixa como `.json` e **entrega o prompt para chats gerarem canções no esquema**. Publicada no GitHub Pages. Ver `meta/ROADMAP.md`.
````

**Texto novo, literal:**

````
> **Estado:** v0.14.0 — ferramenta em uso. Lê, guarda e edita vários acervos, copia por campo, troca módulos de estilo, ajusta o BPM, **mede cada prompt contra os limites do Suno**, exporta Markdown, exporta uma faixa como `.json` e **entrega o prompt para chats gerarem canções no esquema**. Publicada no GitHub Pages. Ver `meta/ROADMAP.md`.
````

### E21 — README: abrir e trocar de acervo pelo seletor — `README.md`

**Ancora, literal:**

````
   **Ou local:** duplo-clique em `app/index.html` (modo `file://`) e clique em *Importar .json* — ou arraste o arquivo para a tela. Cada acervo importado fica guardado no navegador, pelo nome do arquivo: o app reabre no último que você usou, e *acervos (N)*, na linha de origem, troca de um para outro sem procurar o arquivo.
````

**Texto novo, literal:**

````
   **Ou local:** duplo-clique em `app/index.html` (modo `file://`), clique em *Abrir um acervo*, no começo da barra, e em *Importar .json…* — ou arraste o arquivo para a tela. Cada acervo importado fica guardado no navegador, pelo nome do arquivo: o app reabre no último que você usou, e o seletor de acervo (o mesmo botão, que passa a mostrar o título do aberto) troca de um para outro sem procurar o arquivo.
````

### E22 — README: filtros e Estrutura do cartao — `README.md`

**Ancora, literal:**

````
3. Navegue por álbuns, copie style e lyrics por botão e o título clicando nele, marque o que usou. Em *Estrutura*, arraste os blocos para mudar a ordem e esconda os que você não usa (o Exclude já vem oculto: o formulário gratuito do Suno v6 não tem o campo).
````

**Texto novo, literal:**

````
3. Navegue por álbuns, copie style e lyrics por botão e o título clicando nele, marque o que usou. *Filtros*, na barra, escolhe álbum, estado e uso; cada filtro ligado vira uma etiqueta com ×, e a tecla `/` leva à busca. Em *Estrutura do cartão* (no «⋯», à direita da barra), arraste os blocos para mudar a ordem e esconda os que você não usa (o Exclude já vem oculto: o formulário gratuito do Suno v6 não tem o campo).
````

### E23 — README: editar e Salvar na barra — `README.md`

**Ancora, literal:**

````
7. Para reorganizar, ligue *editar* na linha de origem: cada cartão ganha ↑ ↓, *mover…* e *excluir*, e *importar faixas…* traz faixas de outro `.json`. As mudanças ficam num rascunho no navegador; *Baixar .json* baixa com o nome do arquivo original — substitua o antigo por ele, e ele passa a ser a fonte.
````

**Texto novo, literal:**

````
7. Para reorganizar, ligue *editar* na barra: cada cartão ganha ↑ ↓, *mover…* e *excluir*, e *importar faixas…* traz faixas de outro `.json`. As mudanças ficam num rascunho no navegador; a barra mostra quantas são, com *Salvar .json*, que baixa com o nome do arquivo original — substitua o antigo por ele, e ele passa a ser a fonte.
````

### E24 — README: Prompt no menu — `README.md`

**Ancora, literal:**

````
No app, clique em **Prompt**, escreva o seu pedido e copie: o prompt vai inteiro, com o pedido no lugar. Cole num chat novo: ele devolve um arquivo `.json` (ou, se não puder criar arquivo, o JSON num bloco de código, com botão de copiar). Arraste o arquivo para o app. O texto do prompt vive em `schema/PROMPT-PARA-CHATS.md` — o botão busca esse arquivo a cada clique, então o que está no repositório é o que você copia.
````

**Texto novo, literal:**

````
No app, abra o «⋯» da barra, clique em **Prompt para chats**, escreva o seu pedido e copie: o prompt vai inteiro, com o pedido no lugar. Cole num chat novo: ele devolve um arquivo `.json` (ou, se não puder criar arquivo, o JSON num bloco de código, com botão de copiar). Arraste o arquivo para o app. O texto do prompt vive em `schema/PROMPT-PARA-CHATS.md` — o botão busca esse arquivo a cada clique, então o que está no repositório é o que você copia.
````

### E25 — README: Exemplo no menu — `README.md`

**Ancora, literal:**

````
**Exemplo** baixa um acervo pronto (`data/demo.json`) para ver a estrutura.
````

**Texto novo, literal:**

````
**Baixar exemplo**, no mesmo «⋯», baixa um acervo pronto (`data/demo.json`) para ver a estrutura.
````

### E26 — README: fonte de verdade pelo seletor — `README.md`

**Ancora, literal:**

````
O acervo canônico são **arquivos JSON** no esquema: os exemplos versionados em `data/`, e o acervo pessoal fora do repo (DEC-026). O navegador guarda **cópias dos acervos importados** (IndexedDB) e, no localStorage, as marcações por acervo e a estrutura do cartão — cache, nunca a fonte: a linha de origem diz de onde a cópia veio e quando, e *esquecer* a apaga sem tocar no arquivo. Com *editar*, a cópia vira rascunho até você baixar o `.json` e substituir o arquivo. Ver `meta/DECISIONS.md` (DEC-004, DEC-022, DEC-028, DEC-029).
````

**Texto novo, literal:**

````
O acervo canônico são **arquivos JSON** no esquema: os exemplos versionados em `data/`, e o acervo pessoal fora do repo (DEC-026). O navegador guarda **cópias dos acervos importados** (IndexedDB) e, no localStorage, as marcações por acervo e a estrutura do cartão — cache, nunca a fonte: o menu do seletor de acervo diz de onde a cópia veio e quando, e *Esquecer este acervo* a apaga sem tocar no arquivo. Com *editar*, a cópia vira rascunho até você salvar o `.json` e substituir o arquivo. Ver `meta/DECISIONS.md` (DEC-004, DEC-022, DEC-028, DEC-029, DEC-030).
````

### E27 — DECISIONS: DEC-030 — `meta/DECISIONS.md`

**Ancora, literal:**

````
**Consequências:** (+) O aviso só aparece quando há o que perder. (−) Um rascunho gravado pode ficar meses sem ser baixado; a marca «alterado: N alterações não baixadas» na linha de origem é o lembrete.
````

**Texto novo, literal:**

````
**Consequências:** (+) O aviso só aparece quando há o que perder. (−) Um rascunho gravado pode ficar meses sem ser baixado; a marca «alterado: N alterações não baixadas» na linha de origem é o lembrete.

## DEC-030 — Frente de interface: três painéis, SortableJS 1.15.7 embutido, sem o interruptor «editar», em quatro entregas; a I1 é a barra única

**Data:** 2026-11-05
**Status:** aceita
**Contexto:** O dono pediu uma interface «bonita, profissional, intuitiva», com estudo antes (i-044 a i-048). Na 0.13.0, o topo tinha três faixas (cabeçalho de 86 px, filtros e linha de origem, 98 px) e, no celular, 469 px antes da primeira faixa; os filtros sumiam ao rolar; «esquecer», «acervos» e «editar» moravam numa linha de texto miúdo. A análise `meta/analises/261105-ANALISE-frente-de-interface.md`, com protótipo no canvas «Cancioneiro: nova interface», foi decidida pelo dono em 2026-11-05, como recomendada nos quatro pontos.
**Decisão:**
- **Arquitetura B:** barra única no topo, lateral de álbuns e acervos, lista no centro e detalhe à direita. No celular, a lista e o detalhe são telas próprias.
- **Arrastar com o SortableJS 1.15.7 (MIT), embutido no `app/index.html`:** a versão fica fixa, com a licença no cabeçalho e o hash registrado na entrega que o trouxer. Continua um arquivo só, sem build (DEC-002). Todo arrastar tem um caminho sem arrastar, pelo «⋯» da faixa (WCAG 2.5.7).
- **Sem o interruptor «editar»:** sai na I3, junto do «Desfazer»; até lá, fica na barra.
- **Quatro entregas, nesta ordem:** I1 barra única (0.14.0) → I2 lista e detalhe (0.15.0) → I3 organizar (0.16.0) → I4 salvar no arquivo (0.17.0, i-043). Antes de cada spec, um protótipo navegável da entrega no mesmo canvas.
- **I1 (esta versão), spec `meta/specs/261105-barra-unica.md`:** barra fixa de no máximo 48 px (52 no celular) com o seletor de acervo como menu, a busca com a tecla `/`, os filtros num painel com etiquetas removíveis, o rascunho com «Salvar .json», «editar» e o «⋯» com os seis botões do antigo cabeçalho. A regra `[hidden]` passa a valer para o app todo. O cartão não muda.
**Alternativas consideradas:** A, refinar o que existe (menos risco, mas não resolve os filtros nem o lugar da edição); C, uma tabela no estilo Airtable (boa para comparar, ruim para ler e copiar prompts longos); arrastar com código próprio (mais leve, mas foco, toque e rolagem são o que costuma quebrar); só caminhos sem arrastar (seguro, mas não atende ao pedido do dono); manter o interruptor «editar» (menos clique errado, mais um modo para lembrar).
**Consequências:** (+) A I1 sozinha já devolve o espaço do topo e deixa os filtros à vista ao rolar. (+) Cada entrega é usável sozinha. (−) A I3 soma uns 45 KB de biblioteca: medir o tempo de abertura no `file://` antes e depois. (−) Com duas visões (Lista e Cartões), toda saída nova reverifica a regra de domínio nas duas. (−) Sem o interruptor, o clique errado fica mais fácil; é o «Desfazer» que segura isso, e o teste da I3 mede o falso positivo (soltar no mesmo lugar não conta alteração).
````

### E28 — IDEAS: i-043 vira a I4 — `meta/IDEAS.md`

**Ancora, literal:**

````
**Gatilho atingido (2026-11-05):** a entrega 3 está pronta (0.13.0). Com ela, o passo que sobra é baixar e substituir o arquivo; gravar direto tira esse passo.
````

**Texto novo, literal:**

````
**Gatilho atingido (2026-11-05):** a entrega 3 está pronta (0.13.0). Com ela, o passo que sobra é baixar e substituir o arquivo; gravar direto tira esse passo.
**Planejada (DEC-030):** é a I4 da frente de interface (0.17.0), depois de a I3 deixar o «Salvar» fácil de achar.
````

### E29 — IDEAS: i-044 entregue (1) — `meta/IDEAS.md`

**Ancora, literal:**

````
### i-044 💡 A barra de controles não some quando não há acervo
````

**Texto novo, literal:**

````
### i-044 ✅ A barra de controles não some quando não há acervo
````

### E30 — IDEAS: i-044 entregue (2) — `meta/IDEAS.md`

**Ancora, literal:**

````
Achado no teste da entrega 2 (2026-11-05): o CSS `.controls { display: flex }` vence o atributo `hidden` que o `render()` põe na barra quando não há acervo, então os filtros vazios ficam na tela no estado inicial e depois de esquecer todos. Já era assim antes da 0.12.0. O conserto provável é uma linha (`.controls[hidden] { display: none; }`), mas muda o que o dono vê ao abrir o app vazio — conferir na tela antes.
````

**Texto novo, literal:**

````
Achado no teste da entrega 2 (2026-11-05): o CSS `.controls { display: flex }` vence o atributo `hidden` que o `render()` põe na barra quando não há acervo, então os filtros vazios ficam na tela no estado inicial e depois de esquecer todos. Já era assim antes da 0.12.0. O conserto provável é uma linha (`.controls[hidden] { display: none; }`), mas muda o que o dono vê ao abrir o app vazio — conferir na tela antes.
**Entregue (0.14.0, I1, DEC-030):** a regra `[hidden] { display: none !important; }` vale para o app todo; sem acervo, nem a fileira de etiquetas nem o rascunho aparecem. Spec `meta/specs/261105-barra-unica.md`, WO 0025.
````

### E31 — IDEAS: i-045 entregue (1) — `meta/IDEAS.md`

**Ancora, literal:**

````
### i-045 💡 Cabeçalho compacto
````

**Texto novo, literal:**

````
### i-045 ✅ Cabeçalho compacto
````

### E32 — IDEAS: i-045 entregue (2) — `meta/IDEAS.md`

**Ancora, literal:**

````
`[relatado pelo dono, 2026-11-05]` A barra do topo está «muito folgada»; deixá-la quase colada às bordas dos botões. Medido nas capturas dele (Chrome, janela de 720 px de altura): o cabeçalho é fixo (`position: sticky`) e ocupa uns 85 px. Objetivo dito por ele: uma interface «bonita, profissional, intuitiva». Faz parte da frente de interface (i-044 a i-047), que vem **depois** das funcionalidades em curso, por pedido dele, e começa por um turno de pesquisa.
````

**Texto novo, literal:**

````
`[relatado pelo dono, 2026-11-05]` A barra do topo está «muito folgada»; deixá-la quase colada às bordas dos botões. Medido nas capturas dele (Chrome, janela de 720 px de altura): o cabeçalho é fixo (`position: sticky`) e ocupa uns 85 px. Objetivo dito por ele: uma interface «bonita, profissional, intuitiva». Faz parte da frente de interface (i-044 a i-047), que vem **depois** das funcionalidades em curso, por pedido dele, e começa por um turno de pesquisa.
**Entregue (0.14.0, I1, DEC-030):** uma barra única, fixa, de 48 px (no celular, 51), no lugar do cabeçalho, da barra de filtros e da linha de origem.
````

### E33 — IDEAS: i-046 em andamento (1) — `meta/IDEAS.md`

**Ancora, literal:**

````
### i-046 💡 Filtros que acompanham a rolagem, e visões do acervo
````

**Texto novo, literal:**

````
### i-046 🔨 Filtros que acompanham a rolagem, e visões do acervo
````

### E34 — IDEAS: i-046 em andamento (2) — `meta/IDEAS.md`

**Ancora, literal:**

````
`[relatado pelo dono, 2026-11-05]` A barra «Álbum · Estado · Uso · buscar» some ao rolar uma lista grande (nas capturas, só o cabeçalho fica fixo). Ele quer que ela fique fixa ou que se possa chamá-la. Inspirações citadas: o controle e a organização de e-commerce e de tabelas, e de Notion e Airtable, com visões (lista, tabela) e opções melhores. Pede pesquisa antes de spec.
````

**Texto novo, literal:**

````
`[relatado pelo dono, 2026-11-05]` A barra «Álbum · Estado · Uso · buscar» some ao rolar uma lista grande (nas capturas, só o cabeçalho fica fixo). Ele quer que ela fique fixa ou que se possa chamá-la. Inspirações citadas: o controle e a organização de e-commerce e de tabelas, e de Notion e Airtable, com visões (lista, tabela) e opções melhores. Pede pesquisa antes de spec.
**Em andamento (DEC-030):** os filtros fixos, num painel, com etiquetas removíveis e «N de M», entraram na I1 (0.14.0). As visões (Lista e Cartões, com o detalhe à direita) são a I2.
````

### E35 — IDEAS: i-047 planejada e i-048 nova — `meta/IDEAS.md`

**Ancora, literal:**

````
`[relatado pelo dono, 2026-11-05]` Painéis que abrem pela lateral direita, com etiquetas no estilo de «bookmarks». Exemplo dele: os acervos da entrega 2 também numa barra lateral, além da janela. Junto da i-046 na pesquisa. O arrastar cartões para reordenar (fora da entrega 3) entra nesta frente.
````

**Texto novo, literal:**

````
`[relatado pelo dono, 2026-11-05]` Painéis que abrem pela lateral direita, com etiquetas no estilo de «bookmarks». Exemplo dele: os acervos da entrega 2 também numa barra lateral, além da janela. Junto da i-046 na pesquisa. O arrastar cartões para reordenar (fora da entrega 3) entra nesta frente.
**Planejada (DEC-030):** a lateral de álbuns e acervos é a I2 (0.15.0).

### i-048 💡 Edição e organização com UX de verdade, arrastando onde for útil
`[relatado pelo dono, 2026-11-05]` A estrutura para «edição, controle e organização das faixas, acervos e tudo mais» não está prática nem intuitiva, e falta muito UX/UI. Ele pede estudo e planejamento antes, e praticidades como **arrastar objetos** onde for possível, útil e interessante: cartões entre posições e álbuns, faixas para um acervo, arquivos para a tela. Junta-se às i-044 a i-047, numa frente só (análise `meta/analises/261105-ANALISE-frente-de-interface.md`).
**Planejada (DEC-030):** é a I3 (0.16.0): arrastar pela alça, com o SortableJS embutido; o «⋯» por faixa como caminho sem arrastar; seleção em lote; «Desfazer»; o fim do interruptor «editar».
````

### E36 — ROADMAP: a frente de interface em quatro entregas — `meta/ROADMAP.md`

**Ancora, literal:**

````
- ⬜ Refino da interface (i-044 a i-047): cabeçalho compacto, filtros que acompanham a rolagem, visões de lista e tabela, painel lateral. Começa por um turno de pesquisa (Notion, Airtable, filtros de e-commerce) antes de spec.
````

**Texto novo, literal:**

````
- 🔨 Frente de interface (i-043 a i-048, DEC-030), em quatro entregas: ✅ barra única, com o seletor de acervo, os filtros com etiquetas e o «⋯» (0.14.0) · ⬜ lista e detalhe, com a lateral de álbuns e acervos (0.15.0) · ⬜ organizar: arrastar, «⋯» por faixa, lote, «Desfazer», sem o interruptor «editar» (0.16.0) · ⬜ salvar direto no arquivo (0.17.0, i-043).
````

### E37 — STATUS inteiro — `meta/STATUS.md`

**Arquivo inteiro, literal** (substitui o arquivo; chegada `12275f2ad23e4d62f5cd71eb28299dfac7851e3a`):

````
# STATUS.md — Cancioneiro

> **O agora.** O que funciona, o que está em progresso, o que está quebrado, backlog curto.
> Rolante: item resolvido sai daqui e vai para o CHANGELOG. Médio/longo prazo vive no ROADMAP.

**Versão atual:** 0.14.0 · **Fase:** 3a, 3a.2, o BPM da 3b, o prompt-modelo e as conveniências de uso concluídos e conferidos · os álbuns antigos convertidos (i-008, fora do repo) · curadoria no app concluída nas três entregas (DEC-028, DEC-029) · frente de interface na I1 de quatro (DEC-030) · kit de música lido pelo KCM, à espera da resposta (i-039)

---

## Última conversa (2026-11-05, frente de interface: análise, decisão e I1, WO 0025)

- **Entrega 3 da curadoria conferida na tela pelo dono** (roteiro OK `[relatado pelo dono]`): a curadoria (i-040, i-041) está fechada nas três entregas.
- **Frente de interface decidida (DEC-030):** análise `meta/analises/261105-ANALISE-frente-de-interface.md`, com protótipo no canvas «Cancioneiro: nova interface». B (três painéis), SortableJS 1.15.7 embutido, sem o interruptor «editar» (sai na I3, com «Desfazer»), em quatro entregas: I1 → I2 → I3 → I4.
- **I1, barra única (0.14.0):** barra fixa de 48 px com o seletor de acervo, a busca (tecla `/`), Filtros com etiquetas removíveis, o rascunho com «Salvar .json», «editar» e o «⋯». No celular, 95 px de controles no topo (eram 469). Spec `meta/specs/261105-barra-unica.md`; 14 de 14 conferências no Chromium headless, testadas pelo chat.
- **i-048** (edição e organização com UX de verdade, arrastando) registrada; é a I3.
- **Este bloco substitui o anterior, da WO 0024** (entrega 3). O que ele dizia está no CHANGELOG [0.13.0], na spec `meta/specs/261105-curadoria-pela-tela.md` e em `logs/2026-11-05.md` (Conversas 4 a 6).

## Funciona (pronto)

- **Ferramenta `app/index.html`:** importa/carrega JSON, cartões por álbum, copiar Style/Lyrics/Exclude por botão (o botão entrega o texto que está na tela — FIX-007), marca «usei», filtros por álbum/estado/uso, busca, módulos de estilo que recompõem o Style ao vivo, variantes e notas recolhíveis, «Baixar .json» limpo e «Importar .json» que saneia chaves internas e diz quantas removeu (FIX-004/006). A versão aparece no cabeçalho. A importação avisa quantos módulos citados não existem na coleção (FIX-009).
- **Painel de qualidade (0.5.0, DEC-018):** linha abaixo de Style, Lyrics e Exclude com caracteres contra o limite do campo, tags do Style e negações «no X». Vermelho só para truncamento.
- **Custo de cada módulo no chip (0.6.0, DEC-019):** com o painel de módulos aberto, cada chip mostra `−N`, `+N` ou `0` tags; a linha de qualidade diz quanto o style base usa sozinho quando o recomposto passa de 10.
- **Controle de BPM no cartão (0.7.0, DEC-020):** campo 20-300 com `−5`/`+5` e «voltar a N» governa todo «NN bpm» do Style principal; o chip de andamento é atalho (no máximo um ligado); variantes e «Baixar .json» não mudam; o valor é só da sessão.
- **Esquema JSON canônico** (`schema/`). Biblioteca de referência para autoria em `schema/style-modules.json` (27 módulos, sete camadas); cada acervo traz os seus (DEC-016).
- **Datasets:** `data/exemplo-cinzeiro.json` (1 faixa, com os 5 módulos que cita) e `data/demo.json` (2 álbuns, 3 faixas). Os acervos do dono moram fora do repo (DEC-026): `../album-referencias (1).json` (7 faixas, 50 módulos) `../acervos/rainha-da-preguica.json` (10 álbuns, 151 faixas) e `../acervos/albuns-reagrupados.json` (12 álbuns, 205 faixas), os dois gerados pelos conversores.
- **Conversor da família BR** (`scripts/convert_br.py`, 0.9.1, DEC-026): guias `..._VOL<n>_GUIA.md` → coleção no esquema, um álbum por volume, rótulos fora do copiável, variantes e referência levadas; relata o que passa do limite do Suno sem cortar. Teste: `python3 scripts/test_convert_br.py`.
- **Conversor dos guias de `Albuns/`** (`scripts/convert_guides.py`, 0.10.0): formatos mistos → coleção, com mapa de grupos que reprova faixa perdida. Teste: `python3 scripts/test_convert_guides.py`.
- **Kit de música** (`kit-musica/`, 0.10.0, DEC-027): bloco para Instruções e CEREBRO de um projeto de música, skills `macetes-suno` e `revisar-faixa`. Uso à mão em `kit-musica/README.md`.
- **Validação** (`scripts/validate.py`): sintaxe, esquema (com `jsonschema`), integridade referencial dos módulos (id ausente ou objeto no lugar do id, sem traceback — FIX-009), versão igual nos quatro lugares, um BPM só por faixa (DEC-020) e as marcações do prompt que o app lê (DEC-021) e os limites da skill `revisar-faixa` contra o app (DEC-027); código 1 se falhar; a última linha diz se o esquema foi de fato conferido.
- **Export MD** (faixa / álbum / acervo), com o rótulo fora do bloco e o Style da tela nos três (0.9.0, D5).
- **Exportar faixa como `.json`** (0.11.0, DEC-028): botão no rodapé do cartão; a faixa sai como acervo — o álbum de origem (id e título), a faixa e os módulos que ela cita — e importa como qualquer acervo. Sai o dado do acervo, não os módulos ligados nem o BPM da tela; o toast conta os módulos e os citados que não existem. Conferido na tela pelo dono em 2026-11-04.
- **Vários acervos no navegador** (0.12.0, DEC-028): cada importado fica no IndexedDB pelo nome do arquivo; o seletor de acervo, na barra, abre ou esquece cada um; reabre no último aberto; marcas «usei» por acervo. Sem IndexedDB, guarda só o último, como antes.
- **Curadoria pela tela** (0.13.0, DEC-028, DEC-029): «editar» na barra; ↑ ↓, mover, novo álbum, excluir e importar faixas num rascunho gravado no navegador; «● N alterações não salvas» com «Salvar .json» pelo nome de origem.
- **Barra única** (0.14.0, DEC-030): fixa, de 48 px; seletor de acervo como menu, busca com `/`, Filtros num painel com etiquetas removíveis e «N de M», rascunho, «editar» e o «⋯» com Importar, Baixar, Exportar .md, Prompt para chats, Baixar exemplo e Estrutura do cartão. No celular, 51 px, botões de 44 px, a busca numa linha própria e o rascunho no pé.
- **Prompt-modelo** (`schema/PROMPT-PARA-CHATS.md`, DEC-021, DEC-023): contrato de módulo, style com 6 a 8 tags e até 10 com os módulos ligados; pede o JSON como arquivo e, sem arquivo, em bloco de código. Dois retestes em 2026-10-29: 6 de 6 faixas dentro do contrato e do orçamento, nos dois.
- **«Prompt para chats» e «Baixar exemplo»** (0.8.0, DEC-021; no «⋯» desde a 0.14.0): buscam o prompt e o `data/demo.json` do repositório no clique; a janela do prompt recebe o «Meu pedido».
- **Conveniências (0.9.0, DEC-022, DEC-023):** «Estrutura» do cartão (ordem e blocos visíveis, no navegador); copiar o título; arrastar o `.json` para importar; o último acervo importado volta ao abrir, com origem, data e «esquecer»; a importação aceita a resposta do chat colada inteira e avisa.
- **Publicado no GitHub Pages** em `https://joaolucas-nds.github.io/cancioneiro/app/index.html` — o push em `main` publica.

## Em progresso

- **Kit de música no KCM (i-039)** — o KCM leu a carta 01 e responde por carta, sem data. Gatilho: sem resposta até o primeiro projeto de música novo, o projeto usa o kit à mão (`kit-musica/README.md`).

## Quebrado / pendências que travam

- (nada quebrado)

## Pendências do dono

- **Conferir a I1 na tela** — roteiro na conversa de 2026-11-05 (WO 0025), depois do push, no computador e no celular.
- **Instalar o validador de esquema nesta máquina.** Sem `jsonschema` e `referencing`, o `validate.py` só confere sintaxe e diz `ESQUEMA NAO CONFERIDO` na última linha. Uma vez, no CMD: `pip install jsonschema referencing --break-system-packages`. Depois, `python3 scripts/validate.py` deve terminar em `Tudo conforme ao esquema.`

## Backlog curto (próximas ações concretas)

1. **I2 — Lista e detalhe** (i-046, i-047, DEC-030) — protótipo navegável no canvas, depois spec: a visão Lista com cabeçalhos de álbum fixos, o detalhe à direita (no celular, tela própria), a lateral de álbuns e acervos, a visão guardada no navegador. «Cartões» continua.
2. **I3 — Organizar** (i-048) e **I4 — Salvar no arquivo** (i-043), nessa ordem, cada uma com protótipo e spec.
3. **Rampa de BPM** (i-042) — três faixas BR reprovam no `validate.py` por mudarem de andamento de propósito.
4. **Pesquisar outras plataformas de música por IA** (i-032) — um turno de pesquisa antes de qualquer mudança de esquema.
5. **Avisar palavra de andamento que contradiz o BPM** (i-029) — pede uma tabela palavra → faixa de BPM, com fonte e data.
6. **Importar prompts prontos dos álbuns como módulos** — o último ⬜ da 3b no ROADMAP; o índice-mestre da BR e os «estilos originais» do VOL5 trazem fórmulas de estilo.

## Notas de estado

- **Repo local do dono:** `C:\Users\alexk\Tools\cancioneiro\cancioneiro` (Windows). O chat lê e grava na pasta vinculada; commit e push são do Code (DEC-010). A pasta-pai guarda relatórios, notas e o acervo do dono, fora do Git; o lido vai para `../notas-arquivadas/`.
- **Canal:** pasta vinculada é o padrão; a cópia achatada (FlatDrop) é reserva (DEC-017).
- **Limites do Suno:** o v6 saiu em 2026-09-09 e a nota oficial não documenta limite de campo; os números do painel vêm de fonte secundária, com fonte e data no `QUALITY_LIMITS` (DEC-018). Outra fonte secundária (2026-08) põe o ideal em 4 a 7 descritores; o prompt usa 6 a 8. Reconferir quando houver documentação oficial. O `meta/HISTORY.md` §5 ganhou a interface do v6 vista na conta (2026-10-29); o resto do arquivo ainda descreve o v5.5.
- **Exclude no v6-mini:** o formulário gratuito não tem o campo (capturas de 2026-10-29). Desde a 0.9.1 (DEC-025) o bloco vem oculto por padrão, com o aviso «no X → Exclude» junto (D3); o dado continua no JSON e no export. Quem usa o campo liga em «Estrutura».
- **Navegador (DEC-004, DEC-022, DEC-028):** guarda as cópias dos acervos importados (IndexedDB, banco `cancioneiro`), as marcas «usei» por acervo e a estrutura do cartão (`localStorage`, `cancioneiro:ui`). As cópias são cache: se o arquivo mudou fora, importe de novo; o menu do seletor de acervo diz quando a cópia foi feita. O aviso de primeira abertura da 0.14.0 guarda `tour14` no mesmo `cancioneiro:ui`.
- **Rascunho (DEC-028, DEC-029):** com alterações, a cópia guardada está à frente do arquivo até «Salvar .json» e substituir. A marca na barra é o lembrete; esquecer e reimportar pedem confirmação.
- **No `file://`, todas as páginas locais dividem o armazenamento** (sonda de 2026-11-04): o app só lê e grava o que tem o nome `cancioneiro`. O `file://` e o Pages são origens diferentes — o que está guardado num não aparece no outro.
- **Conversores são de primeira geração (DEC-028):** depois de mudar um acervo (à mão ou, com a entrega 3, no app), não rode o conversor por cima dele.
- **«Prompt para chats» e «Baixar exemplo»:** dependem de rede e do Pages. No `file://`, só funcionam se o Pages aceitar o `fetch` de uma página local — não conferido (o dono abriu o `file://` em 2026-10-29, sem relatar o resultado do botão); sem isso, a janela mostra o link para a versão publicada (DEC-021).
- **Estado de sessão** (módulos ligados e BPM escolhido) sobrevive a filtro, busca e «marcar usei»; volta ao acervo ao recarregar a página ou importar de novo (FIX-008, DEC-020).
- **Limite conhecido:** `tryAutoLoad` (carregamento automático pelo Pages) não saneia chaves internas — só a importação por arquivo faz isso. Inócuo enquanto nenhum acervo contaminado for para `data/`.
- **Pendência de contexto — ASU:** o dono perguntou se o «modo ASU» do KCM seria melhor que o modo Code para este projeto; ficou pendente até ele trazer a descrição do ASU `[relatado pelo dono, sem material de apoio]`.
- Design: na recomposição do Style a base manda — desligar um módulo não remove o que já está no style base; módulos só somam. O dedup compara sequências de palavras (FIX-003). Os módulos de gênero e de andamento costumam custar 0 tag por isso (DEC-019). O chip de andamento é atalho do controle de BPM, no máximo um ligado (DEC-020).
````

## Fora de escopo

- A lista, o detalhe e a lateral (I2); o arrastar, o «⋯» por faixa, o lote, o «Desfazer» e o fim do interruptor (I3); salvar no arquivo (I4). O SortableJS **nao** entra nesta WO.
- Spec, CONTEXT e log: ja gravados pelo chat; nao edite.
- Nada em `data/`, `schema/`, `scripts/` ou `kit-musica/`.

## Armadilhas desta WO

- **`autocrlf=true` na maquina do dono:** os hashes valem no disco em LF, antes do `add`. Nao rode `git checkout -- <arquivo>`: ele regrava em CRLF.
- **A E08 e a E18 sao longas** (o cabecalho e a barra de filtros inteiros; o bloco da barra unica, no lugar do fechar da janela de acervos, antes de «A abertura e assincrona»): se o aplicador ler ancora linha a linha, compare o bloco inteiro; o hash de chegada do `app/index.html` e a prova.
- **Remocoes (E02, E07, E10):** o texto novo e so a linha anterior e a seguinte, iguais; nao estranhe.
- **O `validate.py` desta maquina termina em `ESQUEMA NAO CONFERIDO`** (falta `jsonschema`): estado conhecido.
- **Os testes escrevem no stderr:** use `2>&1 >/dev/null | tail -1`.

## Depois de aplicar — conferencia antes do commit

| # | Checagem | Comando | Esperado |
|---|---|---|---|
| 1 | **Os dez arquivos sao os testados** | `sha1sum app/index.html README.md meta/CHANGELOG.md meta/DECISIONS.md meta/IDEAS.md meta/ROADMAP.md meta/STATUS.md meta/specs/261105-barra-unica.md meta/CONTEXT.md logs/2026-11-05.md` | a coluna **chegada**, os dez. **Prova as 37 edicoes.** |
| 2 | Validacao | `python3 scripts/validate.py; echo "exit=$?"` | `exit=0`, com a linha `OK  versao 0.14.0 igual em CHANGELOG, app, README e STATUS`; ultima linha `Tudo conforme ao esquema.` ou `ESQUEMA NAO CONFERIDO (...)` (esta maquina) |
| 3 | Os conversores seguem passando | `python3 scripts/test_convert_br.py 2>&1 >/dev/null \| tail -1` e `python3 scripts/test_convert_guides.py 2>&1 >/dev/null \| tail -1` | `OK` e `OK` |
| 4 | O codigo novo | `grep -c '^function updateBar' app/index.html`, `grep -c '^function renderChips' app/index.html`, `grep -c 'id="acervos-dialog"' app/index.html` | `1`, `1`, `0` |
| 5 | O registro | `grep -m1 '^## \[' meta/CHANGELOG.md`, `grep -c '^## DEC-030 ' meta/DECISIONS.md`, `grep -c '^### i-048 ' meta/IDEAS.md` | `## [0.14.0] — 2026-11-05`, `1`, `1` |
| 6 | A pendencia resolvida saiu | `grep -c '^- \*\*Conferir a entrega 3 na tela' meta/STATUS.md`, `grep -c '^- \*\*Conferir a I1 na tela' meta/STATUS.md` | `0`, `1` |
| 7 | Nada alem do previsto | `GIT_OPTIONAL_LOCKS=0 git status --short --untracked-files=all` | os dez arquivos e esta WO, e nada mais (nenhum `.txt`, nenhum `__pycache__`) |

**Os tres campos de cada passo:** as sete sao rodadas por **quem aplica (o Code)**, na raiz do repo, em Git Bash,
com `LC_ALL=C.UTF-8`. **Chega no ramo?** A checagem 1 cobre os dez arquivos inteiros, inclusive o `app/index.html`
que o chat executou (`updateBar`, `renderChips`, `openPopover`, `closePopovers`, `setOrigin`, `renderAcervosDialog`).
**Esta e qual pergunta?** A 2 e a 3 respondem «funciona?»; as outras, «esta la?». O «funciona?» da barra no
navegador do dono e dele, depois do push, pelo roteiro do chat.

## Relatorio de aplicacao

Grave em `../261105-HHMM-code-cancioneiro-apply-wo0025.txt`, com o `HHMM` de `date +%y%m%d-%H%M` rodado na
hora. Diga o resultado da checagem 1 em primeiro lugar.

**Proximo comando** (ultima linha do relatorio, cru e sozinho):

```
/wrap
```

## Commit

```
git add app/index.html README.md meta/CHANGELOG.md meta/DECISIONS.md meta/IDEAS.md meta/ROADMAP.md meta/STATUS.md meta/specs meta/CONTEXT.md logs/2026-11-05.md meta/workorders
```

```
git commit -m "feat: barra unica no topo e versao 0.14.0" -m "Frente de interface, entrega I1 (DEC-030): barra fixa de 48 px com seletor de acervo, busca com a tecla /, filtros num painel com etiquetas removiveis, rascunho com Salvar .json e o menu de mais acoes; a regra [hidden] vale para o app todo (i-044). Celular com 95 px de controles. Spec com o resultado, CONTEXT, IDEAS (i-043 a i-048), ROADMAP, README, STATUS inteiro."
```

```
git push
```
