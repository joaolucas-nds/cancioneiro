# WO 0048 — Clique direito, lateral em duas areas e o aviso do arraste (0.23.0)

## Cabecalho

> **Tipo:** versao 0.23.0 — app, um teste ajustado, um arquivo de teste novo e meta (DEC-041); o log do dia ja gravado pelo chat.
> **Config sugerida:** Sonnet · `/effort medium` (aplicacao literal por script; muitas edicoes).
> **Pre-requisito:** commit `a6aa20a`, branch `main`, sincronizada com `origin/main`. O `git status --short` mostra exatamente: `?? logs/2026-11-17.md` e `?? meta/workorders/261117-wo0048-clique-direito-e-lateral-0-23-0.md`.
> **Base:** a nota do dono `261117-0934.txt` (o roteiro da 0.22.0 e quatro pedidos, `[relatado pelo dono]`) e a DEC-041, nesta WO. O chat implementou e mediu num clone (log de 2026-11-17).
> **Depende de:** `a6aa20a` (WO 0047).
>
> | arquivo | partida (sha1) | chegada (sha1) |
> |---|---|---|
> | `app/index.html` | `487ccf8557eeee7b80918edb34c07c21174d7259` | `89cc791dd170b25197d5ebcf7a0bfb3695517f44` |
> | `tests/test_varios_json.py` | `9c02548a1ed59b4740033eb2f96d38c923417923` | `aeb5aec4bfe1518c715eb58e63ef202aed7ccc40` |
> | `README.md` | `08c81f43513966521f509eb8be99d254799b7fbc` | `97bb0e3aec45c1f4e1eb1f879939c49bf654f450` |
> | `meta/CHANGELOG.md` | `0d33e30459f1aaa8a78516695144272a0bcfdf02` | `1d2deb8b727367d2a8c4dca6e2a9ea9ac290650a` |
> | `meta/STATUS.md` | `f4338e9704ebc98d17d3391e80cf65b0cde20bfe` | `3fc328fd3ad3093caf7c32a1bb8434e1f431f268` |
> | `meta/IDEAS.md` | `7b29f58d958fb2f8b935ba083f92181cf3031b67` | `57aeff225c9fcb779372a53be44406b2b057db3d` |
> | `meta/DECISIONS.md` | `3027c30b6934263e20527a69701e802bf688ef1c` | `5ebada216caa8ad731bbed96715e375761ee9015` |
> | `tests/test_lateral_e_menus.py` | (nao existe) | `a4444a68f418a5c726668c6e95f2642b3e23d4cc` (arquivo novo, E31) |
> | `logs/2026-11-17.md` | `45d11e3e06bec7fa6f702956261c8baf8629a108` | o mesmo (gravado pelo chat; so versionar) |
>
> **Ancora semantica:** se um trecho-ancora nao bater EXATAMENTE, PARE e reporte.
> **Idempotencia:** antes de cada edicao, procure o texto NOVO INTEIRO; se ja estiver la, PULE e diga no relatorio.
> **Ancoras:** linhas inteiras (uma linha ou um bloco de linhas inteiras), cada uma 1 vez no arquivo no momento da edicao, na ordem abaixo. Toda edicao «substitui a ancora inteira».
> **Âncoras lidas em** (lidas pelo chat NESTE turno, de `a6aa20a` clonado do GitHub e conferido contra o disco do dono — a lista dos versionados com o mesmo sha1; aplicadas em ordem num clone, por um extrator que le so esta WO, com a chegada medida byte a byte):
> - E01 (`app/index.html`, lateral: as duas areas (CSS)): bloco de 4 linhas, começando por `    height: calc(100vh - var(--top-h)); overflow: auto; padding: 12px 8px; border-rig…`
> - E02 (`app/index.html`, «+ Novo album» preso no fim da area): linha `  body.dragging-track .side-new-li { display: list-item; }`
> - E03 (`app/index.html`, CSS do menu do acervo): linha `  #track-pop, #album-pop { position: fixed; z-index: 40; width: 240px; }`
> - E04 (`app/index.html`, CSS dos botoes de opcao): linha `  .multi-list select { margin: 4px 0 0; }`
> - E05 (`app/index.html`, botoes de opcao no celular): bloco de 2 linhas, começando por `    .multi-dialog select, .multi-dialog input[type="text"], .multi-dialog button { mi…`
> - E06 (`app/index.html`, CSS: o aviso do arraste fora da lateral): bloco de 2 linhas, começando por `  body.dragging .drop-hint { display: flex; }`
> - E07 (`app/index.html`, versão 0.23.0): linha `    <span class="version" data-role="app-version">v0.22.0</span>`
> - E08 (`app/index.html`, lateral: as duas areas (HTML)): bloco de 4 linhas, começando por `  <div class="side-head">Álbuns</div>`
> - E09 (`app/index.html`, o menu do acervo (HTML)): bloco de 2 linhas, começando por `  <button type="button" role="menuitem" class="mobile-only" id="am-cancel">Cancelar</…`
> - E10 (`app/index.html`, o texto do aviso num span): linha `<div class="drop-hint" aria-hidden="true">Solte para importar</div>`
> - E11 (`app/index.html`, os botoes de opcao): bloco de 11 linhas, começando por `    const sel = document.createElement("select");`
> - E12 (`app/index.html`, a escolha muda pelo grupo): bloco de 4 linhas, começando por `      sel.addEventListener("change", () => { syncWarn(); syncDest(); });`
> - E13 (`app/index.html`, dragleave limpa a zona): linha `  if (!dragDepth) document.body.classList.remove("dragging");`
> - E14 (`app/index.html`, drop limpa a zona): linha `  e.preventDefault(); dragDepth = 0; document.body.classList.remove("dragging");`
> - E15 (`app/index.html`, o «⋯» do acervo e o clique direito): bloco de 3 linhas, começando por `    li.appendChild(b); ul.appendChild(li);`
> - E16 (`app/index.html`, a zona no body e o aviso da lateral): bloco de 4 linhas, começando por `  const n = Array.from(e.dataTransfer.items || []).filter(i => i.kind === "file").len…`
> - E17 (`app/index.html`, Esc fecha o menu do acervo): bloco de 2 linhas, começando por `    if (albumMenuFor) { e.preventDefault(); e.stopImmediatePropagation(); closeAlbumM…`
> - E18 (`tests/test_varios_json.py`, le os botoes de opcao): bloco de 4 linhas, começando por `    return page.eval_on_selector_all(`
> - E19 (`tests/test_varios_json.py`, clica em «Faixas no aberto»): linha `    page.select_option("#multi-list > li:first-child select", "tracks")`
> - E20 (`tests/test_varios_json.py`, o radio desligado): linha `    assert page.eval_on_selector_all("#multi-list option[value=tracks]", "e => e.map(…`
> - E21 (`tests/test_varios_json.py`, a altura dos botoes de opcao): linha `    small = page.eval_on_selector_all("#multi-dialog select, #multi-dialog button",`
> - E22 (`README.md`, estado v0.23.0): linha `> **Estado:** v0.22.0 — ferramenta em uso. Lê, guarda e edita vários acervos (importa…`
> - E23 (`README.md`, o clique direito e a lateral): linha `7. Para reorganizar, não há nada a ligar: na Lista, arraste a faixa pela alça ⋮⋮ (par…`
> - E24 (`meta/CHANGELOG.md`, entrada [0.23.0]): bloco de 2 linhas, começando por `> Histórico de versões entregues. SemVer + Keep a Changelog. Cresce no topo.`
> - E25 (`meta/STATUS.md`, versão e ultima conversa): bloco de 9 linhas, começando por `**Versão atual:** 0.22.0 · **Fase:** 3a, 3a.2, o BPM da 3b, o prompt-modelo e as conv…`
> - E26 (`meta/STATUS.md`, funciona: clique direito e lateral): linha `- **Importar vários '.json'** (0.22.0, DEC-040): soltar ou escolher vários abre «Impo…`
> - E27 (`meta/STATUS.md`, 91 testes): linha `- **Testes do navegador no CI** (DEC-034): 'tests/' (pytest e Playwright, 81 testes d…`
> - E28 (`meta/STATUS.md`, backlog: conferir a 0.23.0): linha `1. **Conferir a 0.22.0 na tela** (dono): o roteiro do log de 2026-11-16, Conversa 6. …`
> - E29 (`meta/IDEAS.md`, i-061 a i-064): bloco de 2 linhas, começando por ``
> - E30 (`meta/DECISIONS.md`, DEC-041 (no fim do arquivo)): linha `**Na implementação (0.22.0), o que a decisão deixou aberto:** os textos são os da spe…`
> **Canal dos meta neste ciclo = CODE:** STATUS, DECISIONS, IDEAS e CHANGELOG pelo Code (DEC-010); o log do dia ja esta gravado pelo chat.

