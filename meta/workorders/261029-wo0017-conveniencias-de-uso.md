# WO 0017 — Conveniencias de uso: estrutura do cartao, titulo, arrastar, acervo no navegador, prompt em arquivo

## Cabecalho

> **Tipo:** WO de CODIGO (`app/index.html`, `schema/PROMPT-PARA-CHATS.md`) e de registro (inclui CEREBRO e Instrucoes).
> **Config sugerida:** Sonnet · `/effort medium`. 42 edicoes literais, o STATUS inteiro e um arquivo novo (a spec), todos aplicados e testados pelo chat numa copia; cada arquivo tem hash de chegada.
> **Pre-requisito:** commit `74d75f9`, branch `main`, sincronizada com `origin/main`, **arvore limpa** (so esta WO aparece como `??`).
> **Base:** `meta/specs/261029-conveniencias-de-uso.md` (criada por esta WO), decisoes do dono em 2026-10-29: **D1 sim, D2 completa, D3 some, D4 sim (alternativa em bloco de codigo), D5 segue a tela**; e o pedido do dono sobre o lugar do `/apply-wo` (DEC-024).
> **Depende de:** WO 0016, ja aplicada (`6a52111`, wrap `74d75f9`).
>
> **Arquivos — partida e chegada, os dois medidos pelo chat** (chegada = resultado de aplicar literalmente as edicoes abaixo, em LF):
>
> | arquivo | partida (sha1) | chegada (sha1) |
> |---|---|---|
> | `app/index.html` | `73e4a54f04ec58cb943587d446501313c9f784e7` | `403aecbfc50066d2e6cb2b1e6bd4080611e3fed6` |
> | `schema/PROMPT-PARA-CHATS.md` | `577b90fa94faa9b00a3427250c03c7ea0eedf37d` | `7ac49c5f849c9cc71fbccfc47359685150fe02dc` |
> | `meta/CEREBRO.md` | `111a90a920b89fa6aec6a20cac0850ff18701d0f` | `a971fb7be4345b9bb44979c98f583a5d54e3e587` |
> | `INSTRUCOES-DO-PROJETO.md` | `e673e8fcc43ba641a1460ffb6cfa558f99613cfd` | `280ae7fd2b2301e9c1b0a09837f4b773b8fca9f7` |
> | `README.md` | `20c86a70f962ae898fae5b70dd38a079ddf06c77` | `e4203eec825d07f35f88e64f0f94ffe26b716630` |
> | `meta/CONTEXT.md` | `0fd7bde03dbaf91dc0792f31a64e9d4e53f49cf2` | `663f984356c1fdba6c2439df2a0ed72ee7e56033` |
> | `meta/DECISIONS.md` | `293a8797a3980e3858935ba90798e42064cc07f0` | `7451ec4328076910101893d3b4b06b3d3198a838` |
> | `meta/IDEAS.md` | `3486e8d99fff4ef65aa44f91427f0016b74bdcc0` | `6833284049c400f0f53a9854d374185789fef988` |
> | `meta/ROADMAP.md` | `49b78278bec2e094334e66176a1d93a740975998` | `67fc96b62fcf4a787371fc00f9a3d6cbb7efc677` |
> | `logs/2026-10-29.md` | `d1bcdedd5ff71ad614125583a4e22b1e5791d034` | `5e2fb915e80336d868794e1d06c1610f06131f47` |
> | `meta/STATUS.md` | `ad83323800a8a2b94ef4cffa8bca8cc5a32d8f1c` | `cb996d27b7317f050aaaa35b3a94618c8c8518df` |
> | `meta/specs/261029-conveniencias-de-uso.md` | (nao existe) | `6f0efdfdbf6d2998ca271be3f94b2d2c5346abd3` |
>
> **Ancora semantica:** se um trecho-ancora nao bater EXATAMENTE, PARE e reporte.
> **Idempotencia:** antes de cada edicao, procure o texto NOVO INTEIRO; se ja estiver la, PULE e diga no relatorio.
>
> **Ancoras lidas em:** cada ancora foi extraida pelo chat do arquivo de partida (`git show 74d75f9:<arquivo>`, igual ao disco do dono pelos hashes acima, medidos em 2026-10-29) e conferida como ocorrendo **exatamente 1 vez** no estado em que a edicao e aplicada, na ordem abaixo.

---

## 1. Por que

A nota do dono `261029-1106.txt` e o achado da i-037 viraram uma frente so; o dono decidiu D1 a D5. Esta WO entrega:

- **Estrutura do cartao (D2, D3, DEC-023):** botao «Estrutura do cartao» com ordem (↑/↓) e mostrar/ocultar de seis
  blocos, guardada no navegador; a ordem padrao e exatamente a de antes. Com o Exclude oculto, o painel nao manda
  «no X» para ele.
- **Copiar o titulo** (i-033) e **arrastar o `.json`** para a tela (i-034).
- **Acervo guardado no navegador (D1, DEC-022):** o ultimo acervo importado volta ao abrir; a barra mostra de onde
  veio e quando, com «esquecer».
- **Export de album e acervo com o Style da tela (D5).**
- **Prompt (D4):** a «Saida» pede um `.json` para baixar e, sem arquivo, o JSON num unico bloco de codigo. A
  importacao aceita a resposta colada inteira, extrai o JSON e avisa.
- **DEC-024:** no fecho do chat, a linha `/apply-wo` vem antes do «Proximo» (CEREBRO e Instrucoes).
- **Registro:** spec nova, DEC-022 a DEC-024, IDEAS (i-030, i-033 a i-037 em trabalho; i-008 desbloqueada —
  os albuns chegaram; feedback ao kit), ROADMAP, CONTEXT, README, STATUS inteiro, log.

O app de chegada (`403aecbf…`) foi executado pelo chat em Chromium headless: **34 de 34**
criterios da spec, entre eles a estrutura padrao **igual a da 0.8.0** nos tres acervos (blocos, Style, linha de
qualidade). A tabela esta na spec.

**Nao ha versao nova nesta WO.** A 0.9.0 fecha depois da tela e do reteste curto do prompt.
**As Instrucoes mudam:** o dono cola a versao nova no painel do Projeto — nao e passo do Code.

## Edicao 0 — Conferencia de hash e de arvore

```
sha1sum app/index.html schema/PROMPT-PARA-CHATS.md meta/CEREBRO.md INSTRUCOES-DO-PROJETO.md README.md meta/CONTEXT.md meta/DECISIONS.md meta/IDEAS.md meta/ROADMAP.md logs/2026-10-29.md meta/STATUS.md
ls meta/specs/261029-conveniencias-de-uso.md
GIT_OPTIONAL_LOCKS=0 git status --short
```

Os onze batem com a coluna **partida**; a spec **nao existe** (o `ls` falha); e o `git status` mostra **so**
esta WO. Qualquer outra coisa: **PARE e reporte**.

## Edicoes E01 a E42

Na ordem. Copie o que esta ENTRE as linhas de quatro crases, sem elas. **O bloco termina na linha de quatro
crases, nunca num titulo:** varios blocos trazem linhas com `## `, `### ` ou cercas de tres crases (o regex do
app, o esqueleto do CEREBRO).

### E01 — app (1) — `app/index.html`

**Ancora, literal:**

````
  .prompt-dialog [data-role="prompt-status"] { min-height: 1.4em; margin: 10px 0 0; }
</style>
````

**Texto novo, literal:**

