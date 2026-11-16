# SPEC — Importar vários `.json` de uma vez, e onde soltar decide o que vira (i-057)

> **Status:** Rascunho — aguarda o dono nos quatro pontos do fim. Implementação depois deles (0.22.0).
> **Data:** 2026-11-16 (data de criação; não muda depois)
> **Ideia de origem:** i-057 `[relatado pelo dono, 2026-11-15]`; frente escolhida pelo dono em 2026-11-16.
> **Depende de:** 0.21.0 (`822b70d`).

---

## Problema

Hoje o app lê **um** arquivo por vez. Soltar três `.json` importa só o primeiro, sem avisar dos outros. E o
que o arquivo vira depende de onde ele cai:
- solto na página: vira acervo (substitui o aberto na tela e fica guardado);
- solto sobre um álbum (cabeçalho na Lista ou item da lateral): abre «Importar faixas» para aquele álbum.

O dono quer:
- soltar vários de uma vez e escolher, por arquivo, entre **acervo novo** e **faixas no acervo aberto**;
- soltar na **lateral** para importar direto, rápido, como acervo separado («Acervos neste navegador»).

## Como está hoje (lido no código da 0.21.0)

- `document` `drop`: lê `e.dataTransfer.files[0]` e ignora o resto. Sobre um álbum (`fileDropAlbum`), com cópia
  guardada, vai para `readTracksFile(f, album)`; senão, `importFromFile(f, handle)`, que guarda no IndexedDB pelo
  nome do arquivo, abre o acervo e, no Chrome e no Edge, vincula o arquivo para o «Salvar» (DEC-033).
- `#file-input` e `#tracks-input` sem `multiple`.
- «Importar faixas» trabalha com uma origem: o destino (`__keep`, um álbum, `__new`), as caixas por álbum e por
  origem (0.21.0) e um «Desfazer» para a importação inteira.
- Mesmo nome de acervo já guardado com alterações pendentes: `importFromFile` pede confirmação antes de substituir.

## O que construir

### 1. Um arquivo: nada muda
Soltar ou escolher **um** arquivo segue exatamente como hoje, nos três lugares (página, álbum, botões).

### 2. Vários arquivos fora da lateral: a janela «Importar N arquivos»
Uma linha por arquivo, na ordem em que vieram:
- o nome;
- o que ele tem («2 álbuns · 14 faixas · 3 fórmulas», ou «não é um acervo do Cancioneiro», e então a linha
  vem desligada);
- uma escolha: **Acervo novo** · **Faixas no acervo aberto** · **Pular**.

Embaixo, valendo para as faixas de todos os arquivos, o **Destino** de hoje (manter os álbuns de origem, um
álbum, novo álbum). O destino aparece só quando alguma linha está em «Faixas».

Ao confirmar:
- **Acervo novo:** cada arquivo vira um acervo guardado, como no `importFromFile`, mas sem trocar o que está
  aberto (ponto 3). Mesmo nome já guardado com alterações → a linha avisa antes («substitui o guardado; N
  alterações se perdem»), e a confirmação final repete.
- **Faixas:** todos os arquivos marcados entram no aberto **numa operação só**, pela regra de hoje (idêntica
  pula, mesmo id com conteúdo diferente ganha `-2`, fórmulas também), com **um «Desfazer»** e um aviso que soma
  tudo («3 arquivos: 12 faixas e 2 fórmulas importadas · 1 já estava»).
- Sem acervo aberto (ou sem cópia guardada), «Faixas» vem desligada e tudo é acervo novo.

### 3. Soltar na lateral: acervo novo, direto
Soltar um ou vários arquivos na **lateral**, fora de um álbum, guarda cada um como acervo novo, **sem janela**.
O aviso conta («3 acervos guardados: …»), e o seletor de acervo passa a listá-los. Mesmo nome com alterações
pendentes: aí a confirmação aparece, só para esse arquivo. Soltar **sobre um álbum** da lateral continua sendo
«faixas neste álbum» (com vários arquivos, abre a janela do item 2 com «Faixas» e o álbum já escolhidos).

