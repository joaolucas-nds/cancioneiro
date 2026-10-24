# SPEC — Painel de qualidade do prompt (Fase 3a: i-017 a i-020)

> **Status:** Decidida
> **Decidida em:** 2026-10-24 pelo dono — **1: so avisa · 2: nao dispara no instrumental · 3: adia o i-020.**
> Aplicacao: `meta/workorders/261024-wo0009-painel-de-qualidade.md`. Implementacao testada numa copia
> antes de virar WO: 18 de 18 criterios de aceite passaram (ver «Desfecho», no fim).
> **Data:** 2026-10-24 (data de criacao; nao muda depois)
> **Ideias de origem:** i-017, i-018, i-019, i-020 em `meta/IDEAS.md`. Fundamento de dominio em
> `meta/HISTORY.md` §9-11 e §13, **reconferido na web neste turno** (ver «Restricoes»).
> A spec diz **o que** construir e **quando esta pronto**. Como aplicar e a WO, que nasce depois.

---

## Problema

A ferramenta hoje **organiza** prompts mas nao **julga** nenhum. Ela recompoe o Style de cada faixa
somando o base aos modulos ligados, mostra o resultado e deixa copiar — e nao diz nada quando o que vai
ser copiado e ruim para o Suno.

E ha um problema que so uma ferramenta resolve: **o Suno trunca em silencio.** Passou do limite do
campo, o excedente nao chega ao modelo, sem aviso e sem erro; o dono so descobre porque «saiu
estranho». A premissa original do projeto ja intuia isto («consumir espaco desnecessario»).

**O que a medicao deste turno mostrou, e que muda o peso de cada ideia:** o risco nao mora no texto que
o chat escreve — mora nos **modulos**, que so somam. Nenhuma faixa real chega perto do limite pelo
style base; quase todas passam do ponto doce de tags pelos modulos da propria faixa, e todas
truncariam com a biblioteca inteira ligada.

Para quem: o dono, no momento de copiar. O painel e para ser lido em meio segundo antes do clique em
«copiar», nao estudado.

## Restricoes / o que foi medido

### O mundo mudou desde o HISTORY — e o que isso significa para os numeros

O `meta/HISTORY.md` e de julho/2026 e fala de V4.5/V5/V5.5. **O Suno lancou o v6 em 9/set/2026**, em
tres variantes (v6, v6-wild, v6-mini) — confirmado pela nota oficial
(`https://suno.com/release-notes/introducing-v6`). Mas a nota oficial **nao menciona limite de campo
nenhum, nem comportamento de tags**, e **nao diz se os modelos antigos foram aposentados**.

Os numeros vem de **uma fonte secundaria**, que vende produto concorrente
(`https://hookgenius.app/learn/suno-character-limits/`, atualizada em 8-9/set/2026):

| Campo | Limite | Forca da evidencia |
|---|---|---|
| Style of Music | 1.000 | igual ao v5.5; a fonte diz valer para v6 |
| Lyrics | 5.000 (doce ~3.000) | a propria fonte chama de «consenso, nao verificado independentemente» |
| **Exclude Styles** | **1.000** | **novo para nos** — medido pela fonte via `maxlength="1000"` no campo, **em v5.5** |
| Titulo | incerto no v6 | a fonte se contradiz (sem `maxlength` no v6, mas lista 100) |

Truncamento silencioso: a fonte confirma. Tags: a pesquisa dela foi **testada em v5/v5.5 e rotulada
como v6**, e ela mesma suaviza o teto — acima de ~10 tags «o ganho achata, em vez de o resultado
quebrar». Ordem: «o Suno *parece* pesar mais as primeiras tags», sustentado por **um** teste.

**Consequencia de design, nao opiniao:** os limites mudaram uma vez (V4 → V4.5) e o modelo acabou de
mudar de novo sem documentar os numeros. Eles nao podem virar constante espalhada pelo codigo.

### O acervo real contra os limites

Medido executando o `app/index.html` em Chromium headless sobre `data/demo.json` e o
`album-referencias (1).json`, usando a propria `recomposedStyle` do app:

| faixa | recomposto (modulos da faixa) | com TODOS os modulos ligados |
|---|---|---|
| cinzeiro-01 · cinzeiro-04 · brv-04 | 116–174 c · 7–10 tags | 603–637 c · 36–37 tags |
| ar-01 a ar-07 (biblioteca de 50 modulos) | **188–298 c · 11–18 tags** | **1.237–1.296 c · 71–75 tags** |

Lyrics: o mais longo tem **1.464 c** (ar-06) — metade do ponto doce.
Exclude: o mais longo tem **46 c**.