````
  .prompt-dialog [data-role="prompt-status"] { min-height: 1.4em; margin: 10px 0 0; }

  /* ---- Conveniencias de uso (spec 261029-conveniencias-de-uso) ---- */
  /* Copiar o titulo: o v6 tem campo de titulo (o ultimo do formulario). */
  .card-title .title-copy { margin-left: auto; padding: 3px 10px; font-size: 12px; }
  .card-title .title-copy.copied { background: var(--moss); color: #fff; border-color: var(--moss); }
  /* Estrutura do cartao: uma linha por bloco, com mostrar e mover */
  .layout-list { list-style: none; padding: 0; margin: 8px 0 0; display: flex; flex-direction: column; gap: 6px; }
  .layout-list li {
    display: flex; align-items: center; gap: 8px; padding: 6px 10px;
    border: 1px solid var(--line); border-radius: 8px; background: var(--paper-2); font-size: 13px;
  }
  .layout-list li.off span { color: var(--ink-soft); text-decoration: line-through; }
  .layout-list li .move { margin-left: auto; display: flex; gap: 4px; }
  .layout-list li .move button { padding: 2px 8px; }
  /* Origem do acervo (DEC-022): de onde veio o que esta na tela */
  .origin { font-size: 12px; color: var(--ink-soft); display: flex; gap: 8px; align-items: center; }
  .origin button { font-size: 12px; padding: 3px 8px; }
  /* Arrastar o .json para a tela (i-034) */
  .drop-hint {
    position: fixed; inset: 12px; z-index: 50; display: none;
    border: 3px dashed var(--ember); border-radius: var(--radius);
    background: rgba(244, 239, 230, .92); color: var(--ember);
    font-family: var(--serif); font-size: 24px; align-items: center; justify-content: center;
    pointer-events: none;
  }
  body.dragging .drop-hint { display: flex; }
</style>
````

### E02 — app (2) — `app/index.html`

**Ancora, literal:**

````
    <button id="example-btn">Baixar exemplo</button>
    <input type="file" id="file-input" accept=".json,application/json" hidden>
````

**Texto novo, literal:**

````
    <button id="example-btn">Baixar exemplo</button>
    <button id="layout-btn">Estrutura do cartão</button>
    <input type="file" id="file-input" accept=".json,application/json" hidden>
````

### E03 — app (3) — `app/index.html`

**Ancora, literal:**

````
  <span class="note" id="stats"></span>
</div>
````

**Texto novo, literal:**

````
  <span class="note" id="stats"></span>
  <span class="origin" id="origin"></span>
</div>
````

### E04 — app (4) — `app/index.html`

**Ancora, literal:**

````
    <p><strong>Nenhum acervo carregado.</strong></p>
    <p>Clique em <strong>Importar .json</strong> e escolha um arquivo do seu acervo<br>
    (ex.: <code>data/demo.json</code>), ou publique no GitHub Pages para carregar sozinho.</p>
  </div>
````

**Texto novo, literal:**

````
    <p><strong>Nenhum acervo carregado.</strong></p>
    <p>Clique em <strong>Importar .json</strong> ou <strong>arraste o arquivo para esta tela</strong><br>
    (ex.: <code>data/demo.json</code>). O último acervo importado fica guardado neste navegador.</p>
  </div>
````

### E05 — app (5) — `app/index.html`

**Ancora, literal:**

````
</dialog>

````

**Texto novo, literal:**

````
</dialog>

<dialog class="prompt-dialog" id="layout-dialog" aria-labelledby="layout-dialog-title">
  <h2 id="layout-dialog-title">Estrutura do cartão</h2>
  <p>A ordem dos blocos em todos os cartões, e quais aparecem. Fica guardada neste navegador.
  O título fica sempre no topo; o export .md segue a ordem do arquivo.</p>
  <ul class="layout-list" id="layout-list"></ul>
  <div class="dialog-actions">
    <button type="button" id="layout-reset-btn">Restaurar padrão</button>
    <button type="button" id="layout-close-btn" class="spacer">Fechar</button>
  </div>
</dialog>

<div class="drop-hint" aria-hidden="true">Solte o .json para importar</div>

````

### E06 — app (6) — `app/index.html`

**Ancora, literal:**

````
      setCollection(json);
      toast("Acervo carregado de " + path + moduleRefsNotice(json));
````

**Texto novo, literal:**

````
      setCollection(json);
      setOrigin("carregado de " + path.replace(/^\.\.\//, "") + " (GitHub Pages)", false);
      toast("Acervo carregado de " + path + moduleRefsNotice(json));
````

### E07 — app (7) — `app/index.html`

**Ancora, literal:**

````

function importFromFile(file) {
````

**Texto novo, literal:**

````

/** Le o texto de um .json. Aceita tambem a resposta de chat colada inteira: se
    o texto nao for JSON, procura um bloco de codigo (```json ... ```) e, sem ele,
    o trecho do primeiro "{" ao ultimo "}". Devolve {json, extracted} ou lanca.
    `extracted` vira aviso no toast — limpar calado apagaria o sinal (FIX-006). */
function parseCollectionText(text) {
  try { return { json: JSON.parse(text), extracted: false }; } catch (e) { /* tenta extrair */ }
  const fence = text.match(/```(?:json)?[ \t]*\r?\n([\s\S]*?)\r?\n```/);
  if (fence) return { json: JSON.parse(fence[1]), extracted: true };
  const a = text.indexOf("{"), z = text.lastIndexOf("}");
  if (a >= 0 && z > a) return { json: JSON.parse(text.slice(a, z + 1)), extracted: true };
  throw new Error("sem JSON");
}

function importFromFile(file) {
````

### E08 — app (8) — `app/index.html`

**Ancora, literal:**

````
    // so pode envolver a operacao que produz aquela causa (ver FIX-005).
    let json;
    try {
      json = JSON.parse(reader.result);
    } catch (e) {
````

**Texto novo, literal:**

````
    // so pode envolver a operacao que produz aquela causa (ver FIX-005).
    let json, extracted;
    try {
      ({ json, extracted } = parseCollectionText(reader.result));
    } catch (e) {
````

### E09 — app (9) — `app/index.html`

**Ancora, literal:**

````
      setCollection(json);
      toast("Acervo importado: " + (json.title || file.name)
            + (removidas ? " · " + removidas + " campo(s) interno(s) removido(s) — baixe de novo para gravar limpo" : "")
            + moduleRefsNotice(json));
    } catch (e) {
````

**Texto novo, literal:**

````
      setCollection(json);
      const guardado = saveCollectionCache(json, file.name);
      toast("Acervo importado: " + (json.title || file.name)
            + (extracted ? " · JSON extraído de um bloco de código" : "")
            + (removidas ? " · " + removidas + " campo(s) interno(s) removido(s) — baixe de novo para gravar limpo" : "")
            + moduleRefsNotice(json)
            + (guardado ? "" : " · não coube no navegador: ao fechar, ele não volta"));
    } catch (e) {
````

### E10 — app (10) — `app/index.html`

**Ancora, literal:**

````
  L.push("");
  (album.songs || []).forEach(s => L.push(songToMarkdown(s, false)));
  return L.join("\n");
````

**Texto novo, literal:**

````
  L.push("");
  // D5: album e acervo saem como a faixa — o Style da tela (modulos ligados e
  // BPM do controle). Antes saiam com o style base, sem estar escrito (i-037).
  (album.songs || []).forEach(s => L.push(songToMarkdown(s, true)));
  return L.join("\n");
````

### E11 — app (11) — `app/index.html`

**Ancora, literal:**

````
  }
  findNegations(style, lyrics).forEach(n =>
    el.appendChild(qSpan("«" + n + "»: mais confiável no campo Exclude", "warn")));
````

**Texto novo, literal:**

````
  }
  // D3: com o bloco Exclude oculto (o formulario do v6-mini nao tem o campo),
  // o aviso nao manda o usuario para um campo que ele escondeu.
  if (!isHidden("exclude")) findNegations(style, lyrics).forEach(n =>
    el.appendChild(qSpan("«" + n + "»: mais confiável no campo Exclude", "warn")));
````

### E12 — app (12) — `app/index.html`

**Ancora, literal:**

````
  title.appendChild(lang);
  card.appendChild(title);
````

**Texto novo, literal:**

````
  title.appendChild(lang);
  // i-033: o titulo tambem vai para o Suno (campo de titulo do v6). O rotulo e o
  // proprio h3; o botao copia so o texto.
  const tcopy = document.createElement("button");
  tcopy.type = "button"; tcopy.className = "title-copy"; tcopy.textContent = "copiar título";
  tcopy.addEventListener("click", () => copyText(song.title, tcopy));
  title.appendChild(tcopy);
  card.appendChild(title);
````

### E13 — app (13) — `app/index.html`

**Ancora, literal:**

````

  // Campos COPIAVEIS: rotulo fora, conteudo dentro
````

**Texto novo, literal:**

````

  // Os blocos do cartao sao montados num mapa e anexados na ordem da
  // «Estrutura do cartao» (i-030), pulando os ocultos. A ordem padrao e a de antes.
  const blocks = {};
  const put = (key, el) => { (blocks[key] = blocks[key] || []).push(el); };

  // Campos COPIAVEIS: rotulo fora, conteudo dentro
````

### E14 — app (14) — `app/index.html`

**Ancora, literal:**

````
  styleField.appendChild(styleQuality(recomposedStyle(song), song.lyrics, baseTagCount(song)));
  card.appendChild(styleField);
  const lyricsField = fieldBlock("Lyrics", song.lyrics, "lyrics");
````

**Texto novo, literal:**

````
  styleField.appendChild(styleQuality(recomposedStyle(song), song.lyrics, baseTagCount(song)));
  put("style", styleField);
  const lyricsField = fieldBlock("Lyrics", song.lyrics, "lyrics");
````

### E15 — app (15) — `app/index.html`

**Ancora, literal:**

````
    "acima de ~3.000 o Suno tende a correr e pular seções"));
  card.appendChild(lyricsField);

````

**Texto novo, literal:**

````
    "acima de ~3.000 o Suno tende a correr e pular seções"));
  put("lyrics", lyricsField);

````

### E16 — app (16) — `app/index.html`

**Ancora, literal:**

````
      "o Suno corta o que passar de 1.000 — sem aviso", "perto do limite de 1.000"));
    card.appendChild(ex);
  }
````

**Texto novo, literal:**

````
      "o Suno corta o que passar de 1.000 — sem aviso", "perto do limite de 1.000"));
    put("exclude", ex);
  }
````

### E17 — app (17) — `app/index.html`

**Ancora, literal:**

````
  if ((song.styleModules && song.styleModules.length) || Object.keys(App.modulesById).length) {
    card.appendChild(renderModules(song, card));
  }
````

**Texto novo, literal:**

````
  if ((song.styleModules && song.styleModules.length) || Object.keys(App.modulesById).length) {
    put("modules", renderModules(song, card));
  }
````

### E18 — app (18) — `app/index.html`

**Ancora, literal:**

````
    });
    card.appendChild(det);
  }
````

**Texto novo, literal:**

````
    });
    put("variants", det);
  }
````

### E19 — app (19) — `app/index.html`

**Ancora, literal:**

````
    det.appendChild(p);
    card.appendChild(det);
  }

````

**Texto novo, literal:**

````
    det.appendChild(p);
    put("notes", det);
  }

  currentLayout().order.forEach(key => {
    if (!isHidden(key)) (blocks[key] || []).forEach(el => card.appendChild(el));
  });

````

### E20 — app (20) — `app/index.html`

**Ancora, literal:**

````
/* ===================================================================
   Ligacao de eventos + boot
   =================================================================== */
