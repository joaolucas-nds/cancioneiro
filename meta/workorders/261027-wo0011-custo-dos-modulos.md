# WO 0011 — Fase 3a.2: o custo de cada modulo no chip

## Cabecalho

> **Tipo:** WO de CODIGO (`app/index.html`) e de registro.
> **Config sugerida:** Sonnet · `/effort medium`. Dezessete edicoes literais, todas aplicadas e testadas pelo chat numa copia; cada arquivo tem hash de chegada.
> **Pre-requisito:** commit `a9eaf95`, branch `main`, sincronizada com `origin/main`. **A arvore NAO esta limpa:** `meta/specs/261027-custo-dos-modulos.md` e nova (a spec, gravada pelo chat). Nada mais deve aparecer no `git status`.
> **Base:** `meta/specs/261027-custo-dos-modulos.md`, Status **Decidida** em 2026-10-27 (Decisao 1: **(b)**, custo no chip).
> **Depende de:** WO 0010, ja aplicada.
>
> **Arquivo que o chat gravou no disco e esta WO versiona:** `meta/specs/261027-custo-dos-modulos.md` — `3a06c1c3fdac13ac94101ce7bd3dba9ad9f6dc0c`
>
> **Arquivos que esta WO edita — partida e chegada, os dois medidos pelo chat** (chegada = resultado de aplicar literalmente as edicoes abaixo, em LF):
>
> | arquivo | partida (sha1) | chegada (sha1) |
> |---|---|---|
> | `app/index.html` | `2d6362170f83c94b175e54993e42a38d8db76556` | `69112439b4c70aa1a1f0ffc2ba80251193ef2f01` |
> | `meta/DECISIONS.md` | `0cb126a33801e34d81dc983989f848ce30b03de9` | `33be6019f84d077e6b08169eb5161cbaa4b85b52` |
> | `meta/IDEAS.md` | `3bd707b085b1adb908a59c694af7dfb556655bf1` | `a8546e9bd7dd125f902fe82601406e80f2cec574` |
> | `meta/HISTORY.md` | `e75527e9ed3d678581246993fa204e6118847c20` | `9f93e07d94baa5448d98853ed5b67f697580621f` |
> | `meta/STATUS.md` | `820ead36771b6aa321a3231be41d7726c3b4081d` | `25cdf016156f291eff03c2cecf333c150784ab9f` |
>
> **Ancora semantica:** se um trecho-ancora nao bater EXATAMENTE, PARE e reporte.
> **Idempotencia:** antes de cada edicao, procure o texto NOVO INTEIRO; se ja estiver la, PULE e diga no relatorio.
>
> **Ancoras lidas em:** cada ancora foi lida pelo chat direto do disco no turno de 2026-10-27 e conferida como ocorrendo **exatamente 1 vez** no arquivo de partida (`str.count`). O texto literal esta em cada edicao.

---

## 1. Por que

A i-026 pedia uma lista de corte. A medicao mudou o desenho (DEC-019): o excesso de tags vem 100% dos
modulos, os modulos de genero e andamento quase sempre custam 0, e a lista automatica erra em 2 de 7
faixas (manda cortar a voz de rap em rap-pop). A 3a.2 mostra o **custo de cada modulo no chip** e a
**folga do base** na linha de qualidade; o corte e do dono.

O `app/index.html` de chegada (`69112439…`) foi executado pelo chat em Chromium headless, nos dois
temas: **21 de 21** criterios da spec passaram, incluindo os custos exatos de ar-05 e ar-01, o vizinho
de ar-04 indo de +1 a +2 na tela, e todo botao copiar e o export MD identicos ao de antes, byte a byte.

**Fora do codigo, esta WO tambem:** registra a DEC-019; corrige a premissa errada da i-026; captura a
i-028 (o prompt-modelo pedir folga); poe no HISTORY §10 a nuance dos generos centrados na voz; e tira do
STATUS a pendencia de colar as Instrucoes no painel, **que o dono ja fez** — o chat conferiu lendo o
painel.

**O STATUS vai literal, no apply** — nada «a cargo do `/wrap`».

## Edicao 0 — Conferencia de hash e de arvore

```
sha1sum app/index.html meta/DECISIONS.md meta/IDEAS.md meta/HISTORY.md meta/STATUS.md meta/specs/261027-custo-dos-modulos.md
GIT_OPTIONAL_LOCKS=0 git status --short
```