---

## 1. Por que

Depois do roteiro da 0.22.0, o dono pediu quatro mudancas antes do recesso (i-061 a i-064): o aviso do arraste fora da lateral, botoes de opcao na janela de varios, o clique direito abrindo o «⋯» e a lateral com duas areas que rolam. O chat implementou num clone de `a6aa20a`: 91 testes verdes duas vezes (10 novos); os 7 de comportamento novo reprovam na 0.22.0 e os 3 de falso positivo passam nas duas. Esta WO leva o codigo, os testes e o registro (CHANGELOG, README, STATUS, IDEAS, DEC-041).

## Edicao 0 — Conferencia de hash e de arvore

```
sha1sum app/index.html tests/test_varios_json.py README.md meta/CHANGELOG.md meta/STATUS.md meta/IDEAS.md meta/DECISIONS.md logs/2026-11-17.md
GIT_OPTIONAL_LOCKS=0 git status --short
```

Todos batem com **partida**; o `git status` mostra exatamente as duas linhas do Pre-requisito; `tests/test_lateral_e_menus.py` nao existe. Qualquer outra coisa: **PARE e reporte**.

## Edicoes E01 a E31

Na ordem. Copie o que esta ENTRE as linhas de quatro crases, sem elas. Aplique por script, extraindo os blocos da WO; grave em UTF-8 com LF.

### E01 — lateral: as duas areas (CSS)

**Arquivo:** `app/index.html`

**Ancora:**

````
    height: calc(100vh - var(--top-h)); overflow: auto; padding: 12px 8px; border-right: 1px solid var(--line); }
  @media (min-width: 1280px) { .side { display: block; } }
  .side-head { font-size: 11px; letter-spacing: .06em; text-transform: uppercase; color: var(--ink-soft); padding: 4px 8px; }
  .side-head + .side-list { margin-bottom: 18px; }
````

**Texto novo (substitui a ancora inteira):**

````
    height: calc(100vh - var(--top-h)); overflow: hidden; padding: 12px 8px; border-right: 1px solid var(--line);
    flex-direction: column; }
  @media (min-width: 1280px) { .side { display: flex; } }
  .side-head { font-size: 11px; letter-spacing: .06em; text-transform: uppercase; color: var(--ink-soft); padding: 4px 8px; }
  /* 0.23 (i-064): Albuns em cima, com o espaco que sobra; Acervos presos embaixo, com
     teto menor, entao rolam antes. Cada lista rola sozinha; os titulos ficam. */
  .side-sec { display: flex; flex-direction: column; min-height: 0; }
  .side-sec > .side-list { overflow: auto; min-height: 0; }
  .side-sec-albums { flex: 1 1 auto; }
  .side-sec-acervos { flex: 0 1 auto; max-height: 34%; margin-top: 12px; padding-top: 8px; border-top: 1px solid var(--line); }
````

### E02 — «+ Novo album» preso no fim da area

**Arquivo:** `app/index.html`

**Ancora:**

````
  body.dragging-track .side-new-li { display: list-item; }
````

**Texto novo (substitui a ancora inteira):**

````
  body.dragging-track .side-new-li { display: list-item; position: sticky; bottom: 0; background: var(--paper); }
````

### E03 — CSS do menu do acervo

**Arquivo:** `app/index.html`

**Ancora:**

````
  #track-pop, #album-pop { position: fixed; z-index: 40; width: 240px; }
````

**Texto novo (substitui a ancora inteira):**

````
  #track-pop, #album-pop, #store-pop { position: fixed; z-index: 40; width: 240px; }
  #store-pop .tm-danger { color: var(--ember); }
````

### E04 — CSS dos botoes de opcao

**Arquivo:** `app/index.html`

**Ancora:**

````
  .multi-list select { margin: 4px 0 0; }
````

**Texto novo (substitui a ancora inteira):**

````
  /* 0.23 (i-061): os tres botoes de opcao de cada linha */
  .seg { display: inline-flex; align-self: flex-start; margin: 6px 0 2px; border: 1px solid var(--line); border-radius: 8px; overflow: hidden; }
  .seg label { display: flex; cursor: pointer; }
  .seg label + label { border-left: 1px solid var(--line); }
  .seg input { position: absolute; opacity: 0; width: 1px; height: 1px; pointer-events: none; }
  .seg span { padding: 6px 12px; font-size: 13px; color: var(--ink-soft); }
  .seg input:checked + span { background: var(--ink); color: var(--paper); }
  .seg input:focus-visible + span { outline: 2px solid var(--ember); outline-offset: -2px; }
  .seg input:disabled + span { opacity: .45; cursor: default; }
````

### E05 — botoes de opcao no celular

**Arquivo:** `app/index.html`

**Ancora:**

````
    .multi-dialog select, .multi-dialog input[type="text"], .multi-dialog button { min-height: 44px; }
    .multi-dialog .import-list { max-height: none; }
````

**Texto novo (substitui a ancora inteira):**

