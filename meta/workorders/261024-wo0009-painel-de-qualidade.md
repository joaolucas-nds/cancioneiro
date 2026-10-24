# WO 0009 — Painel de qualidade do prompt (Fase 3a) e o botao copiar que copiava o texto antigo

## Cabecalho

> **Tipo:** WO de CODIGO (`app/index.html`) e de registro.
> **Config sugerida:** Sonnet · `/effort medium`. Oito edicoes literais num arquivo so, todas testadas pelo chat antes de virar WO; o julgamento ja foi feito.
> **Pre-requisito:** commit `67bc9a2`, branch `main`, sincronizada com `origin/main`. **A arvore NAO esta limpa:** `meta/specs/` e nova (a spec, gravada pelo chat). Nada mais deve aparecer no `git status`.
> **Base:** `meta/specs/261024-painel-de-qualidade.md`, Status **Decidida** em 2026-10-24 (Decisoes: 1 so avisa · 2 nao dispara no instrumental · 3 adia o i-020).
> **Depende de:** WO 0008, ja aplicada.
>
> **Arquivos que o chat gravou no disco e esta WO versiona** (sha1sum medido pelo chat ao gravar):
> - `meta/specs/261024-painel-de-qualidade.md` — `175718bf8e853d27d3209700642013cc04a7a4c4`
>
> **Arquivo que esta WO EDITA, com o hash de partida e o de chegada** — os dois medidos pelo chat:
> - `app/index.html` — **partida** `f3f1101f6434549265238137e4c836c5eef3d3ae` (33.729 bytes) → **chegada** `2d6362170f83c94b175e54993e42a38d8db76556` (39.181 bytes)
> - A chegada e o arquivo exato que passou nos 18 criterios de aceite. Se as oito edicoes forem aplicadas literalmente sobre a partida, o resultado TEM de ter esse hash. Ver checagem 1.
>
> **Ancora semantica:** se um trecho-ancora nao bater EXATAMENTE, PARE e reporte.
> **Idempotencia:** antes de cada edicao, procure o texto NOVO INTEIRO no arquivo; se ja estiver la, PULE e diga no relatorio.
>
> **Ancoras lidas em:** cada ancora de `app/index.html` foi conferida pelo chat no turno de 2026-10-24 como ocorrendo **exatamente 1 vez** no arquivo de partida (`f3f1101f...`), por `str.count`. Os trechos literais estao em cada edicao abaixo. Para os `meta/`:
> - `meta/DECISIONS.md`, ultima linha do arquivo (fim de DEC-017), que comeca com `**Consequencias:** (+) O CEREBRO deixa de descrever como normal um canal`
> - `meta/STATUS.md` linha 10: `## Última conversa (2026-10-24, WO 0008 — merge do kit v1.131.0)`
> - `meta/IDEAS.md` linha 68, o corpo do i-020: `O Suno pesa mais as tags iniciais; gênero primeiro, clima em seguida. A ferramenta pode sinalizar quando o primeiro fragmento não parece um gênero (comparando com a camada \`genre\` da biblioteca de módulos). Sugestão leve, não imposição.`

---

## 1. Por que

A ferramenta organiza prompts mas nao julga nenhum, e o Suno **trunca em silencio**. A spec mediu onde
o risco mora: nao no texto que o chat escreve (o maior style base tem 174 caracteres), mas nos
**modulos**, que so somam — no album, 7 de 7 faixas ja passam de 10 tags com os modulos da propria
faixa, e todas truncariam com a biblioteca inteira ligada (1.237–1.296 caracteres).

**E a implementacao achou um bug pre-existente que faria o painel mentir — FIX-007.** O botao «copiar»
capturava o texto no momento em que o cartao era criado; o clique num chip so atualizava o bloco
visual. Medido em ar-01: bloco 298 → 322 ao ligar um chip, botao copiando os **298 antigos**. A troca
de estilo por modulo nunca chegou ao Suno pelo botao. A Edicao 1 conserta, e vem primeiro.

