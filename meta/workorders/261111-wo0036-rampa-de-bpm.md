# WO 0036 — Rampa de BPM (0.19.0), com o conteudo da WO 0035 recusada

## Cabecalho

> **Tipo:** versao 0.19.0 — app, `validate.py`, kit, um arquivo de teste novo, CI e meta. Reemite tambem a WO 0035 (recusada na Edicao 0): 0.18.0 conferida e o passo «Dependencias» do CI sem depender do `apt`.
> **Config sugerida:** Sonnet · `/effort medium` (aplicacao literal por script; muitas edicoes).
> **Pre-requisito:** commit `c1fbc17`, branch `main`, sincronizada com `origin/main`. O `git status --short` mostra exatamente: ` M logs/2026-11-11.md`, `?? meta/specs/261111-rampa-de-bpm.md`, `?? meta/workorders/261111-wo0035-ci-e-0-18-conferida.md` e `?? meta/workorders/261111-wo0036-rampa-de-bpm.md`.
> **Base:** o dono decidiu em 2026-11-11 os quatro pontos da spec como recomendados `[relatado pelo dono]`; o dono conferiu a 0.18.0 na tela («roteiro dos albuns ok») `[relatado pelo dono]`; os relatorios `261111-1221` e `261111-1224` registram a WO 0035 recusada.
> **Depende de:** `c1fbc17` (wrap da WO 0035 recusada). A WO 0035 **nao** se aplica mais: ela fica so versionada, como registro.
>
> | arquivo | partida (sha1) | chegada (sha1) |
> |---|---|---|
> | `.github/workflows/testes.yml` | `362c6c03fe4e74a477e7e6daf18f362b25f37fe9` | `a0742d80416c6f8cbf5c9dfcdb68f11a1a1c2390` |
> | `README.md` | `96cfb926140bfaf5fe08c6cb0a911e05ccf58778` | `d4f485c5b6ac36dc8e5a54346b272a684fccb905` |
> | `app/index.html` | `2888edf687a262c321cba0493f5a419cae4387b3` | `4e2a2f98ada2ffb67d399b0b081b45b63727cd4a` |
> | `kit-musica/skills/macetes-suno/SKILL.md` | `2d172dcf36aaa461a93cb715c7c1e2a6c639aaff` | `53915f1bf780b7715afd82479f50d9d74c374440` |
> | `kit-musica/skills/revisar-faixa/SKILL.md` | `11e1cc7460864fde4bbc19e95ec57e0e5d6f6d2e` | `d25f7de8f4828c86895c981e291831d4f62c045f` |
> | `meta/CHANGELOG.md` | `d4c8d7b15a93b87ba360f2471d5b5e812eb9d605` | `af08b09b9bca00d868e277b8921113162ec36070` |
> | `meta/DECISIONS.md` | `0b806f0e660a3fd022d7c5ad1ba0073c6c790fba` | `79fee7c60ff23f0d0366f9423d45e42ebcb6b644` |
> | `meta/IDEAS.md` | `b3f7e9bfc28abe5f73e94dc4a5359e9ff559753a` | `c96eca6d41cdeb4f75b4ef33850159406890472d` |
> | `meta/ROADMAP.md` | `8aa65e907ff0222f02f1ca3d89c6f1014312ef61` | `86dcfe01d121ac85e3c51a17e4d7bf4f5342ee9f` |
> | `meta/STATUS.md` | `1db249552cd4e04dbe2eb60fad63e1d65c556e61` | `9fa79921e3d34e32b73658ea0d3a54aacc362169` |
> | `scripts/validate.py` | `4105ec178c3405eacadcf3e0fc8b0763562e41fa` | `5b2160f4f5a6b476ba4eeece1f558f4f267d6ed9` |
> | `tests/test_bpm.py` | (nao existe) | `3184b15a50b6c140eb9a7e6aa86e75b84a50a4d9` (arquivo novo, E32) |
> | `meta/specs/261111-rampa-de-bpm.md` | `733b82bd519b1bdaf3c6e12e6523b93dc391174c` | o mesmo (gravado pelo chat; so versionar) |
> | `logs/2026-11-11.md` | `dbb7e8121e06ee439d82edd3d9a4f78333a300bb` | o mesmo (gravado pelo chat; so versionar) |
> | `meta/workorders/261111-wo0035-ci-e-0-18-conferida.md` | `465daa9801bf15b09892378901d41acd2bf55475` | o mesmo (gravado pelo chat; so versionar) |
>
> **Ancora semantica:** se um trecho-ancora nao bater EXATAMENTE, PARE e reporte.
> **Idempotencia:** antes de cada edicao, procure o texto NOVO INTEIRO; se ja estiver la, PULE e diga no relatorio. Na edicao de texto novo vazio, se a ancora ja nao estiver la, PULE.
> **Ancoras:** linhas inteiras (uma linha ou um bloco de linhas inteiras), cada uma 1 vez no arquivo, na ordem abaixo. Toda edicao «substitui a ancora inteira»; texto novo vazio = apagar a ancora.
> **Âncoras lidas em** (lidas pelo chat NESTE turno, de `c1fbc17` clonado do repo do dono, conferido no disco do dono; aplicadas em ordem num clone, com a chegada medida):
> - E01 (`app/index.html`, versao 0.19.0): linha `    <span class="version" data-role="app-version">v0.18.0</span>`
> - E02 (`app/index.html`, CSS: o rótulo da rampa): linha `  .bpm-ctl .bpm-msg { color: var(--amber); font-weight: 600; }`
> - E03 (`app/index.html`, rampa: reconhecer e o valor inicial): bloco de 6 linhas, começando por `/** Valor inicial do controle: o numero do style (e o que o Suno ve); sem ele,`
> - E04 (`app/index.html`, rampa: o controle vira rótulo): bloco de 2 linhas, começando por `function bpmControl(song, card) {`
> - E05 (`app/index.html`, rampa: módulo de andamento não entra na recomposição): bloco de 4 linhas, começando por `  active.forEach(id => {`
> - E06 (`app/index.html`, rampa: chips de andamento desligados): bloco de 2 linhas, começando por `      chip.setAttribute("aria-pressed", active.has(m.id) ? "true" : "false");`
> - E07 (`app/index.html`, rampa: aviso âmbar na linha de qualidade): bloco de 3 linhas, começando por `  if (!isHidden("exclude")) findNegations(style, lyrics).forEach(n =>`
> - E08 (`app/index.html`, rampa: export .md): bloco de 2 linhas, começando por `  const bpmMeta = useRecomposed ? currentBpm(song) : song.bpm;`
> - E09 (`app/index.html`, rampa: a coluna BPM da Lista): linha `const bpmText = song => { const v = currentBpm(song); return v ? v + " bpm" : "—"; };`
> - E10 (`scripts/validate.py`, docstring: a rampa): bloco de 2 linhas, começando por `  5. O BPM de cada faixa e um so: o style nao tem dois numeros diferentes, e o`
> - E11 (`scripts/validate.py`, check_bpm com a rampa): bloco de 14 linhas, começando por `def check_bpm(data, rel):`
> - E12 (`scripts/validate.py`, aviso das rampas): bloco de 2 linhas, começando por `    if bad:`
> - E13 (`kit-musica/skills/macetes-suno/SKILL.md`, §5: o Cancioneiro preserva a rampa): linha `  controle de BPM do Cancioneiro. Para acelerar, descreva (gradual build, accelerating…`
> - E14 (`kit-musica/skills/revisar-faixa/SKILL.md`, conferência 7: a rampa): linha `| 7 | **BPM**: dois números no style, ou campo bpm diferente do style | — | um BPM por…`
> - E15 (`meta/CHANGELOG.md`, entrada [0.19.0]): linha `## [0.18.0] — 2026-11-09`
> - E16 (`README.md`, estado v0.19.0): linha `> **Estado:** v0.18.0 — ferramenta em uso. Lê, guarda e edita vários acervos, grava dire…`
> - E17 (`meta/DECISIONS.md`, DEC-036): linha `**Consequências:** (+) Organizar o acervo inteiro sem editar o .json à mão. (+) A desc…`
> - E18 (`meta/IDEAS.md`, i-042 entregue (título)): linha `### i-042 💡 Rampa de BPM no style («95 BPM to 118 BPM»)`
> - E19 (`meta/IDEAS.md`, i-042 entregue (linha)): linha `Achado na conversão BR: três faixas mudam de andamento de propósito. A DEC-020 reprova d…`
> - E20 (`meta/ROADMAP.md`, rampa de BPM): linha `- ✅ Controle de BPM no cartão (i-005, DEC-020) — 0.7.0, conferido na tela pelo dono em 2…`
> - E21 (`meta/STATUS.md`, versão): linha `**Versão atual:** 0.18.0 · **Fase:** 3a, 3a.2, o BPM da 3b, o prompt-modelo e as conveni…`
> - E22 (`meta/STATUS.md`, última conversa): bloco de 7 linhas, começando por `## Última conversa (2026-11-09, organizar os álbuns, WO 0034)`
> - E23 (`meta/STATUS.md`, funciona: a rampa): linha `- **Controle de BPM no cartão (0.7.0, DEC-020):** campo 20-300 com −5/+5 e «voltar a…`
> - E24 (`meta/STATUS.md`, quebrado: o CI e a WO 0035): bloco de 2 linhas, começando por `- **CI do a67ee01 sem veredito** — falha de rede do runner no passo «Dependencias», tr…`
> - E25 (`meta/STATUS.md`, pendências: conferir a rampa): linha `- **Conferir organizar os álbuns na tela** — roteiro na conversa de 2026-11-09 (WO 0034)…`
> - E26 (`meta/STATUS.md`, backlog: sai a rampa): linha `1. **Rampa de BPM** (i-042) — três faixas BR reprovam no validate.py por mudarem de an…`
> - E27 (`meta/STATUS.md`, backlog: renumera 2): linha `2. **Importar prompts prontos dos álbuns como módulos** — o último ⬜ da 3b no ROADMAP; o…`
> - E28 (`meta/STATUS.md`, backlog: renumera 3): linha `3. **Kit de música v2, leva 2** (i-039) — as skills escrever-letra-suno e conceber-al…`
> - E29 (`meta/STATUS.md`, backlog: renumera 4): linha `4. **Pesquisar outras plataformas de música por IA** (i-032) — um turno de pesquisa ante…`
> - E30 (`meta/STATUS.md`, backlog: renumera 5): linha `5. **Avisar palavra de andamento que contradiz o BPM** (i-029) — pede uma tabela palavra…`
> - E31 (`.github/workflows/testes.yml`, CI sem apt obrigatorio): linha `          python -m playwright install --with-deps chromium`
> **Canal dos meta neste ciclo = CODE:** STATUS, CHANGELOG, DECISIONS, ROADMAP, IDEAS e README pelo Code (DEC-010), com o texto abaixo; a spec e o log ja estao gravados pelo chat.

