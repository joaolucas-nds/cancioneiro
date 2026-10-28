# WO 0013 — Fase 3b: o controle de BPM no cartao (e o FIX-008)

## Cabecalho

> **Tipo:** WO de CODIGO (`app/index.html`, `scripts/validate.py`) e de registro.
> **Config sugerida:** Sonnet · `/effort medium`. 23 edicoes literais e um STATUS inteiro, todos aplicados e testados pelo chat numa copia; cada arquivo tem hash de chegada.
> **Pre-requisito:** commit `4aac175`, branch `main`, sincronizada com `origin/main`. **A arvore NAO esta limpa:** `meta/specs/261028-controle-de-bpm.md` e nova (a spec, gravada pelo chat no turno de 2026-10-28; esta WO a edita e a versiona). Nada mais deve aparecer no `git status` alem dela e desta WO.
> **Base:** `meta/specs/261028-controle-de-bpm.md`, Decisoes **1a, 2a, 3a, 4a**, dadas pelo dono em 2026-10-28.
> **Depende de:** WO 0012, ja aplicada.
>
> **Arquivos que esta WO edita — partida e chegada, os dois medidos pelo chat** (chegada = resultado de aplicar literalmente as edicoes abaixo, em LF):
>
> | arquivo | partida (sha1) | chegada (sha1) |
> |---|---|---|
> | `app/index.html` | `6785fca2a47d8fa52a85ac893bd42e171c58e7d7` | `97fe1b3c0c97d4ffe521516f99ec35cae78ea716` |
> | `scripts/validate.py` | `454a39a4d58ed29ed7c86de935f74fdefbf4038c` | `1836d811b1809065e96c55b5d1a286c6fcd7f719` |
> | `meta/DECISIONS.md` | `33be6019f84d077e6b08169eb5161cbaa4b85b52` | `2dc9f1ddf4d0ab1dabce5e6c8768d8e8e23718b9` |
> | `meta/IDEAS.md` | `9e56969d5abf53744d0d684f620a9792886bddea` | `b0e541063bc49e5521ef053f90b2f08ea9b53966` |
> | `meta/ROADMAP.md` | `a01c4533c8de87b36ab6b8216fd0728693868c45` | `2d7db572c56b03f08200b29766558ee3b706d326` |
> | `meta/HISTORY.md` | `9f93e07d94baa5448d98853ed5b67f697580621f` | `f04af0c5081f4546995620456b14faae00a7ea23` |
> | `meta/STATUS.md` | `c3b3b656a2133b69f44eba7985d0b794f31eacc2` | `537a9085f9c1bce2df7937e329bc11a1d1bf2bbf` |
> | `meta/specs/261028-controle-de-bpm.md` | `94f1c597190756f4497d275baff28c5a42d433ef` | `153c60b14c1e7f2d159f13d0046fc3a9906d3ae5` |
>
> **Ancora semantica:** se um trecho-ancora nao bater EXATAMENTE, PARE e reporte.
> **Idempotencia:** antes de cada edicao, procure o texto NOVO INTEIRO; se ja estiver la, PULE e diga no relatorio.
>
> **Ancoras lidas em:** cada ancora foi lida pelo chat direto do disco no turno de 2026-10-28 e conferida como ocorrendo **exatamente 1 vez** no arquivo de partida (`str.count`), aplicadas na ordem abaixo. O texto literal esta em cada edicao.

---

## 1. Por que

A camada Andamento do painel de modulos nunca mudou o BPM: em 49 de 49 cliques ela punha um segundo
numero no prompt. E a i-005, pedido da premissa original, queria o BPM manipulavel no cartao. A spec
mediu, o dono decidiu, e esta WO entrega (DEC-020):

- **Um controle no lugar do «128 BPM»** da linha de metadados: campo numerico 20-300, `−5`/`+5` e
  «voltar a N». Ele reescreve **todo** «NN bpm» do Style principal — base e modulos —, no lugar,
  antes da dedup. Variantes ficam de fora. So da sessao, como os modulos.
- **O chip de andamento vira atalho:** ligar move o controle para o numero dele; no maximo um ligado.
- **O `validate.py` ganha a quinta checagem:** um BPM so por faixa, e o campo `bpm` igual ao do style.
- **FIX-008, achado ao implementar:** filtro, busca e «marcar usei» religavam os chips do acervo, mas
  o bloco de Style seguia com o clique. O estado de sessao agora sobrevive ao re-render e so volta ao
  acervo ao importar de novo.

O `app/index.html` de chegada (`97fe1b3c…`) foi executado pelo chat em Chromium
headless, nos dois temas: **44 de 44** criterios passaram — a lista esta no «Desfecho» da spec. No
valor original, **todo bloco e o export MD saem byte a byte iguais aos da 0.6.0**, no album do dono e
no `data/demo.json`.

**Nao ha versao nova nesta WO.** A 0.7.0 fecha depois da conferencia na tela, como a 0.6.0 fechou.
**O STATUS vai literal, no apply** — nada «a cargo do `/wrap`».

## Edicao 0 — Conferencia de hash e de arvore

```
sha1sum app/index.html scripts/validate.py meta/DECISIONS.md meta/IDEAS.md meta/ROADMAP.md meta/HISTORY.md meta/STATUS.md meta/specs/261028-controle-de-bpm.md
GIT_OPTIONAL_LOCKS=0 git status --short
```

Os oito batem com a coluna **partida**, e o `git status` mostra **so**
`?? meta/specs/261028-controle-de-bpm.md` e esta WO. Qualquer outra coisa: **PARE e reporte**.

## Edicoes 01 a 23

Na ordem. Quase todas sao «trocar mantendo e acrescentando» — o texto novo **comeca com a ancora** —,
por isso a idempotencia e pelo texto novo INTEIRO. Copie o que esta ENTRE as linhas de quatro crases,
sem elas. A Edicao 24 (STATUS) e diferente: nao tem ancora, e o arquivo inteiro.

