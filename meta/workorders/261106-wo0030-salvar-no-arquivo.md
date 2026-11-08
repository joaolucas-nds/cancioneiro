# WO 0030 — I4, salvar no arquivo (0.17.0)

## Cabecalho

> **Tipo:** mista — codigo (`app/index.html`, 24 edicoes) e registro (CHANGELOG, DECISIONS, IDEAS, ROADMAP, README e STATUS, 15 edicoes), mais o versionamento de tres arquivos que o chat gravou.
> **Config sugerida:** Sonnet · `/effort medium`.
> **Pre-requisito:** commit `a9efdef`, branch `main`, sincronizada com `origin/main`. O `git status --short` mostra exatamente: ` M logs/2026-11-06.md`, ` M meta/CONTEXT.md`, ` M meta/specs/261106-salvar-no-arquivo.md` e `?? meta/workorders/261106-wo0030-salvar-no-arquivo.md`.
> **Base:** spec `meta/specs/261106-salvar-no-arquivo.md` (os cinco pontos decididos pelo dono em 2026-11-06, como recomendados → DEC-033, inserida aqui). Implementada e testada pelo chat num clone de `a9efdef`: 14 de 14 criterios no Chromium headless (Resultado na spec).
> **Depende de:** WO 0029 (`24b1fc0`, wrap `a9efdef`).
>
> | arquivo | partida (sha1) | chegada (sha1) |
> |---|---|---|
> | `app/index.html` | `781f4997ce536e18dbefcac8e88433f9c6de59d4` | `9e2ebeb0eaf65dc623cb19db9b2b8e1b285db85e` |
> | `meta/CHANGELOG.md` | `6d4d0e197f88263d37f32b6a6bb7de0f7ba8159b` | `bae6d1ba77a1c63f96fd7e3ba031edcd5609ce67` |
> | `meta/DECISIONS.md` | `2cf7a23a9e23651da2fa847dc85b4a4145a661a3` | `47a83de61af150faadcc095f1ef580a7dc0d92e5` |
> | `meta/IDEAS.md` | `8b79aad07d745461d3b755d07d36aa98172f9202` | `b47de1dc4eeb9ce351defc19ba187aeecec9742e` |
> | `meta/ROADMAP.md` | `337d94523982a90ebf10b10cca89f2e9fafbd0b1` | `f6b41365beaada3223b3829d4ed15053b2a168fd` |
> | `README.md` | `9bf1ea484306a9003690d066b501ec2694476f71` | `acea877d8ae4979bfa8ee9d18af177d17649b25c` |
> | `meta/STATUS.md` | `ea2e69fbfaec3fe4a0b7848e0c1f8f8fda8fe9bf` | `3a5a1eae0f3fab5f98a783bb6b4b7fe26404133e` |
>
> **Arquivos que o chat gravou no disco e esta WO so versiona** (sha1 medido pelo chat ao gravar; partida = chegada):
>
> | arquivo | sha1 |
> |---|---|
> | `meta/CONTEXT.md` | `d18b2f545ded97d4f7385a9659591a59eee94032` |
> | `meta/specs/261106-salvar-no-arquivo.md` | `a194a8b637cd5f3044daa90fd00e51ce71fb94d2` |
> | `logs/2026-11-06.md` | `dd7ce511720a94581779957026ca442b66a474cc` |
>
> **Ancora semantica:** se um trecho-ancora nao bater EXATAMENTE, PARE e reporte.
> **Idempotencia:** antes de cada edicao, procure o texto NOVO INTEIRO; se ja estiver la, PULE e diga no relatorio.
> **Ancoras:** linhas inteiras (ou blocos de linhas inteiras), cada uma ocorrendo exatamente 1 vez no arquivo no estado em que a edicao e aplicada, na ordem abaixo. Toda edicao «substitui a ancora inteira»; nas que acrescentam, o texto novo repete a ancora no comeco ou no fim.
> **Âncoras lidas em** (todas lidas pelo chat NESTE turno, dos arquivos em `a9efdef` — o sha1 de partida acima, igual no disco do dono, conferido; o chat aplicou as 39 edicoes num clone e mediu o sha1 de chegada):
> - E01 (`app/index.html`, versao 0.17.0): linha `    <span class="version" data-role="app-version">v0.16.0</span>`
> - E02 (`app/index.html`, CSS do Salvar com o ▾ e da marca de salvo): linha `  .bar-draft button { height: 26px; }`
> - E03 (`app/index.html`, o ▾ e o menu de salvar na barra): linha `    <button type="button" class="btn-primary" id="draft-save" data-role="dirty-download" t…`
> - E04 (`app/index.html`, Desvincular no seletor de acervo): linha `      <button type="button" role="menuitem" id="forget-btn" class="danger" hidden>Esquecer…`
> - E05 (`app/index.html`, a nota do vinculo no seletor de acervo): linha `      <p class="pop-note" id="origin"></p>`
> - E06 (`app/index.html`, a janela de tres saidas): linha `<dialog class="prompt-dialog" id="move-dialog" aria-labelledby="move-dialog-title">`
> - E07 (`app/index.html`, importFromFile recebe o vinculo): linha `function importFromFile(file) {`
> - E08 (`app/index.html`, importar guarda o vinculo): linha `      const r = await saveAcervo(json, file.name);`
> - E09 (`app/index.html`, importar abre com o vinculo): linha `      App.saved = r.ok; App.changes = 0; App.savedAt = r.savedAt; App.editedAt = null; App…`
> - E10 (`app/index.html`, baixar com vinculo e so copia; a volta fica): linha `  downloadFile(name, JSON.stringify(App.collection, null, 2), "application/json");`
> - E11 (`app/index.html`, guardar o acervo com o vinculo): linha `async function saveAcervo(json, source) {`
> - E12 (`app/index.html`, o registro leva o vinculo): linha `  try { await dbPut({ source, title: json.title || source, savedAt, json }); }`
> - E13 (`app/index.html`, abrir um acervo guardado traz o vinculo): linha `  App.editedAt = rec.editedAt || null; App.unsavedInMemory = false;`
> - E14 (`app/index.html`, esquecer o ultimo acervo limpa o vinculo): linha `  App.saved = false; App.changes = 0; App.originText = ""; App.unsavedInMemory = false;`
> - E15 (`app/index.html`, gravar o rascunho preserva o vinculo): linha `                editedAt: App.editedAt, changes: App.changes, json: App.collection };`
> - E16 (`app/index.html`, a barra: Salvar, o ▾, a marca e a nota do vinculo): linha `  const dirty = App.saved && App.changes > 0;`
> - E17 (`app/index.html`, o menu de salvar entre os paineis da barra): linha `  mais: ["more-btn", "more-pop"],`
> - E18 (`app/index.html`, item do menu de salvar fecha o painel): linha `["acervo-pop", "more-pop"].forEach(id => document.getElementById(id).addEventListener("cli…`
> - E19 (`app/index.html`, os botoes de salvar): linha `document.getElementById("draft-save").addEventListener("click", () => downloadCollection()…`
> - E20 (`app/index.html`, Importar pelo «⋯» passa pela janela do sistema): linha `document.getElementById("menu-import").addEventListener("click", () => document.getElement…`
> - E21 (`app/index.html`, Importar pelo seletor passa pela janela do sistema): linha `document.getElementById("import-btn").addEventListener("click", () =>`
> - E22 (`app/index.html`, soltar o arquivo traz o vinculo): linha `  if (f && alb && App.saved) readTracksFile(f, alb.id);`
> - E23 (`app/index.html`, Ctrl+S salva): linha `  if ((e.ctrlKey || e.metaKey) && !e.altKey && !e.shiftKey && e.key.toLowerCase() === "z")…`
> - E24 (`app/index.html`, o bloco da I4): linha `// A abertura e assincrona (IndexedDB); a importacao espera por ela.`
> - E25 (`meta/CHANGELOG.md`, entrada [0.17.0]): linha `## [0.16.0] — 2026-11-06`
> - E26 (`meta/DECISIONS.md`, DEC-033 no fim): linha `**Consequências:** (+) Organizar fica sempre à mão, sem o interruptor, com um caminho sem …`
> - E27 (`meta/IDEAS.md`, i-043 entregue (titulo)): linha `### i-043 💡 Gravar direto no arquivo do acervo (File System Access)`
> - E28 (`meta/IDEAS.md`, i-043 entregue (linha nova)): linha `**Planejada (DEC-030):** é a I4 da frente de interface (0.17.0), depois de a I3 deixar o «…`
> - E29 (`meta/IDEAS.md`, i-051 nova): linha `[relatado pelo dono, 2026-11-05, na i-048] Soltar uma faixa sobre outro acervo da latera…`
> - E30 (`meta/ROADMAP.md`, frente de interface concluida): linha `- 🔨 Frente de interface (i-043 a i-048, DEC-030), em quatro entregas: ✅ barra única, com o…`
> - E31 (`README.md`, estado v0.17.0): linha `> **Estado:** v0.16.0 — ferramenta em uso. Lê, guarda e edita vários acervos, copia por ca…`
> - E32 (`README.md`, passo 7: salvar no arquivo (e sem a sobra da 0.13.0)): linha `7. Para reorganizar, não há nada a ligar: na Lista, arraste a faixa pela alça ⋮⋮ (para out…`
> - E33 (`README.md`, a copia e o arquivo): linha `O acervo canônico são **arquivos JSON** no esquema: os exemplos versionados em data/, e …`
> - E34 (`meta/STATUS.md`, versao e fase): linha `**Versão atual:** 0.16.0 · **Fase:** 3a, 3a.2, o BPM da 3b, o prompt-modelo e as conveniên…`
> - E35 (`meta/STATUS.md`, ultima conversa): linha `## Última conversa (2026-11-06, I3: protótipo, spec e implementação, WO 0027)`
> - E36 (`meta/STATUS.md`, funciona: salvar no arquivo): linha `- **Organizar** (0.16.0, DEC-030, DEC-032): arrastar pela alça ⋮⋮ na Lista (com filtro, an…`
> - E37 (`meta/STATUS.md`, pendencias do dono): linha `- **Rodar a sonda da I4 e decidir os cinco pontos** — abrir ..\261106-sonda-i4-salvar.htm…`
> - E38 (`meta/STATUS.md`, backlog): linha `1. **I4 — Salvar no arquivo** (i-043, DEC-030) — protótipo e spec prontos (meta/specs/261…`
> - E39 (`meta/STATUS.md`, nota do rascunho): linha `- **Rascunho (DEC-028, DEC-029, DEC-032):** com alterações, a cópia guardada está à frente…`
> **Canal dos meta neste ciclo = CODE:** CHANGELOG, DECISIONS, STATUS sao do Code (DEC-010); IDEAS, ROADMAP e README mudam por esta WO; CONTEXT, a spec e o log do chat ja estao gravados.