| aviso | dispara no acervo de hoje? |
|---|---|
| **i-017** caracteres do Style | **0 faixas** no recomposto atual; **7 de 7** do album com a biblioteca inteira ligada |
| **i-017** caracteres do Lyrics | **0 faixas** |
| **i-018** tags acima de ~10 | **7 de 7** faixas do album, **ja hoje**, so com os modulos da propria faixa |
| **i-019** «no X» no style | **3 faixas** (cinzeiro-01: `no drums`, `no vocals`; cinzeiro-04 e ar-04: `no vocals`) |
| **i-020** primeiro fragmento nao e genero | **0 de 10** faixas |

### O falso positivo que a propria medicao produziu

Procurando «no X» por substring (`'no ' in fragmento`), a medicao deste turno casou **pia·no**,
**sopra·no** e **pia·no and strings** na biblioteca de modulos. E o FIX-003 de novo, e e exatamente a
implementacao que sai por reflexo. Por fronteira de palavra, os nove casos-armadilha abaixo nao casam
e os dois verdadeiros casam:

```
delicate piano arpeggios  -> []        nostalgic synth   -> []
female soprano soloist    -> []        notorious bass    -> []
piano and strings         -> []        snow piano        -> []
nocturne strings          -> []        casino lounge     -> []
techno, no-wave           -> []        <- "no wave" e GENERO, nao negacao
dark ambient, no drums, no vocals -> ['no drums', 'no vocals']
```

### A ferramenta e so-leitura, por desenho

`app/index.html`, comentario na recomposicao: «a ferramenta MOSTRA o resultado e deixa copiar — nao
reescreve o JSON». O DEC-004 diz que o arquivo e a fonte de verdade. **O i-019, como esta escrito no
IDEAS («oferece mover para `excludeStyles` num clique»), quebra isso**: seria a primeira vez que a
ferramenta altera o dado do acervo. Ver Decisao 1.

### Uma negacao do projeto e deliberada

O modulo `vocal-none` (em `schema/style-modules.json` e no album) tem fragmento `no vocals` e a nota
«Reforco redundante ao [Instrumental] no Lyrics. Sempre em faixa instrumental.» E o HISTORY §11 avisa:
«1-2 restricoes negativas ajudam a direcionar — o objetivo nao e eliminar negacoes, e coloca-las no
campo certo». Um aviso ingenuo de «no X» contradiria um modulo que o proprio projeto criou. Ver
Decisao 2.

## Criterios de aceite (verificaveis)

> Cada linha e conferivel por comando (headless) ou por roteiro de tela. «Passou/nao passou», nunca
> «parece bom».

**Onde e o que se mede**
- [ ] O painel mede o **Style recomposto** — o mesmo texto que o botao «copiar» do Style entrega —,
      nunca o `style` base. Conferir: para ar-01 o painel mostra **298** caracteres, nao 164.
- [ ] O painel **se atualiza quando um chip de modulo muda**, sem recarregar. Conferir: em ar-01,
      ligar um chip apagado faz o numero de caracteres subir no mesmo clique.
- [ ] Mede tambem **Lyrics** e **Exclude Styles** (este pela string que o botao «copiar exclude»
      entrega, `excludeStyles.join(", ")`).
- [ ] Os limites vivem num **unico objeto** no app, com a fonte e a data de cada numero ao lado, em
      comentario. Conferir: `grep -c "1000" app/index.html` nao cresce em mais de um lugar por limite.

**i-017 — caracteres**
- [ ] Style: verde ate 850 (85%), ambar de 851 a 1.000, **vermelho acima de 1.000** com o texto
      «o Suno corta o que passar de 1.000 — sem aviso».
- [ ] Lyrics: verde ate 3.000, ambar de 3.001 a 5.000 («acima de ~3.000 o Suno tende a correr e pular
      secoes»), vermelho acima de 5.000.
- [ ] Exclude Styles: mesma regua do Style (1.000).
- [ ] **Prova de vida do vermelho:** em ar-01, com todos os modulos ligados, o Style mostra
      **1.271** caracteres em vermelho. Sem esse caso o vermelho nunca e visto no acervo real.

**i-018 — tags**
- [ ] Conta tags como o Suno as recebe: fragmentos separados por virgula, apos o dedup do recomposto.
      Conferir: ar-01 mostra **18**, cinzeiro-01 mostra **10**.
- [ ] Ate 8: verde. De 9 a 10: neutro. **Acima de 10: ambar**, com o texto «acima de ~10 o efeito das
      ultimas tende a diluir». **Nunca vermelho:** passar de 10 nao perde informacao, so dilui — o
      vermelho fica reservado ao truncamento, que perde.
- [ ] Abaixo de 4: ambar, «vago demais».

**i-019 — negacao no style**
- [ ] Deteccao por **fronteira de palavra**, nunca por substring. Conferir pelos onze casos da secao
      «O falso positivo»: os nove armadilha nao disparam, os dois verdadeiros disparam.