### E01 — CSS do controle de BPM — `app/index.html`

**Ancora, literal:**

````
  .chip .cost { margin-left: 6px; opacity: .75; font-variant-numeric: tabular-nums; }
````

**Texto novo, literal:**

````
  .chip .cost { margin-left: 6px; opacity: .75; font-variant-numeric: tabular-nums; }
  /* Controle de BPM (3b, DEC-020): mora na linha de metadados, fora de todo bloco copiavel. */
  .bpm-ctl { display: inline-flex; align-items: center; gap: 4px; flex-wrap: wrap; }
  .bpm-ctl input {
    width: 4.4em; font-family: var(--mono); font-size: 12px; padding: 1px 4px;
    border: 1px solid var(--line); border-radius: 6px; background: var(--paper); color: var(--ink);
  }
  .bpm-ctl button { font-size: 11px; padding: 1px 7px; }
  .bpm-ctl .bpm-msg { color: var(--amber); font-weight: 600; }
````

### E02 — estado do BPM no App — `app/index.html`

**Ancora, literal:**

````
  activeModules: {},
````

**Texto novo, literal:**

````
  activeModules: {},
  // BPM escolhido no controle, por song.id (DEC-020). Mesma regra: so da sessao,
  // nunca na colecao. Ausente = o valor inicial da faixa (initialBpm).
  bpm: {},
````

### E03 — colecao nova zera o estado de sessao — `app/index.html`

**Ancora, literal:**

````
  App.collection = json;
  App.modulesById = {};
````

**Texto novo, literal:**

````
  App.collection = json;
  // Estado de sessao e por colecao: importar de novo volta ao acervo (FIX-008).
  App.activeModules = {};
  App.bpm = {};
  App.modulesById = {};
````

### E04 — export MD: o BPM do controle na linha de metadados — `app/index.html`

**Ancora, literal:**

````
  if (song.bpm) meta.push("BPM: " + song.bpm);
````

**Texto novo, literal:**

````
  // Com o Style recomposto, o BPM e o do controle (DEC-020) — o mesmo numero do
  // bloco, nunca um aqui e outro la. Sem recompor, o do acervo.
  const bpmMeta = useRecomposed ? currentBpm(song) : song.bpm;
  if (bpmMeta) meta.push("BPM: " + bpmMeta);
````

### E05 — funcoes do BPM, antes da recomposicao — `app/index.html`

**Ancora, literal:**

````
/* ===================================================================
   Recomposicao de style a partir dos modulos ligados
````

**Texto novo, literal:**

````
/* ===================================================================
   Controle de BPM (Fase 3b — spec meta/specs/261028-controle-de-bpm.md, DEC-020)
   O BPM vai para o Suno como texto no Style ("128 bpm"). O controle governa
   TODO "NN bpm" do Style principal — base e fragmentos dos modulos —, antes da
   dedup: assim nunca saem dois numeros (medido na 0.6.0: 49 de 49 cliques em
   chip de andamento punham um segundo BPM). Variantes ficam de fora: cada uma
   tem o andamento dela. Estado so da sessao, como os modulos (FIX-004).
   =================================================================== */
const BPM_RE = /\b(\d{2,3})\s*-?\s*bpm\b/gi;
const BPM_MIN = 20, BPM_MAX = 300;   // os mesmos limites do campo bpm no esquema

/** Primeiro numero de BPM de um texto, ou null. */
function bpmIn(text) {
  const m = new RegExp(BPM_RE.source, "i").exec(text || "");
  return m ? Number(m[1]) : null;
}
/** Valor inicial do controle: o numero do style (e o que o Suno ve); sem ele,
    o campo bpm; sem os dois, null (controle vazio). */
function initialBpm(song) {
  const n = bpmIn(song.style);
  return n !== null ? n : (song.bpm || null);
}
/** Valor em vigor no controle para a faixa, nesta sessao. */
function currentBpm(song) {
  return song.id in App.bpm ? App.bpm[song.id] : initialBpm(song);
}
/** Reescreve todo "NN bpm" de um texto para v. Ocorrencia que ja diz v fica
    como esta — no valor original nada muda, byte a byte. v nulo: nada muda. */
function rewriteBpm(text, v) {
  if (v === null || v === undefined) return text;
  return text.replace(BPM_RE, (m, n) => (Number(n) === v ? m : v + " bpm"));
}
/** Numero de um modulo de andamento — o chip-atalho —, ou null se nao for um. */
function tempoChipBpm(m) {
  return m && m.category === "tempo" ? bpmIn(m.fragment) : null;
}
/** Muda o BPM pelo controle. O chip de andamento ligado com outro numero se
    desliga; voltar ao numero dele nao o religa (o chip e atalho, nao espelho). */
function setBpmFromControl(song, card, v) {
  App.bpm[song.id] = v;
  const active = App.activeModules[song.id];
  if (active) active.forEach(id => {
    const n = tempoChipBpm(App.modulesById[id]);
    if (n !== null && n !== v) active.delete(id);
  });
  refreshCardStyle(song, card);
}

/** Atualiza tudo o que depende do Style recomposto num cartao: o bloco
    copiavel, a linha de qualidade, o recomposto do painel, os chips e seus
    custos, o controle de BPM. Um caminho so para o clique no chip e para o
    controle: dois caminhos deixariam um deles com numero velho (FIX-007). */
function refreshCardStyle(song, card) {
  const composed = recomposedStyle(song);
  const styleBlock = card.querySelector('[data-role="style-block"]');
  if (styleBlock) styleBlock.textContent = composed;
  const oldQ = card.querySelector('[data-role="style-quality"]');
  if (oldQ) oldQ.replaceWith(styleQuality(composed, song.lyrics, baseTagCount(song)));
  const rec = card.querySelector(".recomposed");
  if (rec) rec.textContent = composed;
  const mods = card.querySelector(".modules-details");
  if (mods && mods.syncChips) mods.syncChips();
  const ctl = card.querySelector(".bpm-ctl");
  if (ctl && ctl.sync) ctl.sync();
}

