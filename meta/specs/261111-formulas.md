# SPEC — Fórmulas de referência (0.20.0)

> **Status:** Rascunho — espera os quatro pontos para o dono decidir.
> **Data:** 2026-11-11 (data de criação; não muda depois)
> **Ideia de origem:** o último ⬜ da Fase 3b («importar prompts prontos dos álbuns como módulos»). Opção D da análise `meta/analises/261111-ANALISE-prompts-prontos.md`, escolhida pelo dono em 2026-11-11 `[relatado pelo dono]`.
> **Protótipo:** fileira «0.20 · fórmulas» no canvas «Cancioneiro: nova interface» (`https://claude.ai/artifact/Sk1Xf5Rpr26WfGLbZJ2GAD`), computador e celular. Os textos de fórmula do protótipo são inventados.
> **Depende de:** 0.19.0 (`790aa3a`). Os testes entram em `tests/` (DEC-034).

---

## Problema

Os guias antigos trazem estilos completos já validados («referência rápida», «fórmulas validadas»), que servem de ponto de partida para faixas novas. Nada disso chegou ao app, e a forma prevista (módulo) não serve: um módulo é um trecho de 1 a 3 tags numa camada só, e uma fórmula tem de 5 a 14 tags (medido na análise). Hoje quem quer uma fórmula abre o `.md` e caça o bloco.

## O que construir

### 1. O esquema
- Campo opcional novo na coleção: `styleReferences[]`. Cada item tem `id` (minúsculas-com-hífens, único no acervo), `label` (nome curto), `style` (o copiável: só o que vai para o campo Style do Suno, sem colchetes e sem rótulo), `notes` (opcional: o «por que funciona», a dica de uso) e `source` (opcional: de onde veio, como «BR · índice-mestre»).
- Nenhum outro campo (`additionalProperties: false`). Faixas e módulos não mudam; nenhuma faixa cita fórmula.

### 2. Onde aparecem (ponto 1)
- **Computador (≥ 1280 px):** na lateral, acima de «Todas as faixas», a entrada «Fórmulas · N». Também no menu «⋯ Mais ações», em qualquer largura.
- **Celular:** «⋯ Mais ações» → «Fórmulas (N)».
- **Sem fórmulas no acervo, nada aparece** (o demo e os acervos de hoje continuam como estão).
- As duas entradas abrem a janela «Fórmulas»: no computador, uma janela de cerca de 720 px; no celular, em tela cheia. As fórmulas vêm agrupadas por `source`, na ordem do arquivo. Cada uma mostra:
  - o `label`;
  - a linha de qualidade da mesma função do cartão (`styleQuality`: contagem de tags, o BPM e o aviso de rampa) — uma fórmula acima do orçamento aparece em âmbar, como informação;
  - o `style`, num bloco monoespaçado;
  - as `notes`, recolhidas em «Por que funciona»;
  - o botão **Copiar Style**, que entrega só o `style`, byte a byte.

### 3. Curadoria (ponto 2)
- Cada fórmula tem «Excluir», com o «Desfazer» da I3. A exclusão conta como mudança a salvar.
- Editar e renomear pelo app ficam de fora: corrige-se no arquivo, ou importando de novo.

### 4. Importar
- A janela «Importar faixas» (I3) aceita um arquivo com `albums: []`, desde que ele tenha fórmulas. Quando a origem traz `styleReferences`, a janela ganha a seção «Fórmulas», com uma caixa por fórmula, todas marcadas.
- Mesma regra das faixas:
  - id igual e conteúdo idêntico: pula;
  - id igual e conteúdo diferente: entra com sufixo (`-2`);
  - o resto entra no fim da lista.
- Tudo conta como mudança a salvar, com «Desfazer», e o aviso final soma faixas e fórmulas.
- O destino (álbum) vale só para as faixas.

### 5. Salvar e exportar
- Salvar/Baixar `.json` leva as `styleReferences` (fazem parte da coleção).
- Exportar faixa ou álbum (`.json` ou `.md`) não leva.

### 6. O `validate.py`
- Ids únicos; `label` e `style` não vazios; `style` sem `[` nem `]`.
- Erro com o caminho (`styleReferences[3].style`).
- O esquema (`collection.schema.json`) ganha o campo.

### 7. As fórmulas do dono (ponto 3)
- O chat escreve `../acervos/formulas.json`, fora do repo: uma coleção com `albums: []` e as fórmulas.
- O chat confere, por script, que cada `style` é o bloco de código do guia com as quebras de linha trocadas por «, ». As exceções ficam listadas no próprio script:
  - Grand Anthem: o `[SILENCE - 4 beats] antes do drop final` é instrução de Lyrics e vai para `notes`.
