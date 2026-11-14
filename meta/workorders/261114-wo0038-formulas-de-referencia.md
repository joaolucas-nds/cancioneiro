# WO 0038 — Fórmulas de referência (0.20.0)

## Cabecalho

> **Tipo:** versao 0.20.0 — app, `validate.py`, esquema, um arquivo de teste novo e meta (DEC-037).
> **Config sugerida:** Sonnet · `/effort medium` (aplicacao literal por script; muitas edicoes).
> **Pre-requisito:** commit `3805320`, branch `main`, sincronizada com `origin/main`. O `git status --short` mostra exatamente: ` M logs/2026-11-14.md`, ` M meta/specs/261111-formulas.md` e `?? meta/workorders/261114-wo0038-formulas-de-referencia.md`.
> **Base:** spec `meta/specs/261111-formulas.md`, com os quatro pontos decididos pelo dono em 2026-11-14 `[relatado pelo dono]` (DEC-037). O chat implementou e mediu num clone (log de 2026-11-14, Conversa 3).
> **Depende de:** `3805320` (wrap da WO 0037).
>
> | arquivo | partida (sha1) | chegada (sha1) |
> |---|---|---|
> | `app/index.html` | `4e2a2f98ada2ffb67d399b0b081b45b63727cd4a` | `3dc2acc2c678943391ff0b74b184654c24a4eed8` |
> | `scripts/validate.py` | `5b2160f4f5a6b476ba4eeece1f558f4f267d6ed9` | `01b438beae44adfedf1a9323e59d61ef4858b996` |
> | `schema/collection.schema.json` | `575f69ea48f315ae616f36c687518eed964e3fc8` | `c2c30315d4fe91e962a6fb7123de66f5bf66a129` |
> | `README.md` | `d4f485c5b6ac36dc8e5a54346b272a684fccb905` | `49a3609717d47c60133583377421e08b5688d89f` |
> | `meta/CHANGELOG.md` | `af08b09b9bca00d868e277b8921113162ec36070` | `1c78de99d4d8429809344029adeb718c28d3e2a5` |
> | `meta/DECISIONS.md` | `0071d463b41f0a3d1054d1875ef39b87256427df` | `07e0109ca662ed58d2d34ca861427d0fb6e3118b` |
> | `meta/IDEAS.md` | `a53fcd38d64e0e2e2cc7d45e85ed53b508557938` | `7e6e476c87b2a364a1445a46378497870806f72f` |
> | `meta/ROADMAP.md` | `73aa2d231dee311434418d65e04b6d9cb9f32574` | `4cd400f205f5305f1c108ca2bb7f911c88bddeef` |
> | `meta/STATUS.md` | `17042eedb261c2d2d7711109d3c5d92c2287ac39` | `6a79449f19635919f14499cc221d21b72b94e92c` |
> | `tests/test_formulas.py` | (nao existe) | `83fcdb0d66ab0af63f25c99860850acadf9c5027` (arquivo novo, E37) |
> | `meta/specs/261111-formulas.md` | `137293c608acc06567aab7daa1a5c0baa54e579e` | o mesmo (gravado pelo chat; so versionar) |
> | `logs/2026-11-14.md` | `7c130ade88a60d8778d5b5c842a74ba892f32721` | o mesmo (gravado pelo chat; so versionar) |
>
> **Ancora semantica:** se um trecho-ancora nao bater EXATAMENTE, PARE e reporte.
> **Idempotencia:** antes de cada edicao, procure o texto NOVO INTEIRO; se ja estiver la, PULE e diga no relatorio.
> **Ancoras:** linhas inteiras (uma linha ou um bloco de linhas inteiras), cada uma 1 vez no arquivo no momento da edicao, na ordem abaixo. Toda edicao «substitui a ancora inteira».
> **Âncoras lidas em** (lidas pelo chat NESTE turno, de `3805320` clonado do GitHub e conferido contra o disco do dono — os 128 arquivos versionados com o mesmo sha1; aplicadas em ordem num clone, com a chegada medida):
> - E01 (`app/index.html`, CSS: a janela «Fórmulas» e a seção da importação): bloco de 2 linhas, começando por `  .import-list label { font-size: 13px; margin: 0; }`
> - E02 (`app/index.html`, versão 0.20.0): linha `    <span class="version" data-role="app-version">v0.19.0</span>`
> - E03 (`app/index.html`, «⋯» da barra: a entrada «Fórmulas (N)»): bloco de 2 linhas, começando por `      <div class="pop-head mobile-only" id="more-brand">Cancioneiro</div>`
> - E04 (`app/index.html`, lateral: a entrada «Fórmulas», acima de «Todas as faixas»): bloco de 2 linhas, começando por `<nav class="side" id="side" aria-label="Álbuns e acervos" hidden>`
> - E05 (`app/index.html`, janela de importar: a classe import-dialog): linha `<dialog class="prompt-dialog" id="import-dialog" aria-labelledby="import-dialog-title">`
> - E06 (`app/index.html`, janela de importar: a seção «Fórmulas»): bloco de 2 linhas, começando por `  <ul class="import-list" id="import-list"></ul>`
> - E07 (`app/index.html`, janela de importar: o destino num bloco que some sem faixas): bloco de 2 linhas, começando por `  <input type="text" id="import-new-title" placeholder="título do álbum novo" hidden>`
> - E08 (`app/index.html`, a janela «Fórmulas»): bloco de 4 linhas, começando por `</dialog>`
> - E09 (`app/index.html`, copiar: o plano B dentro da janela aberta): bloco de 3 linhas, começando por `    ta.value = text; document.body.appendChild(ta); ta.select();`
> - E10 (`app/index.html`, importar: título e destino conforme a origem): bloco de 2 linhas, começando por `  document.getElementById("import-source").textContent = name;`
> - E11 (`app/index.html`, importar: as fórmulas marcadas seguem para o importTracks): bloco de 2 linhas, começando por `    dlg.close();`
> - E12 (`app/index.html`, importTracks: recebe as fórmulas): linha `async function importTracks(src, keys, dest, newTitle) {`
> - E13 (`app/index.html`, importTracks: importa as fórmulas): bloco de 4 linhas, começando por `  }));`
> - E14 (`app/index.html`, importTracks: o aviso soma faixas e fórmulas; o bloco das fórmulas): bloco de 4 linhas, começando por `  const tail = parts.length ? " · " + parts.join(" · ") : "";`
> - E15 (`app/index.html`, updateBar: «Fórmulas (N)» só com fórmulas): bloco de 2 linhas, começando por `  document.getElementById("menu-import-tracks").hidden = !App.saved;`
> - E16 (`app/index.html`, renderSide: «Fórmulas · N» só com fórmulas): bloco de 2 linhas, começando por `  if (!App.collection) return;`
> - E17 (`app/index.html`, undoLast: a janela das fórmulas acompanha): linha `  toast("Desfeito: " + u.label + (ok ? "" : " · não consegui guardar no navegador: baixe…`
> - E18 (`scripts/validate.py`, docstring: nove coisas): linha `Checa oito coisas:`
> - E19 (`scripts/validate.py`, docstring: o item 9): bloco de 4 linhas, começando por `  8. A SortableJS embutida no app e a 1.15.7 sem mudanca: o sha256 do trecho`
> - E20 (`scripts/validate.py`, check_formulas): bloco de 2 linhas, começando por `        print(f"ERRO de BPM em {rel} ({len(bad)} faixa(s)):")`
> - E21 (`scripts/validate.py`, check_formulas no modo só sintaxe): bloco de 2 linhas, começando por `            errors += check_bpm(data, rel)`
> - E22 (`scripts/validate.py`, a contagem de fórmulas na linha OK): linha `            print(f"OK  {rel}  ({len(data.get('albums', []))} álbuns, {n_songs} faixas)")`
> - E23 (`scripts/validate.py`, check_formulas no modo com esquema): bloco de 4 linhas, começando por `        errors += check_module_refs(data, rel)`
> - E24 (`schema/collection.schema.json`, styleReferences no esquema): bloco de 2 linhas, começando por `    },`
> - E25 (`README.md`, estado v0.20.0): linha `> **Estado:** v0.19.0 — ferramenta em uso. Lê, guarda e edita vários acervos, grava dire…`
> - E26 (`meta/CHANGELOG.md`, entrada [0.20.0]): bloco de 7 linhas, começando por `# CHANGELOG.md — Cancioneiro`
> - E27 (`meta/DECISIONS.md`, DEC-037 implementada): linha `**Status:** aceita — implementação pendente (0.20.0)`
> - E28 (`meta/IDEAS.md`, i-004: os prompts prontos viraram fórmulas): bloco de 4 linhas, começando por `### i-004 ✅ Módulos de estilo trocáveis por menu (núcleo no v0)`
> - E29 (`meta/IDEAS.md`, i-053 capturada): bloco de 6 linhas, começando por `### i-052 💡 Paleta de módulos do acervo`
> - E30 (`meta/ROADMAP.md`, fórmulas de referência ✅): linha `- ⬜ Fórmulas de referência dos álbuns, copiáveis inteiras (0.20.0, DEC-037). Era «import…`
> - E31 (`meta/STATUS.md`, versão e fase): linha `**Versão atual:** 0.19.0 · **Fase:** 3a, 3a.2, o BPM da 3b, o prompt-modelo e as conveni…`
> - E32 (`meta/STATUS.md`, última conversa): bloco de 8 linhas, começando por `## Última conversa (2026-11-11 a 2026-11-14, rampa conferida, fórmulas decididas, WO 0037)`
> - E33 (`meta/STATUS.md`, funciona: as fórmulas): bloco de 2 linhas, começando por `- **Rampa de BPM** (0.19.0, DEC-036): dois BPM no mesmo trecho do Style, ligados por «to…`
> - E34 (`meta/STATUS.md`, funciona: 61 testes): linha `- **Testes do navegador no CI** (DEC-034): 'tests/' (pytest e Playwright, 44 testes desd…`
> - E35 (`meta/STATUS.md`, pendências: conferir a 0.20.0 e importar as fórmulas): bloco de 4 linhas, começando por `## Pendências do dono`
> - E36 (`meta/STATUS.md`, backlog: sai a 0.20.0 e renumera): bloco de 4 linhas, começando por `1. **Fórmulas de referência (0.20.0, DEC-037)** — spec 'meta/specs/261111-formulas.md' p…`
> **Canal dos meta neste ciclo = CODE:** STATUS, CHANGELOG, DECISIONS, ROADMAP, IDEAS e README pelo Code (DEC-010), com o texto abaixo; a spec e o log ja estao gravados pelo chat.

