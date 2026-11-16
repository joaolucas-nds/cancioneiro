# SPEC — Começar vazio, esquecer todos e a importação por grupo (0.21.0)

> **Status:** Implementada pelo chat num clone em 2026-11-16 (WO 0043). Falta conferir na tela.
> **Data:** 2026-11-16 (data de criação; não muda depois)
> **Ideias de origem:** i-053, i-058, i-059 e o texto da janela de importar; lote escolhido pelo dono em 2026-11-15
> e 2026-11-16 `[relatado pelo dono]`. Decisão: DEC-039.

## O que construir

1. **Abrir vazio** (i-058): sem acervo guardado, a tela vazia também no `https://`; o `data/demo.json` não é
   buscado sozinho. A tela vazia aponta «⋯» → «Baixar exemplo». O `data/exemplo-cinzeiro.json` sai do repo.
2. **Esquecer todos** (i-059): no seletor de acervo, «Esquecer todos os acervos…», visível com dois ou mais
   guardados. Confirma com a contagem de acervos e de alterações não salvas; apaga as cópias do navegador e volta
   à tela vazia. As marcas «usei» ficam.
3. **Caixa do grupo** (i-053): na janela de importar, cada álbum (faixas) e cada origem (fórmulas) tem uma caixa
   que marca ou desmarca o grupo; meio marcada quando só parte está marcada. As fórmulas vêm agrupadas por origem.
4. **O texto da janela:** «Faixa idêntica a uma…» só com faixas, «Fórmula idêntica a uma…» só com fórmulas,
   «Faixa ou fórmula idêntica a uma…» com as duas.

## Critérios de pronto (`tests/test_vazio_e_importar.py`)

| # | Critério |
|---|---|
| C1 | Em `http://`, sem acervo guardado: `App.collection` nulo, a tela vazia visível e nenhum pedido a `demo.json`. |
| C2 | Dois acervos, um com alteração: a confirmação diz «os 2 acervos guardados» e «1 alteração não salva se perde»; depois, nenhum registro no IndexedDB, a tela vazia, as marcas «usei» intactas, e recarregar continua vazio. **Falso positivo:** com um acervo só, o item não aparece; cancelar não apaga nada. |
| C3 | Desmarcar o álbum desmarca as faixas dele; desmarcar uma faixa deixa o grupo meio marcado; só o marcado entra. |
| C4 | Fórmulas agrupadas por origem, na ordem do arquivo; desmarcar a origem tira as dela; o texto certo nos três casos. |

Mais: a suíte inteira passa (61 antes, 67 depois); os testes novos reprovam na 0.20.0.