---

## 1. Por que

A I4 da frente de interface (DEC-030): «Salvar» grava no proprio `.json` onde o navegador deixa (Chrome e Edge no
computador), com o acervo vinculado ao arquivo no IndexedDB; Firefox, Safari e o celular continuam baixando. Fecha a
i-043 e a frente de interface. Versao 0.17.0.

## Armadilhas

- **Copie cada bloco por script ou pelo Edit, nunca redigitando.** Os blocos tem aspas «», travessoes, ✓, ▾ e ⋯; um caractere trocado muda o sha1 de chegada.
- **`</script` nao aparece em nenhum texto novo** (ele fecharia o `<script>` do app). Se aparecer depois de aplicar, PARE.
- **A E24 (o bloco da I4) (`"\n"`)**: dentro do JS o texto e barra invertida + n, entre aspas duplas. Nao troque por quebra de linha real.
- **IDEAS com emoji (💡, ✅) no titulo:** o Edit casa o texto inteiro; nas checagens, procure pelo numero (`^### i-051 `), nunca pelo emoji (Git Bash).
- **CRLF:** o dono tem `autocrlf=true`; os sha1 de chegada sao do arquivo em LF, como no checkout de hoje (`git ls-files --eol` mostra `w/lf`). Se `sha1sum` divergir so por fim de linha, relate e confira com `git diff --stat`.

## Edicao 0 — Conferencia de hash e de arvore

```
sha1sum app/index.html meta/CHANGELOG.md meta/DECISIONS.md meta/IDEAS.md meta/ROADMAP.md README.md meta/STATUS.md meta/CONTEXT.md meta/specs/261106-salvar-no-arquivo.md logs/2026-11-06.md
GIT_OPTIONAL_LOCKS=0 git status --short
```

Os sete da primeira tabela batem com **partida**, os tres da segunda com o sha1 dela; o `git status` mostra exatamente as quatro linhas do Pre-requisito. Qualquer outra coisa: **PARE e reporte**.

## Edicoes E01 a E39

Na ordem. Copie o que esta ENTRE as linhas de quatro crases, sem elas. Cada edicao diz o arquivo.

### E01 — versao 0.17.0

**Arquivo:** `app/index.html`

**Ancora:**

````
    <span class="version" data-role="app-version">v0.16.0</span>
````

**Texto novo (substitui a ancora inteira):**

````
    <span class="version" data-role="app-version">v0.17.0</span>
````

### E02 — CSS do Salvar com o ▾ e da marca de salvo

**Arquivo:** `app/index.html`

**Ancora:**

````
  .bar-draft button { height: 26px; }
````

**Texto novo (substitui a ancora inteira):**

````
  .bar-draft button { height: 26px; }
  /* I4: «Salvar» com o ▾ colado (Salvar em outro arquivo…, Baixar .json) e, depois de
     gravar no arquivo, a marca «✓ Salvo no arquivo às HH:MM», sem o fundo de rascunho. */
  #save-wrap { margin-left: -8px; }
  #draft-save:has(+ #save-wrap:not([hidden])) { border-radius: 6px 0 0 6px; }
  #draft-more { width: 24px; padding: 0; display: inline-flex; align-items: center; justify-content: center;
    border-radius: 0 6px 6px 0; border-left: 1px solid rgba(255,255,255,.4); }
  #draft-more svg { width: 10px; height: 10px; fill: none; stroke: currentColor; stroke-width: 1.6; stroke-linecap: round; }
  .bar-draft.is-saved { background: transparent; border: 1px solid var(--line); color: var(--moss); }
  .bar-draft.is-saved .dot, .bar-draft.is-saved #draft-save { display: none; }
  .bar-draft.is-saved #save-wrap { margin-left: 0; }
  .bar-draft.is-saved #draft-more { background: transparent; border: 0; border-radius: 6px; color: var(--ink-soft); }
  #save-pop { width: 300px; }
  #save-pop .sub { display: block; font-size: 12px; color: var(--ink-soft); }
  #save-pop kbd { float: right; font-family: inherit; font-size: 12px; color: var(--ink-soft); }
````

### E03 — o ▾ e o menu de salvar na barra

**Arquivo:** `app/index.html`

**Ancora:**

````
    <button type="button" class="btn-primary" id="draft-save" data-role="dirty-download" title="Baixa o acervo com as alterações, com o nome do arquivo de origem.">Salvar .json</button>
````

**Texto novo (substitui a ancora inteira):**

````
    <button type="button" class="btn-primary" id="draft-save" data-role="dirty-download" title="Baixa o acervo com as alterações, com o nome do arquivo de origem.">Salvar .json</button>
    <!-- I4: o ▾ ao lado de «Salvar», so onde o app grava direto no arquivo. -->
    <div class="pop-wrap" id="save-wrap" hidden>
      <button type="button" class="btn-primary" id="draft-more" aria-label="Outras formas de salvar" aria-haspopup="menu" aria-expanded="false" aria-controls="save-pop"><svg viewBox="0 0 12 12" aria-hidden="true"><path d="M3 4.5 6 7.5 9 4.5"/></svg></button>
      <div class="pop pop-right" id="save-pop" role="menu" aria-label="Salvar" hidden>
        <button type="button" role="menuitem" id="save-file">Salvar no arquivo <kbd>Ctrl+S</kbd></button>
        <button type="button" role="menuitem" id="save-as">Salvar em outro arquivo…</button>
        <button type="button" role="menuitem" id="save-download">Baixar .json<span class="sub">uma cópia em Downloads; o arquivo vinculado não muda</span></button>
      </div>
    </div>
````

### E04 — Desvincular no seletor de acervo

**Arquivo:** `app/index.html`

**Ancora:**

````
      <button type="button" role="menuitem" id="forget-btn" class="danger" hidden>Esquecer este acervo</button>
````

**Texto novo (substitui a ancora inteira):**