/** O controle de BPM do cartao (DEC-020): campo numerico, -5/+5 e "voltar a N".
    Fica na linha de metadados — referencia que edita o conteudo, nunca dentro
    dele. Valor invalido nao chega ao Style: nunca "NaN bpm" no prompt. */
function bpmControl(song, card) {
  const box = document.createElement("span"); box.className = "bpm-ctl";
  const orig = initialBpm(song);
  const mk = (txt, label) => {
    const b = document.createElement("button"); b.type = "button"; b.textContent = txt;
    if (label) b.setAttribute("aria-label", label);
    return b;
  };
  const minus = mk("\u22125", "diminuir 5 BPM");
  const inp = document.createElement("input");
  inp.type = "number"; inp.min = BPM_MIN; inp.max = BPM_MAX; inp.step = 1;
  inp.placeholder = "\u2014"; inp.setAttribute("aria-label", "BPM do Style");
  const unit = document.createElement("span"); unit.textContent = "BPM";
  const plus = mk("+5", "aumentar 5 BPM");
  const back = mk("");
  const msg = document.createElement("span"); msg.className = "bpm-msg";
  [minus, inp, unit, plus, back, msg].forEach(el => box.appendChild(el));

  box.sync = () => {
    const v = currentBpm(song);
    if (document.activeElement !== inp) inp.value = v === null ? "" : String(v);
    minus.disabled = plus.disabled = v === null;
    back.hidden = v === orig;
    back.textContent = orig === null ? "limpar" : "voltar a " + orig;
    msg.textContent = "";
    inp.removeAttribute("aria-invalid");
  };
  const step = d => {
    const v = currentBpm(song);
    if (v !== null) setBpmFromControl(song, card, Math.min(BPM_MAX, Math.max(BPM_MIN, v + d)));
  };
  minus.addEventListener("click", () => step(-5));
  plus.addEventListener("click", () => step(5));
  back.addEventListener("click", () => setBpmFromControl(song, card, orig));
  inp.addEventListener("input", () => {
    const raw = inp.value.trim();
    if (raw === "" && orig === null) { setBpmFromControl(song, card, null); return; }
    const n = Number(raw);
    if (raw === "" || !Number.isInteger(n) || n < BPM_MIN || n > BPM_MAX) {
      // o Style fica como estava; ao sair do campo, ele volta a mostrar o valor em vigor
      inp.setAttribute("aria-invalid", "true");
      msg.textContent = "use " + BPM_MIN + " a " + BPM_MAX;
      return;
    }
    setBpmFromControl(song, card, n);
  });
  inp.addEventListener("blur", () => box.sync());
  box.sync();
  return box;
}

