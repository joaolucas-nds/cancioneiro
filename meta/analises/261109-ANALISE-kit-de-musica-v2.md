# ANÁLISE — Kit de música v2: o que levar ao nicho Música do KCM depois da 0.17.0

> **Status:** Decidida — pelo dono em 2026-11-09, como recomendada: A, C (com o «Depois de ouvir») e B, D em duas
> levas; a leva 1 depois da i-051; a carta 02 ao KCM depois da leva 2. F e G ficam como ideia.
> **Data:** 2026-11-09 (data de criação; não muda depois)
> **Origem:** pedido do dono em 2026-11-09: «começar a montar aquelas recomendações, skills e qualquer outra ideia
> para o refinamento» do nicho de música do KCM `[relatado pelo dono]`. Continua a i-039 e a análise
> `meta/analises/261029-ANALISE-kit-de-musica.md` (implementada na 0.10.0, DEC-027).
> **Depende de:** nada no app. Não muda o esquema.

---

## Problema

O kit de música (`kit-musica/`, 0.10.0) leva ao KCM três peças: o bloco para Instruções e CEREBRO, a skill
`macetes-suno` (o que tem efeito no Suno) e a skill `revisar-faixa` (conferir antes de entregar). Ele cobre bem
o **pedido** (style, orçamento, limites, rótulo fora do copiável). Faltam três coisas que um projeto de música
gerada por IA faz toda semana e que o kit não ensina:

1. **Escrever a letra para ser cantada pelo Suno.** É o defeito mais medido do acervo: 72 de 151 letras acima de
   5.000 caracteres nos guias antigos. O kit diz o limite, mas não ensina a escrever dentro dele: refrão escrito
   uma vez, sílabas paralelas entre versos, pronúncia em pt-BR, números por extenso.
2. **Conceber um álbum, não só faixas soltas.** A conversão de `Albuns/` mostrou que álbum por cena de uso
   funciona melhor (i-038), e os módulos compartilhados são o que dá unidade sonora (DEC-016). Nada disso está
   no kit.
3. **Iterar depois de ouvir.** O assistente não ouve; o dono gera e relata. O kit diz isso, mas não diz o que
   fazer com o relato: mudar uma variável por vez (i-013), quando criar variante ou módulo, e quando a
   ferramenta certa é do próprio Suno (editar um trecho, Persona, Cover) e não um pedido novo.

Além disso, o kit descreve o Cancioneiro da 0.10.0: não sabe que hoje se importam faixas sobre um álbum, que o
acervo se organiza arrastando e que «Salvar» grava no arquivo (0.13.0 a 0.17.0).

## Restrições / o que foi medido

- **O KCM ainda não respondeu à carta 01** (aviso de lido de 2026-10-31: a resposta vem pela carta 02, sem data).
  A pasta do KCM não está vinculada a esta conversa: **não li** se a i-N25 deles andou. O gatilho da i-039
  continua: sem resposta até o primeiro projeto de música novo, o kit se usa à mão.
- **O teto das Instruções** (~6.900 caracteres) não muda: peça nova vai como skill ou como CEREBRO, nunca como
  linha nova nas Instruções. A Parte 1 do bloco (679 caracteres) fica como está.
- **Fonte única aqui** (DEC-027): números vêm do app e do HISTORY; o `validate.py` prende os limites da
  `revisar-faixa` aos do app. Skill nova que cite número entra na mesma regra.
- **Pesquisa (2026-11-09):**
  - **Metatags no V6 são pista, não comando.** Um guia revisado para o V6 em 2026-09-13 diz isso com todas as
    letras e recomenda descrever a decisão musical da seção (papel, emoção, instrumentação, entrega vocal) em
    vez de confiar numa gramática de colchetes; e mudar uma variável por vez (Jack Righteous). Convergente com o
    HISTORY §3 e a `macetes-suno` §6. **Confiança: convergente, não oficial.**
  - **Recursos do Suno hoje** (página oficial de produtos, lida em 2026-11-09): Voices (a própria voz),
    Stem Splitter (até 12 stems), Covers (outro gênero, mesma melodia), Mashups (duas faixas), Samples,
    **Personas** (vocal, estilo e clima salvos num perfil reutilizável) e Studio 2.0 (estação no navegador).
    A página não traz limites de campo nem nome de modelo. **Nada disso está no kit.**
  - **Uma skill pública de composição para IA** (Nous Research, «songwriting-and-ai-music») cobre estrutura,
    rima, métrica, prosódia, truques fonéticos (números por extenso, siglas espaçadas, testar nome próprio num
    trecho curto) e o fluxo com 3 a 5 gerações por resultado bom. Ela põe a letra em ~3.000 caracteres (40 a 60
    linhas), o mesmo âmbar do app. **Serve de checagem, não de fonte:** é inglês e não fala de pt-BR.
- **Refutação procurada:** o risco real é inflar o kit. Três skills que o projeto de música não aciona são peso
  morto, e cada uma tem de ser mantida quando o Suno muda. Por isso a recomendação abaixo corta para duas skills
  novas e põe as outras ideias como seção da `macetes-suno` ou como ideia com gatilho.

## Opções consideradas (peças candidatas)