````
    .multi-dialog select, .multi-dialog input[type="text"], .multi-dialog button { min-height: 44px; }
    .multi-dialog .seg { display: flex; align-self: stretch; }
    .multi-dialog .seg label { flex: 1; }
    .multi-dialog .seg span { flex: 1; min-height: 44px; display: flex; align-items: center; justify-content: center;
      text-align: center; box-sizing: border-box; padding: 4px 6px; }
    .multi-dialog .import-list { max-height: none; }
````

### E06 — CSS: o aviso do arraste fora da lateral

**Arquivo:** `app/index.html`

**Ancora:**

````
  body.dragging .drop-hint { display: flex; }
</style>
````

**Texto novo (substitui a ancora inteira):**

````
  body.dragging .drop-hint { display: flex; }
  .drop-hint span { padding: 6px 14px; border-radius: 999px; background: rgba(244, 239, 230, .96); }
  /* 0.23 (i-063): com a lateral a vista, o aviso da pagina comeca depois dela: a
     lateral e outra zona (acervo novo), e o desenho de uma nao cobre a outra. */
  @media (min-width: 1280px) { body:has(#side:not([hidden])) .drop-hint { left: 244px; } }
  /* Sobre a lateral: so ela se destaca, com o proprio aviso; o da pagina some. */
  body.drop-zone-side .drop-hint { display: none; }
  #side.file-target { position: sticky; }
  #side.file-target::after { content: attr(data-drop-label); position: absolute; left: 8px; right: 8px; bottom: 12px;
    padding: 10px; border-radius: 8px; background: var(--paper); color: var(--ember); border: 2px dashed var(--ember);
    font-family: var(--serif); font-size: 15px; text-align: center; }
  /* Sobre um album: o album fica a vista (o aviso perde o fundo e sobe para o alto). */
  body.drop-zone-album .drop-hint { background: transparent; border-color: transparent; align-items: flex-start; padding-top: 16px; }
</style>
````

### E07 — versão 0.23.0

**Arquivo:** `app/index.html`

**Ancora:**

````
    <span class="version" data-role="app-version">v0.22.0</span>
````

**Texto novo (substitui a ancora inteira):**

````
    <span class="version" data-role="app-version">v0.23.0</span>
````

### E08 — lateral: as duas areas (HTML)

**Arquivo:** `app/index.html`

**Ancora:**

````
  <div class="side-head">Álbuns</div>
  <ul class="side-list" id="side-albums"></ul>
  <div class="side-head">Acervos neste navegador</div>
  <ul class="side-list" id="side-acervos"></ul>
````

**Texto novo (substitui a ancora inteira):**

````
  <div class="side-sec side-sec-albums">
  <div class="side-head">Álbuns</div>
  <ul class="side-list" id="side-albums"></ul>
  </div>
  <div class="side-sec side-sec-acervos">
  <div class="side-head">Acervos neste navegador</div>
  <ul class="side-list" id="side-acervos"></ul>
  </div>
````

### E09 — o menu do acervo (HTML)

**Arquivo:** `app/index.html`

**Ancora:**

````
  <button type="button" role="menuitem" class="mobile-only" id="am-cancel">Cancelar</button>
</div>
````

**Texto novo (substitui a ancora inteira):**

````
  <button type="button" role="menuitem" class="mobile-only" id="am-cancel">Cancelar</button>
</div>
<!-- 0.23 (i-062): o «⋯» de um acervo da lateral (e o clique direito nele). -->
<div class="pop" id="store-pop" role="menu" aria-labelledby="store-pop-title" hidden>
  <div class="pop-head" id="store-pop-title"></div>
  <button type="button" role="menuitem" id="cm-open">Abrir</button>
  <button type="button" role="menuitem" id="cm-json">Baixar .json</button>
  <button type="button" role="menuitem" id="cm-unlink">Desvincular do arquivo</button>
  <div class="pop-sep"></div>
  <button type="button" role="menuitem" class="tm-danger" id="cm-forget">Esquecer este acervo…</button>
</div>
````

### E10 — o texto do aviso num span

**Arquivo:** `app/index.html`

**Ancora:**

````
<div class="drop-hint" aria-hidden="true">Solte para importar</div>
````

**Texto novo (substitui a ancora inteira):**

````
<div class="drop-hint" aria-hidden="true"><span>Solte para importar</span></div>
````

### E11 — os botoes de opcao

**Arquivo:** `app/index.html`

**Ancora:**

````
    const sel = document.createElement("select");
    sel.className = "multi-choice";
    sel.setAttribute("aria-label", "O que " + e.name + " vira");
    sel.appendChild(new Option("Acervo novo", "new"));
    const ot = new Option(tracksOk ? "Faixas no acervo aberto" : "Faixas no acervo aberto (nenhum aberto)", "tracks");
    ot.disabled = !tracksOk;
    sel.appendChild(ot);
    sel.appendChild(new Option("Pular", "skip"));
    const warn = document.createElement("span"); warn.className = "multi-warn"; warn.hidden = true;
    if (!e.json) {
      li.classList.add("is-off"); sel.value = "skip"; sel.disabled = true;
````

**Texto novo (substitui a ancora inteira):**

````
    // 0.23 (i-061): tres botoes de opcao, lado a lado, no lugar da lista de escolha
    const seg = document.createElement("div");
    seg.className = "seg multi-choice"; seg.setAttribute("role", "radiogroup");
    seg.setAttribute("aria-label", "O que " + e.name + " vira");
    const radio = {};
    [["new", "Acervo novo"], ["tracks", "Faixas no aberto"], ["skip", "Pular"]].forEach(([v, label]) => {
      const lab = document.createElement("label");
      const r = document.createElement("input");
      r.type = "radio"; r.name = "multi-" + i; r.value = v;
      const sp = document.createElement("span"); sp.textContent = label;
      lab.appendChild(r); lab.appendChild(sp); seg.appendChild(lab);
      radio[v] = r;
    });
    if (!tracksOk) { radio.tracks.disabled = true; radio.tracks.parentNode.title = "Nenhum acervo aberto"; }
    // A escolha da linha, lida e gravada como era no <select>
    const sel = {
      get value() { const r = seg.querySelector("input:checked"); return r ? r.value : "skip"; },
      set value(v) { radio[v].checked = true; }
    };
    const warn = document.createElement("span"); warn.className = "multi-warn"; warn.hidden = true;
    if (!e.json) {
      li.classList.add("is-off"); sel.value = "skip"; Object.values(radio).forEach(r => { r.disabled = true; });
````

### E12 — a escolha muda pelo grupo

**Arquivo:** `app/index.html`

**Ancora:**

````
      sel.addEventListener("change", () => { syncWarn(); syncDest(); });
      syncWarn();
    }
    li.appendChild(nm); li.appendChild(info); li.appendChild(sel); li.appendChild(warn);
````

**Texto novo (substitui a ancora inteira):**

````
      seg.addEventListener("change", () => { syncWarn(); syncDest(); });
      syncWarn();
    }
    li.appendChild(nm); li.appendChild(info); li.appendChild(seg); li.appendChild(warn);
````

### E13 — dragleave limpa a zona

**Arquivo:** `app/index.html`

**Ancora:**

````
  if (!dragDepth) document.body.classList.remove("dragging");
````

**Texto novo (substitui a ancora inteira):**

````
  if (!dragDepth) { document.body.classList.remove("dragging"); setDropZone(null); }
````

### E14 — drop limpa a zona

**Arquivo:** `app/index.html`

**Ancora:**

````
  e.preventDefault(); dragDepth = 0; document.body.classList.remove("dragging");
````

**Texto novo (substitui a ancora inteira):**

````
  e.preventDefault(); dragDepth = 0; document.body.classList.remove("dragging"); setDropZone(null);
````

### E15 — o «⋯» do acervo e o clique direito

**Arquivo:** `app/index.html`

**Ancora:**

````
    li.appendChild(b); ul.appendChild(li);
  });
}
````