---

## 1. Por que

O controle de BPM (DEC-020) troca todo numero de BPM do Style pelo valor dele, e o valor inicial e o primeiro numero: «95 BPM building to 115 BPM» era copiado como «95 BPM building to 95 bpm», sem ninguem mexer — nas tres faixas BR com rampa, desde a 0.7.0. A 0.19.0 reconhece a rampa (dois BPM no mesmo trecho ligados por to/building to/rising to/up to/climbing to/→), copia byte a byte, troca o controle por um rotulo, desliga os chips de andamento, avisa em ambar e faz o `validate.py` dar AVISO em vez de ERRO (DEC-036). Junto vai o conteudo da WO 0035: o passo «Dependencias» do CI, que caiu tres vezes no `apt` do runner, e a 0.18.0 conferida no STATUS.

## Edicao 0 — Conferencia de hash e de arvore

```
sha1sum .github/workflows/testes.yml README.md app/index.html kit-musica/skills/macetes-suno/SKILL.md kit-musica/skills/revisar-faixa/SKILL.md meta/CHANGELOG.md meta/DECISIONS.md meta/IDEAS.md meta/ROADMAP.md meta/STATUS.md scripts/validate.py meta/specs/261111-rampa-de-bpm.md logs/2026-11-11.md meta/workorders/261111-wo0035-ci-e-0-18-conferida.md
GIT_OPTIONAL_LOCKS=0 git status --short
```

Todos batem com **partida**; o `git status` mostra exatamente as quatro linhas do Pre-requisito. Qualquer outra coisa: **PARE e reporte**.

## Edicoes E01 a E32

Na ordem. Copie o que esta ENTRE as linhas de quatro crases, sem elas. Aplique por script, extraindo os blocos da WO; grave em UTF-8 com LF.

### E01 — versao 0.19.0

**Arquivo:** `app/index.html`

**Ancora:**

````
    <span class="version" data-role="app-version">v0.18.0</span>
````

**Texto novo (substitui a ancora inteira):**

````
    <span class="version" data-role="app-version">v0.19.0</span>
````

### E02 — CSS: o rótulo da rampa

**Arquivo:** `app/index.html`

**Ancora:**

````
  .bpm-ctl .bpm-msg { color: var(--amber); font-weight: 600; }
````

**Texto novo (substitui a ancora inteira):**

````
  .bpm-ctl .bpm-msg { color: var(--amber); font-weight: 600; }
  .bpm-ramp { display: inline-flex; align-items: center; gap: 6px; padding: 1px 8px; border: 1px dashed var(--ink-soft);
    border-radius: 6px; font-variant-numeric: tabular-nums; }   /* 0.19: rampa de BPM, sem controle (DEC-036) */
  .bpm-ramp .bpm-ramp-note { color: var(--ink-soft); font-size: 11px; }