---

## 1. Por que

Os guias antigos trazem styles completos ja validados, e nada disso chegou ao app; como modulo nao serve (a analise mediu de 5 a 14 tags por formula, contra 1 a 3 de um modulo). A 0.20.0 cria o campo opcional `styleReferences`, a janela «Formulas» (lateral e «⋯», so com formulas), excluir com «Desfazer», a importacao pela janela «Importar faixas» (aceita `albums: []`) e a conferencia no `validate.py` (DEC-037). Fecha a Fase 3b. As 18 formulas do dono ficam fora do repo, em `../acervos/formulas.json`.

## Edicao 0 — Conferencia de hash e de arvore

```
sha1sum app/index.html scripts/validate.py schema/collection.schema.json README.md meta/CHANGELOG.md meta/DECISIONS.md meta/IDEAS.md meta/ROADMAP.md meta/STATUS.md meta/specs/261111-formulas.md logs/2026-11-14.md
GIT_OPTIONAL_LOCKS=0 git status --short
```

Todos batem com **partida**; o `git status` mostra exatamente as tres linhas do Pre-requisito. Qualquer outra coisa: **PARE e reporte**.

## Edicoes E01 a E37

Na ordem. Copie o que esta ENTRE as linhas de quatro crases, sem elas. Aplique por script, extraindo os blocos da WO; grave em UTF-8 com LF.

### E01 — CSS: a janela «Fórmulas» e a seção da importação

**Arquivo:** `app/index.html`

**Ancora:**

````
  .import-list label { font-size: 13px; margin: 0; }
  .prompt-dialog select, .prompt-dialog input[type="text"] { font: inherit; padding: 4px 6px; margin: 0 0 8px; width: 100%; box-sizing: border-box; }
````

**Texto novo (substitui a ancora inteira):**

````
  .import-list label { font-size: 13px; margin: 0; }
  .import-dialog h3, .formulas-dialog h3 { font-size: 13px; font-weight: 600; margin: 10px 0 0; }

  /* ---- 0.20: formulas de referencia (DEC-037) ----
     Uma janela so, aberta pela lateral e pelo «⋯». No celular, em tela cheia. */
  .side-formulas { margin-bottom: 18px; }
  dialog.prompt-dialog.formulas-dialog { width: min(720px, calc(100vw - 32px)); max-height: calc(100vh - 48px); box-sizing: border-box;
    padding: 0; overflow: hidden; }
  dialog.prompt-dialog.formulas-dialog[open] { display: flex; flex-direction: column; }
  .formulas-head { flex: none; display: flex; align-items: center; gap: 8px; padding: 14px 12px 6px 20px; }
  .formulas-head h2 { flex: 1; margin: 0; }
  .formulas-dialog .formulas-intro { margin: 0; padding: 0 20px 8px; }
  .formulas-dialog [data-role="formulas-status"] { display: flex; align-items: center; gap: 10px; margin: 0; padding: 0 20px;
    min-height: 1.4em; }
  .formulas-body { flex: 1; overflow: auto; overscroll-behavior: contain; padding: 4px 20px 20px; }
  .fgroup + .fgroup { margin-top: 14px; }
  .fgroup h3 { margin: 0 0 6px; color: var(--ink-soft); font-weight: 600; }
  .formula { border: 1px solid var(--line); border-radius: 8px; padding: 10px; background: var(--paper-2); }
  .formula + .formula { margin-top: 8px; }
  .formula-head { display: flex; align-items: center; gap: 8px; flex-wrap: wrap; margin-bottom: 4px; }
  .formula-label { flex: 1; min-width: 0; font-weight: 600; }
  .formula .quality { margin: 0 0 6px; }
  .formula .block { max-height: none; }
  .formula-notes { margin-top: 6px; font-size: 13px; }
  .formula-notes summary { cursor: pointer; color: var(--ink-soft); }
  .formula-notes p { margin: 4px 0 0; white-space: pre-wrap; }
  .formula-del { color: var(--ink-soft); }
  .formulas-empty { color: var(--ink-soft); font-size: 13px; }
  @media (max-width: 719px) {
    dialog.prompt-dialog.formulas-dialog { width: 100vw; max-width: 100vw; height: 100dvh; max-height: 100dvh; margin: 0;
      border: 0; border-radius: 0; }
    .formulas-dialog button, .formula-notes summary { min-height: 44px; }
    .formulas-head .dbtn { width: 44px; }
    .formula-notes summary { display: flex; align-items: center; gap: 4px; }
  }
  .prompt-dialog select, .prompt-dialog input[type="text"] { font: inherit; padding: 4px 6px; margin: 0 0 8px; width: 100%; box-sizing: border-box; }
````

### E02 — versão 0.20.0

**Arquivo:** `app/index.html`

**Ancora:**

````
    <span class="version" data-role="app-version">v0.19.0</span>
````

**Texto novo (substitui a ancora inteira):**

````
    <span class="version" data-role="app-version">v0.20.0</span>
````

### E03 — «⋯» da barra: a entrada «Fórmulas (N)»

**Arquivo:** `app/index.html`

**Ancora:**

````
      <div class="pop-head mobile-only" id="more-brand">Cancioneiro</div>
      <button type="button" role="menuitem" id="menu-import">Importar .json…</button>
````

**Texto novo (substitui a ancora inteira):**

````
      <div class="pop-head mobile-only" id="more-brand">Cancioneiro</div>
      <button type="button" role="menuitem" id="menu-formulas" aria-haspopup="dialog" hidden>Fórmulas</button>
      <button type="button" role="menuitem" id="menu-import">Importar .json…</button>
````

### E04 — lateral: a entrada «Fórmulas», acima de «Todas as faixas»

**Arquivo:** `app/index.html`

**Ancora:**

````
<nav class="side" id="side" aria-label="Álbuns e acervos" hidden>
  <div class="side-head">Álbuns</div>
````

**Texto novo (substitui a ancora inteira):**

````
<nav class="side" id="side" aria-label="Álbuns e acervos" hidden>
  <!-- 0.20 (DEC-037): so aparece quando o acervo tem formulas. -->
  <ul class="side-list side-formulas" id="side-formulas" hidden>
    <li><button type="button" class="side-item" id="side-formulas-btn" aria-haspopup="dialog"><span class="t">Fórmulas</span><span class="n" id="side-formulas-n"></span></button></li>
  </ul>
  <div class="side-head">Álbuns</div>
````

### E05 — janela de importar: a classe import-dialog

**Arquivo:** `app/index.html`

**Ancora:**

````
<dialog class="prompt-dialog" id="import-dialog" aria-labelledby="import-dialog-title">
````

**Texto novo (substitui a ancora inteira):**

````
<dialog class="prompt-dialog import-dialog" id="import-dialog" aria-labelledby="import-dialog-title">
````

### E06 — janela de importar: a seção «Fórmulas»

**Arquivo:** `app/index.html`

**Ancora:**

````
  <ul class="import-list" id="import-list"></ul>
  <label for="import-target">Destino</label>
````

**Texto novo (substitui a ancora inteira):**

````
  <ul class="import-list" id="import-list"></ul>
  <!-- 0.20 (DEC-037): so quando a origem traz styleReferences. -->
  <div id="import-formulas" hidden>
    <h3>Fórmulas</h3>
    <ul class="import-list" id="import-formula-list"></ul>
  </div>
  <div id="import-dest">
  <label for="import-target">Destino</label>
````

### E07 — janela de importar: o destino num bloco que some sem faixas

**Arquivo:** `app/index.html`

**Ancora:**

````
  <input type="text" id="import-new-title" placeholder="título do álbum novo" hidden>
  <div class="dialog-actions">
````

**Texto novo (substitui a ancora inteira):**

````
  <input type="text" id="import-new-title" placeholder="título do álbum novo" hidden>
  </div>
  <div class="dialog-actions">
````

### E08 — a janela «Fórmulas»

**Arquivo:** `app/index.html`

**Ancora:**

````
</dialog>
<input type="file" id="tracks-input" accept=".json,application/json" hidden>

