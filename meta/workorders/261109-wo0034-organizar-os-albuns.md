# WO 0034 — Organizar os álbuns (0.18.0)

## Cabecalho

> **Tipo:** mista — codigo (`app/index.html`, 14 edicoes; `tests/test_organizar.py`, 1; `tests/test_albuns.py`, novo) e registro (CHANGELOG, README, DECISIONS, IDEAS, ROADMAP e STATUS, 12 edicoes), mais o versionamento de tres arquivos que o chat gravou.
> **Config sugerida:** Sonnet · `/effort medium`.
> **Pre-requisito:** commit `754acec`, branch `main`, sincronizada com `origin/main`. O `git status --short` mostra exatamente: ` M logs/2026-11-09.md`, ` M meta/CONTEXT.md`, `?? meta/specs/261109-organizar-os-albuns.md` e `?? meta/workorders/261109-wo0034-organizar-os-albuns.md`.
> **Base:** spec `meta/specs/261109-organizar-os-albuns.md`, os cinco pontos decididos pelo dono em 2026-11-09 como recomendados `[relatado pelo dono]` → DEC-035, inserida aqui. Implementada e testada pelo chat num clone de `754acec`: 44 de 44 testes em duas rodadas (12 novos, que reprovam na 0.17.0), `validate.py` com esquema OK.
> **Depende de:** WO 0033 (`47bb0cf`, wrap `754acec`).
>
> | arquivo | partida (sha1) | chegada (sha1) |
> |---|---|---|
> | `app/index.html` | `9e2ebeb0eaf65dc623cb19db9b2b8e1b285db85e` | `2888edf687a262c321cba0493f5a419cae4387b3` |
> | `tests/test_organizar.py` | `c9b711c7cfa884d68f58dfb61faad383b911d398` | `a69e87a11ccb43c572355d0fda87c517ab996051` |
> | `meta/CHANGELOG.md` | `bae6d1ba77a1c63f96fd7e3ba031edcd5609ce67` | `d4c8d7b15a93b87ba360f2471d5b5e812eb9d605` |
> | `README.md` | `4d485becd58c8f73a14db7e418d4b54168983025` | `96cfb926140bfaf5fe08c6cb0a911e05ccf58778` |
> | `meta/DECISIONS.md` | `129e9bab07c1979f395b971fe2b188923a34b113` | `0b806f0e660a3fd022d7c5ad1ba0073c6c790fba` |
> | `meta/IDEAS.md` | `a99933998f2e1a9517628d21e90d69518d6a6593` | `b3f7e9bfc28abe5f73e94dc4a5359e9ff559753a` |
> | `meta/ROADMAP.md` | `f6b41365beaada3223b3829d4ed15053b2a168fd` | `8aa65e907ff0222f02f1ca3d89c6f1014312ef61` |
> | `meta/STATUS.md` | `f482f4754c90b3c6e2295fe6457c5df73149a3fc` | `b39162211db38398bf26b979db615ecf873fdf58` |
> | `tests/test_albuns.py` (novo) | — | `c4e5796346d653137e6370a0401f1a7d82be2c02` |
>
> **Arquivos que o chat gravou no disco e esta WO so versiona** (partida = chegada):
>
> | arquivo | sha1 |
> |---|---|
> | `meta/CONTEXT.md` | `5ee54033326c53e7e7eb9c1521b1f1bcb3255a10` |
> | `meta/specs/261109-organizar-os-albuns.md` | `57f30388ea0ca6840c3b42836a6b5dd166feff65` |
> | `logs/2026-11-09.md` | `1efafd0d6352f943ecb33f04217a87b111d6f340` |
>
> **Ancora semantica:** se um trecho-ancora nao bater EXATAMENTE, PARE e reporte.
> **Idempotencia:** antes de cada edicao, procure o texto NOVO INTEIRO; se ja estiver la, PULE e diga no relatorio. Arquivo novo que ja existe com o sha1 de chegada: PULE; com outro: PARE.
> **Ancoras:** linhas inteiras (ou blocos de linhas inteiras), cada uma 1 vez no arquivo no estado em que a edicao e aplicada, na ordem abaixo. Toda edicao «substitui a ancora inteira».
> **Âncoras lidas em** (todas lidas pelo chat NESTE turno, dos arquivos em `754acec` — sha1 de partida igual no disco do dono, conferido; o chat aplicou as edicoes num clone e mediu a chegada):
> - E01 (`app/index.html`, versao 0.18.0): linha `    <span class="version" data-role="app-version">v0.17.0</span>`
> - E02 (`app/index.html`, CSS: o «⋯» do álbum no cabeçalho): linha `  .album-head .album-md { margin-left: auto; font-size: 12px; padding: 4px 10px; }`
> - E03 (`app/index.html`, CSS: o menu do álbum como o da faixa): linha `  #track-pop { position: fixed; z-index: 40; width: 240px; }`
> - E04 (`app/index.html`, CSS: o menu do álbum vira folha no celular): linha `    #track-pop { left: 0 !important; right: 0; top: auto !important; bottom: 0; width: aut…`
> - E05 (`app/index.html`, HTML: o menu do álbum): linha `<div class="batch" id="batch" role="toolbar" aria-label="Ações em lote" hidden>`
> - E06 (`app/index.html`, HTML: as janelas de renomear e de juntar): linha `<dialog class="prompt-dialog" id="move-dialog" aria-labelledby="move-dialog-title">`
> - E07 (`app/index.html`, render: o «⋯» do álbum no lugar do «exportar álbum .md»): linha `    // botao de exportar este album em .md`
> - E08 (`app/index.html`, lateral: alça e «⋯» em cada álbum): linha `  const item = (title, n, id) => {`
> - E09 (`app/index.html`, lateral: o «⋯» depois do nome): linha `    b.addEventListener("click", () => { document.getElementById("filter-album").value = id…`
> - E10 (`app/index.html`, lateral: liga o arrastar dos álbuns): linha `  nb.textContent = "+ Novo álbum (solte aqui)";`
> - E11 (`app/index.html`, Esc fecha o menu do álbum): linha `    if (trackMenuFor) { e.preventDefault(); e.stopImmediatePropagation(); closeTrackMenu(t…`
> - E12 (`app/index.html`, Alt+↑/↓ no nome do álbum da lateral): linha `  if (e.altKey && !e.ctrlKey && !e.metaKey && (e.key === "ArrowUp" || e.key === "ArrowDown…`
> - E13 (`app/index.html`, o bloco da 0.18): linha `/* ---- Arrastar ---- */`
> - E14 (`app/index.html`, a lateral ganha as alças quando a cópia guardada fica pronta): linha `  setupSortables();`
> - E15 (`tests/test_organizar.py`, esperar o exemplo carregado sozinho): linha `    page = open_app()`
> - E16 (`meta/CHANGELOG.md`, entrada [0.18.0]): linha `## [0.17.0] — 2026-11-06`
> - E17 (`README.md`, estado v0.18.0): linha `> **Estado:** v0.17.0 — ferramenta em uso. Lê, guarda e edita vários acervos, grava direto…`
> - E18 (`README.md`, passo 7: os álbuns): linha `7. Para reorganizar, não há nada a ligar: na Lista, arraste a faixa pela alça ⋮⋮ (para out…`
> - E19 (`meta/DECISIONS.md`, DEC-035): linha `**Consequências:** (+) Toda mudança roda contra tudo o que já funcionava, inclusive o arra…`
> - E20 (`meta/IDEAS.md`, i-049 entregue (título)): linha `### i-049 💡 Organizar os álbuns`
> - E21 (`meta/IDEAS.md`, i-049 entregue (linha)): linha `[capturada pelo chat, 2026-11-06, na spec da I3] Renomear um álbum, reordenar os álbuns …`
> - E22 (`meta/ROADMAP.md`, organizar os álbuns): linha `- ✅ Frente de interface (i-043 a i-048, DEC-030 a DEC-033), em quatro entregas: ✅ barra ún…`
> - E23 (`meta/STATUS.md`, versão): linha `**Versão atual:** 0.17.0 · **Fase:** 3a, 3a.2, o BPM da 3b, o prompt-modelo e as conveniên…`
> - E24 (`meta/STATUS.md`, última conversa): linha `## Última conversa (2026-11-09, I4 conferida, i-051 e o kit de música v2)`
> - E25 (`meta/STATUS.md`, funciona: os álbuns): linha `- **Organizar** (0.16.0, DEC-030, DEC-032): arrastar pela alça ⋮⋮ na Lista (com filtro, an…`
> - E26 (`meta/STATUS.md`, pendências: conferir os álbuns): linha `- **Apagar à mão o ..\sonda-i4-teste.json** — arquivo de teste da sonda, na pasta-pai (o…`
> - E27 (`meta/STATUS.md`, backlog na ordem decidida): linha `1. **Organizar os álbuns** (i-049) — renomear, reordenar na lateral, juntar dois.`
> **Canal dos meta neste ciclo = CODE:** CHANGELOG, DECISIONS e STATUS sao do Code (DEC-010); IDEAS, ROADMAP e README mudam por esta WO; CONTEXT, a spec e o log do chat ja estao gravados.

