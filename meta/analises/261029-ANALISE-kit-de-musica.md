# ANALISE — Kit de música para os projetos do KCM (i-022, i-023, i-024)

> **Status:** Em discussão — espera as decisões 1 a 3 do dono (fim deste arquivo).
> **Data:** 2026-10-29 (data de criação; não muda depois)
> **Ideias de origem:** i-022 (skill que ensina o JSON), i-023 (skill com os macetes do Suno), i-024 (molde de
> skill de estilo próprio) e o feedback ao kit de 2026-10-28 («o nicho de música do KCM ainda não carrega o que
> este projeto aprendeu»). Pedido do dono em 2026-10-29: criar projetos de música para o Suno já «profissionais»
> e adaptados ao Cancioneiro.

## Problema

Os projetos de música que o dono monta com o KCM nascem sem o que este projeto aprendeu sobre o Suno. O custo
está medido no acervo dele: os guias antigos foram escritos por chats sem essas regras, e mesmo a família mais
regular, a «Rainha da Preguiça», chega ao Suno assim:

- **72 de 151 letras passam de 5.000 caracteres**, onde o Suno corta em silêncio; 141 passam de 3.000, onde ele
  começa a correr `[medido por instrumento: scripts/convert_br.py, 2026-10-29]`;
- **138 de 151 styles passam de 10 tags**, onde as últimas perdem efeito (mesma medida);
- **todos os oito formatos** de `Albuns/` e os dez volumes BR põem o rótulo dentro do bloco copiável ou fora de
  qualquer padrão (sonda `../261029-SONDA-albuns-antigos.md`).

Do outro lado, o que o projeto ensina funciona quando é dito: com o contrato do prompt-modelo, dois chats
entregaram 6 de 6 faixas no formato e no orçamento; sem ele, três chats inventaram três formatos de módulo
(spec `meta/specs/261028-prompt-modelo-e-modulos.md`, reteste de 2026-10-29). Conhecimento que não chega ao chat
que escreve a música não vale nada na hora de escrever.

## Restrições / o que foi medido

**O que este projeto sabe e um projeto de música precisaria saber** (cada item com a fonte que o sustenta):

| # | ensinamento | fonte |
|---|---|---|
| 1 | Dois campos: Style (mundo sonoro, sem colchetes) e Lyrics (estrutura e voz, com colchetes) | HISTORY §1 |
| 2 | Rótulo de referência nunca dentro do que vai para o Suno | DEC-005, regra de domínio |
| 3 | Style em cinco camadas audíveis, o mais característico nas primeiras ~20 a 30 palavras | HISTORY §4, §10; prompt-modelo |
| 4 | Orçamento: 6 a 8 tags no style, até 10 com módulos; acima disso as últimas perdem efeito | HISTORY §10, DEC-018 |
| 5 | Letra até ~3.000 caracteres; acima de 5.000 o Suno corta sem avisar | HISTORY §9, `QUALITY_LIMITS` |
| 6 | BPM é aproximação; um número por faixa (rampa «95 to 118 BPM» confunde o controle do app) | DEC-020 |
| 7 | Instrumental: `[Instrumental]` sozinho em loop; tags de arco só em faixa linear | HISTORY §2, §3 |
| 8 | Remover algo vai no Exclude, não em «no X»; o v6-mini gratuito não tem Exclude | HISTORY §5, §11 |
| 9 | A saída é o JSON canônico, em arquivo; módulos na coleção, faixa cita ids | DEC-016, DEC-021, DEC-023 |
| 10 | Um projeto por cena de uso: álbum coerente rende faixas parecidas; arquivo-mistura vira bagunça | proposta de grupos de 2026-10-29 |
| 11 | A interface do Suno muda: limites com fonte e data, e reconferir na conta | HISTORY §12 |

**O que existe pronto:** o prompt-modelo (`schema/PROMPT-PARA-CHATS.md`) já é o item 9 e boa parte do 3 e do 4,
testado; o HISTORY tem o resto, mas é longo e escrito para quem mantém o Cancioneiro, não para quem compõe.

