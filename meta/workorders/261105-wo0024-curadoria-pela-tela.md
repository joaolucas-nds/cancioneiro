# WO 0024 — Curadoria pela tela (entrega 3), DEC-029 e versao 0.13.0

## Cabecalho

> **Tipo:** mista — CODIGO (`app/index.html`) e registro (CHANGELOG, README, DECISIONS, IDEAS, ROADMAP, STATUS inteiro).
> **Config sugerida:** Sonnet · `/effort medium`. 27 edicoes literais e o STATUS inteiro, aplicados e testados pelo chat num clone de `9382f89`; cada arquivo tem hash de chegada.
> **Pre-requisito:** commit `9382f89`, branch `main`, sincronizada com `origin/main`. O `git status` mostra **so** o que o chat gravou: `M logs/2026-11-05.md`, `M meta/CONTEXT.md`, `M meta/specs/261105-curadoria-pela-tela.md` e esta WO (`?? meta/workorders/...wo0024...`).
> **Base:** spec `meta/specs/261105-curadoria-pela-tela.md` (dentro da DEC-028); o dono aceitou em 2026-11-05 o desvio «fechar a aba nao avisa» (vira a DEC-029 nesta WO).
> **Depende de:** WO 0023, ja aplicada (`e6663d8`, wrap `1328f2d`).
>
> **Arquivos — partida e chegada, os dois medidos pelo chat** (em LF; chegada = aplicar literalmente as edicoes abaixo):
>
> | arquivo | partida (sha1) | chegada (sha1) |
> |---|---|---|
> | `app/index.html` | `72c06fefaa27587d60b9f4dcaa9f515a639c2186` | `445190eba9c0a4b8b49c8a8ac0262c8767890ab8` |
> | `README.md` | `e936e7e607fe4cd1e2c1be0e3675b0d7f46cfe41` | `63289284db96b1a0de0cb7ca58b6981e3c95eca7` |
> | `meta/CHANGELOG.md` | `5bf60b933a6baccb0511c6d9361da4c6ce441de4` | `1b1fef576220d70354fcc01f3c2592efc3b161a0` |
> | `meta/DECISIONS.md` | `5bd8181db118f1b600484080e553e326990e69a8` | `89d1a07c5f64f58ca6cd05d2b57518de353b3d31` |
> | `meta/IDEAS.md` | `a57f21e95e7393d2938b76dc086e1bb6e61acfc2` | `fec7015b5d57328b4f73b04229ae185e9a02dcfb` |
> | `meta/ROADMAP.md` | `2d2b1d4c935eab4db47f6dd93f9561dcc58c9180` | `bad164421321dc3d6d629165fce209420bb519ca` |
> | `meta/STATUS.md` | `4ccd796808749b15ecdd03df23d335e6e3db38e8` | `daa4ff550652a37f5ec2e3b15d0bb4fd58ba6848` |
> | `meta/specs/261105-curadoria-pela-tela.md` | `0bee74df21c3dbfcb4d520922ad4f0cb3593138c` | `0bee74df21c3dbfcb4d520922ad4f0cb3593138c` (gravado pelo chat; só versiona) |
> | `meta/CONTEXT.md` | `7e11afbd7eefab68e78c254ebbada3bf56671453` | `7e11afbd7eefab68e78c254ebbada3bf56671453` (gravado pelo chat; só versiona) |
> | `logs/2026-11-05.md` | `beca0b4dd70c1bbaf7c2729b6431f93af28d415f` | `beca0b4dd70c1bbaf7c2729b6431f93af28d415f` (gravado pelo chat; só versiona) |
>
> **Ancora semantica:** se um trecho-ancora nao bater EXATAMENTE, PARE e reporte.
> **Idempotencia:** antes de cada edicao, procure o texto NOVO INTEIRO; se ja estiver la, PULE e diga no relatorio. Arquivo inteiro (E28): se o hash ja for o de chegada, PULE.
> **Ancoras lidas em:** cada ancora foi recortada pelo chat do arquivo de partida (`git show 9382f89:<arquivo>`, igual ao disco do dono pelos hashes da coluna partida, medidos no disco em 2026-11-05) e conferida como ocorrendo **exatamente 1 vez** no estado em que a edicao e aplicada, na ordem abaixo. Ancora sempre de linha inteira. A E11 troca a funcao `setOrigin` inteira (do `function setOrigin` ate a linha antes de `const savedOrigin`).
> **Canal dos meta neste ciclo = CODE:** esta WO e o registro. A spec, o CONTEXT e o log ja estao gravados pelo chat (DEC-010); a WO so os versiona.

---

## 1. Por que

Entrega 3 da curadoria (i-040, DEC-028), pela spec:

- **Modo «editar»** na linha de origem. Desligado, o cartao fica como antes. Ligado, cada cartao ganha ↑ ↓ «mover…» «excluir», e a origem ganha «importar faixas…».
- **Rascunho:** cada operacao grava a copia guardada e soma uma alteracao. A origem mostra «alterado: N alteracoes nao baixadas» com «Baixar .json», que sai com o **nome do arquivo de origem** e zera. Esquecer ou reimportar com alteracoes pedem confirmacao (janela do app).
- **Importar faixas** com as regras da analise (identica pula; id repetido com conteudo diferente vira `-2`; modulos: falta entra, diferente vira `<id>-2` e e citado, fantasma conta).
- **DEC-029:** fechar a aba nao avisa; so avisa quando a gravacao no navegador falhou.

O app de chegada foi executado pelo chat no Chromium headless (`file://`): **19 de 19** conferencias dos 18 criterios da spec; os testes das entregas 1 e 2 seguem em **15 de 15** e **25 de 25**; prova de vida no app de partida (reprova). `validate.py` exit=0 (com `jsonschema`, `Tudo conforme ao esquema.`), `test_convert_br.py` e `test_convert_guides.py` OK.

**Versao 0.13.0 nesta WO.** A conferencia de tela e do dono, depois do push.

## Edicao 0 — Conferencia de hash e de arvore

```
sha1sum app/index.html README.md meta/CHANGELOG.md meta/DECISIONS.md meta/IDEAS.md meta/ROADMAP.md meta/STATUS.md meta/specs/261105-curadoria-pela-tela.md meta/CONTEXT.md logs/2026-11-05.md
GIT_OPTIONAL_LOCKS=0 git status --short
```

Os dez batem com a coluna **partida**; o `git status` mostra exatamente as quatro linhas do Pre-requisito. Qualquer outra coisa: **PARE e reporte**.

## Edicoes E01 a E28

Na ordem. **Todas as secoes de edicao tem o mesmo titulo, `### Exx — ...`**, inclusive a de arquivo inteiro.
Copie o que esta ENTRE as linhas de quatro crases, sem elas. **O bloco termina na linha de quatro crases, nunca
num titulo:** o CHANGELOG, a DECISIONS, a IDEAS e o STATUS trazem `## ` e `### ` dentro do bloco.

### E01 — app: versao — `app/index.html`

**Ancora, literal:**

````
    <span class="version" data-role="app-version">v0.12.0</span>
````

**Texto novo, literal:**

````
    <span class="version" data-role="app-version">v0.13.0</span>
````

### E02 — app: estilo do modo editar — `app/index.html`

**Ancora, literal:**

````
  .card-foot button { font-size: 12px; padding: 5px 10px; }
````

**Texto novo, literal:**

````
  .card-foot button { font-size: 12px; padding: 5px 10px; }
  /* Curadoria (DEC-028): no modo «editar» o rodape ganha ↑ ↓ mover excluir e quebra linha. */
  .card-foot { flex-wrap: wrap; }
  .card-foot .edit-btn { border-style: dashed; }
  .origin [data-role="edit-btn"][aria-pressed="true"] { background: var(--ink); color: var(--paper); border-color: var(--ink); }
  .origin .dirty { color: var(--ember); font-weight: 600; }
  .import-list { list-style: none; padding: 0; margin: 8px 0 12px; max-height: 45vh; overflow: auto;
    display: flex; flex-direction: column; gap: 8px; }
  .import-list li { display: flex; flex-direction: column; gap: 2px; padding: 6px 10px; background: var(--paper-2); border-radius: 6px; }
  .import-list label { font-size: 13px; margin: 0; }
  .prompt-dialog select, .prompt-dialog input[type="text"] { font: inherit; padding: 4px 6px; margin: 0 0 8px; width: 100%; box-sizing: border-box; }