---

## 1. Por que

A i-049 (DEC-035): o «⋯» do album, no cabecalho e na lateral, com renomear, subir e descer, juntar, exportar e
excluir, e o arrastar dos albuns na lateral. Versao 0.18.0. O backlog do STATUS passa a seguir a ordem que o dono
decidiu: rampa de BPM, depois os prompts prontos como modulos.

## Armadilhas

- **Aplique por script, extraindo os blocos da WO** (como nas 0032 e 0033). Os blocos tem «», ⋯, ⋮⋮, ↑ ↓ e JS com `\\n` dentro de string (E14): copie, nunca redigite.
- **`</script` nao aparece em nenhum texto novo.** Se aparecer depois de aplicar, PARE.
- **A E07 tira o botao «exportar album .md»** do cabecalho: ele passa a morar no «⋯» do album (E05 e E14). Nao e perda.
- **Nao rode `pytest` aqui:** o CI roda depois do push (44 testes). O `validate.py` local continua.
- **IDEAS com emoji no titulo** (E19): a ancora traz o 💡 inteiro; nas checagens, procure pelo numero.

## Edicao 0 — Conferencia de hash e de arvore

```
sha1sum app/index.html tests/test_organizar.py meta/CHANGELOG.md README.md meta/DECISIONS.md meta/IDEAS.md meta/ROADMAP.md meta/STATUS.md meta/CONTEXT.md meta/specs/261109-organizar-os-albuns.md logs/2026-11-09.md
GIT_OPTIONAL_LOCKS=0 git status --short
ls tests/test_albuns.py 2>&1
```

Os editados batem com **partida**, os tres do chat com o sha1 deles; o `git status` mostra exatamente as quatro linhas do Pre-requisito; `tests/test_albuns.py` nao existe. Qualquer outra coisa: **PARE e reporte**.

## Edicoes E01 a E27

Na ordem. Copie o que esta ENTRE as linhas de quatro crases, sem elas. Cada edicao diz o arquivo.

### E01 — versao 0.18.0

**Arquivo:** `app/index.html`

**Ancora:**

````
    <span class="version" data-role="app-version">v0.17.0</span>
````

**Texto novo (substitui a ancora inteira):**

````
    <span class="version" data-role="app-version">v0.18.0</span>
````

### E02 — CSS: o «⋯» do álbum no cabeçalho

**Arquivo:** `app/index.html`

**Ancora:**

````
  .album-head .album-md { margin-left: auto; font-size: 12px; padding: 4px 10px; }
````

**Texto novo (substitui a ancora inteira):**

````
  .album-head .album-more { margin-left: auto; font-size: 15px; padding: 2px 10px; line-height: 1.2; }   /* 0.18: o «⋯» do álbum */
````

### E03 — CSS: o menu do álbum como o da faixa

**Arquivo:** `app/index.html`

**Ancora:**

````
  #track-pop { position: fixed; z-index: 40; width: 240px; }
  #track-pop .tm-row { display: flex; gap: 4px; }
  #track-pop .tm-row button { flex: 1; }
  #track-pop .kbd-hint { color: var(--ink-soft); font-size: 11px; margin-left: 6px; }
  #track-pop button:disabled { opacity: .45; cursor: default; }
  #track-pop .tm-danger { color: var(--ember); }
````

**Texto novo (substitui a ancora inteira):**

````
  #track-pop, #album-pop { position: fixed; z-index: 40; width: 240px; }
  #track-pop .tm-row, #album-pop .tm-row { display: flex; gap: 4px; }
  #track-pop .tm-row button, #album-pop .tm-row button { flex: 1; }
  #track-pop .kbd-hint, #album-pop .kbd-hint { color: var(--ink-soft); font-size: 11px; margin-left: 6px; }
  #track-pop button:disabled, #album-pop button:disabled { opacity: .45; cursor: default; }
  #track-pop .tm-danger, #album-pop .tm-danger { color: var(--ember); }
  #album-pop .tm-row { flex-direction: column; gap: 0; }   /* 0.18: «Subir álbum» e «Descer álbum», um por linha */
  /* 0.18: a lateral com a alca e o «⋯» de cada album (a partir de 1280 px). */
  .side-album { display: flex; align-items: center; }
  .side-album .side-item { flex: 1; min-width: 0; }
  .side-grip { flex: none; width: 18px; height: 28px; padding: 0; border: 0; background: transparent; color: var(--ink-soft);
    cursor: grab; letter-spacing: -2px; font-size: 12px; touch-action: none; }
  .side-more { flex: none; width: 26px; height: 26px; padding: 0; border: 0; border-radius: 6px; background: transparent;
    color: var(--ink-soft); font-size: 15px; }
  .side-grip:hover, .side-more:hover { color: var(--ink); }
  .side-album.album-ghost { opacity: .4; }
  #album-desc-input { min-height: 64px; }
````

### E04 — CSS: o menu do álbum vira folha no celular

**Arquivo:** `app/index.html`

**Ancora:**

````
    #track-pop { left: 0 !important; right: 0; top: auto !important; bottom: 0; width: auto; border-radius: 16px 16px 0 0;
      padding: 8px 8px 20px; max-height: 80vh; overflow: auto; }
    #track-pop [role="menuitem"] { min-height: 52px; font-size: 15px; }
    #track-pop .kbd-hint { display: none; }
````

**Texto novo (substitui a ancora inteira):**

````
    #track-pop, #album-pop { left: 0 !important; right: 0; top: auto !important; bottom: 0; width: auto; border-radius: 16px 16px 0 0;
      padding: 8px 8px 20px; max-height: 80vh; overflow: auto; }
    #track-pop [role="menuitem"], #album-pop [role="menuitem"] { min-height: 52px; font-size: 15px; }
    #track-pop .kbd-hint, #album-pop .kbd-hint { display: none; }
    .album-head .album-more { min-width: 44px; min-height: 44px; }
    #album-pop .tm-row { flex-direction: row; gap: 4px; }
````

### E05 — HTML: o menu do álbum

**Arquivo:** `app/index.html`

**Ancora:**

````
<div class="batch" id="batch" role="toolbar" aria-label="Ações em lote" hidden>
````

**Texto novo (substitui a ancora inteira):**

