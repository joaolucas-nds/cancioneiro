# SPEC — Organizar (frente de interface, entrega I3)

> **Status:** Pronta — aplicação pela `meta/workorders/261106-wo0027-organizar.md` (0.16.0, DEC-032)
> **Decidida em:** a frente, em 2026-11-05 (DEC-030: SortableJS 1.15.7 embutido, sem o interruptor «editar», com
> «Desfazer»). Esta é a I3.
> **Data:** 2026-11-06 (data de criação; não muda depois)
> **Ideia de origem:** i-048 (edição e organização com UX de verdade, arrastando onde for útil).
> **Protótipo:** telas «I3 · computador» e «I3 · celular» no canvas «Cancioneiro: nova interface»
> (`https://claude.ai/artifact/Sk1Xf5Rpr26WfGLbZJ2GAD`). As duas são navegáveis: marque caixas, abra o «⋯» de uma
> linha, use Subir, Descer, Excluir e «Desfazer». No celular, use o «⋯» do detalhe e «Selecionar várias…». O arrastar
> em si está na tela «Proposta · arrastando», da análise.
> **Depende de:** 0.15.0 (`36596e2`).

---

## Problema

Desde a 0.13.0 dá para organizar o acervo, mas atrás do interruptor «editar», com ↑ ↓, «mover…» e «excluir» no pé
de cada cartão: uma faixa por vez, um passo por clique. O dono achou isso pouco prático e pediu para arrastar onde
for útil (i-048). A I3 deixa a organização **sempre à mão**: pela alça, pelo «⋯» de cada faixa ou por várias de uma
vez. Um «Desfazer» segura o erro, no lugar do interruptor.

## O que construir

### 1. Sem o interruptor «editar»

- **Sai o «editar» da barra, e o «Ligar editar» do «⋯» do celular.** Organizar não é mais um modo.
- **«Importar faixas…» vai para o «⋯» da barra,** no computador e no celular.
- **O pé do cartão perde ↑ ↓, «mover…» e «excluir».** Na visão Cartões, ganha um botão «⋯», que abre o mesmo menu da
  linha (item 3). No detalhe, o «⋯» fica no alto, ao lado de ‹ ›.
- **Só se organiza um acervo com cópia guardada,** como hoje, porque é na cópia que o rascunho mora. O acervo
  carregado pelo Pages (o exemplo) não tem: nele, a alça não aparece, e as operações de rascunho do «⋯» ficam
  desligadas, com a linha «Para organizar, importe o .json: a cópia guardada é o rascunho.».

### 2. Arrastar pela alça (visão Lista)

- **Cada linha começa com uma alça ⋮⋮** (um botão: «Arrastar <título>»). Arrastar pela alça leva a faixa para outro
  lugar no álbum ou para outro álbum, com uma linha que mostra onde ela vai cair. Arrastar pelo resto da linha não
  pega a faixa, para não atrapalhar a seleção de texto e os botões.
- **Biblioteca:** SortableJS 1.15.7 (MIT), o `Sortable.min.js` do pacote npm sem mudança, embutido num `<script>`
  próprio, antes do código do app. Ele tem 45.478 bytes, e o sha256 é
  `bf4241bc73fef7f11c59a283a69fe8051cdd31c6d8ff5a2b9ba219e7831fcf76` (pacote baixado do npm em 2026-11-06; a 1.15.7,
  de 2026-02-11, é a mais recente). A licença MIT inteira vai num comentário logo acima. O app passa de 158 KB para
  cerca de 204 KB. O `validate.py` passa a conferir esse hash: trocar de versão vira decisão, não acidente.
- **Com filtro ou busca ligados** (ponto 1 para o dono), a faixa solta cai, na ordem completa do álbum, **logo antes
  da próxima faixa visível**; no fim do álbum, logo depois da última visível. As faixas escondidas não mudam de ordem
  entre si.
- **Soltar no mesmo lugar não conta.** Nem alteração, nem aviso.
- **`Esc` durante o arrastar cancela,** e a faixa volta.
- **No celular, a alça só pega depois de segurar um quarto de segundo,** para a rolagem não virar arrastar.

### 3. O «⋯» de cada faixa (o caminho sem arrastar)

O WCAG 2.5.7 pede um caminho de um clique, sem arrastar, para tudo o que se faz arrastando. É este:

- **Onde fica:** no fim de cada linha, no alto do detalhe e no pé do cartão em Cartões. É o mesmo menu nos três.
- **Itens:**
  - **Mover para…**: a janela de hoje, com «novo álbum…»;
  - **Subir** e **Descer**, desligados nas pontas do álbum;
  - **Exportar .md** e **Exportar .json**, iguais aos de hoje;
  - **Excluir…**, que continua pedindo confirmação.