````

### E03 — rampa: reconhecer e o valor inicial

**Arquivo:** `app/index.html`

**Ancora:**

````
/** Valor inicial do controle: o numero do style (e o que o Suno ve); sem ele,
    o campo bpm; sem os dois, null (controle vazio). */
function initialBpm(song) {
  const n = bpmIn(song.style);
  return n !== null ? n : (song.bpm || null);
}
````

**Texto novo (substitui a ancora inteira):**

````
/* Rampa de BPM (0.19.0, i-042, DEC-036): dois BPM no MESMO trecho do style
   (entre virgulas), ligados por "to", "building to", "rising to", "climbing to",
   "up to" ou "→" — «95 BPM building to 115 BPM», «95 to 118 BPM». A rampa sai
   byte a byte como foi escrita: o controle nao reescreve nada nela. Dois
   numeros soltos continuam sendo o caso da DEC-020. A MESMA expressao mora no
   scripts/validate.py (RAMP_RE): mudar uma pede mudar a outra. */
const RAMP_RE = /\b(\d{2,3})(?:\s*-?\s*bpm)?\s*(?:building\s+to|rising\s+to|climbing\s+to|up\s+to|to|→)\s*(\d{2,3})\s*-?\s*bpm\b/i;

/** A rampa do style ({from, to}), ou null. Procura trecho a trecho. */
function rampOf(style) {
  for (const frag of String(style || "").split(",")) {
    const m = RAMP_RE.exec(frag);
    if (m && Number(m[1]) !== Number(m[2])) return { from: Number(m[1]), to: Number(m[2]) };
  }
  return null;
}

/** Valor inicial do controle: o numero do style (e o que o Suno ve); sem ele,
    o campo bpm; sem os dois, null (controle vazio). Com rampa, null: o
    controle nao governa nada e o Style sai como esta (DEC-036). */
function initialBpm(song) {
  if (rampOf(song.style)) return null;
  const n = bpmIn(song.style);
  return n !== null ? n : (song.bpm || null);
}
````

### E04 — rampa: o controle vira rótulo

**Arquivo:** `app/index.html`

**Ancora:**