````
<!-- 0.18 (i-049): o «⋯» do album, no cabecalho e na lateral. -->
<div class="pop" id="album-pop" role="menu" aria-labelledby="album-pop-title" hidden>
  <div class="pop-head" id="album-pop-title"></div>
  <button type="button" role="menuitem" id="am-rename">Renomear…</button>
  <div class="tm-row">
    <button type="button" role="menuitem" id="am-up">Subir álbum<span class="kbd-hint">Alt+↑</span></button>
    <button type="button" role="menuitem" id="am-down">Descer álbum<span class="kbd-hint">Alt+↓</span></button>
  </div>
  <button type="button" role="menuitem" id="am-merge">Juntar com…</button>
  <div class="pop-sep"></div>
  <button type="button" role="menuitem" id="am-md">Exportar álbum .md</button>
  <button type="button" role="menuitem" id="am-json">Exportar álbum .json</button>
  <div class="pop-sep"></div>
  <button type="button" role="menuitem" class="tm-danger" id="am-delete">Excluir álbum…</button>
  <p class="pop-note" id="am-note" hidden>Para organizar, importe o .json: a cópia guardada é o rascunho.</p>
  <button type="button" role="menuitem" class="mobile-only" id="am-cancel">Cancelar</button>
</div>
<div class="batch" id="batch" role="toolbar" aria-label="Ações em lote" hidden>
````

### E06 — HTML: as janelas de renomear e de juntar

**Arquivo:** `app/index.html`

**Ancora:**

````
<dialog class="prompt-dialog" id="move-dialog" aria-labelledby="move-dialog-title">
````

**Texto novo (substitui a ancora inteira):**

````
<!-- 0.18 (i-049): renomear e juntar albuns. -->
<dialog class="prompt-dialog" id="album-dialog" aria-labelledby="album-dialog-title">
  <h2 id="album-dialog-title">Renomear álbum</h2>
  <label for="album-title-input">Título</label>
  <input type="text" id="album-title-input" autocomplete="off">
  <p class="pop-note" id="album-dup-note" hidden>Já existe um álbum com este nome.</p>
  <label for="album-desc-input">Descrição (opcional; não vai para o Suno)</label>
  <textarea id="album-desc-input" rows="2"></textarea>
  <p class="pop-note" id="album-id-note"></p>
  <div class="dialog-actions">
    <button type="button" id="album-cancel-btn">cancelar</button>
    <button type="button" id="album-ok-btn" class="spacer">renomear</button>
  </div>
</dialog>

<dialog class="prompt-dialog" id="merge-dialog" aria-labelledby="merge-dialog-title">
  <h2 id="merge-dialog-title">Juntar álbuns</h2>
  <label for="merge-target">Juntar com</label>
  <select id="merge-target"></select>
  <p id="merge-text"></p>
  <div class="dialog-actions">
    <button type="button" id="merge-cancel-btn">cancelar</button>
    <button type="button" id="merge-ok-btn" class="spacer">juntar</button>
  </div>
</dialog>

<dialog class="prompt-dialog" id="move-dialog" aria-labelledby="move-dialog-title">
````

### E07 — render: o «⋯» do álbum no lugar do «exportar álbum .md»

**Arquivo:** `app/index.html`

**Ancora:**

````
    // botao de exportar este album em .md
    const albMd = document.createElement("button");
    albMd.className = "album-md"; albMd.textContent = "exportar álbum .md";
    albMd.addEventListener("click", () => {
      downloadFile(slug(album.title) + ".md", albumToMarkdown(album), "text/markdown");
      toast("Álbum exportado: " + album.title);
    });
    sec.querySelector(".album-head").appendChild(albMd);
````

**Texto novo (substitui a ancora inteira):**

````
    // 0.18 (i-049): o «⋯» do album; o «exportar album .md» de antes mora nele.
    const albMore = document.createElement("button");
    albMore.type = "button"; albMore.className = "album-more"; albMore.textContent = "⋯";
    albMore.dataset.album = album.id;
    albMore.setAttribute("aria-haspopup", "menu"); albMore.setAttribute("aria-expanded", "false");
    albMore.setAttribute("aria-label", "Ações do álbum " + album.title);
    albMore.addEventListener("click", e => openAlbumMenu(album.id, e.currentTarget));
    sec.querySelector(".album-head").appendChild(albMore);
````

### E08 — lateral: alça e «⋯» em cada álbum

**Arquivo:** `app/index.html`

**Ancora:**

````
  const item = (title, n, id) => {
    const li = document.createElement("li");
````

**Texto novo (substitui a ancora inteira):**

````
  const item = (title, n, id) => {
    const li = document.createElement("li");
    // 0.18 (i-049): cada album ganha a alca (arrastar para reordenar, so com rascunho) e o «⋯».
    if (id) {
      li.className = "side-album"; li.dataset.album = id;
      if (App.saved) {
        const g = document.createElement("button");
        g.type = "button"; g.className = "side-grip"; g.textContent = "⋮⋮"; g.tabIndex = -1;
        g.setAttribute("aria-label", "Arrastar o álbum " + title + " (ou Alt+↑ e Alt+↓ no nome)");
        li.appendChild(g);
      }
    }
````

### E09 — lateral: o «⋯» depois do nome

**Arquivo:** `app/index.html`

**Ancora:**

````
    b.addEventListener("click", () => { document.getElementById("filter-album").value = id; render(); });
    li.appendChild(b); ul.appendChild(li);
  };
````

**Texto novo (substitui a ancora inteira):**

````
    b.addEventListener("click", () => { document.getElementById("filter-album").value = id; render(); });
    li.appendChild(b);
    if (id) {
      const m = document.createElement("button");
      m.type = "button"; m.className = "side-more"; m.textContent = "⋯"; m.dataset.album = id;
      m.setAttribute("aria-haspopup", "menu"); m.setAttribute("aria-expanded", "false");
      m.setAttribute("aria-label", "Ações do álbum " + title);
      m.addEventListener("click", e => openAlbumMenu(id, e.currentTarget));
      li.appendChild(m);
    }
    ul.appendChild(li);
  };
````

### E10 — lateral: liga o arrastar dos álbuns

**Arquivo:** `app/index.html`

**Ancora:**

````
  nb.textContent = "+ Novo álbum (solte aqui)";
  nl.appendChild(nb); ul.appendChild(nl);
}
````

**Texto novo (substitui a ancora inteira):**

````
  nb.textContent = "+ Novo álbum (solte aqui)";
  nl.appendChild(nb); ul.appendChild(nl);
  setupAlbumSortable(ul);   // 0.18
}
````

### E11 — Esc fecha o menu do álbum

**Arquivo:** `app/index.html`

**Ancora:**

````
    if (trackMenuFor) { e.preventDefault(); e.stopImmediatePropagation(); closeTrackMenu(true); return; }
````

**Texto novo (substitui a ancora inteira):**

````
    if (trackMenuFor) { e.preventDefault(); e.stopImmediatePropagation(); closeTrackMenu(true); return; }
    if (albumMenuFor) { e.preventDefault(); e.stopImmediatePropagation(); closeAlbumMenu(true); return; }
````

### E12 — Alt+↑/↓ no nome do álbum da lateral

**Arquivo:** `app/index.html`

**Ancora:**