**Texto novo (substitui a ancora inteira):**

````
    li.appendChild(b);
    // 0.23 (i-062): o «⋯» do acervo, como o dos albuns
    li.className = "side-album side-acervo";
    const m = document.createElement("button");
    m.type = "button"; m.className = "side-more"; m.textContent = "⋯"; m.dataset.source = r.source || "";
    m.setAttribute("aria-haspopup", "menu"); m.setAttribute("aria-expanded", "false");
    m.setAttribute("aria-label", "Ações do acervo " + (r.title || r.source));
    m.addEventListener("click", ev => openAcervoMenu(r.source, r.title || r.source, ev.currentTarget));
    li.appendChild(m);
    ul.appendChild(li);
  });
}

/* ---- O «⋯» de um acervo da lateral (0.23.0, i-062) ----
   Abrir (os outros), Baixar .json (a copia guardada), Desvincular (o aberto, se
   vinculado) e Esquecer, pelo mesmo caminho do seletor de acervo. */
let acervoMenuFor = null, acervoMenuAnchor = null;
function openAcervoMenu(source, title, anchor) {
  if (acervoMenuFor === source && acervoMenuAnchor === anchor) { closeAcervoMenu(true); return; }
  closeAcervoMenu(false); closeAlbumMenu(false); closeTrackMenu(false); closePopovers(false);
  acervoMenuFor = source; acervoMenuAnchor = anchor;
  const open = source === App.source;
  document.getElementById("store-pop-title").textContent = title;
  document.getElementById("cm-open").hidden = open;
  document.getElementById("cm-unlink").hidden = !(open && App.link);
  const pop = document.getElementById("store-pop");
  pop.hidden = false;
  anchor.setAttribute("aria-expanded", "true");
  const r = anchor.getBoundingClientRect(), h = pop.offsetHeight, w = pop.offsetWidth;
  pop.style.top = (r.bottom + 4 + h > window.innerHeight ? Math.max(8, r.top - 4 - h) : r.bottom + 4) + "px";
  pop.style.left = Math.max(8, Math.min(window.innerWidth - w - 8, r.left)) + "px";
  const first = [...pop.querySelectorAll('[role="menuitem"]')].find(b => !b.hidden);
  if (first) first.focus();
}
function closeAcervoMenu(restore) {
  if (!acervoMenuFor) return;
  document.getElementById("store-pop").hidden = true;
  const a = acervoMenuAnchor;
  acervoMenuFor = null; acervoMenuAnchor = null;
  if (a) { a.setAttribute("aria-expanded", "false"); if (restore && a.isConnected) a.focus(); }
}
/** Liga um item do menu do acervo: fecha o menu e roda a acao com a origem. */
function acervoItem(elId, fn) {
  document.getElementById(elId).addEventListener("click", () => {
    const src = acervoMenuFor;
    closeAcervoMenu(false);
    if (src) fn(src);
  });
}
acervoItem("cm-open", async src => {
  let rec = null;
  try { rec = await dbGet(src); } catch (e) { /* trata abaixo */ }
  if (!rec || !openRecord(rec)) { toast("Não consegui abrir " + src); return; }
  toast("Acervo aberto: " + (rec.json.title || rec.source) + moduleRefsNotice(rec.json));
});
acervoItem("cm-json", async src => {
  // O aberto baixa pelo caminho de sempre (o rascunho da tela); os outros, a copia guardada.
  if (src === App.source) { downloadCollection(); return; }
  let rec = null;
  try { rec = await dbGet(src); } catch (e) { /* trata abaixo */ }
  if (!rec) { toast("Não consegui ler " + src); return; }
  downloadFile(src, JSON.stringify(rec.json, null, 2), "application/json");
  toast("Baixado em Downloads como " + src + ".");
});
acervoItem("cm-unlink", () => unlinkFile());
acervoItem("cm-forget", src => forgetAcervo(src));
document.addEventListener("pointerdown", e => {
  if (!acervoMenuFor) return;
  if (document.getElementById("store-pop").contains(e.target) || (acervoMenuAnchor && acervoMenuAnchor.contains(e.target))) return;
  closeAcervoMenu(false);
});

/* ---- Clique direito (0.23.0, i-062): abre o «⋯» de onde se clicou ----
   Faixa (linha da Lista, cartao, detalhe), album (cabecalho e lateral) e acervo
   (lateral); o menu abre no ponto do clique. O menu do navegador continua em campo
   de texto, com texto selecionado, com Shift e no celular (o toque longo seleciona). */
function contextMore(el) {
  const row = el.closest("#main li.row");
  if (row) return row.querySelector(".row-more");
  if (el.closest("#detail")) return App.detailId ? document.getElementById("detail-more") : null;
  const card = el.closest("#main .card");
  if (card) return card.querySelector(".card-more");
  const head = el.closest("#main .album-head");
  if (head) return head.querySelector(".album-more");
  const li = el.closest("#side li.side-album");
  return li ? li.querySelector(".side-more") : null;
}
document.addEventListener("contextmenu", e => {
  if (e.shiftKey || isMobile()) return;
  const el = e.target;
  if (!el || !el.closest || el.closest("input, textarea, select, [contenteditable], .pop, dialog")) return;
  const sel = window.getSelection();
  if (sel && !sel.isCollapsed && String(sel).trim()) return;
  const more = contextMore(el);
  if (!more) return;
  e.preventDefault();
  closeTrackMenu(false); closeAlbumMenu(false); closeAcervoMenu(false);   // reabre no ponto novo
  more.click();
  const pop = ["track-pop", "album-pop", "store-pop"].map(k => document.getElementById(k)).find(p => !p.hidden);
  if (!pop) return;
  const w = pop.offsetWidth, h = pop.offsetHeight;
  pop.style.left = Math.max(8, Math.min(window.innerWidth - w - 8, e.clientX)) + "px";
  pop.style.top = Math.max(8, Math.min(window.innerHeight - h - 8, e.clientY)) + "px";
});
````