/* ===================================================================
   Recomposicao de style a partir dos modulos ligados
````

### E06 — recomposedStyle recebe o BPM — `app/index.html`

**Ancora, literal:**

````
function recomposedStyle(song, activeOverride) {
  // activeOverride: conjunto hipotetico de modulos ligados, para medir o custo de
  // um chip sem tocar no estado da tela (3a.2). Sem ele, vale o estado atual.
  const active = activeOverride || App.activeModules[song.id] || new Set(song.styleModules || []);
````

**Texto novo, literal:**

````
function recomposedStyle(song, activeOverride, bpmOverride) {
  // activeOverride: conjunto hipotetico de modulos ligados, para medir o custo de
  // um chip sem tocar no estado da tela (3a.2). Sem ele, vale o estado atual.
  // bpmOverride: o mesmo para o BPM (custo do chip-atalho de andamento, DEC-020).
  const active = activeOverride || App.activeModules[song.id] || new Set(song.styleModules || []);
  const bpm = bpmOverride !== undefined ? bpmOverride : currentBpm(song);
````

### E07 — o BPM reescrito antes da dedup — `app/index.html`

**Ancora, literal:**

````
  // base primeiro (as primeiras palavras pesam mais no Suno)
  song.style.split(",").forEach(add);
  // depois os fragmentos dos modulos ativos que agreguem algo novo
  active.forEach(id => {
    const m = App.modulesById[id];
    if (m) m.fragment.split(",").forEach(add);
  });
  return frags.join(", ");
````

**Texto novo, literal:**

````
  // base primeiro (as primeiras palavras pesam mais no Suno). O BPM e reescrito
  // ANTES da dedup: "128 bpm" do base e "70 bpm" de um modulo viram o mesmo
  // numero, e a dedup tira o repetido (DEC-020).
  song.style.split(",").forEach(f => add(rewriteBpm(f, bpm)));
  // depois os fragmentos dos modulos ativos que agreguem algo novo
  active.forEach(id => {
    const m = App.modulesById[id];
    if (m) m.fragment.split(",").forEach(f => add(rewriteBpm(f, bpm)));
  });
  // controle preenchido e nenhum BPM no texto: entra no fim (+1 tag, que o painel conta)
  if (bpm !== null && !frags.some(f => bpmIn(f) !== null)) frags.push(bpm + " bpm");
  return frags.join(", ");
````

### E08 — custo do chip-atalho de andamento — `app/index.html`

**Ancora, literal:**

````
  Object.keys(App.modulesById).forEach(id => {
    const w = new Set(active);
    if (w.has(id)) w.delete(id); else w.add(id);
    out[id] = Math.abs(countTags(recomposedStyle(song, w)) - now);
  });
````

**Texto novo, literal:**

````
  Object.keys(App.modulesById).forEach(id => {
    const w = new Set(active);
    let bpm;   // undefined = o BPM em vigor
    if (w.has(id)) w.delete(id);
    else {
      w.add(id);
      // chip de andamento e atalho (DEC-020): ligar desliga o outro e move o BPM
      const chipBpm = tempoChipBpm(App.modulesById[id]);
      if (chipBpm !== null) {
        w.forEach(o => { if (o !== id && tempoChipBpm(App.modulesById[o]) !== null) w.delete(o); });
        bpm = chipBpm;
      }
    }
    out[id] = Math.abs(countTags(recomposedStyle(song, w, bpm)) - now);
  });
````

### E09 — o controle no lugar do «128 BPM» — `app/index.html`

**Ancora, literal:**

````
  if (song.bpm) { const b = document.createElement("span"); b.textContent = song.bpm + " BPM"; meta.appendChild(b); }
````

**Texto novo, literal:**

````
  // o BPM deixa de ser so referencia: e o controle que governa o "NN bpm" do Style (DEC-020)
  meta.appendChild(bpmControl(song, card));
````

### E10 — o estado dos modulos sobrevive ao re-render (FIX-008) — `app/index.html`

**Ancora, literal:**

````
  const active = new Set(song.styleModules || []);
  App.activeModules[song.id] = active;
````

**Texto novo, literal:**

````
  // FIX-008: o estado sobrevive ao re-render (filtro, busca, «marcar usei»). Antes,
  // cada render religava os chips do acervo, mas o bloco de Style — montado antes,
  // com o estado antigo — seguia com o clique: chip e texto copiado divergiam.
  const active = App.activeModules[song.id] || new Set(song.styleModules || []);
  App.activeModules[song.id] = active;
````

### E11 — o clique no chip vai pelo caminho unico — `app/index.html`

**Ancora, literal:**

````
      chip.addEventListener("click", () => {
        const on = active.has(m.id);
        if (on) active.delete(m.id); else active.add(m.id);
        chip.classList.toggle("on");
        chip.setAttribute("aria-pressed", on ? "false" : "true");
        const composed = recomposedStyle(song);
        recompUI.textContent = composed;
        // atualiza o bloco copiavel de Style do cartao (seletor explicito)
        const styleBlock = card.querySelector('[data-role="style-block"]');
        if (styleBlock) styleBlock.textContent = composed;
        const oldQ = card.querySelector('[data-role="style-quality"]');
        if (oldQ) oldQ.replaceWith(styleQuality(composed, song.lyrics, baseTagCount(song)));
        // as contribuicoes interagem pelo dedup: um numero velho num chip vizinho
        // seria o FIX-007 de novo. Recalcula todos.
        refreshCosts();
      });
````

**Texto novo, literal:**

````
      chip.addEventListener("click", () => {
        const on = active.has(m.id);
        if (on) active.delete(m.id); else active.add(m.id);
        // chip de andamento e atalho (DEC-020): no maximo um ligado, e ligar move o BPM
        const chipBpm = tempoChipBpm(m);
        if (!on && chipBpm !== null) {
          active.forEach(o => { if (o !== m.id && tempoChipBpm(App.modulesById[o]) !== null) active.delete(o); });
          App.bpm[song.id] = chipBpm;
        }
        // bloco, qualidade, recomposto, TODOS os chips e custos (o dedup faz um
        // chip mexer no custo do vizinho), controle de BPM: um caminho so
        refreshCardStyle(song, card);
      });
````

### E12 — syncChips: estado de todos os chips a partir do conjunto — `app/index.html`

**Ancora, literal:**

````
  wrap.addEventListener("toggle", refreshCosts);
  return wrap;
````

**Texto novo, literal:**

````
  wrap.addEventListener("toggle", refreshCosts);
  /* Redesenha ligado/desligado de todos os chips a partir do conjunto: o
     chip-atalho de andamento desliga um vizinho, e o controle de BPM desliga
     o chip de andamento sem clique nele. Depois, os custos. */
  wrap.syncChips = () => {
    box.querySelectorAll("button.chip").forEach(c => {
      const on = active.has(c.dataset.mid);
      c.classList.toggle("on", on);
      c.setAttribute("aria-pressed", on ? "true" : "false");
    });
    refreshCosts();
  };
  return wrap;
````

### E13 — docstring: a quinta checagem — `scripts/validate.py`

**Ancora, literal:**

````
  4. A versao e a mesma no topo do meta/CHANGELOG.md, no app, no README e no
     STATUS (i-027).
````

**Texto novo, literal:**

````
  4. A versao e a mesma no topo do meta/CHANGELOG.md, no app, no README e no
     STATUS (i-027).
  5. O BPM de cada faixa e um so: o style nao tem dois numeros diferentes, e o
     campo bpm, quando existe, e o numero do style (DEC-020).
````

### E14 — check_bpm, antes de check_version — `scripts/validate.py`

**Ancora, literal:**

````
def check_version():
````

**Texto novo, literal:**

````
BPM_RE = re.compile(r"\b(\d{2,3})\s*-?\s*bpm\b", re.I)  # a mesma regra do app


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
                bad.append(f"{where} o style tem {len(nums)} BPM diferentes: {', '.join(map(str, nums))}")
            elif field is not None and not nums:
                bad.append(f"{where} campo bpm {field}, mas o style nao tem BPM")
            elif field is not None and nums[0] != field:
                bad.append(f"{where} campo bpm {field}, mas o style diz {nums[0]}")
    if bad:
        print(f"ERRO de BPM em {rel} ({len(bad)} faixa(s)):")
        for b in bad[:8]:
            print(f"   {b}")
        return 1
    return 0


def check_version():
````

### E15 — check_bpm no modo degradado — `scripts/validate.py`

**Ancora, literal:**

````
            errors += check_module_refs(data, rel)
            continue
````

**Texto novo, literal:**

````
            errors += check_module_refs(data, rel)
            errors += check_bpm(data, rel)
            continue
````

### E16 — check_bpm no modo com esquema — `scripts/validate.py`

**Ancora, literal:**

````
        # referencia cruzada: o schema nao alcanca isto
        errors += check_module_refs(data, rel)
````

**Texto novo, literal:**

````
        # referencia cruzada e BPM: o schema nao alcanca isto
        errors += check_module_refs(data, rel)
        errors += check_bpm(data, rel)
````