````
  if (e.altKey && !e.ctrlKey && !e.metaKey && (e.key === "ArrowUp" || e.key === "ArrowDown")
      && t && t.classList && t.classList.contains("row-open")) {
````

**Texto novo (substitui a ancora inteira):**

````
  // 0.18: Alt+↑/↓ no nome de um album da lateral sobe e desce o album.
  if (e.altKey && !e.ctrlKey && !e.metaKey && (e.key === "ArrowUp" || e.key === "ArrowDown")
      && t && t.classList && t.classList.contains("side-item") && t.dataset.album) {
    e.preventDefault(); e.stopImmediatePropagation();
    if (App.saved) moveAlbumAndFocus(t.dataset.album, e.key === "ArrowUp" ? -1 : 1);
    return;
  }
  if (e.altKey && !e.ctrlKey && !e.metaKey && (e.key === "ArrowUp" || e.key === "ArrowDown")
      && t && t.classList && t.classList.contains("row-open")) {
````

### E13 — o bloco da 0.18

**Arquivo:** `app/index.html`

**Ancora:**

````
/* ---- Arrastar ---- */
````

**Texto novo (substitui a ancora inteira):**

````
/* ===================================================================
   Organizar os albuns (0.18.0, i-049 — spec meta/specs/261109-organizar-os-albuns.md,
   DEC-035). O «⋯» do album (cabecalho e lateral): renomear (titulo e
   descricao; o id nao muda), subir e descer, juntar com outro (as faixas vao
   para o fim do destino, que guarda id, titulo e descricao), exportar .md e
   .json, excluir com as faixas. Tudo e operacao de rascunho: beginEdit antes,
   afterEdit depois, um «Desfazer» (I3). Na lateral, a alca arrasta o album.
   =================================================================== */
let albumMenuFor = null, albumMenuAnchor = null;
const findAlbum = id => (App.collection && App.collection.albums || []).find(a => a.id === id) || null;

/** Abre o «⋯» de um album abaixo do botao (no celular, a folha de baixo). */
function openAlbumMenu(id, anchor) {
  const album = findAlbum(id);
  if (!album) return;
  if (albumMenuFor === id && albumMenuAnchor === anchor) { closeAlbumMenu(true); return; }
  closeAlbumMenu(false); closeTrackMenu(false); closePopovers(false);
  albumMenuFor = id; albumMenuAnchor = anchor;
  const list = App.collection.albums, i = list.indexOf(album), can = App.saved;
  document.getElementById("album-pop-title").textContent = album.title;
  document.getElementById("am-rename").disabled = !can;
  document.getElementById("am-up").disabled = !can || i === 0;
  document.getElementById("am-down").disabled = !can || i === list.length - 1;
  document.getElementById("am-merge").disabled = !can || list.length < 2;
  document.getElementById("am-delete").disabled = !can;
  document.getElementById("am-note").hidden = can;
  const pop = document.getElementById("album-pop");
  pop.hidden = false;
  document.getElementById("track-backdrop").hidden = !isMobile();
  anchor.setAttribute("aria-expanded", "true");
  if (!isMobile()) {
    const r = anchor.getBoundingClientRect(), h = pop.offsetHeight, w = pop.offsetWidth;
    const top = r.bottom + 4 + h > window.innerHeight ? Math.max(8, r.top - 4 - h) : r.bottom + 4;
    pop.style.top = top + "px";
    // Na lateral, o menu abre para a direita; no cabecalho, alinhado pela direita do botao.
    const left = anchor.classList.contains("side-more") ? r.left : r.right - w;
    pop.style.left = Math.max(8, Math.min(window.innerWidth - w - 8, left)) + "px";
  } else { pop.style.top = ""; pop.style.left = ""; }
  const first = [...pop.querySelectorAll('[role="menuitem"]')].find(b => !b.disabled && b.offsetParent !== null);
  if (first) first.focus();
}
function closeAlbumMenu(restore) {
  if (!albumMenuFor) return;
  document.getElementById("album-pop").hidden = true;
  if (!trackMenuFor) document.getElementById("track-backdrop").hidden = true;
  const a = albumMenuAnchor;
  albumMenuFor = null; albumMenuAnchor = null;
  if (a) { a.setAttribute("aria-expanded", "false"); if (restore && a.isConnected) a.focus(); }
}
/** Liga um item do menu do album: fecha o menu e roda a acao com o album. */
function albumItem(elId, fn) {
  document.getElementById(elId).addEventListener("click", () => {
    const id = albumMenuFor;
    closeAlbumMenu(false);
    const album = id && findAlbum(id);
    if (album) fn(album);
  });
}

/** Subir/Descer: troca com o vizinho na lista de albuns. */
async function moveAlbumBy(id, d) {
  const list = App.collection.albums, i = list.findIndex(a => a.id === id), j = i + d;
  if (i < 0 || j < 0 || j >= list.length) return;
  beginEdit();
  [list[i], list[j]] = [list[j], list[i]];
  await afterEdit("«" + list[j].title + "» " + (d < 0 ? "subiu" : "desceu") + " na lista de álbuns");
}
/** Alt+↑/↓ na lateral: move e devolve o foco ao nome do album. */
async function moveAlbumAndFocus(id, d) {
  await moveAlbumBy(id, d);
  const b = document.querySelector('#side .side-item[data-album="' + CSS.escape(id) + '"]');
  if (b) b.focus({ preventScroll: true });
}

/** Renomear: titulo e descricao numa janela. O id nao muda (DEC-035). Sem
    mudanca, nao conta alteracao. Descricao vazia tira o campo do album. */
function openRenameDialog(album) {
  const dlg = document.getElementById("album-dialog");
  const ti = document.getElementById("album-title-input"), de = document.getElementById("album-desc-input");
  const ok = document.getElementById("album-ok-btn"), dup = document.getElementById("album-dup-note");
  ti.value = album.title; de.value = album.description || "";
  document.getElementById("album-id-note").textContent =
    "O id do álbum (" + album.id + ") não muda: filtros, exportações e faixas continuam valendo.";
  const sync = () => {
    const t = ti.value.trim();
    ok.disabled = !t;
    dup.hidden = !App.collection.albums.some(a => a !== album && a.title.trim() === t);
  };
  ti.oninput = sync; sync();
  document.getElementById("album-cancel-btn").onclick = () => dlg.close();
  ok.onclick = async () => {
    const t = ti.value.trim(), d = de.value.trim();
    if (!t) { ti.focus(); return; }
    dlg.close();
    if (t === album.title && d === (album.description || "")) return;
    beginEdit();
    const before = album.title;
    album.title = t;
    if (d) album.description = d; else delete album.description;
    await afterEdit(t === before ? "Descrição de «" + t + "» alterada" : "«" + before + "» agora se chama «" + t + "»");
  };
  dlg.showModal();
  ti.select();
}

/** Juntar: as faixas do album de origem vao para o fim do destino, na ordem; a
    origem sai; ficam o id, o titulo e a descricao do destino. O filtro que
    apontava para a origem passa a apontar para o destino. */
function openMergeDialog(src) {
  const others = App.collection.albums.filter(a => a !== src);
  if (!others.length) return;
  const dlg = document.getElementById("merge-dialog"), sel = document.getElementById("merge-target");
  document.getElementById("merge-dialog-title").textContent = "Juntar «" + src.title + "» com…";
  sel.innerHTML = "";
  others.forEach(a => sel.appendChild(new Option(a.title + " (" + nPlural((a.songs || []).length, "faixa", "faixas") + ")", a.id)));
  const sync = () => {
    const dst = findAlbum(sel.value);
    document.getElementById("merge-text").textContent = dst ? "As " + nPlural(src.songs.length, "faixa", "faixas")
      + " de «" + src.title + "» vão para o fim de «" + dst.title + "», na ordem em que estão, e «" + src.title
      + "» sai. Ficam o nome e a descrição de «" + dst.title + "»." : "";
  };
  sel.onchange = sync; sync();
  document.getElementById("merge-cancel-btn").onclick = () => dlg.close();
  document.getElementById("merge-ok-btn").onclick = async () => {
    const dst = findAlbum(sel.value);
    dlg.close();
    if (dst) await mergeAlbums(src.id, dst.id);
  };
  dlg.showModal();
}
async function mergeAlbums(srcId, dstId) {
  const src = findAlbum(srcId), dst = findAlbum(dstId);
  if (!src || !dst || src === dst) return;
  beginEdit();
  const n = (src.songs || []).length;
  dst.songs = (dst.songs || []).concat(src.songs || []);
  App.collection.albums.splice(App.collection.albums.indexOf(src), 1);
  const fa = document.getElementById("filter-album");
  if (fa.value === srcId) fa.value = dstId;   // o rerender guarda o escolhido, se ele existir
  await afterEdit("«" + src.title + "» juntou-se a «" + dst.title + "» (" + nPlural(n, "faixa", "faixas") + ")");
}

/** Excluir o album com as faixas: confirma com a contagem; saem tambem as marcas
    «usei», os modulos ligados e o BPM das faixas. O «Desfazer» volta tudo. */
async function deleteAlbum(id) {
  const album = findAlbum(id);
  if (!album) return;
  const n = (album.songs || []).length;
  if (!(await confirmAsk("Excluir «" + album.title + "» com as " + nPlural(n, "faixa", "faixas")
      + " dele, do rascunho? Para manter as faixas, use «Juntar com…».", "excluir álbum e " + nPlural(n, "faixa", "faixas")))) return;
  beginEdit();
  App.collection.albums.splice(App.collection.albums.indexOf(album), 1);
  (album.songs || []).forEach(s => forgetSongMarks(s.id));
  await afterEdit("«" + album.title + "» excluído com " + nPlural(n, "faixa", "faixas"));
}

/** Exportar o album em .json: um acervo com ele (titulo, descricao e faixas) e
    os modulos que as faixas citam, como o exportar de uma faixa (DEC-028). */
function exportAlbumJson(album) {
  const coll = App.collection;
  const json = { schemaVersion: coll.schemaVersion || "1.0", title: album.title };
  if (coll.targetTool) json.targetTool = coll.targetTool;
  const copy = JSON.parse(JSON.stringify(album));
  json.albums = [copy];
  const mods = [], seen = new Set();
  let missing = 0;
  (album.songs || []).forEach(s => (s.styleModules || []).forEach(id => {
    const m = typeof id === "string" ? App.modulesById[id] : null;
    if (!m) { missing++; return; }
    if (seen.has(id)) return;
    seen.add(id); mods.push(JSON.parse(JSON.stringify(m)));
  }));
  if (mods.length) json.styleModules = mods;
  stripInternalKeys(json);
  const name = album.id + ".json";
  downloadFile(name, JSON.stringify(json, null, 2), "application/json");
  toast("Álbum exportado em .json: " + name + " · " + nPlural(mods.length, "módulo", "módulos")
    + (missing ? " · " + missing + " módulo(s) citado(s) não existe(m) no acervo" : ""));
}

albumItem("am-rename", a => openRenameDialog(a));
albumItem("am-up", a => moveAlbumBy(a.id, -1));
albumItem("am-down", a => moveAlbumBy(a.id, 1));
albumItem("am-merge", a => openMergeDialog(a));
albumItem("am-md", a => { downloadFile(slug(a.title) + ".md", albumToMarkdown(a), "text/markdown"); toast("Álbum exportado: " + a.title); });
albumItem("am-json", a => exportAlbumJson(a));
albumItem("am-delete", a => deleteAlbum(a.id));
document.getElementById("am-cancel").addEventListener("click", () => closeAlbumMenu(true));
document.getElementById("track-backdrop").addEventListener("click", () => closeAlbumMenu(true));
document.addEventListener("pointerdown", e => {
  if (!albumMenuFor) return;
  if (document.getElementById("album-pop").contains(e.target) || (albumMenuAnchor && albumMenuAnchor.contains(e.target))) return;
  closeAlbumMenu(false);
});

/** Arrastar os albuns na lateral pela alca: grupo proprio, separado do das
    faixas (a faixa arrastada continua caindo SOBRE o album, I3). */
let albumSortable = null;
function setupAlbumSortable(ul) {
  if (albumSortable) { try { albumSortable.destroy(); } catch (e) { /* lista redesenhada */ } albumSortable = null; }
  if (typeof Sortable === "undefined" || !App.saved || !ul) return;
  albumSortable = Sortable.create(ul, {
    group: "albuns", handle: ".side-grip", draggable: "li.side-album",
    animation: 120, forceFallback: true, fallbackOnBody: true, fallbackTolerance: 3,
    ghostClass: "album-ghost",
    onEnd: async () => {
      // O mesmo clique sintetico do dragEnd das faixas (armadilha da I3).
      setTimeout(() => document.body.dispatchEvent(new MouseEvent("click", { bubbles: true })), 0);
      const order = [...ul.querySelectorAll("li.side-album")].map(li => li.dataset.album);
      const list = App.collection.albums;
      if (order.join("\n") === list.map(a => a.id).join("\n")) return;   // soltar no mesmo lugar nao conta
      beginEdit();
      const byId = new Map(list.map(a => [a.id, a]));
      App.collection.albums = order.map(id => byId.get(id)).filter(Boolean);
      const moved = order.find((id, k) => list[k] && list[k].id !== id);
      await afterEdit("Álbuns reordenados" + (moved ? ": «" + byId.get(moved).title + "» mudou de lugar" : ""));
    },
  });
}

/* ---- Arrastar ---- */
````

### E14 — a lateral ganha as alças quando a cópia guardada fica pronta

**Arquivo:** `app/index.html`

**Ancora:**

````
  setupSortables();
  syncSelection();
}

/* ---- Soltar um .json sobre um album ---- */
````

**Texto novo (substitui a ancora inteira):**

````
  setupSortables();
  syncSelection();
  renderSide(currentFilters());   // 0.18: as alcas dos albuns na lateral (so a lateral; nao redesenha a lista)
}