## Edicao 0 — Conferencia de hash e de arvore

```
sha1sum app/index.html meta/specs/261024-painel-de-qualidade.md
GIT_OPTIONAL_LOCKS=0 git status --short
```

`app/index.html` tem de ser `f3f1101f...` (partida) e a spec `175718bf...`. O `git status` mostra
**exatamente** `?? meta/specs/` (mais esta WO). Qualquer outra coisa: **PARE e reporte** — se o app nao
for a partida, alguem mexeu nele depois do teste, e as edicoes podem nao produzir o arquivo testado.

## Edicao 1 — FIX-007 — `app/index.html` · o botao copiar le o bloco na hora do clique

**Vem primeiro, e e pre-requisito do resto.** Sem ela o painel mostra um numero e o botao copia outro.

**Ancora, literal:**

```js
  btn.addEventListener("click", () => copyText(content, btn));
  head.appendChild(lab); head.appendChild(btn);
```

**Texto novo, literal:**

```js
  // Le o bloco NA HORA do clique, nao o texto capturado ao criar o cartao: o Style
  // muda quando um chip de modulo e ligado, e copiar o texto antigo fazia o que se
  // via divergir do que se colava no Suno (FIX-007).
  btn.addEventListener("click", () => copyText(pre.textContent, btn));
  head.appendChild(lab); head.appendChild(btn);
```

## Edicao 2a — `app/index.html` · token ambar, tema claro

**Ancora, literal:**

```css
    --moss:       #4b6b4a;   /* estado "usei/aprovada" */
```

**Texto novo, literal:**

```css
    --moss:       #4b6b4a;   /* estado "usei/aprovada" */
    --amber:      #8a6100;   /* painel de qualidade: "vai funcionar, mas pior" */
```

## Edicao 2b — `app/index.html` · token ambar, tema escuro

A ancora e uma linha so, dentro de `@media (prefers-color-scheme: dark)`.

**Ancora, literal:**

```css
      --line: #38332b; --ember: #e0703f; --ember-soft: #4a2a1c; --moss: #8fb271;
```

**Texto novo, literal:**

```css
      --line: #38332b; --ember: #e0703f; --ember-soft: #4a2a1c; --moss: #8fb271; --amber: #d9a441;
```

## Edicao 2c — `app/index.html` · as classes do painel

**Ancora, literal:**

```css
  .exclude { font-size: 12px; color: var(--ink-soft); }
```

**Texto novo, literal:**

```css
  .exclude { font-size: 12px; color: var(--ink-soft); }

  /* Painel de qualidade: le o que vai para o Suno, FORA do bloco copiavel.
     Vermelho (ember) so para perda — o Suno vai cortar texto. Ambar para "pior".
     Nada aqui entra na copia nem no export (regra de dominio inviolavel). */
  .quality { display: flex; flex-wrap: wrap; gap: 4px 12px; margin-top: 4px; font-size: 11px; color: var(--ink-soft); }
  .quality .q.ok      { color: var(--moss); }
  .quality .q.neutral { color: var(--ink-soft); }
  .quality .q.warn    { color: var(--amber); font-weight: 600; }
  .quality .q.over    { color: var(--ember); font-weight: 700; }
```

## Edicao 3 — `app/index.html` · limites e funcoes puras, antes de `fieldBlock`

**A ancora e a linha de abertura de `fieldBlock` e ela REAPARECE no fim do texto novo** — e a forma «trocar» que o modelo de WO avisa. Idempotencia: procure `const QUALITY_LIMITS`; se ja existir, PULE.

**Ancora, literal:**

```js
function fieldBlock(label, content, extraClass) {
```

**Texto novo, literal:**