- O dono importa no acervo aberto pela janela «Importar faixas» e salva. As da BR vão para `rainha-da-preguica.json`; as dos `Albuns/`, para `albuns-reagrupados.json`.

### O que não muda
- Módulos, faixas, controle de BPM, o prompt-modelo (ponto 4) e os conversores.

## Critérios de pronto (o chat mede no Chromium headless; viram `tests/test_formulas.py`)

| # | Critério |
|---|---|
| C1 | Acervo com 3 fórmulas: «Fórmulas · 3» na lateral, acima de «Todas as faixas», e «Fórmulas (3)» no «⋯». Acervo sem fórmulas: nenhum dos dois aparece. |
| C2 | A janela agrupa por `source`, na ordem do arquivo. «Copiar Style» entrega o `style` byte a byte, sem `label` nem `notes`. As `notes` ficam recolhidas. A linha de qualidade é a do cartão para aquele style. |
| C3 | A 390 px, a janela ocupa a tela, os alvos têm ≥ 44 px e a página não rola na horizontal. |
| C4 | Excluir uma fórmula: some, conta como mudança, «Desfazer» devolve na mesma posição. |
| C5 | Importar de um arquivo com `albums: []` e 3 fórmulas: a seção «Fórmulas» aparece. Uma idêntica pula; uma de mesmo id e conteúdo diferente entra como `-2`; uma nova entra. O aviso soma faixas e fórmulas. |
| C6 | Baixar `.json` leva as fórmulas; exportar a faixa e o álbum como `.json` não leva. |
| C7 | `validate.py`: id repetido, `style` vazio e `style` com colchete dão ERRO com o caminho. O acervo válido passa. O esquema aceita o campo e recusa campo a mais. |
| C8 | **Falso positivo:** o acervo demo e os de teste antigos abrem idênticos (sem entrada, sem seção na importação); os testes existentes passam. |
| C9 | `v0.20.0`; nenhum erro de página; os 50 testes passam; os novos reprovam na 0.19.0; a abertura com 205 faixas não piora. |

## Riscos

- **A lateral cresce.** São só uma linha e uma contagem, e só quando há fórmulas. O protótipo mostra o peso.
- **A janela com 18 a 21 fórmulas fica longa no celular:** agrupar por origem e recolher as notas reduz o tamanho; sem busca nesta entrega.
- **Uma fórmula é cópia de um guia de outra época do Suno:** a linha de qualidade mostra o que mudou nas regras (orçamento, BPM); `source` diz de onde veio.

## Fora de escopo

- Editar fórmula no app; criar fórmula a partir de uma faixa; ligar fórmula a faixa.
- A paleta de módulos (decompor fórmulas, tags repetidas do acervo) — vira ideia nova.
- Busca dentro da janela.

## Pontos para o dono decidir

1. **Onde as fórmulas aparecem.**
   - **(a) Uma janela «Fórmulas», aberta pela lateral e pelo «⋯» (recomendado):** funciona igual no computador e no celular, e não se mistura com filtros, busca, seleção e arrastar da lista.
   - (b) Uma vista no lugar da lista, como se fosse um álbum, com o detalhe ao lado: mais espaço, mas cada função da lista (filtro, busca, seleção, alça) precisa saber que ali não é faixa.
2. **O que se faz com elas no app.**
   - **(a) Ler, copiar, importar e excluir (recomendado).** Editar, no arquivo.
   - (b) Também renomear e editar o texto no app: mais tela, e o texto copiável passa a ser editado fora do chat.
   - (c) Só ler e copiar: errou na importação, só corrigindo o arquivo.
3. **Quais entram no `formulas.json`.**
   - **(a) 18 (recomendado):**
     - índice-mestre da BR: 6;
     - VOL1 da BR: 4;
     - VOL5 (os aprovados do VOL4): 4;
     - `album_guia_suno`: 4 listas de clima (romântica suave e intensa, épica heroica e sombria).
     - As 3 listas de voz (feminina, masculina, dueto) ficam de fora: são alternativas («soprano, mezzo-soprano»), não um estilo para colar, e vão para a ideia da paleta.
   - (b) As 21, com as de voz.
4. **O prompt-modelo.**
   - **(a) Não muda nesta entrega (recomendado):** os chats não precisam gerar fórmulas; o campo é opcional.
   - (b) Ensina o campo, para pedir fórmulas junto com o acervo — o prompt cresce de novo.