/* ---- Soltar um .json sobre um album ---- */
````

### E15 — esperar o exemplo carregado sozinho

**Arquivo:** `tests/test_organizar.py`

**Ancora:**

````
    page = open_app()
    page.evaluate("d => { setCollection(d); App.saved = false; render(); }", DEMO)
````

**Texto novo (substitui a ancora inteira):**

````
    page = open_app()
    page.wait_for_function("App.collection && App.collection.albums")   # o exemplo carregado sozinho (http://)
    page.evaluate("d => { setCollection(d); App.saved = false; render(); }", DEMO)
````

### E16 — entrada [0.18.0]

**Arquivo:** `meta/CHANGELOG.md`

**Ancora:**

````
## [0.17.0] — 2026-11-06
````

**Texto novo (substitui a ancora inteira):**

````
## [0.18.0] — 2026-11-09

Organizar os álbuns, não só as faixas (i-049, DEC-035).

### Added
- **O «⋯» do álbum**, no cabeçalho de cada álbum (Lista e Cartões) e ao lado de cada álbum da lateral: Renomear…, Subir álbum e Descer álbum, Juntar com…, Exportar álbum .md, Exportar álbum .json e Excluir álbum…. No celular, ele abre a folha de baixo.
- **Renomear** numa janela, com o título e a descrição do álbum (o campo `description` do esquema, que já existia e passa a aparecer no cabeçalho). O id do álbum não muda. Título igual ao de outro álbum é permitido, com aviso.
- **Reordenar os álbuns** arrastando pela alça ⋮⋮ da lateral, ou com Subir e Descer no «⋯»; `Alt+↑` e `Alt+↓` no nome do álbum da lateral.
- **Juntar com…:** as faixas vão para o fim do álbum escolhido, na ordem; o de origem sai; ficam o id, o título e a descrição do destino. O filtro de álbum acompanha.
- **Excluir álbum…** com as faixas, confirmando com a contagem no botão; saem também as marcas «usei» delas.
- **Exportar álbum .json:** um acervo com o álbum e os módulos que as faixas citam, que importa como qualquer acervo.