### E17 — spec: status Decidida — `meta/specs/261028-controle-de-bpm.md`

**Ancora, literal:**

````
> **Status:** Aberta — aguarda as Decisoes 1 a 4 do dono.
````

**Texto novo, literal:**

````
> **Status:** Decidida
> **Decidida em:** 2026-10-28 pelo dono — **1a, 2a, 3a, 4a** (as quatro recomendadas). Aplicacao:
> `meta/workorders/261028-wo0013-controle-de-bpm.md`. Implementacao testada numa copia antes de
> virar WO: 44 de 44 criterios passaram (ver «Desfecho», no fim).
````

### E18 — spec: Desfecho — `meta/specs/261028-controle-de-bpm.md`

**Ancora, literal:**

````
Responda, por exemplo: «1a 2a 3a 4a».
````

**Texto novo, literal:**

````
Responda, por exemplo: «1a 2a 3a 4a».

---

## Desfecho — 2026-10-28

**Resposta do dono:** «1a 2a 3a 4a».

**Uma coisa que a implementacao revelou (FIX-008):** o estado dos modulos ja se perdia pela metade a
cada re-render. Filtro, busca e «marcar usei» redesenham os cartoes; o painel religava os chips do
acervo, mas o bloco de Style — montado antes dele, com o estado antigo — continuava com o clique.
Medido na 0.6.0: em ar-01, desligar um chip e digitar na busca deixava o bloco com 298 caracteres (o
clique) e os 7 chips acesos (o acervo). O controle de BPM teria o mesmo defeito; a correcao e a
mesma para os dois: o estado de sessao sobrevive ao re-render e so volta ao acervo ao importar de novo.

**Duas precisoes que a implementacao pediu:**
- **Campo `bpm` sem numero no `style`** tambem e divergencia para o validador (Decisao 4): o campo
  diria um andamento que o Suno nunca recebe. Nenhum acervo atual cai nisso.
- **Controle vazio** so e valido em faixa que nasce sem BPM (volta ao original). Em faixa com BPM,
  apagar o campo e invalido como qualquer outro: o Style nao muda e aparece «use 20 a 300».

**Bateria de aceite numa copia do `app/index.html`, Chromium headless, temas claro e escuro: 44 PASSA,
0 FALHA.** Inclui: todo bloco e o export MD byte a byte iguais aos da 0.6.0 no valor original (album
e demo); ar-01 128 → 120 com um BPM so, no bloco, no botao copiar e no export MD («BPM: 120»);
−5/+5; quatro entradas invalidas sem tocar no Style; «voltar a 128» devolvendo o original byte a
byte; as variantes de ar-03 intactas (174 e 80); as **56 combinacoes** de chip de andamento com um
BPM so, o controle no numero do chip e um chip de andamento ligado; a camada Clima aceitando varios;
os custos exatos de ar-01 e ar-05 da 3a.2; os chips-atalho custando 0 em ar-01; o FIX-008 depois da
busca e de «marcar usei»; «Baixar .json» igual ao importado; reimportar zerando; uma faixa de prova
sem BPM (controle vazio, 100 entra no fim com +1 tag, «limpar»); `moduleCosts` em 8 ms; nenhum
`pageerror`; sem rolagem lateral a 375 px. O `validate.py` passa os tres acervos e reprova os tres
casos negativos (campo 75 com style 70; dois numeros no style; campo sem BPM no style), com e sem o
pacote `jsonschema`.
````

### E19 — FIX-008 e DEC-020 no fim — `meta/DECISIONS.md`

**Ancora, literal:**

````
(−) O style base escrito no limite continua sendo gerado assim; a regra que o evitaria mora no prompt-modelo (i-028).
````

**Texto novo, literal:**

````
(−) O style base escrito no limite continua sendo gerado assim; a regra que o evitaria mora no prompt-modelo (i-028).

---

## FIX-008 — O re-render religava os chips, mas o Style continuava com o clique

**Data:** 2026-10-28
**Sintoma:** Depois de clicar num chip de modulo, qualquer re-render — mudar um filtro, digitar na busca, «marcar usei» — mostrava os chips de volta ao estado do acervo, enquanto o bloco de Style seguia com o clique. O botao copiar entregava um texto que os chips nao explicavam. Medido na 0.6.0, em ar-01: um chip desligado e uma letra na busca deixavam o bloco com 298 caracteres e os 7 chips acesos.

**Causa raiz:** `renderCard` monta o bloco de Style ANTES do painel de modulos, lendo `App.activeModules[song.id]` (o estado do clique); depois, `renderModules` substituia esse conjunto por um novo, criado do acervo. Duas leituras do mesmo estado em momentos diferentes do mesmo render.

**Solucao:** `renderModules` reaproveita o conjunto que ja existe para a faixa; so cria um do acervo quando nao ha nenhum. `setCollection` zera `App.activeModules` (e o novo `App.bpm`), entao importar de novo volta ao acervo. Achado ao implementar o controle de BPM, que teria o mesmo defeito.

**Licao:** E o FIX-007 com outra roupa: estado que a interface muda depois de criada tem de ter uma fonte so, lida do mesmo jeito por tudo o que a mostra. Re-render e o teste que pega isso — faltava na bateria.

---

## DEC-020 — Fase 3b: o controle de BPM governa todo «NN bpm» do Style; o chip de andamento vira atalho

**Data:** 2026-10-28
**Contexto:** A i-005 pedia BPM manipulavel no cartao. A spec `meta/specs/261028-controle-de-bpm.md` mediu: as tres fontes de BPM (campo `bpm`, numero no `style`, modulo de andamento) concordam em 10 de 10 faixas; mas a camada Andamento do painel nunca muda o BPM — em 49 de 49 cliques poe um segundo numero no prompt, porque a dedup ve «128 bpm» e «70 bpm» como coisas diferentes, e desligar o modulo da faixa nao tira o numero do style base. Um prototipo que reescreve todo «NN bpm» para um valor so, antes da dedup, deu um BPM so em 56 de 56 combinacoes, sem mudar a contagem de tags.