| # | Peça | O que resolve | Custo | Recomendo |
|---|---|---|---|---|
| A | **Atualizar o kit para a 0.17.0** (README «Como usar hoje»: importar faixas sobre um álbum, salvar no arquivo) | o kit descreve um app de agosto | 1 turno curto | **sim, já** |
| B | **Skill nova `escrever-letra-suno`** | o defeito nº 1 (letra longa) e a pronúncia em pt-BR | médio; precisa de um teste com o dono gerando 2 ou 3 faixas | **sim** |
| C | **`macetes-suno` §10 — recursos do Suno em 2026** (Persona, Cover, editar trecho, Extend, Stem Splitter, Voices), cada um com «quando usar em vez de pedir de novo» | iteração sem reescrever; o kit parado em 2026-10 | baixo, mas envelhece rápido: entra com data e fonte | **sim** |
| D | **Skill nova `conceber-album`**: álbum por cena de uso, lane comum como módulo compartilhado, Persona para a voz, arco de energia e BPM entre faixas, ids estáveis | a unidade do álbum, que hoje depende do chat lembrar | médio | **sim** |
| E | Skill nova `iterar-faixa` (A/B de uma variável, i-013) | o que fazer com o relato do dono | médio | **não como skill:** cabe em 10 linhas na `macetes-suno` («Depois de ouvir») e na Parte 2 do bloco, que já tem o ciclo |
| F | Campo no esquema para o relato de geração (data, versão do Suno, o que se ouviu) | o relato some na conversa | alto: muda o contrato dos chats e o app | **não agora:** ideia com gatilho — se o dono relatar o mesmo ajuste três vezes sem registro |
| G | Variante do kit para outra plataforma (Udio etc., i-032) | — | alto, sem uso hoje | não: fica na i-032 |

## Recomendação

**Kit v2 = A + B + C + D, em duas levas, e uma carta 02 ao KCM no fim.**

- **Leva 1 (barata, sem depender do dono gerar nada):** A, C e o «Depois de ouvir» (E, como seção). Uma WO só
  de documento em `kit-musica/`.
- **Leva 2 (precisa de prova de campo):** B e D. Cada skill é escrita, e o dono a usa num projeto de música real
  (ou num chat novo) pedindo 2 ou 3 faixas; o `revisar-faixa` mede o resultado contra os guias antigos (letra
  acima de 3.000, tags acima de 10). Sem essa prova, a skill não entra no kit: skill não testada é opinião.
- **Carta 02 ao KCM** depois da leva 2, com o mapa atualizado (as duas skills novas em `skillsPack.skills`, a §10
  como `conventions` datada).

**Rascunho do conteúdo das skills novas** (o texto final sai na leva 2):

- `escrever-letra-suno` — *USE ao escrever ou reescrever a letra de uma faixa para o Suno.*
  1. Orçamento antes de escrever: letra até ~3.000 caracteres; refrão completo uma ou duas vezes, depois só a
     tag (`[Chorus]`). Conta com código, não de cabeça (reusa o script da `revisar-faixa`).
  2. Seções com papel: cada tag diz a função e, se ajudar, uma pista curta (`[Verse 2: mais contido]`); a pista
     descreve o que se ouve, não um comando.
  3. Versos paralelos com o mesmo número de sílabas poéticas e a tônica no mesmo lugar (contagem em pt-BR:
     sílaba poética, até a última tônica).
  4. Pronúncia: números e siglas por extenso; palavra estrangeira e nome próprio testados num trecho curto
     antes da faixa inteira; nada de acento gráfico «criativo».
  5. Instrumental e arco: remete à `macetes-suno` §6.
  6. Exemplo ruim e bom, em pt-BR, tirado do acervo de teste (`data/demo.json`), nunca de letra do dono.
- `conceber-album` — *USE ao começar um álbum ou ao reagrupar faixas soltas.*
  1. Uma cena de uso por álbum (onde e para que se ouve), não um gênero.
  2. Uma lane comum: o gênero e a produção viram módulo da coleção, ligado em todas as faixas; o style de cada
     faixa diz só o que muda.
  3. A voz: uma Persona do Suno, se o plano tiver; senão, a mesma frase de voz em todas as faixas.
  4. O arco do álbum: ordem por energia e BPM, sem dois vizinhos iguais; uma faixa de abertura e uma de fecho.
  5. Ids estáveis (`<sigla>-01`…) e títulos de referência fora do copiável.

## Riscos

- **O kit envelhecer mais rápido que o app.** A §10 depende da página de produtos do Suno; entra com a data de
  leitura e a frase «se o dono disser que não existe na conta dele, acredite».
- **Duplicar o KCM.** Se a carta 02 deles chegar com um nicho diferente do proposto, as peças viram material de
  entrada para a análise deles, não um formato a impor.
- **Letra é gosto.** A skill de letra ensina orçamento e cantabilidade, nunca estilo poético; o critério de pronto
  é medido (tamanho, sílabas paralelas), não «ficou bonita».
- **Letras do dono fora de tudo:** exemplos só com dado sintético (o acervo do dono não entra no repo público).

## Ponto de decisão

1. **Quais peças:** recomendo **A, C (com o «Depois de ouvir») e B, D em duas levas**; F e G ficam como ideia.
2. **Quando:** recomendo a leva 1 **depois da i-051** (é uma WO curta de documento), e a leva 2 quando você tiver
   um projeto de música para testar as skills.
3. **Carta 02 ao KCM:** só depois da leva 2 (recomendado), ou já agora avisando que o kit v2 está em curso.