````

### E03 — app: as janelas da curadoria — `app/index.html`

**Ancora, literal:**

````
<div class="drop-hint" aria-hidden="true">Solte o .json para importar</div>
````

**Texto novo, literal:**

````
<dialog class="prompt-dialog" id="confirm-dialog" aria-labelledby="confirm-text">
  <p id="confirm-text"></p>
  <div class="dialog-actions">
    <button type="button" id="confirm-cancel-btn">cancelar</button>
    <button type="button" id="confirm-ok-btn" class="spacer">confirmar</button>
  </div>
</dialog>

<dialog class="prompt-dialog" id="move-dialog" aria-labelledby="move-dialog-title">
  <h2 id="move-dialog-title">Mover faixa</h2>
  <p>«<span id="move-song-title"></span>» vai para o fim do álbum escolhido.</p>
  <label for="move-target">Álbum</label>
  <select id="move-target"></select>
  <input type="text" id="move-new-title" placeholder="título do álbum novo" hidden>
  <div class="dialog-actions">
    <button type="button" id="move-cancel-btn">cancelar</button>
    <button type="button" id="move-ok-btn" class="spacer">mover</button>
  </div>
</dialog>

<dialog class="prompt-dialog" id="import-dialog" aria-labelledby="import-dialog-title">
  <h2 id="import-dialog-title">Importar faixas</h2>
  <p>De <span id="import-source"></span>. Desmarque o que não quer trazer. Faixa idêntica a uma que já está
  aqui é pulada; com o mesmo id e conteúdo diferente, entra com sufixo (-2).</p>
  <ul class="import-list" id="import-list"></ul>
  <label for="import-target">Destino</label>
  <select id="import-target"></select>
  <input type="text" id="import-new-title" placeholder="título do álbum novo" hidden>
  <div class="dialog-actions">
    <button type="button" id="import-cancel-btn">cancelar</button>
    <button type="button" id="import-ok-btn" class="spacer">importar</button>
  </div>
</dialog>
<input type="file" id="tracks-input" accept=".json,application/json" hidden>

<div class="drop-hint" aria-hidden="true">Solte o .json para importar</div>
````

### E04 — app: o demo do Pages nao tem rascunho — `app/index.html`

**Ancora, literal:**

````
      App.source = DEMO_SOURCE;   // as marcas do demo, o mesmo de quem importa demo.json
````

**Texto novo, literal:**

````
      App.source = DEMO_SOURCE;   // as marcas do demo, o mesmo de quem importa demo.json
      App.saved = false; App.changes = 0;   // sem copia guardada, sem curadoria
````

### E05 — app: importar (1), confirma antes de perder o rascunho — `app/index.html`

**Ancora, literal:**

