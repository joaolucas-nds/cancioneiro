# ANALISE — Prompts prontos dos álbuns: módulos ou fórmulas?

> **Status:** Decidida — opção D, pelo dono em 2026-11-11; spec `meta/specs/261111-formulas.md`.
> **Data:** 2026-11-11 (data de criacao; nao muda depois)
> **Origem:** o último ⬜ da Fase 3b no ROADMAP, «Importar prompts prontos dos álbuns como módulos»; GLOSSARY, «prompt pronto». Ordem decidida pelo dono em 2026-11-09.

## Problema

Os guias antigos trazem estilos completos que já funcionaram — o índice-mestre da BR chama de «referência rápida», o VOL1 da BR de «fórmulas validadas», com o porquê de cada uma. Hoje nada disso chega ao app: ficaram nos `.md` da pasta-pai, que os conversores (i-008) não leram. Quem quer gerar uma faixa nova na persona da BR abre o `.md` e caça o bloco. O ROADMAP previa que eles virassem **módulos**; a leitura abaixo mostra que esse encaixe não serve.

## Restricoes / o que foi medido

Medido em 2026-11-11 no disco do dono, por script, só com contagens (nenhum dado foi copiado ao repo).

- **Os dois acervos reais têm 0 módulos** (`rainha-da-preguica.json`: 151 faixas; `albuns-reagrupados.json`: 205). Nos acervos reais o painel de módulos está vazio hoje.
- **Os styles das faixas já passam do orçamento:** de 10 a 14 tags na BR (mediana 12) e de 7 a 17 nos reagrupados (mediana 12), contra 6 a 8 no prompt-modelo (até 10 com os módulos ligados, DEC-021). Módulo só soma (a base manda): qualquer módulo ligado numa faixa real piora a contagem.
- **O contrato de módulo** é um trecho de 1 a 3 tags numa das sete camadas (DEC-021). Um prompt pronto tem de 5 a 14 tags e atravessa camadas (gênero, voz, instrumentos, BPM, produção).
- **As fórmulas descrevem pouco as faixas:** das seis do índice-mestre, a melhor cobre ≥ 50% das tags de 13 faixas da BR; 100 das 151 faixas não têm nenhuma fórmula a ≥ 25%. As faixas divergiram das fórmulas, então elas não servem para reconstruir os styles; servem como ponto de partida para faixas novas.
- **Quantas são**, por leitura dos títulos de seção:
  - índice-mestre da BR: 6 («Estilos Suno — referência rápida»);
  - BR VOL1: 4, com «por que funciona» («O que funciona — fórmulas validadas»);
  - VOL5: 4 («Estilos Suno originais», os aprovados do VOL4);
  - `album_guia_suno.md`: 7 listas de palavras por categoria (romântica suave, épica sombria, voz feminina…).
  - Total: cerca de 21. As «tabelas de referência rápida» dos outros volumes listam faixas, não estilos.
- **Na concorrência** (usesuno, builder): chips por categoria para montar o style, e uma biblioteca de estilos inteiros separada, para navegar e copiar.
- **DEC-028 (3):** depois da curadoria pela tela, o `.json` curado manda; nenhum script grava por cima de um acervo. O que entra no acervo entra pelo app, como mudança a salvar.

## Opcoes consideradas

**A. Cada prompt pronto vira um módulo (o texto do ROADMAP).** Descartada: fura o contrato de 1 a 3 tags e de camada única, e ligar 7 a 14 tags numa faixa de 12 leva a 20 ou mais, com o dedup cortando só o que repete palavra por palavra.

**B. Cada prompt pronto decomposto em módulos de 1 tag, por camada** (cerca de 21 fórmulas viram uma paleta de algumas dezenas de módulos no acervo). Fiel ao «como módulos», mas a fórmula se perde: ninguém consegue mais copiar «o estilo K-Pop Girl Crush» de uma vez, e classificar cada tag em camada pede julgamento tag a tag. Com faixas de 12 tags, a paleta quase só gera alerta de orçamento. Fica como ideia futura junto com a C.

**C. Paleta tirada do que o acervo já usa** (as tags que se repetem: 25 aparecem em 10 faixas ou mais na BR, 34 nos reagrupados). Útil para variar, mas não é o pedido — os prompts prontos são outra coisa. Registrar como ideia nova.

**D. Fórmulas como referência copiável inteira (recomendada).** Campo opcional novo na coleção, `styleReferences[]`, com `id`, `label`, `style` (o copiável, sem rótulo), `notes` (o «por que funciona», referência humana) e a origem. No app, uma entrada «Fórmulas» na lateral, acima dos álbuns, com cartões de copiar Style. As cerca de 21 entram num `../acervos/formulas.json` que o chat escreve à mão, lendo os guias — conversão por chat, como manda a DEC-001: quatro formatos diferentes para 21 blocos não pagam um parser —, e o app as importa no acervo aberto como mudança a salvar. Custo parecido com o da 0.18.0: esquema, app, `validate.py` e testes.

**E. As fórmulas como um álbum «Fórmulas» de faixas comuns, sem código.** Zero mudança no app, mas mistura conceitos: as fórmulas contam como faixas, ganham estado e «usei», e o esquema exige `lyrics`, que fórmula não tem. Descartada.

**F. Fechar o item sem fazer.** O ROADMAP marca o ⬜ como descartado, com esta medição. Honesto, mas deixa as fórmulas validadas presas nos `.md`, que é o que motivou o item.

## Recomendacao

**D.** É o que o GLOSSARY já define como prompt pronto: um style completo já validado, que se copia inteiro para começar uma faixa nova. Segue o padrão da concorrência (biblioteca de estilos ao lado dos chips) e preserva o «por que funciona» como referência, separado do copiável. Não mexe nos módulos nem nas faixas. O item do ROADMAP muda de texto («…como fórmulas de referência copiáveis») e fecha a 3b. A paleta (B + C) vira ideia com os números acima.

Ficam para a spec, com protótipo no canvas: o lugar exato na tela (lateral e celular), o formato do `formulas.json`, a checagem no `validate.py` (ids únicos, style sem colchetes, sem rótulo dentro do copiável) e se o prompt-modelo menciona o campo (recomendação: não, por ora; os chats não precisam gerá-lo).

## Riscos

- **As fórmulas envelhecem** (o Suno muda; DEC: interface muda, reconfirme). Mitigação: `notes` com a origem e a data do guia; o aviso de qualidade do app (contagem de tags, BPM) vale também para elas. Uma fórmula de 14 tags vai aparecer acima do orçamento — é informação, não erro.
- **Um painel a mais na lateral**, que já tem álbuns e organizar. Sinal cedo: no roteiro de tela, o dono não acha as fórmulas ou elas atrapalham a lista. O protótipo mede isso antes do código.
- **Escrever 21 fórmulas à mão** pode errar uma vírgula. Mitigação: o chat confere, por script, que cada `style` é igual, byte a byte, ao bloco de código do guia (normalizando só as quebras de linha em «, »).

## Ponto de decisao

**O que um prompt pronto vira no Cancioneiro?** D (fórmula de referência copiável inteira, com `styleReferences` e a entrada «Fórmulas» na lateral) — recomendado; B (decompor em módulos de 1 tag); F (fechar o item sem fazer).