<div class="drop-hint" aria-hidden="true">Solte o .json para importar</div>
````

**Texto novo (substitui a ancora inteira):**

````
</dialog>
<input type="file" id="tracks-input" accept=".json,application/json" hidden>

<!-- 0.20 (DEC-037): as formulas de referencia do acervo. O Style de cada uma e
     o copiavel; label, notes e source sao referencia e ficam fora do bloco. -->
<dialog class="prompt-dialog formulas-dialog" id="formulas-dialog" aria-labelledby="formulas-dialog-title">
  <div class="formulas-head">
    <h2 id="formulas-dialog-title">Fórmulas</h2>
    <button type="button" class="dbtn" id="formulas-close-btn" aria-label="Fechar">×</button>
  </div>
  <p class="formulas-intro">Styles completos, já validados, para começar uma faixa nova. «Copiar Style» entrega só o texto do bloco.</p>
  <p class="note" data-role="formulas-status" id="formulas-status" role="status"></p>
  <div class="formulas-body" id="formulas-body"></div>
</dialog>

<div class="drop-hint" aria-hidden="true">Solte o .json para importar</div>
````

### E09 — copiar: o plano B dentro da janela aberta

**Arquivo:** `app/index.html`

**Ancora:**

````
    ta.value = text; document.body.appendChild(ta); ta.select();
    try { document.execCommand("copy"); } catch (_) {}
    document.body.removeChild(ta);
````

**Texto novo (substitui a ancora inteira):**

````
    // 0.20: com uma janela aberta, o resto da pagina e inerte; o campo vai para dentro dela
    const host = document.querySelector("dialog[open]") || document.body;
    ta.value = text; host.appendChild(ta); ta.select();
    try { document.execCommand("copy"); } catch (_) {}
    host.removeChild(ta);
````

### E10 — importar: título e destino conforme a origem

**Arquivo:** `app/index.html`

**Ancora:**

````
  document.getElementById("import-source").textContent = name;
  const list = document.getElementById("import-list");
````

**Texto novo (substitui a ancora inteira):**

````
  document.getElementById("import-source").textContent = name;
  const hasSongs = src.albums.some(a => (a.songs || []).length);
  const refs = importableRefs(src);
  fillImportFormulas(refs.list);
  // 0.20: so formulas, sem faixas: o destino (album) nao vale para nada
  document.getElementById("import-dest").hidden = !hasSongs && refs.list.length > 0;
  document.getElementById("import-dialog-title").textContent = !refs.list.length ? "Importar faixas"
    : hasSongs ? "Importar faixas e fórmulas" : "Importar fórmulas";
  const list = document.getElementById("import-list");
````

### E11 — importar: as fórmulas marcadas seguem para o importTracks

**Arquivo:** `app/index.html`

**Ancora:**

````
    dlg.close();
    await importTracks(src, keys, sel.value, inp.value.trim());
````

**Texto novo (substitui a ancora inteira):**

````
    const refKeys = new Set([...document.querySelectorAll('#import-formula-list input[type="checkbox"]')]
      .filter(c => c.checked).map(c => Number(c.dataset.ref)));
    dlg.close();
    await importTracks(src, keys, sel.value, inp.value.trim(), { refs: refs.list, keys: refKeys, invalid: refs.invalid });
````

### E12 — importTracks: recebe as fórmulas

**Arquivo:** `app/index.html`

**Ancora:**

````
async function importTracks(src, keys, dest, newTitle) {
````

**Texto novo (substitui a ancora inteira):**

````
async function importTracks(src, keys, dest, newTitle, refPick) {
````

### E13 — importTracks: importa as fórmulas

**Arquivo:** `app/index.html`

**Ancora:**

````
  }));

  const parts = [];
  if (n.same) parts.push(n.same + (n.same === 1 ? " já estava" : " já estavam"));
````

**Texto novo (substitui a ancora inteira):**

````
  }));

  // 0.20 (DEC-037): as formulas marcadas, pela mesma regra das faixas
  const f = importFormulas(refPick);

  const parts = [];
  if (n.same) parts.push(n.same + (n.same === 1 ? " já estava" : " já estavam"));
````

### E14 — importTracks: o aviso soma faixas e fórmulas; o bloco das fórmulas

**Arquivo:** `app/index.html`

**Ancora:**

````
  const tail = parts.length ? " · " + parts.join(" · ") : "";
  if (!n.imported) { App.undo = prevUndo; toast("Nada importado" + tail); return; }
  await afterEdit(nPlural(n.imported, "faixa importada", "faixas importadas") + tail);
}
````

**Texto novo (substitui a ancora inteira):**

````
  if (f.same) parts.push(nPlural(f.same, "fórmula já estava", "fórmulas já estavam"));
  if (f.renamed) parts.push(nPlural(f.renamed, "fórmula renomeada", "fórmulas renomeadas") + " (id repetido)");
  if (f.invalid) parts.push(nPlural(f.invalid, "fórmula sem id ou style ignorada", "fórmulas sem id ou style ignoradas"));
  const tail = parts.length ? " · " + parts.join(" · ") : "";
  if (!n.imported && !f.imported) { App.undo = prevUndo; toast("Nada importado" + tail); return; }
  // O aviso soma faixas e formulas; so faixas, o texto de antes
  const head = !f.imported ? nPlural(n.imported, "faixa importada", "faixas importadas")
    : (n.imported ? nPlural(n.imported, "faixa", "faixas") + " e " : "")
      + nPlural(f.imported, "fórmula", "fórmulas") + (n.imported + f.imported === 1 ? " importada" : " importadas");
  await afterEdit(head + tail);
}

/* ===================================================================
   Formulas de referencia (0.20.0, DEC-037 — spec meta/specs/261111-formulas.md)
   Styles completos dos guias antigos, para copiar inteiros. Moram em
   collection.styleReferences; nenhuma faixa as cita. Ler, copiar, importar e
   excluir; editar e no arquivo. O copiavel e so o `style` (regra de dominio:
   label, notes e source sao referencia e ficam fora do bloco).
   =================================================================== */

/** As formulas do acervo aberto (lista vazia sem acervo ou sem o campo). */
function formulaList() {
  const r = App.collection && App.collection.styleReferences;
  return Array.isArray(r) ? r : [];
}

/** As formulas importaveis de uma origem: objeto com id e style em texto. As
    outras sao contadas, nunca caladas (FIX-006). */
function importableRefs(src) {
  const all = Array.isArray(src.styleReferences) ? src.styleReferences : [];
  const list = all.filter(r => r && typeof r === "object" && typeof r.id === "string" && r.id
    && typeof r.style === "string");
  return { list, invalid: all.length - list.length };
}

/** A secao «Formulas» da janela de importar: uma caixa por formula, marcadas. */
function fillImportFormulas(list) {
  const box = document.getElementById("import-formulas"), ul = document.getElementById("import-formula-list");
  ul.textContent = "";
  box.hidden = !list.length;
  list.forEach((r, i) => {
    const li = document.createElement("li");
    const lab = document.createElement("label");
    const cb = document.createElement("input");
    cb.type = "checkbox"; cb.checked = true; cb.dataset.ref = String(i);
    lab.appendChild(cb);
    lab.appendChild(document.createTextNode(" " + (r.label || r.id) + " "));
    const m = document.createElement("span"); m.className = "acervo-meta"; m.textContent = r.source ? r.id + " · " + r.source : r.id;
    lab.appendChild(m);
    li.appendChild(lab); ul.appendChild(li);
  });
}

/** Traz as formulas marcadas para o fim da lista. Id igual e conteudo
    identico (objeto inteiro serializado) pula; id igual e conteudo diferente
    entra com sufixo (-2). Chamado de dentro do importTracks, depois do
    beginEdit: a mesma volta do «Desfazer» cobre faixas e formulas. */
function importFormulas(pick) {
  const n = { imported: 0, same: 0, renamed: 0, invalid: pick ? pick.invalid : 0 };
  if (!pick || !pick.refs.length) return n;
  const coll = App.collection;
  const mine = Array.isArray(coll.styleReferences) ? coll.styleReferences : [];
  const ids = new Set(mine.map(r => r && r.id));
  pick.refs.forEach((orig, i) => {
    if (!pick.keys.has(i)) return;
    const r = JSON.parse(JSON.stringify(orig));
    const ex = mine.find(x => x && x.id === r.id);
    if (ex && JSON.stringify(ex) === JSON.stringify(r)) { n.same++; return; }
    if (ids.has(r.id)) { r.id = nextFreeId(r.id, ids); n.renamed++; }
    mine.push(r); ids.add(r.id); n.imported++;
  });
  if (n.imported && !Array.isArray(coll.styleReferences)) coll.styleReferences = mine;
  return n;
}

/** A linha de status da janela (o toast ficaria atras dela). Com `undo`, o
    botao «Desfazer». */
function formulaStatus(msg, undo) {
  const st = document.getElementById("formulas-status");
  st.textContent = msg || "";
  if (undo && App.undo) {
    const b = document.createElement("button");
    b.type = "button"; b.className = "toast-btn formula-undo"; b.textContent = "Desfazer";
    b.addEventListener("click", () => undoLast());
    st.appendChild(b);
  }
}

/** Desenha a janela: agrupada por `source`, na ordem do arquivo (o grupo
    aparece onde aparece a primeira formula dele). */
