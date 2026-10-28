# SPEC — Fase 3b: controle de BPM no cartao (i-005)

> **Status:** Decidida
> **Decidida em:** 2026-10-28 pelo dono — **1a, 2a, 3a, 4a** (as quatro recomendadas). Aplicacao:
> `meta/workorders/261028-wo0013-controle-de-bpm.md`. Implementacao testada numa copia antes de
> virar WO: 44 de 44 criterios passaram (ver «Desfecho», no fim).
> **Data:** 2026-10-28 (data de criacao; nao muda depois)
> **Ideia de origem:** i-005 em `meta/IDEAS.md` («BPM como valor manipulavel na ferramenta, slider ou
> stepper, refletindo no style copiado»). Pedido explicito na premissa original.
> **Depende de:** a 3a.2 (DEC-019), entregue e conferida na tela em 0.6.0.
> A spec diz **o que** construir e **quando esta pronto**. Como aplicar e a WO, que nasce depois.

---

## Problema

O BPM de uma faixa aparece em **tres lugares**: no texto do `style` («128 bpm»), no campo `bpm` (que o
cartao mostra como «128 BPM», so referencia) e, quando a faixa cita um, no fragmento do modulo de
andamento. Hoje nada na ferramenta muda o BPM: para testar a faixa mais lenta, o dono copia o Style,
edita o numero a mao no Suno e torce para nao esquecer um.

E o unico instrumento que parece fazer isso — a camada **Andamento** do painel de modulos — **nunca
muda o BPM; so contradiz**. A medicao abaixo mostra que todo clique num chip de andamento poe um
segundo BPM no prompt.

## Restricoes / o que foi medido

Tudo medido executando o `app/index.html` da 0.6.0 (`6785fca2…`) em Chromium headless sobre
`../album-referencias (1).json`, com a propria `recomposedStyle` do app; e lendo os tres acervos
(`data/demo.json`, `data/exemplo-cinzeiro.json`, o album) por script.

### Hoje as tres fontes concordam — em 10 de 10 faixas

| faixa | campo `bpm` | numero no `style` | modulo de andamento citado |
|---|---|---|---|
| cinzeiro-01 | 70 | 70 | `tempo-slow-70` («slow tempo 70 bpm») |
| cinzeiro-04 · brv-04 | 75 · 128 | 75 · 128 | — |
| ar-01 · ar-03 | 128 | 128 | `tempo-fast-128` («128 bpm») |
| ar-02 | 140 | 140 | `tempo-140` |
| ar-04 | 90 | 90 | `tempo-90` |
| ar-05 · ar-06 | 96 | 96 | `tempo-mid-96` |
| ar-07 | 126 | 126 | `tempo-126` |

Nenhuma faixa tem BPM no `lyrics` (0 de 10). Nenhuma tem dois numeros diferentes no `style`. Nenhuma
esta sem BPM no `style`. **A divergencia entre as fontes e risco, nao fato** — o chat que gera o
acervo tem sido consistente.

### A camada Andamento poe dois BPM no prompt — em 49 de 49 cliques

O album traz 8 modulos de andamento (70, 90, 96, 100, 126, 128, 140, 174). Ligando, em cada faixa,
cada um que ela nao cita:

```
ar-01  ligar tempo-slow-70  ->  "... 128 bpm, ... 70 bpm"   (o mesmo nas 7 faixas, 7 de 7 cada)
```

A dedup por palavras (FIX-003) ve «128 bpm» e «70 bpm» como coisas diferentes, e as duas entram. E
**desligar** o modulo de andamento da faixa nao tira o BPM: ele continua no `style` base («a base
manda», nota de design). Ou seja: o chip de andamento so tem dois efeitos possiveis — nenhum (custo
`0`, como a 3a.2 ja mostra) ou um prompt contraditorio.

### O prototipo da regra resolve os dois — 56 de 56

Prototipo (no proprio app, sem gravar nada): antes da dedup, reescrever **todo** «NN bpm» do base e
dos fragmentos dos modulos para um unico valor V. Resultado:

- **56 de 56** combinacoes (7 faixas × 8 modulos de andamento) saem com **exatamente um** BPM no Style.
- **7 de 7** faixas: trocar o numero **nao muda a contagem de tags** — o painel de qualidade segue igual.
- Efeito colateral bom: o fragmento «slow tempo 70 bpm» vira redundante (ja contem «70 bpm» do base
  reescrito) e sai pela dedup. Exemplo, ar-04 a 70:
  `cinematic downtempo interlude, felt piano chords, ..., slow build, wistful, 70 bpm, c minor, ...`
  — o numero fica **no lugar onde o base o pos**, nao no fim.