### Changed
- O botão «exportar álbum .md» do cabeçalho mora agora no «⋯» do álbum.

Todas as operações têm «Desfazer» e `Ctrl+Z`, como as das faixas. Spec `meta/specs/261109-organizar-os-albuns.md`: 10 de 10 critérios, com 12 testes novos em `tests/test_albuns.py` (44 no total), que reprovam no app da 0.17.0. Abrir 205 faixas: de 246 a 289 ms, contra 251 a 319 ms da 0.17.0 nas mesmas rodadas (sem diferença medível).

---

## [0.17.0] — 2026-11-06
````

### E17 — estado v0.18.0

**Arquivo:** `README.md`

**Ancora:**

````
> **Estado:** v0.17.0 — ferramenta em uso. Lê, guarda e edita vários acervos, grava direto no arquivo do acervo (Chrome e Edge), copia por campo, troca módulos de estilo, ajusta o BPM, **mede cada prompt contra os limites do Suno**, exporta Markdown, exporta uma faixa como `.json` e **entrega o prompt para chats gerarem canções no esquema**. Publicada no GitHub Pages. Ver `meta/ROADMAP.md`.
````

**Texto novo (substitui a ancora inteira):**

````
> **Estado:** v0.18.0 — ferramenta em uso. Lê, guarda e edita vários acervos, grava direto no arquivo do acervo (Chrome e Edge), copia por campo, troca módulos de estilo, ajusta o BPM, **mede cada prompt contra os limites do Suno**, exporta Markdown, exporta uma faixa como `.json` e **entrega o prompt para chats gerarem canções no esquema**. Publicada no GitHub Pages. Ver `meta/ROADMAP.md`.
````

### E18 — passo 7: os álbuns

**Arquivo:** `README.md`

**Ancora:**

````
7. Para reorganizar, não há nada a ligar: na Lista, arraste a faixa pela alça ⋮⋮ (para outra posição, outro álbum ou um álbum da lateral; durante o arrastar, a lateral oferece *+ Novo álbum*), ou use o «⋯» da faixa (*Mover para…*, *Subir*, *Descer*, *Excluir…*; `Alt+↑` e `Alt+↓` no título). Marque as caixas para mover, exportar, marcar ou excluir várias de uma vez. Cada operação mostra *Desfazer* no aviso (ou `Ctrl+Z`), até a próxima. Para trazer faixas de outro `.json`, use *Importar faixas…* no «⋯» da barra, ou solte o arquivo sobre um álbum. As mudanças ficam num rascunho no navegador; a barra mostra quantas são. No Chrome e no Edge do computador, *Salvar* (ou `Ctrl+S`) grava no próprio `.json`: na primeira vez, a janela do sistema pede o arquivo, já com o nome; daí em diante grava direto, e avisa se o arquivo mudou fora do app. O ▾ ao lado tem *Salvar em outro arquivo…* e *Baixar .json*. No Firefox, no Safari e no celular, *Salvar .json* baixa com o nome do arquivo original — substitua o antigo por ele, e ele passa a ser a fonte. Só se organiza um acervo com cópia guardada no navegador (importado por arquivo); no exemplo que o Pages carrega sozinho, o «⋯» só exporta.
````

**Texto novo (substitui a ancora inteira):**

````
7. Para reorganizar, não há nada a ligar: na Lista, arraste a faixa pela alça ⋮⋮ (para outra posição, outro álbum ou um álbum da lateral; durante o arrastar, a lateral oferece *+ Novo álbum*), ou use o «⋯» da faixa (*Mover para…*, *Subir*, *Descer*, *Excluir…*; `Alt+↑` e `Alt+↓` no título). Marque as caixas para mover, exportar, marcar ou excluir várias de uma vez. Os álbuns têm o próprio «⋯», no cabeçalho e na lateral: *Renomear…* (título e descrição), *Subir álbum*, *Descer álbum*, *Juntar com…* e *Excluir álbum…*; na lateral, a alça ⋮⋮ de cada álbum arrasta. Cada operação mostra *Desfazer* no aviso (ou `Ctrl+Z`), até a próxima. Para trazer faixas de outro `.json`, use *Importar faixas…* no «⋯» da barra, ou solte o arquivo sobre um álbum. As mudanças ficam num rascunho no navegador; a barra mostra quantas são. No Chrome e no Edge do computador, *Salvar* (ou `Ctrl+S`) grava no próprio `.json`: na primeira vez, a janela do sistema pede o arquivo, já com o nome; daí em diante grava direto, e avisa se o arquivo mudou fora do app. O ▾ ao lado tem *Salvar em outro arquivo…* e *Baixar .json*. No Firefox, no Safari e no celular, *Salvar .json* baixa com o nome do arquivo original — substitua o antigo por ele, e ele passa a ser a fonte. Só se organiza um acervo com cópia guardada no navegador (importado por arquivo); no exemplo que o Pages carrega sozinho, o «⋯» só exporta.
````

### E19 — DEC-035

**Arquivo:** `meta/DECISIONS.md`

**Ancora:**

````
**Consequências:** (+) Toda mudança roda contra tudo o que já funcionava, inclusive o arrastar da I3; o esquema passa a ser conferido a cada push (fecha na prática a pendência do `jsonschema` e a i-016). (+) A ida e volta do acervo vira teste (i-025). (−) O teste não abre a janela real do sistema nem o aviso de permissão: isso continua no roteiro de tela do dono. (−) Trocar a versão do Playwright, do Chromium ou da SortableJS pode quebrar o teste de arrastar; o CI acusa. (−) Empurrar um arquivo em `.github/workflows/` exige que a credencial do Git tenha o escopo `workflow`.
````

**Texto novo (substitui a ancora inteira):**

````
**Consequências:** (+) Toda mudança roda contra tudo o que já funcionava, inclusive o arrastar da I3; o esquema passa a ser conferido a cada push (fecha na prática a pendência do `jsonschema` e a i-016). (+) A ida e volta do acervo vira teste (i-025). (−) O teste não abre a janela real do sistema nem o aviso de permissão: isso continua no roteiro de tela do dono. (−) Trocar a versão do Playwright, do Chromium ou da SortableJS pode quebrar o teste de arrastar; o CI acusa. (−) Empurrar um arquivo em `.github/workflows/` exige que a credencial do Git tenha o escopo `workflow`.

## DEC-035 — Organizar os álbuns: «⋯» no cabeçalho e na lateral, renomear numa janela sem mudar o id, arrastar na lateral, juntar no fim do destino e excluir com confirmação