function renderFormulasDialog() {
  const body = document.getElementById("formulas-body");
  body.textContent = "";
  const list = formulaList();
  document.getElementById("formulas-dialog-title").textContent = "Fórmulas (" + list.length + ")";
  if (!list.length) {
    const p = document.createElement("p"); p.className = "formulas-empty";
    p.textContent = "Nenhuma fórmula neste acervo.";
    body.appendChild(p);
    return;
  }
  const groups = new Map();
  list.forEach(r => {
    const key = (r && r.source) || "Sem origem";
    if (!groups.has(key)) groups.set(key, []);
    groups.get(key).push(r);
  });
  groups.forEach((items, key) => {
    const sec = document.createElement("section"); sec.className = "fgroup";
    const h = document.createElement("h3"); h.textContent = key; sec.appendChild(h);
    items.forEach(r => sec.appendChild(renderFormula(r)));
    body.appendChild(sec);
  });
}

/** Uma formula: o nome, a linha de qualidade do cartao, o Style num bloco e as
    notas recolhidas em «Por que funciona». */
function renderFormula(r) {
  const art = document.createElement("article");
  art.className = "formula"; art.dataset.id = r.id;
  const head = document.createElement("div"); head.className = "formula-head";
  const lab = document.createElement("span"); lab.className = "formula-label"; lab.textContent = r.label || r.id;
  head.appendChild(lab);
  const copy = document.createElement("button");
  copy.type = "button"; copy.className = "btn-primary formula-copy"; copy.textContent = "Copiar Style";
  // Le o bloco na hora do clique, como no cartao (FIX-007): o que se ve e o que se cola
  copy.addEventListener("click", () => copyText(pre.textContent, copy));
  head.appendChild(copy);
  if (App.saved) {   // excluir mexe no rascunho: so com copia guardada, como as faixas
    const del = document.createElement("button");
    del.type = "button"; del.className = "formula-del"; del.textContent = "Excluir";
    del.setAttribute("aria-label", "Excluir a fórmula " + (r.label || r.id));
    del.addEventListener("click", () => deleteFormula(r.id));
    head.appendChild(del);
  }
  art.appendChild(head);
  art.appendChild(styleQuality(r.style || "", ""));
  const pre = document.createElement("pre");
  pre.className = "block formula-style"; pre.textContent = r.style || "";
  art.appendChild(pre);
  if (r.notes) {
    const det = document.createElement("details"); det.className = "formula-notes";
    const sum = document.createElement("summary"); sum.textContent = "Por que funciona";
    const p = document.createElement("p"); p.textContent = r.notes;
    det.appendChild(sum); det.appendChild(p);
    art.appendChild(det);
  }
  return art;
}

function openFormulasDialog() {
  closePopovers(false);
  formulaStatus("");
  renderFormulasDialog();
  const dlg = document.getElementById("formulas-dialog");
  if (!dlg.open) dlg.showModal();
  document.getElementById("formulas-body").scrollTop = 0;
}

/** Excluir: conta como mudanca a salvar, com o «Desfazer» da I3 (a formula
    volta na mesma posicao, porque a volta e o acervo inteiro). Sem formula
    nenhuma, o campo sai do acervo. */
async function deleteFormula(id) {
  const list = formulaList(), i = list.findIndex(r => r && r.id === id);
  if (i < 0) return;
  const r = list[i];
  if (!(await confirmAsk("Excluir a fórmula «" + (r.label || r.id) + "» deste acervo? Ela continua no arquivo até você salvar.", "excluir"))) return;
  beginEdit();
  list.splice(i, 1);
  if (!list.length) delete App.collection.styleReferences;
  const msg = "Fórmula «" + (r.label || r.id) + "» excluída do rascunho";
  rerender();
  const ok = await persistDraft(true);
  if (App.undo && !App.undo.label) App.undo.label = msg;
  renderFormulasDialog();
  formulaStatus(msg + (ok ? "" : " · não consegui guardar no navegador: baixe o .json para não perder"), true);
}

document.getElementById("side-formulas-btn").addEventListener("click", openFormulasDialog);
document.getElementById("menu-formulas").addEventListener("click", openFormulasDialog);
document.getElementById("formulas-close-btn").addEventListener("click", () =>
  document.getElementById("formulas-dialog").close());
````

### E15 — updateBar: «Fórmulas (N)» só com fórmulas

**Arquivo:** `app/index.html`

**Ancora:**

````
  document.getElementById("menu-import-tracks").hidden = !App.saved;
}
````

**Texto novo (substitui a ancora inteira):**

````
  document.getElementById("menu-import-tracks").hidden = !App.saved;
  // 0.20 (DEC-037): «Formulas (N)», em qualquer largura, so com formulas.
  const nRefs = has ? formulaList().length : 0;
  const mf = document.getElementById("menu-formulas");
  mf.hidden = !nRefs;
  mf.textContent = "Fórmulas (" + nRefs + ")";
}
````

### E16 — renderSide: «Fórmulas · N» só com fórmulas

**Arquivo:** `app/index.html`

**Ancora:**

````
  if (!App.collection) return;
  const ul = document.getElementById("side-albums");
````

**Texto novo (substitui a ancora inteira):**

````
  if (!App.collection) return;
  // 0.20 (DEC-037): «Formulas · N», acima de «Todas as faixas», so com formulas.
  const nRefs = formulaList().length;
  document.getElementById("side-formulas").hidden = !nRefs;
  document.getElementById("side-formulas-n").textContent = nRefs ? String(nRefs) : "";
  document.getElementById("side-formulas-btn").setAttribute("aria-label", "Fórmulas · " + nRefs + " (abre a janela)");
  const ul = document.getElementById("side-albums");
````

### E17 — undoLast: a janela das fórmulas acompanha

**Arquivo:** `app/index.html`

**Ancora:**

````
  toast("Desfeito: " + u.label + (ok ? "" : " · não consegui guardar no navegador: baixe o .json para não perder"));
````

**Texto novo (substitui a ancora inteira):**

````
  const msg = "Desfeito: " + u.label + (ok ? "" : " · não consegui guardar no navegador: baixe o .json para não perder");
  // 0.20: com a janela das formulas aberta, o toast ficaria atras dela
  if (document.getElementById("formulas-dialog").open) { renderFormulasDialog(); formulaStatus(msg); }
  else toast(msg);
````

### E18 — docstring: nove coisas

**Arquivo:** `scripts/validate.py`

**Ancora:**

````
Checa oito coisas:
````

**Texto novo (substitui a ancora inteira):**

````
Checa nove coisas:
````

### E19 — docstring: o item 9

**Arquivo:** `scripts/validate.py`

**Ancora:**

````
  8. A SortableJS embutida no app e a 1.15.7 sem mudanca: o sha256 do trecho
     confere com o do Sortable.min.js do npm (DEC-030, DEC-032).

Rode antes de commitar mudanca em data/ ou schema/ (ver CLAUDE.md).
````

**Texto novo (substitui a ancora inteira):**

````
  8. A SortableJS embutida no app e a 1.15.7 sem mudanca: o sha256 do trecho
     confere com o do Sortable.min.js do npm (DEC-030, DEC-032).
  9. As formulas de referencia (styleReferences, DEC-037): ids unicos, label e
     style nao vazios, style sem colchete (colchete e do campo Lyrics). O erro
     diz o caminho (styleReferences[3].style).

Rode antes de commitar mudanca em data/ ou schema/ (ver CLAUDE.md).
````

### E20 — check_formulas

**Arquivo:** `scripts/validate.py`

**Ancora:**

````
        print(f"ERRO de BPM em {rel} ({len(bad)} faixa(s)):")
        for b in bad[:8]:
````

**Texto novo (substitui a ancora inteira):**

````
        print(f"ERRO de BPM em {rel} ({len(bad)} faixa(s)):")
        for b in bad[:8]:
            print(f"   {b}")
        return 1
    return 0


def check_formulas(data, rel):
    """As formulas de referencia (DEC-037) sao copiaveis inteiras: o style vai
    direto para o campo Style of Music. Id repetido, label ou style vazio e
    colchete no style (instrucao de Lyrics dentro do copiavel) sao erro, com o
    caminho do item. O esquema confere os tipos; isto confere o resto, e roda
    tambem sem o pacote jsonschema.
    """
    refs = data.get("styleReferences")
    if refs is None:
        return 0
    bad, seen = [], {}
    if not isinstance(refs, list):
        bad.append("styleReferences: nao e uma lista")
        refs = []
    for i, ref in enumerate(refs):
        where = f"styleReferences[{i}]"
        if not isinstance(ref, dict):
            bad.append(f"{where}: nao e um objeto")
            continue
        rid = ref.get("id")
        if not isinstance(rid, str) or not rid.strip():
            bad.append(f"{where}.id: vazio")
        elif rid in seen:
            bad.append(f"{where}.id: '{rid}' repetido (o mesmo de styleReferences[{seen[rid]}])")
        else:
            seen[rid] = i
        for key in ("label", "style"):
            val = ref.get(key)
            if not isinstance(val, str) or not val.strip():
                bad.append(f"{where}.{key}: vazio")
        style = ref.get("style")
        if isinstance(style, str) and ("[" in style or "]" in style):
            bad.append(f"{where}.style: tem colchete — colchete e do campo Lyrics; leve a instrucao para notes")
    if bad:
        print(f"ERRO de formula em {rel} ({len(bad)} problema(s)):")
        for b in bad[:8]:
````

### E21 — check_formulas no modo só sintaxe

**Arquivo:** `scripts/validate.py`

**Ancora:**

````
            errors += check_bpm(data, rel)
            continue
````

**Texto novo (substitui a ancora inteira):**

````
            errors += check_bpm(data, rel)
            errors += check_formulas(data, rel)
            continue
````

### E22 — a contagem de fórmulas na linha OK

**Arquivo:** `scripts/validate.py`

**Ancora:**

````
            print(f"OK  {rel}  ({len(data.get('albums', []))} álbuns, {n_songs} faixas)")
````

**Texto novo (substitui a ancora inteira):**

````
            n_refs = len(data.get("styleReferences") or [])
            print(f"OK  {rel}  ({len(data.get('albums', []))} álbuns, {n_songs} faixas"
                  + (f", {n_refs} fórmulas" if n_refs else "") + ")")
````

### E23 — check_formulas no modo com esquema

**Arquivo:** `scripts/validate.py`

**Ancora:**

````
        errors += check_module_refs(data, rel)
        errors += check_bpm(data, rel)

    # versao: a mesma nos quatro lugares (i-027)
````

**Texto novo (substitui a ancora inteira):**

````
        errors += check_module_refs(data, rel)
        errors += check_bpm(data, rel)
        errors += check_formulas(data, rel)

    # versao: a mesma nos quatro lugares (i-027)
````

### E24 — styleReferences no esquema

**Arquivo:** `schema/collection.schema.json`

**Ancora:**