**O que não sei:** o formato do nicho de música do KCM hoje — o que ele gera (Instruções? skills? arquivos de
contexto?) e onde. A pasta do KCM (`C:\Users\alexk\Arquiteturas\Contexto\contexto-modular`) não está ligada a
esta conversa `[não lido]`.

## Opções consideradas

**Decisão 1 — O que entregar.**
- **A (recomendada): um pacote de três peças**, cada uma com um papel:
  1. **Instruções-modelo de projeto de música** — o que um projeto do claude.ai carrega sempre: a regra de
     domínio, o orçamento (4, 5), o contrato de saída (9) e a cena do álbum (10), em uma página.
  2. **Skill «macetes do Suno»** (i-023) — os itens 1 a 8 e 11 em forma de consulta, com exemplos bons e ruins,
     lida quando o chat vai escrever ou revisar uma faixa. É o HISTORY reescrito para quem compõe.
  3. **Skill «revisar faixa»** — checklist que o chat roda antes de entregar: conta caracteres da letra e tags
     do style, procura rótulo no copiável, «no X», dois BPM. É o painel de qualidade do app, antes do app.
  O contrato JSON (i-022) não vira peça nova: as Instruções apontam para o prompt-modelo, que já é a fonte.
- B: só uma carta ao KCM com o resumo, e o KCM constrói. Barato, mas o conhecimento passa a viver em dois lugares
  e o KCM não tem as medidas para conferir.
- C: uma skill só, juntando tudo. Mais simples de instalar; mistura o que se lê sempre (orçamento, saída) com o
  que se consulta (macetes), e paga em contexto a cada conversa.
- **Fora agora:** i-024 (molde de skill por estilo próprio) — depende das três peças estarem em uso; reabre
  quando um projeto de álbum tiver estilo firmado.

**Decisão 2 — Onde mora a fonte.**
- **A (recomendada): neste repo**, numa pasta `kit-musica/`, e o KCM copia de lá. Aqui estão as medidas, o
  validador e o app que confere o resultado; uma regra que muda aqui (limite do Suno, contrato) muda no kit na
  mesma WO.
- B: no KCM. Fica junto dos outros nichos, mas cada mudança de regra do Suno precisa de duas WOs em dois repos.

**Decisão 3 — Como chego ao formato do KCM.**
- **A (recomendada): o dono libera a pasta do KCM nesta conversa** (um pedido de acesso, só leitura do nicho de
  música) e o chat adapta as três peças ao molde dele.
- B: o dono traz para a pasta-pai só o molde do nicho de música.
- C: o chat escreve no formato do Cancioneiro e o KCM adapta.

## Recomendação

**1A, 2A, 3A.** O que decide é a medida do problema: 72 letras cortadas e 138 styles diluídos vieram de chats
que não sabiam as regras, e as regras já estão escritas aqui. Três peças pequenas, cada uma lida no momento em que
serve, custam menos contexto que uma grande e chegam a quem escreve a música.

## Riscos

- **Peça que repete o HISTORY e envelhece separada.** Sinal: um limite muda no `QUALITY_LIMITS` e não muda no
  kit. Mitigação: o `validate.py` conferir os números do kit contra o app, como já confere a versão.
- **Skill grande demais para ser lida.** Sinal: passar de ~2 páginas. Mitigação: exemplo curto por regra, e o
  resto fica no HISTORY.
- **O formato do KCM mudar** depois de adaptado. Sinal: o KCM subir de versão no nicho de música.

## Ponto de decisão

Decisões **1, 2 e 3** (recomendadas **A, A, A**). Com elas: o chat escreve as três peças numa WO, testa a skill
«revisar faixa» contra o acervo da Rainha da Preguiça (deve achar as 72 e as 138) e um projeto-piloto de álbum
(um dos grupos da proposta de `Albuns/`) mede se as faixas novas já saem dentro do orçamento.