### 4. O aviso durante o arraste
A faixa «Solte o .json para importar» passa a dizer onde cada zona leva: sobre a lateral, «Solte aqui: cada
arquivo vira um acervo guardado»; sobre um álbum, «Solte aqui: as faixas vão para este álbum»; no resto, «Solte
para importar» (um arquivo) ou «Solte para escolher o que cada um vira» (vários).

### 5. Os botões
`#file-input` e `#tracks-input` ganham `multiple`: escolher vários pelo botão abre a mesma janela do item 2,
com a escolha padrão do botão («Importar .json…» → acervo novo; «Importar faixas…» → faixas).

## Critérios de pronto (viram `tests/test_varios_json.py`)

| # | Critério |
|---|---|
| V1 | **Falso positivo:** um arquivo solto na página, num álbum ou escolhido pelos botões faz exatamente o que faz na 0.21.0 (os testes de hoje passam sem mudança). |
| V2 | Três arquivos soltos na página: a janela lista os três, na ordem, com o que cada um tem; um arquivo inválido vem desligado e não trava os outros. |
| V3 | Dois em «Acervo novo» e um em «Faixas»: os dois ficam guardados (IndexedDB) sem trocar o aberto; o terceiro entra no aberto; um «Desfazer» devolve o aberto como estava; o aviso soma. |
| V4 | Faixas de dois arquivos com o mesmo id e conteúdo diferente: a segunda entra com `-2`; idêntica pula. |
| V5 | Soltar dois na lateral (fora de álbum): dois acervos guardados, sem janela, o aberto não muda; com o mesmo nome de um guardado com alterações, a confirmação aparece só para ele. |
| V6 | Sem acervo aberto: «Faixas» desligada; tudo vira acervo novo. |
| V7 | A 390 px (sem lateral): a janela ocupa a tela, alvos ≥ 44 px, sem rolagem horizontal. |
| V8 | A suíte inteira passa; os novos reprovam na 0.21.0; nenhum erro de página. |

## Riscos

- **Vínculo do «Salvar» (DEC-033):** soltar vários traz um `FileSystemHandle` por arquivo só durante o `drop`;
  é preciso pegá-los todos ali, antes da janela. Sem eles, os acervos novos ficam sem vínculo (o primeiro
  «Salvar» pede o arquivo), como hoje no Firefox.
- **A janela cresce:** dez arquivos cabem numa lista com rolagem; sem busca.
- **Lateral só a partir de 1280 px:** abaixo disso a zona do item 3 não existe; a janela do item 2 cobre.

## Fora de escopo

- Juntar dois acervos inteiros num só (já se faz por «Faixas»).
- Pastas e `.zip`.
- Arrastar faixa de um acervo para outro (i-050, depois do recesso).

## Pontos para o dono decidir

1. **O padrão de cada linha na janela.**
   - **(a) Pela forma do arquivo (recomendado):** uma faixa exportada (1 álbum, 1 faixa, o formato do
     «Exportar faixa») vem em «Faixas»; o resto vem em «Acervo novo». Sem acervo aberto, tudo «Acervo novo».
   - (b) Tudo em «Acervo novo»; o dono troca o que quiser.
   - (c) Tudo em «Faixas no acervo aberto».
2. **Depois de guardar vários como acervo novo, qual fica aberto?**
   - **(a) O que estava aberto continua (recomendado);** os novos aparecem no seletor. Sem nenhum aberto, abre o
     primeiro da lista.
   - (b) Abre o último importado, como acontece hoje com um arquivo.
3. **A lateral como zona de «acervo novo direto».**
   - **(a) Sim, como o dono descreveu (recomendado),** com o aviso do item 4 deixando claro onde se está.
   - (b) Não: só a janela; a lateral continua sendo só «faixas neste álbum».
4. **Um arquivo solto na lateral (fora de álbum).**
   - **(a) Também vira acervo novo direto, sem trocar o aberto (recomendado):** a zona faz sempre a mesma coisa.
   - (b) Um arquivo continua como hoje (vira acervo e abre); só vários vão direto.
