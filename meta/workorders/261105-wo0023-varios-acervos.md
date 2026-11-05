# WO 0023 — Varios acervos no navegador (curadoria, entrega 2) e versao 0.12.0

## Cabecalho

> **Tipo:** mista — CODIGO (`app/index.html`) e registro (CHANGELOG, README, IDEAS, ROADMAP, STATUS inteiro).
> **Config sugerida:** Sonnet · `/effort medium`. 18 edicoes literais e o STATUS inteiro, aplicados e testados pelo chat num clone de `d9b3030`; cada arquivo tem hash de chegada.
> **Pre-requisito:** commit `d9b3030`, branch `main`, sincronizada com `origin/main`. O `git status` mostra **so** o que o chat gravou: `M logs/2026-11-04.md`, `M meta/CEREBRO.md`, `M meta/CONTEXT.md`, `M meta/specs/261104-varios-acervos.md`, `?? logs/2026-11-05.md` e esta WO (`?? meta/workorders/...wo0023...`).
> **Base:** spec `meta/specs/261104-varios-acervos.md` (dentro da DEC-028, decidida pelo dono em 2026-11-02); sonda de armazenamento do dono (2026-11-04).
> **Depende de:** WO 0022, ja aplicada (`d3ad6f0`, wrap `395dceb`).
>
> **Arquivos — partida e chegada, os dois medidos pelo chat** (em LF; chegada = aplicar literalmente as edicoes abaixo):
>
> | arquivo | partida (sha1) | chegada (sha1) |
> |---|---|---|
> | `app/index.html` | `0cecb28694af6fb7022ed86a812793c1a49740e6` | `72c06fefaa27587d60b9f4dcaa9f515a639c2186` |
> | `README.md` | `22964e30a7e3d41910be8f85ed9189a6521d4261` | `e936e7e607fe4cd1e2c1be0e3675b0d7f46cfe41` |
> | `meta/CHANGELOG.md` | `5b6e87be4591189087c9eb07a5ba27db0c3d03ab` | `5bf60b933a6baccb0511c6d9361da4c6ce441de4` |
> | `meta/IDEAS.md` | `7f2c164da87b0465e534c3c032c2ce27f551e5aa` | `a57f21e95e7393d2938b76dc086e1bb6e61acfc2` |
> | `meta/ROADMAP.md` | `136a685a25a6e349909e77f3beb0e18863b8d5c4` | `2d2b1d4c935eab4db47f6dd93f9561dcc58c9180` |
> | `meta/STATUS.md` | `aec8d3665f1681d1a6d1d793777ef4c3c95e6ad4` | `be5655d2879e668a8459a6ee4f4f86c3f036aa84` |
> | `meta/specs/261104-varios-acervos.md` | `126720e4bd87cdb9f52fa2da68984970c0943bc4` | `126720e4bd87cdb9f52fa2da68984970c0943bc4` (gravado pelo chat; só versiona) |
> | `meta/CONTEXT.md` | `6533732c97377de8b545ec9aee3760969789f8d0` | `6533732c97377de8b545ec9aee3760969789f8d0` (gravado pelo chat; só versiona) |
> | `meta/CEREBRO.md` | `2fbaea98043cc68f64fef1ff885319d038bf522c` | `2fbaea98043cc68f64fef1ff885319d038bf522c` (gravado pelo chat; só versiona) |
> | `logs/2026-11-04.md` | `09bcce26646730ed3e5aa4698cd0a290606c997f` | `09bcce26646730ed3e5aa4698cd0a290606c997f` (gravado pelo chat; só versiona) |
> | `logs/2026-11-05.md` | `ca408fe7dbc74ebcfe722920197905525131c5af` | `ca408fe7dbc74ebcfe722920197905525131c5af` (gravado pelo chat; só versiona) |
>
> **Ancora semantica:** se um trecho-ancora nao bater EXATAMENTE, PARE e reporte.
> **Idempotencia:** antes de cada edicao, procure o texto NOVO INTEIRO; se ja estiver la, PULE e diga no relatorio. Arquivo inteiro (E19): se o hash ja for o de chegada, PULE.
> **Ancoras lidas em:** cada ancora foi recortada pelo chat do arquivo de partida (`git show d9b3030:<arquivo>`, igual ao disco do dono pelos hashes da coluna partida, medidos no disco em 2026-11-05) e conferida como ocorrendo **exatamente 1 vez** no estado em que a edicao e aplicada, na ordem abaixo. Ancora sempre de linha inteira. A E09 e um bloco de varias dezenas de linhas (o trecho «Acervo guardado no navegador» inteiro, do comentario de abertura ate o fim de `boot()`): substitua o bloco todo.
> **Canal dos meta neste ciclo = CODE:** esta WO e o registro. A spec, o CONTEXT, o CEREBRO e os dois logs ja estao gravados pelo chat (DEC-010); a WO so os versiona.

---

## 1. Por que

Entrega 2 da curadoria (i-041, DEC-028), pela spec:

- Cada `.json` importado fica no IndexedDB (banco `cancioneiro`), pelo nome do arquivo; reimportar substitui.
- O botao «acervos (N)», na linha de origem, abre a janela para abrir outro ou esquecer um; o app reabre no ultimo aberto.
- Marcas «usei» por acervo (`App.ui.usedBy[<arquivo>]`), com migracao das antigas para todo acervo que tem o id.
- A copia antiga (`cancioneiro:acervo`) migra, e so e apagada depois de lida de volta e comparada. Sem IndexedDB, o app segue como na 0.11.0.
- De passagem, uma guarda: importar um `.json` sem `albums` nao guarda mais a copia (antes guardava, e o toast de erro era coberto).

O app de chegada foi executado pelo chat no Chromium headless (`file://` e `http://` local): **25 de 25** conferencias dos 16 criterios da spec, com acervos sinteticos de 960 mil, 430 mil e 22 mil caracteres; o teste da entrega 1 segue em **15 de 15**; prova de vida no app de partida (reprova). `validate.py` exit=0 (com `jsonschema`, `Tudo conforme ao esquema.`), `test_convert_br.py` e `test_convert_guides.py` OK.

**Versao 0.12.0 nesta WO.** A conferencia de tela e do dono, depois do push. **Achado fora do escopo** (nao conserte aqui): a barra de controles nao some sem acervo, porque `.controls { display: flex }` vence o `hidden` — virou a i-044.

## Edicao 0 — Conferencia de hash e de arvore