**Data:** 2026-11-09
**Status:** aceita
**Contexto:** A I3 organizou as faixas; os álbuns só nasciam e sumiam ao esvaziar (i-049). A spec `meta/specs/261109-organizar-os-albuns.md` trouxe cinco pontos, decididos pelo dono em 2026-11-09, os cinco como recomendados `[relatado pelo dono]`.
**Decisão:**
- **O «⋯» do álbum mora no cabeçalho** (Lista e Cartões, inclusive no celular) **e na lateral** (a partir de 1280 px). O «exportar álbum .md» do cabeçalho entra nele, junto de um «Exportar álbum .json».
- **Renomear numa janela**, com título e descrição (o `description` do esquema). **O id do álbum não muda.**
- **Reordenar arrastando pela alça da lateral** (SortableJS, grupo próprio, separado do das faixas) **e por Subir/Descer no «⋯»**, com `Alt+↑`/`Alt+↓`.
- **Juntar:** as faixas da origem vão para o fim do destino, na ordem; ficam id, título e descrição do destino.
- **Excluir álbum** existe, com a contagem de faixas no botão da confirmação e «Desfazer».
**Alternativas consideradas:** o «⋯» só na lateral (some abaixo de 1280 px e no celular); renomear com clique duplo no título (sem a descrição, e compete com o clique que filtra); mudar o id junto com o título (quebra filtros e referências); só Subir/Descer (lento com 12 álbuns); perguntar nome e posição ao juntar (uma pergunta a mais por junção); não ter «Excluir álbum» (o mais seguro, e o mais lento).
**Consequências:** (+) Organizar o acervo inteiro sem editar o `.json` à mão. (+) A descrição do álbum, que estava no esquema desde a fase 1, ganha uso. (−) Excluir álbum é a operação mais destrutiva do app (dezenas de faixas num clique); seguram a confirmação com a contagem, o «Desfazer» e, no arquivo, o aviso de mudança da I4. (−) Dois arrastares na lateral: o teste da I3 que solta faixa sobre álbum da lateral virou teste de regressão (`tests/test_albuns.py`).
````

### E20 — i-049 entregue (título)

**Arquivo:** `meta/IDEAS.md`

**Ancora:**

````
### i-049 💡 Organizar os álbuns
````

**Texto novo (substitui a ancora inteira):**

````
### i-049 ✅ Organizar os álbuns
````

### E21 — i-049 entregue (linha)

**Arquivo:** `meta/IDEAS.md`

**Ancora:**

````
`[capturada pelo chat, 2026-11-06, na spec da I3]` Renomear um álbum, reordenar os álbuns arrastando na lateral e juntar dois. A I3 organiza as faixas; os álbuns só nascem (pelo «+ Novo álbum» ou pelo «Mover para…») e somem quando esvaziam. Fora da I3 por escopo.
````

**Texto novo (substitui a ancora inteira):**

````
`[capturada pelo chat, 2026-11-06, na spec da I3]` Renomear um álbum, reordenar os álbuns arrastando na lateral e juntar dois. A I3 organiza as faixas; os álbuns só nascem (pelo «+ Novo álbum» ou pelo «Mover para…») e somem quando esvaziam. Fora da I3 por escopo.
**Entregue (0.18.0, DEC-035):** o «⋯» do álbum (cabeçalho e lateral) com Renomear (título e descrição; o id não muda), Subir/Descer, Juntar com…, Exportar .md e .json e Excluir álbum; arrastar na lateral pela alça. Spec `meta/specs/261109-organizar-os-albuns.md`.
````

### E22 — organizar os álbuns

**Arquivo:** `meta/ROADMAP.md`

**Ancora:**

````
- ✅ Frente de interface (i-043 a i-048, DEC-030 a DEC-033), em quatro entregas: ✅ barra única, com o seletor de acervo, os filtros com etiquetas e o «⋯» (0.14.0) · ✅ lista e detalhe, com a lateral de álbuns e acervos (0.15.0) · ✅ organizar: arrastar, «⋯» por faixa, lote, «Desfazer», sem o interruptor «editar» (0.16.0) · ✅ salvar direto no arquivo, onde o navegador deixa (0.17.0, DEC-033).
````

**Texto novo (substitui a ancora inteira):**

````
- ✅ Frente de interface (i-043 a i-048, DEC-030 a DEC-033), em quatro entregas: ✅ barra única, com o seletor de acervo, os filtros com etiquetas e o «⋯» (0.14.0) · ✅ lista e detalhe, com a lateral de álbuns e acervos (0.15.0) · ✅ organizar: arrastar, «⋯» por faixa, lote, «Desfazer», sem o interruptor «editar» (0.16.0) · ✅ salvar direto no arquivo, onde o navegador deixa (0.17.0, DEC-033).
- ✅ Organizar os álbuns: renomear, reordenar, juntar, exportar e excluir (0.18.0, i-049, DEC-035).
````

### E23 — versão

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
**Versão atual:** 0.17.0 · **Fase:** 3a, 3a.2, o BPM da 3b, o prompt-modelo e as conveniências de uso concluídos e conferidos · os álbuns antigos convertidos (i-008, fora do repo) · curadoria no app concluída nas três entregas (DEC-028, DEC-029) · frente de interface concluída e conferida nas quatro entregas (DEC-030 a DEC-033) · kit de música lido pelo KCM, à espera da resposta (i-039)
````

**Texto novo (substitui a ancora inteira):**

````
**Versão atual:** 0.18.0 · **Fase:** 3a, 3a.2, o BPM da 3b, o prompt-modelo e as conveniências de uso concluídos e conferidos · os álbuns antigos convertidos (i-008, fora do repo) · curadoria no app concluída nas três entregas (DEC-028, DEC-029) · frente de interface concluída e conferida nas quatro entregas (DEC-030 a DEC-033) · organizar os álbuns (0.18.0, DEC-035) à espera da conferência na tela · kit de música lido pelo KCM, à espera da resposta (i-039)
````

### E24 — última conversa

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
## Última conversa (2026-11-09, I4 conferida, i-051 e o kit de música v2)

- **I4 conferida na tela pelo dono** (os 10 itens do roteiro OK `[relatado pelo dono]`, WO 0031): salvar no arquivo (0.17.0) está fechado, e a frente de interface, com as quatro entregas.
- **i-051, testes do navegador no CI** (DEC-034, WO 0032): `tests/` com 32 testes, só com dados sintéticos, e o GitHub Actions a cada push, com o `validate.py` com esquema e os testes dos conversores. Fecha também a i-016 e a i-025. Aplicada e empurrada (`de49282`); o primeiro ✓ está confirmado: `gh run list` mostra `completed success` para o run «testes» (1m15s) `[medido por instrumento]`.
- **Kit de música v2, leva 1** (WO 0033): o README do kit na 0.17.0, a `macetes-suno` com «Depois de ouvir» (§10) e as ferramentas do Suno de 2026 (§11), e o ciclo do `BLOCO-SUNO.md` com elas. A leva 2 espera um projeto de música para a prova de campo. Aplicada e empurrada (`47bb0cf`); CI `completed success` (run «testes» 42679747519, 1m2s) `[medido por instrumento]`.
- **Este bloco substitui o anterior, da WO 0030** (I4). O que ele dizia está no CHANGELOG [0.17.0], na spec `meta/specs/261106-salvar-no-arquivo.md` e em `logs/2026-11-06.md` (Conversas 11 e 12).

````

**Texto novo (substitui a ancora inteira):**

````
## Última conversa (2026-11-09, organizar os álbuns, WO 0034)

- **Ordem das próximas frentes, decidida pelo dono:** organizar os álbuns (i-049) → rampa de BPM (i-042) → importar os prompts prontos dos álbuns como módulos, que fecha a Fase 3b.
- **Organizar os álbuns (0.18.0, DEC-035):** protótipo no canvas, spec `meta/specs/261109-organizar-os-albuns.md` com os cinco pontos decididos pelo dono como recomendados, 10 de 10 critérios e 12 testes novos (`tests/test_albuns.py`), testados pelo chat; falta a conferência na tela pelo dono.
- **Este bloco substitui o anterior** (I4 conferida, i-051 e o kit v2, leva 1). O que ele dizia está no CHANGELOG [0.17.0], na DEC-034, na análise `meta/analises/261109-ANALISE-kit-de-musica-v2.md` e em `logs/2026-11-09.md` (Conversas 1 a 6).

````

