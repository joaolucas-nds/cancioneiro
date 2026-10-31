# Kit de música — o que o Cancioneiro sabe sobre o Suno, para projetos de música

> **Fonte única aqui** (DEC-027): os números e as regras vêm do app, do `meta/HISTORY.md` e das decisões
> deste repo; o `scripts/validate.py` reprova se os limites da skill `revisar-faixa` divergirem do painel
> de qualidade do app. O KCM (Kit de Contexto Modular) copia daqui — não o contrário.

## Para que serve

Os projetos de música que o dono monta com o KCM nascem do nicho **Música**, feito para música tocada:
DAW, arranjo, mix e master. Quando a faixa é **gerada pelo Suno**, o artefato muda — o que se escreve é o
pedido (style e letra) — e entram regras que o nicho não traz: limites que cortam em silêncio, orçamento de
tags, rótulo fora do copiável, o JSON que o Cancioneiro lê. Medido nos guias antigos do dono, escritos sem
essas regras: 72 de 151 letras acima do limite, 138 de 151 styles com tags demais.

## As três peças

| Peça | O que é | Quando é lida |
|---|---|---|
| `BLOCO-SUNO.md` | Parte 1: cinco linhas para as Instruções do projeto (679 caracteres). Parte 2: seção para o CEREBRO do projeto | sempre (Parte 1); sob demanda (Parte 2) |
| `skills/macetes-suno/SKILL.md` | o que tem efeito no Suno e o que é mito, com exemplo bom e ruim | ao escrever ou reescrever style e letra |
| `skills/revisar-faixa/SKILL.md` | oito conferências por faixa, com script que conta (não estima) | antes de entregar faixa ou álbum |

O contrato do JSON não é peça nova: é o prompt-modelo (`schema/PROMPT-PARA-CHATS.md`, ou o botão «Prompt»
do app), que o projeto recebe junto.

## Como usar hoje, sem esperar o KCM

1. Crie o projeto de música pelo KCM, nicho Música.
2. Cole a Parte 1 do `BLOCO-SUNO.md` no fim das Instruções do projeto (meça: o KCM tem teto) e a Parte 2 no
   `meta/CEREBRO.md` dele.
3. Suba ao projeto as duas skills e o prompt-modelo.
4. Peça faixas; o chat entrega o `.json`; arraste para o Cancioneiro.

## Como o KCM pode absorver (mapa para o molde do nicho)

O nicho Música do KCM é um módulo (`src/niches/music.js`) com `behaviors`, `conventions`, `contextFiles`,
`skillsPack`, `promptsExtra` e `outputs`. Proposta de encaixe, sem mexer no que o nicho já faz para música
tocada:

| Peça do kit | Campo do nicho no KCM |
|---|---|
| eixo «música tocada × gerada por IA» | um seletor no `topbar` (hoje há «DAW / ferramenta»), que liga o resto |
| Parte 1 do bloco | `behaviors` (curto nas Instruções, inteiro no CEREBRO) e `conventions` |
| Parte 2 do bloco | seção do CEREBRO gerado |
| `macetes-suno`, `revisar-faixa` | `skillsPack.skills` (o formato dele: `name`, `gatilho`, `description`, `body`) |
| pedido de faixa no JSON | `promptsExtra` («Gerar faixa para o Suno») e `outputs` (o `.json`) |
| catálogo | `FAIXAS.md` segue com estado e o que falta; o JSON é o copiável |

O behavior `sound_honest` do nicho («não ouço áudio») continua valendo e ganha a forma do Suno: o dono gera,
ouve e relata.

## Manter em sincronia

- Limite do Suno mudou → muda o `QUALITY_LIMITS` do app, a skill `revisar-faixa` e o HISTORY na mesma WO; o
  `validate.py` acusa a skill que ficou para trás.
- Regra nova do prompt-modelo → conferir o `BLOCO-SUNO.md` e a `macetes-suno`.
- O que mudar aqui chega ao KCM por carta (correspondência entre projetos, CEREBRO).