```
sha1sum app/index.html README.md meta/CHANGELOG.md meta/IDEAS.md meta/ROADMAP.md meta/STATUS.md meta/specs/261104-varios-acervos.md meta/CONTEXT.md meta/CEREBRO.md logs/2026-11-04.md logs/2026-11-05.md
GIT_OPTIONAL_LOCKS=0 git status --short
```

Os onze batem com a coluna **partida** (o `logs/2026-11-05.md` ja existe, gravado pelo chat: a partida dele e a chegada); o `git status` mostra exatamente as seis linhas do Pre-requisito. Qualquer outra coisa: **PARE e reporte**.

## Edicoes E01 a E19

Na ordem. **Todas as secoes de edicao tem o mesmo titulo, `### Exx — ...`**, inclusive a de arquivo inteiro.
Copie o que esta ENTRE as linhas de quatro crases, sem elas. **O bloco termina na linha de quatro crases, nunca
num titulo:** o CHANGELOG, a IDEAS e o STATUS trazem `## ` e `### ` dentro do bloco.

### E01 — app: comentario de topo — `app/index.html`

**Ancora, literal:**

````
  Fonte de verdade = o arquivo JSON (DEC-004). O localStorage guarda SO estado
  efemero (marcacoes "usei", filtros). Se o localStorage falhar, a ferramenta
  continua 100% funcional, so nao lembra as marcas entre sessoes.
````

**Texto novo, literal:**

````
  Fonte de verdade = o arquivo JSON (DEC-004). O navegador guarda copias:
  os acervos importados no IndexedDB (banco "cancioneiro", DEC-028) e, no
  localStorage, as marcas "usei" por acervo e a estrutura do cartao. Se o
  navegador recusar, a ferramenta continua funcional, so nao lembra.
````

### E02 — app: marcas por acervo — `app/index.html`

**Ancora, literal:**

````
/** Marca de "usei" por id de cancao. */
function isUsed(id) { return !!(App.ui.used && App.ui.used[id]); }
function toggleUsed(id) {
  App.ui.used = App.ui.used || {};
  if (App.ui.used[id]) delete App.ui.used[id]; else App.ui.used[id] = true;
  saveUiState();
}
````

**Texto novo, literal:**

````
/** Marca de "usei" por acervo e id de cancao: App.ui.usedBy[<arquivo>][<id>]
    (DEC-028). Ate a 0.11.0 era so por id, e o mesmo id em dois acervos
    (brv-04, cinzeiro-01) marcava nos dois; a migracao esta em migrateMarks. */
function isUsed(id) {
  const m = App.ui.usedBy && App.ui.usedBy[App.source];
  return !!(m && m[id]);
}
function toggleUsed(id) {
  const by = App.ui.usedBy = App.ui.usedBy || {};
  const m = by[App.source] = by[App.source] || {};
  if (m[id]) delete m[id]; else m[id] = true;
  if (!Object.keys(m).length) delete by[App.source];
  saveUiState();
}
````

### E03 — app: o demo do Pages tem nome de acervo — `app/index.html`

**Ancora, literal:**