### As variantes tem BPM proprio, de proposito

| faixa | BPM principal | variantes |
|---|---|---|
| ar-03 | 128 | VAR A «drum and bass 174» → **174** · VAR B «piano e voz crescendo» → **80** |
| ar-01 · ar-02 · brv-04 | 128 · 140 · 128 | 124 · 128 · 130 |
| ar-05 · cinzeiro-04 | 96 · 75 | iguais ao principal |

Em ar-03 VAR A, o 174 **e** a variante. O controle nao pode tocar nelas.

### O que o Suno diz sobre BPM (outubro de 2026)

- A nota oficial do v6 (2026-09-09) **nao menciona** BPM nem tempo.
- O help center oficial documenta BPM **so no Studio** («Transport controls», editado em 2025-09-25):
  projeto com Tempo padrao 120, «Follow Track» ou «Manual Tempo». **Nao documenta campo de BPM no
  Create** — o BPM continua indo como texto no Style.
- Guia secundario de 2026: o v6 «le o style mais literalmente»; e o slider **Variety** acima de 0 pode
  reescrever as tags do style (testado no v5, nao confirmado para BPM). Se for verdade, Variety 0 e a
  condicao para o numero chegar intacto — registro de dominio, nao codigo.
- O HISTORY ja registra: BPM e aproximacao, nao comando. **A ferramenta ajuda a escrever o numero;
  nao garante que o Suno obedeca.**

## Criterios de aceite (verificaveis)

> Escritos para as opcoes recomendadas: **1(a), 2(a), 3(a), 4(a)**. Outra escolha reescreve esta
> secao antes da WO.

**O controle**
- [ ] O «128 BPM» da linha de metadados do cartao vira um controle: campo numerico (20 a 300, o
      limite do esquema), botoes `−5` e `+5`, e — so quando o valor difere do original — um botao
      «voltar a 128».
- [ ] Valor inicial = o numero que esta no `style` (e o que o Suno ve). Se o `style` nao tiver
      numero, o campo `bpm`. Se nenhum dos dois, o controle nasce vazio.
- [ ] Mudar o valor reescreve **todo** «NN bpm» do Style recomposto para o novo valor, antes da dedup:
      o bloco copiavel, a linha de qualidade e o recomposto do painel de modulos mudam na hora.
- [ ] O botao «copiar» do Style entrega o numero novo (FIX-007: o que se ve e o que se cola).
- [ ] Conferir em ar-01: 128 → 120 → o Style copiado tem `120 bpm` uma vez e `128` nenhuma.
- [ ] Faixa sem BPM no `style` e controle preenchido: «NN bpm» entra **no fim** do Style (+1 tag, que
      a linha de qualidade conta). Controle vazio: nada entra. (Nenhuma faixa real cai aqui; o teste
      usa uma faixa de prova.)
- [ ] Valor fora de 20-300 ou nao numerico: o Style nao muda e o campo mostra o limite. Nunca
      `NaN bpm` no prompt.

**Os chips de andamento**
- [ ] Clicar num chip de andamento **move o controle** para o numero dele e desliga o outro chip de
      andamento que estava ligado (no maximo um ligado). O Style fica com um BPM so.
- [ ] Mudar o controle a mao para um numero que nao e de nenhum chip desliga o chip de andamento
      ligado; voltar ao numero de um chip nao o religa sozinho (o chip e atalho, nao espelho).
- [ ] **Falso positivo desta spec:** em nenhuma das 56 combinacoes (7 faixas × 8 chips) o Style tem
      dois BPM. E os chips das **outras** camadas continuam ligando e desligando como hoje, mais de
      um por camada.

**O que nao pode regredir**
- [ ] As variantes copiam exatamente o texto delas: ar-03 VAR A continua `174`, com o controle em
      qualquer valor.
- [ ] Com o controle no valor original, todo botao copiar e o export MD saem **byte a byte** iguais
      aos da 0.6.0.
- [ ] O export MD usa o valor do controle **nos dois lugares**: no bloco do Style e na linha de
      metadados («BPM: 120»). Nunca um numero num e outro no outro.
- [ ] «Baixar .json» sai igual ao importado: o controle nao grava na colecao.
- [ ] Os custos dos chips (3a.2) continuam certos depois de mexer no controle.
- [ ] Os dois temas usam os tokens que ja existem; nenhuma cor literal. Nada de rolagem lateral a
      375 px. Nenhum `pageerror`.

**O validador (Decisao 4)**
- [ ] `scripts/validate.py` reprova (codigo 1) a faixa cujo `style` tem dois numeros de BPM
      diferentes, ou cujo campo `bpm` difere do numero do `style`, dizendo a faixa e os dois numeros.