````
      <button type="button" role="menuitem" id="unlink-btn" hidden>Desvincular do arquivo</button>
      <button type="button" role="menuitem" id="forget-btn" class="danger" hidden>Esquecer este acervo</button>
````

### E05 — a nota do vinculo no seletor de acervo

**Arquivo:** `app/index.html`

**Ancora:**

````
      <p class="pop-note" id="origin"></p>
````

**Texto novo (substitui a ancora inteira):**

````
      <p class="pop-note" id="origin"></p>
      <p class="pop-note" id="link-note" hidden></p>
````

### E06 — a janela de tres saidas

**Arquivo:** `app/index.html`

**Ancora:**

````
<dialog class="prompt-dialog" id="move-dialog" aria-labelledby="move-dialog-title">
````

**Texto novo (substitui a ancora inteira):**

````
<!-- I4: escolha entre varias saidas (o arquivo mudou fora do app, ou sumiu). -->
<dialog class="prompt-dialog" id="choice-dialog" aria-labelledby="choice-text">
  <p id="choice-text"></p>
  <div class="dialog-actions" id="choice-actions"></div>
</dialog>

<dialog class="prompt-dialog" id="move-dialog" aria-labelledby="move-dialog-title">
````

### E07 — importFromFile recebe o vinculo

**Arquivo:** `app/index.html`

**Ancora:**