- **Teclado:** com o foco no título da linha, `Alt+↑` e `Alt+↓` sobem e descem a faixa. Como hoje, Subir e Descer
  andam na ordem completa do álbum, mesmo com filtro ligado.
- **No celular, o menu é uma folha que sobe do pé da tela,** com botões de 52 px, e traz também «Selecionar
  várias…» (item 4).

### 4. Várias de uma vez

- **No computador, uma caixa de seleção em cada linha,** depois da alça.
  - `Shift`+clique marca o intervalo.
  - A caixa no cabeçalho do álbum marca as faixas visíveis dele, e fica meio marcada quando só algumas estão.
- **Com uma ou mais marcadas, uma barra escura aparece no pé da tela:** «N faixas selecionadas», com estas ações:
  - **Mover para…**: as N vão juntas, na ordem em que estavam;
  - **Exportar .json**: um acervo com as N, nos álbuns de origem, com os módulos que elas citam, como o exportar de
    uma faixa;
  - **Marcar usei**, que vira «Desmarcar usei» quando todas já estão marcadas;
  - **Excluir…**, com confirmação;
  - **×**, que tira a seleção, como o `Esc`.
- **Quando a seleção some:**
  - um filtro ou uma busca que esconde uma faixa marcada tira ela da seleção;
  - trocar de acervo ou ir para Cartões limpa tudo.
- **No celular, as caixas só aparecem em modo de seleção** (ponto 3 para o dono):
  - entra-se por «Selecionar várias…» no «⋯» do detalhe;
  - a lista volta com a faixa marcada, e as caixas de 44 px tomam o lugar da alça;
  - tocar na linha marca ou desmarca;
  - a barra de lote fica no pé, e o × sai do modo.

### 5. A lateral durante o arrastar

- **Cada álbum da lateral vira alvo:** soltar sobre ele leva a faixa para o fim daquele álbum. Ele se acende enquanto
  a faixa está em cima.
- **«+ Novo álbum (solte aqui)» aparece no fim da lista de álbuns só enquanto se arrasta.** Soltar nele pede o título e
  cria o álbum com a faixa. Fora do arrastar, ele não aparece: um álbum sem faixa não fica no acervo (a regra da
  0.13.0).

### 6. «Desfazer»

- **Toda operação de rascunho deixa «Desfazer» no aviso:**
  - arrastar;
  - Mover, Subir e Descer;
  - Excluir;
  - as operações de lote;
  - importar faixas.

  `Ctrl+Z` (`⌘Z` no Mac) faz o mesmo, fora de um campo de texto. Dentro de um campo, ele desfaz o texto, como sempre.
- **Volta o acervo inteiro ao que era antes da operação:** a ordem, os álbuns, as faixas excluídas com as marcas «usei»
  delas, os módulos ligados e o BPM da sessão delas, e o número de alterações do rascunho. O aviso diz «Desfeito: …».
- **Uma volta só,** a da última operação. Trocar de acervo, importar outro e «Salvar .json» esquecem a volta.
- **Marcar «usei» não é operação de rascunho** (fica nas marcas do navegador) e não entra no «Desfazer»: desmarcar já
  desfaz.

### 7. Soltar um `.json` sobre um álbum

- **Arrastar um arquivo do computador sobre o cabeçalho de um álbum** (na Lista) **ou sobre um álbum da lateral**
  acende o alvo. Soltar abre «importar faixas» com aquele álbum já escolhido como destino.
- **Soltar em qualquer outro lugar** importa como acervo, como hoje.
- Sem cópia guardada, soltar sobre o álbum também importa como acervo, com um aviso.

### 8. Larguras

A linha ganha três colunas (alça, caixa e «⋯»). As colunas cedem antes do título, nesta ordem: Idioma, BPM, Estado e,
por último, o texto da saúde (a marca ●▲■ fica). O título nunca fica com menos de 160 px, nas mesmas larguras da I2.

### O que não muda

- O cartão, salvo o pé (item 1).
- A Lista, os Cartões, o detalhe, a lateral, os filtros e o rascunho com «Salvar .json» (DEC-028).
- O que se copia e o que se exporta.
- Os dados do acervo. No navegador, nada novo em `cancioneiro:ui`.

## O que muda para quem usa (a conta tem de fechar)