````
      const json = await res.json();
      setCollection(json);
      setOrigin("carregado de " + path.replace(/^\.\.\//, "") + " (GitHub Pages)", false);
````

**Texto novo, literal:**

````
      const json = await res.json();
      App.source = DEMO_SOURCE;   // as marcas do demo, o mesmo de quem importa demo.json
      setCollection(json);
      setOrigin("carregado de " + path.replace(/^\.\.\//, "") + " (GitHub Pages)", false);
````

### E04 — app: importar (1), leitura assincrona — `app/index.html`

**Ancora, literal:**

````
  reader.onload = () => {
````

**Texto novo, literal:**

````
  reader.onload = async () => {
````

### E05 — app: importar (2), guarda no IndexedDB — `app/index.html`

**Ancora, literal:**

````
    const removidas = stripInternalKeys(json);
    try {
      setCollection(json);
      const guardado = saveCollectionCache(json, file.name);
      toast("Acervo importado: " + (json.title || file.name)
            + (extracted ? " · JSON extraído de um bloco de código" : "")
            + (removidas ? " · " + removidas + " campo(s) interno(s) removido(s) — baixe de novo para gravar limpo" : "")
            + moduleRefsNotice(json)
            + (guardado ? "" : " · não coube no navegador: ao fechar, ele não volta"));
````

**Texto novo, literal:**

````
    const removidas = stripInternalKeys(json);
    // A abertura (boot) precisa ter terminado: senao ela poderia abrir o acervo
    // guardado por cima deste, ou o banco ainda nao estaria pronto.
    await bootDone;
    try {
      const before = App.source;
      App.source = file.name;   // antes do render: as marcas sao deste acervo
      setCollection(json);
      // setCollection recusou (sem `albums`): nao guarda o que nao e acervo.
      if (App.collection !== json) { App.source = before; return; }
      App.ui.open = file.name;
      saveUiState();
      const r = await saveAcervo(json, file.name);
      if (r.ok) savedOrigin(file.name, r.savedAt);
      else setOrigin("importado de " + file.name + " · não guardado no navegador", false);
      toast("Acervo importado: " + (json.title || file.name)
            + (extracted ? " · JSON extraído de um bloco de código" : "")
            + (removidas ? " · " + removidas + " campo(s) interno(s) removido(s) — baixe de novo para gravar limpo" : "")
            + moduleRefsNotice(json)
            + (r.replaced ? " · substituiu a cópia de " + fmtDate(r.replaced) : "")
            + (r.ok ? "" : " · não coube no navegador: ao fechar, ele não volta")
            + noDbNotice());
````

### E06 — app: versao — `app/index.html`

**Ancora, literal:**

````
    <span class="version" data-role="app-version">v0.11.0</span>
````

**Texto novo, literal:**

````
    <span class="version" data-role="app-version">v0.12.0</span>
````

### E07 — app: estilo da janela de acervos — `app/index.html`

**Ancora, literal:**

````
  .origin button { font-size: 12px; padding: 3px 8px; }
````

**Texto novo, literal:**

````
  .origin button { font-size: 12px; padding: 3px 8px; }
  /* Janela «acervos» (DEC-028): um acervo guardado por linha. */
  .acervos-list { list-style: none; padding: 0; margin: 8px 0 0; display: flex; flex-direction: column; gap: 6px; }
  .acervos-list li { display: flex; gap: 10px; align-items: center; padding: 8px 10px;
    background: var(--paper-2); border-radius: 6px; font-size: 13px; }
  .acervos-list .acervo-info { display: flex; flex-direction: column; gap: 2px; min-width: 0; }
  .acervos-list .acervo-meta { font-size: 12px; color: var(--ink-soft); overflow-wrap: anywhere; }
  .acervos-list .acervo-actions { margin-left: auto; display: flex; gap: 6px; align-items: center; flex-shrink: 0; }
  .acervos-list .acervo-open { font-size: 12px; color: var(--ink-soft); font-style: italic; }
````

### E08 — app: a janela de acervos — `app/index.html`

**Ancora, literal:**

````
<div class="drop-hint" aria-hidden="true">Solte o .json para importar</div>
````

**Texto novo, literal:**

````
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

<div class="drop-hint" aria-hidden="true">Solte o .json para importar</div>
````

### E09 — app: o bloco do acervo guardado vira o de varios acervos — `app/index.html`

**Ancora, literal:**

````
/* ===================================================================
   Acervo guardado no navegador (i-035, DEC-022)
   Cache, nao fonte: guarda a copia do ULTIMO arquivo importado, que o app nunca
   edita (FIX-004) — por isso a copia e igual ao arquivo. O risco e o arquivo
   mudar fora e a copia ficar velha sem ninguem ver: a linha de origem diz de
   onde veio e quando, e «esquecer» apaga a copia.
   =================================================================== */
const CACHE_KEY = "cancioneiro:acervo";

/** Guarda a colecao; devolve false se o navegador recusar (cota, modo privado). */
function saveCollectionCache(json, source) {
  try {
    const savedAt = new Date().toISOString();
    localStorage.setItem(CACHE_KEY, JSON.stringify({ savedAt, source, json }));
    setOrigin("importado de " + source + " em " + fmtDate(savedAt) + " · guardado neste navegador", true);
    return true;
  } catch (e) {
    setOrigin("importado de " + source + " · não guardado no navegador", false);
    return false;
  }
}
function loadCollectionCache() {
  try {
    const c = JSON.parse(localStorage.getItem(CACHE_KEY) || "null");
    return c && c.json && Array.isArray(c.json.albums) ? c : null;
  } catch (e) { return null; }
}
function fmtDate(iso) {
  const d = new Date(iso);
  return isNaN(d) ? "?" : d.toLocaleString("pt-BR", { dateStyle: "short", timeStyle: "short" });
}

/** A linha de origem na barra de controles; com `forgettable`, o botao «esquecer». */
function setOrigin(text, forgettable) {
  const el = document.getElementById("origin");
  el.textContent = "";
  const t = document.createElement("span"); t.textContent = "Acervo " + text; el.appendChild(t);
  if (forgettable) {
    const b = document.createElement("button"); b.type = "button"; b.textContent = "esquecer";
    b.title = "Apaga a cópia guardada neste navegador. O arquivo no seu computador não é tocado.";
    b.addEventListener("click", forgetCollection);
    el.appendChild(b);
  }
}

/** Apaga a copia e volta ao estado inicial (no Pages, o demo carrega de novo). */
function forgetCollection() {
  try { localStorage.removeItem(CACHE_KEY); } catch (e) { /* nada a apagar */ }
  App.collection = null; App.activeModules = {}; App.bpm = {}; App.modulesById = {};
  document.getElementById("main").innerHTML = EMPTY_HTML;
  document.getElementById("origin").textContent = "";
  document.getElementById("stats").textContent = "";
  render();
  toast("Cópia esquecida. O arquivo no seu computador não foi tocado.");
  tryAutoLoad();
}

/** Abertura: a copia guardada, se houver; senao, a carga automatica do Pages. */
function boot() {
  const c = loadCollectionCache();
  if (!c) { tryAutoLoad(); return; }
  stripInternalKeys(c.json);
  setCollection(c.json);
  setOrigin("importado de " + (c.source || "arquivo") + " em " + fmtDate(c.savedAt) + " · guardado neste navegador", true);
  toast("Acervo do navegador: " + (c.json.title || c.source) + " · importado em " + fmtDate(c.savedAt)
        + moduleRefsNotice(c.json));
}
````

**Texto novo, literal:**

````
/* ===================================================================
   Acervos guardados no navegador (i-041, DEC-028 — spec
   meta/specs/261104-varios-acervos.md; antes, DEC-022: so o ultimo)
   Cache, nao fonte (DEC-004): o arquivo importado e a verdade. Cada acervo
   importado fica no IndexedDB (banco "cancioneiro", deposito "acervos"),
   com o NOME DO ARQUIVO como chave: reimportar o mesmo arquivo substitui.
   No file:// todas as paginas locais sao a MESMA origem (sonda de 2026-11-04:
   9 das 11 chaves do localStorage eram de outros projetos) — por isso o banco
   tem nome proprio e o app nunca le nem apaga chave sem o prefixo
   "cancioneiro:". Sem IndexedDB, o app volta ao modo da 0.11.0: um acervo
   so, no localStorage (CACHE_KEY).
   =================================================================== */
const CACHE_KEY = "cancioneiro:acervo";   // formato da 0.9.0 a 0.11.0, e o modo sem IndexedDB
const DB_NAME = "cancioneiro", DB_STORE = "acervos";
const DEMO_SOURCE = "demo.json";           // chave das marcas do acervo que o Pages carrega sozinho
// db: o banco, ou null = sem IndexedDB (modo da 0.11.0). count: quantos guardados.
const Store = { db: null, count: 0, noDbNoticeShown: false };
App.source = null;                         // o nome do arquivo do acervo aberto

/** Abre o banco; resolve com ele, ou com null se o navegador recusar. */
function openDb() {
  return new Promise(resolve => {
    let req;
    try { req = indexedDB.open(DB_NAME, 1); } catch (e) { resolve(null); return; }
    req.onupgradeneeded = () => req.result.createObjectStore(DB_STORE, { keyPath: "source" });
    req.onsuccess = () => resolve(req.result);
    req.onerror = () => resolve(null);
    req.onblocked = () => resolve(null);
  });
}
/** Uma operacao no deposito, como Promise; `fn(store)` devolve o request.
    Resolve so no `complete` da transacao: so entao o dado esta gravado. */
function dbDo(mode, fn) {
  return new Promise((resolve, reject) => {
    let tx, req;
    try {
      tx = Store.db.transaction(DB_STORE, mode);
      req = fn(tx.objectStore(DB_STORE));
    } catch (e) { reject(e); return; }
    tx.oncomplete = () => resolve(req && req.result);
    tx.onerror = () => reject(tx.error || new Error("IndexedDB"));
    tx.onabort = () => reject(tx.error || new Error("IndexedDB: transação abortada"));
  });
}
const dbGet = source => dbDo("readonly", s => s.get(source));
const dbPut = rec => dbDo("readwrite", s => s.put(rec));
const dbDelete = source => dbDo("readwrite", s => s.delete(source));
const dbAll = () => dbDo("readonly", s => s.getAll());
async function refreshCount() {
  try { Store.count = Store.db ? await dbDo("readonly", s => s.count()) : 0; } catch (e) { /* fica o anterior */ }
}
const newest = recs => recs.slice().sort((a, b) => String(b.savedAt).localeCompare(String(a.savedAt)))[0];

/** O aviso do modo sem IndexedDB, uma vez por sessao (vai colado ao proximo toast). */
function noDbNotice() {
  if (Store.db || Store.noDbNoticeShown) return "";
  Store.noDbNoticeShown = true;
  return " · este navegador não deixou guardar vários acervos; guardo só o último";
}

/** Guarda o acervo importado. Devolve {ok, savedAt, replaced}: `replaced` e a
    data da copia de mesmo nome que foi substituida, ou null. */
async function saveAcervo(json, source) {
  const savedAt = new Date().toISOString();
  if (!Store.db) {
    try { localStorage.setItem(CACHE_KEY, JSON.stringify({ savedAt, source, json })); }
    catch (e) { return { ok: false, savedAt, replaced: null }; }
    return { ok: true, savedAt, replaced: null };
  }
  let prev = null;
  try { prev = await dbGet(source); } catch (e) { /* sem a anterior, segue */ }
  try { await dbPut({ source, title: json.title || source, savedAt, json }); }
  catch (e) { return { ok: false, savedAt, replaced: null }; }
  await refreshCount();
  requestPersistOnce();
  return { ok: true, savedAt, replaced: prev ? prev.savedAt : null };
}

/** Pede ao navegador, uma vez, para nao descartar os acervos sob pressao de disco.
    O resultado aparece na janela de acervos, nao no toast. */
function requestPersistOnce() {
  if (App.ui.persistAsked || !navigator.storage || !navigator.storage.persist) return;
  App.ui.persistAsked = true;
  saveUiState();
  navigator.storage.persist().catch(() => { /* a janela mostra o estado real */ });
}

/** Le a copia do formato antigo (0.9.0 a 0.11.0) ou do modo sem IndexedDB. */
function loadCollectionCache() {
  try {
    const c = JSON.parse(localStorage.getItem(CACHE_KEY) || "null");
    return c && c.json && Array.isArray(c.json.albums) ? c : null;
  } catch (e) { return null; }
}
function fmtDate(iso) {
  const d = new Date(iso);
  return isNaN(d) ? "?" : d.toLocaleString("pt-BR", { dateStyle: "short", timeStyle: "short" });
}

/** A linha de origem na barra de controles. Com `forgettable`, o «esquecer» do
    acervo aberto; com acervos guardados, o «acervos (N)» entre os dois. */
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
const savedOrigin = (source, savedAt) =>
  setOrigin("importado de " + source + " em " + fmtDate(savedAt) + " · guardado neste navegador", true);

/** Abre um acervo guardado. Zera modulos ligados e BPM da sessao (setCollection,
    FIX-008) e grava qual esta aberto. */
function openRecord(rec) {
  stripInternalKeys(rec.json);
  const before = App.source;
  App.source = rec.source;
  setCollection(rec.json);
  if (App.collection !== rec.json) { App.source = before; return false; }
  App.ui.open = rec.source;
  saveUiState();
  savedOrigin(rec.source, rec.savedAt);
  return true;
}

/** Copia as marcas do formato antigo (`used`, so por id) para `usedBy`: cada marca
    vai para todo acervo guardado que tem uma faixa com aquele id — nos ids que
    colidem (brv-04, cinzeiro-01) vai para os dois, que e o que a tela mostrava.
    Id que nao existe em nenhum vai para o demo do Pages. Depois, `used` sai. */
function migrateMarks(records) {
  const old = App.ui.used;
  if (!old) return;
  const by = App.ui.usedBy = App.ui.usedBy || {};
  const idsOf = recs => recs.map(r => ({ source: r.source,
    ids: new Set((r.json.albums || []).flatMap(a => (a.songs || []).map(s => s.id))) }));
  const index = idsOf(records);
  Object.keys(old).forEach(id => {
    const hits = index.filter(x => x.ids.has(id));
    (hits.length ? hits.map(x => x.source) : [DEMO_SOURCE])
      .forEach(src => { (by[src] = by[src] || {})[id] = true; });
  });
  delete App.ui.used;
  saveUiState();
}

/** Migra a copia do formato antigo para o IndexedDB: grava, le de volta e compara;
    SO entao apaga a chave antiga. Se algo falhar, a chave fica e o app segue no
    modo sem IndexedDB nesta sessao (devolve false). */
async function migrateLegacy(legacy) {
  const rec = { source: legacy.source || "acervo.json", title: legacy.json.title || legacy.source,
                savedAt: legacy.savedAt, json: legacy.json };
  try {
    await dbPut(rec);
    const back = await dbGet(rec.source);
    if (!back || JSON.stringify(back.json) !== JSON.stringify(legacy.json)) throw new Error("leitura diferente");
  } catch (e) {
    console.warn("[cancioneiro] migracao para o IndexedDB falhou; segue a copia antiga:", e);
    return false;
  }
  try { localStorage.removeItem(CACHE_KEY); } catch (e) { /* fica; a proxima abertura tenta de novo */ }
  if (!App.ui.open) { App.ui.open = rec.source; saveUiState(); }
  return true;
}

/** Abertura: migra o formato antigo, abre o ultimo acervo aberto (ou o importado
    mais recente) e, sem nenhum guardado, faz a carga automatica do Pages. */
async function boot() {
  Store.db = ("indexedDB" in window && window.indexedDB) ? await openDb() : null;
  const legacy = loadCollectionCache();
  if (Store.db && legacy && !(await migrateLegacy(legacy))) Store.db = null;
  let records = [];
  if (Store.db) {
    try { records = await dbAll(); } catch (e) { Store.db = null; }
  }
  if (!Store.db) {
    const c = loadCollectionCache();
    records = c ? [{ source: c.source || "acervo.json", title: c.json.title, savedAt: c.savedAt, json: c.json }] : [];
  }
  Store.count = Store.db ? records.length : 0;
  migrateMarks(records);
  const pick = records.find(r => r.source === App.ui.open) || newest(records);
  if (!pick) { tryAutoLoad(); return; }
  openRecord(pick);
  toast("Acervo do navegador: " + (pick.json.title || pick.source) + " · importado em " + fmtDate(pick.savedAt)
        + moduleRefsNotice(pick.json) + noDbNotice());
}

/** Esquece um acervo: so ele sai do navegador. As marcas «usei» dele ficam, e
    reimportar o arquivo as traz de volta. Se era o aberto, abre o importado mais
    recente que sobrou; sem nenhum, volta ao estado inicial (no Pages, o demo). */
async function forgetAcervo(source) {
  if (!source) return;
  if (Store.db) {
    try { await dbDelete(source); } catch (e) { toast("Não consegui esquecer: " + e.message); return; }
    await refreshCount();
  } else {
    try { localStorage.removeItem(CACHE_KEY); } catch (e) { /* nada a apagar */ }
  }
  const msg = "Cópia de " + source + " esquecida. As marcas «usei» dela ficam: reimportar o arquivo as traz de volta."
    + " O arquivo no seu computador não foi tocado.";
  if (source !== App.source) { refreshOrigin(); toast(msg); return; }
  let rest = [];
  if (Store.db) { try { rest = await dbAll(); } catch (e) { rest = []; } }
  if (rest.length) { openRecord(newest(rest)); toast(msg); return; }
  App.collection = null; App.activeModules = {}; App.bpm = {}; App.modulesById = {}; App.source = null;
  delete App.ui.open; saveUiState();
  document.getElementById("main").innerHTML = EMPTY_HTML;
  document.getElementById("origin").textContent = "";
  document.getElementById("stats").textContent = "";
  render();
  toast(msg);
  tryAutoLoad();
}

/** Redesenha a linha de origem do acervo aberto (depois de mudar a contagem). */
async function refreshOrigin() {
  if (!App.source || !Store.db) return;
  let rec = null;
  try { rec = await dbGet(App.source); } catch (e) { /* sem registro */ }
  if (rec) savedOrigin(rec.source, rec.savedAt);
  else setOrigin("importado de " + App.source + " · não guardado no navegador", false);
}

/** A janela «acervos»: um por linha, do importado mais recente ao mais antigo. */
async function renderAcervosDialog() {
  const list = document.getElementById("acervos-list");
  let recs = [];
  try { recs = await dbAll(); } catch (e) { recs = []; }
  recs.sort((a, b) => String(b.savedAt).localeCompare(String(a.savedAt)));
  list.textContent = "";
  const plural = (n, um, varios) => n + " " + (n === 1 ? um : varios);
  recs.forEach(r => {
    const albums = (r.json.albums || []);
    const songs = albums.reduce((n, a) => n + (a.songs || []).length, 0);
    const li = document.createElement("li");
    li.dataset.source = r.source;
    const info = document.createElement("div"); info.className = "acervo-info";
    const t = document.createElement("strong"); t.textContent = r.title || r.source;
    const m = document.createElement("span"); m.className = "acervo-meta";
    m.textContent = r.source + " · importado em " + fmtDate(r.savedAt) + " · "
      + plural(albums.length, "álbum", "álbuns") + ", " + plural(songs, "faixa", "faixas");
    info.appendChild(t); info.appendChild(m); li.appendChild(info);
    const act = document.createElement("div"); act.className = "acervo-actions";
    if (r.source === App.source) {
      const s = document.createElement("span"); s.className = "acervo-open"; s.textContent = "aberto";
      act.appendChild(s);
    } else {
      const o = document.createElement("button"); o.type = "button"; o.textContent = "abrir";
      o.addEventListener("click", async () => {
        let rec = null;
        try { rec = await dbGet(r.source); } catch (e) { /* trata abaixo */ }
        if (!rec || !openRecord(rec)) { toast("Não consegui abrir " + r.source); return; }
        document.getElementById("acervos-dialog").close();
        toast("Acervo aberto: " + (rec.json.title || rec.source) + moduleRefsNotice(rec.json));
      });
      act.appendChild(o);
    }
    const f = document.createElement("button"); f.type = "button"; f.textContent = "esquecer";
    f.addEventListener("click", async () => { await forgetAcervo(r.source); renderAcervosDialog(); });
    act.appendChild(f);
    li.appendChild(act);
    list.appendChild(li);
  });
  if (!recs.length) {
    const li = document.createElement("li"); li.textContent = "Nenhum acervo guardado."; list.appendChild(li);
  }
  let persisted = null;
  try { persisted = navigator.storage && navigator.storage.persisted ? await navigator.storage.persisted() : null; }
  catch (e) { persisted = null; }
  document.getElementById("acervos-persist").textContent = persisted === null
    ? "Guardado de forma persistente: não sei (o navegador não diz)."
    : persisted ? "Guardado de forma persistente: sim."
    : "Guardado de forma persistente: não — sem espaço em disco, o navegador pode apagar estas cópias. O arquivo continua sendo a fonte.";
}
async function openAcervosDialog() {
  await renderAcervosDialog();
  document.getElementById("acervos-dialog").showModal();
}
````

### E10 — app: o fechar da janela e a abertura assincrona — `app/index.html`

**Ancora, literal:**

````
boot();
````

**Texto novo, literal:**

````
document.getElementById("acervos-close-btn").addEventListener("click", () =>
  document.getElementById("acervos-dialog").close());

// A abertura e assincrona (IndexedDB); a importacao espera por ela.
const bootDone = boot();
````

### E11 — CHANGELOG: 0.12.0 — `meta/CHANGELOG.md`

**Ancora, literal:**

````
## [0.11.0] — 2026-11-02
````

**Texto novo, literal:**

````
## [0.12.0] — 2026-11-05

Segunda das três entregas da curadoria no app (i-041, DEC-028): vários acervos guardados no navegador.

### Added
- **Vários acervos no navegador:** cada `.json` importado fica guardado no IndexedDB (banco `cancioneiro`), pelo nome do arquivo; reimportar o mesmo arquivo substitui a cópia, e o toast diz de quando era a anterior. O botão «acervos (N)», na linha de origem, abre a janela com os guardados — título, arquivo, data, álbuns e faixas — para abrir outro sem seletor de arquivo ou esquecer um. O app reabre no último acervo aberto. Na primeira gravação, pede ao navegador para guardar de forma persistente; a janela mostra o resultado.

### Changed
- **Marcas «usei» por acervo.** Até a 0.11.0 eram só por id, e o mesmo id em dois acervos (`brv-04` na Rainha e no demo, `cinzeiro-01` no demo e no exemplo) marcava nos dois. A migração copia cada marca antiga para todo acervo guardado que tem aquele id, então nada some da tela.
- **Migração da cópia antiga** (`cancioneiro:acervo`, da 0.9.0 à 0.11.0): é gravada no IndexedDB, lida de volta e comparada, e só então apagada. Se falhar, ela fica, e o app segue como na 0.11.0. Sem IndexedDB, o app guarda só o último, como antes, e avisa uma vez.
- **Esquecer** apaga só aquele acervo; as marcas dele ficam, e reimportar o arquivo as traz de volta.
- **Importar um `.json` que não é acervo** (sem `albums`) não guarda mais a cópia. Antes, o toast de erro era coberto por «Acervo importado».

Spec `meta/specs/261104-varios-acervos.md`: 25 de 25 conferências dos 16 critérios no Chromium headless, com acervos sintéticos do tamanho dos reais (960 mil, 430 mil e 22 mil caracteres) e prova de vida no app da 0.11.0; o teste da entrega 1 continua em 15 de 15.

---

## [0.11.0] — 2026-11-02
````

### E12 — README: versao — `README.md`

**Ancora, literal:**

````
> **Estado:** v0.11.0 — ferramenta em uso. Lê o acervo, copia por campo, troca módulos de estilo, ajusta o BPM, **mede cada prompt contra os limites do Suno**, exporta Markdown, exporta uma faixa como `.json` e **entrega o prompt para chats gerarem canções no esquema**. Publicada no GitHub Pages. Ver `meta/ROADMAP.md`.
````

**Texto novo, literal:**

````
> **Estado:** v0.12.0 — ferramenta em uso. Lê e guarda vários acervos, copia por campo, troca módulos de estilo, ajusta o BPM, **mede cada prompt contra os limites do Suno**, exporta Markdown, exporta uma faixa como `.json` e **entrega o prompt para chats gerarem canções no esquema**. Publicada no GitHub Pages. Ver `meta/ROADMAP.md`.
````

### E13 — README: varios acervos — `README.md`

**Ancora, literal:**

````
   **Ou local:** duplo-clique em `app/index.html` (modo `file://`) e clique em *Importar .json* — ou arraste o arquivo para a tela. O último acervo importado fica guardado no navegador e volta quando você reabre.
````

**Texto novo, literal:**

````
   **Ou local:** duplo-clique em `app/index.html` (modo `file://`) e clique em *Importar .json* — ou arraste o arquivo para a tela. Cada acervo importado fica guardado no navegador, pelo nome do arquivo: o app reabre no último que você usou, e *acervos (N)*, na linha de origem, troca de um para outro sem procurar o arquivo.
````

### E14 — README: fonte de verdade — `README.md`

**Ancora, literal:**

````
O acervo canônico são **arquivos JSON** no esquema: os exemplos versionados em `data/`, e o acervo pessoal fora do repo (DEC-026). O navegador (localStorage) guarda as marcações, a estrutura do cartão e uma **cópia do último acervo importado** — cache, nunca a fonte: a linha de origem diz de onde ela veio e quando, e *esquecer* a apaga. Ver `meta/DECISIONS.md` (DEC-004, DEC-022).
````

**Texto novo, literal:**

````
O acervo canônico são **arquivos JSON** no esquema: os exemplos versionados em `data/`, e o acervo pessoal fora do repo (DEC-026). O navegador guarda **cópias dos acervos importados** (IndexedDB) e, no localStorage, as marcações por acervo e a estrutura do cartão — cache, nunca a fonte: a linha de origem diz de onde a cópia veio e quando, e *esquecer* a apaga sem tocar no arquivo. Ver `meta/DECISIONS.md` (DEC-004, DEC-022, DEC-028).
````

### E15 — IDEAS: i-041 entregue (1) — `meta/IDEAS.md`

**Ancora, literal:**

````
### i-041 💡 Mais de um acervo guardado no navegador
````

**Texto novo, literal:**

````
### i-041 ✅ Mais de um acervo guardado no navegador
````

### E16 — IDEAS: i-041 entregue (2) — `meta/IDEAS.md`

**Ancora, literal:**

````
**Decidida (2026-11-02, DEC-028):** IndexedDB, um acervo por nome de arquivo, marcas «usei» por acervo (hoje colidem: `brv-04`, `cinzeiro-01`). É a entrega 2 da curadoria; a sonda `../261102-sonda-armazenamento.html` mede o navegador do dono antes da spec.
````

**Texto novo, literal:**

````
**Decidida (2026-11-02, DEC-028):** IndexedDB, um acervo por nome de arquivo, marcas «usei» por acervo (hoje colidem: `brv-04`, `cinzeiro-01`). É a entrega 2 da curadoria; a sonda `../261102-sonda-armazenamento.html` mede o navegador do dono antes da spec.
**Entregue (0.12.0, 2026-11-05):** spec `meta/specs/261104-varios-acervos.md`, WO 0023. A sonda (Chrome 156, `file://`) mostrou o IndexedDB funcionando e a origem `file://` compartilhada com outras páginas locais. Janela «acervos (N)», reabre no último aberto, marcas por acervo com migração, ramo sem IndexedDB.
````

### E17 — IDEAS: i-043 com a API medida, e i-044 nova — `meta/IDEAS.md`

**Ancora, literal:**

````
Achado na análise da curadoria (2026-11-02, opção F4): no Chrome e no Edge o app pode abrir o `.json` com permissão de gravar e «Salvar» no mesmo arquivo, sem passar por Downloads. Não existe no Firefox nem no Safari, e a permissão é pedida de novo a cada sessão. **Gatilho:** depois da entrega 3 da curadoria (DEC-028), se a sonda mostrar a API no navegador do dono — entra como «Salvar no arquivo» onde existir, com «Baixar» onde não.
````

**Texto novo, literal:**

````
Achado na análise da curadoria (2026-11-02, opção F4): no Chrome e no Edge o app pode abrir o `.json` com permissão de gravar e «Salvar» no mesmo arquivo, sem passar por Downloads. Não existe no Firefox nem no Safari, e a permissão é pedida de novo a cada sessão. **Gatilho:** depois da entrega 3 da curadoria (DEC-028), se a sonda mostrar a API no navegador do dono — entra como «Salvar no arquivo» onde existir, com «Baixar» onde não.
**Medido (2026-11-04, sonda):** no Chrome 156 do dono existem as três APIs — `showSaveFilePicker`, `showOpenFilePicker` e `getAsFileSystemHandle` (arrastar com permissão de gravar). Falta só a entrega 3.

### i-044 💡 A barra de controles não some quando não há acervo
Achado no teste da entrega 2 (2026-11-05): o CSS `.controls { display: flex }` vence o atributo `hidden` que o `render()` põe na barra quando não há acervo, então os filtros vazios ficam na tela no estado inicial e depois de esquecer todos. Já era assim antes da 0.12.0. O conserto provável é uma linha (`.controls[hidden] { display: none; }`), mas muda o que o dono vê ao abrir o app vazio — conferir na tela antes.
````

### E18 — ROADMAP: entrega 2 — `meta/ROADMAP.md`

**Ancora, literal:**

````
- 🔨 Curadoria no app e vários acervos (i-040, i-041, DEC-028), em três entregas: ✅ exportar faixa como `.json` (0.11.0) · ⬜ vários acervos no navegador (IndexedDB, marcas «usei» por acervo) · ⬜ curadoria pela tela (excluir, reordenar, mover, novo álbum, importar faixas) num rascunho marcado.
````

**Texto novo, literal:**

````
- 🔨 Curadoria no app e vários acervos (i-040, i-041, DEC-028), em três entregas: ✅ exportar faixa como `.json` (0.11.0) · ✅ vários acervos no navegador (IndexedDB, marcas «usei» por acervo; 0.12.0) · ⬜ curadoria pela tela (excluir, reordenar, mover, novo álbum, importar faixas) num rascunho marcado.
````

### E19 — STATUS inteiro — `meta/STATUS.md`

**Arquivo inteiro, literal** (substitui o arquivo; chegada `be5655d2879e668a8459a6ee4f4f86c3f036aa84`):

````
# STATUS.md — Cancioneiro

> **O agora.** O que funciona, o que está em progresso, o que está quebrado, backlog curto.
> Rolante: item resolvido sai daqui e vai para o CHANGELOG. Médio/longo prazo vive no ROADMAP.

**Versão atual:** 0.12.0 · **Fase:** 3a, 3a.2, o BPM da 3b, o prompt-modelo e as conveniências de uso concluídos e conferidos · os álbuns antigos convertidos (i-008, fora do repo) · curadoria no app em curso, entrega 2 de 3 (DEC-028) · kit de música lido pelo KCM, à espera da resposta (i-039)

---

## Última conversa (2026-11-04 e 2026-11-05, curadoria no app: entrega 2, WO 0023)

- **Entrega 1 conferida na tela pelo dono** (2026-11-04, roteiro de 6 itens, tudo OK `[relatado pelo dono]`).
- **Sonda de armazenamento** (Chrome 156, `file://`): o IndexedDB grava e lê 1,5 milhão de caracteres; o `localStorage` tem 5.242.731 caracteres no total; a cota é de 10.737 MB; as APIs de gravar direto no arquivo existem. No `file://`, todas as páginas locais são a mesma origem: 9 das 11 chaves do `localStorage` são de outros projetos.
- **Entrega 2 (0.12.0):** vários acervos no IndexedDB, pelo nome do arquivo; janela «acervos (N)» na linha de origem; reabre no último aberto; marcas «usei» por acervo, com migração; a cópia antiga só sai depois de lida de volta. Spec `meta/specs/261104-varios-acervos.md`; 25 de 25 conferências no Chromium headless, testadas pelo chat.
- **Carta 02 ao KCM** (`../261105-cancioneiro-para-kcm-02-chaves-no-file.md`, com o dono): as chaves `kit-state-*`, `kit-niche` e `base_v4` no `localStorage` do `file://`, para o KCM conferir se são dele e se estão limpas.
- **Este bloco substitui o anterior, de 2026-11-02** (decisão da curadoria e entrega 1). O que ele dizia está no CHANGELOG [0.11.0], na DEC-028 e em `logs/2026-11-02.md` (Conversas 1 e 2).

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
- **Prompt-modelo** (`schema/PROMPT-PARA-CHATS.md`, DEC-021, DEC-023): contrato de módulo, style com 6 a 8 tags e até 10 com os módulos ligados; pede o JSON como arquivo e, sem arquivo, em bloco de código. Dois retestes em 2026-10-29: 6 de 6 faixas dentro do contrato e do orçamento, nos dois.
- **Botões «Prompt» e «Exemplo»** (0.8.0, DEC-021): buscam o prompt e o `data/demo.json` do repositório no clique; a janela do prompt recebe o «Meu pedido».
- **Conveniências (0.9.0, DEC-022, DEC-023):** «Estrutura» do cartão (ordem e blocos visíveis, no navegador); copiar o título; arrastar o `.json` para importar; o último acervo importado volta ao abrir, com origem, data e «esquecer»; a importação aceita a resposta do chat colada inteira e avisa.
- **Publicado no GitHub Pages** em `https://joaolucas-nds.github.io/cancioneiro/app/index.html` — o push em `main` publica.

## Em progresso

- **Curadoria no app** (i-040, DEC-028) — entregas 1 (0.11.0) e 2 (0.12.0) feitas. Próxima: a 3, excluir, reordenar, mover, novo álbum e importar faixas num rascunho marcado.
- **Kit de música no KCM (i-039)** — o KCM leu a carta 01 e responde por carta, sem data. Gatilho: sem resposta até o primeiro projeto de música novo, o projeto usa o kit à mão (`kit-musica/README.md`).

## Quebrado / pendências que travam

- (nada quebrado)

## Pendências do dono

- **Conferir a entrega 2 na tela** — roteiro na conversa de 2026-11-05, depois do push da WO 0023.
- **Levar a carta 02 ao KCM** — `../261105-cancioneiro-para-kcm-02-chaves-no-file.md`, para a pasta-pai do KCM.
- **Instalar o validador de esquema nesta máquina.** Sem `jsonschema` e `referencing`, o `validate.py` só confere sintaxe e diz `ESQUEMA NAO CONFERIDO` na última linha. Uma vez, no CMD: `pip install jsonschema referencing --break-system-packages`. Depois, `python3 scripts/validate.py` deve terminar em `Tudo conforme ao esquema.`

## Backlog curto (próximas ações concretas)

1. **Entrega 3 da curadoria: excluir, reordenar, mover, novo álbum, importar faixas** (i-040) — num rascunho marcado, com as regras de id e módulo repetidos da análise.
2. **A barra de controles não some sem acervo** (i-044) — defeito antigo de CSS, achado no teste da entrega 2; conferir na tela antes de consertar.
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
- **No `file://`, todas as páginas locais dividem o armazenamento** (sonda de 2026-11-04): o app só lê e grava o que tem o nome `cancioneiro`. O `file://` e o Pages são origens diferentes — o que está guardado num não aparece no outro.
- **Conversores são de primeira geração (DEC-028):** depois de mudar um acervo (à mão ou, com a entrega 3, no app), não rode o conversor por cima dele.
- **Botões «Prompt» e «Exemplo»:** dependem de rede e do Pages. No `file://`, só funcionam se o Pages aceitar o `fetch` de uma página local — não conferido (o dono abriu o `file://` em 2026-10-29, sem relatar o resultado do botão); sem isso, a janela mostra o link para a versão publicada (DEC-021).
- **Estado de sessão** (módulos ligados e BPM escolhido) sobrevive a filtro, busca e «marcar usei»; volta ao acervo ao recarregar a página ou importar de novo (FIX-008, DEC-020).
- **Limite conhecido:** `tryAutoLoad` (carregamento automático pelo Pages) não saneia chaves internas — só a importação por arquivo faz isso. Inócuo enquanto nenhum acervo contaminado for para `data/`.
- **Pendência de contexto — ASU:** o dono perguntou se o «modo ASU» do KCM seria melhor que o modo Code para este projeto; ficou pendente até ele trazer a descrição do ASU `[relatado pelo dono, sem material de apoio]`.
- Design: na recomposição do Style a base manda — desligar um módulo não remove o que já está no style base; módulos só somam. O dedup compara sequências de palavras (FIX-003). Os módulos de gênero e de andamento costumam custar 0 tag por isso (DEC-019). O chip de andamento é atalho do controle de BPM, no máximo um ligado (DEC-020).
````

## Fora de escopo

- A entrega 3 (excluir, mover, importar faixas, o rascunho marcado) e a i-043 (gravar direto no arquivo).
- A i-044 (a barra de controles que nao some): so registrada.
- Spec, CONTEXT, CEREBRO e os logs: ja gravados pelo chat; nao edite.
- Nada em `data/`, `schema/`, `scripts/` ou `kit-musica/`.

## Armadilhas desta WO

- **`autocrlf=true` na maquina do dono:** os hashes valem no disco em LF, antes do `add`. Nao rode `git checkout -- <arquivo>`: ele regrava em CRLF.
- **A E09 e longa:** se o seu aplicador ler ancora linha a linha, compare o bloco inteiro; o hash de chegada do `app/index.html` e a prova.
- **O `validate.py` desta maquina termina em `ESQUEMA NAO CONFERIDO`** (falta `jsonschema`): estado conhecido.
- **Os testes escrevem no stderr:** use `2>&1 >/dev/null | tail -1`.

## Depois de aplicar — conferencia antes do commit

| # | Checagem | Comando | Esperado |
|---|---|---|---|
| 1 | **Os onze arquivos sao os testados** | `sha1sum app/index.html README.md meta/CHANGELOG.md meta/IDEAS.md meta/ROADMAP.md meta/STATUS.md meta/specs/261104-varios-acervos.md meta/CONTEXT.md meta/CEREBRO.md logs/2026-11-04.md logs/2026-11-05.md` | a coluna **chegada**, os onze. **Prova as 19 edicoes.** |
| 2 | Validacao | `python3 scripts/validate.py; echo "exit=$?"` | `exit=0`, com a linha `OK  versao 0.12.0 igual em CHANGELOG, app, README e STATUS`; ultima linha `Tudo conforme ao esquema.` ou `ESQUEMA NAO CONFERIDO (...)` (esta maquina) |
| 3 | Os conversores seguem passando | `python3 scripts/test_convert_br.py 2>&1 >/dev/null \| tail -1` e `python3 scripts/test_convert_guides.py 2>&1 >/dev/null \| tail -1` | `OK` e `OK` |
| 4 | O codigo novo | `grep -c '^async function boot' app/index.html`, `grep -c '^const bootDone = boot();' app/index.html`, `grep -c '^function migrateMarks' app/index.html` | `1`, `1`, `1` |
| 5 | O codigo velho saiu | `grep -c '^function saveCollectionCache' app/index.html`, `grep -c '^function forgetCollection' app/index.html`, `grep -c '^boot();' app/index.html` | `0`, `0`, `0` |
| 6 | O registro | `grep -m1 '^## \[' meta/CHANGELOG.md`, `grep -c '^### i-044 ' meta/IDEAS.md`, `grep -c '^- \*\*Conferir a entrega 1 na tela' meta/STATUS.md` | `## [0.12.0] — 2026-11-05`, `1`, `0` |
| 7 | Nada alem do previsto | `GIT_OPTIONAL_LOCKS=0 git status --short --untracked-files=all` | os onze arquivos e esta WO, e nada mais (nenhum `.txt`, nenhum `__pycache__`) |

**Os tres campos de cada passo:** as sete sao rodadas por **quem aplica (o Code)**, na raiz do repo, em Git Bash,
com `LC_ALL=C.UTF-8`. **Chega no ramo?** A checagem 1 cobre os onze arquivos inteiros, inclusive o `app/index.html`
que o chat executou (`boot`, `migrateLegacy`, `migrateMarks`, `saveAcervo`, `forgetAcervo`, a janela). **Esta e qual
pergunta?** A 2 e a 3 respondem «funciona?»; as outras, «esta la?». O «funciona?» da janela no navegador do dono e
dele, depois do push, pelo roteiro do chat.

## Relatorio de aplicacao

Grave em `../261105-HHMM-code-cancioneiro-apply-wo0023.txt`, com o `HHMM` de `date +%y%m%d-%H%M` rodado na
hora. Diga o resultado da checagem 1 em primeiro lugar.

**Proximo comando** (ultima linha do relatorio, cru e sozinho):

```
/wrap
```

## Commit

```
git add app/index.html README.md meta/CHANGELOG.md meta/IDEAS.md meta/ROADMAP.md meta/STATUS.md meta/specs meta/CONTEXT.md meta/CEREBRO.md logs/2026-11-04.md logs/2026-11-05.md meta/workorders
```

```
git commit -m "feat: varios acervos no navegador e versao 0.12.0" -m "Entrega 2 da curadoria (i-041, DEC-028): cada json importado fica no IndexedDB pelo nome do arquivo; janela acervos na linha de origem; reabre no ultimo aberto; marcas usei por acervo, com migracao; a copia antiga so sai depois de lida de volta. Spec com o resultado, CONTEXT e CEREBRO (file:// e origem compartilhada), IDEAS (i-041, i-043, i-044), ROADMAP, README, STATUS inteiro."
```

```
git push
```