- [ ] `no-wave` e qualquer `no` seguido de hifen **nao** disparam.
- [ ] Ao detectar, **so avisa** (Decisao 1): nada no acervo muda.
- [ ] `no vocals` **nao** dispara em faixa instrumental (Decisao 2) — ver «Desfecho» para a definicao de instrumental que a medicao impos.

**i-020 — ordem** *(sujeito a Decisao 3)*
- [ ] Se o primeiro fragmento do recomposto nao corresponder a nenhum fragmento da camada `genre` da
      biblioteca carregada, uma nota **neutra** (nunca ambar) diz «o genero rende mais nas primeiras
      palavras». Conferir: nenhuma das 10 faixas reais dispara.

**O que nao pode regredir**
- [ ] O botao «copiar» de cada campo entrega **exatamente** o mesmo texto de antes. O painel le, nao
      altera. Conferir: string copiada de ar-01 antes e depois da mudanca, byte a byte.
- [ ] **Regra de dominio inviolavel:** nenhum texto do painel entra no bloco copiavel nem no export MD.
      Conferir: o `.md` exportado de ar-01 nao contem «caracteres», «tags» nem nenhuma frase de aviso.
- [ ] Faixa sem `excludeStyles` nao ganha linha de exclude vazia.
- [ ] Os dois temas (claro e escuro) usam os tokens de cor que ja existem (`--moss`, `--ember`,
      `--ink-soft`), mais **um** token novo para o ambar — nunca cor literal.

## Decisoes de design

- **Medir o recomposto, nao o base.** E o que vai para o Suno. Medir o base seria medir o texto que
  nunca passa do limite e ignorar o vetor real de risco, que sao os chips.
- **Tres niveis, e o vermelho e so para perda.** Vermelho = o Suno vai cortar texto. Ambar = vai
  funcionar, mas pior. Verde = ok. Passar de 10 tags e ambar e nao vermelho porque, pela propria fonte,
  o ganho achata e nada se perde — e um painel que acende vermelho em 7 de 7 faixas vira ruido que se
  aprende a ignorar, e leva junto o vermelho que importa.
- **Limites como configuracao, com fonte e data.** Um objeto unico, comentado com «fonte, data,
  modelo». Quando o Suno mudar de novo, muda-se uma linha e se sabe de onde veio a anterior.
- **Nenhum bloqueio.** O painel avisa; nunca impede de copiar. O dono pode querer colar 1.200
  caracteres sabendo que perde o fim.
- **Exclude Styles entra no painel.** E o unico numero novo que a reconferencia trouxe, e o campo e
  copiavel — tem o mesmo risco de truncamento dos outros dois.
- **Descartado: medir na hora de copiar, com um alerta.** Alerta interrompe o gesto e o dono aprende a
  fecha-lo sem ler. O painel fica sempre visivel, ao lado do botao.

## Fora de escopo

- **Editar o Style a mao no cartao** (opcao (b) do handoff de julho). E outra frente, e muda a
  natureza da ferramenta do mesmo jeito que a Decisao 1.
- **Sugestao automatica do que cortar** (o i-018 menciona «sugerindo o que cortar pela ordem de
  prioridade»). Exige classificar cada fragmento por camada, o que o recomposto nao carrega hoje.
  Candidata a 3a.2, depois desta.
- **Controle de BPM** (i-005). Mexe na mesma area do cartao, mas e 3b.
- **Combobox de modulos** (i-011).
- **Titulo.** A propria fonte se contradiz sobre o limite no v6.
- **Atualizar o `meta/HISTORY.md` sobre o v6.** E registro, e vai pela WO desta spec — nao e
  construcao.

## Passos

1. **O objeto de limites**, com fonte e data, e uma funcao pura que recebe um texto e um limite e
   devolve `{n, nivel}`. Testavel sem DOM.
2. **i-017 no Style**, ligado ao recomposto e ao clique dos chips. E o passo que prova a arquitetura:
   se ele atualiza ao vivo, os outros sao repeticao.
3. **i-017 em Lyrics e Exclude.**
4. **i-018**, reaproveitando a contagem do passo 2.
5. **i-019**, so depois das Decisoes 1 e 2.
6. **i-020**, so se a Decisao 3 o mantiver.
7. **Regressao:** a string copiada e o export MD byte a byte, antes e depois.

Cada passo entrega algo visivel e testavel sozinho. Se a WO for uma so, ela segue esta ordem; se for
fatiada, o corte natural e entre o passo 4 e o 5 — tudo antes dele so le, tudo depois depende de
decisao.

---

## Ponto de decisao — tres perguntas, e o resto da spec nao depende delas

### Decisao 1 — O i-019 «migra num clique» ou so avisa?

O IDEAS diz «oferece mover para `excludeStyles` num clique». Isso seria **a primeira vez que a
ferramenta escreve no acervo** — hoje ela e so-leitura por desenho, e o DEC-004 faz do arquivo a fonte
de verdade.