document.getElementById("import-btn").addEventListener("click", () =>
````

**Texto novo, literal:**

````
/* ===================================================================
   Estrutura do cartao (i-030, DEC-023)
   Ordem e visibilidade dos blocos, por navegador, em App.ui.layout (estado de
   interface, DEC-004). A ordem padrao e exatamente a de antes desta funcao.
   O export .md nao segue a estrutura: e documento do acervo, ordem fixa.
   =================================================================== */
const CARD_BLOCKS = [
  { key: "style",    label: "Style of Music" },
  { key: "lyrics",   label: "Lyrics" },
  { key: "exclude",  label: "Exclude styles" },
  { key: "modules",  label: "Módulos de estilo" },
  { key: "variants", label: "Variantes de estilo" },
  { key: "notes",    label: "Notas de produção" },
];

/** A estrutura em uso: a salva, completada com blocos que ela nao conheca
    (versao nova do app) e limpa de chaves que nao existem mais. */
function currentLayout() {
  const known = CARD_BLOCKS.map(b => b.key);
  const saved = (App.ui && App.ui.layout) || {};
  const order = (saved.order || []).filter(k => known.includes(k));
  known.forEach(k => { if (!order.includes(k)) order.push(k); });
  const hidden = (saved.hidden || []).filter(k => known.includes(k));
  return { order, hidden };
}
function isHidden(key) { return currentLayout().hidden.includes(key); }
function saveLayout(layout) { App.ui.layout = layout; saveUiState(); render(); renderLayoutDialog(); }

function renderLayoutDialog() {
  const list = document.getElementById("layout-list");
  const lay = currentLayout();
  list.innerHTML = "";
  lay.order.forEach((key, i) => {
    const def = CARD_BLOCKS.find(b => b.key === key);
    const li = document.createElement("li");
    li.className = lay.hidden.includes(key) ? "off" : "";
    const cb = document.createElement("input");
    cb.type = "checkbox"; cb.checked = !lay.hidden.includes(key);
    cb.setAttribute("aria-label", "mostrar " + def.label);
    cb.addEventListener("change", () => {
      const hidden = lay.hidden.filter(k => k !== key);
      if (!cb.checked) hidden.push(key);
      saveLayout({ order: lay.order, hidden });
    });
    const name = document.createElement("span"); name.textContent = def.label;
    const mv = document.createElement("span"); mv.className = "move";
    const mk = (txt, delta, label) => {
      const b = document.createElement("button"); b.type = "button"; b.textContent = txt;
      b.setAttribute("aria-label", label + " " + def.label);
      const j = i + delta;
      b.disabled = j < 0 || j >= lay.order.length;
      b.addEventListener("click", () => {
        const order = lay.order.slice(); [order[i], order[j]] = [order[j], order[i]];
        saveLayout({ order, hidden: lay.hidden });
      });
      return b;
    };
    mv.appendChild(mk("↑", -1, "subir")); mv.appendChild(mk("↓", 1, "descer"));
    li.appendChild(cb); li.appendChild(name); li.appendChild(mv);
    list.appendChild(li);
  });
}

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

/* ===================================================================
   Ligacao de eventos + boot
   =================================================================== */
const EMPTY_HTML = document.getElementById("main").innerHTML;
document.getElementById("import-btn").addEventListener("click", () =>
````

### E21 — app (21) — `app/index.html`

**Ancora, literal:**

````
document.getElementById("example-btn").addEventListener("click", downloadExample);
["filter-album", "filter-state", "filter-used"].forEach(id =>
````

**Texto novo, literal:**

````
document.getElementById("example-btn").addEventListener("click", downloadExample);
document.getElementById("layout-btn").addEventListener("click", () => {
  renderLayoutDialog();
  document.getElementById("layout-dialog").showModal();
});
document.getElementById("layout-close-btn").addEventListener("click", () =>
  document.getElementById("layout-dialog").close());
document.getElementById("layout-reset-btn").addEventListener("click", () =>
  saveLayout({ order: CARD_BLOCKS.map(b => b.key), hidden: [] }));

// i-034: soltar um arquivo em qualquer lugar = importar, pelo mesmo caminho do
// botao. So reage a arraste de ARQUIVO (texto arrastado segue o normal).
let dragDepth = 0;
const hasFiles = e => e.dataTransfer && Array.from(e.dataTransfer.types || []).includes("Files");
document.addEventListener("dragenter", e => {
  if (!hasFiles(e)) return;
  e.preventDefault(); dragDepth++; document.body.classList.add("dragging");
});
document.addEventListener("dragover", e => { if (hasFiles(e)) e.preventDefault(); });
document.addEventListener("dragleave", e => {
  if (!hasFiles(e)) return;
  dragDepth = Math.max(0, dragDepth - 1);
  if (!dragDepth) document.body.classList.remove("dragging");
});
document.addEventListener("drop", e => {
  if (!hasFiles(e)) return;
  e.preventDefault(); dragDepth = 0; document.body.classList.remove("dragging");
  const f = e.dataTransfer.files[0];
  if (f) importFromFile(f);
});
["filter-album", "filter-state", "filter-used"].forEach(id =>
````

### E22 — app (22) — `app/index.html`

**Ancora, literal:**

````

tryAutoLoad();
</script>
````

**Texto novo, literal:**

````

boot();
</script>
````

### E23 — prompt: a Saida (1) — `schema/PROMPT-PARA-CHATS.md`

**Ancora, literal:**

````
## Saída
- Responda **APENAS com o JSON válido**, sem texto antes ou depois, sem cercas de ``` markdown.
- JSON válido: aspas duplas, sem vírgula sobrando, sem comentários.
````

**Texto novo, literal:**

````
## Saída
- **Se você consegue criar arquivos para download**, entregue um arquivo `.json` com o nome do `id` do álbum (ex.: `album-slug.json`), contendo só o JSON.
- **Se não consegue**, responda com o JSON inteiro dentro de **um único bloco de código** marcado como `json`, sem texto antes ou depois do bloco.
- JSON válido: aspas duplas, sem vírgula sobrando, sem comentários.
````

### E24 — prompt: a Saida (2) — `schema/PROMPT-PARA-CHATS.md`

**Ancora, literal:**

````
- O prompt ensina as cinco camadas e a regra copiável/referência — é o principal contra a bagunça dos álbuns antigos.
- Teste ponta a ponta: copie o prompt pelo app, peça algo num chat novo fora de Projeto, salve a resposta e importe na ferramenta; depois `python3 scripts/validate.py <arquivo>`.
````

**Texto novo, literal:**

````
- O prompt ensina as cinco camadas e a regra copiável/referência — é o principal contra a bagunça dos álbuns antigos.
- **Saída em arquivo ou em bloco de código (DEC-023):** o arquivo baixa pronto para arrastar no app; o bloco de código tem botão de copiar que entrega só o JSON. Se a resposta for colada inteira (com as cercas ou texto em volta), a importação extrai o JSON e avisa no toast — não é para depender disso, é rede de segurança.
- Teste ponta a ponta: copie o prompt pelo app, peça algo num chat novo fora de Projeto, baixe o arquivo (ou copie o bloco) e arraste/importe na ferramenta; depois `python3 scripts/validate.py <arquivo>`.
````

### E25 — CEREBRO: o lugar do /apply-wo (1) — `meta/CEREBRO.md`

**Ancora, literal:**

````
Todo turno de trabalho fecha assim. **Próximo** vem antes de um divisor; o resto vem depois dele. **Quando cada linha aparece é CONDIÇÃO OBSERVÁVEL, não julgamento** — o teste é «a condição é falsa?», nunca «me pareceu que não se aplicava»: **Próximo**, **Estado** e **Config recomendada** saem SEMPRE; **Arquivar / Manter** sai quando houver qualquer arquivo avulso na pasta-pai, e essa condição se verifica LISTANDO a pasta-pai, não lembrando; **Handoff** sai quando algum arquivo foi entregue NESTE turno. Fora disso a linha não existe — e linha sem conteúdo real não aparece: não escreva «nada a arquivar» nem invente handoff. **Reconstituir este bloco de memória é o que o faz derivar, e a variação é compensatória:** quem lembra do campo que esqueceu da última vez esquece outro — medido em quatro turnos seguidos, quatro formas diferentes, com o formato fixo escrito no arquivo lido a cada mensagem. Por isso o esqueleto abaixo existe: **copie e preencha, não reconstitua.**
1. **Próximo** — sempre presente, ANTES do divisor, em duas partes: **(a) Ação** — a próxima coisa concreta a fazer; **(b) Peça no próximo turno** — a frase que o usuário pode mandar de volta para retomar sem reconstruir contexto (a frente sugerida, já redigida como pedido). Não é lista de possibilidades: é uma ação e um pedido.
````

**Texto novo, literal:**

````
Todo turno de trabalho fecha assim. **Próximo** vem antes de um divisor; o resto vem depois dele. **Quando cada linha aparece é CONDIÇÃO OBSERVÁVEL, não julgamento** — o teste é «a condição é falsa?», nunca «me pareceu que não se aplicava»: **Próximo**, **Estado** e **Config recomendada** saem SEMPRE; **Arquivar / Manter** sai quando houver qualquer arquivo avulso na pasta-pai, e essa condição se verifica LISTANDO a pasta-pai, não lembrando; **Handoff** sai quando algum arquivo foi entregue NESTE turno. Fora disso a linha não existe — e linha sem conteúdo real não aparece: não escreva «nada a arquivar» nem invente handoff. **Reconstituir este bloco de memória é o que o faz derivar, e a variação é compensatória:** quem lembra do campo que esqueceu da última vez esquece outro — medido em quatro turnos seguidos, quatro formas diferentes, com o formato fixo escrito no arquivo lido a cada mensagem. Por isso o esqueleto abaixo existe: **copie e preencha, não reconstitua.**
0. **Aplicar** — só quando houver WO neste turno: a linha `/apply-wo <arquivo>` sozinha, num bloco de código, **logo antes do divisor e do Próximo** — no fim do corpo da resposta, onde a leitura termina, e não no rodapé depois de Estado, Arquivar, Config e Handoff (DEC-024: no fim da mensagem, o dono rolava até o fundo a cada WO). É o primeiro gesto dele depois de ler; o resto do fecho é consulta.
1. **Próximo** — sempre presente, ANTES do divisor, em duas partes: **(a) Ação** — a próxima coisa concreta a fazer; **(b) Peça no próximo turno** — a frase que o usuário pode mandar de volta para retomar sem reconstruir contexto (a frente sugerida, já redigida como pedido). Não é lista de possibilidades: é uma ação e um pedido.
````

### E26 — CEREBRO: o lugar do /apply-wo (2) — `meta/CEREBRO.md`

**Ancora, literal:**

````
**Esqueleto — copie e preencha; a condição de cada linha está à direita:**
```
````

**Texto novo, literal:**

````
**Esqueleto — copie e preencha; a condição de cada linha está à direita:**
~~~
**Aplicar no Code**                           (se há WO NESTE turno — antes do divisor)
```
/apply-wo meta/workorders/<arquivo da WO>
```
````

### E27 — CEREBRO: o lugar do /apply-wo (3) — `meta/CEREBRO.md`

**Ancora, literal:**

````
- `<arquivo>` → <destino>
```
**De quem é este bloco:** da raia de **planejamento** (o assistente no chat). Quem **executa** no Claude Code não fecha assim — fecha com o **relatório de trabalho**: o que fez, o que encontrou que foge do que a tarefa pedia, os arquivos tocados, o resultado do build/validação e o commit. Trocar o relatório por este formulário perde a informação que só quem executou tem.
````

**Texto novo, literal:**

````
- `<arquivo>` → <destino>
~~~
**De quem é este bloco:** da raia de **planejamento** (o assistente no chat). Quem **executa** no Claude Code não fecha assim — fecha com o **relatório de trabalho**: o que fez, o que encontrou que foge do que a tarefa pedia, os arquivos tocados, o resultado do build/validação e o commit. Trocar o relatório por este formulário perde a informação que só quem executou tem.
````

### E28 — Instrucoes: o lugar do /apply-wo (1) — `INSTRUCOES-DO-PROJETO.md`

**Ancora, literal:**

````
**Arquivo não lido não se deduz — leia do disco; o Code mede o que roda.**
**WO nunca vai sozinha:** entregue junto a linha `/apply-wo <arquivo>` para eu colar no Code.
**Commit:** havendo WO no turno, o bloco é de quem APLICA e cobre tudo. Não havendo WO, é do chat: os três comandos em ordem, mensagem sem acento. Bloco git parcial (só `add`) não serve.
````

**Texto novo, literal:**

````
**Arquivo não lido não se deduz — leia do disco; o Code mede o que roda.**
**WO nunca vai sozinha:** a linha `/apply-wo <arquivo>` vai num bloco de código logo ANTES do «Próximo» do fecho, para eu colar no Code.
**Commit:** havendo WO no turno, o bloco é de quem APLICA e cobre tudo. Não havendo WO, é do chat: os três comandos em ordem, mensagem sem acento. Bloco git parcial (só `add`) não serve.
````

### E29 — README (1) — `README.md`

**Ancora, literal:**

````
1. **Pelo navegador (recomendado):** abra a versão publicada no GitHub Pages — o acervo carrega sozinho.
   **Ou local:** duplo-clique em `app/index.html` (modo `file://`) e clique em *Importar .json*.
2. Escolha um acervo de `data/` (ex.: `demo.json`).
3. Navegue por álbuns, copie style/lyrics por botão, marque o que usou.
4. Ligue/desligue **módulos de estilo** por camada para gerar variações — o Style recompõe ao vivo. Para mudar o andamento, use o campo de **BPM** do cartão (ou um chip da camada Andamento, que é atalho para ele): o número muda em todo o Style, nunca aparecem dois. O Suno trata BPM como aproximação.
````

**Texto novo, literal:**

````
1. **Pelo navegador (recomendado):** abra a versão publicada no GitHub Pages — o acervo carrega sozinho.
   **Ou local:** duplo-clique em `app/index.html` (modo `file://`) e clique em *Importar .json* — ou arraste o arquivo para a tela. O último acervo importado fica guardado no navegador e volta quando você reabre.
2. Escolha um acervo de `data/` (ex.: `demo.json`).
3. Navegue por álbuns, copie título, style e lyrics por botão, marque o que usou. Em *Estrutura do cartão*, escolha a ordem dos blocos e esconda os que você não usa (o Exclude, por exemplo, não existe no formulário gratuito do Suno v6).
4. Ligue/desligue **módulos de estilo** por camada para gerar variações — o Style recompõe ao vivo. Para mudar o andamento, use o campo de **BPM** do cartão (ou um chip da camada Andamento, que é atalho para ele): o número muda em todo o Style, nunca aparecem dois. O Suno trata BPM como aproximação.
````

### E30 — README (2) — `README.md`

**Ancora, literal:**

````

No app, clique em **Prompt para chats**, escreva o seu pedido e copie: o prompt vai inteiro, com o pedido no lugar. Cole num chat novo e importe o JSON que ele devolver. O texto do prompt vive em `schema/PROMPT-PARA-CHATS.md` — o botão busca esse arquivo a cada clique, então o que está no repositório é o que você copia.

````

**Texto novo, literal:**

````

No app, clique em **Prompt para chats**, escreva o seu pedido e copie: o prompt vai inteiro, com o pedido no lugar. Cole num chat novo: ele devolve um arquivo `.json` (ou, se não puder criar arquivo, o JSON num bloco de código, com botão de copiar). Arraste o arquivo para o app. O texto do prompt vive em `schema/PROMPT-PARA-CHATS.md` — o botão busca esse arquivo a cada clique, então o que está no repositório é o que você copia.

````

### E31 — README (3) — `README.md`

**Ancora, literal:**

````

O acervo canônico são os **arquivos JSON versionados** em `data/`. O navegador (localStorage) guarda só estado efêmero (marcações da sessão) — nunca o acervo. Ver `meta/DECISIONS.md` (DEC-004).

````

**Texto novo, literal:**

````

O acervo canônico são os **arquivos JSON versionados** em `data/`. O navegador (localStorage) guarda as marcações, a estrutura do cartão e uma **cópia do último acervo importado** — cache, nunca a fonte: a linha de origem diz de onde ela veio e quando, e *esquecer* a apaga. Ver `meta/DECISIONS.md` (DEC-004, DEC-022).

````

### E32 — CONTEXT (1) — `meta/CONTEXT.md`

**Ancora, literal:**

````
- **Nome "cancioneiro"** (DEC-003): português, evoca coletânea de canções, não amarra à marca "Suno" — sobrevive a troca de plataforma.
- **Dado canônico em arquivo versionado, não em `localStorage`** (DEC-004): o navegador é cache/rascunho; o JSON no repo é a verdade. Evita perder acervo ao limpar o navegador.

````

**Texto novo, literal:**

````
- **Nome "cancioneiro"** (DEC-003): português, evoca coletânea de canções, não amarra à marca "Suno" — sobrevive a troca de plataforma.
- **Dado canônico em arquivo versionado, não em `localStorage`** (DEC-004): o navegador é cache/rascunho; o JSON no repo é a verdade. Evita perder acervo ao limpar o navegador. O navegador guarda uma **cópia do último acervo importado** para ele voltar ao abrir — cache, com a origem e a data na tela e um botão para esquecer (DEC-022).

````

### E33 — CONTEXT (2) — `meta/CONTEXT.md`

**Ancora, literal:**

````
| Export | Markdown gerado por JS | Formato limpo (rótulo FORA do bloco copiável). |
| Persistência de sessão | `localStorage` só para estado efêmero (marcações "copiado", filtros) | Nunca fonte de verdade — ver DEC-004. |
| Repositório | Git; desenvolvido no Claude Code + chat de planejamento | Ver seção "Raias" no CEREBRO. |
````

**Texto novo, literal:**

````
| Export | Markdown gerado por JS | Formato limpo (rótulo FORA do bloco copiável). |
| Persistência no navegador | `localStorage`: marcações «usei», a estrutura do cartão e a cópia do último acervo importado | Nunca fonte de verdade — ver DEC-004 e DEC-022. |
| Repositório | Git; desenvolvido no Claude Code + chat de planejamento | Ver seção "Raias" no CEREBRO. |
````

### E34 — CONTEXT (3) — `meta/CONTEXT.md`

**Ancora, literal:**

````
- **Não parsear MD de convenção livre.** Os álbuns antigos (`ALBUM_*`, `album_guia_suno.md`) usam convenções diferentes entre si (`[ESTILO SUNO]`, `[LETRA]`, `[VAR A]`). A conversão para o esquema é semi-manual/assistida por chat, não um parser universal confiável.
- **`localStorage` não é backup.** Limpar o navegador apaga marcações. O acervo real está no JSON versionado.
- **A interface do Suno muda.** Nomes de botões/menus (Extend, Persona, Custom Mode, Creative Sliders) variam entre versões. O conhecimento no HISTORY tem data — reconfirmar na conta antes de assumir que algo sumiu.
````

**Texto novo, literal:**

````
- **Não parsear MD de convenção livre.** Os álbuns antigos (`ALBUM_*`, `album_guia_suno.md`) usam convenções diferentes entre si (`[ESTILO SUNO]`, `[LETRA]`, `[VAR A]`). A conversão para o esquema é semi-manual/assistida por chat, não um parser universal confiável.
- **`localStorage` não é backup.** Limpar o navegador apaga marcações, a estrutura do cartão e a cópia do acervo. O acervo real está no JSON versionado; a cópia guardada pode estar velha se o arquivo mudou fora — a linha de origem diz quando ela foi importada.
- **A interface do Suno muda.** Nomes de botões/menus (Extend, Persona, Custom Mode, Creative Sliders) variam entre versões. O conhecimento no HISTORY tem data — reconfirmar na conta antes de assumir que algo sumiu.
````

### E35 — CONTEXT (4) — `meta/CONTEXT.md`

**Ancora, literal:**

````

Ferramenta pessoal de hobby. Uso típico: abrir `index.html`, importar o JSON do acervo, escolher um álbum, copiar o style de uma faixa (botão), copiar a letra (botão), gerar no Suno, marcar a faixa como usada. Para levar uma seleção a um chat ou Projeto, exportar em `.md`. Para gerar canções novas: «Prompt para chats» → colar num chat novo → importar o JSON que ele devolver.
````

**Texto novo, literal:**

````

Ferramenta pessoal de hobby. Uso típico: abrir `index.html`, importar o JSON do acervo, escolher um álbum, copiar o style de uma faixa (botão), copiar a letra (botão), gerar no Suno, marcar a faixa como usada. Para levar uma seleção a um chat ou Projeto, exportar em `.md`. Para gerar canções novas: «Prompt para chats» → colar num chat novo → arrastar para o app o `.json` que ele devolver (ou importar). A ordem e a visibilidade dos blocos do cartão se ajustam em «Estrutura do cartão».
````

### E36 — DEC-022 a DEC-024 no fim (1) — `meta/DECISIONS.md`

**Ancora, literal:**

````
**Consequencias:** (+) Quem gera o acervo recebe o contrato que o app le; quem usa o app pega o prompt atual sem abrir pasta, e cada push o atualiza. (+) O acoplamento entre o botao e o arquivo do prompt tem checagem. (−) O botao depende de rede e do Pages; no `file://`, de o Pages aceitar o `fetch` de uma pagina local, nao conferido (sem isso, cai no link). (−) O prompt cresceu de 5.829 para 8.954 bytes (6.500 caracteres copiados); o reteste mede se a adesao caiu. (−) Os numeros de tags vem de fonte secundaria e divergem entre si (ate 8, contra 4 a 7).
````

**Texto novo, literal:**

````
**Consequencias:** (+) Quem gera o acervo recebe o contrato que o app le; quem usa o app pega o prompt atual sem abrir pasta, e cada push o atualiza. (+) O acoplamento entre o botao e o arquivo do prompt tem checagem. (−) O botao depende de rede e do Pages; no `file://`, de o Pages aceitar o `fetch` de uma pagina local, nao conferido (sem isso, cai no link). (−) O prompt cresceu de 5.829 para 8.954 bytes (6.500 caracteres copiados); o reteste mede se a adesao caiu. (−) Os numeros de tags vem de fonte secundaria e divergem entre si (ate 8, contra 4 a 7).

---

## DEC-022 — O último acervo importado fica guardado no navegador, como cache (amplia a DEC-004)

**Data:** 2026-10-29
**Status:** aceita
**Contexto:** O dono fecha o navegador e o acervo some; só as marcas «usei» voltam (nota `261029-1106.txt`, i-035). A DEC-004 diz que o navegador é cache/rascunho e o JSON versionado é a verdade — e até aqui o app não guardava o acervo nem como cache.
**Decisão:** O último acervo **importado** (botão ou arrastar) é guardado em `localStorage` (`cancioneiro:acervo`: a coleção, o nome do arquivo e a hora) e volta ao abrir, antes da carga automática do Pages. A barra de controles mostra a **origem** («Acervo importado de X em dd/mm/aaaa hh:mm · guardado neste navegador») com o botão **«esquecer»**, que apaga a cópia. Se o navegador recusar, o app importa assim mesmo e avisa. A DEC-004 continua: a fonte é o arquivo; a cópia é cache.
**Alternativas consideradas:** não guardar (o atrito do dono fica); guardar vários acervos (sem pedido e com mais estado para ficar velho); IndexedDB (o acervo de 27 KB cabe com folga no `localStorage`, e a API síncrona simplifica a abertura).
**Consequências:** (+) Abrir o app volta ao último acervo, também no `file://`. (+) O app nunca edita o acervo (FIX-004), então a cópia é igual ao arquivo importado. (−) Se o arquivo mudar fora, a cópia fica velha até importar de novo — a linha de origem com data é o que avisa. (−) Outro navegador ou perfil não vê a cópia.

---

## DEC-023 — Estrutura do cartão configurável; export de álbum segue a tela; o prompt pede arquivo, com bloco de código como alternativa

**Data:** 2026-10-29
**Status:** aceita
**Contexto:** Nota do dono de 2026-10-29 e capturas da conta dele: o v6-mini não tem campo de Exclude; o dono preenche o Suno de baixo para cima e quer controlar a estrutura do cartão; copiar o JSON do chat para o Bloco de notas é atrito. Achado no mesmo dia: o export de álbum saía com o `style` base, o de faixa com o recomposto (i-037). Decisões do dono: D2 completa, D3 some, D4 sim (com o JSON em bloco de código como alternativa), D5 segue a tela.
**Decisão:** (1) «Estrutura do cartão»: ordem (↑/↓) e visibilidade de seis blocos — Style, Lyrics, Exclude, Módulos, Variantes, Notas —, em `App.ui.layout` no navegador; a ordem padrão é a de antes; título e metadados ficam no topo; o export `.md` não segue a estrutura. (2) Com o Exclude oculto, o painel de qualidade não sugere levar «no X» para ele. (3) Botão «copiar título» no cartão. (4) Arrastar um arquivo para a tela importa pelo mesmo caminho do botão. (5) `albumToMarkdown` usa o Style recomposto. (6) O prompt pede um `.json` para download; quem não puder criar arquivo responde com o JSON num único bloco de código `json`. A importação aceita a resposta colada inteira: extrai o bloco de código (ou do primeiro `{` ao último `}`) e diz no toast que extraiu.
**Alternativas consideradas:** alternar entre duas ordens prontas (o dono pediu a completa); esconder o Exclude só no v6-mini (o app não sabe o plano de quem usa); export seguir a estrutura do cartão (o `.md` é documento do acervo, e esconder lá apagaria dado); manter «só o JSON, sem cercas» como alternativa (o bloco de código tem botão de copiar que entrega só o JSON — refinamento do dono); importação estrita (resposta colada inteira falharia sem explicação).
**Consequências:** (+) A tela se ajusta ao formulário de quem usa; o padrão não muda nada para quem não mexer. (+) Resposta do chat vira arquivo arrastável, ou bloco com botão de copiar. (−) O prompt mudou na «Saída» depois do reteste de 2026-10-29: pede reteste curto. (−) Mais estado de interface no navegador (estrutura e acervo).

---

## DEC-024 — No fecho do chat, a linha `/apply-wo` vem antes do «Próximo»

**Data:** 2026-10-29
**Status:** aceita
**Contexto:** O fecho de turno segue o esqueleto do CEREBRO (Próximo, Estado, Arquivar/Manter, Config, Handoff), que não tinha lugar para o comando a colar no Code; por uma regra escrita só num brief de handoff, a linha ia «por último na mensagem». O dono, que cola a linha a cada WO, precisava rolar até o fim da resposta para achá-la `[relatado pelo dono, 2026-10-29]`.
**Decisão:** Havendo WO no turno, o bloco de código com `/apply-wo <arquivo>` vem **logo antes do divisor e do «Próximo»** — no fim do corpo, onde a leitura termina. Fica no CEREBRO (item 0 do fecho, e no esqueleto) e nas Instruções.
**Alternativas consideradas:** manter no fim (o atrito é diário); pôr no começo da resposta (vem antes de o dono saber o que a WO faz).
**Consequências:** (+) Um gesto a menos por WO. (−) As Instruções mudaram: o dono cola a versão nova no painel do Projeto.
````

### E37 — IDEAS (1) — `meta/IDEAS.md`

**Ancora, literal:**

````
Converter os `ALBUM_*.md` e `album_guia_suno.md` para o esquema, um álbum por vez (semi-assistido por chat), populando `data/`. Começar pelo `album_guia_suno.md` (mais limpo). Backlog do STATUS.

````

**Texto novo, literal:**

````
Converter os `ALBUM_*.md` e `album_guia_suno.md` para o esquema, um álbum por vez (semi-assistido por chat), populando `data/`. Começar pelo `album_guia_suno.md` (mais limpo). Backlog do STATUS.
**Desbloqueada em 2026-10-29:** o dono trouxe os álbuns para a pasta-pai — `../Album Rainha da Preguiça/` (11 arquivos: índice-mestre e 10 volumes) e `../Albuns/` (8 guias, entre eles o `album_guia_suno.md`), cerca de 44 mil linhas `[medido por instrumento: wc -l]`. Ainda não lidos: frente própria.

````

### E38 — IDEAS (2) — `meta/IDEAS.md`

**Ancora, literal:**

````

### i-030 💡 Ordem dos campos no cartao: Lyrics acima do Style, como no Suno
`[relatado pelo dono, 2026-10-28]` O cartao mostra Style em cima e Lyrics embaixo; no Suno e o contrario, e copiar na ordem da tela agilizaria. O dono prefere que seja **configuravel**. A preferencia e estado de interface e pode morar no navegador (DEC-004). A decidir na spec: se o export MD segue a ordem escolhida, e onde fica o controle (cabecalho ou cartao).
````

**Texto novo, literal:**

````

### i-030 🔨 Ordem dos campos no cartao: Lyrics acima do Style, como no Suno
`[relatado pelo dono, 2026-10-28]` O cartao mostra Style em cima e Lyrics embaixo; no Suno e o contrario, e copiar na ordem da tela agilizaria. O dono prefere que seja **configuravel**. A preferencia e estado de interface e pode morar no navegador (DEC-004). A decidir na spec: se o export MD segue a ordem escolhida, e onde fica o controle (cabecalho ou cartao).
````

### E39 — IDEAS (3) — `meta/IDEAS.md`

**Ancora, literal:**

````

### i-033 💡 Copiar o titulo da faixa com um clique
`[relatado pelo dono, 2026-10-29, nota 1106]` Faltou copiar facil o nome da musica. O formulario do v6 tem campo de titulo (o ultimo, antes de «Save to»). Um botao «copiar» ao lado do titulo do cartao, com a mesma marcacao de copiado dos outros campos.

### i-034 💡 Arrastar o .json para a tela e carregar
`[relatado pelo dono, 2026-10-29, nota 1106]` Soltar o arquivo em qualquer lugar da pagina = importar, pelo mesmo caminho do botao (saneamento e avisos iguais: FIX-006, FIX-009). Combina com o prompt que entrega arquivo (i-036): baixar do chat e arrastar para o app.

### i-035 💡 O acervo continuar carregado depois de fechar o navegador
`[relatado pelo dono, 2026-10-29, nota 1106]` Hoje so as marcas «usei» sobrevivem; o acervo some ao fechar. Guardar uma copia do ultimo acervo importado no navegador e recarrega-la ao abrir. **Toca a DEC-004** (o navegador e cache, nunca fonte): uma copia do ultimo arquivo importado e cache legitimo, porque o app nao edita o acervo (FIX-004) — a copia e igual ao arquivo. Risco a tratar: o arquivo mudar fora (um chat gerou versao nova) e o app seguir mostrando a copia velha sem aviso; mitigacao: dizer na tela de onde veio o acervo e quando foi importado, e um botao para esquecer a copia. A carga automatica do Pages (`demo.json`) passa a valer so quando nao houver copia. Pede DEC propria.

### i-036 💡 O prompt pedir o JSON como arquivo para baixar
`[relatado pelo dono, 2026-10-29, nota 1106]` Em vez de texto para copiar, o chat entregar um `.json` para download. Ganha: sem colar no Bloco de notas, sem erro de codificacao, nome de arquivo pronto — e casa com a i-034. Custa: depende de o chat conseguir criar arquivo (varia por produto e por recurso ligado), e o texto atual do prompt foi o que passou no reteste de 2026-10-29 — mudar exige retestar. Forma candidata: pedir arquivo **se o chat puder criar arquivos**, e manter «so o JSON, sem texto» como alternativa.

### i-037 💡 Export de album e de acervo com o Style da tela
Achado em 2026-10-29 nos `.md` que o dono exportou: o export de **faixa** sai com o Style recomposto (modulos ligados, controle de BPM), o de **album** e o de **acervo** saem com o `style` base (`albumToMarkdown` chama `songToMarkdown(s, false)`), desde a 0.4.0. Em ar-01, 18 tags na faixa e 10 no album. Pode ser o certo — o album como documento do acervo, a faixa como «o que vou colar agora» —, mas a diferenca nao aparece na tela nem estava escrita. Decidir: os tres seguem a tela, ou o album/acervo continua base e o botao diz isso.

````

**Texto novo, literal:**

````

### i-033 🔨 Copiar o titulo da faixa com um clique
`[relatado pelo dono, 2026-10-29, nota 1106]` Faltou copiar facil o nome da musica. O formulario do v6 tem campo de titulo (o ultimo, antes de «Save to»). Um botao «copiar» ao lado do titulo do cartao, com a mesma marcacao de copiado dos outros campos.

### i-034 🔨 Arrastar o .json para a tela e carregar
`[relatado pelo dono, 2026-10-29, nota 1106]` Soltar o arquivo em qualquer lugar da pagina = importar, pelo mesmo caminho do botao (saneamento e avisos iguais: FIX-006, FIX-009). Combina com o prompt que entrega arquivo (i-036): baixar do chat e arrastar para o app.

### i-035 🔨 O acervo continuar carregado depois de fechar o navegador
`[relatado pelo dono, 2026-10-29, nota 1106]` Hoje so as marcas «usei» sobrevivem; o acervo some ao fechar. Guardar uma copia do ultimo acervo importado no navegador e recarrega-la ao abrir. **Toca a DEC-004** (o navegador e cache, nunca fonte): uma copia do ultimo arquivo importado e cache legitimo, porque o app nao edita o acervo (FIX-004) — a copia e igual ao arquivo. Risco a tratar: o arquivo mudar fora (um chat gerou versao nova) e o app seguir mostrando a copia velha sem aviso; mitigacao: dizer na tela de onde veio o acervo e quando foi importado, e um botao para esquecer a copia. A carga automatica do Pages (`demo.json`) passa a valer so quando nao houver copia. Pede DEC propria.

### i-036 🔨 O prompt pedir o JSON como arquivo para baixar
`[relatado pelo dono, 2026-10-29, nota 1106]` Em vez de texto para copiar, o chat entregar um `.json` para download. Ganha: sem colar no Bloco de notas, sem erro de codificacao, nome de arquivo pronto — e casa com a i-034. Custa: depende de o chat conseguir criar arquivo (varia por produto e por recurso ligado), e o texto atual do prompt foi o que passou no reteste de 2026-10-29 — mudar exige retestar. Forma candidata: pedir arquivo **se o chat puder criar arquivos**, e manter «so o JSON, sem texto» como alternativa.

### i-037 🔨 Export de album e de acervo com o Style da tela
Achado em 2026-10-29 nos `.md` que o dono exportou: o export de **faixa** sai com o Style recomposto (modulos ligados, controle de BPM), o de **album** e o de **acervo** saem com o `style` base (`albumToMarkdown` chama `songToMarkdown(s, false)`), desde a 0.4.0. Em ar-01, 18 tags na faixa e 10 no album. Pode ser o certo — o album como documento do acervo, a faixa como «o que vou colar agora» —, mas a diferenca nao aparece na tela nem estava escrita. Decidir: os tres seguem a tela, ou o album/acervo continua base e o botao diz isso.

**Em trabalho (2026-10-29, WO 0017):** as i-030, i-033 a i-037 viraram uma frente so, `meta/specs/261029-conveniencias-de-uso.md` (DEC-022, DEC-023). Decisoes do dono: acervo guardado no navegador (D1), estrutura completa (D2), aviso de negacao some com o Exclude oculto (D3), prompt pede arquivo e, sem arquivo, o JSON em bloco de codigo (D4), export segue a tela (D5). Fecha na 0.9.0, depois da tela e do reteste curto do prompt.

````

### E40 — IDEAS (4) — `meta/IDEAS.md`

**Ancora, literal:**

````
- **[2026-10-28] O nicho de musica do KCM ainda nao carrega o que este projeto aprendeu sobre o Suno** `[relatado pelo dono]`. Os projetos de musica que o KCM monta nascem sem o conhecimento destilado aqui: `meta/HISTORY.md` §1-13 (o que tem efeito no Suno, com fonte e confianca), a regra de dominio (rotulo fora do copiavel) e o contrato prompt -> JSON. E o teste base de 2026-10-28 mostra o custo de calar: pedido o que o prompt nao ensinava (modulos), tres chats inventaram tres formatos. Sugestao ao kit: o nicho de musica trazer um resumo desse material como ponto de partida — candidato natural e a i-023 (skill com os macetes do Suno), que ja tem o conteudo pronto.

````

**Texto novo, literal:**

````
- **[2026-10-28] O nicho de musica do KCM ainda nao carrega o que este projeto aprendeu sobre o Suno** `[relatado pelo dono]`. Os projetos de musica que o KCM monta nascem sem o conhecimento destilado aqui: `meta/HISTORY.md` §1-13 (o que tem efeito no Suno, com fonte e confianca), a regra de dominio (rotulo fora do copiavel) e o contrato prompt -> JSON. E o teste base de 2026-10-28 mostra o custo de calar: pedido o que o prompt nao ensinava (modulos), tres chats inventaram tres formatos. Sugestao ao kit: o nicho de musica trazer um resumo desse material como ponto de partida — candidato natural e a i-023 (skill com os macetes do Suno), que ja tem o conteudo pronto.
- **[2026-10-29] O fecho de turno nao tem lugar para o comando que o dono cola, e o rodape e o pior lugar.** O esqueleto do CEREBRO tem Proximo, Estado, Arquivar/Manter, Config e Handoff; a linha `/apply-wo` ficou sem endereco, e uma regra escrita so num brief a mandou para o fim da mensagem — o dono rolava ate o fundo a cada WO `[relatado pelo dono]`. Sugestao ao kit: o esqueleto trazer um item «Aplicar» (o comando a colar, num bloco de codigo) **antes** do divisor e do Proximo, e dizer que todo comando que o dono copia vai em bloco de codigo, inclusive a resposta que um chat externo devolve (aqui: o JSON do prompt-modelo, DEC-023). Adotado neste projeto na DEC-024.

````

### E41 — ROADMAP (1) — `meta/ROADMAP.md`

**Ancora, literal:**

````
- ✅ Script de validação de acervo `scripts/validate.py`.
- ⬜ Converter `album_guia_suno.md` inteiro como segundo dataset (i-008).
````

**Texto novo, literal:**

````
- ✅ Script de validação de acervo `scripts/validate.py`.
- 🔨 Conveniências de uso: estrutura do cartão configurável, copiar título, arrastar o `.json`, acervo guardado no navegador, prompt que entrega arquivo, export de álbum com o Style da tela (DEC-022, DEC-023; i-030, i-033 a i-037) — aplicadas, falta a tela e o reteste do dono.
- ⬜ Converter `album_guia_suno.md` inteiro como segundo dataset (i-008).
````

### E42 — log: Conversa 3 no fim (1) — `logs/2026-10-29.md`

**Ancora, literal:**

````
- Spec das conveniências (i-030, i-033 a i-037).
````

**Texto novo, literal:**

````
- Spec das conveniências (i-030, i-033 a i-037).

## Conversa 3 — chat: conveniências de uso (WO 0017)

### Objetivo do dia
Transformar a nota do dono `261029-1106.txt` e a i-037 numa frente só, com as decisões dele (D1 a D5).

### Feito
- Relatórios da WO 0016 (`6a52111`) e do `/wrap` (`74d75f9`) conferidos contra o `git log`.
- Spec `meta/specs/261029-conveniencias-de-uso.md`, decidida pelo dono: D1 sim, D2 completa, D3 some, D4 sim (com o JSON em bloco de código como alternativa — refinamento dele), D5 segue a tela.
- Implementado numa cópia e testado em Chromium headless contra a 0.8.0: 34 de 34 `[medido por instrumento]`. Padrão byte a byte igual ao da 0.8.0 nos três acervos.
- Prompt: a «Saída» pede arquivo e, sem arquivo, bloco de código; a importação tolera a resposta colada inteira e avisa.
- DEC-024: a linha `/apply-wo` passa para antes do «Próximo» (CEREBRO e Instruções).
- Álbuns antigos chegaram à pasta-pai: medidos (19 arquivos, ~44 mil linhas), não lidos.
- WO 0017 escrita.

### Decisões
DEC-022 (acervo guardado no navegador, amplia a DEC-004), DEC-023 (estrutura do cartão, export, prompt em arquivo/bloco), DEC-024 (lugar do `/apply-wo` no fecho).

### Bugs
Nenhum.

### Aprendizados / armadilhas
- Regra que vive só num documento derivado (o brief) não é regra do projeto — ninguém a revisa, e ela dirige o comportamento do mesmo jeito. Achada ao procurar onde mudar o fecho: o repo não tinha a regra.
- «Mostrar/ocultar» precisa de padrão idêntico ao de antes, senão quem não mexe vê o app mudar: os módulos viraram bloco próprio só para isso.
- O toast fica atrás de um `<dialog>` modal (0.8.0); a janela da estrutura não precisa de status próprio porque a mudança aparece nos cartões atrás dela.

### Onde parei
WO 0017 entregue. Falta a tela e o reteste curto do prompt (roteiro do dono).

### Próximos passos
Aplicar a WO 0017; colar as Instruções novas no painel; roteiro do dono; fechar a 0.9.0. Depois, a i-008 com os álbuns que chegaram.
````

## Edicao E43 — STATUS inteiro — `meta/STATUS.md`

Sem ancora: substitua o arquivo inteiro. **O que saiu e para onde foi:** o bloco «Ultima conversa» do fecho da
0.8.0 (esta no CHANGELOG [0.8.0] e no log de 2026-10-29); a pendencia «trazer os albuns antigos» (feita — i-008
desbloqueada); os itens 1 e 2 do backlog (viraram esta WO). Entraram: «Em progresso» das conveniencias, as
pendencias de colar as Instrucoes e do roteiro, a nota do navegador e a correcao da linha do Export MD.

````
# STATUS.md — Cancioneiro

> **O agora.** O que funciona, o que está em progresso, o que está quebrado, backlog curto.
> Rolante: item resolvido sai daqui e vai para o CHANGELOG. Médio/longo prazo vive no ROADMAP.

**Versão atual:** 0.8.0 · **Fase:** 3a, 3a.2, o BPM da 3b e o prompt-modelo concluídos · conveniências de uso aplicadas (WO 0017), à espera da tela e do reteste curto do prompt · Fase 2 com i-008 desbloqueada

---

## Última conversa (2026-10-29, conveniências de uso)

- **Decisões do dono** sobre a nota `261029-1106.txt`: D1 acervo guardado no navegador, D2 estrutura do cartão completa, D3 aviso de negação some com o Exclude oculto, D4 prompt pede arquivo (e, sem arquivo, o JSON em bloco de código), D5 export de álbum segue a tela. Spec `meta/specs/261029-conveniencias-de-uso.md`; DEC-022 e DEC-023; aplicadas pela WO 0017, testadas pelo chat numa cópia (34 de 34).
- **Fecho do chat (DEC-024):** a linha `/apply-wo` vem antes do «Próximo». CEREBRO e Instruções mudaram — o dono cola as Instruções novas no painel do Projeto.
- **Álbuns antigos chegaram** à pasta-pai (`../Album Rainha da Preguiça/`, `../Albuns/`, 19 arquivos, ~44 mil linhas): a i-008 está desbloqueada; ainda não lidos.
- **Este bloco substitui o anterior, de 2026-10-29, que fechava a 0.8.0.** O que ele dizia está no CHANGELOG [0.8.0], na spec do prompt-modelo e em `logs/2026-10-29.md`.

## Funciona (pronto)

- **Ferramenta `app/index.html`:** importa/carrega JSON, cartões por álbum, copiar Style/Lyrics/Exclude por botão (o botão entrega o texto que está na tela — FIX-007), marca «usei», filtros por álbum/estado/uso, busca, módulos de estilo que recompõem o Style ao vivo, variantes e notas recolhíveis, «Baixar .json» limpo e «Importar .json» que saneia chaves internas e diz quantas removeu (FIX-004/006). A versão aparece no cabeçalho. A importação avisa quantos módulos citados não existem na coleção (FIX-009).
- **Painel de qualidade (0.5.0, DEC-018):** linha abaixo de Style, Lyrics e Exclude com caracteres contra o limite do campo, tags do Style e negações «no X». Vermelho só para truncamento.
- **Custo de cada módulo no chip (0.6.0, DEC-019):** com o painel de módulos aberto, cada chip mostra `−N`, `+N` ou `0` tags; a linha de qualidade diz quanto o style base usa sozinho quando o recomposto passa de 10.
- **Controle de BPM no cartão (0.7.0, DEC-020):** campo 20-300 com `−5`/`+5` e «voltar a N» governa todo «NN bpm» do Style principal; o chip de andamento é atalho (no máximo um ligado); variantes e «Baixar .json» não mudam; o valor é só da sessão.
- **Esquema JSON canônico** (`schema/`). Biblioteca de referência para autoria em `schema/style-modules.json` (27 módulos, sete camadas); cada acervo traz os seus (DEC-016).
- **Datasets:** `data/exemplo-cinzeiro.json` (1 faixa, com os 5 módulos que cita) e `data/demo.json` (2 álbuns, 3 faixas). O álbum de referências do dono mora fora do repo, em `../album-referencias (1).json` (7 faixas, 50 módulos).
- **Validação** (`scripts/validate.py`): sintaxe, esquema (com `jsonschema`), integridade referencial dos módulos (id ausente ou objeto no lugar do id, sem traceback — FIX-009), versão igual nos quatro lugares, um BPM só por faixa (DEC-020) e as marcações do prompt que o app lê (DEC-021); código 1 se falhar; a última linha diz se o esquema foi de fato conferido.
- **Export MD** (faixa / álbum / acervo), com o rótulo fora do bloco. Na 0.8.0 a faixa sai com o Style recomposto e álbum/acervo com o `style` base; a WO 0017 faz os três seguirem a tela (D5, à espera da conferência).
- **Prompt-modelo** (`schema/PROMPT-PARA-CHATS.md`, DEC-021): contrato de módulo, style com 6 a 8 tags e até 10 com os módulos ligados. Retestado em 2026-10-29: 6 de 6 faixas dentro do contrato e do orçamento.
- **Botões «Prompt para chats» e «Baixar exemplo»** (0.8.0, DEC-021): buscam o prompt e o `data/demo.json` do repositório no clique; a janela do prompt recebe o «Meu pedido».
- **Publicado no GitHub Pages** em `https://joaolucas-nds.github.io/cancioneiro/app/index.html` — o push em `main` publica.

## Em progresso

- **Conveniências de uso (DEC-022, DEC-023; i-030, i-033 a i-037)** — aplicadas pela WO 0017. Falta: (1) a conferência na tela, no app publicado; (2) o reteste curto do prompt (só a «Saída» mudou). Com os dois, fecha a 0.9.0 (CHANGELOG, README já descreve).
  - «Estrutura do cartão» (ordem e mostrar/ocultar de 6 blocos, no navegador; padrão = ordem antiga); «copiar título»; arrastar o `.json` para a tela; o último acervo importado volta ao abrir, com a origem e «esquecer» na barra; export de álbum e acervo com o Style da tela.
  - Prompt: pede um `.json` para baixar; sem arquivo, o JSON num único bloco de código. A importação aceita a resposta colada inteira e avisa que extraiu.

## Quebrado / pendências que travam

- (nada quebrado)

## Pendências do dono

- **Colar as Instruções novas no painel do Projeto** — `INSTRUCOES-DO-PROJETO.md` mudou na WO 0017 (DEC-024).
- **Conferir na tela e retestar o prompt** — roteiro entregue pelo chat na conversa de 2026-10-29, depois do push da WO 0017.
- **Instalar o validador de esquema nesta máquina.** Sem `jsonschema` e `referencing`, o `validate.py` só confere sintaxe e diz `ESQUEMA NAO CONFERIDO` na última linha. Uma vez, no CMD: `pip install jsonschema referencing --break-system-packages`. Depois, `python3 scripts/validate.py` deve terminar em `Tudo conforme ao esquema.`

## Backlog curto (próximas ações concretas)

1. **Fechar as conveniências** na 0.9.0, depois do roteiro do dono.
2. **Converter os álbuns antigos** (i-008) — chegaram em 2026-10-29; começar por medir o formato deles (sonda) e converter um.
3. **Pesquisar outras plataformas de música por IA** (i-032) — um turno de pesquisa antes de qualquer mudança de esquema.
4. **Avisar palavra de andamento que contradiz o BPM** (i-029) — pede uma tabela palavra → faixa de BPM, com fonte e data.
5. **Importar prompts prontos dos álbuns como módulos** — o último ⬜ da 3b no ROADMAP; combina com a 2.

## Notas de estado

- **Repo local do dono:** `C:\Users\alexk\Tools\cancioneiro\cancioneiro` (Windows). O chat lê e grava na pasta vinculada; commit e push são do Code (DEC-010). A pasta-pai guarda relatórios, notas e o acervo do dono, fora do Git; o lido vai para `../notas-arquivadas/`.
- **Canal:** pasta vinculada é o padrão; a cópia achatada (FlatDrop) é reserva (DEC-017).
- **Limites do Suno:** o v6 saiu em 2026-09-09 e a nota oficial não documenta limite de campo; os números do painel vêm de fonte secundária, com fonte e data no `QUALITY_LIMITS` (DEC-018). Outra fonte secundária (2026-08) põe o ideal em 4 a 7 descritores; o prompt usa 6 a 8. Reconferir quando houver documentação oficial. O `meta/HISTORY.md` §5 ganhou a interface do v6 vista na conta (2026-10-29); o resto do arquivo ainda descreve o v5.5.
- **Exclude no v6-mini:** o formulário gratuito não tem o campo (capturas de 2026-10-29). Com a WO 0017, o bloco pode ser ocultado em «Estrutura do cartão», e o aviso «no X → Exclude» some junto (D3); o dado continua no JSON.
- **Navegador (DEC-004, DEC-022):** guarda as marcas «usei», a estrutura do cartão e a cópia do último acervo importado. A cópia é cache: se o arquivo mudou fora, importe de novo; a linha de origem diz quando a cópia foi feita.
- **Botões de prompt e exemplo:** dependem de rede e do Pages. No `file://`, só funcionam se o Pages aceitar o `fetch` de uma página local — não conferido (o dono abriu o `file://` em 2026-10-29, sem relatar o resultado do botão); sem isso, a janela mostra o link para a versão publicada (DEC-021).
- **Estado de sessão** (módulos ligados e BPM escolhido) sobrevive a filtro, busca e «marcar usei»; volta ao acervo ao recarregar a página ou importar de novo (FIX-008, DEC-020).
- **Limite conhecido:** `tryAutoLoad` (carregamento automático pelo Pages) não saneia chaves internas — só a importação por arquivo faz isso. Inócuo enquanto nenhum acervo contaminado for para `data/`.
- **Pendência de contexto — ASU:** o dono perguntou se o «modo ASU» do KCM seria melhor que o modo Code para este projeto; ficou pendente até ele trazer a descrição do ASU `[relatado pelo dono, sem material de apoio]`.
- Design: na recomposição do Style a base manda — desligar um módulo não remove o que já está no style base; módulos só somam. O dedup compara sequências de palavras (FIX-003). Os módulos de gênero e de andamento costumam custar 0 tag por isso (DEC-019). O chip de andamento é atalho do controle de BPM, no máximo um ligado (DEC-020).
````

## Edicao E44 — spec, arquivo novo — `meta/specs/261029-conveniencias-de-uso.md`

Sem ancora: crie o arquivo com o bloco abaixo.

````
# SPEC — Conveniências de uso: estrutura do cartão, título, arrastar, acervo no navegador, prompt em arquivo

> **Status:** Decidida
> **Decidida em:** 2026-10-29 pelo dono — **D1 sim, D2 completa, D3 some, D4 sim, D5 segue a tela**; na D4,
> a alternativa ao arquivo é o JSON **dentro de um bloco de código** (refinamento do dono, mesma mensagem).
> Aplicação: `meta/workorders/261029-wo0017-conveniencias-de-uso.md`.
> **Data:** 2026-10-29 (data de criação; não muda depois)
> **Ideias de origem:** i-030, i-033, i-034, i-035, i-036 (nota do dono `261029-1106.txt`) e i-037 (achada nos
> `.md` exportados). Decisões propostas no turno de 2026-10-29 e respondidas na mensagem seguinte.
> **Depende de:** 0.8.0 (DEC-021). Toca a DEC-004 (navegador) — ver DEC-022.

---

## Problema

A nota do dono de 2026-10-29 junta atritos de uso, medidos nas capturas da conta dele:

1. **O título não se copia.** O formulário do v6 tem campo de título (o último, antes de «Save to»).
2. **A ordem do cartão é fixa.** Título → Style → Lyrics serve a quem preenche o Suno de baixo para cima (o
   dono faz assim), mas ele quer controlar a estrutura e guardar a escolha, com a ordem atual como padrão.
3. **O Exclude não tem destino na conta dele:** o formulário do v6-mini gratuito não tem o campo. O bloco e o
   aviso «no X → Exclude» do painel mandam para um campo que não existe ali.
4. **Carregar exige o botão e o seletor de arquivo**, e **o acervo some ao fechar o navegador** — só as marcas
   «usei» sobrevivem.
5. **A resposta do chat vem como texto para copiar** e colar no Bloco de notas.
6. **O export de álbum/acervo saía com o `style` base**, o de faixa com o recomposto (i-037) — sem estar escrito.

## Decisões

**D1 — Acervo guardado no navegador (i-035) → DEC-022.** O último acervo **importado** (botão ou arrastar) fica
numa cópia no `localStorage` e volta ao abrir. É cache, não fonte (DEC-004 segue): o app nunca edita o acervo
(FIX-004), então a cópia é igual ao arquivo. Contra o risco de a cópia ficar velha sem ninguém ver, uma **linha de
origem** na barra de controles diz de onde veio e quando («Acervo importado de X em dd/mm/aaaa hh:mm · guardado
neste navegador») e tem o botão **«esquecer»**. A cópia vence a carga automática do Pages; esquecer volta a ela.
Se o navegador recusar (cota, modo privado), importa assim mesmo e o toast avisa.

**D2 — Estrutura do cartão completa (i-030) → DEC-023.** Botão «Estrutura do cartão» abre uma janela com os seis
blocos — Style, Lyrics, Exclude, Módulos, Variantes, Notas —, cada um com «mostrar» e ↑/↓, mais «Restaurar
padrão». Vale para todos os cartões, guardado no navegador (`App.ui.layout`, estado de interface). **Escolhas
técnicas:** o título e a linha de metadados (BPM, tom, contexto) ficam sempre no topo; os módulos são bloco
próprio, para a ordem padrão ser **exatamente** a de antes; o export `.md` **não** segue a estrutura (é documento
do acervo, ordem fixa, e mostra tudo).

**D3 — Exclude oculto leva junto o aviso de negação.** Com o bloco Exclude oculto, a linha de qualidade deixa de
dizer ««no X»: mais confiável no campo Exclude». O dado continua no JSON.

**D4 — O prompt pede arquivo; a alternativa é bloco de código (i-036) → DEC-023.** A seção «Saída» passa a pedir um
`.json` para download com o nome do `id` do álbum; quem não puder criar arquivo responde com o JSON inteiro em
**um único bloco de código `json`**, sem texto fora. O botão de copiar do bloco entrega só o JSON. Rede de
segurança no app: se o arquivo importado não for JSON puro (resposta colada inteira), a importação extrai o
bloco de código — ou o trecho do primeiro `{` ao último `}` — e **diz no toast** que extraiu (FIX-006: limpar
calado apaga o sinal). Lixo continua recusado.

**D5 — Export de álbum e acervo segue a tela (i-037) → DEC-023.** `albumToMarkdown` passa a usar o Style
recomposto, como a faixa: módulos ligados e BPM do controle.

**Sem decisão do dono (técnico):** copiar o título (i-033) e arrastar o `.json` (i-034, mesmo caminho do botão:
saneamento, avisos, cópia guardada; só reage a arraste de arquivo).

## Critérios de aceite

Executados pelo chat em Chromium headless sobre o app de chegada, contra a 0.8.0 (`73e4a54f`):

- [x] Estrutura padrão: blocos, Style e linha de qualidade **iguais aos da 0.8.0** nos três acervos (7, 3 e 1 cartões).
- [x] «copiar título» copia só o título e mostra «copiado ✓».
- [x] A janela lista os seis blocos na ordem padrão; ↑ do primeiro e ↓ do último desabilitados.
- [x] Ocultar o Exclude o tira de todos os cartões; subir o Lyrics o põe acima do Style; o Style copiado não muda.
- [x] A estrutura sobrevive ao recarregar; «Restaurar padrão» volta à ordem da 0.8.0.
- [x] Recarregar traz o acervo importado, com toast «Acervo do navegador: …» e a linha de origem com data e «esquecer».
- [x] «esquecer» limpa a tela e a cópia; recarregar depois disso não traz o acervo.
- [x] Aviso «no drums» aparece com o Exclude visível e some com ele oculto (D3).
- [x] Com o Style oculto, clicar num chip não dá erro.
- [x] Arrastar um arquivo mostra «Solte o .json para importar»; soltar importa; arrastar texto é ignorado.
- [x] Resposta colada com cercas e texto em volta importa e avisa «JSON extraído de um bloco de código»; lixo é recusado; JSON limpo não avisa.
- [x] Export do álbum = Style da tela (18 tags em ar-01); export do acervo leva o BPM do controle (D5).
- [x] Navegador recusando a cópia: importa e avisa «não coube no navegador».
- [x] Servido por http: sem cópia, o demo carrega com origem «GitHub Pages»; com cópia, ela vence; «esquecer» traz o demo.
- [x] A janela do prompt continua abrindo; nenhum erro de página.
- [x] `validate.py` verde (as marcações do prompt seguem as mesmas).

**Resultado: 34 de 34.** Faltam, e são do dono: a tela real (layout, celular), o reteste do prompt (D4) com chats.

## Fora de escopo

- Mais de um acervo guardado ao mesmo tempo (a cópia é a do último importado).
- Guardar a estrutura ou o acervo fora do navegador (outro aparelho não vê).
- A i-008 (os álbuns antigos chegaram em 2026-10-29: frente própria).

## Riscos

- **Cópia velha:** o arquivo mudou e a cópia não. Mitigação: a linha de origem com data; importar de novo substitui.
- **`localStorage` no `file://`:** o Chrome guarda por arquivo local; outro navegador ou perfil não vê. Esperado.
- **O prompt mudou de novo:** o texto que passou no reteste de 2026-10-29 foi o anterior; esta mudança só toca a
  «Saída», mas exige reteste curto (roteiro do dono).
- **Toast longo:** o aviso do cache somado a outros pode passar de uma linha; dura até 6 s (0.8.0).
````

## Fora de escopo

- **CHANGELOG e a 0.9.0** — so depois da tela e do reteste, na proxima WO.
- **i-008** — os albuns chegaram, mas a conversao e frente propria.
- `data/`, `scripts/` e o esquema — nada muda.

## Armadilhas desta WO

- **Blocos com `## `, `### ` e com cercas de tres crases dentro** (DECISIONS, IDEAS, log, STATUS, spec; o regex
  `parseCollectionText` do app; o esqueleto do CEREBRO, que passa a usar `~~~` por fora): delimite pelas
  **quatro** crases.
- **JavaScript com barras invertidas** (`\s`, `\r?\n`, `/^\.\.\//`): copie literal; e o interpretador que as le.
- **A ultima linha do app troca `tryAutoLoad();` por `boot();`.** Sem ela, o acervo guardado nunca volta.
- **Fim de linha:** os arquivos sao LF. Se um hash de chegada divergir, rode `file <arquivo>` antes de concluir
  que uma edicao errou.

## Depois de aplicar — conferencia antes do commit

| # | Checagem | Comando | Esperado |
|---|---|---|---|
| 1 | **Os doze arquivos sao os testados** | `sha1sum app/index.html schema/PROMPT-PARA-CHATS.md meta/CEREBRO.md INSTRUCOES-DO-PROJETO.md README.md meta/CONTEXT.md meta/DECISIONS.md meta/IDEAS.md meta/ROADMAP.md logs/2026-10-29.md meta/STATUS.md meta/specs/261029-conveniencias-de-uso.md` | a coluna **chegada** do cabecalho, os doze. **Prova as 44 edicoes.** |
| 2 | As funcoes novas do app | `grep -cE 'function (parseCollectionText\|currentLayout\|isHidden\|saveLayout\|renderLayoutDialog\|saveCollectionCache\|loadCollectionCache\|fmtDate\|setOrigin\|forgetCollection\|boot)\b' app/index.html` | `11` |
| 3 | O boot novo e o export | `grep -c '^boot();$' app/index.html`, `grep -c '^tryAutoLoad();$' app/index.html`, `grep -c 'songToMarkdown(s, true)' app/index.html` | `1`, `0`, `1` |
| 4 | Prompt, Instrucoes e CEREBRO | `grep -c 'um único bloco de código' schema/PROMPT-PARA-CHATS.md`, `grep -c 'ANTES do «Próximo»' INSTRUCOES-DO-PROJETO.md`, `grep -c '^0\. \*\*Aplicar\*\*' meta/CEREBRO.md` | `1`, `1`, `1` |
| 5 | Os registros | `grep -cE '^## DEC-02[234] ' meta/DECISIONS.md`, `grep -cE '^### i-03[03-7] 🔨' meta/IDEAS.md`, `grep -c '^## Conversa 3' logs/2026-10-29.md` | `3`, `6`, `1` |
| 6 | Validacao passa | `python3 scripts/validate.py; echo "exit=$?"` | `exit=0`, com `OK  prompt com as marcacoes que o app le` e `OK  versao 0.8.0` |
| 7 | O album do dono tambem passa | `python3 scripts/validate.py "../album-referencias (1).json"; echo "exit=$?"` | `exit=0` |
| 8 | Nada de dados | `GIT_OPTIONAL_LOCKS=0 git status --short data scripts` | saida **vazia** |
| 9 | Nenhum relatorio `.txt` no repo | `GIT_OPTIONAL_LOCKS=0 git status --short \| grep -c '\.txt'` | `0` |
| 10 | Tamanho das Instrucoes | `wc -m INSTRUCOES-DO-PROJETO.md` | `6691` |

**Os tres campos de cada passo:** as dez sao rodadas por **quem aplica (o Code)**, na raiz do repo
(`C:\Users\alexk\Tools\cancioneiro\cancioneiro`), em Git Bash, com `LC_ALL=C.UTF-8`. **Chega no ramo?**
A checagem 1 cobre os doze arquivos inteiros, e o app de chegada foi executado pelo chat. **Esta e qual
pergunta?** As dez respondem «esta la?». A tela, o arrastar de verdade e o reteste do prompt vao no roteiro
que o chat entrega **no corpo da resposta**, nao aqui.

## Relatorio de aplicacao

Grave em `../261029-HHMM-code-cancioneiro-apply-wo0017.txt`, com o `HHMM` de `date +%y%m%d-%H%M` rodado na
hora. Diga o resultado da checagem 1 em primeiro lugar. A conferencia na tela, o reteste e colar as
Instrucoes no painel **nao sao seus**.

**Proximo comando** (ultima linha do relatorio, cru e sozinho):

```
/wrap
```

## Commit

```
git add app/index.html schema/PROMPT-PARA-CHATS.md meta/CEREBRO.md INSTRUCOES-DO-PROJETO.md README.md meta/CONTEXT.md meta/DECISIONS.md meta/IDEAS.md meta/ROADMAP.md logs/2026-10-29.md meta/STATUS.md meta/specs/261029-conveniencias-de-uso.md meta/workorders
```

```
git commit -m "feat: estrutura do cartao, copiar titulo, arrastar json, acervo guardado no navegador" -m "DEC-022: o ultimo acervo importado fica em cache no navegador e volta ao abrir, com origem, data e botao esquecer. DEC-023: estrutura do cartao configuravel (ordem e mostrar/ocultar, padrao igual ao anterior), aviso de negacao some com o Exclude oculto, copiar titulo, arrastar o json para importar, export de album e acervo com o Style da tela, prompt pede arquivo e, sem arquivo, o JSON em bloco de codigo, importacao extrai o JSON de resposta colada e avisa. DEC-024: no fecho do chat a linha apply-wo vem antes do Proximo (CEREBRO e Instrucoes)."
```

```
git push
```