```js
/* ===================================================================
   Painel de qualidade (Fase 3a — spec meta/specs/261024-painel-de-qualidade.md)
   Os LIMITES ficam num lugar so, com fonte e data: o Suno ja mudou esses
   numeros uma vez (V4 -> V4.5) e lancou o v6 em 2026-09-09 sem documenta-los.
   Quando mudarem de novo, muda-se aqui e se sabe de onde veio o anterior.
   =================================================================== */
const QUALITY_LIMITS = {
  // Fonte: hookgenius.app/learn/suno-character-limits (atualizada 2026-09-08/09).
  // A nota oficial do v6 (suno.com/release-notes/introducing-v6) NAO traz limites.
  style:   { warn: 850,  max: 1000 },  // v4.5..v6
  lyrics:  { warn: 3000, max: 5000 },  // 5.000 = consenso; ~3.000 = onde o Suno "corre"
  exclude: { warn: 850,  max: 1000 },  // medido via maxlength, em v5.5
  // Tags: HISTORY §10 + mesma fonte (testado em v5/v5.5). Acima de ~10 o ganho
  // achata, nao quebra — por isso e ambar, nunca vermelho.
  tags:    { vague: 4, sweet: 8, many: 10 },
};

/** Nivel de um comprimento contra um limite: ok | warn | over. */
function lengthLevel(n, lim) {
  if (n > lim.max) return "over";
  if (n > lim.warn) return "warn";
  return "ok";
}

/** Tags como o Suno as recebe: fragmentos nao vazios separados por virgula. */
function countTags(style) {
  return style.split(",").filter(t => t.trim()).length;
}

/** "no X" por FRONTEIRA de palavra. Substring casaria pia-no e sopra-no (FIX-003
    de novo); "no-wave" e genero, nao negacao, e nao casa porque pede espaco. */
const NEGATION_RE = /(?<![a-z])no\s+[a-z][a-z-]*(?:\s+[a-z][a-z-]*)?/gi;
function findNegations(style, lyrics) {
  // Decisao 2 da spec: "no vocals" em faixa INSTRUMENTAL e reforco deliberado
  // (modulo vocal-none; HISTORY §11), nao erro. Instrumental = Lyrics sem
  // nenhuma linha de letra: so tags entre colchetes. Cobre [Instrumental] e a
  // faixa linear com [Intro]/[Build]/[Climax]/[Outro], que o dominio tambem aceita.
  const linhas = (lyrics || "").split("\n").map(l => l.trim()).filter(Boolean);
  const instrumental = linhas.length > 0 && linhas.every(l => /^\[[^\]]*\]$/.test(l));
  const out = [];
  style.split(",").forEach(frag => {
    (frag.match(NEGATION_RE) || []).forEach(m => {
      const t = m.trim().toLowerCase();
      if (instrumental && /^no\s+vocals?$/.test(t)) return;
      if (!out.includes(t)) out.push(t);
    });
  });
  return out;
}

function qSpan(text, level) {
  const s = document.createElement("span");
  s.className = "q " + level; s.textContent = text;
  return s;
}
function fmt(n) { return n.toLocaleString("pt-BR"); }

/** Linha de qualidade de um campo de texto (Lyrics, Exclude). */
function lengthQuality(text, lim, overMsg, warnMsg) {
  const el = document.createElement("div"); el.className = "quality";
  const n = text.length, lv = lengthLevel(n, lim);
  el.appendChild(qSpan(fmt(n) + " / " + fmt(lim.max) + " caracteres", lv));
  if (lv === "over") el.appendChild(qSpan(overMsg, "over"));
  else if (lv === "warn") el.appendChild(qSpan(warnMsg, "warn"));
  return el;
}

/** Linha de qualidade do Style recomposto: caracteres + tags + negacoes. */
function styleQuality(style, lyrics) {
  const el = lengthQuality(style, QUALITY_LIMITS.style,
    "o Suno corta o que passar de 1.000 — sem aviso", "perto do limite de 1.000");
  el.setAttribute("data-role", "style-quality");
  const t = countTags(style), L = QUALITY_LIMITS.tags;
  const tl = t < L.vague ? "warn" : t <= L.sweet ? "ok" : t <= L.many ? "neutral" : "warn";
  el.appendChild(qSpan(t + " tags", tl));
  if (t < L.vague) el.appendChild(qSpan("vago demais", "warn"));
  if (t > L.many)  el.appendChild(qSpan("acima de ~10 o efeito das últimas tende a diluir", "warn"));
  findNegations(style, lyrics).forEach(n =>
    el.appendChild(qSpan("«" + n + "»: mais confiável no campo Exclude", "warn")));
  return el;
}

function fieldBlock(label, content, extraClass) {
```