````
function importFromFile(file) {
````

**Texto novo (substitui a ancora inteira):**

````
/** Importa um acervo. Com `handle` (aberto pela janela do sistema ou solto, no
    Chrome), o acervo ja nasce vinculado ao arquivo (I4). */
function importFromFile(file, handle) {
````

### E08 — importar guarda o vinculo

**Arquivo:** `app/index.html`

**Ancora:**

````
      const r = await saveAcervo(json, file.name);
````

**Texto novo (substitui a ancora inteira):**

````
      // I4: o vinculo e a marca do arquivo como foi lido (data e tamanho).
      const link = handle && Store.db ? { handle, stamp: { lastModified: file.lastModified, size: file.size } } : null;
      const r = await saveAcervo(json, file.name, link);
````

### E09 — importar abre com o vinculo

**Arquivo:** `app/index.html`

**Ancora:**

````
      App.saved = r.ok; App.changes = 0; App.savedAt = r.savedAt; App.editedAt = null; App.unsavedInMemory = false;
````

**Texto novo (substitui a ancora inteira):**

````
      App.saved = r.ok; App.changes = 0; App.savedAt = r.savedAt; App.editedAt = null; App.unsavedInMemory = false;
      App.link = r.ok ? link : null; App.lastWrite = null;
````

### E10 — baixar com vinculo e so copia; a volta fica

**Arquivo:** `app/index.html`

**Ancora:**

````
  downloadFile(name, JSON.stringify(App.collection, null, 2), "application/json");
  if (!App.saved) return;
  App.undo = null;   // I3: depois de salvar, a volta nao vale mais
  App.changes = 0;
````

**Texto novo (substitui a ancora inteira):**

````
  downloadFile(name, JSON.stringify(App.collection, null, 2), "application/json");
  if (!App.saved) return;
  // I4: com o acervo vinculado a um arquivo, baixar e so uma copia: o arquivo
  // vinculado nao mudou, entao o rascunho continua a frente dele.
  if (App.link && canWriteFile()) {
    toast("Baixado em Downloads como " + name + ". O arquivo vinculado (" + App.link.handle.name + ") não mudou.");
    return;
  }
  keepUndoAfterSave();   // I4 (DEC-033): a volta continua valendo depois de salvar
  App.changes = 0;
````

### E11 — guardar o acervo com o vinculo

**Arquivo:** `app/index.html`

**Ancora:**

````
async function saveAcervo(json, source) {
````

**Texto novo (substitui a ancora inteira):**

````
async function saveAcervo(json, source, link) {
````

### E12 — o registro leva o vinculo

**Arquivo:** `app/index.html`

**Ancora:**

````
  try { await dbPut({ source, title: json.title || source, savedAt, json }); }
````

**Texto novo (substitui a ancora inteira):**

````
  const rec = { source, title: json.title || source, savedAt, json };
  if (link) { rec.fileHandle = link.handle; rec.fileStamp = link.stamp; }   // I4: o vinculo com o arquivo
  try { await dbPut(rec); }
````

### E13 — abrir um acervo guardado traz o vinculo

**Arquivo:** `app/index.html`

**Ancora:**

````
  App.editedAt = rec.editedAt || null; App.unsavedInMemory = false;
````

**Texto novo (substitui a ancora inteira):**

````
  App.editedAt = rec.editedAt || null; App.unsavedInMemory = false;
  App.link = rec.fileHandle ? { handle: rec.fileHandle, stamp: rec.fileStamp || null } : null;   // I4
  App.lastWrite = null;
````

### E14 — esquecer o ultimo acervo limpa o vinculo

**Arquivo:** `app/index.html`

**Ancora:**

````
  App.saved = false; App.changes = 0; App.originText = ""; App.unsavedInMemory = false;
````

**Texto novo (substitui a ancora inteira):**

````
  App.saved = false; App.changes = 0; App.originText = ""; App.unsavedInMemory = false;
  App.link = null; App.lastWrite = null;   // I4
````

### E15 — gravar o rascunho preserva o vinculo

**Arquivo:** `app/index.html`

**Ancora:**

````
                editedAt: App.editedAt, changes: App.changes, json: App.collection };
````

**Texto novo (substitui a ancora inteira):**

````
                editedAt: App.editedAt, changes: App.changes, json: App.collection };
  // I4: o vinculo com o arquivo mora no mesmo registro; sem ele aqui, gravar o rascunho o apagaria.
  if (App.link) { rec.fileHandle = App.link.handle; rec.fileStamp = App.link.stamp; }
````

### E16 — a barra: Salvar, o ▾, a marca e a nota do vinculo

**Arquivo:** `app/index.html`

**Ancora:**

````
  const dirty = App.saved && App.changes > 0;
  document.getElementById("bar-draft").hidden = !dirty;
  document.body.classList.toggle("has-draft", dirty);
  document.getElementById("draft-text").textContent =
    dirty ? nPlural(App.changes, "alteração não salva", "alterações não salvas") : "";
````

**Texto novo (substitui a ancora inteira):**

````
  const dirty = App.saved && App.changes > 0;
  // I4: onde o app grava direto, «Salvar» com o ▾ e, depois de gravar, a marca de salvo.
  const direct = App.saved && canWriteFile();
  const savedMark = direct && !dirty && !!App.lastWrite;
  const bar = document.getElementById("bar-draft");
  bar.hidden = !(dirty || savedMark);
  bar.classList.toggle("is-saved", savedMark);
  document.body.classList.toggle("has-draft", dirty);
  document.getElementById("draft-text").textContent =
    dirty ? nPlural(App.changes, "alteração não salva", "alterações não salvas")
    : savedMark ? "✓ Salvo no arquivo às " + App.lastWrite : "";
  const save = document.getElementById("draft-save");
  save.textContent = direct ? "Salvar" : "Salvar .json";
  save.title = !direct ? "Baixa o acervo com as alterações, com o nome do arquivo de origem."
    : App.link ? "Grava em " + App.link.handle.name + " (Ctrl+S)"
    : "Escolha o arquivo do acervo uma vez; depois o app grava direto nele (Ctrl+S)";
  document.getElementById("save-wrap").hidden = !direct;
  document.getElementById("unlink-btn").hidden = !(direct && App.link);
  const note = document.getElementById("link-note");
  note.hidden = !App.saved;
  note.textContent = !App.saved ? "" : direct
    ? (App.link ? "Vinculado a " + App.link.handle.name + ": «Salvar» grava nele."
       : "Sem vínculo com o arquivo: o primeiro «Salvar» pede o arquivo e vincula.")
    : (fileApi() ? "No celular, «Salvar .json» baixa uma cópia."
       : "Este navegador não grava direto no arquivo: «Salvar .json» baixa uma cópia.");
````

### E17 — o menu de salvar entre os paineis da barra

**Arquivo:** `app/index.html`

**Ancora:**

````
  mais: ["more-btn", "more-pop"],
````

**Texto novo (substitui a ancora inteira):**

````
  mais: ["more-btn", "more-pop"],
  salvar: ["draft-more", "save-pop"],   // I4
````

### E18 — item do menu de salvar fecha o painel

**Arquivo:** `app/index.html`

**Ancora:**

````
["acervo-pop", "more-pop"].forEach(id => document.getElementById(id).addEventListener("click", e => {
````

**Texto novo (substitui a ancora inteira):**

````
["acervo-pop", "more-pop", "save-pop"].forEach(id => document.getElementById(id).addEventListener("click", e => {
````

### E19 — os botoes de salvar

**Arquivo:** `app/index.html`

**Ancora:**

````
document.getElementById("draft-save").addEventListener("click", () => downloadCollection());
````

**Texto novo (substitui a ancora inteira):**

````
document.getElementById("draft-save").addEventListener("click", () => saveDraft());
// I4: o ▾ de salvar e os itens dele; desvincular mora no seletor de acervo.
document.getElementById("draft-more").addEventListener("click", () => togglePopover("salvar"));
document.getElementById("save-file").addEventListener("click", () => saveDraft());
document.getElementById("save-as").addEventListener("click", saveAsOther);
document.getElementById("save-download").addEventListener("click", downloadCollection);
document.getElementById("unlink-btn").addEventListener("click", unlinkFile);
````

### E20 — Importar pelo «⋯» passa pela janela do sistema

**Arquivo:** `app/index.html`

**Ancora:**

````
document.getElementById("menu-import").addEventListener("click", () => document.getElementById("file-input").click());
````

**Texto novo (substitui a ancora inteira):**

````
document.getElementById("menu-import").addEventListener("click", pickAndImport);   // I4
````

### E21 — Importar pelo seletor passa pela janela do sistema

**Arquivo:** `app/index.html`

**Ancora:**

````
document.getElementById("import-btn").addEventListener("click", () =>
  document.getElementById("file-input").click());
````

**Texto novo (substitui a ancora inteira):**

````
document.getElementById("import-btn").addEventListener("click", pickAndImport);   // I4
````

### E22 — soltar o arquivo traz o vinculo

**Arquivo:** `app/index.html`

**Ancora:**

````
  if (f && alb && App.saved) readTracksFile(f, alb.id);
  else if (f) importFromFile(f);
````

**Texto novo (substitui a ancora inteira):**

````
  if (f && alb && App.saved) { readTracksFile(f, alb.id); return; }
  if (!f) return;
  // I4: no Chrome, o arquivo solto traz o vinculo. getAsFileSystemHandle so pode
  // ser chamado durante o drop; sem ele (ou se falhar), importa como antes.
  const item = Array.from(e.dataTransfer.items || []).find(i => i.kind === "file");
  const hp = canWriteFile() && item && item.getAsFileSystemHandle ? item.getAsFileSystemHandle() : null;
  if (!hp) { importFromFile(f); return; }
  hp.then(h => importFromFile(f, h && h.kind === "file" ? h : null), () => importFromFile(f));
````

### E23 — Ctrl+S salva

**Arquivo:** `app/index.html`

**Ancora:**

````
  if ((e.ctrlKey || e.metaKey) && !e.altKey && !e.shiftKey && e.key.toLowerCase() === "z") {
````

**Texto novo (substitui a ancora inteira):**

````
  // I4 (DEC-033): Ctrl+S / ⌘S salva, ate dentro de um campo de texto, e nunca abre o
  // «salvar pagina» do navegador. Sem alteracoes, nao faz nada visivel.
  if ((e.ctrlKey || e.metaKey) && !e.altKey && !e.shiftKey && e.key.toLowerCase() === "s") {
    e.preventDefault(); e.stopImmediatePropagation();
    if (!document.querySelector("dialog[open]") && App.saved && App.changes > 0) saveDraft();
    return;
  }
  if ((e.ctrlKey || e.metaKey) && !e.altKey && !e.shiftKey && e.key.toLowerCase() === "z") {
````

### E24 — o bloco da I4

**Arquivo:** `app/index.html`

**Ancora:**

````
// A abertura e assincrona (IndexedDB); a importacao espera por ela.
````

**Texto novo (substitui a ancora inteira):**

````
/* ===================================================================
   Salvar no arquivo (I4, DEC-033 — spec meta/specs/261106-salvar-no-arquivo.md)
   Onde a File System Access existe (Chrome e Edge no computador), «Salvar»
   grava no proprio .json. O acervo fica VINCULADO ao arquivo: o handle mora no
   registro do IndexedDB, com a data e o tamanho do arquivo na ultima leitura ou
   gravacao, para perceber quando ele mudou fora do app. Nada disso vai para o
   .json. A permissao de gravar e do navegador, que a pede de novo em outra
   sessao. Firefox, Safari e o celular baixam, como antes.
   =================================================================== */
App.link = null;        // { handle, stamp: { lastModified, size } } do acervo aberto, ou null
App.lastWrite = null;   // «HH:MM» da ultima gravacao no arquivo, para a marca da barra
App.writing = false;    // uma gravacao por vez (o botao e o Ctrl+S juntos)

/** A API existe e a pagina nao esta num iframe (onde as janelas sao recusadas). */
function fileApi() {
  let top = false;
  try { top = window.self === window.top; } catch (e) { top = false; }
  return "showSaveFilePicker" in window && "showOpenFilePicker" in window && top;
}
/** O app grava direto no arquivo: com a API, no computador e com o IndexedDB (onde o
    vinculo mora). No celular, mesmo com a API, baixa (ponto 5 da spec). */
function canWriteFile() { return fileApi() && !isMobile() && !!Store.db; }

const JSON_TYPES = [{ description: "Acervo do Cancioneiro", accept: { "application/json": [".json"] } }];
const hhmm = () => new Date().toLocaleTimeString("pt-BR", { hour: "2-digit", minute: "2-digit" });
const stampOf = f => ({ lastModified: f.lastModified, size: f.size });

/** Depois de salvar, a volta da ultima operacao continua valendo (DEC-033): desfazer
    devolve o rascunho a uma alteracao a frente do arquivo. */
function keepUndoAfterSave() { if (App.undo) App.undo.changes = 1; }

/** Janela com varias saidas; resolve com o valor do botao escolhido, ou "cancel" no Esc.
    `options`: [valor, rotulo, principal?]. */
function chooseAsk(message, options) {
  return new Promise(resolve => {
    const dlg = document.getElementById("choice-dialog");
    document.getElementById("choice-text").textContent = message;
    const box = document.getElementById("choice-actions");
    box.textContent = "";
    let done = false;
    const finish = v => { if (done) return; done = true; if (dlg.open) dlg.close(); resolve(v); };
    options.forEach(([value, label, primary], i) => {
      const b = document.createElement("button");
      b.type = "button"; b.textContent = label; b.dataset.value = value;
      if (primary) b.classList.add("btn-primary");
      if (i === 1) b.classList.add("spacer");
      b.addEventListener("click", () => finish(value));
      box.appendChild(b);
    });
    dlg.oncancel = e => { e.preventDefault(); finish("cancel"); };
    dlg.showModal();
  });
}

/** «Importar .json…»: no computador com a API, pela janela do sistema, que traz o
    vinculo; nos outros, pelo <input type=file> de sempre. */
async function pickAndImport() {
  if (!canWriteFile()) { document.getElementById("file-input").click(); return; }
  let h;
  try { [h] = await window.showOpenFilePicker({ types: JSON_TYPES }); }
  catch (e) { if (e.name !== "AbortError") document.getElementById("file-input").click(); return; }
  let f;
  try { f = await h.getFile(); } catch (e) { toast("Não consegui ler o arquivo: " + e.message); return; }
  importFromFile(f, h);
}

/** O texto que vai para o arquivo: o do «Baixar .json», com a quebra de linha final. */
function collectionText() {
  stripInternalKeys(App.collection);
  return JSON.stringify(App.collection, null, 2) + "\n";
}

/** Grava no arquivo. O Chrome escreve num .crswap ao lado e so troca no close():
    uma falha no meio nao deixa o arquivo pela metade. Devolve a marca nova, ou
    null (e avisa) se falhou. */
async function writeHandle(h) {
  try {
    const w = await h.createWritable();
    await w.write(collectionText());
    await w.close();
    return stampOf(await h.getFile());
  } catch (e) {
    toast("Não consegui gravar em " + h.name + ": " + e.message + ". O rascunho continua guardado neste navegador.");
    return null;
  }
}

/** Gravou: vincula ao arquivo, zera as alteracoes e guarda o vinculo no registro. */
async function afterFileWrite(h, stamp) {
  App.link = { handle: h, stamp };
  App.changes = 0; App.lastWrite = hhmm();
  keepUndoAfterSave();
  const ok = await persistDraft(false);
  toast("Salvo em " + h.name + " às " + App.lastWrite + "."
    + (h.name !== App.source ? " Neste navegador, o acervo continua com o nome " + App.source + "." : "")
    + (ok ? "" : " Não consegui guardar o vínculo neste navegador."));
}

/** «Salvar» e Ctrl+S: grava no arquivo vinculado; sem vinculo, pede o arquivo uma vez;
    onde nao grava direto, baixa. */
async function saveDraft() {
  if (!App.collection) return;
  if (!App.saved || !canWriteFile()) { downloadCollection(); return; }
  if (App.writing) return;
  App.writing = true;
  try {
    if (App.link) await saveLinked();
    else await saveAsFile(true);
  } finally { App.writing = false; }
}
/** «Salvar em outro arquivo…», do ▾. */
async function saveAsOther() {
  if (!App.collection || !App.saved || App.writing) return;
  App.writing = true;
  try { await saveAsFile(false); } finally { App.writing = false; }
}

/** A janela «Salvar como», com o nome de origem. `first`: o primeiro «Salvar» de um
    acervo sem vinculo, que diz antes o que vai acontecer. */
async function saveAsFile(first) {
  if (first) toast("Escolha o arquivo " + App.source + " para o app gravar nele daqui em diante; a janela já vem com o nome.");
  let h;
  try { h = await window.showSaveFilePicker({ suggestedName: App.source || "acervo.json", types: JSON_TYPES }); }
  catch (e) {
    if (e.name !== "AbortError") toast("Não consegui abrir a janela de salvar: " + e.message);
    else if (first) toast("Nada foi gravado.");
    return;
  }
  const stamp = await writeHandle(h);
  if (stamp) await afterFileWrite(h, stamp);
}

/** Grava no arquivo vinculado: a permissao (o aviso do navegador, uma vez por sessao),
    a conferencia de mudanca fora do app (data e tamanho) e a gravacao. */
async function saveLinked() {
  const h = App.link.handle, name = h.name;
  let p = "denied";
  try {
    p = await h.queryPermission({ mode: "readwrite" });
    if (p !== "granted") p = await h.requestPermission({ mode: "readwrite" });
  } catch (e) { p = "denied"; }
  if (p !== "granted") {
    toast("Sem permissão para gravar em " + name + ": nada foi gravado. Tente de novo, ou use «Baixar .json» no ▾.");
    return;
  }
  let f = null;
  try { f = await h.getFile(); } catch (e) { f = null; }
  if (!f) {
    const v = await chooseAsk(name + " não foi encontrado: foi movido, renomeado ou apagado. O rascunho continua guardado neste navegador.",
      [["cancel", "Cancelar"], ["other", "Salvar em outro arquivo…", true]]);
    if (v === "other") await saveAsFile(false);
    return;
  }
  const s = App.link.stamp;
  if (s && (f.lastModified !== s.lastModified || f.size !== s.size)) {
    const v = await chooseAsk(name + " mudou fora do app: foi alterado em " + fmtDate(f.lastModified)
      + ", depois da última vez que o app o leu ou gravou (" + fmtDate(s.lastModified) + "). Substituir grava "
      + (App.changes === 1 ? "a alteração" : "as " + App.changes + " alterações") + " por cima do que mudou lá.",
      [["cancel", "Cancelar"], ["other", "Salvar em outro arquivo…"], ["replace", "Substituir mesmo assim", true]]);
    if (v === "other") { await saveAsFile(false); return; }
    if (v !== "replace") return;
  }
  const stamp = await writeHandle(h);
  if (stamp) await afterFileWrite(h, stamp);
}

/** Desvincula o acervo aberto do arquivo: o proximo «Salvar» pede a janela de novo. */
async function unlinkFile() {
  if (!App.link) return;
  const name = App.link.handle.name;
  App.link = null; App.lastWrite = null;
  await persistDraft(false);
  toast("Desvinculado de " + name + ". O próximo «Salvar» pede o arquivo de novo.");
}

// A abertura e assincrona (IndexedDB); a importacao espera por ela.
````

### E25 — entrada [0.17.0]

**Arquivo:** `meta/CHANGELOG.md`

**Ancora:**

````
## [0.16.0] — 2026-11-06
````

**Texto novo (substitui a ancora inteira):**

````
## [0.17.0] — 2026-11-06

Quarta e última entrega da frente de interface (I4, DEC-030, DEC-033): «Salvar» grava no próprio `.json`, onde o navegador deixa. Fecha a i-043.

### Added
- **«Salvar» grava no arquivo** no Chrome e no Edge do computador. No primeiro «Salvar» de um acervo, a janela do sistema vem com o nome do arquivo de origem; o acervo fica vinculado àquele arquivo, e os próximos «Salvar» gravam sem janela. Ao reabrir o app, o navegador pede uma vez a permissão de editar.
- **`Ctrl+S` (`⌘S`)** salva, até dentro de um campo de texto, e não abre mais o «salvar página» do navegador. Sem alterações, não faz nada.
- **O ▾ ao lado de «Salvar»:** Salvar no arquivo, Salvar em outro arquivo… (vincula ao escolhido) e Baixar .json (uma cópia em Downloads; com vínculo, o rascunho continua não salvo).
- **Importar pela janela do sistema** («Importar .json…» e «Importar outro .json…») e soltar o arquivo na tela já vinculam o acervo ao arquivo.
- **Arquivo mudado fora do app:** antes de gravar, o app compara a data e o tamanho do arquivo com os da última leitura ou gravação e pergunta: Cancelar, Salvar em outro arquivo… ou Substituir mesmo assim. Arquivo sumido: avisa e oferece salvar em outro.
- **O vínculo no seletor de acervo** («Vinculado a X», ou «Sem vínculo») e **Desvincular do arquivo**. Esquecer o acervo apaga o vínculo junto.
- Depois de gravar, a barra mostra «✓ Salvo no arquivo às HH:MM».

### Changed
- **«Desfazer» continua valendo depois de salvar** (revê a DEC-032): desfazer devolve o rascunho a «1 alteração não salva». Vale também para o «Salvar .json» que baixa.
- Firefox, Safari e o celular continuam com «Salvar .json», que baixa como antes; o seletor de acervo diz por quê.

Spec `meta/specs/261106-salvar-no-arquivo.md`: 14 de 14 critérios no Chromium headless (em `http://127.0.0.1`, com as janelas do sistema trocadas por arquivos da pasta privada do navegador), com prova de vida no app da 0.16.0. Abrir 205 faixas leva de 1 a 34 ms a mais que a 0.16.0 nas mesmas rodadas (o limite era 50); gravar 205 faixas (293 KB), de 10 a 14 ms. A sonda no Chrome 156 do dono, no `file://`, confirmou a janela de salvar, gravar de novo sem janela, guardar o vínculo e abrir pela janela. O app passa de 239 KB para 253 KB.

---

## [0.16.0] — 2026-11-06
````

### E26 — DEC-033 no fim

**Arquivo:** `meta/DECISIONS.md`

**Ancora:**

````
**Consequências:** (+) Organizar fica sempre à mão, sem o interruptor, com um caminho sem arrastar para tudo (o «⋯», WCAG 2.5.7). (+) O hash no `validate.py` torna visível qualquer mudança na biblioteca. (−) São 45 KB de código de terceiro no app; abrir 205 faixas ficou até cerca de 30 ms mais lento que na 0.15.0. (−) A SortableJS, no modo de arrastar que o app usa, engole o primeiro clique depois de soltar; o app desfaz isso com um clique sintético ao fim de cada arrastar (comentado em `dragEnd`), e uma versão nova pede reconferir. (−) Com filtro ligado, pode haver faixas escondidas entre a solta e a vizinha; o aviso e o «Desfazer» seguram.
````

**Texto novo (substitui a ancora inteira):**

````
**Consequências:** (+) Organizar fica sempre à mão, sem o interruptor, com um caminho sem arrastar para tudo (o «⋯», WCAG 2.5.7). (+) O hash no `validate.py` torna visível qualquer mudança na biblioteca. (−) São 45 KB de código de terceiro no app; abrir 205 faixas ficou até cerca de 30 ms mais lento que na 0.15.0. (−) A SortableJS, no modo de arrastar que o app usa, engole o primeiro clique depois de soltar; o app desfaz isso com um clique sintético ao fim de cada arrastar (comentado em `dragEnd`), e uma versão nova pede reconferir. (−) Com filtro ligado, pode haver faixas escondidas entre a solta e a vizinha; o aviso e o «Desfazer» seguram.

## DEC-033 — I4: «Salvar» grava no arquivo vinculado (File System Access), com o vínculo no IndexedDB; o «Desfazer» continua depois de salvar; o celular baixa

**Data:** 2026-11-06
**Status:** aceita
**Contexto:** A spec da I4 (`meta/specs/261106-salvar-no-arquivo.md`) trouxe cinco pontos, decididos pelo dono em 2026-11-06, os cinco como recomendados, depois da sonda no Chrome 156 dele: no `file://`, a janela de salvar, gravar de novo sem janela, guardar o vínculo no IndexedDB e a janela de abrir funcionaram `[medido por instrumento, sonda do dono]`. Firefox (posição negativa) e Safari (contrária) não terão a API.
**Decisão:**
- **Onde a API existe no computador (Chrome, Edge), «Salvar» grava no próprio `.json`.** O acervo fica vinculado ao arquivo: o handle, a data e o tamanho do arquivo na última leitura ou gravação moram no registro do acervo no IndexedDB (`fileHandle`, `fileStamp`), nunca no `.json`.
- **O vínculo nasce em três caminhos:** no primeiro «Salvar» (a janela vem com o nome de origem), ao importar pela janela do sistema e ao soltar o arquivo na tela.
- **Antes de gravar, o app compara data e tamanho** e pergunta se o arquivo mudou fora: cancelar, salvar em outro, ou substituir. Não mescla.
- **O «Desfazer» da última operação continua valendo depois de salvar;** desfazer volta a 1 alteração. Revê o «salvar esquece a volta» da DEC-032.
- **`Ctrl+S` salva em qualquer navegador,** até num campo de texto; onde não grava direto, baixa.
- **No celular, mesmo com a API (Chrome Android 132+), «Salvar .json» baixa.**
**Alternativas consideradas:** vincular só no primeiro «Salvar» (duas janelas para quem importa e salva em seguida); vincular só ao importar (exige reimportar os acervos que já estão no navegador); gravar sem conferir o arquivo (a versão de fora some em silêncio); salvar sozinho a cada operação (o aviso de permissão no meio da curadoria, e o «Desfazer» e o aviso de arquivo mudado ficariam confusos); gravar também no Android (sem gravação atômica e sem criar arquivo novo).
**Consequências:** (+) Salvar custa um clique ou `Ctrl+S`, sem Downloads nem substituir à mão. (+) Editar o `.json` fora do app com um rascunho aberto não se perde em silêncio. (−) Uma permissão do navegador por sessão; se o «Permitir em todas as visitas» vale no `file://` não foi medido (a sonda não passou pelo fechar e reabrir). (−) O teste automático não abre a janela real: as janelas são trocadas por arquivos da pasta privada do navegador, em `http://127.0.0.1`, e, no headless, ler do IndexedDB um handle guardado derruba a aba fora de um perfil persistente. (−) Dois caminhos de salvar para manter: gravar e baixar.
````

### E27 — i-043 entregue (titulo)

**Arquivo:** `meta/IDEAS.md`

**Ancora:**

````
### i-043 💡 Gravar direto no arquivo do acervo (File System Access)
````

**Texto novo (substitui a ancora inteira):**

````
### i-043 ✅ Gravar direto no arquivo do acervo (File System Access)
````

### E28 — i-043 entregue (linha nova)

**Arquivo:** `meta/IDEAS.md`

**Ancora:**

````
**Planejada (DEC-030):** é a I4 da frente de interface (0.17.0), depois de a I3 deixar o «Salvar» fácil de achar.
````

**Texto novo (substitui a ancora inteira):**

````
**Planejada (DEC-030):** é a I4 da frente de interface (0.17.0), depois de a I3 deixar o «Salvar» fácil de achar.
**Entregue (0.17.0, I4, DEC-033):** «Salvar» grava no arquivo vinculado no Chrome e no Edge do computador; o vínculo nasce no primeiro «Salvar», ao importar pela janela ou ao soltar o arquivo; o app pergunta antes de gravar por cima de um arquivo mudado fora. Firefox, Safari e o celular baixam. Spec `meta/specs/261106-salvar-no-arquivo.md`.
````

### E29 — i-051 nova

**Arquivo:** `meta/IDEAS.md`

**Ancora:**

````
`[relatado pelo dono, 2026-11-05, na i-048]` Soltar uma faixa sobre outro acervo da lateral para copiá-la ou movê-la para ele. Mexe em dois rascunhos de uma vez (e em dois arquivos a salvar), e pede uma análise própria antes da spec. Hoje o caminho é exportar a faixa em `.json` e importá-la no outro acervo.
````

**Texto novo (substitui a ancora inteira):**

````
`[relatado pelo dono, 2026-11-05, na i-048]` Soltar uma faixa sobre outro acervo da lateral para copiá-la ou movê-la para ele. Mexe em dois rascunhos de uma vez (e em dois arquivos a salvar), e pede uma análise própria antes da spec. Hoje o caminho é exportar a faixa em `.json` e importá-la no outro acervo.

### i-051 💡 Versionar os testes do navegador
`[capturada pelo chat, 2026-11-06, na I4]` Os testes no Chromium headless de cada entrega (curadoria 1 a 3, I1 a I4) moram só na sessão do chat que os escreveu: a conversa seguinte não os tem, e a regressão da I4 teve de ser por fumaça (importar, lista, detalhe, «⋯», Cartões). Guardar em `tests/` (Playwright, Python) e rodar antes de cada WO de código. Pede decidir onde roda (a máquina do dono não tem Playwright) e o custo de manter.
````

### E30 — frente de interface concluida

**Arquivo:** `meta/ROADMAP.md`

**Ancora:**

````
- 🔨 Frente de interface (i-043 a i-048, DEC-030), em quatro entregas: ✅ barra única, com o seletor de acervo, os filtros com etiquetas e o «⋯» (0.14.0) · ✅ lista e detalhe, com a lateral de álbuns e acervos (0.15.0) · ✅ organizar: arrastar, «⋯» por faixa, lote, «Desfazer», sem o interruptor «editar» (0.16.0) · ⬜ salvar direto no arquivo (0.17.0, i-043).
````

**Texto novo (substitui a ancora inteira):**

````
- ✅ Frente de interface (i-043 a i-048, DEC-030 a DEC-033), em quatro entregas: ✅ barra única, com o seletor de acervo, os filtros com etiquetas e o «⋯» (0.14.0) · ✅ lista e detalhe, com a lateral de álbuns e acervos (0.15.0) · ✅ organizar: arrastar, «⋯» por faixa, lote, «Desfazer», sem o interruptor «editar» (0.16.0) · ✅ salvar direto no arquivo, onde o navegador deixa (0.17.0, DEC-033).
````

### E31 — estado v0.17.0

**Arquivo:** `README.md`

**Ancora:**

````
> **Estado:** v0.16.0 — ferramenta em uso. Lê, guarda e edita vários acervos, copia por campo, troca módulos de estilo, ajusta o BPM, **mede cada prompt contra os limites do Suno**, exporta Markdown, exporta uma faixa como `.json` e **entrega o prompt para chats gerarem canções no esquema**. Publicada no GitHub Pages. Ver `meta/ROADMAP.md`.
````

**Texto novo (substitui a ancora inteira):**

````
> **Estado:** v0.17.0 — ferramenta em uso. Lê, guarda e edita vários acervos, grava direto no arquivo do acervo (Chrome e Edge), copia por campo, troca módulos de estilo, ajusta o BPM, **mede cada prompt contra os limites do Suno**, exporta Markdown, exporta uma faixa como `.json` e **entrega o prompt para chats gerarem canções no esquema**. Publicada no GitHub Pages. Ver `meta/ROADMAP.md`.
````

### E32 — passo 7: salvar no arquivo (e sem a sobra da 0.13.0)

**Arquivo:** `README.md`

**Ancora:**

````
7. Para reorganizar, não há nada a ligar: na Lista, arraste a faixa pela alça ⋮⋮ (para outra posição, outro álbum ou um álbum da lateral; durante o arrastar, a lateral oferece *+ Novo álbum*), ou use o «⋯» da faixa (*Mover para…*, *Subir*, *Descer*, *Excluir…*; `Alt+↑` e `Alt+↓` no título). Marque as caixas para mover, exportar, marcar ou excluir várias de uma vez. Cada operação mostra *Desfazer* no aviso (ou `Ctrl+Z`), até a próxima. Para trazer faixas de outro `.json`, use *Importar faixas…* no «⋯» da barra, ou solte o arquivo sobre um álbum. As mudanças ficam num rascunho no navegador; a barra mostra quantas são, com *Salvar .json*, que baixa com o nome do arquivo original — substitua o antigo por ele, e ele passa a ser a fonte. Só se organiza um acervo com cópia guardada no navegador (importado por arquivo); no exemplo que o Pages carrega sozinho, o «⋯» só exporta. cada cartão ganha ↑ ↓, *mover…* e *excluir*, e *importar faixas…* traz faixas de outro `.json`. As mudanças ficam num rascunho no navegador; a barra mostra quantas são, com *Salvar .json*, que baixa com o nome do arquivo original — substitua o antigo por ele, e ele passa a ser a fonte.
````

**Texto novo (substitui a ancora inteira):**

````
7. Para reorganizar, não há nada a ligar: na Lista, arraste a faixa pela alça ⋮⋮ (para outra posição, outro álbum ou um álbum da lateral; durante o arrastar, a lateral oferece *+ Novo álbum*), ou use o «⋯» da faixa (*Mover para…*, *Subir*, *Descer*, *Excluir…*; `Alt+↑` e `Alt+↓` no título). Marque as caixas para mover, exportar, marcar ou excluir várias de uma vez. Cada operação mostra *Desfazer* no aviso (ou `Ctrl+Z`), até a próxima. Para trazer faixas de outro `.json`, use *Importar faixas…* no «⋯» da barra, ou solte o arquivo sobre um álbum. As mudanças ficam num rascunho no navegador; a barra mostra quantas são. No Chrome e no Edge do computador, *Salvar* (ou `Ctrl+S`) grava no próprio `.json`: na primeira vez, a janela do sistema pede o arquivo, já com o nome; daí em diante grava direto, e avisa se o arquivo mudou fora do app. O ▾ ao lado tem *Salvar em outro arquivo…* e *Baixar .json*. No Firefox, no Safari e no celular, *Salvar .json* baixa com o nome do arquivo original — substitua o antigo por ele, e ele passa a ser a fonte. Só se organiza um acervo com cópia guardada no navegador (importado por arquivo); no exemplo que o Pages carrega sozinho, o «⋯» só exporta.
````

### E33 — a copia e o arquivo

**Arquivo:** `README.md`

**Ancora:**

````
O acervo canônico são **arquivos JSON** no esquema: os exemplos versionados em `data/`, e o acervo pessoal fora do repo (DEC-026). O navegador guarda **cópias dos acervos importados** (IndexedDB) e, no localStorage, as marcações por acervo e a estrutura do cartão — cache, nunca a fonte: o menu do seletor de acervo diz de onde a cópia veio e quando, e *Esquecer este acervo* a apaga sem tocar no arquivo. Ao organizar, a cópia vira rascunho até você salvar o `.json` e substituir o arquivo. Ver `meta/DECISIONS.md` (DEC-004, DEC-022, DEC-028, DEC-029, DEC-030, DEC-031, DEC-032).
````

**Texto novo (substitui a ancora inteira):**

````
O acervo canônico são **arquivos JSON** no esquema: os exemplos versionados em `data/`, e o acervo pessoal fora do repo (DEC-026). O navegador guarda **cópias dos acervos importados** (IndexedDB) e, no localStorage, as marcações por acervo e a estrutura do cartão — cache, nunca a fonte: o menu do seletor de acervo diz de onde a cópia veio e quando, e *Esquecer este acervo* a apaga sem tocar no arquivo. Ao organizar, a cópia vira rascunho até você salvar: no Chrome e no Edge do computador, «Salvar» grava no próprio arquivo, vinculado à cópia; nos outros, baixa o `.json` para substituir o antigo. Ver `meta/DECISIONS.md` (DEC-004, DEC-022, DEC-028, DEC-029, DEC-030, DEC-031, DEC-032, DEC-033).
````

### E34 — versao e fase

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
**Versão atual:** 0.16.0 · **Fase:** 3a, 3a.2, o BPM da 3b, o prompt-modelo e as conveniências de uso concluídos e conferidos · os álbuns antigos convertidos (i-008, fora do repo) · curadoria no app concluída nas três entregas (DEC-028, DEC-029) · frente de interface com a I3 conferida e a I4 em spec (DEC-030 a DEC-032) · kit de música lido pelo KCM, à espera da resposta (i-039)
````

**Texto novo (substitui a ancora inteira):**

````
**Versão atual:** 0.17.0 · **Fase:** 3a, 3a.2, o BPM da 3b, o prompt-modelo e as conveniências de uso concluídos e conferidos · os álbuns antigos convertidos (i-008, fora do repo) · curadoria no app concluída nas três entregas (DEC-028, DEC-029) · frente de interface nas quatro entregas, a I4 à espera da conferência na tela (DEC-030 a DEC-033) · kit de música lido pelo KCM, à espera da resposta (i-039)
````

### E35 — ultima conversa

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
## Última conversa (2026-11-06, I3: protótipo, spec e implementação, WO 0027)

- **I2 conferida na tela pelo dono** (roteiro OK `[relatado pelo dono]`): lista e detalhe (0.15.0) estão fechados.
- **I3, organizar (0.16.0):** protótipo no canvas «Cancioneiro: nova interface» (fileira da I3), spec `meta/specs/261106-organizar.md` e os três pontos decididos pelo dono como recomendados (DEC-032): arrastar com filtro pela regra da próxima visível, Cartões só com o «⋯», seleção no celular pelo «⋯». 15 de 15 critérios no Chromium headless, testados pelo chat.
- **WO 0027 aplicada e empurrada** (`6a07bfd`, 0.16.0): validação verde. **I3 conferida na tela pelo dono** (os 11 itens do roteiro OK `[relatado pelo dono, 2026-11-06]`): organizar está fechado.
- **WO 0028 recusada pelo Code** (cabeçalho sem «Âncoras lidas em») e reemitida pelo chat como WO 0029, com o campo.
- **I4, salvar no arquivo:** protótipo no canvas (fileira da I4), spec `meta/specs/261106-salvar-no-arquivo.md` em rascunho, com cinco pontos para o dono, e a sonda `../261106-sonda-i4-salvar.html` para ele rodar no Chrome antes de decidir.
- **Este bloco substitui o anterior, da WO 0026** (I2). O que ele dizia está no CHANGELOG [0.15.0], na spec `meta/specs/261106-lista-e-detalhe.md` e em `logs/2026-11-06.md` (Conversas 1 a 3).

````

**Texto novo (substitui a ancora inteira):**

````
## Última conversa (2026-11-06, I4: sonda, pontos e implementação, WO 0030)

- **WO 0029 aplicada e empurrada** (`24b1fc0`, wrap `a9efdef`): a I3 conferida, a recusa da WO 0028 e a I4 em spec ficaram registradas.
- **Sonda da I4 no Chrome 156 do dono** (`file://`): janela de salvar, gravar de novo sem janela, vínculo guardado no IndexedDB, janela de abrir e handle ao arrastar, todos OK `[medido por instrumento]`. Não mediu o fechar e reabrir nem o arquivo mudado fora: a página não foi reaberta e o arquivo de teste não foi editado.
- **I4, salvar no arquivo (0.17.0):** os cinco pontos decididos pelo dono como recomendados (DEC-033); 14 de 14 critérios no Chromium headless, testados pelo chat; falta a conferência na tela pelo dono.
- **Este bloco substitui o anterior, da WO 0029** (I3 conferida e a I4 em spec). O que ele dizia está no CHANGELOG [0.16.0], nas specs `meta/specs/261106-organizar.md` e `meta/specs/261106-salvar-no-arquivo.md` e em `logs/2026-11-06.md` (Conversas 4 a 10).

````

### E36 — funciona: salvar no arquivo

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
- **Organizar** (0.16.0, DEC-030, DEC-032): arrastar pela alça ⋮⋮ na Lista (com filtro, antes da próxima visível) e para os álbuns da lateral ou «+ Novo álbum»; o «⋯» de cada faixa (linha, detalhe e cartão) com Mover, Subir, Descer, Exportar e Excluir, e `Alt+↑`/`Alt+↓`; caixas e barra de lote; «Desfazer» e `Ctrl+Z` da última operação; soltar o `.json` sobre um álbum importa faixas nele. Só com cópia guardada no navegador. A SortableJS 1.15.7 vai embutida, com o hash no `validate.py`. Conferido na tela pelo dono em 2026-11-06.
````

**Texto novo (substitui a ancora inteira):**

````
- **Organizar** (0.16.0, DEC-030, DEC-032): arrastar pela alça ⋮⋮ na Lista (com filtro, antes da próxima visível) e para os álbuns da lateral ou «+ Novo álbum»; o «⋯» de cada faixa (linha, detalhe e cartão) com Mover, Subir, Descer, Exportar e Excluir, e `Alt+↑`/`Alt+↓`; caixas e barra de lote; «Desfazer» e `Ctrl+Z` da última operação; soltar o `.json` sobre um álbum importa faixas nele. Só com cópia guardada no navegador. A SortableJS 1.15.7 vai embutida, com o hash no `validate.py`. Conferido na tela pelo dono em 2026-11-06.
- **Salvar no arquivo** (0.17.0, DEC-033): no Chrome e no Edge do computador, «Salvar» (ou `Ctrl+S`) grava no próprio `.json`; o primeiro «Salvar» de um acervo pede o arquivo na janela do sistema, e importar pela janela ou soltar o arquivo já vinculam. Antes de gravar, confere se o arquivo mudou fora. O ▾ tem «Salvar em outro arquivo…» e «Baixar .json»; o seletor de acervo mostra o vínculo e «Desvincular». Firefox, Safari e o celular baixam. O «Desfazer» continua depois de salvar.
````

### E37 — pendencias do dono

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
- **Rodar a sonda da I4 e decidir os cinco pontos** — abrir `..\261106-sonda-i4-salvar.html` no Chrome, seguir os passos da página e salvar o relatório na pasta-pai; os pontos estão no fim de `meta/specs/261106-salvar-no-arquivo.md`.
````

**Texto novo (substitui a ancora inteira):**

````
- **Conferir a I4 na tela** — roteiro na conversa de 2026-11-06 (WO 0030), depois do push, no Chrome do computador (com fechar e reabrir o app) e no celular. Apagar à mão o `..\sonda-i4-teste.json`.
````

### E38 — backlog

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
1. **I4 — Salvar no arquivo** (i-043, DEC-030) — protótipo e spec prontos (`meta/specs/261106-salvar-no-arquivo.md`); faltam a sonda e os cinco pontos do dono, depois a implementação pelo chat e a WO (0.17.0).
2. **Organizar os álbuns** (i-049) — renomear, reordenar na lateral, juntar dois; candidata depois da I4.
3. **Rampa de BPM** (i-042) — três faixas BR reprovam no `validate.py` por mudarem de andamento de propósito.
4. **Pesquisar outras plataformas de música por IA** (i-032) — um turno de pesquisa antes de qualquer mudança de esquema.
5. **Avisar palavra de andamento que contradiz o BPM** (i-029) — pede uma tabela palavra → faixa de BPM, com fonte e data.
````

**Texto novo (substitui a ancora inteira):**

````
1. **Organizar os álbuns** (i-049) — renomear, reordenar na lateral, juntar dois.
2. **Versionar os testes do navegador** (i-051) — os testes de cada entrega ficaram fora do repositório; a regressão da I4 foi por fumaça.
3. **Rampa de BPM** (i-042) — três faixas BR reprovam no `validate.py` por mudarem de andamento de propósito.
4. **Pesquisar outras plataformas de música por IA** (i-032) — um turno de pesquisa antes de qualquer mudança de esquema.
5. **Avisar palavra de andamento que contradiz o BPM** (i-029) — pede uma tabela palavra → faixa de BPM, com fonte e data.
````

### E39 — nota do rascunho

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
- **Rascunho (DEC-028, DEC-029, DEC-032):** com alterações, a cópia guardada está à frente do arquivo até «Salvar .json» e substituir. A marca na barra é o lembrete; esquecer e reimportar pedem confirmação. O «Desfazer» guarda só a última operação, na memória da aba: recarregar a página o esquece.
````

**Texto novo (substitui a ancora inteira):**

````
- **Rascunho (DEC-028, DEC-029, DEC-032, DEC-033):** com alterações, a cópia guardada está à frente do arquivo até «Salvar .json» e substituir. A marca na barra é o lembrete; esquecer e reimportar pedem confirmação. O «Desfazer» guarda só a última operação, na memória da aba: recarregar a página o esquece. Onde o app grava direto (Chrome e Edge no computador), o rascunho fica vinculado ao arquivo, e «Salvar» grava nele; o «Desfazer» continua depois de salvar. O vínculo mora no registro do acervo no IndexedDB, e esquecer o acervo o apaga.
````

## Depois de aplicar — conferencia antes do commit

| # | Checagem | Comando | Esperado |
|---|---|---|---|
| 1 | Os sete arquivos editados sao os previstos | `sha1sum app/index.html meta/CHANGELOG.md meta/DECISIONS.md meta/IDEAS.md meta/ROADMAP.md README.md meta/STATUS.md` | a coluna **chegada**, os sete |
| 2 | Os tres do chat nao mudaram | `sha1sum meta/CONTEXT.md meta/specs/261106-salvar-no-arquivo.md logs/2026-11-06.md` | os sha1 da segunda tabela |
| 3 | Validacao | `python3 scripts/validate.py; echo "exit=$?"` | `exit=0`, com `OK  versao 0.17.0 igual em CHANGELOG, app, README e STATUS` e `OK  biblioteca: SortableJS 1.15.7 embutida sem mudanca` |
| 4 | O codigo da I4 entrou uma vez | `grep -c '^async function saveLinked' app/index.html` e `grep -c '^<dialog class="prompt-dialog" id="choice-dialog"' app/index.html` | `1` e `1` (linhas) |
| 5 | Os registros | `grep -c '^## \[0.17.0\]' meta/CHANGELOG.md`, `grep -c '^## DEC-033 ' meta/DECISIONS.md` e `grep -c '^### i-051 ' meta/IDEAS.md` | `1`, `1` e `1` |
| 6 | Nada alem do previsto | `GIT_OPTIONAL_LOCKS=0 git status --short --untracked-files=all` | os dez arquivos e esta WO |

As checagens 4 e 5 foram rodadas pelo chat no clone, no shell Linux; no Git Bash, **nao testado** — com a 1 verde, relate o cru e nao pare.
**Esta e qual pergunta?** A 1 responde «esta la?» (os arquivos inteiros). O «presta?» o chat mediu no Chromium headless (Resultado da spec) e o dono confere na tela, pelo roteiro da conversa.

## Relatorio de aplicacao

Grave em `../AAMMDD-HHMM-code-cancioneiro-apply-wo0030.txt`, com o carimbo de `date +%y%m%d-%H%M` rodado na hora. Diga o resultado da checagem 1 em primeiro lugar. **Depois das checagens**, acrescente a sua secao no log (`## Conversa 12 — Code: WO 0030 aplicada`, curta) e inclua o log no mesmo commit; o sha1 do log muda por isso, e e esperado. Sem `/wrap` depois.

## Commit

```
git add app/index.html README.md meta/CHANGELOG.md meta/DECISIONS.md meta/IDEAS.md meta/ROADMAP.md meta/STATUS.md meta/CONTEXT.md meta/specs/261106-salvar-no-arquivo.md logs/2026-11-06.md meta/workorders/261106-wo0030-salvar-no-arquivo.md
```

```
git commit -m "feat: salvar no arquivo, versao 0.17.0" -m "Frente de interface, entrega I4 (DEC-033): Salvar grava no proprio .json no Chrome e no Edge do computador, com o acervo vinculado ao arquivo no IndexedDB; janela no primeiro Salvar, ao importar e ao soltar; aviso se o arquivo mudou fora; Ctrl+S; Desfazer depois de salvar; Firefox, Safari e celular baixam. Spec com o resultado, CONTEXT, IDEAS (i-043, i-051), ROADMAP, README, STATUS."
```

```
git push
```