````
    await bootDone;
    try {
      const before = App.source;
````

**Texto novo, literal:**

````
    await bootDone;
    // Mesmo nome com alteracoes nao baixadas: o arquivo substituiria o rascunho.
    const pending = await recordChanges(file.name);
    if (pending > 0 && !(await confirmAsk("Importar " + file.name + " substitui o rascunho guardado, e as "
        + nPlural(pending, "alteração não baixada se perde", "alterações não baixadas se perdem") + ".", "substituir"))) return;
    try {
      const before = App.source;
````

### E06 — app: importar (2), o estado do rascunho — `app/index.html`

**Ancora, literal:**

````
      const r = await saveAcervo(json, file.name);
      if (r.ok) savedOrigin(file.name, r.savedAt);
````

**Texto novo, literal:**

````
      const r = await saveAcervo(json, file.name);
      App.saved = r.ok; App.changes = 0; App.savedAt = r.savedAt; App.editedAt = null; App.unsavedInMemory = false;
      if (r.ok) savedOrigin(file.name, r.savedAt);
````

### E07 — app: Baixar .json com o nome de origem — `app/index.html`

**Ancora, literal:**

````
function downloadCollection() {
  if (!App.collection) { toast("Nada para baixar ainda"); return; }
  downloadFile(slug(App.collection.title) + ".json",
    JSON.stringify(App.collection, null, 2), "application/json");
}
````

**Texto novo, literal:**

````
/** «Baixar .json». Com rascunho (acervo guardado), sai com o NOME DO ARQUIVO de
    origem, para substituir o antigo, e zera a contagem de alteracoes (DEC-028).
    Sem copia guardada (o demo do Pages), sai com o titulo, como antes. */
function downloadCollection() {
  if (!App.collection) { toast("Nada para baixar ainda"); return; }
  stripInternalKeys(App.collection);
  const name = App.saved && App.source ? App.source : slug(App.collection.title) + ".json";
  downloadFile(name, JSON.stringify(App.collection, null, 2), "application/json");
  if (!App.saved) return;
  App.changes = 0;
  persistDraft(false).then(() => { App.unsavedInMemory = false; });
  toast("Baixado como " + name + ". Substitua o arquivo antigo por este: ele passa a ser a fonte."
        + " Se o navegador acrescentar «(1)» ao nome, tire ao substituir.");
}
````

### E08 — app: o filtro de album sobrevive a curadoria — `app/index.html`

**Ancora, literal:**

````
function populateAlbumFilter() {
  const sel = document.getElementById("filter-album");
  sel.innerHTML = '<option value="">todos</option>';
  (App.collection.albums || []).forEach(a => {
    const o = document.createElement("option");
    o.value = a.id; o.textContent = a.title; sel.appendChild(o);
  });
}
````

**Texto novo, literal:**

````
/** Com `keep` (curadoria), mantem o album escolhido se ele ainda existir. */
function populateAlbumFilter(keep) {
  const sel = document.getElementById("filter-album");
  const cur = sel.value;
  sel.innerHTML = '<option value="">todos</option>';
  (App.collection.albums || []).forEach(a => {
    const o = document.createElement("option");
    o.value = a.id; o.textContent = a.title; sel.appendChild(o);
  });
  if (keep && [...sel.options].some(o => o.value === cur)) sel.value = cur;
}
````

### E09 — app: o cartao sabe o id da faixa — `app/index.html`

**Ancora, literal:**

````
  card.className = "card" + (isUsed(song.id) ? " used" : "");
````

**Texto novo, literal:**

````
  card.className = "card" + (isUsed(song.id) ? " used" : "");
  card.dataset.id = song.id;   // para a curadoria trazer o cartao movido para a tela
````

### E10 — app: os botoes do modo editar no rodape — `app/index.html`

**Ancora, literal:**

````
  foot.appendChild(jsonBtn);
  card.appendChild(foot);
````

**Texto novo, literal:**

````
  foot.appendChild(jsonBtn);
  // Modo «editar» (DEC-028): so com o acervo guardado, que e onde o rascunho mora.
  if (App.editing && App.saved) {
    const loc = locateSong(song.id);
    const mk = (txt, title, fn, off) => {
      const b = document.createElement("button");
      b.type = "button"; b.className = "edit-btn"; b.textContent = txt; b.title = title; b.disabled = !!off;
      b.addEventListener("click", fn);
      foot.appendChild(b);
    };
    mk("↑", "Subir no álbum", () => moveSongBy(song.id, -1), !loc || loc.index === 0);
    mk("↓", "Descer no álbum", () => moveSongBy(song.id, 1), !loc || loc.index === loc.album.songs.length - 1);
    mk("mover…", "Levar para outro álbum ou para um álbum novo", () => openMoveDialog(song.id));
    mk("excluir", "Tirar do rascunho; o arquivo só muda quando você baixar o novo", () => deleteSong(song.id));
  }
  card.appendChild(foot);
````

### E11 — app: a linha de origem com o rascunho e o editar — `app/index.html`

**Ancora, literal:**

````
function setOrigin(text, forgettable) {
  const el = document.getElementById("origin");
  el.textContent = "";
  const t = document.createElement("span"); t.textContent = "Acervo " + text; el.appendChild(t);
  if (Store.db && Store.count > 0) {
    const l = document.createElement("button"); l.type = "button";
    l.textContent = "acervos (" + Store.count + ")"; l.dataset.role = "acervos-btn";
    l.title = "Os acervos guardados neste navegador: abrir outro ou esquecer.";
    l.addEventListener("click", openAcervosDialog);
    el.appendChild(l);
  }
  if (forgettable) {
    const b = document.createElement("button"); b.type = "button"; b.textContent = "esquecer";
    b.title = "Apaga a cópia deste acervo guardada neste navegador. O arquivo no seu computador não é tocado.";
    b.addEventListener("click", () => forgetAcervo(App.source));
    el.appendChild(b);
  }
}
````

**Texto novo, literal:**

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

### E12 — app: abrir um acervo traz o rascunho dele — `app/index.html`

**Ancora, literal:**

````
  App.ui.open = rec.source;
  saveUiState();
  savedOrigin(rec.source, rec.savedAt);
  return true;
````

**Texto novo, literal:**

````
  App.ui.open = rec.source;
  saveUiState();
  App.saved = true; App.changes = rec.changes || 0; App.savedAt = rec.savedAt;
  App.editedAt = rec.editedAt || null; App.unsavedInMemory = false;
  savedOrigin(rec.source, rec.savedAt);
  return true;
````

### E13 — app: a migracao leva a contagem — `app/index.html`

**Ancora, literal:**

````
  const rec = { source: legacy.source || "acervo.json", title: legacy.json.title || legacy.source,
                savedAt: legacy.savedAt, json: legacy.json };
````

**Texto novo, literal:**

````
  const rec = { source: legacy.source || "acervo.json", title: legacy.json.title || legacy.source,
                savedAt: legacy.savedAt, json: legacy.json,
                changes: legacy.changes || 0, editedAt: legacy.editedAt || null };
````

### E14 — app: sem IndexedDB, o rascunho tambem — `app/index.html`

**Ancora, literal:**

````
    records = c ? [{ source: c.source || "acervo.json", title: c.json.title, savedAt: c.savedAt, json: c.json }] : [];
````

**Texto novo, literal:**

````
    records = c ? [{ source: c.source || "acervo.json", title: c.json.title, savedAt: c.savedAt, json: c.json,
                     changes: c.changes || 0, editedAt: c.editedAt || null }] : [];
````

### E15 — app: esquecer confirma antes de perder o rascunho — `app/index.html`

**Ancora, literal:**

````
async function forgetAcervo(source) {
  if (!source) return;
````

**Texto novo, literal:**

````
async function forgetAcervo(source) {
  if (!source) return;
  const pending = await recordChanges(source);
  if (pending > 0 && !(await confirmAsk("Esquecer " + source + "? "
      + nPlural(pending, "alteração não baixada se perde", "alterações não baixadas se perdem") + ".", "esquecer"))) return;
````

### E16 — app: esquecer o ultimo zera o rascunho — `app/index.html`

**Ancora, literal:**

````
  App.collection = null; App.activeModules = {}; App.bpm = {}; App.modulesById = {}; App.source = null;
````

**Texto novo, literal:**

````
  App.collection = null; App.activeModules = {}; App.bpm = {}; App.modulesById = {}; App.source = null;
  App.saved = false; App.changes = 0; App.originText = ""; App.unsavedInMemory = false;
````

### E17 — app: o bloco da curadoria — `app/index.html`

**Ancora, literal:**

````
/* ===================================================================
   Ligacao de eventos + boot
````

**Texto novo, literal:**

````
/* ===================================================================
   Curadoria pela tela (i-040, DEC-028 — spec meta/specs/261105-curadoria-pela-tela.md)
   O app edita o RASCUNHO: a copia guardada do acervo aberto (entrega 2).
   Cada operacao grava o rascunho e soma 1 em App.changes; «Baixar .json»
   baixa com o nome do arquivo de origem e zera. O arquivo continua sendo a
   fonte (DEC-004): o rascunho so vira fonte quando o dono substitui o arquivo.
   Fechar a aba NAO avisa, porque o rascunho ja esta gravado no navegador; so
   avisa quando a gravacao falhou (App.unsavedInMemory).
   =================================================================== */
App.editing = false;          // o interruptor «editar», so da sessao
App.saved = false;            // o acervo aberto tem copia guardada (sem ela, nao ha rascunho)
App.changes = 0;              // alteracoes desde a importacao ou o ultimo «Baixar .json»
App.savedAt = null; App.editedAt = null;
App.unsavedInMemory = false;  // a ultima gravacao do rascunho falhou
App.originText = ""; App.originForget = false;   // o que setOrigin redesenha

const nPlural = (n, um, varios) => n + " " + (n === 1 ? um : varios);

/** Grava o rascunho do acervo aberto; com `count`, soma uma alteracao.
    Devolve false se o navegador recusou (o rascunho fica so na memoria). */
async function persistDraft(count) {
  if (!App.collection || !App.saved) return false;
  if (count) { App.changes++; App.editedAt = new Date().toISOString(); }
  const rec = { source: App.source, title: App.collection.title || App.source, savedAt: App.savedAt,
                editedAt: App.editedAt, changes: App.changes, json: App.collection };
  let ok = true;
  if (Store.db) { try { await dbPut(rec); } catch (e) { ok = false; } }
  else { try { localStorage.setItem(CACHE_KEY, JSON.stringify(rec)); } catch (e) { ok = false; } }
  App.unsavedInMemory = !ok;
  setOrigin();
  return ok;
}

/** Quantas alteracoes nao baixadas tem o acervo guardado com esse nome. */
async function recordChanges(source) {
  if (source === App.source && App.saved) return App.changes;
  if (Store.db) {
    try { const r = await dbGet(source); return (r && r.changes) || 0; } catch (e) { return 0; }
  }
  const c = loadCollectionCache();
  return c && c.source === source ? (c.changes || 0) : 0;
}

/** Janela de confirmacao do app (sem confirm() do navegador). Resolve true/false. */
function confirmAsk(message, okLabel) {
  return new Promise(resolve => {
    const dlg = document.getElementById("confirm-dialog");
    document.getElementById("confirm-text").textContent = message;
    const ok = document.getElementById("confirm-ok-btn");
    ok.textContent = okLabel || "confirmar";
    let done = false;
    const finish = v => { if (done) return; done = true; if (dlg.open) dlg.close(); resolve(v); };
    ok.onclick = () => finish(true);
    document.getElementById("confirm-cancel-btn").onclick = () => finish(false);
    dlg.oncancel = e => { e.preventDefault(); finish(false); };
    dlg.showModal();
  });
}

function locateSong(id) {
  for (const album of (App.collection && App.collection.albums) || []) {
    const i = (album.songs || []).findIndex(s => s.id === id);
    if (i >= 0) return { album, index: i };
  }
  return null;
}
/** Id de album a partir do titulo: sem acento, so [a-z0-9-] (o padrao do esquema). */
function idSlug(title) {
  const s = String(title || "").normalize("NFD").replace(/[̀-ͯ]/g, "");
  return slug(s) || "album";
}
function nextFreeId(base, taken) {
  if (!taken.has(base)) return base;
  let n = 2;
  while (taken.has(base + "-" + n)) n++;
  return base + "-" + n;
}
const allSongIds = () => new Set((App.collection.albums || []).flatMap(a => (a.songs || []).map(s => s.id)));
const albumIdSet = () => new Set((App.collection.albums || []).map(a => a.id));
function addModule(m) {
  (App.collection.styleModules = App.collection.styleModules || []).push(m);
  App.modulesById[m.id] = m;
}

/** Album que ficou sem faixa sai do rascunho: a tela nao mostra album vazio,
    e mante-lo criaria um album invisivel. Devolve o trecho do toast. */
function pruneEmpty(album) {
  if ((album.songs || []).length) return "";
  const list = App.collection.albums, i = list.indexOf(album);
  if (i >= 0) list.splice(i, 1);
  return " · o álbum «" + album.title + "» ficou vazio e saiu";
}

/** Redesenha mantendo a rolagem; com `focusId`, so rola se aquele cartao saiu
    da tela. Um cartao costuma ser mais alto que a janela, entao rolar sempre
    («nearest») mexeria na pagina a cada ↑/↓. */
function rerender(focusId) {
  const y = window.scrollY;
  populateAlbumFilter(true);
  render();
  window.scrollTo(0, y);
  if (focusId) {
    const c = document.querySelector('.card[data-id="' + CSS.escape(focusId) + '"]');
    if (!c) return;
    const r = c.getBoundingClientRect();
    if (r.bottom < 0 || r.top > window.innerHeight) c.scrollIntoView({ block: "start" });
  }
}
/** Fecho comum das operacoes: redesenha, grava o rascunho (+1) e avisa. */
async function afterEdit(msg, focusId) {
  rerender(focusId);
  const ok = await persistDraft(true);
  toast(msg + (ok ? "" : " · não consegui guardar no navegador: baixe o .json para não perder"));
}

function toggleEditing() {
  App.editing = !App.editing;
  setOrigin();
  rerender();
}

/** ↑ / ↓: troca com a vizinha na ordem COMPLETA do album, mesmo com filtro ligado. */
async function moveSongBy(id, delta) {
  const loc = locateSong(id);
  if (!loc) return;
  const songs = loc.album.songs, j = loc.index + delta;
  if (j < 0 || j >= songs.length) return;
  [songs[loc.index], songs[j]] = [songs[j], songs[loc.index]];
  await afterEdit("«" + songs[j].title + "» " + (delta < 0 ? "subiu" : "desceu") + " em «" + loc.album.title + "»", id);
}

/** «mover…»: para o fim de outro album, ou de um album novo. A marca «usei», os
    modulos ligados e o BPM vao junto, porque ficam presos ao id da faixa. */
function openMoveDialog(id) {
  const loc = locateSong(id);
  if (!loc) return;
  const dlg = document.getElementById("move-dialog");
  const sel = document.getElementById("move-target"), inp = document.getElementById("move-new-title");
  document.getElementById("move-song-title").textContent = loc.album.songs[loc.index].title;
  sel.innerHTML = "";
  App.collection.albums.filter(a => a !== loc.album).forEach(a => sel.appendChild(new Option(a.title, a.id)));
  sel.appendChild(new Option("novo álbum…", "__new"));
  inp.value = "";
  const sync = () => { inp.hidden = sel.value !== "__new"; };
  sel.onchange = sync; sync();
  document.getElementById("move-cancel-btn").onclick = () => dlg.close();
  document.getElementById("move-ok-btn").onclick = async () => {
    let target;
    if (sel.value === "__new") {
      const title = inp.value.trim();
      if (!title) { inp.focus(); return; }
      target = { id: nextFreeId(idSlug(title), albumIdSet()), title, songs: [] };
      App.collection.albums.push(target);
    } else {
      target = App.collection.albums.find(a => a.id === sel.value);
    }
    if (!target) return;
    dlg.close();
    const src = loc.album;
    const [song] = src.songs.splice(loc.index, 1);
    target.songs.push(song);
    const gone = pruneEmpty(src);
    await afterEdit("«" + song.title + "» foi para «" + target.title + "»" + gone, song.id);
  };
  dlg.showModal();
}

/** «excluir»: com confirmacao. A faixa sai do rascunho e a marca «usei» dela sai. */
async function deleteSong(id) {
  const loc = locateSong(id);
  if (!loc) return;
  const song = loc.album.songs[loc.index];
  if (!(await confirmAsk("Excluir «" + song.title + "» deste acervo? Ela continua no arquivo até você baixar o novo.", "excluir"))) return;
  loc.album.songs.splice(loc.index, 1);
  const by = App.ui.usedBy && App.ui.usedBy[App.source];
  if (by && by[id]) {
    delete by[id];
    if (!Object.keys(by).length) delete App.ui.usedBy[App.source];
    saveUiState();
  }
  delete App.activeModules[id]; delete App.bpm[id];
  const gone = pruneEmpty(loc.album);
  await afterEdit("«" + song.title + "» excluída do rascunho" + gone);
}

/* ---- Importar faixas (regras da analise, item 4 da spec) ---- */
function pickTracksFile() { document.getElementById("tracks-input").click(); }

/** Le o .json de origem pelo mesmo leitor da importacao (aceita resposta de chat). */
function readTracksFile(file) {
  const reader = new FileReader();
  reader.onload = () => {
    let src;
    try { src = parseCollectionText(reader.result).json; }
    catch (e) { toast("Arquivo inválido: não é um JSON válido"); return; }
    stripInternalKeys(src);
    if (!src || !Array.isArray(src.albums)) { toast("JSON sem 'albums' — não parece uma coleção do Cancioneiro"); return; }
    openImportDialog(src, file.name);
  };
  reader.onerror = () => toast("Não consegui ler o arquivo");
  reader.readAsText(file);
}

function openImportDialog(src, name) {
  const dlg = document.getElementById("import-dialog");
  document.getElementById("import-source").textContent = name;
  const list = document.getElementById("import-list");
  list.textContent = "";
  src.albums.forEach((a, ai) => {
    const li = document.createElement("li");
    const h = document.createElement("strong"); h.textContent = a.title || a.id || "álbum"; li.appendChild(h);
    (a.songs || []).forEach((s, si) => {
      const lab = document.createElement("label");
      const cb = document.createElement("input");
      cb.type = "checkbox"; cb.checked = true; cb.dataset.key = ai + ":" + si;
      lab.appendChild(cb);
      lab.appendChild(document.createTextNode(" " + (s.title || s.id) + " "));
      const m = document.createElement("span"); m.className = "acervo-meta"; m.textContent = s.id;
      lab.appendChild(m);
      li.appendChild(lab);
    });
    list.appendChild(li);
  });
  const sel = document.getElementById("import-target"), inp = document.getElementById("import-new-title");
  sel.innerHTML = "";
  sel.appendChild(new Option("manter os álbuns de origem", "__keep"));
  App.collection.albums.forEach(a => sel.appendChild(new Option(a.title, a.id)));
  sel.appendChild(new Option("novo álbum…", "__new"));
  inp.value = "";
  const sync = () => { inp.hidden = sel.value !== "__new"; };
  sel.onchange = sync; sync();
  document.getElementById("import-cancel-btn").onclick = () => dlg.close();
  document.getElementById("import-ok-btn").onclick = async () => {
    if (sel.value === "__new" && !inp.value.trim()) { inp.focus(); return; }
    const keys = new Set([...list.querySelectorAll('input[type="checkbox"]')]
      .filter(c => c.checked).map(c => c.dataset.key));
    dlg.close();
    await importTracks(src, keys, sel.value, inp.value.trim());
  };
  dlg.showModal();
}

/** Traz as faixas marcadas. Id repetido: identico (objeto inteiro serializado,
    nunca so o titulo) pula; diferente entra com sufixo. Modulo citado: o que
    falta entra; o identico nao duplica; o diferente entra com sufixo e a faixa
    importada passa a citar o id novo; o que nao existe em lugar nenhum fica
    citado e e contado (FIX-006: nada de saneamento mudo). */
async function importTracks(src, keys, dest, newTitle) {
  const coll = App.collection;
  const n = { imported: 0, same: 0, renamed: 0, modsAdded: 0, modsRenamed: 0, missing: 0 };
  const ids = allSongIds();
  const srcMods = {};
  (src.styleModules || []).forEach(m => { if (m && typeof m.id === "string") srcMods[m.id] = m; });
  const modIds = new Set(Object.keys(App.modulesById));
  const renamedMods = {};
  const findSong = id => {
    for (const a of coll.albums) { const s = (a.songs || []).find(x => x.id === id); if (s) return s; }
    return null;
  };
  let fixed = null;   // destino unico (album escolhido ou novo); null = manter os de origem
  if (dest === "__new") fixed = { id: nextFreeId(idSlug(newTitle), albumIdSet()), title: newTitle, songs: [] };
  else if (dest !== "__keep") fixed = coll.albums.find(a => a.id === dest) || null;

  src.albums.forEach((a, ai) => (a.songs || []).forEach((orig, si) => {
    if (!keys.has(ai + ":" + si)) return;
    const s = JSON.parse(JSON.stringify(orig));
    const ex = ids.has(s.id) ? findSong(s.id) : null;
    if (ex && JSON.stringify(ex) === JSON.stringify(s)) { n.same++; return; }
    if (ids.has(s.id)) { s.id = nextFreeId(s.id, ids); n.renamed++; }
    if (Array.isArray(s.styleModules)) {
      s.styleModules = s.styleModules.map(ref => {
        if (typeof ref !== "string") { n.missing++; return ref; }
        const sm = srcMods[ref], em = App.modulesById[ref];
        if (!sm) { if (!em) n.missing++; return ref; }
        if (!em) { addModule(JSON.parse(JSON.stringify(sm))); modIds.add(ref); n.modsAdded++; return ref; }
        if (JSON.stringify(em) === JSON.stringify(sm)) return ref;
        if (!renamedMods[ref]) {
          const nid = nextFreeId(ref, modIds); modIds.add(nid);
          const copy = JSON.parse(JSON.stringify(sm)); copy.id = nid;
          addModule(copy); renamedMods[ref] = nid; n.modsRenamed++;
        }
        return renamedMods[ref];
      });
    }
    let target = fixed;
    if (!target) {
      target = coll.albums.find(x => x.id === a.id);
      if (!target) {
        const taken = albumIdSet();
        target = { id: a.id && !taken.has(a.id) ? a.id : nextFreeId(idSlug(a.title), taken),
                   title: a.title || a.id || "Álbum importado", songs: [] };
        coll.albums.push(target);
      }
    } else if (!coll.albums.includes(target)) {
      coll.albums.push(target);
    }
    target.songs.push(s);
    ids.add(s.id);
    n.imported++;
  }));

  const parts = [];
  if (n.same) parts.push(n.same + (n.same === 1 ? " já estava" : " já estavam"));
  if (n.renamed) parts.push(nPlural(n.renamed, "renomeada", "renomeadas") + " (id repetido)");
  if (n.modsAdded) parts.push(nPlural(n.modsAdded, "módulo trazido", "módulos trazidos"));
  if (n.modsRenamed) parts.push(nPlural(n.modsRenamed, "módulo renomeado", "módulos renomeados"));
  if (n.missing) parts.push(nPlural(n.missing, "citado que não existe", "citados que não existem"));
  const tail = parts.length ? " · " + parts.join(" · ") : "";
  if (!n.imported) { toast("Nada importado" + tail); return; }
  await afterEdit(nPlural(n.imported, "faixa importada", "faixas importadas") + tail);
}

document.getElementById("tracks-input").addEventListener("change", e => {
  if (e.target.files[0]) readTracksFile(e.target.files[0]);
  e.target.value = "";
});
// So avisa ao fechar a aba se o rascunho NAO esta gravado (a gravacao falhou).
window.addEventListener("beforeunload", e => {
  if (App.unsavedInMemory) { e.preventDefault(); e.returnValue = ""; }
});

/* ===================================================================
   Ligacao de eventos + boot
````

### E18 — CHANGELOG: 0.13.0 — `meta/CHANGELOG.md`

**Ancora, literal:**

````
## [0.12.0] — 2026-11-05
````

**Texto novo, literal:**

````
## [0.13.0] — 2026-11-05

Terceira e última entrega da curadoria no app (i-040, DEC-028): editar o acervo pela tela.

### Added
- **Modo «editar»**, na linha de origem: liga a curadoria. Desligado, o cartão fica como antes. Ligado, cada cartão ganha ↑, ↓, «mover…» (para outro álbum ou para um álbum novo) e «excluir» (com confirmação), e a linha de origem ganha «importar faixas…».
- **Rascunho:** cada operação grava a cópia do acervo no navegador e soma uma alteração. A linha de origem mostra «alterado: N alterações não baixadas» com o botão «Baixar .json», que baixa com o **nome do arquivo de origem**, para substituir o antigo, e zera a contagem. Esquecer ou reimportar com alterações pendentes pedem confirmação.
- **Importar faixas** de outro `.json`, inclusive uma faixa exportada solta: uma janela lista as faixas, todas marcadas, e o destino (por padrão, o álbum de origem de cada uma). Faixa idêntica é pulada; mesmo id com conteúdo diferente entra com sufixo (`-2`). Módulo citado: o que falta entra; o diferente entra com sufixo, e a faixa passa a citá-lo; o que não existe em lugar nenhum fica citado. O toast conta cada caso.

### Changed
- «Baixar .json» de um acervo guardado sai com o nome do arquivo de origem, não com o título.
- Álbum que fica sem faixa sai do acervo.
- Fechar a aba não avisa: o rascunho já está gravado. Só avisa se a gravação no navegador falhar (DEC-029).

Spec `meta/specs/261105-curadoria-pela-tela.md`: 19 de 19 conferências dos 18 critérios no Chromium headless, com prova de vida no app da 0.12.0; os testes das entregas 1 e 2 seguem em 15 de 15 e 25 de 25.

---

## [0.12.0] — 2026-11-05
````

### E19 — README: versao — `README.md`

**Ancora, literal:**

````
> **Estado:** v0.12.0 — ferramenta em uso. Lê e guarda vários acervos, copia por campo, troca módulos de estilo, ajusta o BPM, **mede cada prompt contra os limites do Suno**, exporta Markdown, exporta uma faixa como `.json` e **entrega o prompt para chats gerarem canções no esquema**. Publicada no GitHub Pages. Ver `meta/ROADMAP.md`.
````

**Texto novo, literal:**

````
> **Estado:** v0.13.0 — ferramenta em uso. Lê, guarda e edita vários acervos, copia por campo, troca módulos de estilo, ajusta o BPM, **mede cada prompt contra os limites do Suno**, exporta Markdown, exporta uma faixa como `.json` e **entrega o prompt para chats gerarem canções no esquema**. Publicada no GitHub Pages. Ver `meta/ROADMAP.md`.
````

### E20 — README: a curadoria — `README.md`

**Ancora, literal:**

````
6. Exporte em `.md` (faixa, álbum ou acervo inteiro) se precisar do formato legível. Uma faixa também sai em `.json` (*exportar .json* no cartão): é um acervo de uma faixa só, com os módulos que ela usa, para mandar a um chat ou juntar a outro acervo.
````

**Texto novo, literal:**

````
6. Exporte em `.md` (faixa, álbum ou acervo inteiro) se precisar do formato legível. Uma faixa também sai em `.json` (*exportar .json* no cartão): é um acervo de uma faixa só, com os módulos que ela usa, para mandar a um chat ou juntar a outro acervo.
7. Para reorganizar, ligue *editar* na linha de origem: cada cartão ganha ↑ ↓, *mover…* e *excluir*, e *importar faixas…* traz faixas de outro `.json`. As mudanças ficam num rascunho no navegador; *Baixar .json* baixa com o nome do arquivo original — substitua o antigo por ele, e ele passa a ser a fonte.
````

### E21 — README: fonte de verdade com o rascunho — `README.md`

**Ancora, literal:**

````
O acervo canônico são **arquivos JSON** no esquema: os exemplos versionados em `data/`, e o acervo pessoal fora do repo (DEC-026). O navegador guarda **cópias dos acervos importados** (IndexedDB) e, no localStorage, as marcações por acervo e a estrutura do cartão — cache, nunca a fonte: a linha de origem diz de onde a cópia veio e quando, e *esquecer* a apaga sem tocar no arquivo. Ver `meta/DECISIONS.md` (DEC-004, DEC-022, DEC-028).
````

**Texto novo, literal:**

````
O acervo canônico são **arquivos JSON** no esquema: os exemplos versionados em `data/`, e o acervo pessoal fora do repo (DEC-026). O navegador guarda **cópias dos acervos importados** (IndexedDB) e, no localStorage, as marcações por acervo e a estrutura do cartão — cache, nunca a fonte: a linha de origem diz de onde a cópia veio e quando, e *esquecer* a apaga sem tocar no arquivo. Com *editar*, a cópia vira rascunho até você baixar o `.json` e substituir o arquivo. Ver `meta/DECISIONS.md` (DEC-004, DEC-022, DEC-028, DEC-029).
````

### E22 — DECISIONS: DEC-029 — `meta/DECISIONS.md`

**Ancora, literal:**

````
**Consequências:** (+) Curar pela tela, sem chat nem WO; o reagrupamento da i-038 passa a caber no app. (+) Trocar de acervo sem importar de novo. (−) A DEC-022 perde «a cópia é igual ao arquivo»: depois da entrega 3 a cópia pode estar à frente do arquivo, e a marca de rascunho é o que avisa. (−) Rascunho não baixado se perde se o navegador limpar os dados. (−) Regerar pelos guias depois de curar apaga a curadoria — por isso o item 3.
````

**Texto novo, literal:**

````
**Consequências:** (+) Curar pela tela, sem chat nem WO; o reagrupamento da i-038 passa a caber no app. (+) Trocar de acervo sem importar de novo. (−) A DEC-022 perde «a cópia é igual ao arquivo»: depois da entrega 3 a cópia pode estar à frente do arquivo, e a marca de rascunho é o que avisa. (−) Rascunho não baixado se perde se o navegador limpar os dados. (−) Regerar pelos guias depois de curar apaga a curadoria — por isso o item 3.

## DEC-029 — Fechar a aba não avisa sobre alterações não baixadas; só avisa quando a gravação no navegador falhou (revê um ponto da análise da curadoria)

**Data:** 2026-11-05
**Status:** aceita
**Contexto:** A análise da curadoria (F1) previa confirmação ao fechar a aba com alteração não baixada. Na entrega 2, o acervo passou a ficar gravado no navegador; na entrega 3, cada operação grava o rascunho na hora. Fechar a aba, portanto, não perde nada. Proposto na spec `meta/specs/261105-curadoria-pela-tela.md` e aceito pelo dono em 2026-11-05 («sem o aviso ao fechar a aba»).
**Decisão:** O app não avisa ao fechar a aba. A única exceção é quando a gravação do rascunho no navegador falha: o toast avisa na hora, e o aviso ao fechar fica ligado até o próximo «Baixar .json». Esquecer e reimportar com alterações pendentes continuam pedindo confirmação, porque esses dois apagam o rascunho.
**Alternativas consideradas:** avisar sempre que houver alteração não baixada (apareceria em todo fechamento, sem perda real, e ensinaria a ignorar o aviso); não avisar nem quando a gravação falha (perderia o rascunho em silêncio).
**Consequências:** (+) O aviso só aparece quando há o que perder. (−) Um rascunho gravado pode ficar meses sem ser baixado; a marca «alterado: N alterações não baixadas» na linha de origem é o lembrete.
````

### E23 — IDEAS: i-040 entregue (1) — `meta/IDEAS.md`

**Ancora, literal:**

````
### i-040 🔨 Curadoria no app: excluir, exportar e importar faixas
````

**Texto novo, literal:**

````
### i-040 ✅ Curadoria no app: excluir, exportar e importar faixas
````

### E24 — IDEAS: i-040 entregue (2) — `meta/IDEAS.md`

**Ancora, literal:**

````
**Decidida (2026-11-02, DEC-028):** análise `meta/analises/261102-ANALISE-curadoria-no-app.md`, F1 + G1 em três entregas. **Entrega 1 feita (0.11.0):** exportar faixa como `.json` (spec `meta/specs/261102-exportar-faixa-json.md`). A entrega 2 é a i-041; a 3 é o resto desta ideia (excluir, reordenar, mover, novo álbum, importar faixas), num rascunho marcado.
````

**Texto novo, literal:**

````
**Decidida (2026-11-02, DEC-028):** análise `meta/analises/261102-ANALISE-curadoria-no-app.md`, F1 + G1 em três entregas. **Entrega 1 feita (0.11.0):** exportar faixa como `.json` (spec `meta/specs/261102-exportar-faixa-json.md`). A entrega 2 é a i-041; a 3 é o resto desta ideia (excluir, reordenar, mover, novo álbum, importar faixas), num rascunho marcado.
**Entregue (0.13.0, 2026-11-05):** a entrega 3, spec `meta/specs/261105-curadoria-pela-tela.md`, WO 0024 — modo «editar», ↑ ↓, mover, novo álbum, excluir, importar faixas, rascunho com «Baixar .json» pelo nome de origem. Fechar a aba não avisa (DEC-029).
````

### E25 — IDEAS: i-043 com o gatilho atingido — `meta/IDEAS.md`

**Ancora, literal:**

````
**Medido (2026-11-04, sonda):** no Chrome 156 do dono existem as três APIs — `showSaveFilePicker`, `showOpenFilePicker` e `getAsFileSystemHandle` (arrastar com permissão de gravar). Falta só a entrega 3.
````

**Texto novo, literal:**

````
**Medido (2026-11-04, sonda):** no Chrome 156 do dono existem as três APIs — `showSaveFilePicker`, `showOpenFilePicker` e `getAsFileSystemHandle` (arrastar com permissão de gravar). Falta só a entrega 3.
**Gatilho atingido (2026-11-05):** a entrega 3 está pronta (0.13.0). Com ela, o passo que sobra é baixar e substituir o arquivo; gravar direto tira esse passo.
````

### E26 — IDEAS: a frente de interface (i-045 a i-047) — `meta/IDEAS.md`

**Ancora, literal:**

````
Achado no teste da entrega 2 (2026-11-05): o CSS `.controls { display: flex }` vence o atributo `hidden` que o `render()` põe na barra quando não há acervo, então os filtros vazios ficam na tela no estado inicial e depois de esquecer todos. Já era assim antes da 0.12.0. O conserto provável é uma linha (`.controls[hidden] { display: none; }`), mas muda o que o dono vê ao abrir o app vazio — conferir na tela antes.
````

**Texto novo, literal:**

````
Achado no teste da entrega 2 (2026-11-05): o CSS `.controls { display: flex }` vence o atributo `hidden` que o `render()` põe na barra quando não há acervo, então os filtros vazios ficam na tela no estado inicial e depois de esquecer todos. Já era assim antes da 0.12.0. O conserto provável é uma linha (`.controls[hidden] { display: none; }`), mas muda o que o dono vê ao abrir o app vazio — conferir na tela antes.

### i-045 💡 Cabeçalho compacto
`[relatado pelo dono, 2026-11-05]` A barra do topo está «muito folgada»; deixá-la quase colada às bordas dos botões. Medido nas capturas dele (Chrome, janela de 720 px de altura): o cabeçalho é fixo (`position: sticky`) e ocupa uns 85 px. Objetivo dito por ele: uma interface «bonita, profissional, intuitiva». Faz parte da frente de interface (i-044 a i-047), que vem **depois** das funcionalidades em curso, por pedido dele, e começa por um turno de pesquisa.

### i-046 💡 Filtros que acompanham a rolagem, e visões do acervo
`[relatado pelo dono, 2026-11-05]` A barra «Álbum · Estado · Uso · buscar» some ao rolar uma lista grande (nas capturas, só o cabeçalho fica fixo). Ele quer que ela fique fixa ou que se possa chamá-la. Inspirações citadas: o controle e a organização de e-commerce e de tabelas, e de Notion e Airtable, com visões (lista, tabela) e opções melhores. Pede pesquisa antes de spec.

### i-047 💡 Painel lateral com abas
`[relatado pelo dono, 2026-11-05]` Painéis que abrem pela lateral direita, com etiquetas no estilo de «bookmarks». Exemplo dele: os acervos da entrega 2 também numa barra lateral, além da janela. Junto da i-046 na pesquisa. O arrastar cartões para reordenar (fora da entrega 3) entra nesta frente.
````

### E27 — ROADMAP: curadoria concluida e a frente de interface — `meta/ROADMAP.md`

**Ancora, literal:**

````
- 🔨 Curadoria no app e vários acervos (i-040, i-041, DEC-028), em três entregas: ✅ exportar faixa como `.json` (0.11.0) · ✅ vários acervos no navegador (IndexedDB, marcas «usei» por acervo; 0.12.0) · ⬜ curadoria pela tela (excluir, reordenar, mover, novo álbum, importar faixas) num rascunho marcado.
````

**Texto novo, literal:**

````
- ✅ Curadoria no app e vários acervos (i-040, i-041, DEC-028), em três entregas: ✅ exportar faixa como `.json` (0.11.0) · ✅ vários acervos no navegador (IndexedDB, marcas «usei» por acervo; 0.12.0) · ✅ curadoria pela tela (excluir, reordenar, mover, novo álbum, importar faixas) num rascunho, com «Baixar .json» pelo nome de origem (0.13.0, DEC-029).
- ⬜ Refino da interface (i-044 a i-047): cabeçalho compacto, filtros que acompanham a rolagem, visões de lista e tabela, painel lateral. Começa por um turno de pesquisa (Notion, Airtable, filtros de e-commerce) antes de spec.
````

### E28 — STATUS inteiro — `meta/STATUS.md`

**Arquivo inteiro, literal** (substitui o arquivo; chegada `daa4ff550652a37f5ec2e3b15d0bb4fd58ba6848`):

````
# STATUS.md — Cancioneiro

> **O agora.** O que funciona, o que está em progresso, o que está quebrado, backlog curto.
> Rolante: item resolvido sai daqui e vai para o CHANGELOG. Médio/longo prazo vive no ROADMAP.

**Versão atual:** 0.13.0 · **Fase:** 3a, 3a.2, o BPM da 3b, o prompt-modelo e as conveniências de uso concluídos e conferidos · os álbuns antigos convertidos (i-008, fora do repo) · curadoria no app concluída nas três entregas (DEC-028, DEC-029) · kit de música lido pelo KCM, à espera da resposta (i-039)

---

## Última conversa (2026-11-05, curadoria no app: entrega 3, WO 0024)

- **Entrega 2 conferida na tela pelo dono** (2026-11-05, roteiro de 8 itens, tudo OK `[relatado pelo dono]`); a carta 02 foi levada ao KCM.
- **Entrega 3 (0.13.0):** modo «editar» na linha de origem; ↑ ↓, mover (inclusive para álbum novo), excluir e importar faixas, num rascunho gravado a cada operação; «Baixar .json» com o nome de origem zera a contagem. Fechar a aba não avisa, só quando a gravação falha (DEC-029). Spec `meta/specs/261105-curadoria-pela-tela.md`; 19 de 19 conferências no Chromium headless, testadas pelo chat.
- **Ideias de interface do dono** (i-045 a i-047, com a i-044): cabeçalho compacto, filtros que acompanham a rolagem, visões no estilo Notion e Airtable, painel lateral. Vêm depois das funcionalidades, com pesquisa antes.
- **Este bloco substitui o anterior, de 2026-11-04 e 2026-11-05** (entrega 2). O que ele dizia está no CHANGELOG [0.12.0], na spec `meta/specs/261104-varios-acervos.md` e em `logs/2026-11-05.md` (Conversas 1 e 2).

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
- **Vários acervos no navegador** (0.12.0, DEC-028): cada importado fica no IndexedDB pelo nome do arquivo; «acervos (N)» na linha de origem abre a janela para abrir ou esquecer; reabre no último aberto; marcas «usei» por acervo. Sem IndexedDB, guarda só o último, como antes.
- **Curadoria pela tela** (0.13.0, DEC-028, DEC-029): «editar» na linha de origem; ↑ ↓, mover, novo álbum, excluir e importar faixas num rascunho gravado no navegador; «alterado: N alterações não baixadas» com «Baixar .json» pelo nome de origem.
- **Prompt-modelo** (`schema/PROMPT-PARA-CHATS.md`, DEC-021, DEC-023): contrato de módulo, style com 6 a 8 tags e até 10 com os módulos ligados; pede o JSON como arquivo e, sem arquivo, em bloco de código. Dois retestes em 2026-10-29: 6 de 6 faixas dentro do contrato e do orçamento, nos dois.
- **Botões «Prompt» e «Exemplo»** (0.8.0, DEC-021): buscam o prompt e o `data/demo.json` do repositório no clique; a janela do prompt recebe o «Meu pedido».
- **Conveniências (0.9.0, DEC-022, DEC-023):** «Estrutura» do cartão (ordem e blocos visíveis, no navegador); copiar o título; arrastar o `.json` para importar; o último acervo importado volta ao abrir, com origem, data e «esquecer»; a importação aceita a resposta do chat colada inteira e avisa.
- **Publicado no GitHub Pages** em `https://joaolucas-nds.github.io/cancioneiro/app/index.html` — o push em `main` publica.

## Em progresso

- **Kit de música no KCM (i-039)** — o KCM leu a carta 01 e responde por carta, sem data. Gatilho: sem resposta até o primeiro projeto de música novo, o projeto usa o kit à mão (`kit-musica/README.md`).

## Quebrado / pendências que travam

- (nada quebrado)

## Pendências do dono

- **Conferir a entrega 3 na tela** — roteiro na conversa de 2026-11-05 (WO 0024), depois do push.
- **Instalar o validador de esquema nesta máquina.** Sem `jsonschema` e `referencing`, o `validate.py` só confere sintaxe e diz `ESQUEMA NAO CONFERIDO` na última linha. Uma vez, no CMD: `pip install jsonschema referencing --break-system-packages`. Depois, `python3 scripts/validate.py` deve terminar em `Tudo conforme ao esquema.`

## Backlog curto (próximas ações concretas)

1. **Gravar direto no arquivo** (i-043) — o gatilho foi atingido com a entrega 3; tira o passo «baixar e substituir». Só Chrome e Edge; «Baixar» continua onde não houver.
2. **Frente de interface** (i-044 a i-047) — um turno de pesquisa (Notion, Airtable, filtros de e-commerce) antes de spec: cabeçalho compacto, filtros que acompanham a rolagem, visões, painel lateral, a barra que não some sem acervo.
3. **Rampa de BPM** (i-042) — três faixas BR reprovam no `validate.py` por mudarem de andamento de propósito.
4. **Pesquisar outras plataformas de música por IA** (i-032) — um turno de pesquisa antes de qualquer mudança de esquema.
5. **Avisar palavra de andamento que contradiz o BPM** (i-029) — pede uma tabela palavra → faixa de BPM, com fonte e data.
6. **Importar prompts prontos dos álbuns como módulos** — o último ⬜ da 3b no ROADMAP; o índice-mestre da BR e os «estilos originais» do VOL5 trazem fórmulas de estilo.

## Notas de estado

- **Repo local do dono:** `C:\Users\alexk\Tools\cancioneiro\cancioneiro` (Windows). O chat lê e grava na pasta vinculada; commit e push são do Code (DEC-010). A pasta-pai guarda relatórios, notas e o acervo do dono, fora do Git; o lido vai para `../notas-arquivadas/`.
- **Canal:** pasta vinculada é o padrão; a cópia achatada (FlatDrop) é reserva (DEC-017).
- **Limites do Suno:** o v6 saiu em 2026-09-09 e a nota oficial não documenta limite de campo; os números do painel vêm de fonte secundária, com fonte e data no `QUALITY_LIMITS` (DEC-018). Outra fonte secundária (2026-08) põe o ideal em 4 a 7 descritores; o prompt usa 6 a 8. Reconferir quando houver documentação oficial. O `meta/HISTORY.md` §5 ganhou a interface do v6 vista na conta (2026-10-29); o resto do arquivo ainda descreve o v5.5.
- **Exclude no v6-mini:** o formulário gratuito não tem o campo (capturas de 2026-10-29). Desde a 0.9.1 (DEC-025) o bloco vem oculto por padrão, com o aviso «no X → Exclude» junto (D3); o dado continua no JSON e no export. Quem usa o campo liga em «Estrutura».
- **Navegador (DEC-004, DEC-022, DEC-028):** guarda as cópias dos acervos importados (IndexedDB, banco `cancioneiro`), as marcas «usei» por acervo e a estrutura do cartão (`localStorage`, `cancioneiro:ui`). As cópias são cache: se o arquivo mudou fora, importe de novo; a linha de origem diz quando a cópia foi feita.
- **Rascunho (DEC-028, DEC-029):** com alterações, a cópia guardada está à frente do arquivo até «Baixar .json» e substituir. A marca na linha de origem é o lembrete; esquecer e reimportar pedem confirmação.
- **No `file://`, todas as páginas locais dividem o armazenamento** (sonda de 2026-11-04): o app só lê e grava o que tem o nome `cancioneiro`. O `file://` e o Pages são origens diferentes — o que está guardado num não aparece no outro.
- **Conversores são de primeira geração (DEC-028):** depois de mudar um acervo (à mão ou, com a entrega 3, no app), não rode o conversor por cima dele.
- **Botões «Prompt» e «Exemplo»:** dependem de rede e do Pages. No `file://`, só funcionam se o Pages aceitar o `fetch` de uma página local — não conferido (o dono abriu o `file://` em 2026-10-29, sem relatar o resultado do botão); sem isso, a janela mostra o link para a versão publicada (DEC-021).
- **Estado de sessão** (módulos ligados e BPM escolhido) sobrevive a filtro, busca e «marcar usei»; volta ao acervo ao recarregar a página ou importar de novo (FIX-008, DEC-020).
- **Limite conhecido:** `tryAutoLoad` (carregamento automático pelo Pages) não saneia chaves internas — só a importação por arquivo faz isso. Inócuo enquanto nenhum acervo contaminado for para `data/`.
- **Pendência de contexto — ASU:** o dono perguntou se o «modo ASU» do KCM seria melhor que o modo Code para este projeto; ficou pendente até ele trazer a descrição do ASU `[relatado pelo dono, sem material de apoio]`.
- Design: na recomposição do Style a base manda — desligar um módulo não remove o que já está no style base; módulos só somam. O dedup compara sequências de palavras (FIX-003). Os módulos de gênero e de andamento costumam custar 0 tag por isso (DEC-019). O chip de andamento é atalho do controle de BPM, no máximo um ligado (DEC-020).
````

## Fora de escopo

- Renomear ou reordenar albuns, editar o texto de uma faixa, desfazer, arrastar cartoes (fora da spec).
- A i-043 (gravar direto no arquivo) e a frente de interface (i-044 a i-047): so registradas.
- Spec, CONTEXT e log: ja gravados pelo chat; nao edite.
- Nada em `data/`, `schema/`, `scripts/` ou `kit-musica/`.

## Armadilhas desta WO

- **`autocrlf=true` na maquina do dono:** os hashes valem no disco em LF, antes do `add`. Nao rode `git checkout -- <arquivo>`: ele regrava em CRLF.
- **A E17 e longa** (o bloco da curadoria inteiro, antes de «Ligacao de eventos + boot»): se o aplicador ler ancora linha a linha, compare o bloco inteiro; o hash de chegada do `app/index.html` e a prova.
- **O `validate.py` desta maquina termina em `ESQUEMA NAO CONFERIDO`** (falta `jsonschema`): estado conhecido.
- **Os testes escrevem no stderr:** use `2>&1 >/dev/null | tail -1`.

## Depois de aplicar — conferencia antes do commit

| # | Checagem | Comando | Esperado |
|---|---|---|---|
| 1 | **Os dez arquivos sao os testados** | `sha1sum app/index.html README.md meta/CHANGELOG.md meta/DECISIONS.md meta/IDEAS.md meta/ROADMAP.md meta/STATUS.md meta/specs/261105-curadoria-pela-tela.md meta/CONTEXT.md logs/2026-11-05.md` | a coluna **chegada**, os dez. **Prova as 28 edicoes.** |
| 2 | Validacao | `python3 scripts/validate.py; echo "exit=$?"` | `exit=0`, com a linha `OK  versao 0.13.0 igual em CHANGELOG, app, README e STATUS`; ultima linha `Tudo conforme ao esquema.` ou `ESQUEMA NAO CONFERIDO (...)` (esta maquina) |
| 3 | Os conversores seguem passando | `python3 scripts/test_convert_br.py 2>&1 >/dev/null \| tail -1` e `python3 scripts/test_convert_guides.py 2>&1 >/dev/null \| tail -1` | `OK` e `OK` |
| 4 | O codigo novo | `grep -c '^async function importTracks' app/index.html`, `grep -c '^function confirmAsk' app/index.html`, `grep -c '^async function persistDraft' app/index.html` | `1`, `1`, `1` |
| 5 | O registro | `grep -m1 '^## \[' meta/CHANGELOG.md`, `grep -c '^## DEC-029 ' meta/DECISIONS.md`, `grep -c '^### i-047 ' meta/IDEAS.md` | `## [0.13.0] — 2026-11-05`, `1`, `1` |
| 6 | As pendencias resolvidas sairam | `grep -c '^- \*\*Levar a carta 02' meta/STATUS.md`, `grep -c '^- \*\*Conferir a entrega 2 na tela' meta/STATUS.md` | `0`, `0` |
| 7 | Nada alem do previsto | `GIT_OPTIONAL_LOCKS=0 git status --short --untracked-files=all` | os dez arquivos e esta WO, e nada mais (nenhum `.txt`, nenhum `__pycache__`) |

**Os tres campos de cada passo:** as sete sao rodadas por **quem aplica (o Code)**, na raiz do repo, em Git Bash,
com `LC_ALL=C.UTF-8`. **Chega no ramo?** A checagem 1 cobre os dez arquivos inteiros, inclusive o `app/index.html`
que o chat executou (`setOrigin`, `persistDraft`, `moveSongBy`, `openMoveDialog`, `deleteSong`, `importTracks`,
`downloadCollection`). **Esta e qual pergunta?** A 2 e a 3 respondem «funciona?»; as outras, «esta la?». O «funciona?»
da curadoria no navegador do dono e dele, depois do push, pelo roteiro do chat.

## Relatorio de aplicacao

Grave em `../261105-HHMM-code-cancioneiro-apply-wo0024.txt`, com o `HHMM` de `date +%y%m%d-%H%M` rodado na
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
git commit -m "feat: curadoria pela tela e versao 0.13.0" -m "Entrega 3 da curadoria (i-040, DEC-028): modo editar; subir, descer, mover, novo album, excluir e importar faixas num rascunho gravado no navegador; Baixar .json com o nome de origem zera a contagem. DEC-029: fechar a aba nao avisa, so quando a gravacao falha. Spec com o resultado, CONTEXT, IDEAS (i-040, i-043, i-045 a i-047), ROADMAP, README, STATUS inteiro."
```

```
git push
```
