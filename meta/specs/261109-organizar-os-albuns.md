# SPEC — Organizar os álbuns (0.18.0)

> **Status:** Pronta — aplicação pela `meta/workorders/261109-wo0034-organizar-os-albuns.md` (0.18.0, DEC-035)
> **Data:** 2026-11-09 (data de criação; não muda depois)
> **Ideia de origem:** i-049 (renomear um álbum, reordenar os álbuns arrastando na lateral e juntar dois).
> **Ordem decidida pelo dono em 2026-11-09:** i-049 → i-042 (rampa de BPM) → importar prompts prontos como módulos,
> que fecha a Fase 3b `[relatado pelo dono]`.
> **Protótipo:** telas «0.18 · computador» e «0.18 · celular» no canvas «Cancioneiro: nova interface»
> (`https://claude.ai/artifact/Sk1Xf5Rpr26WfGLbZJ2GAD`). A do computador é navegável: abra o «⋯» de um álbum (na
> lateral ou no cabeçalho), Renomear, Subir/Descer, Juntar com…, Excluir álbum… e «Desfazer»; a alça ⋮⋮ da lateral,
> no protótipo, desce o álbum (no app, arrasta).
> **Depende de:** 0.17.0 (`dc99fb0`). Os testes entram em `tests/` e rodam no CI (DEC-034).

---

## Problema

A I3 deixou as **faixas** fáceis de organizar; os **álbuns** não. Um álbum só nasce (pelo «+ Novo álbum» ou pelo
«Mover para… › novo álbum») e só some quando esvazia. Não dá para corrigir o nome dado na pressa, pôr os álbuns
numa ordem que faça sentido nem juntar dois que eram o mesmo. Hoje, cada uma dessas coisas é editar o `.json` à
mão — com o risco de quebrar o arquivo — ou mover as faixas uma a uma.

## O que construir

### 1. O «⋯» do álbum

- **Onde fica** (ponto 1): no cabeçalho de cada álbum, na Lista e nos Cartões, e ao lado de cada álbum da lateral,
  a partir de 1280 px. O botão «exportar álbum .md» do cabeçalho entra nele.
- **Itens:**
  - **Renomear…** (item 2);
  - **Subir álbum** e **Descer álbum**, desligados nas pontas;
  - **Juntar com…** (item 4), desligado quando o acervo tem um álbum só;
  - **Exportar álbum .md** (o de hoje) e **Exportar álbum .json** (um acervo com o álbum e os módulos que as faixas
    dele citam, como o exportar de uma faixa; importa como qualquer acervo);
  - **Excluir álbum…** (item 5).
- **Teclado:** com o foco no nome do álbum na lateral, `Alt+↑` e `Alt+↓` sobem e descem o álbum, como as faixas.
- **No celular:** o «⋯» do cabeçalho abre a folha de baixo, com botões de 52 px, como o da faixa.
- **Sem cópia guardada** (o exemplo do Pages): só os dois Exportar, com a mesma explicação do «⋯» da faixa.

### 2. Renomear

- **Uma janela com o título e a descrição** (ponto 2). A descrição é o campo `description` do esquema, que já
  existe e hoje não se edita pela tela; ela aparece em cinza no cabeçalho do álbum, depois da contagem.
- **O id do álbum não muda** (ponto 3): o filtro, as exportações e os ids das faixas continuam valendo.
- Título vazio não renomeia (o botão fica desligado). Título igual a outro álbum é permitido, com um aviso na janela
  («Já existe um álbum com este nome»), porque o id continua distinto.
- Conta uma alteração e deixa «Desfazer».

### 3. Reordenar

- **Arrastar pela alça ⋮⋮ de cada álbum da lateral** (ponto 4), com a SortableJS que já está embutida, num grupo
  separado do das faixas: álbum não cai dentro de álbum, e faixa arrastada continua caindo sobre o álbum como hoje.
- **Subir e Descer no «⋯»**, para quem não arrasta (WCAG 2.5.7) e no celular, onde não há lateral.
- A Lista e os Cartões seguem a ordem nova. Soltar no mesmo lugar não conta.

### 4. Juntar

- **«Juntar com…»** abre a lista dos outros álbuns. As faixas do álbum de origem vão **para o fim do destino**, na
  ordem em que estavam; o álbum de origem sai. Ficam o nome, a descrição e o id do destino (ponto 5).
- O aviso diz quantas faixas foram: «“X” juntou-se a “Y” (N faixas)», com «Desfazer».
- Se o filtro de álbum apontava para o de origem, ele passa para o destino.

### 5. Excluir álbum

- **«Excluir álbum…»** confirma contando as faixas: «Sai o álbum com as N faixas dele, do rascunho». O botão da
  confirmação diz «Excluir álbum e N faixas». A janela lembra que «Juntar com…» guarda as faixas.
