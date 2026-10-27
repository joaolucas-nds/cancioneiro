# SPEC — Fase 3a.2: o custo de cada modulo em tags (i-026)

> **Status:** Decidida
> **Decidida em:** 2026-10-27 pelo dono — **Decisao 1: (b), custo no chip.** Aplicacao:
> `meta/workorders/261027-wo0011-custo-dos-modulos.md`. Implementacao testada numa copia antes de
> virar WO: 21 de 21 criterios passaram (ver «Desfecho», no fim).
> **Data:** 2026-10-27 (data de criacao; nao muda depois)
> **Ideia de origem:** i-026 em `meta/IDEAS.md` («sugerir o que cortar quando ha tags demais»).
> **Depende de:** a 3a (DEC-018), entregue e conferida na tela em 0.5.0.
> A spec diz **o que** construir e **quando esta pronto**. Como aplicar e a WO, que nasce depois.

---

## Problema

O painel da 3a avisa em ambar quando o Style recomposto passa de ~10 tags — e no album de
referencias ele acende em **7 de 7 faixas**, com 11 a 18 tags. Aviso que sempre acende vira
paisagem: o dono aprende a nao ler a linha, e com ela vai embora o vermelho que importa. A i-026
pede que o aviso vire acao — dizer o que cortar.

E ha um problema mais antigo, que a medicao deste turno trouxe a tona: **ligar um chip de modulo
muitas vezes nao muda nada**, sem que a ferramenta diga. Em ar-05, 4 dos 6 modulos ligados
contribuem com **zero** tags — o fragmento deles ja esta no style base («a base manda», nota de
design do projeto). O dono liga, ve o chip aceso, e o prompt e o mesmo.

## Restricoes / o que foi medido

Tudo medido executando o `app/index.html` da 0.5.0 (`2d636217…`) em Chromium headless sobre
`data/demo.json` e `../album-referencias (1).json`, com as proprias `recomposedStyle` e `countTags`
do app. Contribuicao **marginal** de um modulo = quantas tags somem do recomposto ao desliga-lo, com
os outros como estao.

### O excesso vem 100% dos modulos — o style base nunca passa de 10

| faixa | tags do base | tags do recomposto | excesso | soma das marginais |
|---|---|---|---|---|
| cinzeiro-01 · cinzeiro-04 · brv-04 | 10 · 8 · 7 | 10 · 9 · 7 | 0 | — |
| ar-01 | **10** | 18 | 8 | 8 |
| ar-02 | 9 | 13 | 3 | 4 |
| ar-03 | 8 | 12 | 2 | 4 |
| ar-04 | **10** | 13 | 3 | 3 |
| ar-05 | 9 | 11 | 1 | 2 |
| ar-06 | 8 | 12 | 2 | 4 |
| ar-07 | 9 | 17 | 7 | 8 |

Em **todas** as faixas que passam de 10, desligar modulos basta para voltar a 10.

**Isto derruba a premissa que eu mesmo escrevi na i-026** («exige classificar cada fragmento por
camada, o que o recomposto nao carrega hoje: o fragmento do modulo sabe a camada, o do style base
nao»). Nenhum caso real precisa classificar o base. O problema dificil da 3a.2 nao existe nos dados.

### A armadilha: os modulos de genero e de andamento custam zero

Nas 7 faixas do album, **o modulo de genero contribui 0 em 5** e **o de andamento contribui 0 em
todas** — o fragmento ja esta no base. Uma sugestao que siga a prioridade do HISTORY §10 de baixo
para cima (BPM primeiro) mandaria desligar exatamente os modulos que nao mudam nada. Qualquer
sugestao tem de ser pela **contribuicao marginal medida**, nunca so pela camada.

### O dominio contradiz a prioridade generica — em 2 de 7 faixas reais

Simulei a sugestao automatica por prioridade de camada (HISTORY §10: genero > clima > instrumento
principal > vocal > BPM; `production` logo apos o BPM e `motion` entre instrumento e clima, que o
HISTORY nao cobre) e, em paralelo, por «menos cliques» (maior contribuicao primeiro). **As duas
chegam ao mesmo conjunto de cortes nas 7 faixas** — so a ordem muda. E as duas mandam cortar primeiro:

```
ar-05  (rap pop crossover)        -> vocal-male-rap (-1)
ar-06  (german rap pop crossover) -> vocal-male-rap (-1), vocal-male-raspy-hook (-1)
```