**Decisao:** (1) Um controle na linha de metadados do cartao (campo numerico 20-300, −5/+5, «voltar a N») governa todo «NN bpm» do Style principal — base e fragmentos dos modulos —, reescrito no lugar, antes da dedup. Valor inicial: o numero do `style`; sem ele, o campo `bpm`; sem os dois, vazio (e, preenchido, o numero entra no fim). Variantes ficam de fora. O export MD leva o valor do controle no bloco e na linha de metadados. (2) O valor e so da sessao, como os modulos: nao vai para o «Baixar .json» nem para o navegador. (3) O chip de andamento vira atalho: ligar move o controle para o numero dele e desliga o outro chip de andamento; mudar o controle para outro numero desliga o chip; voltar ao numero dele nao o religa. (4) O `validate.py` reprova faixa com dois BPM diferentes no `style`, ou com campo `bpm` diferente do numero do `style` (ou sem numero no `style`).

**Alternativas consideradas:** guardar o valor no navegador ou no .json — descartadas: o primeiro faria o Style copiado depois de recarregar misturar BPM novo com modulos originais; o segundo faria o app editar o acervo, papel que o FIX-004 tirou dele. Chips de andamento intocados (custo 0 quase sempre: um botao que nao faz nada) ou escondidos (perde os atalhos). Slider: ~1 BPM por pixel no celular. Validador so avisando, ou sem checagem: o erro de autoria ficaria escondido pelo controle, que escolhe o numero do `style`.

**Consequencias:** (+) O prompt nunca leva dois andamentos — o defeito silencioso da camada Andamento some. (+) No valor original, tudo o que se copia e exporta e byte a byte o da 0.6.0. (+) Os 8 andamentos do album viram pontos de salto. (−) O controle nao sabe se a palavra combina com o numero: a 140, ar-04 ainda diz «downtempo» (i-029). (−) O fragmento de um modulo de andamento que traz palavras alem do numero («slow tempo 70 bpm») perde as palavras pela dedup quando o base ja tem um BPM — o que o chip entrega e o numero.
````

### E20 — i-005: nota de implementacao — `meta/IDEAS.md`

**Ancora, literal:**

````
BPM como valor manipulável na ferramenta (slider ou stepper), refletindo no style copiado. Cuidado registrado no HISTORY: Suno trata BPM como aproximação, não comando exato — a ferramenta ajuda a *escrever* o BPM, não garante que o Suno obedeça. Fase 3.
````

**Texto novo, literal:**

````
BPM como valor manipulável na ferramenta (slider ou stepper), refletindo no style copiado. Cuidado registrado no HISTORY: Suno trata BPM como aproximação, não comando exato — a ferramenta ajuda a *escrever* o BPM, não garante que o Suno obedeça. Fase 3.
**Implementada em 2026-10-28 (DEC-020)** — campo numérico no cartão, não slider (spec `meta/specs/261028-controle-de-bpm.md`, Decisão 3). Vira ✅ depois da conferência na tela.
````

### E21 — i-029 depois da i-028 — `meta/IDEAS.md`

**Ancora, literal:**

````
Pesar contra: o base mais curto pode ficar vago (abaixo de 4 tags o painel ja avisa).
````

**Texto novo, literal:**

````
Pesar contra: o base mais curto pode ficar vago (abaixo de 4 tags o painel ja avisa).

### i-029 💡 Avisar quando a palavra de andamento contradiz o BPM
`[nascido da spec do BPM, 2026-10-28]` Com o controle, ar-04 vai a 140 e continua dizendo «downtempo» e «slow build». A linha de qualidade poderia avisar, em ambar, quando uma palavra de andamento do Style («downtempo», «slow», «uptempo», «fast») briga com o numero. Pesar contra: exige uma tabela palavra → faixa de BPM, conhecimento de dominio que muda com o Suno — o mesmo motivo que tirou a tabela de generos vocais da DEC-019. Se entrar, a tabela mora num objeto unico com fonte e data, como o `QUALITY_LIMITS`.
````

### E22 — 3b: BPM aplicado — `meta/ROADMAP.md`

**Ancora, literal:**

````
- ⬜ Controle de BPM por slider/stepper (i-005).
````

**Texto novo, literal:**

````
- 🔨 Controle de BPM no cartão (i-005, DEC-020) — aplicado, aguarda a conferência na tela; campo numérico, não slider.
````

### E23 — §5: o BPM no v6 — `meta/HISTORY.md`

**Ancora, literal:**

````
a ferramenta ajuda a *escrever* o BPM, não garante obediência.
````

**Texto novo, literal:**

````
a ferramenta ajuda a *escrever* o BPM, não garante obediência.
- **BPM no v6 (conferido em 2026-10-28):** a nota oficial do v6 (2026-09-09) não fala de tempo, e o help center oficial só documenta BPM no **Studio** («Transport controls»: Tempo padrão 120, «Follow Track» ou «Manual Tempo»). Na criação, o BPM continua indo como **texto no Style**. Não confirmado: um guia secundário de 2026 diz que o slider **Variety** acima de 0 pode reescrever as tags do Style (testado no v5) — se valer para o BPM, Variety 0 é a condição para o número do controle chegar intacto. Fontes na spec `meta/specs/261028-controle-de-bpm.md`.
````

## Edicao 24 — STATUS inteiro — `meta/STATUS.md`

**Sem ancora.** Substitua o arquivo **inteiro** pelo bloco abaixo, em LF, terminando com uma quebra de
linha depois da ultima linha. A partida e garantida pela Edicao 0. Este bloco **nao** pertence a E23:
se o seu aplicador le os blocos por expressao regular, pare a E23 no primeiro fecho de quatro crases.

````
# STATUS.md — Cancioneiro

