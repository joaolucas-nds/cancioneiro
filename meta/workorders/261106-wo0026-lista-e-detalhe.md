# WO 0026 — Lista e detalhe (frente de interface, I2), DEC-031 e versao 0.15.0

## Cabecalho

> **Tipo:** mista — CODIGO (`app/index.html`) e registro (CHANGELOG, README, DECISIONS, IDEAS, ROADMAP, STATUS inteiro).
> **Config sugerida:** Sonnet · `/effort medium`. 26 edicoes literais e o STATUS inteiro, aplicados e testados pelo chat num clone de `7dfd672`; cada arquivo tem hash de chegada.
> **Pre-requisito:** commit `7dfd672`, branch `main`, sincronizada com `origin/main`. O `git status` mostra **so** o que o chat gravou: `M logs/2026-11-06.md`, `M meta/CONTEXT.md`, `M meta/specs/261106-lista-e-detalhe.md` e esta WO (`?? meta/workorders/...wo0026...`).
> **Base:** spec `meta/specs/261106-lista-e-detalhe.md`, com os tres pontos decididos pelo dono em 2026-11-06 (viram a DEC-031 nesta WO); a frente e a DEC-030.
> **Depende de:** WO 0025, ja aplicada (`0158c88`, wrap `3b6b94f`).
>
> **Arquivos — partida e chegada, os dois medidos pelo chat** (em LF; chegada = aplicar literalmente as edicoes abaixo):
>
> | arquivo | partida (sha1) | chegada (sha1) |
> |---|---|---|
> | `app/index.html` | `04f9484721e0aa8ca5b6a5ddfd64652acee94548` | `556b5557f59e6c8935e8473aefbe5d1d8e84f74a` |
> | `README.md` | `f047d3dff285aeeb8cbfa351ad3fc1dcd7fcce3d` | `457aba7429ac2608ee1d9946e1c5f99afca32e41` |
> | `meta/CHANGELOG.md` | `957d0d54f71a55629d41fd97dca862325e54fcbd` | `90571f8f2cea09e2dbec2697bdbc46f58db7e8fd` |
> | `meta/DECISIONS.md` | `be49dcecfcdf85c87a2cbbefd3dae5cc9cb57fff` | `273cb57faa24d151c81b984af2a8ba7dd568f1ea` |
> | `meta/IDEAS.md` | `e5504c028eaabbdb2893fd52eb189c76735ffcc8` | `134cdd655332936685f9e188597a63f61b39e63d` |
> | `meta/ROADMAP.md` | `0d097d6a07184c1cabe1bdc9cc21994054e42c6d` | `ed7e8295b4546e2066e1d30dca79bf5c4c59d063` |
> | `meta/STATUS.md` | `15c0436293d960da809c9730b4de3664da09a69f` | `2853814f26e882371eafbb6b6919e1d8ca4c560a` |
> | `meta/specs/261106-lista-e-detalhe.md` | `41abeb6f6c3993d3863ea9732d2a7597ce60cc4e` | `41abeb6f6c3993d3863ea9732d2a7597ce60cc4e` (gravado pelo chat; só versiona) |
> | `meta/CONTEXT.md` | `749fab6968413761d5645016869a6ccb3f42dc8d` | `749fab6968413761d5645016869a6ccb3f42dc8d` (gravado pelo chat; só versiona) |
> | `logs/2026-11-06.md` | `09384dfaeabc3f734ae5ebf8f24adf106954c33e` | `09384dfaeabc3f734ae5ebf8f24adf106954c33e` (gravado pelo chat; só versiona) |
>
> **Ancora semantica:** se um trecho-ancora nao bater EXATAMENTE, PARE e reporte.
> **Idempotencia:** antes de cada edicao, procure o texto NOVO INTEIRO; se ja estiver la, PULE e diga no relatorio. Arquivo inteiro (E27): se o hash ja for o de chegada, PULE.
> **Ancoras lidas em:** cada ancora foi recortada pelo chat do arquivo de partida (`git show 7dfd672:<arquivo>`; os tres do chat, depois de gravados) e conferida como ocorrendo **exatamente 1 vez** no estado em que a edicao e aplicada, na ordem abaixo. Ancora sempre de linha inteira. Nenhuma edicao desta WO remove trecho sem pôr outro no lugar.
> **Canal dos meta neste ciclo = CODE:** esta WO e o registro. A spec, o CONTEXT e o log ja estao gravados pelo chat (DEC-010); a WO so os versiona.

---

## 1. Por que

Segunda entrega da frente de interface (i-046, i-047), pela spec da I2:

- **Visao Lista** (a padrao) ou **Cartoes** (a de antes), num par de botoes na barra; no celular, no «⋯». A escolha fica em `cancioneiro:ui` (`view`).
- **Lista:** uma linha de 44 px por faixa, por album, com o cabecalho do album fixo; titulo, estado, idioma, BPM, **saude** (o pior nivel do painel de qualidade) e os botoes **Style**, **Lyrics** (so o conteudo, o Style recomposto na hora) e ✓ «usei».
- **Detalhe a direita:** o cartao de hoje, sem mudanca, com ‹ ›, setas, `Esc` e `#faixa=<id>` no endereco (recarregar reabre; o «Voltar» fecha).
- **Lateral** a partir de 1280 px: albuns (filtram) e acervos guardados (abrem). **Celular:** detalhe em tela propria, com os botoes de copiar no pe.
- **DEC-031** registra os tres pontos decididos pelo dono: Lista por padrao, celular sem gaveta (contraria a analise), titulo da linha abre o detalhe.

O app de chegada foi executado pelo chat no Chromium headless (`file://`): **15 de 15** criterios; os testes das entregas 1 a 3 e da I1 seguem em **15 de 15**, **25 de 25**, **19 de 19** e **14 de 14** (os da curadoria e da I1 em Cartoes, onde medem o cartao); prova de vida no app de partida (reprova). A Lista de 300 faixas desenha em cerca de 50 ms. `validate.py` exit=0 com `jsonschema`, `test_convert_br.py` e `test_convert_guides.py` OK. O chat olhou a tela a 1366, 1024, 800 e 390 px.

**Versao 0.15.0 nesta WO.** A conferencia de tela e do dono, depois do push.

## Edicao 0 — Conferencia de hash e de arvore

```
sha1sum app/index.html README.md meta/CHANGELOG.md meta/DECISIONS.md meta/IDEAS.md meta/ROADMAP.md meta/STATUS.md meta/specs/261106-lista-e-detalhe.md meta/CONTEXT.md logs/2026-11-06.md
GIT_OPTIONAL_LOCKS=0 git status --short
```

Os dez batem com a coluna **partida**; o `git status` mostra exatamente as quatro linhas do Pre-requisito. Qualquer outra coisa: **PARE e reporte**.

## Edicoes E01 a E27

Na ordem. **Todas as secoes de edicao tem o mesmo titulo, `### Exx — ...`**, inclusive a de arquivo inteiro.
Copie o que esta ENTRE as linhas de quatro crases, sem elas. **O bloco termina na linha de quatro crases, nunca
num titulo:** o CHANGELOG, a DECISIONS, a IDEAS e o STATUS trazem `## ` e `### ` dentro do bloco.

### E01 — app: o CSS da lista, da lateral e do detalhe — `app/index.html`

**Ancora, literal:**

````
  .cards { display: grid; grid-template-columns: repeat(auto-fill, minmax(340px, 1fr)); gap: 16px; }
````

**Texto novo, literal:**