| Gesto de hoje (0.15.0) | Na I3 |
|---|---|
| Ligar «editar» para organizar | nada a ligar: a alça e o «⋯» estão sempre ali |
| ↑ ↓ no pé do cartão | arrastar pela alça; Subir e Descer no «⋯»; `Alt+↑` e `Alt+↓` |
| «mover…» no pé do cartão | arrastar para outro álbum, na lista ou na lateral; «Mover para…» no «⋯» |
| «excluir» no pé do cartão | «Excluir…» no «⋯», com confirmação e «Desfazer» |
| «importar faixas…» na barra, com «editar» ligado | no «⋯» da barra; ou soltar o `.json` sobre um álbum |
| Uma faixa por vez | várias, pelas caixas e pela barra de lote |
| Errou, refaz à mão | «Desfazer» ou `Ctrl+Z`, até a próxima operação |

## Critérios de pronto (o chat mede no Chromium headless, `file://`, antes da WO)

| # | Critério |
|---|---|
| C1 | Sem interruptor: a barra não tem «editar»; com cópia guardada, o «⋯» da barra tem «Importar faixas…»; o «⋯» do celular não tem «Ligar editar». O pé do cartão não tem ↑ ↓, «mover…» nem «excluir», e em Cartões tem o «⋯». |
| C2 | Arrastar pela alça para baixo de outra faixa do mesmo álbum muda a ordem no rascunho (+1 alteração, aviso com «Desfazer»); para outro álbum, a faixa cai na posição solta. **Falso positivo:** soltar no mesmo lugar não muda a ordem, o número de alterações nem mostra aviso. |
| C3 | Com um filtro ligado, a faixa solta cai logo antes da próxima visível, na ordem completa; as escondidas mantêm a ordem entre si. |
| C4 | Soltar sobre um álbum da lateral leva a faixa ao fim dele. «+ Novo álbum» só existe durante o arrastar; soltar nele pede o título e cria o álbum com a faixa. |
| C5 | O «⋯» da linha, do detalhe e do cartão tem os mesmos itens; Subir e Descer ficam desligados nas pontas; «Mover para…» abre a janela; «Excluir…» pede confirmação; os dois Exportar saem iguais aos de hoje. `Alt+↑` e `Alt+↓` no título sobem e descem. |
| C6 | Seleção: a caixa marca; `Shift`+clique marca o intervalo; a caixa do álbum marca as visíveis e fica meio marcada com parte; a barra diz «N faixas selecionadas»; × e `Esc` limpam; um filtro que esconde uma marcada tira ela da seleção. |
| C7 | Lote: «Mover para…» leva as N juntas, na ordem; «Exportar .json» sai um acervo com as N, nos álbuns de origem e com os módulos citados, que passa no `validate.py` e importa de volta; «Marcar usei» marca todas e vira «Desmarcar usei»; «Excluir…» confirma e tira as N. |
| C8 | Depois de cada operação de rascunho, «Desfazer» e `Ctrl+Z` voltam o acervo, as marcas «usei» das excluídas e o número de alterações; só a última; «Salvar .json» e trocar de acervo esquecem a volta. **Falso positivo:** `Ctrl+Z` dentro da busca não mexe no acervo. |
| C9 | Sem cópia guardada: não há alça; o «⋯» traz os Exportar, e as operações de rascunho desligadas, com a explicação; o lote só exporta e marca usei. |
| C10 | Soltar um `.json` sobre o cabeçalho de um álbum, ou sobre ele na lateral, abre «importar faixas» com ele escolhido; soltar fora importa como acervo. |
| C11 | No celular (390×844): a alça só pega depois de segurar; o «⋯» do detalhe abre a folha com os itens e «Selecionar várias…»; ela volta à lista com caixas de 44 px e a barra de lote; tocar na linha marca; × sai. |
| C12 | A 1366, 1024 e 800 px, com o detalhe aberto: sem rolagem lateral e o título com pelo menos 160 px. A barra de lote não cobre o rascunho nem o aviso. |
| C13 | O `<script>` da biblioteca é o `Sortable.min.js` 1.15.7 sem mudança (o sha256 acima), com a licença MIT logo acima; o `validate.py` confere o hash e reprova se ele mudar. |
| C14 | Abrir o app com um acervo de 205 faixas fica, no máximo, 100 ms mais lento que a 0.15.0 (média de 5, `file://`); a Lista de 300 faixas, com as alças, desenha em no máximo 200 ms. |
| C15 | O cabeçalho diz `v0.16.0`; nenhum erro de página; os testes das entregas 1 a 3, da I1 e da I2 continuam passando (os que ligavam «editar» passam a usar o «⋯»). |

**Prova de vida:** o mesmo teste no app da 0.15.0 reprova (no mínimo C1, C2 e C8).