Os cinco primeiros batem com a coluna **partida**, a spec com `3a06c1c3…`, e o `git status` mostra
**so** `?? meta/specs/261027-custo-dos-modulos.md` e esta WO. Qualquer outra coisa: **PARE e reporte**.

## Edicoes 01 a 17

Na ordem. Varias sao «trocar mantendo e acrescentando» — o texto novo **comeca com a ancora** —, por isso
a idempotencia e pelo texto novo INTEIRO. A E15 **remove** uma linha: o texto novo
e vazio. Copie o que esta ENTRE as linhas de quatro crases, sem elas.

### E01 — recomposedStyle aceita um conjunto de modulos hipotetico — `app/index.html`

**Ancora, literal:**

````
function recomposedStyle(song) {
  const active = App.activeModules[song.id] || new Set(song.styleModules || []);
````

**Texto novo, literal:**

````
function recomposedStyle(song, activeOverride) {
  // activeOverride: conjunto hipotetico de modulos ligados, para medir o custo de
  // um chip sem tocar no estado da tela (3a.2). Sem ele, vale o estado atual.
  const active = activeOverride || App.activeModules[song.id] || new Set(song.styleModules || []);
````

### E02 — o custo dentro do chip, em CSS — `app/index.html`

**Ancora, literal:**

````
  .chip.on { background: var(--ember); color: #fff; border-color: var(--ember); }
````

**Texto novo, literal:**

````
  .chip.on { background: var(--ember); color: #fff; border-color: var(--ember); }
  /* Custo do modulo em tags (3a.2): quanto o chip muda o Style DESTE cartao.
     Herda a cor do chip (le tanto apagado quanto aceso); so a opacidade separa. */
  .chip .cost { margin-left: 6px; opacity: .75; font-variant-numeric: tabular-nums; }
````

### E03 — funcoes puras: tags do base e custo de cada modulo — `app/index.html`

**Ancora, literal:**

````
function qSpan(text, level) {
````

**Texto novo, literal:**

````
/** Tags do style base sozinho, depois do dedup (nenhum modulo ligado). */
function baseTagCount(song) {
  return countTags(recomposedStyle(song, new Set()));
}

/** Custo marginal de cada modulo da biblioteca para ESTE cartao, em tags:
    quanto o recomposto muda se aquele chip for clicado agora (ligado: quanto
    sai; desligado: quanto entra). Medido, nunca deduzido da camada: os modulos
    de genero e de andamento costumam custar 0 porque o fragmento ja esta no
    base ("a base manda"), e uma regra por camada mandaria desliga-los a toa.
    Spec meta/specs/261027-custo-dos-modulos.md. ~10-13 ms para 50 modulos. */
function moduleCosts(song, active) {
  const now = countTags(recomposedStyle(song, active));
  const out = {};
  Object.keys(App.modulesById).forEach(id => {
    const w = new Set(active);
    if (w.has(id)) w.delete(id); else w.add(id);
    out[id] = Math.abs(countTags(recomposedStyle(song, w)) - now);
  });
  return out;
}

function qSpan(text, level) {
````

### E04 — styleQuality recebe as tags do base — `app/index.html`

**Ancora, literal:**

````
function styleQuality(style, lyrics) {
````

**Texto novo, literal:**

````
function styleQuality(style, lyrics, baseTags) {
````

### E05 — a frase da folga do base — `app/index.html`

**Ancora, literal:**

````
  if (t > L.many)  el.appendChild(qSpan("acima de ~10 o efeito das últimas tende a diluir", "warn"));
````

**Texto novo, literal:**

````
  if (t > L.many)  el.appendChild(qSpan("acima de ~10 o efeito das últimas tende a diluir", "warn"));
  // Folga do base (3a.2): diz de onde vem o excesso. Medido no acervo real, o
  // base nunca passa de 10 sozinho — quando passa, o problema e o base, nao os chips.
  if (t > L.many && typeof baseTags === "number") {
    el.appendChild(qSpan(baseTags >= L.many
      ? "o style base sozinho já usa " + baseTags + " de " + L.many + " tags — nenhum módulo cabe sem cortar o base"
      : "o style base usa " + baseTags + " de " + L.many + "; os módulos somam +" + (t - baseTags), "neutral"));
  }
````

### E06 — renderCard passa as tags do base — `app/index.html`

**Ancora, literal:**

````
  styleField.appendChild(styleQuality(recomposedStyle(song), song.lyrics));
````

**Texto novo, literal:**

````
  styleField.appendChild(styleQuality(recomposedStyle(song), song.lyrics, baseTagCount(song)));
````

### E07 — o chip ganha o rotulo e o elemento do custo — `app/index.html`

**Ancora, literal:**

````
      chip.textContent = m.label;
````

**Texto novo, literal:**

````
      chip.dataset.mid = m.id;
      const chipLabel = document.createElement("span"); chipLabel.textContent = m.label;
      const chipCost = document.createElement("span"); chipCost.className = "cost";
      chip.appendChild(chipLabel); chip.appendChild(chipCost);
````

### E08 — o clique recalcula a folga e todos os custos — `app/index.html`

**Ancora, literal:**

````
        if (oldQ) oldQ.replaceWith(styleQuality(composed, song.lyrics));
````

**Texto novo, literal:**

````
        if (oldQ) oldQ.replaceWith(styleQuality(composed, song.lyrics, baseTagCount(song)));
        // as contribuicoes interagem pelo dedup: um numero velho num chip vizinho
        // seria o FIX-007 de novo. Recalcula todos.
        refreshCosts();
````

### E09 — refreshCosts e o calculo so com o painel aberto — `app/index.html`

**Ancora, literal:**

````
  wrap.appendChild(box);
  return wrap;
}
````

**Texto novo, literal:**

````
  wrap.appendChild(box);

  /* Escreve em cada chip o custo dele em tags. So roda com o painel ABERTO:
     cartao fechado nao gasta nada. Ligado: "−N" (o que sai); desligado: "+N"
     (o que entra); "0" quando o chip nao muda o prompt — o caso que hoje engana. */
  function refreshCosts() {
    if (!wrap.open) return;
    const costs = moduleCosts(song, active);
    box.querySelectorAll("button.chip").forEach(c => {
      const n = costs[c.dataset.mid] || 0;
      const el = c.querySelector(".cost");
      el.textContent = n === 0 ? "0" : (active.has(c.dataset.mid) ? "\u2212" : "+") + n;
    });
  }
  wrap.addEventListener("toggle", refreshCosts);
  return wrap;
}
````

### E10 — DEC-019 no fim — `meta/DECISIONS.md`

**Ancora, literal:**

````
**Consequencias:** (+) O truncamento silencioso passa a ser visivel no unico ponto em que ainda se pode evitar. (+) A funcao central dos modulos volta a funcionar no botao (FIX-007). (+) Mudar um limite e mudar uma linha, sabendo de onde veio a anterior. (−) Os limites dependem de uma fonte que vende produto concorrente; reconferir quando a nota oficial do Suno os documentar. (−) O aviso de tags vai acender ambar em quase todas as faixas do album — e informacao verdadeira, mas e a que mais rapido vira paisagem; se isso acontecer, o sinal e o dono deixar de ler a linha, e o remedio e a sugestao de corte (3a.2), nao baixar o aviso.
````

**Texto novo, literal:**

````
**Consequencias:** (+) O truncamento silencioso passa a ser visivel no unico ponto em que ainda se pode evitar. (+) A funcao central dos modulos volta a funcionar no botao (FIX-007). (+) Mudar um limite e mudar uma linha, sabendo de onde veio a anterior. (−) Os limites dependem de uma fonte que vende produto concorrente; reconferir quando a nota oficial do Suno os documentar. (−) O aviso de tags vai acender ambar em quase todas as faixas do album — e informacao verdadeira, mas e a que mais rapido vira paisagem; se isso acontecer, o sinal e o dono deixar de ler a linha, e o remedio e a sugestao de corte (3a.2), nao baixar o aviso.

---

## DEC-019 — Fase 3a.2: o custo de cada modulo aparece no chip; a ferramenta nao sugere o corte

**Data:** 2026-10-27
**Contexto:** A i-026 pedia «sugerir o que cortar quando ha tags demais». A medicao no app real (`meta/specs/261027-custo-dos-modulos.md`) mostrou tres coisas. (1) O style base nunca passa de 10 tags (7 a 10 nas dez faixas): o excesso vem 100% dos modulos, e a classificacao do base por camada que a i-026 dava como requisito nao e necessaria em nenhum caso real. (2) Os modulos de genero e de andamento contribuem 0 tags em quase toda faixa, porque o fragmento ja esta no base — uma sugestao pela prioridade de camada mandaria desliga-los a toa. (3) A lista de corte automatica, pela prioridade do HISTORY §10 ou por menos cliques, chega ao mesmo resultado e manda cortar primeiro a voz de rap em ar-05 e ar-06, que sao rap-pop: a prioridade generica erra em 2 de 7 faixas reais.

**Decisao:** Cada chip mostra o seu custo marginal em tags para aquele cartao — `−N` ligado, `+N` desligado, `0` quando nao muda o prompt —, recalculado em todos os chips a cada clique e so com o painel aberto. Quando o recomposto passa de 10 tags, a linha de qualidade diz quanto o style base usa sozinho. A ferramenta mostra o custo; quem escolhe o corte e o dono.

**Alternativas consideradas:** (a) lista de corte automatica — descartada pela medicao acima; (c) a (b) com uma sugestao destacada pelo maior custo — descartada: esse criterio empata em 6 das 7 faixas, e um desempate arbitrario num destaque e lido como conselho; (d) corrigir a prioridade com uma tabela de generos centrados na voz — descartada: congelaria em codigo um conhecimento que muda com o Suno.

**Consequencias:** (+) O chip que acende sem mudar nada passa a dizer `0` — o defeito silencioso mais antigo do painel de modulos. (+) Em ar-01 e ar-04 a folga diz que o problema e o base, nao os chips. (+) 7-15 ms por cartao aberto. (−) A informacao e mais densa: 50 chips com numero. (−) O style base escrito no limite continua sendo gerado assim; a regra que o evitaria mora no prompt-modelo (i-028).
````

### E11 — i-026: a premissa corrigida — `meta/IDEAS.md`

**Ancora, literal:**

````
`[nascido da spec do painel, 2026-10-24]` O painel ja avisa quando o Style passa de ~10 tags, mas nao diz QUAIS cortar. O HISTORY §10 traz a ordem de prioridade (genero > clima > instrumento principal > vocal > BPM). Medido: 7 de 7 faixas do album de referencias passam de 10 tags so com os modulos da propria faixa (11 a 18) — o aviso ambar vai acender quase sempre, e aviso que sempre acende vira paisagem. A sugestao e o que transforma o aviso em acao. Exige classificar cada fragmento por camada, o que o recomposto nao carrega hoje: o fragmento do modulo sabe a camada, o do style base nao.
````

**Texto novo, literal:**

````
`[nascido da spec do painel, 2026-10-24]` O painel ja avisa quando o Style passa de ~10 tags, mas nao diz QUAIS cortar. O HISTORY §10 traz a ordem de prioridade (genero > clima > instrumento principal > vocal > BPM). Medido: 7 de 7 faixas do album de referencias passam de 10 tags so com os modulos da propria faixa (11 a 18) — o aviso ambar vai acender quase sempre, e aviso que sempre acende vira paisagem. A sugestao e o que transforma o aviso em acao. Exige classificar cada fragmento por camada, o que o recomposto nao carrega hoje: o fragmento do modulo sabe a camada, o do style base nao.

**Corrigido em 2026-10-27 (DEC-019).** A frase acima sobre classificar o base estava errada: medido, o style base nunca passa de 10 tags e o excesso vem todo dos modulos. E a lista de corte automatica erra em 2 de 7 faixas (manda cortar a voz de rap em rap-pop). A 3a.2 entrega o **custo de cada modulo no chip** e a folga do base, nao uma sugestao; aguarda a conferencia na tela.
````

### E12 — i-028 depois do i-027 — `meta/IDEAS.md`

**Ancora, literal:**

````
`[nascido da exploracao de 2026-10-21, candidato C4]` STATUS, CHANGELOG e README dizem a versao; o `app/index.html` publicado nao a declara em lugar nenhum. Consequencia observada: a captura de tela de 2026-10-17 nao permitia saber qual versao estava no ar. Uma linha discreta no rodape (ou no `title`) torna todo print do dono datavel, e um teste pode afirmar que ela bate com o topo do CHANGELOG. Pequeno; candidato a ir junto da proxima WO de codigo.
````

**Texto novo, literal:**

````
`[nascido da exploracao de 2026-10-21, candidato C4]` STATUS, CHANGELOG e README dizem a versao; o `app/index.html` publicado nao a declara em lugar nenhum. Consequencia observada: a captura de tela de 2026-10-17 nao permitia saber qual versao estava no ar. Uma linha discreta no rodape (ou no `title`) torna todo print do dono datavel, e um teste pode afirmar que ela bate com o topo do CHANGELOG. Pequeno; candidato a ir junto da proxima WO de codigo.

### i-028 💡 O prompt-modelo pedir folga para os modulos
`[nascido da spec da 3a.2, 2026-10-27]` Em ar-01 e ar-04 o style base que o chat escreveu ja usa 10 de 10 tags: nenhum modulo cabe sem estourar. O painel agora diz isso, mas so depois. A regra que o evitaria mora em quem escreve o base — o `schema/PROMPT-PARA-CHATS.md` poderia pedir «style base com 6 a 8 tags, deixando folga para os modulos». Pesar contra: o base mais curto pode ficar vago (abaixo de 4 tags o painel ja avisa).
````

### E13 — §10: a prioridade e generica — `meta/HISTORY.md`

**Ancora, literal:**

````
- Prioridade quando precisar cortar: genero > clima > instrumento principal > estilo vocal > BPM.
````

**Texto novo, literal:**

````
- Prioridade quando precisar cortar: genero > clima > instrumento principal > estilo vocal > BPM.
  **Nuance medida em 2026-10-27 (DEC-019):** a ordem e generica. Em generos centrados na voz (rap,
  rap-pop) o estilo vocal E o genero, e corta-lo primeiro desmonta a faixa — aplicada ao album de
  referencias, a ordem mandou cortar a voz de rap em 2 de 7 faixas. Por isso a ferramenta mostra o
  custo de cada modulo e nao sugere o corte.
````

### E14 — Em progresso — `meta/STATUS.md`

**Ancora, literal:**

````
## Em progresso

- (nada)
````

**Texto novo, literal:**

````
## Em progresso

- **3a.2 — custo de cada módulo no chip** (DEC-019, WO 0011): aplicada; falta a conferência na tela do dono.
````

### E15 — sai a pendencia do painel, ja feita — `meta/STATUS.md`

**Ancora, literal:**

````
- **Colar as Instruções no painel do Projeto.** O painel ainda tem a versão anterior à WO 0008 e diverge do `INSTRUCOES-DO-PROJETO.md` em duas linhas: `**Config:**` (falta `/ultracode`) e `**Commit:**` (falta «Bloco git parcial (só `add`) não serve.»). Abrir o arquivo, copiar tudo, colar no painel.

````

**Texto novo, literal:**

````

````

### E16 — backlog 1 — `meta/STATUS.md`

**Ancora, literal:**

````
1. **3a.2 — sugerir o que cortar quando há tags demais** (i-026). 7 de 7 faixas do álbum já acendem âmbar; aviso que sempre acende vira paisagem.
````

**Texto novo, literal:**

````
1. **3a.2 — custo de cada módulo no chip** (i-026, DEC-019): aplicada na WO 0011, aguarda a conferência na tela. A lista de corte automática foi descartada pela medição.
````

### E17 — Ultima conversa — `meta/STATUS.md`

**Ancora, literal:**

````
- **Aplicada pela WO 0010** (commit `95e6239`, empurrado): CHANGELOG, ROADMAP, IDEAS, README e este STATUS conferidos por hash de chegada; nenhum arquivo de produto tocado.
````

**Texto novo, literal:**

````
- **Aplicada pela WO 0010** (commit `95e6239`, empurrado): CHANGELOG, ROADMAP, IDEAS, README e este STATUS conferidos por hash de chegada; nenhum arquivo de produto tocado.
- **Painel do Projeto atualizado pelo dono** `[relatado pelo dono, 2026-10-27; conferido pelo chat via leitura do painel]` — as Instruções do painel batem com o `INSTRUCOES-DO-PROJETO.md`.
- **3a.2 decidida e aplicada:** o dono escolheu a opção (b) da spec `meta/specs/261027-custo-dos-modulos.md` — custo no chip, sem sugestão de corte (DEC-019).
````

## Fora de escopo

- **ROADMAP, CHANGELOG e o ✅ da i-026** — so depois da conferencia na tela do dono, e entram na proxima
  WO, sem WO propria so para isso.
- **i-028** (folga no prompt-modelo) — capturada, nao implementada.
- Corte automatico, classificar o base, tabela de generos vocais — descartados na DEC-019.
- `data/`, `schema/`, `scripts/` — nada muda.

## Armadilhas desta WO

- **E01 muda a assinatura de `recomposedStyle`** (ganha um segundo parametro opcional). Os chamadores
  antigos continuam corretos porque ele e opcional — conferido pela regressao byte a byte do chat.
- **E06 troca o `textContent` do chip por dois `span`.** Nao reintroduza `chip.textContent = ...` em
  lugar nenhum: apagaria o elemento do custo.
- **E08 tem `\u2212`** (o sinal de menos tipografico) dentro de uma string JS. Copie literal: e o
  JavaScript que o converte, nao o editor.
- **O custo so aparece com o painel aberto.** Se, testando, o chip mostrar so o rotulo com o painel
  fechado, e o comportamento certo.
- **Fim de linha:** os cinco arquivos sao LF. Se um hash de chegada divergir, rode `file <arquivo>`
  antes de concluir que uma edicao errou.

## Depois de aplicar — conferencia antes do commit

| # | Checagem | Comando | Esperado |
|---|---|---|---|
| 1 | **Os cinco arquivos sao os testados** | `sha1sum app/index.html meta/DECISIONS.md meta/IDEAS.md meta/HISTORY.md meta/STATUS.md` | a coluna **chegada** do cabecalho, os cinco. **Prova as dezessete edicoes.** |
| 2 | As funcoes novas | `grep -cE "function (moduleCosts\|baseTagCount\|refreshCosts)\b" app/index.html` | `3` |
| 3 | O recalculo no clique | `grep -c "refreshCosts();" app/index.html` | `1` |
| 4 | Nenhum `textContent` no chip | `grep -c "chip.textContent" app/index.html` | `0` |
| 5 | Os registros | `grep -c "^## DEC-019" meta/DECISIONS.md`, `grep -c "^### i-028" meta/IDEAS.md`, `grep -c "Corrigido em 2026-10-27" meta/IDEAS.md` | `1`, `1`, `1` |
| 6 | A pendencia do painel saiu | `grep -c "Colar as Instruções no painel" meta/STATUS.md` | `0` |
| 7 | Nada de produto alem do app | `GIT_OPTIONAL_LOCKS=0 git status --short data schema scripts` | saida **vazia** |
| 8 | Validacao nao regrediu | `python3 scripts/validate.py; echo "exit=$?"` | `exit=0` |
| 9 | Nenhum relatorio `.txt` no repo | `GIT_OPTIONAL_LOCKS=0 git status --short \| grep -c '\.txt'` | `0` |

**Os tres campos de cada passo:** as nove sao rodadas por **quem aplica (o Code)**, na raiz do repo
(`C:\Users\alexk\Tools\cancioneiro\cancioneiro`), em Git Bash. **Chega no ramo?** A checagem 1 cobre
os cinco arquivos inteiros, e o de chegada do app foi executado pelo chat. **Esta e qual pergunta?** As
nove respondem «esta la?». A parte que so a tela do dono responde vai no roteiro que o chat entrega **no
corpo da resposta**, nao aqui.

## Relatorio de aplicacao

Grave em `../261027-HHMM-code-cancioneiro-apply-wo0011.txt`, com o `HHMM` de `date +%y%m%d-%H%M` rodado
na hora. Diga o resultado da checagem 1 em primeiro lugar. A conferencia na tela **nao e sua**.

**Proximo comando** (ultima linha do relatorio, cru e sozinho):

```
/wrap
```

## Commit

```
git add app/index.html meta/DECISIONS.md meta/IDEAS.md meta/HISTORY.md meta/STATUS.md meta/specs meta/workorders
```

```
git commit -m "feat: custo de cada modulo no chip e a folga do style base" -m "DEC-019: cada chip mostra quantas tags ele muda no Style daquele cartao (menos N ligado, mais N desligado, 0 quando nao muda nada), recalculado em todos os chips a cada clique e so com o painel aberto; a linha de qualidade diz quanto o style base usa sozinho. A lista de corte automatica foi descartada: a medicao mostrou que ela mandaria cortar a voz de rap em faixas de rap-pop. Corrige a premissa da i-026, captura a i-028 e anota no HISTORY a nuance dos generos centrados na voz."
```

```
git push
```