- **(a) So avisa** — destaca o «no X» e diz «mais confiavel no campo Exclude». O dono corrige o JSON
  por conta. Zero mudanca de natureza. **Recomendado para a 3a.**
- **(b) Migra num clique** — altera `style` e `excludeStyles` em memoria; para persistir, o dono baixa
  o `.json`. Mais util, mas abre a pergunta que a ferramenta nunca precisou responder: o que acontece
  com uma alteracao que o dono esqueceu de baixar? Isto pede analise propria, nao uma linha de spec.

### Decisao 2 — `no vocals` em faixa instrumental dispara?

O modulo `vocal-none` do proprio projeto injeta `no vocals` como «reforco redundante ao
[Instrumental]», e o HISTORY §11 diz que 1-2 negacoes ajudam.

- **(a) Dispara sempre** — consistente, mas contradiz um modulo do projeto em toda faixa instrumental.
- **(b) Nao dispara para `no vocals` quando o Lyrics contem `[Instrumental]`** — reconhece o reforco
  deliberado; tudo o mais dispara. **Recomendado.** Conferir: cinzeiro-01 continua avisando `no drums`
  e para de avisar `no vocals`.
- **(c) Tom informativo, nunca ambar** — avisa tudo, mas como dica neutra.

### Decisao 3 — O i-020 entra na 3a?

Medido: **dispara em 0 de 10 faixas reais.** A evidencia de dominio e a mais fraca das quatro («o
Suno *parece*», um teste so). E a deteccao comparando com a camada `genre` e fragil: `dark ambient
cinematic intro` so casou porque contem `dark ambient`.

- **(a) Entra, como nota neutra** — custo baixo, valor baixo.
- **(b) Fica para depois** — volta ao IDEAS com o numero medido («0/10 em 2026-10-24») como gatilho
  para reabrir. **Recomendado:** o painel nasce com tres avisos que disparam de verdade, e o quarto
  entra quando aparecer a primeira faixa que ele pegaria.

---

## Desfecho — 2026-10-24

**Respostas do dono:** Decisao 1 → **(a) so avisa**. Decisao 2 → **nao dispara no instrumental**.
Decisao 3 → **(b) adia o i-020**, que volta ao IDEAS com o numero medido como gatilho.

**Duas coisas que a implementacao revelou e que esta spec nao tinha previsto:**

**1. Um bug pre-existente que tornava o painel enganoso — vira FIX-007.** O botao «copiar» de cada
campo capturava o texto no momento em que o cartao era criado (`copyText(content, btn)`), mas o clique
num chip de modulo so atualizava o bloco visual. Medido em headless, em ar-01: o bloco foi de **298 para
322** caracteres ao ligar um chip, e o botao continuou entregando **os 298 antigos**. O que se via nao
era o que se copiava — toda a troca de estilo por modulo (i-004) nunca chegou ao Suno pelo botao, so
pelo export MD, que recompoe na hora. Sem corrigir isto, o painel mostraria 322 e o botao copiaria 298,
e o dono confiaria no painel. Correcao: o botao le o bloco na hora do clique. Uma linha.

**2. A redacao da Decisao 2 era mais estreita que a intencao.** A opcao (b) dizia «quando o Lyrics
contem `[Instrumental]`». O dono respondeu «nao dispara no **instrumental**». A medicao mostrou a
diferenca: cinzeiro-01 e instrumental (style com `no vocals`, Lyrics so com
`[Intro] [Build] [Climax] [Outro]`), mas nao usa a tag `[Instrumental]` — o que o dominio deste projeto
aceita para faixa linear. Com a redacao literal ele avisaria `no vocals`. A implementacao segue a
intencao: **instrumental = Lyrics sem nenhuma linha de letra, so tags entre colchetes.** Testado nos
dois lados: cinzeiro-01 avisa so `no drums`; faixa com letra e `no vocals` avisa (e contraditorio);
Lyrics vazio avisa (nao ha prova de instrumental); a excecao vale so para `no vocals`, nunca para
`no drums`. **Se o dono preferir a regra literal, e uma linha em `findNegations`.**

**Bateria de aceite, rodada numa copia do `app/index.html` em Chromium headless, temas claro e escuro:
18 PASSA, 0 FALHA.** Inclui: recomposto e nao base (298, nao 164); atualizacao ao vivo (298 → 322); o
vermelho visto de verdade (ar-01 com todos os modulos ligados: 1.271); 18 tags em ambar e nenhum
vermelho no estado normal; os 9 casos-armadilha de negacao sem disparo; **todo botao copiar entregando
o mesmo texto de antes, byte a byte, em 27 botoes do album e 11 do demo**; export MD sem nenhum texto do
painel; nenhum `pageerror`.