## Resultado (medido pelo chat em 2026-11-06, Chromium headless, `file://`, app de chegada da WO 0027)

**15 de 15 critérios.** Acervo de teste: as três faixas do `data/demo.json` e faixas feitas a partir delas, em três
álbuns, 15 faixas (no álbum C, metade «gerada», para os filtros); outro igual para trocar de acervo; e dois grandes, de
205 e 300 faixas, para o C14.

| # | O que foi conferido | Resultado |
|---|---|---|
| C1 | a barra e o «⋯» do celular sem «editar»; «Importar faixas…» no «⋯» da barra; o pé do cartão com «marcar usei», os dois Exportar e o «⋯», sem ↑ ↓, «mover…» nem «excluir» | OK |
| C2 | arrastar a primeira faixa do álbum A pela alça para baixo da terceira muda a ordem (+1, aviso com «Desfazer»); outra, para o álbum B, cai onde soltou; soltar no mesmo lugar não muda a ordem, a contagem nem mostra aviso | OK |
| C3 | com Estado «gerada», a faixa solta cai logo antes da próxima visível na ordem completa; as «ideia» escondidas mantêm a ordem entre si | OK |
| C4 | soltar no álbum B da lateral leva a faixa ao fim dele; «+ Novo álbum» só fica visível durante o arrastar; soltar nele pede o título e cria o álbum com a faixa | OK |
| C5 | o «⋯» da linha, do detalhe e do cartão têm os mesmos itens; Subir desligado na primeira e Descer na última; «Mover para…» abre a janela; «Excluir…» confirma; os dois Exportar saem iguais aos do cartão; `Alt+↑` e `Alt+↓` no título | OK |
| C6 | a caixa marca; `Shift`+clique marca o intervalo; a caixa do álbum marca as visíveis e fica meio marcada com parte; «N faixas selecionadas»; × e `Esc` limpam; um filtro que esconde uma marcada a tira da seleção | OK |
| C7 | «Mover para…» leva duas faixas juntas, na ordem, ao fim do álbum B; com duas de álbuns diferentes, «Exportar .json» sai um acervo com os dois álbuns de origem e só os módulos citados, que passa no esquema e importa de volta; «Marcar usei» marca as duas e vira «Desmarcar usei»; «Excluir…» confirma e tira as duas | OK |
| C8 | excluir uma faixa marcada «usei» e clicar «Desfazer» volta a faixa, a marca e a contagem; depois de dois Descer, `Ctrl+Z` volta só o último; «Salvar .json» e trocar de acervo esquecem a volta; `Ctrl+Z` na busca não mexe no acervo | OK |
| C9 | sem cópia guardada (o caso do exemplo do Pages): sem alça; o «⋯» só com os Exportar e a explicação; o lote com Mover e Excluir desligados | OK |
| C10 | soltar um `.json` sobre o cabeçalho do álbum B, ou sobre ele na lateral, abre «importar faixas» com o B escolhido; fora deles, importa como acervo | OK |
| C11 | a 390×844: as listas arrastáveis pegam só pela alça e, no toque, depois de segurar 250 ms (`delay`, `delayOnTouchOnly`); o «⋯» do detalhe abre a folha de baixo com «Selecionar várias…»; caixas de 44 px e a barra de lote; tocar na linha marca; × sai | OK |
| C12 | a 1366, 1024 e 800 px, com o detalhe aberto: sem rolagem lateral, título com pelo menos 160 px; a barra de lote acima do rascunho e o aviso acima dela | OK |
| C13 | o `<script id="lib-sortable">` traz a licença MIT e, da linha marcada até o fim, os 45.478 bytes do `Sortable.min.js` 1.15.7 (sha256 `bf4241bc…`); o `validate.py` diz `OK  biblioteca` e reprova uma cópia com «1.15.7» trocado por «1.15.8» dentro da biblioteca | OK |
| C14 | abrir com 205 faixas, média de 5, em três rodadas: 148, 152 e 159 ms, contra 134, 151 e 127 ms da 0.15.0 nas mesmas rodadas (no pior caso, +32 ms; o limite era +100); a Lista de 300 faixas com alças desenha em cerca de 60 ms | OK |
| C15 | `v0.16.0`; nenhum erro de página | OK |

**Prova de vida, medida:** no app da 0.15.0 o C1 reprova e o teste para no C2, porque não há alça para arrastar.