````
function bpmControl(song, card) {
  const box = document.createElement("span"); box.className = "bpm-ctl";
````

**Texto novo (substitui a ancora inteira):**

````
function bpmControl(song, card) {
  const ramp = rampOf(song.style);
  if (ramp) {
    // 0.19 (DEC-036): numa rampa o controle vira rotulo; nada a reescrever.
    const r = document.createElement("span"); r.className = "bpm-ctl bpm-ramp";
    r.title = "Rampa de BPM: o Style vai como está escrito; o controle não mexe numa rampa.";
    r.textContent = "rampa " + ramp.from + " → " + ramp.to + " bpm";
    const note = document.createElement("span"); note.className = "bpm-ramp-note";
    note.textContent = "o controle não mexe numa rampa";
    r.appendChild(note);
    r.sync = () => {};
    return r;
  }
  const box = document.createElement("span"); box.className = "bpm-ctl";
````

### E05 — rampa: módulo de andamento não entra na recomposição

**Arquivo:** `app/index.html`

**Ancora:**

````
  active.forEach(id => {
    const m = App.modulesById[id];
    if (m) m.fragment.split(",").forEach(f => add(rewriteBpm(f, bpm)));
  });
````

**Texto novo (substitui a ancora inteira):**

````
  const ramp = rampOf(song.style);
  active.forEach(id => {
    const m = App.modulesById[id];
    // 0.19: numa rampa, modulo de andamento poria um terceiro BPM (DEC-036)
    if (m && !(ramp && tempoChipBpm(m) !== null)) m.fragment.split(",").forEach(f => add(rewriteBpm(f, bpm)));
  });
````

### E06 — rampa: chips de andamento desligados

**Arquivo:** `app/index.html`

**Ancora:**

````
      chip.setAttribute("aria-pressed", active.has(m.id) ? "true" : "false");
      chip.addEventListener("click", () => {
````

**Texto novo (substitui a ancora inteira):**

````
      chip.setAttribute("aria-pressed", active.has(m.id) ? "true" : "false");
      if (tempoChipBpm(m) !== null && rampOf(song.style)) {
        // 0.19 (DEC-036): numa faixa com rampa, ligar um andamento poria um terceiro BPM
        chip.disabled = true;
        chip.title = "Desligado: esta faixa tem uma rampa de BPM no Style.";
      }
      chip.addEventListener("click", () => {
````

### E07 — rampa: aviso âmbar na linha de qualidade

**Arquivo:** `app/index.html`

**Ancora:**

````
  if (!isHidden("exclude")) findNegations(style, lyrics).forEach(n =>
    el.appendChild(qSpan("«" + n + "»: mais confiável no campo Exclude", "warn")));
  return el;
````

**Texto novo (substitui a ancora inteira):**

````
  if (!isHidden("exclude")) findNegations(style, lyrics).forEach(n =>
    el.appendChild(qSpan("«" + n + "»: mais confiável no campo Exclude", "warn")));
  // 0.19 (DEC-036): a rampa sai como foi escrita, mas o Suno nao a segue
  const ramp = rampOf(style);
  if (ramp) el.appendChild(qSpan("rampa de BPM (" + ramp.from + " → " + ramp.to + "): o Suno não segue mudança de andamento"
    + " numa geração; para crescer, descreva («gradual build») e deixe um BPM", "warn"));
  return el;
````

### E08 — rampa: export .md

**Arquivo:** `app/index.html`

**Ancora:**

````
  const bpmMeta = useRecomposed ? currentBpm(song) : song.bpm;
  if (bpmMeta) meta.push("BPM: " + bpmMeta);
````

**Texto novo (substitui a ancora inteira):**

````
  const bpmMeta = useRecomposed ? currentBpm(song) : song.bpm;
  const rampMeta = rampOf(song.style);   // 0.19: a rampa, como esta no Style
  if (rampMeta) meta.push("BPM: rampa " + rampMeta.from + " → " + rampMeta.to);
  else if (bpmMeta) meta.push("BPM: " + bpmMeta);
````

### E09 — rampa: a coluna BPM da Lista

**Arquivo:** `app/index.html`

**Ancora:**

````
const bpmText = song => { const v = currentBpm(song); return v ? v + " bpm" : "—"; };
````

**Texto novo (substitui a ancora inteira):**

````
const bpmText = song => { const r = rampOf(song.style); if (r) return r.from + "→" + r.to + " bpm";   // 0.19
  const v = currentBpm(song); return v ? v + " bpm" : "—"; };
````

### E10 — docstring: a rampa

**Arquivo:** `scripts/validate.py`

**Ancora:**

````
  5. O BPM de cada faixa e um so: o style nao tem dois numeros diferentes, e o
     campo bpm, quando existe, e o numero do style (DEC-020).
````

**Texto novo (substitui a ancora inteira):**

````
  5. O BPM de cada faixa e um so: o style nao tem dois numeros diferentes, e o
     campo bpm, quando existe, e o numero do style (DEC-020). Uma rampa
     declarada («95 BPM building to 115 BPM», no mesmo trecho) e AVISO, nao
     erro; o campo bpm, se houver, e o numero de partida (DEC-036).
````

### E11 — check_bpm com a rampa

**Arquivo:** `scripts/validate.py`

**Ancora:**

````
def check_bpm(data, rel):
    """O BPM de cada faixa e um so (DEC-020).

    O app governa todo "NN bpm" do style a partir de um valor inicial; style com
    dois numeros, ou campo bpm que nao e o do style, e erro de autoria que o
    controle esconderia. Variantes ficam de fora: cada uma tem o andamento dela.
    """
    bad = []
    for album in data.get("albums", []):
        for song in album.get("songs", []):
            nums = sorted({int(n) for n in BPM_RE.findall(song.get("style", "") or "")})
            field = song.get("bpm")
            where = f"[{album.get('id', '?')} > {song.get('id', '?')}]"
            if len(nums) > 1:
````

**Texto novo (substitui a ancora inteira):**

````
# Rampa de BPM (DEC-036): dois BPM no MESMO trecho do style, ligados por uma das
# seis formas. A mesma expressao do app (RAMP_RE em app/index.html): mudar uma
# pede mudar a outra.
RAMP_RE = re.compile(r"\b(\d{2,3})(?:\s*-?\s*bpm)?\s*(?:building\s+to|rising\s+to|climbing\s+to|up\s+to|to|→)"
                     r"\s*(\d{2,3})\s*-?\s*bpm\b", re.I)


def ramp_of(style):
    """A rampa do style, (partida, chegada), ou None. Procura trecho a trecho."""
    for frag in (style or "").split(","):
        m = RAMP_RE.search(frag)
        if m and int(m.group(1)) != int(m.group(2)):
            return int(m.group(1)), int(m.group(2))
    return None


def check_bpm(data, rel):
    """O BPM de cada faixa e um so (DEC-020), salvo a rampa declarada (DEC-036).

    O app governa todo "NN bpm" do style a partir de um valor inicial; style com
    dois numeros, ou campo bpm que nao e o do style, e erro de autoria que o
    controle esconderia. A rampa («95 BPM building to 115 BPM») o app preserva e
    nao controla: aqui ela e AVISO, e o campo bpm, se houver, e a partida.
    Variantes ficam de fora: cada uma tem o andamento dela.
    """
    bad, ramps = [], []
    for album in data.get("albums", []):
        for song in album.get("songs", []):
            style = song.get("style", "") or ""
            field = song.get("bpm")
            where = f"[{album.get('id', '?')} > {song.get('id', '?')}]"
            ramp = ramp_of(style)
            if ramp:
                rest = [frag for frag in style.split(",") if not RAMP_RE.search(frag)]
                loose = sorted({int(n) for frag in rest for n in BPM_RE.findall(frag)})
                ramps.append(f"{where} rampa de BPM: {ramp[0]} -> {ramp[1]}")
                if loose:
                    bad.append(f"{where} rampa {ramp[0]} -> {ramp[1]} e outro BPM no style: {', '.join(map(str, loose))}")
                elif field is not None and field != ramp[0]:
                    bad.append(f"{where} campo bpm {field}, mas a rampa parte de {ramp[0]}")
                continue
            nums = sorted({int(n) for n in BPM_RE.findall(style)})
            if len(nums) > 1:
````

### E12 — aviso das rampas

**Arquivo:** `scripts/validate.py`

**Ancora:**

````
    if bad:
        print(f"ERRO de BPM em {rel} ({len(bad)} faixa(s)):")
````

**Texto novo (substitui a ancora inteira):**

````
    if ramps:
        print(f"AVISO de BPM em {rel} ({len(ramps)} faixa(s) com rampa; o Suno nao segue mudanca de andamento numa geracao):")
        for r in ramps[:8]:
            print(f"   {r}")
    if bad:
        print(f"ERRO de BPM em {rel} ({len(bad)} faixa(s)):")
````

### E13 — §5: o Cancioneiro preserva a rampa

**Arquivo:** `kit-musica/skills/macetes-suno/SKILL.md`

**Ancora:**

````
  controle de BPM do Cancioneiro. Para acelerar, descreva (`gradual build, accelerating`), não some números.
````

**Texto novo (substitui a ancora inteira):**

````
  controle de BPM do Cancioneiro. Para acelerar, descreva (`gradual build, accelerating`), não some números.
  Se a rampa for escolha consciente, escreva-a num trecho só (`95 BPM building to 115 BPM`): desde a 0.19.0 o
  Cancioneiro a reconhece, copia como está e avisa em âmbar; dois números soltos continuam sendo erro.
````

### E14 — conferência 7: a rampa

**Arquivo:** `kit-musica/skills/revisar-faixa/SKILL.md`

**Ancora:**

````
| 7 | **BPM**: dois números no style, ou campo `bpm` diferente do style | — | um BPM por faixa; rampa («95 to 118 BPM») o app não controla |
````

**Texto novo (substitui a ancora inteira):**

````
| 7 | **BPM**: dois números no style, ou campo `bpm` diferente do style | — | um BPM por faixa; rampa num trecho só («95 BPM building to 115 BPM») o app preserva e avisa, mas o Suno não segue: prefira um BPM e descreva a subida |
````

### E15 — entrada [0.19.0]

**Arquivo:** `meta/CHANGELOG.md`

**Ancora:**

````
## [0.18.0] — 2026-11-09
````

**Texto novo (substitui a ancora inteira):**

````
## [0.19.0] — 2026-11-11

Rampa de BPM (i-042, DEC-036): o Style com rampa sai como foi escrito.

### Fixed
- **A rampa de BPM era reescrita em silêncio.** O controle de BPM (DEC-020) troca todo número de BPM pelo valor dele, e o valor inicial é o primeiro número: «95 BPM building to 115 BPM» copiava como «95 BPM building to 95 bpm», sem ninguém mexer no controle. Afetava as três faixas BR com rampa desde a 0.7.0. Agora a rampa é reconhecida e sai byte a byte.

### Added
- **Rampa reconhecida:** dois BPM no mesmo trecho do Style ligados por `to`, `building to`, `rising to`, `up to`, `climbing to` ou `→`. Dois números soltos continuam sendo o caso da DEC-020.
- Numa faixa com rampa, o controle de BPM vira o rótulo «rampa 95 → 115 bpm», os chips de andamento ficam desligados, a coluna BPM da Lista mostra «95→115 bpm» e a linha de qualidade avisa em âmbar que o Suno não segue mudança de andamento numa geração. O export `.md` leva «BPM: rampa 95 → 115».
- `validate.py`: a rampa declarada é AVISO, não erro; o campo `bpm`, se houver, é o número de partida.

### Changed
- `revisar-faixa` (conferência 7) e `macetes-suno` (§5) dizem que o Cancioneiro preserva a rampa, e continuam recomendando um BPM com a subida descrita.
- CI: o passo «Dependencias» instala o navegador sem depender do `apt` do runner, que ficou sem DNS três vezes em 2026-11-11; as bibliotecas do sistema, já presentes no runner, com três tentativas de 3 minutos.

Spec `meta/specs/261111-rampa-de-bpm.md`: 7 de 7 critérios, com 6 testes novos em `tests/test_bpm.py` (50 no total).

---

## [0.18.0] — 2026-11-09
````

### E16 — estado v0.19.0

**Arquivo:** `README.md`

**Ancora:**

````
> **Estado:** v0.18.0 — ferramenta em uso. Lê, guarda e edita vários acervos, grava direto no arquivo do acervo (Chrome e Edge), copia por campo, troca módulos de estilo, ajusta o BPM, **mede cada prompt contra os limites do Suno**, exporta Markdown, exporta uma faixa como `.json` e **entrega o prompt para chats gerarem canções no esquema**. Publicada no GitHub Pages. Ver `meta/ROADMAP.md`.
````

**Texto novo (substitui a ancora inteira):**

````
> **Estado:** v0.19.0 — ferramenta em uso. Lê, guarda e edita vários acervos, grava direto no arquivo do acervo (Chrome e Edge), copia por campo, troca módulos de estilo, ajusta o BPM, **mede cada prompt contra os limites do Suno**, exporta Markdown, exporta uma faixa como `.json` e **entrega o prompt para chats gerarem canções no esquema**. Publicada no GitHub Pages. Ver `meta/ROADMAP.md`.
````

### E17 — DEC-036

**Arquivo:** `meta/DECISIONS.md`

**Ancora:**

````
**Consequências:** (+) Organizar o acervo inteiro sem editar o `.json` à mão. (+) A descrição do álbum, que estava no esquema desde a fase 1, ganha uso. (−) Excluir álbum é a operação mais destrutiva do app (dezenas de faixas num clique); seguram a confirmação com a contagem, o «Desfazer» e, no arquivo, o aviso de mudança da I4. (−) Dois arrastares na lateral: o teste da I3 que solta faixa sobre álbum da lateral virou teste de regressão (`tests/test_albuns.py`).
````

**Texto novo (substitui a ancora inteira):**

````
**Consequências:** (+) Organizar o acervo inteiro sem editar o `.json` à mão. (+) A descrição do álbum, que estava no esquema desde a fase 1, ganha uso. (−) Excluir álbum é a operação mais destrutiva do app (dezenas de faixas num clique); seguram a confirmação com a contagem, o «Desfazer» e, no arquivo, o aviso de mudança da I4. (−) Dois arrastares na lateral: o teste da I3 que solta faixa sobre álbum da lateral virou teste de regressão (`tests/test_albuns.py`).

## DEC-036 — Rampa de BPM: reconhecida no texto do Style, preservada byte a byte, sem controle, com aviso âmbar; no validador, AVISO (revê a DEC-020)

**Data:** 2026-11-11
**Status:** aceita
**Contexto:** Três faixas BR mudam de andamento de propósito («95 BPM building to 115 BPM»), e o `validate.py` as reprovava pela DEC-020 (i-042). Medido na spec `meta/specs/261111-rampa-de-bpm.md`: o app copiava a rampa com o segundo número trocado pelo primeiro, sem ninguém mexer no controle de BPM. Pesquisa de 2026-11-11: o Suno não segue mudança de andamento numa geração. Os quatro pontos da spec, decididos pelo dono como recomendados `[relatado pelo dono, 2026-11-11]`.
**Decisão:**
- **Rampa = dois BPM no mesmo trecho do Style** (entre vírgulas), ligados por `to`, `building to`, `rising to`, `up to`, `climbing to` ou `→`. Só texto: o esquema não muda. A mesma expressão no app e no `validate.py`.
- **Numa rampa, o Style sai byte a byte;** o controle de BPM vira rótulo, e os chips e módulos de andamento ficam de fora.
- **Aviso âmbar** na linha de qualidade, com a recomendação de um BPM e a subida descrita.
- **No `validate.py`, AVISO** (código 0); o campo `bpm`, se houver, é a partida. Dois números soltos continuam ERRO (DEC-020).
**Alternativas consideradas:** um campo `bpmEnd` no esquema (muda o contrato dos chats); o controle deslocar os dois números juntos (mais código, para algo que o Suno não segue); sem aviso; aviso com um botão que troca a rampa (o app passaria a editar o Style); manter o erro (forçaria editar as três faixas à mão).
**Consequências:** (+) O que se copia é o que está escrito, também na rampa — a promessa da DEC-020. (+) As três faixas passam no `validate.py` com aviso. (−) Uma forma de ligação fora da lista cai na DEC-020 e o validador reprova: falha alta, não silenciosa. (−) A lista de formas mora em dois lugares (app e validador), com um comentário apontando um para o outro.
````

### E18 — i-042 entregue (título)

**Arquivo:** `meta/IDEAS.md`

**Ancora:**

````
### i-042 💡 Rampa de BPM no style («95 BPM to 118 BPM»)
````

**Texto novo (substitui a ancora inteira):**

````
### i-042 ✅ Rampa de BPM no style («95 BPM to 118 BPM»)
````

### E19 — i-042 entregue (linha)

**Arquivo:** `meta/IDEAS.md`

**Ancora:**

````
Achado na conversão BR: três faixas mudam de andamento de propósito. A DEC-020 reprova dois BPM no `validate.py`, e o controle de BPM do cartão igualaria os dois números. Decidir: o controle não aparecer (ou avisar) quando o style tem uma rampa, e o `validate.py` aceitar o par ligado por «to»/«building to», sem perder o erro de autoria que a DEC-020 pega.
````

**Texto novo (substitui a ancora inteira):**

````
Achado na conversão BR: três faixas mudam de andamento de propósito. A DEC-020 reprova dois BPM no `validate.py`, e o controle de BPM do cartão igualaria os dois números. Decidir: o controle não aparecer (ou avisar) quando o style tem uma rampa, e o `validate.py` aceitar o par ligado por «to»/«building to», sem perder o erro de autoria que a DEC-020 pega.
**Entregue (0.19.0, DEC-036):** a rampa (dois BPM no mesmo trecho, ligados por «to» e afins) é reconhecida e sai como foi escrita; o controle vira rótulo e avisa em âmbar; o `validate.py` dá AVISO. Achado na spec: o app reescrevia a rampa em silêncio desde a 0.7.0.
````

### E20 — rampa de BPM

**Arquivo:** `meta/ROADMAP.md`

**Ancora:**

````
- ✅ Controle de BPM no cartão (i-005, DEC-020) — 0.7.0, conferido na tela pelo dono em 2026-10-28; campo numérico, não slider, e o chip de andamento vira atalho.
````

**Texto novo (substitui a ancora inteira):**

````
- ✅ Controle de BPM no cartão (i-005, DEC-020) — 0.7.0, conferido na tela pelo dono em 2026-10-28; campo numérico, não slider, e o chip de andamento vira atalho.
- ✅ Rampa de BPM preservada e avisada (i-042, DEC-036) — 0.19.0.
````

### E21 — versão

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
**Versão atual:** 0.18.0 · **Fase:** 3a, 3a.2, o BPM da 3b, o prompt-modelo e as conveniências de uso concluídos e conferidos · os álbuns antigos convertidos (i-008, fora do repo) · curadoria no app concluída nas três entregas (DEC-028, DEC-029) · frente de interface concluída e conferida nas quatro entregas (DEC-030 a DEC-033) · organizar os álbuns (0.18.0, DEC-035) à espera da conferência na tela · kit de música lido pelo KCM, à espera da resposta (i-039)
````

**Texto novo (substitui a ancora inteira):**

````
**Versão atual:** 0.19.0 · **Fase:** 3a, 3a.2, o BPM da 3b, o prompt-modelo e as conveniências de uso concluídos e conferidos · os álbuns antigos convertidos (i-008, fora do repo) · curadoria no app concluída nas três entregas (DEC-028, DEC-029) · frente de interface concluída e conferida nas quatro entregas (DEC-030 a DEC-033) · organizar os álbuns (0.18.0, DEC-035) conferido · rampa de BPM (0.19.0, DEC-036) à espera da conferência na tela · kit de música lido pelo KCM, à espera da resposta (i-039)
````

### E22 — última conversa

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
## Última conversa (2026-11-09, organizar os álbuns, WO 0034)

- **Ordem das próximas frentes, decidida pelo dono:** organizar os álbuns (i-049) → rampa de BPM (i-042) → importar os prompts prontos dos álbuns como módulos, que fecha a Fase 3b.
- **Organizar os álbuns (0.18.0, DEC-035):** protótipo no canvas, spec `meta/specs/261109-organizar-os-albuns.md` com os cinco pontos decididos pelo dono como recomendados, 10 de 10 critérios e 12 testes novos (`tests/test_albuns.py`), testados pelo chat; falta a conferência na tela pelo dono.
- **WO 0034 aplicada e empurrada (`a67ee01`, 2026-11-11):** 27 edições + `tests/test_albuns.py`, 9 sha1 de chegada conferidos, `validate.py` exit=0 (só sintaxe: `jsonschema` ausente nesta máquina). **CI vermelho, mas sem rodar teste algum:** o run `43036351737` caiu nas duas tentativas no passo «Dependencias» (`apt`: `Temporary failure resolving 'azure.archive.ubuntu.com'`); «Validar», «Conversores» e «Navegador» foram pulados `[medido por instrumento]`. Os 44 testes seguem sem veredito no CI.
- **Este bloco substitui o anterior** (I4 conferida, i-051 e o kit v2, leva 1). O que ele dizia está no CHANGELOG [0.17.0], na DEC-034, na análise `meta/analises/261109-ANALISE-kit-de-musica-v2.md` e em `logs/2026-11-09.md` (Conversas 1 a 6).
````

**Texto novo (substitui a ancora inteira):**

````
## Última conversa (2026-11-11, 0.18 conferida, CI e rampa de BPM, WO 0036)

- **0.18.0 conferida na tela pelo dono** em 2026-11-11 (os 8 itens do roteiro OK `[relatado pelo dono]`): organizar os álbuns está fechado.
- **WO 0035 recusada** na Edição 0 (o HEAD andou para `0d639f7` depois da leitura do chat); o conteúdo dela foi para a WO 0036.
- **CI:** o passo «Dependencias» deixa de depender do `apt` do runner (o navegador sozinho; as bibliotecas do sistema com três tentativas de 3 minutos, sem derrubar o job). Os testes não rodam no CI desde a 0.18.0: o primeiro veredito é o do push da WO 0036.
- **Rampa de BPM (0.19.0, DEC-036):** o app copiava «95 BPM building to 115 BPM» como «95 BPM building to 95 bpm», desde a 0.7.0; agora a rampa sai como foi escrita, com rótulo no lugar do controle, aviso âmbar e AVISO no `validate.py`. Os quatro pontos decididos pelo dono como recomendados; 7 de 7 critérios e 6 testes novos (`tests/test_bpm.py`), testados pelo chat. Falta a conferência na tela pelo dono.
- **Este bloco substitui o anterior, da WO 0034** (organizar os álbuns). O que ele dizia está no CHANGELOG [0.18.0], na spec `meta/specs/261109-organizar-os-albuns.md` e em `logs/2026-11-09.md` e `logs/2026-11-11.md`.
````

### E23 — funciona: a rampa

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
- **Controle de BPM no cartão (0.7.0, DEC-020):** campo 20-300 com `−5`/`+5` e «voltar a N» governa todo «NN bpm» do Style principal; o chip de andamento é atalho (no máximo um ligado); variantes e «Baixar .json» não mudam; o valor é só da sessão.
````

**Texto novo (substitui a ancora inteira):**

````
- **Controle de BPM no cartão (0.7.0, DEC-020):** campo 20-300 com `−5`/`+5` e «voltar a N» governa todo «NN bpm» do Style principal; o chip de andamento é atalho (no máximo um ligado); variantes e «Baixar .json» não mudam; o valor é só da sessão.
- **Rampa de BPM** (0.19.0, DEC-036): dois BPM no mesmo trecho do Style, ligados por «to» e afins, saem como foram escritos; o controle vira o rótulo «rampa 95 → 115 bpm», os chips de andamento ficam desligados e a linha de qualidade avisa em âmbar. O `validate.py` dá AVISO; dois números soltos continuam ERRO.
````

### E24 — quebrado: o CI e a WO 0035

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
- **CI do `a67ee01` sem veredito** — falha de rede do runner no passo «Dependencias», três vezes (duas no run `43036351737`, uma no run `43044109509` do commit do wrap, `45312d5`) — não é pontual. Re-rodar (`gh run rerun 43036351737 --failed`) ou empurrar de novo; se repetir, WO para o passo de instalação do `testes.yml` (cache ou nova tentativa).
- **WO 0035 recusada pelo Code em 2026-11-11 (Edição 0 vermelha):** o HEAD era `0d639f7`, não `45312d5`; a âncora E03 e os sha1 de `meta/STATUS.md` e `logs/2026-11-11.md` já não batiam. Nada aplicado. Falta o chat reemitir a WO sobre `0d639f7`; `meta/specs/261111-rampa-de-bpm.md` e a própria WO seguem sem versionar.
````

**Texto novo (substitui a ancora inteira):**

````
- **CI sem veredito desde a 0.18.0** — o passo «Dependencias» caiu três vezes no `apt` do runner. A WO 0036 muda o passo; conferir o resultado no push dela.
````

### E25 — pendências: conferir a rampa

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
- **Conferir organizar os álbuns na tela** — roteiro na conversa de 2026-11-09 (WO 0034), depois do push, no computador e no celular.
````

**Texto novo (substitui a ancora inteira):**

````
- **Conferir a rampa de BPM na tela** — roteiro na conversa de 2026-11-11 (WO 0036), depois do push, com uma das três faixas BR com rampa.
````

### E26 — backlog: sai a rampa

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
1. **Rampa de BPM** (i-042) — três faixas BR reprovam no `validate.py` por mudarem de andamento de propósito.
````

**Texto novo:** vazio — apague a ancora inteira (a linha e a sua quebra).

### E27 — backlog: renumera 2

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
2. **Importar prompts prontos dos álbuns como módulos** — o último ⬜ da 3b no ROADMAP; o índice-mestre da BR e os «estilos originais» do VOL5 trazem fórmulas de estilo.
````

**Texto novo (substitui a ancora inteira):**

````
1. **Importar prompts prontos dos álbuns como módulos** — o último ⬜ da 3b no ROADMAP; o índice-mestre da BR e os «estilos originais» do VOL5 trazem fórmulas de estilo.
````

### E28 — backlog: renumera 3

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
3. **Kit de música v2, leva 2** (i-039) — as skills `escrever-letra-suno` e `conceber-album`, com prova de campo num projeto de música do dono; depois, a carta 02 ao KCM.
````

**Texto novo (substitui a ancora inteira):**

````
2. **Kit de música v2, leva 2** (i-039) — as skills `escrever-letra-suno` e `conceber-album`, com prova de campo num projeto de música do dono; depois, a carta 02 ao KCM.
````

### E29 — backlog: renumera 4

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
4. **Pesquisar outras plataformas de música por IA** (i-032) — um turno de pesquisa antes de qualquer mudança de esquema.
````

**Texto novo (substitui a ancora inteira):**

````
3. **Pesquisar outras plataformas de música por IA** (i-032) — um turno de pesquisa antes de qualquer mudança de esquema.
````

### E30 — backlog: renumera 5

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
5. **Avisar palavra de andamento que contradiz o BPM** (i-029) — pede uma tabela palavra → faixa de BPM, com fonte e data.
````

**Texto novo (substitui a ancora inteira):**

````
4. **Avisar palavra de andamento que contradiz o BPM** (i-029) — pede uma tabela palavra → faixa de BPM, com fonte e data.
````

### E31 — CI sem apt obrigatorio

**Arquivo:** `.github/workflows/testes.yml`

**Ancora:**

````
          python -m playwright install --with-deps chromium
````

**Texto novo (substitui a ancora inteira):**

````
          python -m playwright install chromium
          # As bibliotecas do sistema ja vem no runner do GitHub. O apt do runner as vezes
          # fica sem DNS (2026-11-11, run 43036351737): tres tentativas de 3 minutos, e o job
          # segue se falharem. Faltando biblioteca de verdade, o passo «Navegador» acusa.
          for i in 1 2 3; do
            timeout 180 python -m playwright install-deps chromium && break
            echo "install-deps falhou ($i de 3)"; sleep 15
          done
````

### E32 — arquivo novo: os testes da rampa

**Arquivo novo:** `tests/test_bpm.py` — crie com exatamente o conteudo abaixo (termina com uma quebra de linha).

````
"""Rampa de BPM (0.19.0, i-042, DEC-036; criterios da spec meta/specs/261111-rampa-de-bpm.md).
Faixas sinteticas, feitas a partir do data/demo.json."""
import copy
import json
import os
import subprocess
import sys
import tempfile

from conftest import DEMO, ROOT, import_demo, write_tmp_collection

RAMP = "dream pop, soft female vocal, 95 BPM building to 115 BPM, warm synths"


def coll_with(styles, bpms=None, tempo_module=False):
    """Acervo de um album com uma faixa por style (ids r0, r1...)."""
    coll = copy.deepcopy(DEMO)
    base = copy.deepcopy(DEMO["albums"][0]["songs"][0])
    songs = []
    for i, st in enumerate(styles):
        s = copy.deepcopy(base)
        s.update(id=f"r{i}", title=f"Faixa {i + 1}", style=st)
        s.pop("bpm", None)
        s["styleModules"] = []
        if bpms and bpms[i] is not None:
            s["bpm"] = bpms[i]
        songs.append(s)
    coll["albums"] = [{"id": "a", "title": "A", "songs": songs}]
    if tempo_module:
        coll.setdefault("styleModules", []).append(
            {"id": "tempo-100", "label": "midtempo 100", "category": "tempo", "fragment": "midtempo 100 bpm"})
    return coll


def copied_style(page, sid):
    page.click(f'#main li.row[data-id="{sid}"] [data-role="row-style"]')
    page.wait_for_timeout(150)
    return page.evaluate("navigator.clipboard.readText()")


def test_c1_rampa_sai_byte_a_byte(open_app):
    page = open_app()
    import_demo(page, write_tmp_collection(coll_with([RAMP])))
    assert copied_style(page, "r0") == RAMP
    page.click('#main li.row[data-id="r0"] .row-open')
    assert page.text_content('#detail [data-role="style-block"]') == RAMP


def test_c2_formas_de_ligacao(open_app):
    yes = ["pop, 95 BPM to 118 BPM", "pop, 95 bpm building to 115 bpm", "pop, 90 bpm rising to 120 bpm",
           "pop, 90 bpm up to 120 bpm", "pop, 90 bpm climbing to 120 bpm", "pop, 90 → 120 bpm", "pop, 95 to 118 BPM"]
    no = ["pop, 95 bpm, 115 bpm", "pop, 95 bpm 115 bpm", "pop, 95 bpm"]
    page = open_app()
    got = page.evaluate("xs => xs.map(s => rampOf(s))", yes + no)
    assert all(got[: len(yes)]) and not any(got[len(yes):]), got


def test_c3_rotulo_chips_e_aviso(open_app):
    page = open_app()
    import_demo(page, write_tmp_collection(coll_with([RAMP], tempo_module=True)))
    page.click('#main li.row[data-id="r0"] .row-open')
    assert "rampa 95 → 115 bpm" in page.text_content("#detail .bpm-ramp")
    assert page.eval_on_selector_all("#detail .bpm-ctl input", "e => e.length") == 0
    page.evaluate("document.querySelectorAll('#detail details').forEach(d => d.open = true)")
    chip = page.locator('#detail button.chip[data-mid="tempo-100"]')
    assert chip.is_disabled()
    assert "rampa de BPM (95 → 115)" in page.text_content('#detail [data-role="style-quality"]')
    assert page.text_content('#main li.row[data-id="r0"]').count("95→115 bpm") == 1


def test_c4_bpm_unico_continua_controlado(open_app):
    """Falso positivo: faixa com um BPM, como na 0.18.0 (DEC-020)."""
    page = open_app()
    import_demo(page, write_tmp_collection(coll_with(["pop, 100 bpm, warm synths"])))
    page.click('#main li.row[data-id="r0"] .row-open')
    page.click('#detail .bpm-ctl button[aria-label="aumentar 5 BPM"]')
    assert page.text_content('#detail [data-role="style-block"]') == "pop, 105 bpm, warm synths"
    assert page.eval_on_selector_all("#detail .bpm-ramp", "e => e.length") == 0


def test_c5_export_md(open_app):
    page = open_app()
    import_demo(page, write_tmp_collection(coll_with([RAMP])))
    page.click('#main li.row[data-id="r0"] .row-more')
    with page.expect_download() as d:
        page.click("#tm-md")
    md = open(d.value.path(), encoding="utf-8").read()
    assert RAMP in md and "BPM: rampa 95 → 115" in md


def test_c6_validate(tmp_path):
    styles = ["pop, 95 BPM building to 115 BPM", "pop, 95 to 118 BPM", "pop, 90 → 120 bpm", "pop, 95 bpm, 115 bpm"]
    path = tmp_path / "rampas.json"
    path.write_text(json.dumps(coll_with(styles, [None, 95, 120, None]), ensure_ascii=False), encoding="utf-8")
    out = subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "validate.py"), str(path)],
                         capture_output=True, text=True).stdout
    assert "AVISO de BPM" in out and "[a > r0] rampa de BPM: 95 -> 115" in out
    assert "[a > r1]" not in out.split("ERRO de BPM")[-1]           # bpm = partida: passa
    assert "[a > r2] campo bpm 120, mas a rampa parte de 90" in out  # bpm = chegada: erro
    assert "[a > r3] o style tem 2 BPM diferentes: 95, 115" in out   # dois soltos: erro
    only_ramps = tmp_path / "so-rampas.json"
    only_ramps.write_text(json.dumps(coll_with(styles[:2], [None, 95]), ensure_ascii=False), encoding="utf-8")
    r = subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "validate.py"), str(only_ramps)],
                       capture_output=True, text=True)
    assert "ERRO de BPM" not in r.stdout