### E16 — a zona no body e o aviso da lateral

**Arquivo:** `app/index.html`

**Ancora:**

````
  const n = Array.from(e.dataTransfer.items || []).filter(i => i.kind === "file").length;
  const hint = document.querySelector(".drop-hint"), text = dropHintText(zone, n);
  if (hint.textContent !== text) hint.textContent = text;
});
````

**Texto novo (substitui a ancora inteira):**

````
  setDropZone(zone.kind);
  const n = Array.from(e.dataTransfer.items || []).filter(i => i.kind === "file").length;
  const hint = document.querySelector(".drop-hint span"), text = dropHintText(zone, n);
  if (hint.textContent !== text) hint.textContent = text;
  // 0.23: na lateral, o aviso e dela (o CSS o desenha no pe da lateral)
  if (zone.kind === "side" && zone.el.dataset.dropLabel !== text) zone.el.dataset.dropLabel = text;
});
/** A zona do arraste no <body> (0.23): o CSS decide o que desenhar em cada uma. */
function setDropZone(kind) {
  ["page", "album", "side"].forEach(k => document.body.classList.toggle("drop-zone-" + k, k === kind));
}
````

### E17 — Esc fecha o menu do acervo

**Arquivo:** `app/index.html`

**Ancora:**

````
    if (albumMenuFor) { e.preventDefault(); e.stopImmediatePropagation(); closeAlbumMenu(true); return; }
    if ((App.selection.size || App.selecting) && !openPop && !document.querySelector("dialog[open]") && !isTextField(t)) {
````

**Texto novo (substitui a ancora inteira):**

````
    if (albumMenuFor) { e.preventDefault(); e.stopImmediatePropagation(); closeAlbumMenu(true); return; }
    if (acervoMenuFor) { e.preventDefault(); e.stopImmediatePropagation(); closeAcervoMenu(true); return; }
    if ((App.selection.size || App.selecting) && !openPop && !document.querySelector("dialog[open]") && !isTextField(t)) {
````

### E18 — le os botoes de opcao

**Arquivo:** `tests/test_varios_json.py`

**Ancora:**

````
    return page.eval_on_selector_all(
        "#multi-list > li", "e => e.map(li => [li.querySelector('.multi-name').textContent,"
        " li.querySelector('.multi-info').textContent, li.querySelector('select').value,"
        " li.querySelector('select').disabled])")
````

**Texto novo (substitui a ancora inteira):**

````
    # 0.23 (i-061): a escolha e um grupo de botoes de opcao; «desligada» = os tres desligados
    return page.eval_on_selector_all(
        "#multi-list > li", "e => e.map(li => [li.querySelector('.multi-name').textContent,"
        " li.querySelector('.multi-info').textContent, (li.querySelector('.seg input:checked') || {}).value,"
        " [...li.querySelectorAll('.seg input')].every(r => r.disabled)])")
````

### E19 — clica em «Faixas no aberto»

**Arquivo:** `tests/test_varios_json.py`

**Ancora:**

````
    page.select_option("#multi-list > li:first-child select", "tracks")
````

**Texto novo (substitui a ancora inteira):**

````
    page.click("#multi-list > li:first-child .seg label:has(input[value=tracks])")
````

### E20 — o radio desligado

**Arquivo:** `tests/test_varios_json.py`

**Ancora:**

````
    assert page.eval_on_selector_all("#multi-list option[value=tracks]", "e => e.map(o => o.disabled)") == [True, True]
````

**Texto novo (substitui a ancora inteira):**

````
    assert page.eval_on_selector_all("#multi-list input[value=tracks]", "e => e.map(o => o.disabled)") == [True, True]
````

### E21 — a altura dos botoes de opcao

**Arquivo:** `tests/test_varios_json.py`

**Ancora:**

````
    small = page.eval_on_selector_all("#multi-dialog select, #multi-dialog button",
````

**Texto novo (substitui a ancora inteira):**

````
    small = page.eval_on_selector_all("#multi-dialog select, #multi-dialog button, #multi-dialog .seg span",
````

### E22 — estado v0.23.0

**Arquivo:** `README.md`

**Ancora:**

````
> **Estado:** v0.22.0 — ferramenta em uso. Lê, guarda e edita vários acervos (importa vários `.json` de uma vez), grava direto no arquivo do acervo (Chrome e Edge), copia por campo, troca módulos de estilo, ajusta o BPM, **mede cada prompt contra os limites do Suno**, guarda as **fórmulas de referência** dos guias para copiar inteiras, exporta Markdown, exporta uma faixa como `.json` e **entrega o prompt para chats gerarem canções no esquema**. Publicada no GitHub Pages. Ver `meta/ROADMAP.md`.
````

**Texto novo (substitui a ancora inteira):**

````
> **Estado:** v0.23.0 — ferramenta em uso. Lê, guarda e edita vários acervos (importa vários `.json` de uma vez), grava direto no arquivo do acervo (Chrome e Edge), copia por campo, troca módulos de estilo, ajusta o BPM, **mede cada prompt contra os limites do Suno**, guarda as **fórmulas de referência** dos guias para copiar inteiras, exporta Markdown, exporta uma faixa como `.json` e **entrega o prompt para chats gerarem canções no esquema**. Publicada no GitHub Pages. Ver `meta/ROADMAP.md`.
````

### E23 — o clique direito e a lateral

**Arquivo:** `README.md`

**Ancora:**

````
7. Para reorganizar, não há nada a ligar: na Lista, arraste a faixa pela alça ⋮⋮ (para outra posição, outro álbum ou um álbum da lateral; durante o arrastar, a lateral oferece *+ Novo álbum*), ou use o «⋯» da faixa (*Mover para…*, *Subir*, *Descer*, *Excluir…*; `Alt+↑` e `Alt+↓` no título). Marque as caixas para mover, exportar, marcar ou excluir várias de uma vez. Os álbuns têm o próprio «⋯», no cabeçalho e na lateral: *Renomear…* (título e descrição), *Subir álbum*, *Descer álbum*, *Juntar com…* e *Excluir álbum…*; na lateral, a alça ⋮⋮ de cada álbum arrasta. Cada operação mostra *Desfazer* no aviso (ou `Ctrl+Z`), até a próxima. Para trazer faixas de outro `.json` (ou de vários), use *Importar faixas…* no «⋯» da barra, ou solte o arquivo sobre um álbum. As mudanças ficam num rascunho no navegador; a barra mostra quantas são. No Chrome e no Edge do computador, *Salvar* (ou `Ctrl+S`) grava no próprio `.json`: na primeira vez, a janela do sistema pede o arquivo, já com o nome; daí em diante grava direto, e avisa se o arquivo mudou fora do app. O ▾ ao lado tem *Salvar em outro arquivo…* e *Baixar .json*. No Firefox, no Safari e no celular, *Salvar .json* baixa com o nome do arquivo original — substitua o antigo por ele, e ele passa a ser a fonte. Só se organiza um acervo com cópia guardada no navegador (importado por arquivo).
````

**Texto novo (substitui a ancora inteira):**

````
7. Para reorganizar, não há nada a ligar: na Lista, arraste a faixa pela alça ⋮⋮ (para outra posição, outro álbum ou um álbum da lateral; durante o arrastar, a lateral oferece *+ Novo álbum*), ou use o «⋯» da faixa (*Mover para…*, *Subir*, *Descer*, *Excluir…*; `Alt+↑` e `Alt+↓` no título). Marque as caixas para mover, exportar, marcar ou excluir várias de uma vez. Os álbuns têm o próprio «⋯», no cabeçalho e na lateral: *Renomear…* (título e descrição), *Subir álbum*, *Descer álbum*, *Juntar com…* e *Excluir álbum…*; na lateral, a alça ⋮⋮ de cada álbum arrasta. No computador, o clique direito numa faixa, num álbum ou num acervo da lateral abre o mesmo «⋯», no ponto do clique (com `Shift`, ou com texto selecionado, vale o menu do navegador); o «⋯» do acervo tem *Abrir*, *Baixar .json*, *Desvincular do arquivo* e *Esquecer este acervo…*. Na lateral, Álbuns e Acervos têm cada um a sua área, e cada lista rola sozinha. Cada operação mostra *Desfazer* no aviso (ou `Ctrl+Z`), até a próxima. Para trazer faixas de outro `.json` (ou de vários), use *Importar faixas…* no «⋯» da barra, ou solte o arquivo sobre um álbum. As mudanças ficam num rascunho no navegador; a barra mostra quantas são. No Chrome e no Edge do computador, *Salvar* (ou `Ctrl+S`) grava no próprio `.json`: na primeira vez, a janela do sistema pede o arquivo, já com o nome; daí em diante grava direto, e avisa se o arquivo mudou fora do app. O ▾ ao lado tem *Salvar em outro arquivo…* e *Baixar .json*. No Firefox, no Safari e no celular, *Salvar .json* baixa com o nome do arquivo original — substitua o antigo por ele, e ele passa a ser a fonte. Só se organiza um acervo com cópia guardada no navegador (importado por arquivo).
````

### E24 — entrada [0.23.0]

**Arquivo:** `meta/CHANGELOG.md`

**Ancora:**

````
> Histórico de versões entregues. SemVer + Keep a Changelog. Cresce no topo.

````

**Texto novo (substitui a ancora inteira):**

````
> Histórico de versões entregues. SemVer + Keep a Changelog. Cresce no topo.

---

## [0.23.0] — 2026-11-17

O clique direito abre o «⋯», a lateral ganha duas áreas que rolam sozinhas e o aviso do arraste deixa de cobrir a lateral (i-061 a i-064, DEC-041).

### Added
- **Clique direito** (computador) numa faixa (linha da Lista, cartão ou detalhe), num álbum (cabeçalho ou lateral) ou num acervo da lateral abre o «⋯» dele, no ponto do clique. Com `Shift`, num campo de texto ou com texto selecionado, e no celular, continua o menu do navegador.
- **O «⋯» do acervo, na lateral:** *Abrir* (os outros), *Baixar .json* (a cópia guardada; o aberto baixa o rascunho da tela), *Desvincular do arquivo* (o aberto, se vinculado) e *Esquecer este acervo…*, pelo mesmo caminho do seletor.

### Changed
- **Janela «Importar N arquivos»:** a escolha de cada linha é um grupo de três botões, *Acervo novo* · *Faixas no aberto* · *Pular*, no lugar da lista de escolha. No celular, os três dividem a largura, com 44 px de altura.
- **A lateral em duas áreas:** Álbuns em cima, com o espaço que sobra; Acervos presos no pé, com teto de um terço da altura. Cada lista rola sozinha e os títulos ficam. Enquanto se arrasta uma faixa, *+ Novo álbum* fica à vista no fim da área dos álbuns.

### Fixed
- **O aviso do arraste cobria a lateral** (0.22.0): o desenho da página começa depois dela. Sobre a lateral, só ela se destaca, com o aviso no pé; sobre um álbum, o álbum fica à vista e o aviso sobe, sem a moldura da página.

10 testes novos em `tests/test_lateral_e_menus.py` (91 no total); os da janela de vários leem os botões de opção.

````

### E25 — versão e ultima conversa

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
**Versão atual:** 0.22.0 · **Fase:** 3a, 3a.2, o BPM da 3b, o prompt-modelo e as conveniências de uso concluídos e conferidos · os álbuns antigos convertidos (i-008, fora do repo) · curadoria no app concluída nas três entregas (DEC-028, DEC-029) · frente de interface concluída e conferida nas quatro entregas (DEC-030 a DEC-033) · organizar os álbuns (0.18.0, DEC-035) conferido · rampa de BPM (0.19.0, DEC-036) conferida · fórmulas de referência (0.20.0, DEC-037) conferidas na tela · importar vários `.json` (0.22.0, DEC-040) à espera da conferência na tela · a Fase 3 concluída · kit de música lido pelo KCM, à espera da resposta (i-039)

---

## Última conversa (2026-11-16, 0.22.0: importar vários `.json`, WO 0047)

- **0.22.0 implementada pelo chat num clone** (i-057, DEC-040): a janela «Importar N arquivos», a lateral como zona de «acervo novo», o aviso do arraste por zona, `multiple` nos botões e os vínculos pegos durante o `drop`. 81 testes, duas rodadas; os 12 de comportamento novo reprovam na 0.21.0, e os 2 de falso positivo (um arquivo) passam nas duas `[medido pelo chat, no clone]`. Falta a conferência na tela do dono (roteiro no log de 2026-11-16, Conversa 6) e o CI.
- **Escolhidos na implementação** (o que a DEC-040 deixou aberto): os textos da janela e do aviso; o mesmo nome do acervo aberto em «Acervo novo» substitui o que está na tela; sem IndexedDB, a lateral não é zona; os acervos novos entram no seletor pela regra de sempre (o mais recente primeiro).
- **Este bloco substitui o anterior** (a conversa de 2026-11-14 a 2026-11-16, encerrada por handoff). O que ele dizia está em `logs/2026-11-16.md`.
````

**Texto novo (substitui a ancora inteira):**

````
**Versão atual:** 0.23.0 · **Fase:** 3a, 3a.2, o BPM da 3b, o prompt-modelo e as conveniências de uso concluídos e conferidos · os álbuns antigos convertidos (i-008, fora do repo) · curadoria no app concluída nas três entregas (DEC-028, DEC-029) · frente de interface concluída e conferida nas quatro entregas (DEC-030 a DEC-033) · organizar os álbuns (0.18.0, DEC-035) conferido · rampa de BPM (0.19.0, DEC-036) conferida · fórmulas de referência (0.20.0, DEC-037) conferidas na tela · importar vários `.json` (0.22.0, DEC-040) conferido na tela · clique direito e lateral em duas áreas (0.23.0, DEC-041) à espera da conferência na tela · a Fase 3 concluída · kit de música lido pelo KCM, à espera da resposta (i-039)

---

## Última conversa (2026-11-16 a 2026-11-17, 0.22.0 e 0.23.0, WO 0047 e 0048)

- **0.22.0 aplicada e conferida:** `a6aa20a`, CI verde (run `44082742521`, `[medido pelo Code]`); roteiro de tela feito pelo dono `[relatado pelo dono, 2026-11-17]`, com um defeito (o aviso do arraste cobria a lateral, i-063). O passo 7 (o vínculo do arraste) tem a marca no disco: o arquivo do teste foi regravado às 09:39, depois do apply `[medido pelo chat]`.
- **0.23.0 implementada pelo chat num clone** (DEC-041): o aviso do arraste fora da lateral (i-063), os botões de opção na janela de vários (i-061), o clique direito (i-062) e a lateral em duas áreas (i-064). 91 testes, duas rodadas; os 7 de comportamento novo reprovam na 0.22.0 e os 3 de falso positivo passam nas duas `[medido pelo chat, no clone]`. Falta o CI e a conferência na tela (roteiro no log de 2026-11-17).
- **Este bloco substitui o anterior** (a 0.22.0 no clone). O que ele dizia está em `logs/2026-11-16.md`, Conversa 6.
````

### E26 — funciona: clique direito e lateral

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
- **Importar vários `.json`** (0.22.0, DEC-040): soltar ou escolher vários abre «Importar N arquivos», com «Acervo novo», «Faixas no acervo aberto» ou «Pular» por arquivo; o acervo novo fica guardado sem trocar o aberto; as faixas de todos entram numa operação, com um «Desfazer». Na lateral, fora de um álbum, cada arquivo vira acervo guardado, sem janela (também um só). O aviso do arraste diz a zona.
````

**Texto novo (substitui a ancora inteira):**

````
- **Clique direito e lateral em duas áreas** (0.23.0, DEC-041): no computador, o clique direito numa faixa, num álbum ou num acervo da lateral abre o «⋯» dele no ponto do clique (`Shift`, campo de texto e texto selecionado deixam o do navegador); o acervo da lateral ganhou «⋯» (Abrir, Baixar .json, Desvincular, Esquecer). Na lateral, Álbuns e Acervos têm cada um a sua área, que rola sozinha.
- **Importar vários `.json`** (0.22.0, DEC-040; botões de opção desde a 0.23.0): soltar ou escolher vários abre «Importar N arquivos», com «Acervo novo», «Faixas no aberto» ou «Pular» por arquivo; o acervo novo fica guardado sem trocar o aberto; as faixas de todos entram numa operação, com um «Desfazer». Na lateral, fora de um álbum, cada arquivo vira acervo guardado, sem janela (também um só). O aviso do arraste diz a zona.
````

### E27 — 91 testes

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
- **Testes do navegador no CI** (DEC-034): `tests/` (pytest e Playwright, 81 testes desde a 0.22.0, dados só sintéticos) e `.github/workflows/testes.yml`, que roda o `validate.py` com esquema, os testes dos conversores e o `pytest tests` a cada push na `main`. O resultado é o ✓ ou ✗ no commit e a aba Actions.
````

**Texto novo (substitui a ancora inteira):**

````
- **Testes do navegador no CI** (DEC-034): `tests/` (pytest e Playwright, 91 testes desde a 0.23.0, dados só sintéticos) e `.github/workflows/testes.yml`, que roda o `validate.py` com esquema, os testes dos conversores e o `pytest tests` a cada push na `main`. O resultado é o ✓ ou ✗ no commit e a aba Actions.
````

### E28 — backlog: conferir a 0.23.0

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
1. **Conferir a 0.22.0 na tela** (dono): o roteiro do log de 2026-11-16, Conversa 6. Depois dela, o recesso decidido pelo dono.
````

**Texto novo (substitui a ancora inteira):**

````
1. **Conferir a 0.23.0 na tela** (dono): o roteiro do log de 2026-11-17. Depois dela, o recesso decidido pelo dono.
````

### E29 — i-061 a i-064

**Arquivo:** `meta/IDEAS.md`

**Ancora:**

````

## Feedback para o Kit
````

**Texto novo (substitui a ancora inteira):**

````

### i-061 ✅ Botões de opção no lugar da lista de escolha, na janela de vários
`[relatado pelo dono, 2026-11-17]` Na janela «Importar N arquivos», trocar a lista de escolha por botões de opção única (ou um deslizar de três): acervo novo, faixas no acervo, pular; o dono pediu sugestão de texto. **Entregue (0.23.0, 2026-11-17, DEC-041):** três botões lado a lado, *Acervo novo* · *Faixas no aberto* · *Pular*.

### i-062 ✅ O clique direito abre o «⋯»
`[relatado pelo dono, 2026-11-17]` O botão direito do mouse abre o menu de contexto: na faixa, o mesmo do «⋯»; na lateral, o do álbum e o do acervo (ele perguntou se o acervo teria alguma ação). **Entregue (0.23.0, 2026-11-17, DEC-041):** faixa, álbum e acervo, no ponto do clique; o acervo da lateral ganhou «⋯» (Abrir, Baixar .json, Desvincular, Esquecer).

### i-063 ✅ O aviso do arraste não cobre a lateral
`[relatado pelo dono, 2026-11-17, no roteiro da 0.22.0]` O desenho vermelho do arraste ainda cobria a tela inteira, por cima da lateral, que desde a 0.22.0 é outra zona (acervo novo direto): confuso. Pediu também tirar qualquer outra colisão da função antiga. **Entregue (0.23.0, 2026-11-17):** o aviso da página começa depois da lateral; sobre a lateral, só ela se destaca, com o aviso no pé; sobre um álbum, sem a moldura da página.

### i-064 ✅ A lateral com áreas fixas para Álbuns e Acervos
`[relatado pelo dono, 2026-11-17]` As duas listas da lateral não têm lugar fixo: dependem do tamanho dos álbuns. Proposta dele: Acervos num espaço fixo no canto de baixo; as duas rolam ao atingir o limite; Álbuns com mais espaço, então Acervos rola mais cedo. Liga-se à i-047 (painel lateral). **Entregue (0.23.0, 2026-11-17, DEC-041):** Álbuns em cima com o que sobra, Acervos presos no pé com teto de um terço; cada lista rola sozinha.

## Feedback para o Kit
````

### E30 — DEC-041 (no fim do arquivo)

**Arquivo:** `meta/DECISIONS.md`

**Ancora:**

````
**Na implementação (0.22.0), o que a decisão deixou aberto:** os textos são os da spec, quase literais. O mesmo nome do acervo aberto, em «Acervo novo», substitui o que está na tela (guardar sem abrir deixaria a tela com um rascunho que já não é o guardado). Sem IndexedDB (um acervo só), a lateral não é zona e a janela abre o último guardado. Os acervos novos entram no seletor pela regra de sempre, o mais recente primeiro. Pelos botões, o padrão de cada linha é o do botão («Importar .json…» → acervo novo; «Importar faixas…» → faixas), como diz a spec, item 5; a forma do arquivo decide só no arraste.
````

**Texto novo (substitui a ancora inteira):**

````
**Na implementação (0.22.0), o que a decisão deixou aberto:** os textos são os da spec, quase literais. O mesmo nome do acervo aberto, em «Acervo novo», substitui o que está na tela (guardar sem abrir deixaria a tela com um rascunho que já não é o guardado). Sem IndexedDB (um acervo só), a lateral não é zona e a janela abre o último guardado. Os acervos novos entram no seletor pela regra de sempre, o mais recente primeiro. Pelos botões, o padrão de cada linha é o do botão («Importar .json…» → acervo novo; «Importar faixas…» → faixas), como diz a spec, item 5; a forma do arquivo decide só no arraste.

## DEC-041 — O clique direito abre o «⋯», e a lateral tem duas áreas que rolam

**Data:** 2026-11-17
**Status:** aceita (0.23.0)
**Contexto:** Depois do roteiro da 0.22.0, o dono pediu (2026-11-17) quatro mudanças antes do recesso: o aviso do arraste não cobrir a lateral (i-063), botões de opção na janela de vários (i-061), o clique direito abrir o menu de contexto da faixa, do álbum e do acervo (i-062) e a lateral com lugar fixo para Álbuns e Acervos, cada um rolando sozinho (i-064) `[relatado pelo dono]`.
**Decisão:**
- **O clique direito abre o «⋯» que já existe** (faixa, álbum) **no ponto do clique**: nenhum menu novo para a faixa e o álbum, a mesma lista de ações. O menu do navegador continua com `Shift`, em campo de texto, com texto selecionado e no celular (o toque longo é do navegador; o «⋯» está à mão).
- **O acervo da lateral ganha o próprio «⋯»**: Abrir (os outros), Baixar .json, Desvincular do arquivo (o aberto, se vinculado) e Esquecer este acervo…, chamando as funções do seletor (`openRecord`, `downloadCollection`, `unlinkFile`, `forgetAcervo`).
- **A lateral em duas áreas:** Álbuns com o espaço que sobra, Acervos presos no pé com teto de 34% da altura; cada lista rola, os títulos não.
- **A escolha da janela de vários vira três botões de opção** (rádio estilizado): «Acervo novo · Faixas no aberto · Pular».
**Alternativas consideradas:** um menu de contexto próprio, diferente do «⋯» (duas listas de ações para manter); tomar o clique direito sempre (perde o «copiar» do navegador sobre texto selecionado); um deslizar de três posições na janela (esconde as opções que não estão marcadas e é menos claro com o teclado); a lateral rolando inteira, como antes.
**Consequências:** (+) Um gesto a menos para cada ação, sem nada novo para aprender. (+) A lista de acervos não some para baixo de uma lista longa de álbuns. (−) Com muitos acervos e pouca altura, a área deles mostra poucas linhas de cada vez. (−) O «Desvincular» do acervo só aparece no aberto, porque o vínculo vive no acervo aberto.
````

### E31 — arquivo novo: os testes da lateral e dos menus

**Arquivo:** `tests/test_lateral_e_menus.py` (novo). Crie com o conteudo abaixo, inteiro. Se ja existir com o sha1 da chegada, PULE; com outro conteudo, PARE e reporte.

````
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
````

## Depois de aplicar — conferencia antes do commit

| # | Checagem | Comando | Esperado |
|---|---|---|---|
| 1 | Os arquivos sao os previstos | `sha1sum app/index.html tests/test_varios_json.py README.md meta/CHANGELOG.md meta/STATUS.md meta/IDEAS.md meta/DECISIONS.md tests/test_lateral_e_menus.py logs/2026-11-17.md` | a coluna **chegada** |
| 2 | Versao | `grep -c 'data-role="app-version">v0.23.0<' app/index.html` | `1` |
| 3 | O menu do acervo e o clique direito | `grep -c 'id="store-pop"' app/index.html` e `grep -c 'addEventListener("contextmenu"' app/index.html` | `1` e `1` |
| 4 | O id do seletor nao se repete | `grep -c 'id="acervo-pop"' app/index.html` | `1` |
| 5 | Validacao | `python scripts/validate.py; echo "exit=$?"` | `exit=0`, versao 0.23.0 |
| 6 | Nada alem do previsto | `GIT_OPTIONAL_LOCKS=0 git status --short --untracked-files=all` | os 9 arquivos da tabela e esta WO |
| 7 | Depois do push: o CI | `gh run list --limit 1`, em laco com `gh run view <id> --json status,conclusion` ate `completed` | `success`; se vermelho, o passo e as ultimas 30 linhas de `gh run view <id> --log-failed` |

As checagens 2 a 5 rodaram no clone do chat; no Git Bash, **nao testado**. O chat rodou os 91 testes duas vezes no clone (cerca de 57 s) e mediu que os 7 de comportamento novo reprovam na 0.22.0. O pytest local do Code nao roda: o veredito e o CI (checagem 7).
**Esta e qual pergunta?** A 1 responde «esta la?»; a 7, «os testes passam no CI?». Nenhuma responde «funciona na tela?»: isso e o roteiro do dono (log de 2026-11-17).

## Relatorio de aplicacao

Grave em `../AAMMDD-HHMM-code-cancioneiro-apply-wo0048.txt`, com o carimbo de `date +%y%m%d-%H%M` rodado na hora. Checagem 1 em primeiro lugar e o estado final do CI. **Sem `/wrap` depois desta WO**, e sem secao sua no log, salvo se algo fugir do literal.

## Commit

```
git add app/index.html tests/test_varios_json.py README.md meta/CHANGELOG.md meta/STATUS.md meta/IDEAS.md meta/DECISIONS.md tests/test_lateral_e_menus.py logs/2026-11-17.md meta/workorders/261117-wo0048-clique-direito-e-lateral-0-23-0.md
```

```
git commit -m "feat: clique direito, lateral em duas areas e aviso do arraste (0.23.0)" -m "O clique direito abre o menu da faixa, do album e do acervo no ponto do clique; o acervo da lateral ganha menu proprio; Albuns e Acervos em areas que rolam sozinhas; botoes de opcao na janela de varios; o aviso do arraste nao cobre mais a lateral (DEC-041). 10 testes novos."
```

```
git push
```