## Edicao 4a — `app/index.html` · anexar as linhas de Style e Lyrics no cartao

**Ancora, literal:**

```js
  styleField.querySelector(".block").setAttribute("data-role", "style-block");
  card.appendChild(styleField);
  card.appendChild(fieldBlock("Lyrics", song.lyrics, "lyrics"));
```

**Texto novo, literal:**

```js
  styleField.querySelector(".block").setAttribute("data-role", "style-block");
  styleField.appendChild(styleQuality(recomposedStyle(song), song.lyrics));
  card.appendChild(styleField);
  const lyricsField = fieldBlock("Lyrics", song.lyrics, "lyrics");
  lyricsField.appendChild(lengthQuality(song.lyrics, QUALITY_LIMITS.lyrics,
    "o Suno corta o que passar de 5.000 — sem aviso",
    "acima de ~3.000 o Suno tende a correr e pular seções"));
  card.appendChild(lyricsField);
```

## Edicao 4b — `app/index.html` · anexar a linha de Exclude

**Ancora, literal:**

```js
    ex.appendChild(document.createElement("br")); ex.appendChild(btn);
    card.appendChild(ex);
```

**Texto novo, literal:**

```js
    ex.appendChild(document.createElement("br")); ex.appendChild(btn);
    ex.appendChild(lengthQuality(song.excludeStyles.join(", "), QUALITY_LIMITS.exclude,
      "o Suno corta o que passar de 1.000 — sem aviso", "perto do limite de 1.000"));
    card.appendChild(ex);
```

## Edicao 5 — `app/index.html` · atualizar o painel quando um chip muda

**Ancora, literal:**

```js
        const styleBlock = card.querySelector('[data-role="style-block"]');
        if (styleBlock) styleBlock.textContent = composed;
```

**Texto novo, literal:**

```js
        const styleBlock = card.querySelector('[data-role="style-block"]');
        if (styleBlock) styleBlock.textContent = composed;
        const oldQ = card.querySelector('[data-role="style-quality"]');
        if (oldQ) oldQ.replaceWith(styleQuality(composed, song.lyrics));
```

## Edicao 6 — `meta/DECISIONS.md` · FIX-007 e DEC-018

**Ancora:** a ULTIMA linha do arquivo (fim de DEC-017), citada no cabecalho. Insira DEPOIS dela,
precedido de uma linha em branco e de `---`.