````
    },
    "albums": {
````

**Texto novo (substitui a ancora inteira):**

````
    },
    "styleReferences": {
      "type": "array",
      "description": "Formulas de referencia (DEC-037): styles completos ja validados, para copiar inteiros como ponto de partida. Nenhuma faixa cita formula. Opcional.",
      "items": {
        "type": "object",
        "required": ["id", "label", "style"],
        "additionalProperties": false,
        "properties": {
          "id": {
            "type": "string",
            "pattern": "^[a-z0-9][a-z0-9-]*$",
            "description": "Id unico da formula no acervo."
          },
          "label": { "type": "string", "minLength": 1, "description": "Nome curto (referencia humana, nunca vai para o Suno)." },
          "style": {
            "type": "string",
            "minLength": 1,
            "description": "O copiavel: so o que vai para o campo Style of Music, sem colchetes e sem rotulo."
          },
          "notes": { "type": ["string", "null"], "description": "Por que funciona, dica de uso. Nao vai para o Suno." },
          "source": { "type": ["string", "null"], "description": "De onde veio (ex.: 'BR · indice-mestre'). Agrupa na janela." }
        }
      }
    },
    "albums": {
````

### E25 — estado v0.20.0

**Arquivo:** `README.md`

**Ancora:**

````
> **Estado:** v0.19.0 — ferramenta em uso. Lê, guarda e edita vários acervos, grava direto no arquivo do acervo (Chrome e Edge), copia por campo, troca módulos de estilo, ajusta o BPM, **mede cada prompt contra os limites do Suno**, exporta Markdown, exporta uma faixa como `.json` e **entrega o prompt para chats gerarem canções no esquema**. Publicada no GitHub Pages. Ver `meta/ROADMAP.md`.
````

**Texto novo (substitui a ancora inteira):**

````
> **Estado:** v0.20.0 — ferramenta em uso. Lê, guarda e edita vários acervos, grava direto no arquivo do acervo (Chrome e Edge), copia por campo, troca módulos de estilo, ajusta o BPM, **mede cada prompt contra os limites do Suno**, guarda as **fórmulas de referência** dos guias para copiar inteiras, exporta Markdown, exporta uma faixa como `.json` e **entrega o prompt para chats gerarem canções no esquema**. Publicada no GitHub Pages. Ver `meta/ROADMAP.md`.
````

### E26 — entrada [0.20.0]

**Arquivo:** `meta/CHANGELOG.md`

**Ancora:**

````
# CHANGELOG.md — Cancioneiro

> Histórico de versões entregues. SemVer + Keep a Changelog. Cresce no topo.

---

## [0.19.0] — 2026-11-11
````

**Texto novo (substitui a ancora inteira):**

````
# CHANGELOG.md — Cancioneiro

> Histórico de versões entregues. SemVer + Keep a Changelog. Cresce no topo.

---

## [0.20.0] — 2026-11-14

Fórmulas de referência (DEC-037): os styles validados dos guias antigos, para copiar inteiros. Fecha a Fase 3b.

### Added
- **Campo `styleReferences` na coleção** (opcional): `id`, `label`, `style` (só o copiável), `notes` e `source`; nenhum outro campo. Nenhuma faixa cita fórmula.
- **Janela «Fórmulas»**, aberta pela lateral («Fórmulas», acima de «Todas as faixas», a partir de 1280 px) e pelo «⋯» («Fórmulas (N)»), só quando o acervo tem fórmulas. Agrupa por `source`, na ordem do arquivo; cada fórmula mostra a linha de qualidade do cartão, o Style num bloco, «Copiar Style» (só o `style`, byte a byte) e as notas recolhidas em «Por que funciona». No celular, em tela cheia.
- **Excluir fórmula**, com confirmação e «Desfazer» na própria janela; conta como alteração a salvar. Sem fórmula nenhuma, o campo sai do acervo. Editar continua sendo no arquivo.
- **Importar fórmulas** pela janela «Importar faixas», que aceita `albums: []` com fórmulas: a seção «Fórmulas», com uma caixa por fórmula; idêntica pula, mesmo id e conteúdo diferente entra com `-2`. O aviso soma faixas e fórmulas; o destino vale só para as faixas.
- `validate.py`: ids únicos, `label` e `style` não vazios e `style` sem colchete, com o caminho no erro (`styleReferences[3].style`).

### Changed
- O plano B do copiar (sem a API da área de transferência) põe o campo de texto dentro da janela aberta, onde o resto da página é inerte.

Spec `meta/specs/261111-formulas.md`: 9 de 9 critérios, com 11 testes novos em `tests/test_formulas.py` (61 no total). Salvar e baixar o `.json` levam as fórmulas; exportar faixa ou álbum, não. As 18 fórmulas do dono ficam fora do repo, em `../acervos/formulas.json`.

---

## [0.19.0] — 2026-11-11
````

### E27 — DEC-037 implementada

**Arquivo:** `meta/DECISIONS.md`

**Ancora:**

````
**Status:** aceita — implementação pendente (0.20.0)
````

**Texto novo (substitui a ancora inteira):**

````
**Status:** aceita — implementada na 0.20.0 (2026-11-14)
````

### E28 — i-004: os prompts prontos viraram fórmulas

**Arquivo:** `meta/IDEAS.md`

**Ancora:**

````
### i-004 ✅ Módulos de estilo trocáveis por menu (núcleo no v0)
Fragmentos de estilo nomeados (`melancholic`, `taiko-drums`, `female-soprano`, faixas de BPM) que se ligam/desligam por menu de contexto, recompondo o campo `style` final e gerando variações sem reescrever. Importar os "estilos construídos por chat" (prompts prontos dos álbuns) como módulos. Ver `schema/style-modules.json`. Fase 3.

### i-005 ✅ Controle de BPM por slider/roll
````

**Texto novo (substitui a ancora inteira):**

````
### i-004 ✅ Módulos de estilo trocáveis por menu (núcleo no v0)
Fragmentos de estilo nomeados (`melancholic`, `taiko-drums`, `female-soprano`, faixas de BPM) que se ligam/desligam por menu de contexto, recompondo o campo `style` final e gerando variações sem reescrever. Importar os "estilos construídos por chat" (prompts prontos dos álbuns) como módulos. Ver `schema/style-modules.json`. Fase 3.
**Revisto (2026-11-14, DEC-037):** os prompts prontos não viraram módulos, e sim fórmulas de referência copiáveis inteiras (`styleReferences`, 0.20.0); decompô-los em módulos ficou na i-052.

### i-005 ✅ Controle de BPM por slider/roll
````

### E29 — i-053 capturada

**Arquivo:** `meta/IDEAS.md`

**Ancora:**

````
### i-052 💡 Paleta de módulos do acervo
`[capturada pelo chat, 2026-11-11, na análise dos prompts prontos]` Os dois acervos reais têm 0 módulos: o painel de módulos fica vazio com dado real. Uma paleta por acervo poderia vir de duas fontes: (1) as tags que se repetem nas faixas (medido em 2026-11-11: 25 tags aparecem em 10 faixas ou mais na BR, 34 nos reagrupados) e (2) as fórmulas decompostas, uma tag por módulo, mais as 3 listas de voz do `album_guia_suno` que ficaram fora das fórmulas (DEC-037). Limite medido: os styles das faixas já têm de 10 a 17 tags (mediana 12), e módulo só soma — ligar um piora o orçamento. Classificar cada tag numa das sete camadas pede julgamento. Pede análise antes da spec.

## Feedback para o Kit

- **[2026-07-19] Nicho pediria uma variante "ferramenta+conteúdo".** Este projeto é dev, mas o "produto" é metade código (app) e metade dado curado (acervo JSON). O template de Desenvolvimento cobre bem a parte código; a parte "acervo de dados como entregável" ficou por conta do CONTEXT. Não faltou nada crítico, mas um nicho híbrido "ferramenta que consome conteúdo estruturado" seria útil.
````

**Texto novo (substitui a ancora inteira):**

````
### i-052 💡 Paleta de módulos do acervo
`[capturada pelo chat, 2026-11-11, na análise dos prompts prontos]` Os dois acervos reais têm 0 módulos: o painel de módulos fica vazio com dado real. Uma paleta por acervo poderia vir de duas fontes: (1) as tags que se repetem nas faixas (medido em 2026-11-11: 25 tags aparecem em 10 faixas ou mais na BR, 34 nos reagrupados) e (2) as fórmulas decompostas, uma tag por módulo, mais as 3 listas de voz do `album_guia_suno` que ficaram fora das fórmulas (DEC-037). Limite medido: os styles das faixas já têm de 10 a 17 tags (mediana 12), e módulo só soma — ligar um piora o orçamento. Classificar cada tag numa das sete camadas pede julgamento. Pede análise antes da spec.

### i-053 💡 Marcar e desmarcar por origem na importação de fórmulas
`[capturada pelo chat, 2026-11-14, na 0.20.0]` O `../acervos/formulas.json` tem as 18 fórmulas; cada acervo recebe só as dele (10 na BR, 8 nos reagrupados), e a janela de importar traz todas marcadas: o dono desmarca 8 ou 10 caixas à mão. Uma caixa por `source` (marca ou desmarca o grupo) resolveria; o mesmo valeria para os álbuns da importação de faixas. Esperar o uso dizer se a importação de fórmulas se repete antes de fazer.

## Feedback para o Kit

- **[2026-07-19] Nicho pediria uma variante "ferramenta+conteúdo".** Este projeto é dev, mas o "produto" é metade código (app) e metade dado curado (acervo JSON). O template de Desenvolvimento cobre bem a parte código; a parte "acervo de dados como entregável" ficou por conta do CONTEXT. Não faltou nada crítico, mas um nicho híbrido "ferramenta que consome conteúdo estruturado" seria útil.
````

### E30 — fórmulas de referência ✅

**Arquivo:** `meta/ROADMAP.md`

**Ancora:**

````
- ⬜ Fórmulas de referência dos álbuns, copiáveis inteiras (0.20.0, DEC-037). Era «importar prompts prontos como módulos»: a análise `meta/analises/261111-ANALISE-prompts-prontos.md` mediu que como módulo não serve.
````

**Texto novo (substitui a ancora inteira):**

````
- ✅ Fórmulas de referência dos álbuns, copiáveis inteiras (DEC-037) — 0.20.0. Era «importar prompts prontos como módulos»: a análise `meta/analises/261111-ANALISE-prompts-prontos.md` mediu que como módulo não serve.
````

### E31 — versão e fase

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
**Versão atual:** 0.19.0 · **Fase:** 3a, 3a.2, o BPM da 3b, o prompt-modelo e as conveniências de uso concluídos e conferidos · os álbuns antigos convertidos (i-008, fora do repo) · curadoria no app concluída nas três entregas (DEC-028, DEC-029) · frente de interface concluída e conferida nas quatro entregas (DEC-030 a DEC-033) · organizar os álbuns (0.18.0, DEC-035) conferido · rampa de BPM (0.19.0, DEC-036) conferida · fórmulas de referência (0.20.0, DEC-037) com spec pronta, a implementar · kit de música lido pelo KCM, à espera da resposta (i-039)
````

**Texto novo (substitui a ancora inteira):**

````
**Versão atual:** 0.20.0 · **Fase:** 3a, 3a.2, o BPM da 3b, o prompt-modelo e as conveniências de uso concluídos e conferidos · os álbuns antigos convertidos (i-008, fora do repo) · curadoria no app concluída nas três entregas (DEC-028, DEC-029) · frente de interface concluída e conferida nas quatro entregas (DEC-030 a DEC-033) · organizar os álbuns (0.18.0, DEC-035) conferido · rampa de BPM (0.19.0, DEC-036) conferida · fórmulas de referência (0.20.0, DEC-037) entregues, a conferir na tela · a Fase 3b concluída · kit de música lido pelo KCM, à espera da resposta (i-039)
````

### E32 — última conversa

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
## Última conversa (2026-11-11 a 2026-11-14, rampa conferida, fórmulas decididas, WO 0037)

- **0.19.0 conferida na tela pelo dono** («rampa ok» `[relatado pelo dono, 2026-11-11 16:20]`): a rampa de BPM está fechada. CI verde no `790aa3a` (run `43082294050`, `[medido pelo Code, relatório 261111-1555]`).
- **Prompts prontos — análise** `meta/analises/261111-ANALISE-prompts-prontos.md`: os dois acervos reais têm 0 módulos e styles de 10 a 17 tags; uma fórmula tem de 5 a 14 tags, contra 1 a 3 de um módulo. O dono escolheu a opção D, fórmula de referência copiável inteira `[relatado pelo dono, 2026-11-11 17:12]` (DEC-037).
- **Spec da 0.20.0** `meta/specs/261111-formulas.md`, com protótipo na fileira «0.20» do canvas; os quatro pontos como recomendados `[relatado pelo dono, 2026-11-14 09:21]`. **A implementação não começou:** nenhum código e nenhum `../acervos/formulas.json` escrito.
- **Conversa do chat encerrada** em 2026-11-14 a pedido do dono (pesada); a próxima arranca pelo `../261114-HANDOFF-BRIEF.md`.
- **WO 0037 aplicada pelo Code** em 2026-11-14 (`255ba51`, CI verde, run `43595539716`, `[medido pelo Code]`): só registro, sem código; o app segue na 0.19.0.
- **Este bloco substitui o anterior, da WO 0036** (rampa de BPM). O que ele dizia está no CHANGELOG [0.19.0], na spec `meta/specs/261111-rampa-de-bpm.md` e em `logs/2026-11-11.md`.
````

**Texto novo (substitui a ancora inteira):**

````
## Última conversa (2026-11-14, fórmulas de referência, WO 0038)

- **0.20.0 implementada pelo chat num clone** pela spec `meta/specs/261111-formulas.md`: o campo `styleReferences`, a janela «Fórmulas», excluir com «Desfazer», a seção «Fórmulas» na importação e o `validate.py`. 61 testes, duas vezes, no clone `[medido pelo chat]`; os 11 novos reprovam no app da 0.19.0.
- **`../acervos/formulas.json` escrito pelo chat** (18 fórmulas, `albums: []`), conferido contra os guias por `../acervos/conferir-formulas.py`: 18 de 18, com a Grand Anthem como única exceção. As linhas dos blocos que já terminam em vírgula não ganham outra.
- **Falta conferir na tela** e importar as fórmulas nos dois acervos (pendência do dono abaixo).
- **Este bloco substitui o anterior** (rampa conferida, fórmulas decididas, WO 0037). O que ele dizia está no CHANGELOG [0.19.0], na DEC-037 e em `logs/2026-11-14.md`.
````

### E33 — funciona: as fórmulas

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
- **Rampa de BPM** (0.19.0, DEC-036): dois BPM no mesmo trecho do Style, ligados por «to» e afins, saem como foram escritos; o controle vira o rótulo «rampa 95 → 115 bpm», os chips de andamento ficam desligados e a linha de qualidade avisa em âmbar. O `validate.py` dá AVISO; dois números soltos continuam ERRO.
- **Esquema JSON canônico** (`schema/`). Biblioteca de referência para autoria em `schema/style-modules.json` (27 módulos, sete camadas); cada acervo traz os seus (DEC-016).
````

**Texto novo (substitui a ancora inteira):**

````
- **Rampa de BPM** (0.19.0, DEC-036): dois BPM no mesmo trecho do Style, ligados por «to» e afins, saem como foram escritos; o controle vira o rótulo «rampa 95 → 115 bpm», os chips de andamento ficam desligados e a linha de qualidade avisa em âmbar. O `validate.py` dá AVISO; dois números soltos continuam ERRO.
- **Fórmulas de referência** (0.20.0, DEC-037): `styleReferences` na coleção; a janela «Fórmulas», pela lateral e pelo «⋯», com a linha de qualidade, «Copiar Style» byte a byte, as notas recolhidas e «Excluir» com «Desfazer»; entram pela janela «Importar faixas» (`albums: []` aceito). Salvar leva; exportar faixa ou álbum, não.
- **Esquema JSON canônico** (`schema/`). Biblioteca de referência para autoria em `schema/style-modules.json` (27 módulos, sete camadas); cada acervo traz os seus (DEC-016).
````

### E34 — funciona: 61 testes

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
- **Testes do navegador no CI** (DEC-034): `tests/` (pytest e Playwright, 44 testes desde a 0.18.0, dados só sintéticos) e `.github/workflows/testes.yml`, que roda o `validate.py` com esquema, os testes dos conversores e o `pytest tests` a cada push na `main`. O resultado é o ✓ ou ✗ no commit e a aba Actions.
````

**Texto novo (substitui a ancora inteira):**

````
- **Testes do navegador no CI** (DEC-034): `tests/` (pytest e Playwright, 61 testes desde a 0.20.0, dados só sintéticos) e `.github/workflows/testes.yml`, que roda o `validate.py` com esquema, os testes dos conversores e o `pytest tests` a cada push na `main`. O resultado é o ✓ ou ✗ no commit e a aba Actions.
````

### E35 — pendências: conferir a 0.20.0 e importar as fórmulas

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
## Pendências do dono

- **Apagar à mão o `..\sonda-i4-teste.json`** — arquivo de teste da sonda, na pasta-pai (o chat não apaga arquivo seu).
- **Instalar o validador de esquema nesta máquina.** Sem `jsonschema` e `referencing`, o `validate.py` só confere sintaxe e diz `ESQUEMA NAO CONFERIDO` na última linha. Uma vez, no CMD: `pip install jsonschema referencing --break-system-packages`. Depois, `python3 scripts/validate.py` deve terminar em `Tudo conforme ao esquema.` Desde a DEC-034 o CI confere o esquema a cada push: instalar aqui passa a ser opcional.
````

**Texto novo (substitui a ancora inteira):**

````
## Pendências do dono

- **Conferir a 0.20.0 na tela e importar as fórmulas** — roteiro na conversa de 2026-11-14 (WO 0038): no acervo BR, só as 10 da BR; no reagrupados, só as 8 dos `Albuns/`; salvar os dois.
- **Apagar à mão o `..\sonda-i4-teste.json`** — arquivo de teste da sonda, na pasta-pai (o chat não apaga arquivo seu).
- **Instalar o validador de esquema nesta máquina.** Sem `jsonschema` e `referencing`, o `validate.py` só confere sintaxe e diz `ESQUEMA NAO CONFERIDO` na última linha. Uma vez, no CMD: `pip install jsonschema referencing --break-system-packages`. Depois, `python3 scripts/validate.py` deve terminar em `Tudo conforme ao esquema.` Desde a DEC-034 o CI confere o esquema a cada push: instalar aqui passa a ser opcional.
````

### E36 — backlog: sai a 0.20.0 e renumera

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
1. **Fórmulas de referência (0.20.0, DEC-037)** — spec `meta/specs/261111-formulas.md` pronta, com os pontos decididos: implementar num clone (chat), escrever `../acervos/formulas.json` com as 18 fórmulas conferidas contra os guias, WO para o Code. Fecha a 3b.
2. **Kit de música v2, leva 2** (i-039) — as skills `escrever-letra-suno` e `conceber-album`, com prova de campo num projeto de música do dono; depois, a carta 02 ao KCM.
3. **Pesquisar outras plataformas de música por IA** (i-032) — um turno de pesquisa antes de qualquer mudança de esquema.
4. **Avisar palavra de andamento que contradiz o BPM** (i-029) — pede uma tabela palavra → faixa de BPM, com fonte e data.
````

**Texto novo (substitui a ancora inteira):**

````
1. **Kit de música v2, leva 2** (i-039) — as skills `escrever-letra-suno` e `conceber-album`, com prova de campo num projeto de música do dono; depois, a carta 02 ao KCM.
2. **Pesquisar outras plataformas de música por IA** (i-032) — um turno de pesquisa antes de qualquer mudança de esquema.
3. **Avisar palavra de andamento que contradiz o BPM** (i-029) — pede uma tabela palavra → faixa de BPM, com fonte e data.
````

### E37 — arquivo novo: os testes das fórmulas

**Arquivo novo:** `tests/test_formulas.py` — crie com exatamente o conteudo abaixo (termina com uma quebra de linha).

````
"""Formulas de referencia (0.20.0, DEC-037; criterios da spec meta/specs/261111-formulas.md).
Formulas e acervos sinteticos, feitos a partir do data/demo.json."""
import copy
import json
import os
import subprocess
import sys

from conftest import DEMO, ROOT, changes, import_demo, write_tmp_collection

REFS = [
    {"id": "f-um", "label": "Fórmula um", "source": "Guia A",
     "style": "dream pop, soft female vocal, warm synths, 92 bpm", "notes": "Funciona pela voz na frente."},
    {"id": "f-dois", "label": "Fórmula dois", "source": "Guia B",
     "style": "synthwave, male vocal, analog bass, 95 BPM building to 115 BPM"},
    {"id": "f-tres", "label": "Fórmula três", "source": "Guia A",
     "style": "lo-fi hip hop, mellow piano, vinyl crackle, rain ambience, jazzy chords, "
              "soft drums, tape hiss, warm bass, late night, cozy, chill, nostalgic"},
]


def coll_with(refs, albums=True):
    """O demo com estas formulas; sem `albums`, so as formulas (albums: [])."""
    coll = copy.deepcopy(DEMO)
    if not albums:
        coll["albums"] = []
    coll["styleReferences"] = copy.deepcopy(refs)
    return coll


def open_refs(open_app, refs=REFS, **kw):
    page = open_app(**kw)
    import_demo(page, write_tmp_collection(coll_with(refs)))
    return page


def ref_ids(page):
    return page.evaluate("(App.collection.styleReferences || []).map(r => r.id)")


def open_dialog_by_side(page):
    page.click("#side-formulas-btn")
    page.wait_for_selector("#formulas-dialog[open]")


def test_c1_entradas_so_com_formulas(open_app):
    page = open_refs(open_app)
    assert page.is_visible("#side-formulas-btn")
    assert page.text_content("#side-formulas-btn .t") == "Fórmulas"
    assert page.text_content("#side-formulas-btn .n") == "3"
    # acima de «Todas as faixas»
    top_f = page.eval_on_selector("#side-formulas-btn", "e => e.getBoundingClientRect().top")
    top_all = page.eval_on_selector("#side-albums .side-item", "e => e.getBoundingClientRect().top")
    assert top_f < top_all
    page.click("#more-btn")
    assert page.is_visible("#menu-formulas")
    assert page.text_content("#menu-formulas") == "Fórmulas (3)"
    page.click("#menu-formulas")
    page.wait_for_selector("#formulas-dialog[open]")
    assert page.eval_on_selector_all("#formulas-body .formula", "e => e.length") == 3


def test_c1_sem_formulas_nada_aparece(open_app):
    page = open_app()
    import_demo(page)
    assert page.is_hidden("#side-formulas-btn")
    page.click("#more-btn")
    assert page.is_hidden("#menu-formulas")


def test_c2_janela_agrupa_copia_e_qualidade(open_app):
    page = open_refs(open_app)
    open_dialog_by_side(page)
    groups = page.eval_on_selector_all("#formulas-body .fgroup",
                                       "e => e.map(g => [g.querySelector('h3').textContent,"
                                       " [...g.querySelectorAll('.formula')].map(f => f.dataset.id)])")
    assert groups == [["Guia A", ["f-um", "f-tres"]], ["Guia B", ["f-dois"]]]
    # notas recolhidas; a formula sem notas nao tem o bloco
    assert page.eval_on_selector_all("#formulas-body details.formula-notes", "e => e.map(d => d.open)") == [False]
    for r in REFS:
        sel = f'#formulas-body .formula[data-id="{r["id"]}"]'
        page.click(sel + " .formula-copy")
        assert page.evaluate("navigator.clipboard.readText()") == r["style"]   # byte a byte, sem label nem notes
        got = page.text_content(sel + " .quality")
        want = page.evaluate("s => styleQuality(s, '').textContent", r["style"])
        assert got == want
    # a rampa avisa; a de 12 tags avisa em ambar
    assert "rampa de BPM" in page.text_content('.formula[data-id="f-dois"] .quality')
    assert page.eval_on_selector_all('.formula[data-id="f-tres"] .quality .q.warn', "e => e.length") >= 1


def test_c3_celular_tela_cheia_e_alvos(open_app):
    page = open_refs(open_app, width=390, height=844, mobile=True)
    page.click("#more-btn")
    page.click("#menu-formulas")
    page.wait_for_selector("#formulas-dialog[open]")
    box = page.eval_on_selector("#formulas-dialog", "e => { const r = e.getBoundingClientRect();"
                                " return [r.left, r.top, r.width, r.height]; }")
    assert box[0] == 0 and box[1] == 0 and box[2] == 390 and box[3] == 844
    small = page.eval_on_selector_all(
        "#formulas-dialog button, #formulas-dialog summary",
        "e => e.filter(x => x.offsetParent !== null && x.getBoundingClientRect().height < 44).map(x => x.className)")
    assert small == []
    assert page.evaluate("document.documentElement.scrollWidth") <= 390
    assert page.eval_on_selector("#formulas-body", "e => e.scrollWidth <= e.clientWidth")


def test_c4_excluir_e_desfazer(open_app):
    page = open_refs(open_app)
    open_dialog_by_side(page)
    page.click('.formula[data-id="f-dois"] .formula-del')
    page.click("#confirm-ok-btn")
    page.wait_for_selector("#formulas-status .formula-undo")   # a janela ja foi redesenhada
    assert ref_ids(page) == ["f-um", "f-tres"]
    assert changes(page) == 1
    assert page.is_hidden('.formula[data-id="f-dois"]')
    assert page.text_content("#side-formulas-btn .n") == "2"
    page.click("#formulas-status .formula-undo")
    page.wait_for_function("document.getElementById('formulas-status').textContent.startsWith('Desfeito')")
    assert ref_ids(page) == ["f-um", "f-dois", "f-tres"]   # na mesma posicao
    assert changes(page) == 0
    assert page.is_visible('.formula[data-id="f-dois"]')


def test_c4_excluir_a_ultima_tira_o_campo(open_app):
    page = open_refs(open_app, refs=REFS[:1])
    open_dialog_by_side(page)
    page.click('.formula[data-id="f-um"] .formula-del')
    page.click("#confirm-ok-btn")
    page.wait_for_selector("#formulas-status .formula-undo")
    assert "styleReferences" not in page.evaluate("Object.keys(App.collection)")
    page.click("#formulas-close-btn")
    assert page.is_hidden("#side-formulas-btn")


def test_c5_importar_so_formulas(open_app):
    page = open_refs(open_app, refs=REFS[:2])
    changed = dict(REFS[1], style=REFS[1]["style"] + ", glossy")
    novo = {"id": "f-nova", "label": "Nova", "style": "bossa nova, nylon guitar, brushed drums"}
    src = write_tmp_collection(coll_with([REFS[0], changed, novo], albums=False))
    page.set_input_files("#tracks-input", src)
    page.wait_for_selector("#import-dialog[open]")
    assert page.is_visible("#import-formulas")
    assert page.is_hidden("#import-dest")              # o destino vale so para as faixas
    assert page.text_content("#import-dialog-title") == "Importar fórmulas"
    assert page.eval_on_selector_all("#import-formula-list input", "e => e.map(c => c.checked)") == [True] * 3
    page.click("#import-ok-btn")
    page.wait_for_function("document.getElementById('toast').textContent.includes('importad')")
    assert ref_ids(page) == ["f-um", "f-dois", "f-dois-2", "f-nova"]
    assert page.evaluate("App.collection.styleReferences[2].style") == changed["style"]
    toast = page.text_content("#toast")
    assert toast.startswith("2 fórmulas importadas · 1 fórmula já estava · 1 fórmula renomeada (id repetido)")
    assert changes(page) == 1
    page.click("#toast .toast-btn")                    # «Desfazer»
    page.wait_for_function("App.collection.styleReferences.length === 2")


def test_c5_importar_faixas_e_formulas_soma(open_app):
    page = open_app()
    import_demo(page)
    src_coll = copy.deepcopy(DEMO)
    src_coll["albums"] = [{"id": "outro", "title": "Outro", "songs": [dict(DEMO["albums"][0]["songs"][0], id="nova-faixa")]}]
    src_coll["styleReferences"] = [REFS[0]]
    page.set_input_files("#tracks-input", write_tmp_collection(src_coll))
    page.wait_for_selector("#import-dialog[open]")
    assert page.text_content("#import-dialog-title") == "Importar faixas e fórmulas"
    assert page.is_visible("#import-dest")
    page.click("#import-ok-btn")
    page.wait_for_function("document.getElementById('toast').textContent.includes('importad')")
    assert page.text_content("#toast").startswith("1 faixa e 1 fórmula importadas")


def test_c6_baixar_leva_exportar_nao(open_app, tmp_path):
    page = open_refs(open_app)
    page.click("#more-btn")
    with page.expect_download() as d:
        page.click("#download-btn")
    path = tmp_path / "acervo.json"
    d.value.save_as(path)
    assert json.loads(path.read_text(encoding="utf-8"))["styleReferences"] == REFS
    for expr in ("exportSongJson(App.collection.albums[0].songs[0])", "exportAlbumJson(App.collection.albums[0])"):
        with page.expect_download() as d:
            page.evaluate(expr)
        p = tmp_path / "saida.json"
        d.value.save_as(p)
        assert "styleReferences" not in json.loads(p.read_text(encoding="utf-8"))
    md = page.evaluate("songToMarkdown(App.collection.albums[0].songs[0], true) + albumToMarkdown(App.collection.albums[0])")
    assert all(r["style"] not in md and r["label"] not in md for r in REFS)


def run_validate(path):
    return subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "validate.py"), str(path)],
                          capture_output=True, text=True)