**Num rap, a voz de rap e o genero.** A regra «vocal vale menos que instrumento» e generica e erra
aqui. Para acertar, a ferramenta precisaria de uma tabela de generos centrados na voz — exatamente o
tipo de conhecimento que muda com o Suno e que este projeto ja aprendeu a nao congelar em codigo.

### Em ar-01, a sugestao seria «desligue 5 dos 7 modulos»

O base de ar-01 ja usa **10 de 10** tags. Qualquer modulo que acrescente algo estoura. A lista de
cortes seria tecnicamente correta e inutil: o que ela diz, de verdade, e que **o base foi escrito no
limite e nao deixou folga para modulo nenhum** — e isso e uma informacao sobre o style base, nao uma
lista de chips.

### E viavel calcular o custo de todos os chips

Os 50 custos marginais de um cartao (um `recomposedStyle` por chip) levam **9,9 ms** em ar-05 e
**12,9 ms** em ar-01, medidos com `performance.now()`.

## Criterios de aceite (verificaveis)

> Escritos para a opcao recomendada da Decisao 1, a **(b)**. Se o dono escolher (a) ou (c), esta secao
> se reescreve antes da WO.

**O custo no chip**
- [ ] Cada chip mostra, ao lado do rotulo, quantas tags ele muda no recomposto **daquele cartao**:
      chip ligado `−N` (o que sai se desligar), chip desligado `+N` (o que entra se ligar).
- [ ] **Chip ligado de custo zero aparece como `0`, nunca escondido** — e o falso positivo desta
      spec: e justamente o caso que hoje engana. Conferir em ar-05: `genre-rap-pop −1`,
      `vocal-male-rap −1`, e `instr-piano-strings`, `vocal-male-raspy-hook`,
      `mood-defiant-celebratory`, `tempo-mid-96` todos `0`.
- [ ] Conferir em ar-01: `motion-build-drop −2`, `instr-sub-bass −2`, `vocal-female-topline −2`,
      `instr-supersaw −1`, `mood-bittersweet-euphoric −1`, `genre-progressive-house 0`,
      `tempo-fast-128 0`.
- [ ] **Depois de qualquer clique num chip, os custos de TODOS os chips daquele cartao se
      recalculam** — as contribuicoes interagem pelo dedup, e um numero velho num chip vizinho seria
      o FIX-007 de novo, em outro lugar.
- [ ] Os custos so sao calculados quando o painel de modulos daquele cartao esta **aberto**. Cartao
      fechado nao gasta nada. Conferir: tempo por cartao ≤ 20 ms (medido hoje: 10-13 ms).

**A folga do base, na linha de qualidade**
- [ ] Quando o recomposto passa de 10 tags, a linha de qualidade do Style diz quanto o base usa
      sozinho: «o style base usa N de 10 tags; os modulos somam +M».
- [ ] Quando o base sozinho ja usa 10 ou mais: «o style base sozinho ja usa N de 10 — nenhum modulo
      cabe sem cortar o base». Conferir em ar-01 e ar-04.
- [ ] Ate 10 tags no recomposto, nada novo aparece.

**O que nao pode regredir**
- [ ] O rotulo do chip continua sendo o `label` do modulo; o custo e um elemento separado dentro dele.
- [ ] Todo botao «copiar» entrega o mesmo texto de antes, byte a byte — o custo nunca entra no Style.
- [ ] O export MD nao contem nenhum custo nem a frase da folga.
- [ ] Clicar o chip continua ligando e desligando como hoje; `aria-pressed` continua certo.
- [ ] Os dois temas usam os tokens que ja existem; nenhuma cor literal.
- [ ] Nenhum `pageerror`.

## Decisoes de design

- **Mostrar o custo, nao decidir o corte.** A medicao mostrou que a regra de prioridade erra em 2 de
  7 faixas e que a lista de cortes, onde e longa, esconde a causa real (o base no limite). O chip ja
  e o lugar onde o dono decide; e la que a informacao tem de estar.
- **Custo marginal recalculado, nunca a camada.** Medir e barato (10-13 ms) e e a unica forma de nao
  sugerir desligar um modulo que nao muda nada.
- **Tags, nao caracteres, no chip.** O excesso de tags acende em 7 de 7 faixas; o de caracteres so
  com a biblioteca inteira ligada, e a linha de qualidade ja o mostra ao vivo a cada clique.