```
---

## FIX-007 — O botao copiar entregava o Style de antes do clique no modulo

**Data:** 2026-10-24
**Sintoma:** Ligar ou desligar um chip de modulo mudava o Style mostrado no cartao, mas o botao «copiar» do Style continuava entregando o texto anterior. Medido em headless em ar-01: bloco de 298 para 322 caracteres ao ligar um chip, e o botao entregando os 298 antigos. O que se via nao era o que se colava no Suno.

**Causa raiz:** `fieldBlock` registrava `copyText(content, btn)`, com `content` capturado por closure no momento em que o cartao era montado. O clique no chip atualizava `pre.textContent` do bloco, mas nunca o `content` da closure. O export MD nao era afetado porque recompoe na hora — e por isso a divergencia nunca apareceu em nenhuma conferencia de arquivo.

**Solucao:** O botao le `pre.textContent` no momento do clique. Para todo campo que nao muda depois de criado (Lyrics, variantes), o texto e identico ao de antes — conferido byte a byte nos 27 botoes do album e nos 11 do demo.

**Licao:** Estado que a interface atualiza depois de criada nao pode ser lido de uma copia feita na criacao. O defeito era invisivel a qualquer instrumento que le arquivo, e so apareceu porque o painel de qualidade precisava que o numero mostrado e o texto copiado fossem o mesmo — o painel foi o primeiro codigo deste projeto a exigir isso, e por isso o primeiro a revela-lo. A funcao central dos modulos (i-004) estava quebrada no caminho mais usado desde o v0.

---

## DEC-018 — Painel de qualidade: mede o recomposto, so avisa, e o vermelho e reservado a perda

**Data:** 2026-10-24
**Contexto:** Fase 3a (i-017 a i-019). A spec `meta/specs/261024-painel-de-qualidade.md` mediu o acervo real contra os limites do Suno — reconferidos na web, porque o Suno lancou o v6 em 2026-09-09 e a nota oficial nao documenta limite nenhum; os numeros vem de fonte secundaria, com a forca de cada um declarada na spec.

**Decisao:** O painel mede o **Style recomposto** (o mesmo texto que o botao copia), atualiza a cada clique em chip, e mede tambem Lyrics e Exclude Styles. Os limites vivem num unico objeto `QUALITY_LIMITS`, com fonte e data em comentario. Tres niveis: verde, ambar («vai funcionar, mas pior») e vermelho **so para truncamento**, o unico caso que perde informacao — passar de 10 tags e ambar, nunca vermelho, porque dilui sem perder, e um vermelho em 7 de 7 faixas viraria ruido que leva junto o vermelho que importa. «no X» detectado por **fronteira de palavra** (substring casaria pia-no e sopra-no) e **so avisa**: a ferramenta continua so-leitura, como o DEC-004 manda. `no vocals` nao dispara em faixa **instrumental**, definida como Lyrics sem nenhuma linha de letra — o que cobre `[Instrumental]` e a faixa linear com tags de arco. O painel nunca bloqueia a copia.

**Alternativas consideradas:** (a) migrar o «no X» para o Exclude num clique — descartada pelo dono: seria a primeira vez que a ferramenta escreve no acervo, e pede analise propria; (b) definir instrumental como «Lyrics contem `[Instrumental]`» — descartada na implementacao: era a redacao literal da opcao aprovada, mas mais estreita que a intencao («nao dispara no instrumental»), e faria cinzeiro-01, que e instrumental, avisar `no vocals`; (c) alerta modal na hora de copiar — descartada: interrompe o gesto e se aprende a fechar sem ler; (d) i-020, aviso de ordem — adiado pelo dono: dispara em 0 de 10 faixas reais, com a evidencia mais fraca das quatro.

**Consequencias:** (+) O truncamento silencioso passa a ser visivel no unico ponto em que ainda se pode evitar. (+) A funcao central dos modulos volta a funcionar no botao (FIX-007). (+) Mudar um limite e mudar uma linha, sabendo de onde veio a anterior. (−) Os limites dependem de uma fonte que vende produto concorrente; reconferir quando a nota oficial do Suno os documentar. (−) O aviso de tags vai acender ambar em quase todas as faixas do album — e informacao verdadeira, mas e a que mais rapido vira paisagem; se isso acontecer, o sinal e o dono deixar de ler a linha, e o remedio e a sugestao de corte (3a.2), nao baixar o aviso.
```

## Edicao 7 — `meta/IDEAS.md` · o i-020 adiado, com o gatilho

**Ancora:** o corpo do i-020, citado no cabecalho (linha 68). Insira, **logo depois dessa linha**, uma
linha em branco e:

```
**Adiado em 2026-10-24 (Decisao 3 da spec do painel de qualidade).** Medido: dispara em **0 de 10** faixas reais (demo + album-referencias) — todas comecam com genero. Evidencia de dominio a mais fraca das quatro da Fase 3a (o Suno «parece» pesar mais as primeiras tags; um teste so), e a deteccao comparando com a camada `genre` e fragil: `dark ambient cinematic intro` so casou porque contem `dark ambient`. **Gatilho para reabrir:** a primeira faixa real cujo primeiro fragmento nao seja genero.
```

## Edicao 8 — `meta/STATUS.md`

A cargo do `/wrap`, em append. **Ancora:** a linha 10,
`## Última conversa (2026-10-24, WO 0008 — merge do kit v1.131.0)` — esse bloco **tem de continuar no
arquivo**, e os quatro anteriores tambem. `grep -c "^## Última conversa"` deve ir de **5 para 6**.

No bloco novo: o painel entregue (i-017, i-018, i-019); o FIX-007; o i-020 adiado; e que a conferencia
na tela e do dono e **ainda nao foi feita** no momento do commit. Nao marque a Fase 3a como concluida no
ROADMAP: isso fica para depois da conferencia na tela.

## Fora de escopo

- **ROADMAP.** Marcar i-017/018/019 como entregues so depois da conferencia na tela do dono.
- **Migrar «no X» para o Exclude** (Decisao 1). A ferramenta continua so-leitura.
- **Sugestao do que cortar** quando ha tags demais — e a 3a.2, depois desta.
- **i-020** — adiado, com gatilho no IDEAS.
- **Atualizar `meta/HISTORY.md` sobre o v6.** Registro, mas e doc grande e vivo: vai por WO propria.
- **`tryAutoLoad`** e o saneamento que ele nao faz — risco registrado no STATUS desde a WO 0007.

## Armadilhas desta WO

- **A Edicao 1 vem primeiro, e e a unica que muda o comportamento de algo que ja existia.** O resto so
  acrescenta. Se a Edicao 1 falhar, **PARE** — sem ela o painel mostra um numero e o botao copia outro.
- **A ancora da Edicao 3 reaparece no fim do texto novo** (`function fieldBlock(...) {`). Aplicando com
  substituicao de texto, e correto; aplicando duas vezes, duplica tudo. Idempotencia: `const QUALITY_LIMITS`.
- **As regex da Edicao 3 tem barra invertida** (`\s`, `\[`, `\n`). Elas estao literais no bloco: copie
  sem reescapar. Um `\\s` a mais quebra a deteccao em silencio — e e a checagem 1 (o hash) que pega.
- **O texto do painel nunca entra no `<pre>`.** As linhas `.quality` sao filhas do `.field`, irmas do
  bloco. Se o `git diff` mostrar qualquer coisa sendo anexada ao `pre`, esta errado — e o FIX-007
  passaria a copiar o texto do painel junto, violando a regra de dominio.
- **`python3 scripts/validate.py` nao se aplica** (nenhum dado muda), mas rode para confirmar que nada
  regrediu.
- **Fim de linha:** o arquivo de partida e LF. Se o hash de chegada divergir, rode
  `git diff --stat app/index.html` e `file app/index.html` antes de concluir que uma edicao errou — CRLF
  muda o hash sem mudar o codigo.

## Depois de aplicar — conferencia antes do commit