def test_c7_validate_formulas(tmp_path):
    ok = tmp_path / "ok.json"
    ok.write_text(json.dumps(coll_with(REFS), ensure_ascii=False), encoding="utf-8")
    r = run_validate(ok)
    assert r.returncode == 0, r.stdout
    assert "3 fórmulas" in r.stdout
    bad_refs = copy.deepcopy(REFS)
    bad_refs[2]["id"] = "f-um"                                   # id repetido
    bad_refs[1]["style"] = ""                                    # style vazio
    bad_refs.append({"id": "f-quatro", "label": "Q", "style": "epic, choir, [SILENCE - 4 beats]"})
    bad = tmp_path / "bad.json"
    bad.write_text(json.dumps(coll_with(bad_refs), ensure_ascii=False), encoding="utf-8")
    r = run_validate(bad)
    assert r.returncode == 1
    assert "styleReferences[2].id: 'f-um' repetido" in r.stdout
    assert "styleReferences[1].style: vazio" in r.stdout
    assert "styleReferences[3].style: tem colchete" in r.stdout
    extra = copy.deepcopy(REFS)
    extra[0]["bpm"] = 92                                         # campo a mais: o esquema recusa
    ex = tmp_path / "extra.json"
    ex.write_text(json.dumps(coll_with(extra), ensure_ascii=False), encoding="utf-8")
    r = run_validate(ex)
    if "ESQUEMA NAO CONFERIDO" not in r.stdout:                  # sem jsonschema o esquema nao roda
        assert r.returncode == 1 and "ERRO de schema" in r.stdout