### E25 — funciona: os álbuns

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
- **Organizar** (0.16.0, DEC-030, DEC-032): arrastar pela alça ⋮⋮ na Lista (com filtro, antes da próxima visível) e para os álbuns da lateral ou «+ Novo álbum»; o «⋯» de cada faixa (linha, detalhe e cartão) com Mover, Subir, Descer, Exportar e Excluir, e `Alt+↑`/`Alt+↓`; caixas e barra de lote; «Desfazer» e `Ctrl+Z` da última operação; soltar o `.json` sobre um álbum importa faixas nele. Só com cópia guardada no navegador. A SortableJS 1.15.7 vai embutida, com o hash no `validate.py`. Conferido na tela pelo dono em 2026-11-06.
````

**Texto novo (substitui a ancora inteira):**

````
- **Organizar** (0.16.0, DEC-030, DEC-032): arrastar pela alça ⋮⋮ na Lista (com filtro, antes da próxima visível) e para os álbuns da lateral ou «+ Novo álbum»; o «⋯» de cada faixa (linha, detalhe e cartão) com Mover, Subir, Descer, Exportar e Excluir, e `Alt+↑`/`Alt+↓`; caixas e barra de lote; «Desfazer» e `Ctrl+Z` da última operação; soltar o `.json` sobre um álbum importa faixas nele. Só com cópia guardada no navegador. A SortableJS 1.15.7 vai embutida, com o hash no `validate.py`. Conferido na tela pelo dono em 2026-11-06.
- **Organizar os álbuns** (0.18.0, DEC-035): o «⋯» do álbum no cabeçalho e na lateral, com Renomear (título e descrição; o id não muda), Subir/Descer (`Alt+↑`/`Alt+↓` na lateral), Juntar com… (no fim do destino), Exportar .md e .json e Excluir álbum (com a contagem e «Desfazer»); na lateral, a alça arrasta o álbum.
````

### E26 — pendências: conferir os álbuns

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
- **Apagar à mão o `..\sonda-i4-teste.json`** — arquivo de teste da sonda, na pasta-pai (o chat não apaga arquivo seu).
````

**Texto novo (substitui a ancora inteira):**

````
- **Conferir organizar os álbuns na tela** — roteiro na conversa de 2026-11-09 (WO 0034), depois do push, no computador e no celular.
- **Apagar à mão o `..\sonda-i4-teste.json`** — arquivo de teste da sonda, na pasta-pai (o chat não apaga arquivo seu).
````

### E27 — backlog na ordem decidida

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
1. **Organizar os álbuns** (i-049) — renomear, reordenar na lateral, juntar dois.
2. **Kit de música v2, leva 2** (i-039) — as skills `escrever-letra-suno` e `conceber-album`, com prova de campo num projeto de música do dono; depois, a carta 02 ao KCM.
3. **Rampa de BPM** (i-042) — três faixas BR reprovam no `validate.py` por mudarem de andamento de propósito.
4. **Pesquisar outras plataformas de música por IA** (i-032) — um turno de pesquisa antes de qualquer mudança de esquema.
5. **Avisar palavra de andamento que contradiz o BPM** (i-029) — pede uma tabela palavra → faixa de BPM, com fonte e data.
6. **Importar prompts prontos dos álbuns como módulos** — o último ⬜ da 3b no ROADMAP; o índice-mestre da BR e os «estilos originais» do VOL5 trazem fórmulas de estilo.

````

**Texto novo (substitui a ancora inteira):**

````
1. **Rampa de BPM** (i-042) — três faixas BR reprovam no `validate.py` por mudarem de andamento de propósito.
2. **Importar prompts prontos dos álbuns como módulos** — o último ⬜ da 3b no ROADMAP; o índice-mestre da BR e os «estilos originais» do VOL5 trazem fórmulas de estilo.
3. **Kit de música v2, leva 2** (i-039) — as skills `escrever-letra-suno` e `conceber-album`, com prova de campo num projeto de música do dono; depois, a carta 02 ao KCM.
4. **Pesquisar outras plataformas de música por IA** (i-032) — um turno de pesquisa antes de qualquer mudança de esquema.
5. **Avisar palavra de andamento que contradiz o BPM** (i-029) — pede uma tabela palavra → faixa de BPM, com fonte e data.

````

## Arquivo novo N01

Crie com o conteudo entre as linhas de quatro crases, mais a quebra de linha final.

### N01 — `tests/test_albuns.py`

````
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
````

## Depois de aplicar — conferencia antes do commit

| # | Checagem | Comando | Esperado |
|---|---|---|---|
| 1 | Os editados e o novo sao os previstos | `sha1sum app/index.html tests/test_organizar.py meta/CHANGELOG.md README.md meta/DECISIONS.md meta/IDEAS.md meta/ROADMAP.md meta/STATUS.md tests/test_albuns.py` | a coluna **chegada**, os 9 |
| 2 | Os tres do chat nao mudaram | `sha1sum meta/CONTEXT.md meta/specs/261109-organizar-os-albuns.md logs/2026-11-09.md` | os sha1 da segunda tabela |
| 3 | Validacao | `python3 scripts/validate.py; echo "exit=$?"` | `exit=0`, com `OK  versao 0.18.0 igual em CHANGELOG, app, README e STATUS` e `OK  biblioteca: SortableJS 1.15.7 embutida sem mudanca` |
| 4 | O codigo entrou uma vez | `grep -c '^async function mergeAlbums' app/index.html` e `grep -c '^<div class="pop" id="album-pop"' app/index.html` | `1` e `1` (linhas) |
| 5 | Os registros | `grep -c '^## \[0.18.0\]' meta/CHANGELOG.md`, `grep -c '^## DEC-035 ' meta/DECISIONS.md` e `grep -c '^### i-049 ' meta/IDEAS.md` | `1`, `1` e `1` |
| 6 | Nada alem do previsto | `GIT_OPTIONAL_LOCKS=0 git status --short --untracked-files=all` | os editados, o novo, os tres do chat e esta WO |
| 7 | Depois do push: o CI | `gh run list --limit 1` | a execucao «testes» do commit desta WO; relate o estado cru. Se ainda estiver em andamento, espere e rode de novo antes de fechar o relatorio |

As checagens 4 e 5 foram rodadas pelo chat no clone, no shell Linux; no Git Bash, **nao testado** — com a 1 verde, relate o cru e nao pare. CI vermelho nao desfaz o push: relate a saida (`gh run view --log-failed`).
**Esta e qual pergunta?** A 1 responde «esta la?»; o CI e o roteiro de tela do dono respondem «presta?».

## Relatorio de aplicacao

Grave em `../AAMMDD-HHMM-code-cancioneiro-apply-wo0034.txt`, com o carimbo de `date +%y%m%d-%H%M` rodado na hora. Checagem 1 em primeiro lugar, e o estado final do CI. **Sem `/wrap` depois desta WO**, e sem secao sua no log, salvo se algo fugir do literal.

## Commit

```
git add app/index.html tests README.md meta/CHANGELOG.md meta/DECISIONS.md meta/IDEAS.md meta/ROADMAP.md meta/STATUS.md meta/CONTEXT.md meta/specs/261109-organizar-os-albuns.md logs/2026-11-09.md meta/workorders/261109-wo0034-organizar-os-albuns.md
```

```
git commit -m "feat: organizar os albuns, versao 0.18.0" -m "i-049 (DEC-035): o menu do album no cabecalho e na lateral, com renomear (titulo e descricao, id fixo), subir e descer, juntar no fim do destino, exportar .md e .json e excluir com confirmacao; arrastar os albuns na lateral. 12 testes novos. Spec com o resultado, CONTEXT, IDEAS, ROADMAP, README, STATUS e log."
```

```
git push
```