| # | Checagem | Comando | Esperado |
|---|---|---|---|
| 1 | **O resultado e o arquivo testado** | `sha1sum app/index.html` e `wc -c < app/index.html` | `2d6362170f83c94b175e54993e42a38d8db76556` e `39181`. **Esta checagem sozinha prova as oito edicoes.** Se divergir e o fim de linha for LF, uma edicao saiu diferente do literal — `diff` contra o texto da WO. |
| 2 | FIX-007: o botao le o bloco | `grep -cF "copyText(pre.textContent, btn)" app/index.html` e `grep -cF "copyText(content, btn)" app/index.html` | `1` e `0` |
| 3 | Os limites num lugar so | `grep -cF "const QUALITY_LIMITS" app/index.html` | `1` |
| 4 | As funcoes do painel | `grep -cE "function (styleQuality\|lengthQuality\|findNegations\|countTags\|lengthLevel)\b" app/index.html` | `5` |
| 5 | Os tres campos ligados | `grep -cF "QUALITY_LIMITS.lyrics" app/index.html` e `grep -cF "QUALITY_LIMITS.exclude" app/index.html` | `1` e `1` |
| 6 | Atualizacao ao vivo | `grep -cF "replaceWith(styleQuality" app/index.html` | `1` |
| 7 | O token novo, nos dois temas | `grep -cF -- "--amber" app/index.html` | `3` (claro, escuro, e o `var(--amber)` da classe) |
| 8 | Nada de produto alem do app | `GIT_OPTIONAL_LOCKS=0 git status --short data schema scripts` | saida **vazia** |
| 9 | Validacao nao regrediu | `python3 scripts/validate.py; echo "exit=$?"` | `exit=0` |
| 10 | Os registros | `grep -c "^## FIX-007" meta/DECISIONS.md`, `grep -c "^## DEC-018" meta/DECISIONS.md`, `grep -c "^## FIX-00[1-6]" meta/DECISIONS.md` | `1`, `1`, `6` |
| 11 | O i-020 adiado com gatilho | `grep -c "Adiado em 2026-10-24" meta/IDEAS.md` e `grep -c "^### i-020" meta/IDEAS.md` | `1` e `1` |
| 12 | A spec versionada e Decidida | `GIT_OPTIONAL_LOCKS=0 git ls-files meta/specs \| wc -l` (depois do `add`) e `grep -c "^> \*\*Status:\*\* Decidida" meta/specs/261024-painel-de-qualidade.md` | `1` e `1` |
| 13 | Os blocos antigos do STATUS | `grep -c "^## Última conversa" meta/STATUS.md` | `6` |
| 14 | Nenhum relatorio `.txt` no repo | `GIT_OPTIONAL_LOCKS=0 git status --short \| grep -c '\.txt'` | `0` |

**Os tres campos de cada passo:** as catorze sao rodadas por **quem aplica (o Code)**, na raiz do repo
(`C:\Users\alexk\Tools\cancioneiro\cancioneiro`), em Git Bash. **Chega no ramo?** A checagem 1 cobre as
oito edicoes de uma vez, porque o arquivo de chegada foi executado pelo chat em Chromium headless e
passou nos 18 criterios da spec — incluindo o vermelho visto de verdade (1.271 em ar-01 com todos os
modulos) e o botao copiar byte a byte em 38 botoes. **Esta e qual pergunta?** As catorze respondem
«esta la?». «Presta?» foi respondida pelo chat sobre o arquivo de chegada, e a parte que so a tela do
dono responde vai no roteiro que o chat entrega **no corpo da resposta**, nao aqui.

## Relatorio de aplicacao

Grave em `../261024-HHMM-code-cancioneiro-apply-wo0009.txt`, com o `HHMM` de `date +%y%m%d-%H%M`
rodado na hora. Diga o resultado da checagem 1 em primeiro lugar. A conferencia na tela **nao e sua** —
registre apenas que ela e do dono e foi entregue no chat.

**Proximo comando** (ultima linha do relatorio, cru e sozinho):

```
/wrap
```

## Commit

```
git add app/index.html meta/specs meta/DECISIONS.md meta/IDEAS.md meta/STATUS.md meta/workorders logs
```

```
git commit -m "feat: painel de qualidade do prompt e o copiar que entregava o texto antigo" -m "FIX-007: o botao copiar capturava o texto ao criar o cartao e nunca via o clique nos chips de modulo; passa a ler o bloco na hora do clique. DEC-018: painel de qualidade mede o Style recomposto, Lyrics e Exclude contra limites num objeto unico com fonte e data, conta tags, e detecta negacao por fronteira de palavra so avisando; vermelho reservado ao truncamento. i-020 adiado com gatilho."
```

```
git push
```