- **A folga do base e frase, nao numero solto.** «N de 10» sozinho nao diz que o problema e o base; a
  frase diz.
- **Descartado: corrigir a prioridade do HISTORY com uma tabela de generos vocais.** Seria congelar no
  codigo um conhecimento de dominio que muda com o Suno — o oposto do que o DEC-018 fez com os limites.

## Fora de escopo

- **Corte automatico** ou botao «aplicar sugestao». O clique no chip ja existe.
- **Classificar o style base por camada.** Nenhum caso real precisa (ver «Restricoes»).
- **Corrigir o style base.** A folga mostra o problema; reescrever o base e trabalho do chat que gera
  o acervo — candidato a regra no `schema/PROMPT-PARA-CHATS.md` («deixe folga para modulos»), em
  ideia propria.
- **Atualizar a prioridade do HISTORY §10** com a nuance dos generos centrados na voz. E registro de
  dominio, vai pela WO desta spec como nota, nao como codigo.
- **i-020, BPM (i-005), versao no app (i-027).**

## Passos

1. Funcao pura que, dado um cartao e o conjunto de modulos ligados, devolve o custo marginal de cada
   modulo da biblioteca. Testavel sem DOM, contra os numeros de ar-05 e ar-01 acima.
2. O custo dentro de cada chip, calculado ao abrir o painel e recalculado em todos os chips a cada
   clique.
3. A frase da folga do base na linha de qualidade do Style.
4. Regressao: copia byte a byte, export MD, `aria-pressed`, os dois temas.

---

## Ponto de decisao

### Decisao 1 — O que a 3a.2 entrega?

- **(a) Lista de corte automatica, como a i-026 descreve** — «para voltar a 10: desligue X e Y». E o
  que foi pedido. Medido: manda cortar a voz de rap em ar-05 e ar-06, e em ar-01 manda desligar 5 de
  7 modulos sem dizer que o problema e o base.
- **(b) Custo no chip + folga do base na linha de qualidade.** Cada chip mostra `+N` ou `−N` tags; a
  linha diz quando o base sozinho ja esta no limite. Nenhuma prioridade embutida; quem conhece a faixa
  escolhe o corte. Resolve tambem o chip que hoje acende sem mudar nada. **Recomendado.**
- **(c) (b) mais uma sugestao destacada, so pela maior contribuicao** (sem prioridade de camada). Em ar-05
  destacaria `genre-rap-pop` ou `vocal-male-rap`, ambos `−1` — o desempate seria arbitrario, e o
  arbitrario num destaque parece recomendacao.

---

## Desfecho — 2026-10-27

**Resposta do dono:** Decisao 1 → **(b)**. Ele perguntou por que a (c) nao foi recomendada; a resposta,
medida: o unico criterio de um destaque seria o tamanho do custo, e esse criterio **empata em 6 das 7
faixas** do album (ar-07: quatro modulos a −2; ar-02 e ar-06: quatro a −1; ar-05: genero e voz de rap
a −1). Desempate arbitrario num destaque e lido como conselho. E custo mede tamanho, nao valor: o
modulo que mais soma costuma ser o escolhido de proposito.

**Uma coisa que a implementacao revelou:** a interacao entre modulos pelo dedup — o motivo de o
clique recalcular TODOS os custos do cartao — existe, mas e rara: em todo o album, so **2 cliques**
mudam o custo de um chip vizinho (desligar `mood-nostalgic` em ar-04 leva `mood-bittersweet-euphoric`
de +1 para +2, e o simetrico em ar-07). O primeiro teste de vizinhanca falhou por ter escolhido um
clique sem interacao; foi trocado pelo caso real, que passa. Recalcular todos continua sendo o certo:
custa 7-15 ms, e o caso raro e justamente o que um numero velho esconderia.

**Bateria de aceite numa copia do `app/index.html`, Chromium headless, temas claro e escuro: 21 PASSA,
0 FALHA.** Inclui os custos exatos de ar-05 e ar-01; o chip clicado trocando de sinal; o vizinho de
ar-04 indo de +1 a +2 na tela; nenhum custo calculado com os paineis fechados; `moduleCosts` em 7-15 ms
em ar-01; a folga em ar-01, ar-04 e ar-07, e sumindo quando o corte traz o recomposto de volta a 10;
todo botao copiar e o export MD identicos ao de antes, byte a byte, com e sem chips clicados.