- Saem também as marcas «usei» das faixas excluídas; «Desfazer» volta tudo, como o excluir de faixas da I3.
- Se o filtro de álbum apontava para ele, volta para «Todas as faixas».

### 6. «Desfazer»

Renomear, reordenar, juntar e excluir álbum são operações de rascunho como as da I3: uma alteração cada, aviso com
«Desfazer» e `Ctrl+Z`, só a última, e a volta continua depois de salvar (DEC-033).

### O que não muda

- O esquema: `id`, `title`, `description` e `songs` já existem; nada novo no `.json`.
- A regra da 0.13.0: álbum sem faixa não fica no acervo (por isso não há «Novo álbum» vazio).
- O cartão, o detalhe, o arrastar de faixas, o salvar no arquivo.

## O que muda para quem usa (a conta tem de fechar)

| Hoje (0.17.0) | Na 0.18.0 |
|---|---|
| Nome errado: editar o `.json` à mão | «⋯» › Renomear…, com «Desfazer» |
| Ordem dos álbuns: a do arquivo | arrastar na lateral; Subir/Descer no «⋯» |
| Juntar dois: mover as faixas e esperar o álbum esvaziar | «⋯» › Juntar com…, uma operação |
| Apagar um álbum: excluir cada faixa | «⋯» › Excluir álbum…, com confirmação e «Desfazer» |
| Descrição do álbum: só no `.json` | na janela de renomear e no cabeçalho |
| «exportar álbum .md» solto no cabeçalho | no «⋯» do álbum, junto do novo .json |

## Critérios de pronto (o chat mede no Chromium headless; viram testes em `tests/test_albuns.py`)

| # | Critério |
|---|---|
| C1 | O «⋯» do álbum existe no cabeçalho (Lista e Cartões) e na lateral (≥ 1280 px), com os mesmos itens; Subir desligado no primeiro, Descer no último; «Juntar com…» desligado com um álbum só. Sem cópia guardada: só os Exportar. |
| C2 | Renomear muda o título e a descrição no rascunho (+1 alteração), na lateral, no cabeçalho e no filtro; o id não muda; título vazio não renomeia; «Desfazer» volta. |
| C3 | Subir e Descer mudam a ordem de `albums` (+1); a Lista segue. `Alt+↑`/`Alt+↓` no nome da lateral fazem o mesmo. |
| C4 | Arrastar um álbum pela alça da lateral muda a ordem (+1). **Falso positivo:** soltar no mesmo lugar não conta. Arrastar uma faixa sobre um álbum da lateral continua levando a faixa ao fim dele (regressão da I3). |
| C5 | Juntar A com B: as faixas de A no fim de B, na ordem; A sai; B guarda id, título e descrição; +1 alteração; o filtro que apontava para A aponta para B; «Desfazer» volta os dois álbuns. |
| C6 | Excluir álbum confirma com a contagem; tira o álbum, as faixas e as marcas «usei» delas; +1; filtro em «Todas»; «Desfazer» volta álbum, faixas e marcas. **Falso positivo:** cancelar não muda nada. |
| C7 | Exportar álbum .json sai um acervo com o álbum e só os módulos citados, que passa no `validate.py` e importa de volta. |
| C8 | Celular (390×844): o «⋯» do cabeçalho abre a folha com os itens; Subir/Descer funcionam. |
| C9 | Depois de salvar no arquivo, o `.json` gravado tem a ordem, os nomes e as junções novas (o teste da ida e volta cobre). |
| C10 | `v0.18.0`; nenhum erro de página; os 32 testes de `tests/` continuam passando no CI; abrir 205 faixas fica no máximo 30 ms mais lento que a 0.17.0 nas mesmas rodadas. |

**Prova de vida:** os testes novos reprovam no app da 0.17.0 (no mínimo C1, C2 e C5).

## Resultado (medido pelo chat em 2026-11-09, Chromium headless, app de chegada da WO 0034)

**10 de 10 critérios**, em 12 testes novos (`tests/test_albuns.py`), num acervo sintético de 4 álbuns de 3 faixas.