def test_c8_falso_positivo_importar_sem_formulas(open_app):
    page = open_app()
    import_demo(page)
    page.set_input_files("#tracks-input", write_tmp_collection(DEMO))
    page.wait_for_selector("#import-dialog[open]")
    assert page.is_hidden("#import-formulas")
    assert page.is_visible("#import-dest")
    assert page.text_content("#import-dialog-title") == "Importar faixas"
    assert "fórmula" not in page.inner_text("#import-dialog").lower()   # o que se ve
    page.click("#import-ok-btn")
    assert "styleReferences" not in page.evaluate("Object.keys(App.collection)")
    assert page.is_hidden("#side-formulas-btn")
````

## Depois de aplicar — conferencia antes do commit

| # | Checagem | Comando | Esperado |
|---|---|---|---|
| 1 | Os arquivos sao os previstos | `sha1sum app/index.html scripts/validate.py schema/collection.schema.json README.md meta/CHANGELOG.md meta/DECISIONS.md meta/IDEAS.md meta/ROADMAP.md meta/STATUS.md tests/test_formulas.py meta/specs/261111-formulas.md logs/2026-11-14.md` | a coluna **chegada** |
| 2 | Versao | `grep -c 'data-role="app-version">v0.20.0<' app/index.html` | `1` |
| 3 | O campo no esquema e a conferencia | `grep -c '"styleReferences"' schema/collection.schema.json` e `grep -c '^def check_formulas' scripts/validate.py` | `1` e `1` |
| 4 | Validacao | `python3 scripts/validate.py; echo "exit=$?"` | `exit=0`, versao 0.20.0 |
| 5 | Testes, se o ambiente local tiver pytest e Playwright | `python -m pytest tests -q` | `61 passed`; sem o ambiente, diga «nao rodado» — a checagem 7 responde |
| 6 | Nada alem do previsto | `GIT_OPTIONAL_LOCKS=0 git status --short --untracked-files=all` | os 12 arquivos da tabela e esta WO |
| 7 | Depois do push: o CI | `gh run list --limit 1`, em laco com `gh run view <id> --json status,conclusion` ate `completed` (o `gh run watch` passa dos 300 s) | relate o estado cru e, se vermelho, o passo que caiu (`gh run view <id> --log-failed`, as ultimas 30 linhas) |

As checagens 2 a 4 rodaram no clone do chat, shell Linux; no Git Bash, **nao testado**. O chat rodou os 61 testes cinco vezes seguidas (cerca de 48 s cada) e mediu que 9 dos 11 novos reprovam na 0.19.0 (os outros 2 sao o falso positivo e a guarda do export, que passam nas duas).
**Esta e qual pergunta?** A 1 responde «esta la?»; a 7 responde «os testes passam no CI, com o esquema conferido?».

## Relatorio de aplicacao

Grave em `../AAMMDD-HHMM-code-cancioneiro-apply-wo0038.txt`, com o carimbo de `date +%y%m%d-%H%M` rodado na hora. Checagem 1 em primeiro lugar e o estado final do CI. **Sem `/wrap` depois desta WO**, e sem secao sua no log, salvo se algo fugir do literal.

## Commit

```
git add app/index.html scripts/validate.py schema/collection.schema.json README.md meta/CHANGELOG.md meta/DECISIONS.md meta/IDEAS.md meta/ROADMAP.md meta/STATUS.md tests/test_formulas.py meta/specs/261111-formulas.md logs/2026-11-14.md meta/workorders/261114-wo0038-formulas-de-referencia.md
```

```
git commit -m "feat: formulas de referencia (0.20.0)" -m "Campo styleReferences na colecao; janela Formulas pela lateral e pelo menu, com Copiar Style, notas recolhidas e Excluir com Desfazer; importacao aceita albums vazio com formulas; validate.py confere ids, label, style e colchete (DEC-037). 11 testes novos. Fecha a Fase 3b."
```

```
git push
```