> **O agora.** O que funciona, o que está em progresso, o que está quebrado, backlog curto.
> Rolante: item resolvido sai daqui e vai para o CHANGELOG. Médio/longo prazo vive no ROADMAP.

**Versão atual:** 0.6.0 · **Fase:** 3b em curso — controle de BPM aplicado, aguarda a conferência na tela · Fase 2 com i-008 em aberto

---

## Última conversa (2026-10-28, controle de BPM)

- **Spec do BPM decidida pelo dono** (`meta/specs/261028-controle-de-bpm.md`): 1a só na sessão, 2a chip de andamento vira atalho, 3a campo numérico com −5/+5, 4a o validador reprova BPM divergente. Aplicada pela WO 0013 (DEC-020).
- **Achado no caminho, corrigido junto (FIX-008):** filtro, busca e «marcar usei» religavam os chips do acervo, mas o bloco de Style seguia com o clique — chip e texto copiado divergiam.
- **Este bloco substitui o anterior, de 2026-10-27, que fechava a 3a.2 e a 0.6.0.** O que ele dizia está no CHANGELOG (0.6.0), no DECISIONS (DEC-019) e em `logs/2026-10-27.md`.

## Funciona (pronto)

- **Ferramenta `app/index.html`:** importa/carrega JSON, cartões por álbum, copiar Style/Lyrics/Exclude por botão (o botão entrega o texto que está na tela — FIX-007), marca «usei», filtros por álbum/estado/uso, busca, módulos de estilo que recompõem o Style ao vivo, variantes e notas recolhíveis, «Baixar .json» limpo e «Importar .json» que saneia chaves internas e diz quantas removeu (FIX-004/006). A versão aparece no cabeçalho.
- **Painel de qualidade (0.5.0, DEC-018):** linha abaixo de Style, Lyrics e Exclude com caracteres contra o limite do campo, tags do Style e negações «no X». Vermelho só para truncamento.
- **Custo de cada módulo no chip (0.6.0, DEC-019):** com o painel de módulos aberto, cada chip mostra `−N`, `+N` ou `0` tags; a linha de qualidade diz quanto o style base usa sozinho quando o recomposto passa de 10.
- **Esquema JSON canônico** (`schema/`). Biblioteca de referência para autoria em `schema/style-modules.json` (27 módulos, sete camadas); cada acervo traz os seus (DEC-016).
- **Datasets:** `data/exemplo-cinzeiro.json` (1 faixa, com os 5 módulos que cita) e `data/demo.json` (2 álbuns, 3 faixas). O álbum de referências do dono mora fora do repo, em `../album-referencias (1).json` (7 faixas, 50 módulos).
- **Validação** (`scripts/validate.py`): sintaxe, esquema (com `jsonschema`), integridade referencial dos módulos, versão igual nos quatro lugares e um BPM só por faixa (DEC-020); código 1 se falhar; a última linha diz se o esquema foi de fato conferido.
- **Export MD** (faixa / álbum / acervo), com o Style recomposto e o rótulo fora do bloco.
- **Prompt-modelo** (`schema/PROMPT-PARA-CHATS.md`) para chats gerarem JSON no esquema.
- **Publicado no GitHub Pages** em `https://joaolucas-nds.github.io/cancioneiro/app/index.html` — o push em `main` publica.

## Em progresso

- **Controle de BPM no cartão (3b, i-005, DEC-020)** — aplicado pela WO 0013 e testado pelo chat numa cópia (44 de 44 critérios). Falta a conferência na tela do dono, com o roteiro que o chat entregou na conversa de 2026-10-28; depois, o fecho da 0.7.0 no CHANGELOG, ROADMAP, IDEAS e README.

## Quebrado / pendências que travam

- (nada quebrado)

## Pendências do dono

- **Instalar o validador de esquema nesta máquina.** Sem `jsonschema` e `referencing`, o `validate.py` só confere sintaxe e diz `ESQUEMA NAO CONFERIDO` na última linha. Uma vez, no CMD: `pip install jsonschema referencing --break-system-packages`. Depois, `python3 scripts/validate.py` deve terminar em `Tudo conforme ao esquema.` — o arquivo do álbum já foi validado fora daqui com 0 erros.

## Backlog curto (próximas ações concretas)

1. **Folga no prompt-modelo** (i-028) — pedir ao chat um style base com 6 a 8 tags. Em ar-01 e ar-04 o base nasce com 10 de 10.
2. **Testar o prompt-modelo ponta a ponta:** colar num chat, gerar uma faixa, importar.
3. **Converter 1 álbum real** (i-008) — depende de o dono trazer um `.md` de origem para a pasta-pai.

## Notas de estado

- **Repo local do dono:** `C:\Users\alexk\Tools\cancioneiro\cancioneiro` (Windows). O chat lê e grava na pasta vinculada; commit e push são do Code (DEC-010). A pasta-pai guarda relatórios, notas e o acervo do dono, fora do Git; o lido vai para `../notas-arquivadas/`.
- **Canal:** pasta vinculada é o padrão; a cópia achatada (FlatDrop) é reserva (DEC-017).
- **Limites do Suno:** o v6 saiu em 2026-09-09 e a nota oficial não documenta limite de campo; os números do painel vêm de fonte secundária, com fonte e data no `QUALITY_LIMITS` (DEC-018). Reconferir quando houver documentação oficial. O `meta/HISTORY.md` ainda descreve o v5.5 e precisa de uma atualização sobre o v6.
- **Estado de sessão** (módulos ligados e BPM escolhido) sobrevive a filtro, busca e «marcar usei»; volta ao acervo ao recarregar a página ou importar de novo (FIX-008, DEC-020).
- **Limite conhecido:** `tryAutoLoad` (carregamento automático pelo Pages) não saneia chaves internas — só a importação por arquivo faz isso. Inócuo enquanto nenhum acervo contaminado for para `data/`.
- **Pendência de contexto — ASU:** o dono perguntou se o «modo ASU» do KCM seria melhor que o modo Code para este projeto; ficou pendente até ele trazer a descrição do ASU `[relatado pelo dono, sem material de apoio]`.
- Os álbuns antigos de julho não estão na pasta. Para converter um (i-008), trazer o `.md` de origem para a pasta-pai.
- Design: na recomposição do Style a base manda — desligar um módulo não remove o que já está no style base; módulos só somam. O dedup compara sequências de palavras (FIX-003). Os módulos de gênero e de andamento costumam custar 0 tag por isso (DEC-019). O chip de andamento é atalho do controle de BPM, no máximo um ligado (DEC-020).
````