````

## Depois de aplicar — conferencia antes do commit

| # | Checagem | Comando | Esperado |
|---|---|---|---|
| 1 | Os arquivos sao os previstos | `sha1sum .github/workflows/testes.yml README.md app/index.html kit-musica/skills/macetes-suno/SKILL.md kit-musica/skills/revisar-faixa/SKILL.md meta/CHANGELOG.md meta/DECISIONS.md meta/IDEAS.md meta/ROADMAP.md meta/STATUS.md scripts/validate.py tests/test_bpm.py meta/specs/261111-rampa-de-bpm.md logs/2026-11-11.md meta/workorders/261111-wo0035-ci-e-0-18-conferida.md` | a coluna **chegada** |
| 2 | Versao | `grep -c 'data-role="app-version">v0.19.0<' app/index.html` | `1` |
| 3 | A mesma expressao nos dois lugares | `grep -c '^const RAMP_RE' app/index.html` e `grep -c '^RAMP_RE' scripts/validate.py` | `1` e `1` |
| 4 | O CI sem `--with-deps` | `grep -c 'with-deps' .github/workflows/testes.yml` | `0` |
| 5 | Validacao | `python3 scripts/validate.py; echo "exit=$?"` | `exit=0`, versao 0.19.0 |
| 6 | Testes, se o ambiente local tiver pytest e Playwright | `python -m pytest tests -q` | `50 passed`; sem o ambiente, diga «nao rodado» — a checagem 8 responde |
| 7 | Nada alem do previsto | `GIT_OPTIONAL_LOCKS=0 git status --short --untracked-files=all` | os 15 arquivos da tabela e esta WO |
| 8 | Depois do push: o CI | `gh run list --limit 1`, em laco com `gh run view <id> --json status,conclusion` ate `completed` (o `gh run watch` passa dos 300 s) | relate o estado cru e, se vermelho, o passo que caiu (`gh run view <id> --log-failed`, as ultimas 30 linhas) |