````
  .cards { display: grid; grid-template-columns: repeat(auto-fill, minmax(340px, 1fr)); gap: 16px; }

  /* ---- Lista e detalhe (I2, DEC-030 — spec meta/specs/261106-lista-e-detalhe.md) ----
     .shell poe lado a lado a lateral (#side), o miolo (#main) e o detalhe (#detail).
     A lateral e o detalhe ficam fixos abaixo do topo; --top-h e a altura medida
     do #top (48 px sem etiquetas, 84 com), nunca um numero escrito aqui. */
  :root { --top-h: 48px; }
  .shell { display: flex; align-items: flex-start; }
  .shell > main { flex: 1 1 auto; min-width: 0; }
  body.view-list main { max-width: none; margin: 0; padding: 0 0 32px; container-type: inline-size; container-name: lista; }
  body.view-list .album { margin: 0; }
  body.view-list .album-head { position: sticky; top: var(--top-h); z-index: 3; background: var(--paper);
    margin: 0; padding: 14px 16px 8px; border-bottom: 1px solid var(--ink); }
  body.view-list .album-head h2 { font-size: 18px; }
  body.view-list .album-desc { margin: 6px 16px 8px; }

  .rows { list-style: none; margin: 0; padding: 0; }
  .row { display: flex; align-items: center; gap: 8px; height: 44px; box-sizing: border-box;
    padding: 0 12px 0 16px; border-bottom: 1px solid var(--line); cursor: pointer; }
  .row.is-open { background: var(--paper-2); }
  .row-open { flex: 1 1 auto; min-width: 160px; height: 36px; padding: 0; border: 0; background: transparent;
    text-align: left; font-weight: 600; color: var(--ink); overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
  .row-open:hover { color: var(--ember); }
  .row.used .row-open, .row.used .row-meta { color: var(--ink-soft); }
  /* No computador, os quatro campos sao colunas da linha; no celular, uma linha de texto. */
  .row-meta { display: contents; }
  .row-state { flex: none; width: 64px; }
  .row-lang { flex: none; width: 90px; font-size: 12px; color: var(--ink-soft); overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
  .row-bpm { flex: none; width: 58px; font-size: 12px; color: var(--ink-soft); white-space: nowrap; }
  .row-health { flex: none; width: 150px; font-size: 12px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
  .row-health.ok { color: var(--moss); }
  .row-health.warn { color: var(--amber); font-weight: 600; }
  .row-health.over { color: var(--ember); font-weight: 700; }
  .row-copy { flex: none; min-width: 60px; height: 28px; padding: 0 8px; font-size: 12px; }
  .row-copy.copied { background: var(--moss); color: #fff; border-color: var(--moss); }
  .row-used { flex: none; width: 28px; height: 28px; padding: 0; font-size: 12px; color: var(--ink-soft); }
  .row-used[aria-pressed="true"] { background: var(--moss); border-color: var(--moss); color: #fff; }
  /* As colunas cedem antes do titulo, que nunca fica com menos de 160 px. */
  @container lista (max-width: 760px) { .row-lang { display: none; } }
  @container lista (max-width: 660px) { .row-bpm { display: none; } }
  @container lista (max-width: 600px) { .row-state { display: none; } }

  .side { display: none; flex: 0 0 232px; width: 232px; box-sizing: border-box; position: sticky; top: var(--top-h);
    height: calc(100vh - var(--top-h)); overflow: auto; padding: 12px 8px; border-right: 1px solid var(--line); }
  @media (min-width: 1280px) { .side { display: block; } }
  .side-head { font-size: 11px; letter-spacing: .06em; text-transform: uppercase; color: var(--ink-soft); padding: 4px 8px; }
  .side-head + .side-list { margin-bottom: 18px; }
  .side-list { list-style: none; margin: 0; padding: 0; }
  .side-item { width: 100%; display: flex; align-items: center; gap: 8px; padding: 7px 8px; border: 0; border-radius: 6px;
    background: transparent; text-align: left; }
  .side-item .t { flex: 1; min-width: 0; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
  .side-item .n { color: var(--ink-soft); font-size: 12px; }
  .side-item[aria-current="true"] { background: var(--paper-2); font-weight: 600; color: var(--ink); }
  .side-item.empty-album { color: var(--ink-soft); }

  .detail { flex: 0 0 auto; width: clamp(400px, 34vw, 520px); box-sizing: border-box; position: sticky; top: var(--top-h);
    height: calc(100vh - var(--top-h)); display: flex; flex-direction: column; border-left: 1px solid var(--line); background: var(--paper); }
  .detail-head { flex: none; height: 44px; display: flex; align-items: center; gap: 4px; padding: 0 8px 0 16px;
    border-bottom: 1px solid var(--line); }
  .detail-ctx { flex: 1; min-width: 0; font-size: 12px; color: var(--ink-soft); overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
  .dbtn { flex: none; width: 32px; height: 32px; padding: 0; border-color: transparent; background: transparent; font-size: 16px;
    display: inline-flex; align-items: center; justify-content: center; }
  .dbtn:disabled { opacity: .35; cursor: default; }
  .dbtn svg { width: 18px; height: 18px; fill: none; stroke: currentColor; stroke-width: 1.8; stroke-linecap: round; stroke-linejoin: round; }
  .detail-back, .detail-foot { display: none; }
  .detail-body { flex: 1; overflow: auto; overscroll-behavior: contain; padding: 12px; }
  /* 720 a 959 px: o detalhe abre por cima da lista, a direita. */
  @media (min-width: 720px) and (max-width: 959px) {
    .detail { position: fixed; right: 0; top: var(--top-h); bottom: 0; height: auto; width: min(480px, calc(100vw - 48px));
      z-index: 12; box-shadow: -12px 0 32px rgba(35,32,27,.18); }
  }
  .view-switch { display: flex; flex-shrink: 0; border: 1px solid var(--line); border-radius: 8px; overflow: hidden; }
  .view-switch button { border: 0; border-radius: 0; background: transparent; }
  .view-switch button + button { border-left: 1px solid var(--line); }
  .view-switch button[aria-pressed="true"] { background: var(--ink); color: var(--paper); }
  .pop [role="menuitemradio"] { text-align: left; border: 0; background: transparent; height: auto; padding: 9px 10px; border-radius: 8px; }
  .pop [role="menuitemradio"][aria-checked="true"] { font-weight: 600; }
  .pop [role="menuitemradio"][aria-checked="true"]::before { content: "✓ "; }
  /* A barra ganhou «Lista | Cartoes»: abaixo de 1180 px o nome sai (a versao segue no «⋯»). */
  @media (max-width: 1179px) { .brand { display: none; } }

  @media (max-width: 719px) {
    .view-switch { display: none; }
    .row { height: auto; min-height: 64px; padding: 6px 4px 6px 16px; display: grid;
      grid-template-columns: minmax(0, 1fr) 44px; grid-template-areas: "t u" "m u"; column-gap: 4px; row-gap: 2px; }
    .row-open { grid-area: t; height: auto; min-width: 0; font-size: 15px; }
    .row-meta { grid-area: m; display: block; font-size: 12px; color: var(--ink-soft); overflow: hidden;
      text-overflow: ellipsis; white-space: nowrap; }
    .row-meta > span { display: inline !important; width: auto; }
    .row-meta > span + span::before { content: " · "; color: var(--ink-soft); font-weight: 400; }
    .row-meta .badge { border: 0; background: none; padding: 0; font-size: 12px; }
    .row-copy { display: none; }
    .row-used { grid-area: u; width: 44px; height: 44px; }
    .detail { position: fixed; inset: 0; width: auto; height: auto; z-index: 20; border: 0; }
    .detail-head { height: 52px; padding: 0 4px; }
    .dbtn { width: 44px; height: 44px; }
    .detail-back { display: inline-flex; }
    .detail-close { display: none; }
    .detail-body { padding: 12px 12px 16px; }
    .detail-foot { display: flex; flex: none; gap: 8px; padding: 10px 12px 16px; border-top: 1px solid var(--line); background: var(--paper); }
    .detail-foot button { flex: 1; height: 48px; font-size: 15px; }
    .detail-foot #detail-copy-title { flex: 0 0 72px; }
    body.detail-open .bar-draft { z-index: 25; bottom: 84px; }
    body.detail-open .toast { bottom: 84px; }
  }
````

### E02 — app: versao 0.15.0 — `app/index.html`

**Ancora, literal:**

````
    <span class="version" data-role="app-version">v0.14.0</span>
````

**Texto novo, literal:**

````
    <span class="version" data-role="app-version">v0.15.0</span>
````

### E03 — app: Lista | Cartoes na barra — `app/index.html`

**Ancora, literal:**

````
  <div class="bar-space"></div>
````

**Texto novo, literal:**

````
  <div class="view-switch" id="view-switch" role="group" aria-label="Visão">
    <button type="button" id="view-list" aria-pressed="true">Lista</button>
    <button type="button" id="view-cards" aria-pressed="false">Cartões</button>
  </div>
  <div class="bar-space"></div>
````

### E04 — app: a visao no «⋯» do celular — `app/index.html`

**Ancora, literal:**

````
      <button type="button" role="menuitem" class="mobile-only" id="menu-import-tracks" hidden>Importar faixas…</button>
````

**Texto novo, literal:**

````
      <button type="button" role="menuitem" class="mobile-only" id="menu-import-tracks" hidden>Importar faixas…</button>
      <div class="pop-sep mobile-only"></div>
      <button type="button" role="menuitemradio" class="mobile-only" id="menu-view-list" aria-checked="true">Visão: Lista</button>
      <button type="button" role="menuitemradio" class="mobile-only" id="menu-view-cards" aria-checked="false">Visão: Cartões</button>
````

### E05 — app: o aviso de primeira abertura da 0.15.0 — `app/index.html`

**Ancora, literal:**

````
<div class="tour" id="tour" role="status" hidden>Prompt, Exemplo, Importar, Baixar e Exportar agora ficam em <b>⋯</b>, no canto direito da barra. <button type="button" class="link" id="tour-ok">entendi</button></div>
````

**Texto novo, literal:**

````
<div class="tour" id="tour15" role="status" hidden>Nova visão em lista: clique numa faixa para ver o cartão ao lado. Os cartões de antes estão em <b>Cartões</b>. <button type="button" class="link" id="tour15-ok">entendi</button></div>
<div class="tour" id="tour" role="status" hidden>Prompt, Exemplo, Importar, Baixar e Exportar agora ficam em <b>⋯</b>, no canto direito da barra. <button type="button" class="link" id="tour-ok">entendi</button></div>
````

### E06 — app: a lateral, antes do miolo — `app/index.html`

**Ancora, literal:**

````
<main id="main">
````

**Texto novo, literal:**

````
<div class="shell" id="shell">
<nav class="side" id="side" aria-label="Álbuns e acervos" hidden>
  <div class="side-head">Álbuns</div>
  <ul class="side-list" id="side-albums"></ul>
  <div class="side-head">Acervos neste navegador</div>
  <ul class="side-list" id="side-acervos"></ul>
</nav>
<main id="main">
````

### E07 — app: o detalhe, depois do miolo — `app/index.html`

**Ancora, literal:**

````
</main>

<div class="toast" id="toast"></div>
````

**Texto novo, literal:**

````
</main>
<aside class="detail" id="detail" aria-label="Detalhe da faixa" hidden>
  <div class="detail-head">
    <button type="button" class="dbtn detail-back" id="detail-back" aria-label="Voltar à lista"><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M12.5 4.5 7 10l5.5 5.5"/></svg></button>
    <span class="detail-ctx" id="detail-ctx"></span>
    <button type="button" class="dbtn" id="detail-prev" aria-label="Faixa anterior">‹</button>
    <button type="button" class="dbtn" id="detail-next" aria-label="Próxima faixa">›</button>
    <button type="button" class="dbtn detail-close" id="detail-close" aria-label="Fechar o detalhe">×</button>
  </div>
  <div class="detail-body" id="detail-body"></div>
  <div class="detail-foot" id="detail-foot">
    <button type="button" class="btn-primary" id="detail-copy-style">Copiar Style</button>
    <button type="button" id="detail-copy-lyrics">Copiar Lyrics</button>
    <button type="button" id="detail-copy-title" aria-label="Copiar o título">Título</button>
  </div>
</aside>
</div>

<div class="toast" id="toast"></div>
````

### E08 — app: sem acervo, sem lateral nem detalhe — `app/index.html`

**Ancora, literal:**

````
  if (!App.collection) { document.getElementById("chips").hidden = true; updateBar(); return; }
````

**Texto novo, literal:**

````
  if (!App.collection) {
    document.getElementById("chips").hidden = true;
    document.getElementById("side").hidden = true;
    closeDetail({ noFocus: true });
    updateBar();
    return;
  }
````

### E09 — app: na Lista, uma linha por faixa — `app/index.html`

**Ancora, literal:**

````
    const grid = document.createElement("div");
    grid.className = "cards";
    songs.forEach(song => grid.appendChild(renderCard(song)));
    sec.appendChild(grid);
````

**Texto novo, literal:**

````
    // I2: na Lista, uma linha por faixa; em Cartoes, a grade de sempre.
    if (currentView() === "list") {
      const rows = document.createElement("ul");
      rows.className = "rows";
      songs.forEach(song => rows.appendChild(renderRow(song)));
      sec.appendChild(rows);
    } else {
      const grid = document.createElement("div");
      grid.className = "cards";
      songs.forEach(song => grid.appendChild(renderCard(song)));
      sec.appendChild(grid);
    }
````

### E10 — app: a lateral e o detalhe acompanham o render — `app/index.html`

**Ancora, literal:**

````
  renderChips(f, shown, all);
  updateBar();
}
````

**Texto novo, literal:**

````
  renderChips(f, shown, all);
  renderSide(f);
  updateBar();
  if (currentView() === "list") { afterListRender(); openFromHash(); }
}
````

### E11 — app: modulo e BPM do cartao chegam a linha — `app/index.html`

**Ancora, literal:**

````
  const ctl = card.querySelector(".bpm-ctl");
  if (ctl && ctl.sync) ctl.sync();
}
````

**Texto novo, literal:**

````
  const ctl = card.querySelector(".bpm-ctl");
  if (ctl && ctl.sync) ctl.sync();
  updateRow(song);   // I2: o BPM e a saude da linha desta faixa, sem redesenhar a Lista
}
````

### E12 — app: trocar de acervo fecha o detalhe — `app/index.html`

**Ancora, literal:**

````
  (json.styleModules || []).forEach(m => { App.modulesById[m.id] = m; });
  populateAlbumFilter();
  render();
````

**Texto novo, literal:**

````
  (json.styleModules || []).forEach(m => { App.modulesById[m.id] = m; });
  closeDetail({ noFocus: true });   // I2: a faixa aberta era do acervo anterior
  populateAlbumFilter();
  render();
````

### E13 — app: a lateral lista os acervos de novo — `app/index.html`

**Ancora, literal:**

````
  if (text !== undefined) { App.originText = text; App.originForget = !!forgettable; }
  updateBar();
}
````

**Texto novo, literal:**

````
  if (text !== undefined) { App.originText = text; App.originForget = !!forgettable; }
  updateBar();
  renderSideAcervos();   // I2: abrir, importar ou esquecer muda a lista da lateral
}
````

### E14 — app: a curadoria rola ate a linha ou o cartao — `app/index.html`

**Ancora, literal:**

````
    const c = document.querySelector('.card[data-id="' + CSS.escape(focusId) + '"]');
````

**Texto novo, literal:**

````
    // I2: no miolo, a linha (Lista) ou o cartao (Cartoes); o do detalhe nao conta.
    const c = document.querySelector('#main [data-id="' + CSS.escape(focusId) + '"]');
````

### E15 — app: o item de visao tambem fecha o «⋯» — `app/index.html`

**Ancora, literal:**

````
  if (e.target.closest('[role="menuitem"]')) closePopovers(false);
````

**Texto novo, literal:**

````
  if (e.target.closest('[role="menuitem"], [role="menuitemradio"]')) closePopovers(false);
````

### E16 — app: o bloco da lista e do detalhe — `app/index.html`

**Ancora, literal:**

````
// A abertura e assincrona (IndexedDB); a importacao espera por ela.
````

**Texto novo, literal:**

````
/* ===================================================================
   Lista e detalhe (I2, DEC-030 — spec meta/specs/261106-lista-e-detalhe.md)
   A visao Lista desenha uma linha por faixa; o detalhe, a direita, mostra o
   cartao de hoje (renderCard, sem mudanca). A lateral filtra por album e troca
   de acervo. A visao fica em App.ui.view ("list" | "cards"); sem escolha, Lista.
   =================================================================== */
function currentView() { return App.ui.view === "cards" ? "cards" : "list"; }

/** Liga a visao escolhida: classes do body, botoes da barra e itens do «⋯». */
function syncView() {
  const v = currentView();
  document.body.classList.toggle("view-list", v === "list");
  document.body.classList.toggle("view-cards", v === "cards");
  document.getElementById("view-list").setAttribute("aria-pressed", v === "list" ? "true" : "false");
  document.getElementById("view-cards").setAttribute("aria-pressed", v === "cards" ? "true" : "false");
  document.getElementById("menu-view-list").setAttribute("aria-checked", v === "list" ? "true" : "false");
  document.getElementById("menu-view-cards").setAttribute("aria-checked", v === "cards" ? "true" : "false");
}
function setView(v) {
  if (currentView() === v) return;
  App.ui.view = v;
  saveUiState();
  if (v === "cards") closeDetail({ noFocus: true });
  syncView();
  render();
}

const HEALTH_MARK = { ok: "●", warn: "▲", over: "■" };
/** Resumo do painel de qualidade para a linha: o PIOR nivel entre as marcas que o
    cartao mostraria (as mesmas funcoes e a mesma visibilidade de blocos), e uma
    frase curta. O nivel neutro (9 e 10 tags) conta como dentro. */
function songHealth(song) {
  const levels = [], notes = [];
  const collect = el => el.querySelectorAll(".q").forEach(q => levels.push(q.classList[1]));
  const lenNote = (n, lim, name, warnText) => {
    const lv = lengthLevel(n, lim);
    if (lv === "over") notes.push(["over", name + " passa de " + fmt(lim.max)]);
    else if (lv === "warn") notes.push(["warn", warnText]);
  };
  if (!isHidden("style")) {
    const st = recomposedStyle(song);
    collect(styleQuality(st, song.lyrics, baseTagCount(song)));
    lenNote(st.length, QUALITY_LIMITS.style, "Style", "Style perto de " + fmt(QUALITY_LIMITS.style.max));
    const t = countTags(st), L = QUALITY_LIMITS.tags;
    if (t < L.vague || t > L.many) notes.push(["warn", "Style " + t + " tags"]);
    if (!isHidden("exclude")) findNegations(st, song.lyrics).forEach(n => notes.push(["warn", "«" + n + "» no Exclude"]));
  }
  if (!isHidden("lyrics")) {
    const ly = song.lyrics || "";
    collect(lengthQuality(ly, QUALITY_LIMITS.lyrics, "", ""));
    lenNote(ly.length, QUALITY_LIMITS.lyrics, "Lyrics", "Lyrics acima de " + fmt(QUALITY_LIMITS.lyrics.warn));
  }
  if (!isHidden("exclude") && song.excludeStyles && song.excludeStyles.length) {
    const ex = song.excludeStyles.join(", ");
    collect(lengthQuality(ex, QUALITY_LIMITS.exclude, "", ""));
    lenNote(ex.length, QUALITY_LIMITS.exclude, "Exclude", "Exclude perto de " + fmt(QUALITY_LIMITS.exclude.max));
  }
  const level = levels.includes("over") ? "over" : levels.includes("warn") ? "warn" : "ok";
  const note = notes.find(n => n[0] === level);
  return { level, text: level === "ok" ? "tudo dentro" : (note ? note[1] : "pede atenção") };
}
function fillHealth(el, song) {
  const h = songHealth(song);
  el.className = "row-health " + h.level;
  el.dataset.level = h.level;
  el.textContent = HEALTH_MARK[h.level] + " " + h.text;
  el.title = h.text;
}
const bpmText = song => { const v = currentBpm(song); return v ? v + " bpm" : "—"; };

/** Uma linha da Lista. Os botoes copiam SO o conteudo (regra de dominio): o
    rotulo fica no botao e no aria-label. O Style e recomposto na hora do clique,
    com os modulos e o BPM da sessao, como o «copiar» do cartao (FIX-007). */
function renderRow(song) {
  const li = document.createElement("li");
  li.className = "row" + (isUsed(song.id) ? " used" : "");
  li.dataset.id = song.id;
  const open = document.createElement("button");
  open.type = "button"; open.className = "row-open"; open.textContent = song.title;
  open.setAttribute("aria-controls", "detail"); open.setAttribute("aria-expanded", "false");
  open.addEventListener("click", () => openDetail(song.id));
  li.appendChild(open);
  const meta = document.createElement("span"); meta.className = "row-meta";
  const cell = (cls, text) => { const s = document.createElement("span"); s.className = cls; if (text !== undefined) s.textContent = text; meta.appendChild(s); return s; };
  const st = cell("row-state");
  const b = document.createElement("span"); b.className = "badge state"; b.textContent = song.state; st.appendChild(b);
  cell("row-lang", song.language || "");
  cell("row-bpm", bpmText(song));
  fillHealth(cell("row-health"), song);
  li.appendChild(meta);
  const copyBtn = (role, label, what, get) => {
    const c = document.createElement("button");
    c.type = "button"; c.className = "row-copy"; c.dataset.role = role; c.textContent = label;
    c.setAttribute("aria-label", "Copiar " + what + " de " + song.title);
    c.addEventListener("click", () => copyText(get(), c));
    li.appendChild(c);
  };
  copyBtn("row-style", "Style", "o Style", () => recomposedStyle(song));
  copyBtn("row-lyrics", "Lyrics", "a Lyrics", () => song.lyrics || "");
  const u = document.createElement("button");
  u.type = "button"; u.className = "row-used"; u.textContent = "✓";
  u.setAttribute("aria-pressed", isUsed(song.id) ? "true" : "false");
  u.setAttribute("aria-label", "Usei " + song.title);
  u.title = "Marcar ou desmarcar «usei»";
  u.addEventListener("click", () => {
    toggleUsed(song.id);
    const y = window.scrollY; render(); window.scrollTo(0, y);
    const again = document.querySelector('#main li.row[data-id="' + CSS.escape(song.id) + '"] .row-used');
    if (again) again.focus({ preventScroll: true });
  });
  li.appendChild(u);
  // Clique no resto da linha (estado, BPM, saude) tambem abre; o teclado usa o titulo.
  li.addEventListener("click", e => { if (!e.target.closest("button")) openDetail(song.id); });
  return li;
}

/** O que muda no cartao (modulo, BPM) chega a linha sem redesenhar a Lista. */
function updateRow(song) {
  const li = document.querySelector('#main li.row[data-id="' + CSS.escape(song.id) + '"]');
  if (!li) return;
  li.querySelector(".row-bpm").textContent = bpmText(song);
  fillHealth(li.querySelector(".row-health"), song);
}

const rowButtons = () => [...document.querySelectorAll("#main .row-open")];
const rowIds = () => [...document.querySelectorAll("#main li.row")].map(li => li.dataset.id);
const rowButton = id => document.querySelector('#main li.row[data-id="' + CSS.escape(id) + '"] .row-open');
function hashId() {
  const m = /^#faixa=(.+)$/.exec(location.hash);
  if (!m) return null;
  try { return decodeURIComponent(m[1]); } catch (e) { return null; }
}
function clearHash() { if (location.hash) history.replaceState(null, "", location.pathname + location.search); }

/** Abre (ou troca) a faixa do detalhe. A primeira abertura empilha #faixa=<id>
    no historico, para o «Voltar» fechar; trocar com ‹ › so substitui. Aberto
    pelo endereco (recarregar), nada e empilhado: fechar so limpa o endereco. */
function openDetail(id, opts = {}) {
  if (currentView() !== "list" || !locateSong(id)) return;
  const was = App.detailId;
  App.detailId = id;
  const h = "#faixa=" + encodeURIComponent(id);
  if (!opts.fromHistory) {
    if (!was && !opts.fromHash) { history.pushState(null, "", h); App.detailPushed = true; }
    else if (location.hash !== h) history.replaceState(null, "", h);
  }
  document.getElementById("detail").hidden = false;
  document.body.classList.add("detail-open");
  renderDetail();
  if (!was && isMobile()) document.getElementById("detail-back").focus();
}
function closeDetail(opts = {}) {
  const id = App.detailId;
  if (!id) return;
  App.detailId = null; App.detailHtml = null;
  document.getElementById("detail").hidden = true;
  document.body.classList.remove("detail-open");
  document.getElementById("detail-body").textContent = "";
  markOpenRow();
  if (opts.fromHistory) App.detailPushed = false;
  else if (App.detailPushed) { App.detailPushed = false; history.back(); }
  else clearHash();
  if (!opts.noFocus) { const b = rowButton(id); if (b) b.focus({ preventScroll: true }); }
}
function markOpenRow() {
  document.querySelectorAll("#main li.row").forEach(li => {
    const on = li.dataset.id === App.detailId;
    li.classList.toggle("is-open", on);
    if (on) li.setAttribute("aria-current", "true"); else li.removeAttribute("aria-current");
    li.querySelector(".row-open").setAttribute("aria-expanded", on ? "true" : "false");
  });
}
/** Redesenha o detalhe. Se o cartao novo sai igual ao que foi desenhado, o atual
    fica (e com ele o que a pessoa abriu, como os modulos); senao, troca. */
function renderDetail() {
  const id = App.detailId, loc = id && locateSong(id);
  if (!loc) return;
  const song = loc.album.songs[loc.index];
  const body = document.getElementById("detail-body");
  const fresh = renderCard(song), html = fresh.outerHTML;
  const same = App.detailShown === id;
  if (!(same && App.detailHtml === html && body.firstChild)) {
    const y = same ? body.scrollTop : 0;
    body.textContent = ""; body.appendChild(fresh); body.scrollTop = y;
    App.detailHtml = html; App.detailShown = id;
  }
  const ids = rowIds(), i = ids.indexOf(id);
  const inAlbum = (loc.album.songs || []).filter(s => ids.includes(s.id));
  App.detailPos = i;
  document.getElementById("detail-ctx").textContent = loc.album.title + " · " +
    (i >= 0 ? (inAlbum.findIndex(s => s.id === id) + 1) + " de " + inAlbum.length : "fora do filtro");
  document.getElementById("detail-prev").disabled = i <= 0;
  document.getElementById("detail-next").disabled = i < 0 || i >= ids.length - 1;
  markOpenRow();
}
function stepDetail(d) {
  const ids = rowIds(), i = ids.indexOf(App.detailId);
  if (i < 0 || !ids[i + d]) return;
  openDetail(ids[i + d]);
  const b = rowButton(ids[i + d]);
  if (b && !isMobile()) { b.focus({ preventScroll: true }); b.scrollIntoView({ block: "nearest" }); }
}
/** ↑ / ↓ com o foco num titulo: vai ao titulo vizinho, atravessando albuns. */
function stepRow(btn, d) {
  const all = rowButtons(), next = all[all.indexOf(btn) + d];
  if (!next) return;
  next.focus();
  next.scrollIntoView({ block: "nearest" });
  if (App.detailId) openDetail(next.closest("li").dataset.id);
}
/** Fecho do render() na Lista: o detalhe acompanha a lista nova. A faixa aberta
    que saiu do acervo (excluida) fecha o detalhe e leva o foco a linha seguinte. */
function afterListRender() {
  if (!App.detailId) return;
  if (!locateSong(App.detailId)) {
    const i = App.detailPos || 0;
    closeDetail({ noFocus: true });
    const all = rowButtons(), b = all[Math.min(i, all.length - 1)];
    if (b) b.focus({ preventScroll: true });
    return;
  }
  renderDetail();
}
/** Primeira Lista com acervo: um #faixa=<id> no endereco reabre aquela faixa. */
function openFromHash() {
  if (App.hashTried || !App.collection) return;
  App.hashTried = true;
  const id = hashId();
  if (!id) return;
  if (currentView() === "list" && locateSong(id)) openDetail(id, { fromHash: true });
  else clearHash();
}

/** A lateral: «Todas as faixas» e os albuns, com a contagem que passa nos OUTROS
    filtros (estado, uso, busca). Clicar poe o filtro de album, o mesmo do painel. */
function renderSide(f) {
  const side = document.getElementById("side");
  side.hidden = !App.collection;
  if (!App.collection) return;
  const ul = document.getElementById("side-albums");
  ul.textContent = "";
  const item = (title, n, id) => {
    const li = document.createElement("li");
    const b = document.createElement("button");
    b.type = "button"; b.className = "side-item" + (n ? "" : " empty-album");
    if ((f.album || "") === id) b.setAttribute("aria-current", "true");
    const t = document.createElement("span"); t.className = "t"; t.textContent = title;
    const c = document.createElement("span"); c.className = "n"; c.textContent = n;
    b.appendChild(t); b.appendChild(c);
    b.addEventListener("click", () => { document.getElementById("filter-album").value = id; render(); });
    li.appendChild(b); ul.appendChild(li);
  };
  const albums = App.collection.albums || [];
  const counts = albums.map(a => (a.songs || []).filter(s => songMatches(s, f)).length);
  item("Todas as faixas", counts.reduce((x, y) => x + y, 0), "");
  albums.forEach((a, i) => item(a.title, counts[i], a.id));
}
/** Os acervos guardados na lateral, como no seletor; o aberto marcado. Le o
    banco so com a lateral visivel e quando algo mudou (aberto, quantos, data):
    dbAll traz os acervos inteiros, e o setOrigin roda a cada troca. */
const SIDE_MQ = window.matchMedia("(min-width: 1280px)");
let sideKey = null;
async function renderSideAcervos() {
  if (!SIDE_MQ.matches) { sideKey = null; return; }
  const key = [App.source, Store.count, App.savedAt, !!App.collection].join("|");
  if (key === sideKey) return;
  sideKey = key;
  const ul = document.getElementById("side-acervos");
  let recs = [];
  if (Store.db) { try { recs = await dbAll(); } catch (e) { recs = []; } }
  if (!recs.length && App.collection) recs = [{ source: App.source, title: App.collection.title, json: App.collection }];
  recs.sort((a, b) => String(b.savedAt || "").localeCompare(String(a.savedAt || "")));
  ul.textContent = "";
  recs.forEach(r => {
    const li = document.createElement("li");
    const b = document.createElement("button");
    b.type = "button"; b.className = "side-item"; b.dataset.source = r.source || "";
    const open = r.source === App.source;
    if (open) b.setAttribute("aria-current", "true");
    const t = document.createElement("span"); t.className = "t"; t.textContent = r.title || r.source;
    const c = document.createElement("span"); c.className = "n";
    c.textContent = open ? "aberto" : String(((r.json && r.json.albums) || []).reduce((n, a) => n + (a.songs || []).length, 0));
    b.appendChild(t); b.appendChild(c);
    if (!open) b.addEventListener("click", async () => {
      let rec = null;
      try { rec = await dbGet(r.source); } catch (e) { /* trata abaixo */ }
      if (!rec || !openRecord(rec)) { toast("Não consegui abrir " + r.source); return; }
      toast("Acervo aberto: " + (rec.json.title || rec.source) + moduleRefsNotice(rec.json));
    });
    li.appendChild(b); ul.appendChild(li);
  });
}

if (SIDE_MQ.addEventListener) SIDE_MQ.addEventListener("change", () => renderSideAcervos());
document.getElementById("view-list").addEventListener("click", () => setView("list"));
document.getElementById("view-cards").addEventListener("click", () => setView("cards"));
document.getElementById("menu-view-list").addEventListener("click", () => setView("list"));
document.getElementById("menu-view-cards").addEventListener("click", () => setView("cards"));
document.getElementById("detail-close").addEventListener("click", () => closeDetail());
document.getElementById("detail-back").addEventListener("click", () => closeDetail());
document.getElementById("detail-prev").addEventListener("click", () => stepDetail(-1));
document.getElementById("detail-next").addEventListener("click", () => stepDetail(1));
const detailSong = () => { const l = App.detailId && locateSong(App.detailId); return l ? l.album.songs[l.index] : null; };
document.getElementById("detail-copy-style").addEventListener("click", e => { const s = detailSong(); if (s) copyText(recomposedStyle(s), e.currentTarget); });
document.getElementById("detail-copy-lyrics").addEventListener("click", e => { const s = detailSong(); if (s) copyText(s.lyrics || "", e.currentTarget); });
document.getElementById("detail-copy-title").addEventListener("click", e => { const s = detailSong(); if (s) copyText(s.title, e.currentTarget); });
window.addEventListener("popstate", () => {
  const id = hashId();
  if (id && App.collection && locateSong(id)) openDetail(id, { fromHistory: true });
  else {
    closeDetail({ fromHistory: true });
    if (id) clearHash();   // um #faixa= que nao existe neste acervo e ignorado, e o endereco fica limpo
  }
});
document.addEventListener("keydown", e => {
  const t = e.target;
  if ((e.key === "ArrowDown" || e.key === "ArrowUp") && t && t.classList && t.classList.contains("row-open")) {
    e.preventDefault(); stepRow(t, e.key === "ArrowDown" ? 1 : -1); return;
  }
  // Esc fecha o detalhe so quando nada na frente dele pede o Esc: um painel da
  // barra (o ouvinte da I1 fecha primeiro), uma janela ou a busca do celular.
  if (e.key === "Escape" && App.detailId && !openPop && !e.defaultPrevented && !document.querySelector("dialog[open]")
      && !(t && t.id === "search" && isMobile())) {
    e.preventDefault(); closeDetail();
  }
});
// --top-h: a altura do #top, medida (48 px sem etiquetas, 84 com, mais o aviso).
(() => {
  const top = document.getElementById("top");
  const set = () => document.documentElement.style.setProperty("--top-h", top.offsetHeight + "px");
  set();
  if ("ResizeObserver" in window) new ResizeObserver(set).observe(top);
})();
document.getElementById("tour15").hidden = !!App.ui.tour15;
document.getElementById("tour15-ok").addEventListener("click", () => {
  App.ui.tour15 = true; saveUiState();
  document.getElementById("tour15").hidden = true;
});
syncView();

// A abertura e assincrona (IndexedDB); a importacao espera por ela.
````

### E17 — CHANGELOG: 0.15.0 — `meta/CHANGELOG.md`

**Ancora, literal:**

````
## [0.14.0] — 2026-11-05
````

**Texto novo, literal:**

````
## [0.15.0] — 2026-11-06

Segunda entrega da frente de interface (I2, DEC-030, DEC-031): as faixas numa lista, com o cartão ao lado da escolhida. O cartão não muda.

### Added
- **Visão Lista** (a padrão) e **Cartões** (a de antes), num par de botões na barra; no celular, no «⋯». A escolha fica no navegador (`view` em `cancioneiro:ui`).
- **A lista:** uma linha de 44 px por faixa, agrupada por álbum, com o cabeçalho do álbum fixo ao rolar. Colunas: título, estado, idioma, BPM, saúde e os botões **Style**, **Lyrics** e ✓ «usei». Os dois botões copiam só o conteúdo, o Style recomposto na hora, igual ao «copiar» do cartão.
- **Saúde da faixa:** o pior nível do painel de qualidade do cartão, com marca e texto («● tudo dentro», «▲ Style 12 tags», «■ Lyrics passa de 5.000»).
- **O detalhe à direita:** clicar no título abre o cartão de hoje ao lado da lista, com ‹ › para andar pela lista filtrada e × ou `Esc` para fechar. `↓` e `↑` no título andam de faixa. O endereço guarda a faixa (`#faixa=<id>`): recarregar reabre, e o «Voltar» do navegador fecha. Entre 720 e 959 px, o detalhe abre por cima da lista.
- **A lateral** (a partir de 1280 px): os álbuns, com a contagem dos outros filtros (clicar filtra), e os acervos guardados (clicar abre).
- **Celular:** linhas de 64 px com o ✓ de 44; o detalhe em tela cheia, com «Copiar Style», «Copiar Lyrics» e «Título» fixos no pé; voltar devolve a lista na mesma rolagem.
- Um aviso de uma linha na primeira abertura diz onde está cada coisa (`tour15`).

### Changed
- Na Lista, clicar no título da faixa abre o detalhe; copiar o título fica no cartão, como antes. Em Cartões, nada muda.
- Abaixo de 1180 px de largura, o nome «Cancioneiro» sai da barra para caber o par Lista | Cartões; a versão segue no «⋯».

Spec `meta/specs/261106-lista-e-detalhe.md`: 15 de 15 critérios no Chromium headless, com prova de vida no app da 0.14.0; a Lista de 300 faixas desenha em cerca de 50 ms. Os testes das entregas 1 a 3 e da I1 seguem em 15 de 15, 25 de 25, 19 de 19 e 14 de 14, rodados em Cartões onde medem o cartão.

---

## [0.14.0] — 2026-11-05
````

### E18 — README: versao — `README.md`

**Ancora, literal:**

````
> **Estado:** v0.14.0 — ferramenta em uso. Lê, guarda e edita vários acervos, copia por campo, troca módulos de estilo, ajusta o BPM, **mede cada prompt contra os limites do Suno**, exporta Markdown, exporta uma faixa como `.json` e **entrega o prompt para chats gerarem canções no esquema**. Publicada no GitHub Pages. Ver `meta/ROADMAP.md`.
````

**Texto novo, literal:**

````
> **Estado:** v0.15.0 — ferramenta em uso. Lê, guarda e edita vários acervos, copia por campo, troca módulos de estilo, ajusta o BPM, **mede cada prompt contra os limites do Suno**, exporta Markdown, exporta uma faixa como `.json` e **entrega o prompt para chats gerarem canções no esquema**. Publicada no GitHub Pages. Ver `meta/ROADMAP.md`.
````

### E19 — README: a lista e o detalhe — `README.md`

**Ancora, literal:**

````
3. Navegue por álbuns, copie style e lyrics por botão e o título clicando nele, marque o que usou. *Filtros*, na barra, escolhe álbum, estado e uso; cada filtro ligado vira uma etiqueta com ×, e a tecla `/` leva à busca. Em *Estrutura do cartão* (no «⋯», à direita da barra), arraste os blocos para mudar a ordem e esconda os que você não usa (o Exclude já vem oculto: o formulário gratuito do Suno v6 não tem o campo).
````

**Texto novo, literal:**

````
3. As faixas aparecem numa **lista**, uma por linha, agrupadas por álbum: copie o Style ou a Lyrics pelos botões da linha, marque o que usou no ✓ e veja a saúde do prompt (● dentro, ▲ atenção, ■ o Suno vai cortar). Clique no título para abrir o **cartão** ao lado, com tudo o que ele tem; ‹ › e as setas ↑ ↓ andam de faixa, e o endereço guarda a aberta. *Cartões*, na barra, volta à grade de antes, onde clicar no título copia o título. Na lateral (em telas largas), clique num álbum para filtrar ou noutro acervo para abri-lo. *Filtros*, na barra, escolhe álbum, estado e uso; cada filtro ligado vira uma etiqueta com ×, e a tecla `/` leva à busca. Em *Estrutura do cartão* (no «⋯», à direita da barra), arraste os blocos para mudar a ordem e esconda os que você não usa (o Exclude já vem oculto: o formulário gratuito do Suno v6 não tem o campo).
````

### E20 — README: DEC-031 na lista — `README.md`

**Ancora, literal:**

````
O acervo canônico são **arquivos JSON** no esquema: os exemplos versionados em `data/`, e o acervo pessoal fora do repo (DEC-026). O navegador guarda **cópias dos acervos importados** (IndexedDB) e, no localStorage, as marcações por acervo e a estrutura do cartão — cache, nunca a fonte: o menu do seletor de acervo diz de onde a cópia veio e quando, e *Esquecer este acervo* a apaga sem tocar no arquivo. Com *editar*, a cópia vira rascunho até você salvar o `.json` e substituir o arquivo. Ver `meta/DECISIONS.md` (DEC-004, DEC-022, DEC-028, DEC-029, DEC-030).
````

**Texto novo, literal:**

````
O acervo canônico são **arquivos JSON** no esquema: os exemplos versionados em `data/`, e o acervo pessoal fora do repo (DEC-026). O navegador guarda **cópias dos acervos importados** (IndexedDB) e, no localStorage, as marcações por acervo e a estrutura do cartão — cache, nunca a fonte: o menu do seletor de acervo diz de onde a cópia veio e quando, e *Esquecer este acervo* a apaga sem tocar no arquivo. Com *editar*, a cópia vira rascunho até você salvar o `.json` e substituir o arquivo. Ver `meta/DECISIONS.md` (DEC-004, DEC-022, DEC-028, DEC-029, DEC-030, DEC-031).
````

### E21 — DECISIONS: DEC-031 — `meta/DECISIONS.md`

**Ancora, literal:**

````
**Consequências:** (+) A I1 sozinha já devolve o espaço do topo e deixa os filtros à vista ao rolar. (+) Cada entrega é usável sozinha. (−) A I3 soma uns 45 KB de biblioteca: medir o tempo de abertura no `file://` antes e depois. (−) Com duas visões (Lista e Cartões), toda saída nova reverifica a regra de domínio nas duas. (−) Sem o interruptor, o clique errado fica mais fácil; é o «Desfazer» que segura isso, e o teste da I3 mede o falso positivo (soltar no mesmo lugar não conta alteração).
````

**Texto novo, literal:**

````
**Consequências:** (+) A I1 sozinha já devolve o espaço do topo e deixa os filtros à vista ao rolar. (+) Cada entrega é usável sozinha. (−) A I3 soma uns 45 KB de biblioteca: medir o tempo de abertura no `file://` antes e depois. (−) Com duas visões (Lista e Cartões), toda saída nova reverifica a regra de domínio nas duas. (−) Sem o interruptor, o clique errado fica mais fácil; é o «Desfazer» que segura isso, e o teste da I3 mede o falso positivo (soltar no mesmo lugar não conta alteração).

## DEC-031 — I2: Lista por padrão, celular sem gaveta, título da linha abre o detalhe

**Data:** 2026-11-06
**Status:** aceita
**Contexto:** A spec da I2 (`meta/specs/261106-lista-e-detalhe.md`) trouxe três pontos para o dono, e um deles contraria a análise da frente, que previa uma gaveta da lateral no celular. Decididos por ele em 2026-11-06, os três como recomendados.
**Decisão:**
- **Sem escolha guardada, o app abre em Lista.** Cartões continua a um clique, e a escolha fica no navegador.
- **No celular, sem lateral nem gaveta.** O álbum se escolhe em Filtros, e o acervo, no seletor; a gaveta seria um terceiro caminho para o mesmo lugar, num quinto botão de uma barra de 390 px.
- **Na Lista, o título da linha abre o detalhe.** Copiar o título fica no cartão do detalhe, como sempre; em Cartões, nada muda.
**Alternativas consideradas:** abrir em Cartões (o costume); a gaveta da análise; o título copiar e um botão «abrir» à parte (mais um alvo por linha).
**Consequências:** (+) A I2 entrega o ganho dela já na primeira abertura. (−) Quem copiava o título pelo clique na Lista passa a abrir o detalhe; o aviso da primeira abertura diz onde está cada coisa. (−) Se a gaveta fizer falta no celular, ela volta como ideia.
````

### E22 — IDEAS: i-046 entregue (1) — `meta/IDEAS.md`

**Ancora, literal:**

````
### i-046 🔨 Filtros que acompanham a rolagem, e visões do acervo
````

**Texto novo, literal:**

````
### i-046 ✅ Filtros que acompanham a rolagem, e visões do acervo
````

### E23 — IDEAS: i-046 entregue (2) — `meta/IDEAS.md`

**Ancora, literal:**

````
**Em andamento (DEC-030):** os filtros fixos, num painel, com etiquetas removíveis e «N de M», entraram na I1 (0.14.0). As visões (Lista e Cartões, com o detalhe à direita) são a I2.
````

**Texto novo, literal:**

````
**Entregue (DEC-030, DEC-031):** os filtros fixos, num painel, com etiquetas removíveis e «N de M», entraram na I1 (0.14.0); as visões Lista e Cartões, com o detalhe à direita, na I2 (0.15.0). A tabela no estilo Airtable (opção C da análise) e ordenar por coluna ficaram de fora; voltam como ideia se fizerem falta.
````

### E24 — IDEAS: i-047 em andamento (1) — `meta/IDEAS.md`

**Ancora, literal:**

````
### i-047 💡 Painel lateral com abas
````

**Texto novo, literal:**

````
### i-047 🔨 Painel lateral com abas
````

### E25 — IDEAS: i-047 em andamento (2) — `meta/IDEAS.md`

**Ancora, literal:**

````
**Planejada (DEC-030):** a lateral de álbuns e acervos é a I2 (0.15.0).
````

**Texto novo, literal:**

````
**Em andamento (DEC-030, DEC-031):** a lateral de álbuns e acervos entrou na I2 (0.15.0), à esquerda e sem abas, a partir de 1280 px; o detalhe da faixa é o painel da direita. Em aberto: as abas no estilo de «bookmarks» do pedido e a lateral no celular (sem gaveta, por decisão do dono).
````

### E26 — ROADMAP: I2 entregue — `meta/ROADMAP.md`

**Ancora, literal:**

````
- 🔨 Frente de interface (i-043 a i-048, DEC-030), em quatro entregas: ✅ barra única, com o seletor de acervo, os filtros com etiquetas e o «⋯» (0.14.0) · ⬜ lista e detalhe, com a lateral de álbuns e acervos (0.15.0) · ⬜ organizar: arrastar, «⋯» por faixa, lote, «Desfazer», sem o interruptor «editar» (0.16.0) · ⬜ salvar direto no arquivo (0.17.0, i-043).
````

**Texto novo, literal:**

````
- 🔨 Frente de interface (i-043 a i-048, DEC-030), em quatro entregas: ✅ barra única, com o seletor de acervo, os filtros com etiquetas e o «⋯» (0.14.0) · ✅ lista e detalhe, com a lateral de álbuns e acervos (0.15.0) · ⬜ organizar: arrastar, «⋯» por faixa, lote, «Desfazer», sem o interruptor «editar» (0.16.0) · ⬜ salvar direto no arquivo (0.17.0, i-043).
````

### E27 — STATUS inteiro — `meta/STATUS.md`

**Arquivo inteiro, literal** (substitui o arquivo; chegada `2853814f26e882371eafbb6b6919e1d8ca4c560a`):

````
# STATUS.md — Cancioneiro

> **O agora.** O que funciona, o que está em progresso, o que está quebrado, backlog curto.
> Rolante: item resolvido sai daqui e vai para o CHANGELOG. Médio/longo prazo vive no ROADMAP.

**Versão atual:** 0.15.0 · **Fase:** 3a, 3a.2, o BPM da 3b, o prompt-modelo e as conveniências de uso concluídos e conferidos · os álbuns antigos convertidos (i-008, fora do repo) · curadoria no app concluída nas três entregas (DEC-028, DEC-029) · frente de interface na I2 de quatro (DEC-030, DEC-031) · kit de música lido pelo KCM, à espera da resposta (i-039)

---

## Última conversa (2026-11-06, I2: protótipo, spec e implementação, WO 0026)

- **I1 conferida na tela pelo dono** (roteiro OK `[relatado pelo dono]`): a barra única (0.14.0) está fechada.
- **I2, lista e detalhe (0.15.0):** protótipo no canvas «Cancioneiro: nova interface» (fileira da I2), spec `meta/specs/261106-lista-e-detalhe.md` e os três pontos decididos pelo dono como recomendados (DEC-031): Lista por padrão, celular sem gaveta, título da linha abre o detalhe. 15 de 15 critérios no Chromium headless, testados pelo chat.
- **Este bloco substitui o anterior, da WO 0025** (I1). O que ele dizia está no CHANGELOG [0.14.0], na spec `meta/specs/261105-barra-unica.md` e em `logs/2026-11-05.md` (Conversas 8 a 10).

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
- **Lista e detalhe** (0.15.0, DEC-030, DEC-031): Lista (padrão) ou Cartões; uma linha por faixa com Style, Lyrics, ✓ e a saúde do prompt; o cartão de hoje ao lado, com ‹ ›, setas e `#faixa=<id>` no endereço; a lateral de álbuns e acervos a partir de 1280 px; no celular, o detalhe em tela própria com os botões de copiar no pé.
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

- **Conferir a I2 na tela** — roteiro na conversa de 2026-11-06 (WO 0026), depois do push, no computador e no celular.
- **Instalar o validador de esquema nesta máquina.** Sem `jsonschema` e `referencing`, o `validate.py` só confere sintaxe e diz `ESQUEMA NAO CONFERIDO` na última linha. Uma vez, no CMD: `pip install jsonschema referencing --break-system-packages`. Depois, `python3 scripts/validate.py` deve terminar em `Tudo conforme ao esquema.`

## Backlog curto (próximas ações concretas)

1. **I3 — Organizar** (i-048, DEC-030) — protótipo navegável no canvas, depois spec: a alça ⋮⋮ com o SortableJS 1.15.7 embutido, o «⋯» por faixa como caminho sem arrastar, a seleção em lote, o «Desfazer» e o fim do interruptor «editar».
2. **I4 — Salvar no arquivo** (i-043), depois da I3, com protótipo e spec.
3. **Rampa de BPM** (i-042) — três faixas BR reprovam no `validate.py` por mudarem de andamento de propósito.
4. **Pesquisar outras plataformas de música por IA** (i-032) — um turno de pesquisa antes de qualquer mudança de esquema.
5. **Avisar palavra de andamento que contradiz o BPM** (i-029) — pede uma tabela palavra → faixa de BPM, com fonte e data.
6. **Importar prompts prontos dos álbuns como módulos** — o último ⬜ da 3b no ROADMAP; o índice-mestre da BR e os «estilos originais» do VOL5 trazem fórmulas de estilo.

## Notas de estado

- **Repo local do dono:** `C:\Users\alexk\Tools\cancioneiro\cancioneiro` (Windows). O chat lê e grava na pasta vinculada; commit e push são do Code (DEC-010). A pasta-pai guarda relatórios, notas e o acervo do dono, fora do Git; o lido vai para `../notas-arquivadas/`.
- **Canal:** pasta vinculada é o padrão; a cópia achatada (FlatDrop) é reserva (DEC-017).
- **Limites do Suno:** o v6 saiu em 2026-09-09 e a nota oficial não documenta limite de campo; os números do painel vêm de fonte secundária, com fonte e data no `QUALITY_LIMITS` (DEC-018). Outra fonte secundária (2026-08) põe o ideal em 4 a 7 descritores; o prompt usa 6 a 8. Reconferir quando houver documentação oficial. O `meta/HISTORY.md` §5 ganhou a interface do v6 vista na conta (2026-10-29); o resto do arquivo ainda descreve o v5.5.
- **Exclude no v6-mini:** o formulário gratuito não tem o campo (capturas de 2026-10-29). Desde a 0.9.1 (DEC-025) o bloco vem oculto por padrão, com o aviso «no X → Exclude» junto (D3); o dado continua no JSON e no export. Quem usa o campo liga em «Estrutura».
- **Navegador (DEC-004, DEC-022, DEC-028):** guarda as cópias dos acervos importados (IndexedDB, banco `cancioneiro`), as marcas «usei» por acervo e a estrutura do cartão (`localStorage`, `cancioneiro:ui`). As cópias são cache: se o arquivo mudou fora, importe de novo; o menu do seletor de acervo diz quando a cópia foi feita. Os avisos de primeira abertura guardam `tour14` (0.14.0) e `tour15` (0.15.0), e a visão escolhida, `view`, no mesmo `cancioneiro:ui`.
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

- A I3 (alca, arrastar, selecao em lote, «⋯» por faixa, «Desfazer», o fim do interruptor «editar») e a I4 (salvar no arquivo). O SortableJS **nao** entra nesta WO.
- Spec, CONTEXT e log: ja gravados pelo chat; nao edite.
- Nada em `data/`, `schema/`, `scripts/` ou `kit-musica/`.

## Armadilhas desta WO

- **`autocrlf=true` na maquina do dono:** os hashes valem no disco em LF, antes do `add`. Nao rode `git checkout -- <arquivo>`: ele regrava em CRLF.
- **A E01 e a E16 sao longas** (o CSS da lista, da lateral e do detalhe; o bloco de codigo da I2, antes de «A abertura e assincrona»): se o aplicador ler ancora linha a linha, compare o bloco inteiro; o hash de chegada do `app/index.html` e a prova.
- **A E06 e a E07 abrem e fecham um `<div class="shell">`** em volta do `<main>`: as duas vao juntas.
- **O `validate.py` desta maquina termina em `ESQUEMA NAO CONFERIDO`** (falta `jsonschema`): estado conhecido.
- **Os testes escrevem no stderr:** use `2>&1 >/dev/null | tail -1`.

## Depois de aplicar — conferencia antes do commit

| # | Checagem | Comando | Esperado |
|---|---|---|---|
| 1 | **Os dez arquivos sao os testados** | `sha1sum app/index.html README.md meta/CHANGELOG.md meta/DECISIONS.md meta/IDEAS.md meta/ROADMAP.md meta/STATUS.md meta/specs/261106-lista-e-detalhe.md meta/CONTEXT.md logs/2026-11-06.md` | a coluna **chegada**, os dez. **Prova as 27 edicoes.** |
| 2 | Validacao | `python3 scripts/validate.py; echo "exit=$?"` | `exit=0`, com a linha `OK  versao 0.15.0 igual em CHANGELOG, app, README e STATUS`; ultima linha `Tudo conforme ao esquema.` ou `ESQUEMA NAO CONFERIDO (...)` (esta maquina) |
| 3 | Os conversores seguem passando | `python3 scripts/test_convert_br.py 2>&1 >/dev/null \| tail -1` e `python3 scripts/test_convert_guides.py 2>&1 >/dev/null \| tail -1` | `OK` e `OK` |
| 4 | O codigo novo | `grep -c '^function renderRow' app/index.html`, `grep -c '^function openDetail' app/index.html`, `grep -c 'id="detail"' app/index.html` | `1`, `1`, `1` |
| 5 | O registro | `grep -m1 '^## \[' meta/CHANGELOG.md`, `grep -c '^## DEC-031 ' meta/DECISIONS.md`, `grep -c '^### i-046 ✅' meta/IDEAS.md` | `## [0.15.0] — 2026-11-06`, `1`, `1` |
| 6 | A pendencia resolvida saiu | `grep -c '^- \*\*Conferir a I1 na tela' meta/STATUS.md`, `grep -c '^- \*\*Conferir a I2 na tela' meta/STATUS.md` | `0`, `1` |
| 7 | Nada alem do previsto | `GIT_OPTIONAL_LOCKS=0 git status --short --untracked-files=all` | os dez arquivos e esta WO, e nada mais (nenhum `.txt`, nenhum `__pycache__`) |

**Os tres campos de cada passo:** as sete sao rodadas por **quem aplica (o Code)**, na raiz do repo, em Git Bash,
com `LC_ALL=C.UTF-8`. **Chega no ramo?** A checagem 1 cobre os dez arquivos inteiros, inclusive o `app/index.html`
que o chat executou (`render`, `renderRow`, `songHealth`, `openDetail`, `closeDetail`, `renderSide`, `refreshCardStyle`).
**Esta e qual pergunta?** A 2 e a 3 respondem «funciona?»; as outras, «esta la?». O «funciona?» da lista no
navegador do dono e dele, depois do push, pelo roteiro do chat.

## Relatorio de aplicacao

Grave em `../261106-HHMM-code-cancioneiro-apply-wo0026.txt`, com o `HHMM` de `date +%y%m%d-%H%M` rodado na
hora. Diga o resultado da checagem 1 em primeiro lugar.

**Proximo comando** (ultima linha do relatorio, cru e sozinho):

```
/wrap
```

## Commit

```
git add app/index.html README.md meta/CHANGELOG.md meta/DECISIONS.md meta/IDEAS.md meta/ROADMAP.md meta/STATUS.md meta/specs meta/CONTEXT.md logs/2026-11-06.md meta/workorders
```

```
git commit -m "feat: lista e detalhe, versao 0.15.0" -m "Frente de interface, entrega I2 (DEC-030, DEC-031): visao Lista por padrao, uma linha por faixa com Style, Lyrics, usei e a saude do prompt; o cartao de hoje no detalhe a direita, com setas e o endereco #faixa=; lateral de albuns e acervos a partir de 1280 px; no celular, detalhe em tela propria. Spec com o resultado, CONTEXT, IDEAS (i-046, i-047), ROADMAP, README, STATUS inteiro."
```

```
git push
```