- [ ] Os tres acervos atuais passam (10 de 10 concordam). Teste negativo: `bpm` 75 com «70 bpm» no
      style reprova.

## Decisoes de design (ja tomadas pela medicao)

- **Uma regra so: o controle governa todo «NN bpm» do Style principal.** E o que o prototipo
  mostrou funcionar em 56 de 56, sem tocar na dedup e sem mudar a contagem de tags.
- **O numero fica onde o base o pos.** Reescrever no lugar preserva a ordem que o chat escolheu (as
  primeiras palavras pesam mais).
- **O controle mora onde o BPM ja aparece**, na linha de metadados. Fora do bloco copiavel — a regra
  inviolavel do projeto continua de pe: o controle e referencia que edita o conteudo, nunca entra nele.
- **Variantes fora.** Cada variante e uma faixa-irma com o andamento dela.

## Fora de escopo

- **Contradicao de palavras.** A 140, ar-04 continua dizendo «downtempo» e «slow build». Avisar exige
  saber que palavra combina com que faixa de BPM — tabela de dominio que muda com o Suno. Candidata a
  ideia propria (**i-029**, aviso de andamento contraditorio), capturada pela WO.
- **BPM no Lyrics** (`[110 BPM]`, tag de secao). Nenhuma faixa usa; outro campo, outra spec.
- **Manual Tempo do Studio.** Recurso da DAW do Suno, nao do prompt.
- **Half-time / double-time.** «half-time» em ar-02 e palavra do base; o controle nao a interpreta.
- **Mexer no `schema/style-modules.json`** (renomear «Rapido ~128 BPM», etc.). Os modulos seguem como
  estao; so o comportamento do chip muda.

## Passos

1. Funcao pura `withBpm(style, v)` (reescreve todo «NN bpm»; sem numero e com v, acrescenta no fim)
   e o valor inicial por faixa. Testavel sem DOM contra a tabela acima.
2. `recomposedStyle` aplica o valor do controle ao base e aos fragmentos antes da dedup.
3. O controle na linha de metadados; a mudanca atualiza bloco, qualidade, recomposto e custos — pelo
   mesmo caminho do clique no chip.
4. Chips de andamento como atalho exclusivo.
5. Export MD com o valor do controle nos dois lugares.
6. `check_bpm` no `validate.py`.
7. Regressao: copia e export byte a byte no valor original, variantes, «Baixar .json», os dois temas.

---

## Ponto de decisao

### Decisao 1 — O valor escolhido fica guardado?

- **(a) So nesta sessao, como os modulos.** Recarregou, volta ao do acervo. O export MD leva o valor
  escolhido. Coerente com os chips: guardar um e nao o outro faria o Style copiado depois de recarregar
  misturar BPM novo com modulos originais. **Recomendado.**
- **(b) Lembrado no navegador, como o «usei».** Sobrevive ao recarregar, mas so naquele navegador, e o
  dono ve um numero que o arquivo nao tem.
- **(c) Gravado no «Baixar .json»** (campo `bpm` e texto do `style`). O app passa a editar o acervo — o
  que ate hoje ele nao faz (o FIX-004 tirou estado da colecao de proposito). Mudanca de papel, nao de
  recurso.

### Decisao 2 — O que fazer com a camada Andamento?

- **(a) O chip vira atalho:** clicar move o controle para o numero dele; no maximo um ligado.
  Aproveita os 8 andamentos do album como pontos de salto. **Recomendado.**
- **(b) Deixar os chips como estao**, so com o numero reescrito pelo controle. Sem contradicao, mas o
  chip passa a ter custo `0` quase sempre: um botao que nao faz nada.
- **(c) Esconder a camada Andamento** quando a faixa tem controle de BPM. Mais simples; perde os
  atalhos.

### Decisao 3 — Que forma o controle tem?

- **(a) Campo numerico com `−5` / `+5` e «voltar a N».** Valor exato, digita-se direto, cabe na linha
  de metadados no celular. **Recomendado.**
- **(b) Slider, como a i-005 sugeriu.** Bom para explorar, ruim para acertar um numero: 280 valores
  num trilho de ~300 px no celular e ~1 BPM por pixel.

### Decisao 4 — O validador confere o BPM do acervo?

- **(a) Sim, como erro (codigo 1):** dois numeros no `style`, ou `bpm` diferente do `style`. Hoje
  passa 10 de 10; o custo e zero e pega o erro do chat na autoria. **Recomendado.**
- **(b) So aviso** (nao muda o codigo de saida).
- **(c) Nao.** O controle ja escolhe o numero do `style`; a divergencia so confunde a referencia.

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