As checagens 2 a 5 rodaram no clone do chat, shell Linux; no Git Bash, **nao testado**. O chat rodou os 50 testes duas vezes (45 s) e mediu que 5 dos 6 novos reprovam na 0.18.0 (o sexto e o falso positivo, que passa nas duas). O workflow so se testa no GitHub: o chat conferiu o YAML e a sintaxe do bash.
**Esta e qual pergunta?** A 1 responde «esta la?»; a 8 e a primeira vez que os testes rodam no CI desde a 0.18.0, e a resposta a «o passo novo segura a falha do apt?».

## Relatorio de aplicacao

Grave em `../AAMMDD-HHMM-code-cancioneiro-apply-wo0036.txt`, com o carimbo de `date +%y%m%d-%H%M` rodado na hora. Checagem 1 em primeiro lugar e o estado final do CI. **Sem `/wrap` depois desta WO**, e sem secao sua no log, salvo se algo fugir do literal.

## Commit

```
git add .github/workflows/testes.yml README.md app/index.html kit-musica/skills/macetes-suno/SKILL.md kit-musica/skills/revisar-faixa/SKILL.md meta/CHANGELOG.md meta/DECISIONS.md meta/IDEAS.md meta/ROADMAP.md meta/STATUS.md scripts/validate.py tests/test_bpm.py meta/specs/261111-rampa-de-bpm.md logs/2026-11-11.md meta/workorders/261111-wo0035-ci-e-0-18-conferida.md meta/workorders/261111-wo0036-rampa-de-bpm.md
```

```
git commit -m "feat: rampa de BPM preservada e avisada (0.19.0)" -m "A rampa no mesmo trecho do Style sai byte a byte; o controle de BPM vira rotulo, os chips de andamento desligam e a linha de qualidade avisa. validate.py: rampa e AVISO (DEC-036, i-042). 6 testes novos. CI instala o navegador sem depender do apt. Conteudo da WO 0035, recusada, incluido."
```

```
git push
```