**Regressão:** os testes das entregas 1 a 3, da I1 e da I2 seguem em 15 de 15, 25 de 25, 19 de 19, 14 de 14 e 15 de 15.
Os que ligavam «editar» passam pelo «⋯» (da linha, do cartão ou do detalhe); os que comparam o `<main>` dos Cartões com
uma versão anterior tiram antes o «⋯» do pé, que é a única diferença. `validate.py` exit=0 com `jsonschema`, e os dois
conversores OK.

**Onde a implementação saiu da spec:**
- **O app ficou com 239 KB**, não os cerca de 204 previstos: 45 KB da biblioteca e 35 KB do código e do CSS da I3
  (seleção, menu, lote, «Desfazer», o arrastar para a lateral e para arquivos).
- **A SortableJS engole o primeiro clique depois de soltar** (no modo de arrastar que o app usa, o mesmo no mouse e no
  toque). Sem correção, o «mover» da janela do «+ Novo álbum» não respondia ao primeiro clique. O app dispara um clique
  sintético ao fim de cada arrastar; está comentado em `dragEnd`.
- **Tocar ou clicar na alça abre o «⋯»** da faixa. No celular, onde a linha não tem o «⋯», é por ela (e pelo detalhe)
  que se chega ao menu.
- **No celular, o detalhe continua aberto depois de Subir ou Descer**, na mesma faixa; o «←» volta à lista com a nova
  ordem.
- **«Mover para…» em lote pula as faixas que já estão no álbum de destino**, e diz «Nada a mover» se forem todas.
- **Quando o acervo ganha a cópia guardada**, o app só põe as alças nas linhas, sem redesenhar a lista: o redesenho
  dobrado custava cerca de 100 ms ao abrir 205 faixas.
- **A barra de lote empurra o fim da lista**, para não cobrir as últimas linhas; no celular, a contagem e o × ficam numa
  linha e as quatro ações na outra.

**O que a revisão visual pegou:** a barra de lote cobria as duas últimas linhas da lista, e no celular o × caía sozinho
numa terceira linha da barra e os rótulos quebravam em dois.

## Fora de escopo

- **A I4:** salvar direto no arquivo (i-043).
- **Organizar os álbuns:** renomear, reordenar arrastando na lateral, juntar dois. Vira ideia nova.
- **Arrastar uma faixa para outro acervo** da lateral, que a i-048 também cita. Mexe em dois rascunhos de uma vez e
  pede uma análise própria: vira ideia nova.
- **Mais de uma volta no «Desfazer», e o «Refazer».**
- **Arrastar na visão Cartões** (ponto 2): lá, o «⋯».

## Riscos

- **Código de terceiro dentro do app.** São 45 KB de biblioteca; o hash fica no `validate.py`. Sinal: o app abrir mais
  devagar no `file://`, e o C14 mede.
- **Arrastar com filtro ligado pode surpreender:** a faixa cai perto da vizinha visível, mas pode haver escondidas
  entre as duas. Mitigação: a regra é uma só e está no aviso («… foi para antes de «X»»), e o «Desfazer» volta.
- **Sem o interruptor, o clique errado fica mais fácil.** O «Desfazer» segura isso, e excluir ainda confirma. O C2
  mede o falso positivo: soltar no mesmo lugar não conta.
- **O redesenho a cada operação** recria as listas arrastáveis (uma por álbum). Com 300 faixas, o C14 mede.
- **O teclado:** `Alt+↑` e `Alt+↓` podem ser atalhos do sistema em algum ambiente; o «⋯» continua como caminho.
- **O celular:** segurar para arrastar compete com o gesto de rolar. Por isso o caminho principal lá é o «⋯» e a
  seleção, e a alça é extra.

## Pontos para o dono decidir

**Decididos pelo dono em 2026-11-06, os três como recomendados** (DEC-032): arrastar com filtro pela regra da
próxima visível, Cartões só com o «⋯», no celular a seleção entra pelo «⋯».

1. **Arrastar com filtro ou busca ligados:** **permitir, com a regra do item 2 (recomendado):** a faixa cai antes da
   próxima visível, e o «Desfazer» cobre a surpresa. Ou desligar a alça enquanto houver filtro, deixando só o «⋯»
   (mais previsível, menos à mão).
2. **Na visão Cartões, só o «⋯», sem arrastar (recomendado):** arrastar cartões de 700 px numa grade é impreciso, e a
   Lista é onde se organiza. Ou arrastar também a grade.
3. **No celular, a seleção entra por «Selecionar várias…» no «⋯» (recomendado):** fica claro e não compete com o
   segurar da alça. Ou segurar a linha para começar a selecionar, como nos apps de e-mail (mais rápido, mas o mesmo
   gesto da alça, a poucos milímetros).