| # | O que foi conferido | Resultado |
|---|---|---|
| C1 | o «⋯» no cabeçalho e na lateral com os mesmos 7 itens; Subir desligado no primeiro, Descer no último; sem cópia guardada, só os Exportar, a nota, e nenhuma alça na lateral | OK |
| C2 | renomear muda título e descrição (+1), na lateral e no cabeçalho; o id fica; título vazio desliga o botão; nome repetido avisa; sem mudança não conta; «Desfazer» volta | OK |
| C3 | Descer pelo «⋯» e `Alt+↑` no nome da lateral mudam a ordem de `albums` e a Lista segue | OK |
| C4 | arrastar o álbum pela alça da lateral muda a ordem (+1); soltar no mesmo lugar não conta; arrastar uma faixa sobre um álbum da lateral continua levando-a ao fim dele | OK |
| C5 | juntar: as faixas no fim do destino, na ordem; a origem sai; o destino guarda id e título; o filtro passa para o destino; «Desfazer» volta os dois | OK |
| C6 | excluir: a confirmação diz «3 faixas»; cancelar não muda nada; confirmar tira o álbum e a marca «usei»; «Desfazer» volta álbum e marca | OK |
| C7 | exportar o álbum em `.json`: `al-02.json`, só o álbum, só os módulos citados; importa de volta | OK |
| C8 | a 390×844, o «⋯» do cabeçalho abre a folha (com «Cancelar») e Descer funciona | OK |
| C9 | a ordem e os nomes novos vão para o arquivo: coberto pela ida e volta (`tests/test_roundtrip.py`) e pelo salvar da I4 | OK |
| C10 | `v0.18.0`, sem erro de página; os 44 testes passam; abrir 205 faixas: 289, 246 e 261 ms, contra 319, 274 e 251 ms da 0.17.0 nas mesmas rodadas (sem diferença medível; o limite era +30) | OK |

**Prova de vida:** os testes novos reprovam no app da 0.17.0 (não há o «⋯» do álbum).

**Onde a implementação saiu da spec:**
- **No menu do computador, Subir e Descer álbum ficam um por linha** (com o atalho ao lado); lado a lado, quebravam. No celular, ficam lado a lado, como os da faixa.
- **A lateral ganha as alças quando a cópia guardada fica pronta,** sem redesenhar a lista: é a mesma armadilha da I3 (`App.saved` chega depois do primeiro desenho).
- **Testes que montam o acervo sem cópia guardada esperam o exemplo carregar sozinho** (em `http://` o app busca o `data/demo.json`); sem isso, ele chegava depois e cobria o acervo do teste. Valeu também para o teste equivalente da I3.

## Riscos

- **Excluir álbum é a operação mais destrutiva do app até aqui** (dezenas de faixas num clique). Seguram: a
  confirmação com a contagem no botão, o «Desfazer», a cópia guardada e, no arquivo, o aviso de mudança da I4. Se o
  dono preferir, o ponto 5 tira essa operação (sobra juntar ou mover faixas).
- **Dois arrastares na lateral:** a lateral já é alvo das faixas (I3). O grupo separado da SortableJS e a alça só no
  álbum evitam a confusão; o C4 mede a regressão.
- **A SortableJS engole o primeiro clique depois de soltar** (armadilha da I3): o clique sintético do `dragEnd`
  precisa valer também para a lista de álbuns.
- **Nome repetido:** permitido, porque o id distingue; o aviso na janela evita o engano.

## Fora de escopo

- **Arrastar uma faixa para outro acervo** (i-050): pede análise própria.
- **Criar álbum vazio:** contraria a regra da 0.13.0; o álbum nasce com uma faixa, como hoje.
- **Separar um álbum em dois:** é «Mover para… › novo álbum» com as faixas marcadas, que já existe.
- **Mudar o id do álbum pela tela.**

## Pontos para o dono decidir

**Decididos pelo dono em 2026-11-09, os cinco como recomendados** (DEC-035).

1. **Onde mora o «⋯» do álbum.**
   - **(a) No cabeçalho do álbum e na lateral (recomendado):** a lateral só aparece a partir de 1280 px; o cabeçalho
     está em toda largura, inclusive no celular.
   - (b) Só na lateral: menos botões na Lista, mas some no notebook estreito e no celular.
2. **Como renomear.**
   - **(a) Numa janela, com título e descrição (recomendado):** cabe a descrição, que hoje não se edita, e o
     «Desfazer» é um só.
   - (b) Clique duplo no título, editando no lugar: mais rápido, mas a descrição fica de fora e o clique duplo
     compete com o clique que filtra o álbum na lateral.
3. **O id do álbum ao renomear.**
   - **(a) Não muda (recomendado):** filtros, exportações e o histórico do arquivo continuam valendo.
   - (b) Muda junto com o título: o id «fala» o nome novo, mas qualquer referência ao antigo quebra.
4. **Como reordenar.**
   - **(a) Arrastar pela alça na lateral, mais Subir/Descer no «⋯» (recomendado).**
   - (b) Só Subir/Descer: sem risco de confundir com o arrastar de faixas, mas lento com 12 álbuns.
5. **Juntar e excluir.**
   - **(a) Juntar leva as faixas para o fim do destino e fica o nome do destino; Excluir álbum existe, com
     confirmação e «Desfazer» (recomendado).**
   - (b) Juntar perguntando qual nome fica e onde entram as faixas: mais controle, mais uma pergunta por junção.
   - (c) Sem «Excluir álbum»: para tirar um álbum, junta-se a outro ou excluem-se as faixas pela seleção.