## Fora de escopo

- **CHANGELOG, README, o ✅ da i-005 e a 0.7.0** — so depois da conferencia na tela, na proxima WO.
- **i-029** (avisar palavra de andamento contraditoria) — capturada, nao implementada.
- `data/`, `schema/` — nada muda; os modulos de andamento seguem como estao.

## Armadilhas desta WO

- **Varias edicoes terminam com a propria ancora** (E05 termina com o cabecalho da recomposicao; E14
  com `def check_version():`). Aplicar duas vezes duplicaria o bloco: a idempotencia pelo texto novo
  INTEIRO e o que impede. O chat conferiu que as 23 ancoras sao unicas em qualquer ordem; siga a dada.
- **E05 e E14 trazem `\b`, `\d`, `\s` e `\u2212`** em strings JavaScript e Python. Copie literal: e o
  interpretador que os converte, nao o editor.
- **E11 remove as linhas que atualizavam o bloco no clique** e as troca por `refreshCardStyle(song, card)`.
  Nao reintroduza `chip.classList.toggle("on")` no clique: o `syncChips` (E12) e quem desenha os chips agora,
  porque o chip-atalho desliga o vizinho.
- **`recomposedStyle` ganha um terceiro parametro opcional.** Os chamadores antigos continuam certos;
  conferido pela regressao byte a byte do chat.
- **Fim de linha:** os oito arquivos sao LF. Se um hash de chegada divergir, rode `file <arquivo>`
  antes de concluir que uma edicao errou.

## Depois de aplicar — conferencia antes do commit

| # | Checagem | Comando | Esperado |
|---|---|---|---|
| 1 | **Os oito arquivos sao os testados** | `sha1sum app/index.html scripts/validate.py meta/DECISIONS.md meta/IDEAS.md meta/ROADMAP.md meta/HISTORY.md meta/STATUS.md meta/specs/261028-controle-de-bpm.md` | a coluna **chegada** do cabecalho, os oito. **Prova as 24 edicoes.** |
| 2 | As funcoes novas do app | `grep -cE 'function (bpmIn\|initialBpm\|currentBpm\|rewriteBpm\|tempoChipBpm\|setBpmFromControl\|refreshCardStyle\|bpmControl)\b' app/index.html` | `8` |
| 3 | Um caminho so para atualizar o cartao | `grep -c 'refreshCardStyle(song, card);' app/index.html`, `grep -c 'recompUI.textContent = composed' app/index.html` | `2`, `0` |
| 4 | A checagem nova do validador | `grep -c '^def check_bpm' scripts/validate.py`, `grep -c 'errors += check_bpm(data, rel)' scripts/validate.py` | `1`, `2` |
| 5 | Os registros | `grep -c '^## FIX-008' meta/DECISIONS.md`, `grep -c '^## DEC-020' meta/DECISIONS.md`, `grep -c '^### i-029' meta/IDEAS.md`, `grep -c 'Status:\*\* Decidida' meta/specs/261028-controle-de-bpm.md` | `1`, `1`, `1`, `1` |
| 6 | Validacao passa | `python3 scripts/validate.py; echo "exit=$?"` | `exit=0` |
| 7 | O BPM do album do dono tambem passa | `python3 scripts/validate.py "../album-referencias (1).json"; echo "exit=$?"` | `exit=0` |
| 8 | Nada de dados | `GIT_OPTIONAL_LOCKS=0 git status --short data schema` | saida **vazia** |
| 9 | Nenhum relatorio `.txt` no repo | `GIT_OPTIONAL_LOCKS=0 git status --short \| grep -c '\.txt'` | `0` |

**Os tres campos de cada passo:** as nove sao rodadas por **quem aplica (o Code)**, na raiz do repo
(`C:\Users\alexk\Tools\cancioneiro\cancioneiro`), em Git Bash, com `LC_ALL=C.UTF-8`. **Chega no ramo?**
A checagem 1 cobre os oito arquivos inteiros, e o app de chegada foi executado pelo chat. **Esta e qual
pergunta?** As nove respondem «esta la?». O que so a tela do dono responde vai no roteiro que o chat
entrega **no corpo da resposta**, nao aqui.

## Relatorio de aplicacao

Grave em `../261028-HHMM-code-cancioneiro-apply-wo0013.txt`, com o `HHMM` de `date +%y%m%d-%H%M` rodado
na hora. Diga o resultado da checagem 1 em primeiro lugar. A conferencia na tela **nao e sua**.

**Proximo comando** (ultima linha do relatorio, cru e sozinho):

```
/wrap
```

## Commit

```
git add app/index.html scripts/validate.py meta/DECISIONS.md meta/IDEAS.md meta/ROADMAP.md meta/HISTORY.md meta/STATUS.md meta/specs/261028-controle-de-bpm.md meta/workorders
```

```
git commit -m "feat: controle de BPM no cartao e chip de andamento como atalho" -m "DEC-020: um campo numerico na linha de metadados governa todo NN bpm do Style principal, reescrito antes da dedup; o chip de andamento move o controle e fica no maximo um ligado; variantes e o Baixar .json nao mudam. O validate.py reprova faixa com dois BPM ou com campo bpm diferente do style. FIX-008: filtro, busca e marcar usei religavam os chips, mas o Style seguia com o clique; o estado de sessao agora sobrevive ao re-render. Captura a i-029 e anota no HISTORY o BPM no v6."
```

```
git push
```
