# SPEC — Lista e detalhe (frente de interface, entrega I2)

> **Status:** Pronta — aplicação pela `meta/workorders/261106-wo0026-lista-e-detalhe.md` (0.15.0, DEC-031)
> **Decidida em:** a frente, em 2026-11-05 (DEC-030: B, SortableJS embutido, sem o interruptor «editar», I1 → I2 → I3 → I4). Esta é a I2.
> **Data:** 2026-11-06 (data de criação; não muda depois)
> **Ideias de origem:** i-046 (as visões) e i-047 (a lateral).
> **Protótipo:** telas «I2 · computador» e «I2 · celular» no canvas «Cancioneiro: nova interface»
> (`https://claude.ai/artifact/Sk1Xf5Rpr26WfGLbZJ2GAD`). As duas são navegáveis: clique numa faixa, num álbum da
> lateral, em Lista/Cartões, em «Style» e no ✓; no celular, toque no título e use «←».
> **Depende de:** 0.14.0 (`0158c88`).

---

## Problema

Na 0.14.0, o topo já cabe numa linha, mas o miolo ainda é a grade de cartões: três por tela (medido na 0.13.0, com
«editar» ligado). Para achar uma faixa num acervo de 150 é preciso rolar dezenas de telas, e para copiar um Style é preciso achar o
cartão. A I2 põe as faixas numa **lista** de uma linha cada, com o **cartão de hoje ao lado** da faixa escolhida. Ela não
muda como se edita (a I3 muda) nem o que o cartão mostra.

## O que construir

### 1. A visão (Lista ou Cartões)

- **Na barra, depois de Filtros,** um par de botões **Lista | Cartões** (`role="group"`, cada um com `aria-pressed`). No
  celular, os dois vão para o «⋯», como itens de escolha única.
- **A escolha fica no navegador** (`view` em `cancioneiro:ui`: `"list"` ou `"cards"`). **Sem escolha guardada, abre em
  Lista** (ponto 1 para o dono).
- **Cartões é a 0.14.0 como está:** a mesma grade e os mesmos cartões, sem o detalhe. A lateral (item 4) aparece nas duas
  visões.

### 2. A lista

- **Agrupada por álbum, na ordem do acervo,** só com as faixas que passam nos filtros. O cabeçalho de cada álbum (título,
  contagem e «exportar álbum .md») **fica fixo logo abaixo do topo** enquanto se rola dentro dele.
- **Uma linha por faixa, de 44 px** no computador, com estas colunas:

| Coluna | O que mostra | Clique |
|---|---|---|
| Título | o título, cortado com «…» se não couber | **abre o detalhe** (ponto 3 para o dono) |
| Estado | a etiqueta de estado | — |
| Idioma | o idioma | — |
| BPM | o BPM em vigor (o do controle, se mudado; DEC-020) | — |
| Saúde | o resumo do painel de qualidade (abaixo) | — |
| **Style** | botão | copia o Style **recomposto**, igual ao «copiar» do cartão |
| **Lyrics** | botão | copia a Lyrics |
| ✓ | «usei», com `aria-pressed` | marca e desmarca, como «marcar usei» |

- **Regra de domínio:** os dois botões copiam **só o conteúdo**. O rótulo («Style», «Lyrics», o título da faixa) fica no
  botão e no `aria-label` («Copiar o Style de Brasas Eternas»), nunca no texto copiado. O Style é calculado **na hora do
  clique**, com os módulos ligados e o BPM da sessão (FIX-007), para que a linha e o cartão copiem a mesma coisa.
- **Saúde:** o pior nível entre as medidas que o painel de qualidade do cartão mostra (mesmos limites, `QUALITY_LIMITS`),
  com marca e texto, nunca só cor:
  - ■ vermelho, quando algo passa do limite: «Lyrics passa de 5.000»;
  - ▲ âmbar, quando algo está perto ou pede atenção: «Style perto de 1.000», «Style 12 tags», «"no drums" no Exclude»;
  - ● verde, «tudo dentro». O nível neutro do painel (9 e 10 tags) conta como dentro.
- **A linha usada fica esmaecida,** como o cartão usado.
- **Colunas que somem antes do título:** quando a lista fica estreita (detalhe aberto, janela menor), some o Idioma e
  depois o BPM, para o título nunca ficar com menos de 160 px.
- **Teclado:** `Tab` passa pelos botões da linha. Com o foco num título, `↓` e `↑` vão ao título da próxima e da anterior,
  atravessando álbuns; com o detalhe aberto, ele acompanha. `Enter` abre o detalhe.

### 3. O detalhe (à direita)

- **Abre ao clicar no título.** Mostra **o cartão de hoje, sem mudança**, com a mesma estrutura configurável (DEC-023): o
  painel de qualidade, os módulos, o BPM, a Lyrics, as variantes, as notas e o rodapé. Com «editar» ligado, o rodapé traz
  ↑ ↓, mover e excluir, como hoje. Clicar no título do cartão continua copiando o título.
- **No alto do detalhe:** «álbum · N de M», com ‹ e › para a faixa anterior e a seguinte da lista filtrada (atravessando
  álbuns), e × para fechar.
- **A linha aberta fica marcada** (`aria-current="true"`, fundo do cartão).
- **`Esc` fecha** o detalhe, quando nenhum popover está aberto (o popover fecha primeiro), e o foco volta ao título da
  linha.
- **O detalhe tem rolagem própria,** fixo ao lado da lista, da altura da tela abaixo do topo.
- **O que muda no detalhe chega à linha:** ligar um módulo ou mudar o BPM no cartão atualiza o BPM e a saúde da linha
  dela, sem redesenhar a lista (a rolagem não muda).
- **O endereço guarda a faixa:** abrir põe `#faixa=<id>` no endereço, e trocar com ‹ › só substitui. Recarregar com o
  endereço reabre a mesma faixa. O «Voltar» do navegador fecha o detalhe. Um id que não existe no acervo é ignorado, sem
  erro, e o endereço fica limpo.
- **Curadoria:** mover a faixa aberta (pelo ↑ ↓ ou pelo «mover…» do cartão) mantém o detalhe nela, e a linha muda de
  lugar. Excluir fecha o detalhe e leva o foco à linha seguinte. As linhas não ganham controles de edição: isso é a I3.

### 4. A lateral (à esquerda, de 1280 px de largura para cima)

- **Álbuns:** «Todas as faixas» e cada álbum, com a contagem de faixas que passam nos **outros** filtros (estado, uso,
  busca); um álbum com 0 aparece apagado. Clicar põe o filtro de álbum, que é o mesmo do painel Filtros, com a etiqueta
  dele; «Todas as faixas» tira. O escolhido fica marcado (`aria-current`).
- **Acervos neste navegador:** os guardados, como no seletor de acervo, com o aberto marcado; clicar abre outro.
  Esquecer continua no seletor.
- **Fixa ao lado da lista,** com rolagem própria. Abaixo de 1280 px, ela não aparece: o mesmo conteúdo está no painel
  Filtros e no seletor de acervo.

### 5. As larguras

| Largura | Como fica |
|---|---|
| ≥ 1280 px | lateral (232 px) + lista + detalhe (entre 400 e 520 px, 34% da largura) |
| 960 a 1279 px | lista + detalhe, sem a lateral |
| 720 a 959 px | lista; o detalhe abre **por cima** dela, à direita (até 480 px, com sombra) |
| < 720 px | lista e detalhe em **telas próprias** (item 6) |

Em nenhuma largura há rolagem horizontal da página.

### 6. Celular (abaixo de 720 px)

- **A linha tem pelo menos 64 px,** em duas linhas de texto: o título e, embaixo, «estado · idioma · BPM · saúde». O ✓ de
  «usei» tem 44 px. Os botões Style e Lyrics saem da linha (não cabem com 44 px): copiar fica no detalhe, a um toque.
- **Tocar no título abre o detalhe em tela cheia:**
  - no alto, «←» (voltar à lista), «álbum · N de M», ‹ e ›;
  - o cartão de hoje;
  - no pé, fixos: **Copiar Style** (o principal), **Copiar Lyrics** e **Título**, que copiam o mesmo que os botões do
    computador.
- **Voltar** (o «←» ou o do celular) devolve à lista na mesma posição de rolagem.
- **Sem lateral nem gaveta** (ponto 2 para o dono): o álbum se escolhe em Filtros, e o acervo, no seletor.
- **O rascunho** continua no pé, como na 0.14.0; com o detalhe aberto, ele sobe para cima dos botões de copiar.

### 7. Primeira abertura

Um aviso de uma linha, como o da 0.14.0: «Nova visão em lista: clique numa faixa para ver o cartão ao lado. Os cartões
de antes estão em Cartões.» Some em «entendi» e não volta (`tour15` em `cancioneiro:ui`).

### O que não muda

- O cartão, o painel de qualidade, os módulos, o BPM, as marcas, a estrutura do cartão, a barra, os filtros e o rascunho.
- A curadoria da 0.13.0, com o interruptor «editar», que só sai na I3.
- Nenhum dado do acervo. No navegador, dois campos novos em `cancioneiro:ui`: `view` e `tour15`.

## O que muda para quem usa (a conta tem de fechar)

| Gesto de hoje | Na I2 |
|---|---|
| Rolar a grade para achar a faixa | a lista, uma linha por faixa, com os álbuns na lateral |
| Copiar o Style ou a Lyrics no cartão | também da linha, sem abrir nada; ou no detalhe, como hoje |
| Clicar no título do cartão copia o título | na **Lista**, o título da linha abre o detalhe, e o do cartão (no detalhe) continua copiando; em **Cartões**, nada muda |
| Marcar «usei» no rodapé | também no ✓ da linha |
| Escolher o álbum no painel Filtros | também na lateral |
| Trocar de acervo no seletor | também na lateral |

## Critérios de pronto (o chat mede no Chromium headless, `file://`, antes da WO)

| # | Critério |
|---|---|
| C1 | Sem `view` guardado, abre em Lista; escolher Cartões sobrevive ao recarregar. Em Cartões, abaixo de 1280 px, o `<main>` é idêntico ao da 0.14.0 para o mesmo acervo. |
| C2 | Uma linha por faixa que passa nos filtros, na ordem do acervo, agrupadas por álbum; o número de linhas bate com o «N de M»; cada linha tem 44 px no computador. |
| C3 | Rolando dentro de um álbum, o cabeçalho dele fica logo abaixo do topo (a distância é a altura do `#top`, com 1 px de folga). |
| C4 | «Style» da linha copia exatamente o que o «copiar» do Style do cartão da mesma faixa copia, também depois de ligar um módulo e mudar o BPM no detalhe; «Lyrics» copia a Lyrics. Nenhum dos dois leva rótulo ou título (regra de domínio). |
| C5 | Para cada faixa do acervo de teste, o nível da saúde é o pior entre as marcas `.q` do cartão dela, e tem texto. **Falso positivo:** a faixa com 10 tags (nível neutro) mostra «tudo dentro». |
| C6 | O ✓ marca e desmarca como «marcar usei» (a mesma chave `usedBy`); a linha esmaece; o filtro Uso responde. |
| C7 | Clicar no título abre o detalhe com o mesmo cartão (o mesmo HTML que a visão Cartões dá para a faixa); a linha fica com `aria-current`; ‹ e › andam pela lista filtrada, atravessando álbuns; × e `Esc` fecham, e o foco volta ao título. |
| C8 | Com o foco num título, `↓` e `↑` vão à faixa seguinte e à anterior, e o detalhe aberto acompanha. **Falso positivo:** com o foco na busca, `↓` e `↑` não mudam a faixa. |
| C9 | Abrir o detalhe põe `#faixa=<id>`; recarregar reabre a mesma faixa; o «Voltar» do navegador fecha o detalhe; um id inexistente é ignorado, sem erro de página. |
| C10 | A 1366 px, a lateral lista «Todas as faixas» e os álbuns com as contagens dos outros filtros; clicar num álbum põe o filtro (com a etiqueta) e marca `aria-current`; «Todas» tira; os acervos guardados aparecem, o aberto marcado, e clicar abre outro. A 1279 px, a lateral não aparece. |
| C11 | A 1366, 1024 e 800 px, sem rolagem horizontal; a 800, o detalhe fica por cima da lista; o título da linha nunca tem menos de 160 px. |
| C12 | No celular (390×844): linhas de pelo menos 64 px, ✓ de 44 px; tocar abre o detalhe em tela cheia; o pé copia o mesmo que o C4; voltar (o botão e o do navegador) devolve à lista na mesma rolagem. |
| C13 | Com «editar»: mover a faixa aberta mantém o detalhe nela e muda a linha de lugar; excluir fecha o detalhe; o rascunho conta como na 0.14.0. |
| C14 | Mudar um módulo ou o BPM no detalhe atualiza o BPM e a saúde da linha, e a rolagem da lista não muda. |
| C15 | A Lista de um acervo de 300 faixas desenha em no máximo 200 ms; o cabeçalho diz `v0.15.0`; nenhum erro de página; os testes das entregas 1 a 3 e da I1 continuam passando (em Cartões, onde medem o cartão). |

**Prova de vida:** o mesmo teste no app da 0.14.0 reprova (no mínimo C1, C2 e C7).

## Resultado (medido pelo chat em 2026-11-06, Chromium headless, `file://`, app de chegada da WO 0026)

**15 de 15 critérios.** Acervo de teste: as três faixas do `data/demo.json` e faixas feitas para cada nível de saúde
(10 tags, 12 tags, Lyrics acima de 5.000, Style perto de 1.000), em três álbuns, 19 faixas; outro com 300, para o C15.

| # | O que foi conferido | Resultado |
|---|---|---|
| C1 | sem `view`, abre em Lista; Cartões sobrevive ao recarregar; em Cartões, a 1279 px, o `<main>` é idêntico ao da 0.14.0 | OK |
| C2 | as 19 linhas na ordem do acervo; com Estado «gerada», o número de linhas bate com o «N de M»; 44 px cada | OK |
| C3 | rolando dentro do álbum B, o cabeçalho dele fica rente ao pé do `#top` (1 px de folga) | OK |
| C4 | depois de ligar um módulo e subir 5 BPM no detalhe, «Style» da linha copia o mesmo texto do «copiar» do cartão, com «80 bpm»; «Lyrics» copia a Lyrics; nenhum dos dois leva rótulo nem título | OK |
| C5 | nas 19 faixas, o nível da linha é o pior `.q` do cartão; 10 tags dá «● tudo dentro» (o falso positivo) | OK |
| C6 | o ✓ marca e desmarca; com Uso «só usados», sobra só a faixa marcada | OK |
| C7 | o detalhe tem o mesmo HTML que `renderCard`; «Álbum A · 4 de 4»; › vai à primeira do álbum B e ‹ volta; × e `Esc` fecham e devolvem o foco ao título | OK |
| C8 | `↓` e `↑` no título andam e o detalhe acompanha; com o foco na busca, `↓` não muda a faixa | OK |
| C9 | `#faixa=t-doze` no endereço; recarregar reabre; × não sai do app; o «Voltar» fecha; um id inexistente, trocado no endereço ou recarregado, some sem erro | OK |
| C10 | a 1366, «Todas as faixas» (19) e os três álbuns; com Estado «gerada», as contagens batem; clicar no álbum B filtra, põe a etiqueta e marca; «Todas» tira; os dois acervos guardados aparecem e o outro abre; a 1279, a lateral some | OK |
| C11 | a 1366, 1024 e 800 px, com o detalhe aberto: sem rolagem lateral; o detalhe ao lado nas duas primeiras e por cima a 800; o título com pelo menos 160 px | OK |
| C12 | a 390×844: linhas de 64 px ou mais, ✓ de 44×44; o detalhe cobre a tela, com o pé; «Copiar Style» copia o recomposto, «Título» o título; o «←» e o «Voltar» do navegador devolvem a mesma rolagem | OK |
| C13 | com «editar», ↑ no detalhe sobe a faixa e o detalhe fica nela; «excluir» fecha o detalhe e leva o foco a uma linha; o rascunho conta cada operação | OK |
| C14 | +5 BPM e três módulos no detalhe: a linha mostra «80 bpm» e a saúde nova; é o mesmo elemento (não redesenhou) e a rolagem não mudou | OK |
| C15 | a Lista de 300 faixas desenha em cerca de 50 ms (média de 5); `v0.15.0`; nenhum erro de página | OK |

**Prova de vida, medida:** no app da 0.14.0 o teste para no começo, antes do C1, porque o aviso da 0.15.0 e a Lista não
existem lá.

**Regressão:** os testes das entregas 1 a 3 e da I1 seguem em 15 de 15, 25 de 25, 19 de 19 e 14 de 14. Os três que medem
o cartão (exportar, curadoria e I1) rodam com a visão Cartões e o aviso novo já vistos, por um invólucro que semeia
`cancioneiro:ui` uma vez por aba. O dos acervos roda na Lista: conta linhas além de cartões, numa mudança de duas linhas.

**Onde a implementação saiu da spec:**
- **O Estado também cede** quando a lista fica com menos de 600 px. Sem isso, a 960 px com o detalhe aberto, a lista tem
  560 px e o título ficaria com 126; a ordem de saída é Idioma, BPM, Estado. O estado continua no detalhe.
- **O nome «Cancioneiro» sai da barra abaixo de 1180 px**, para caber Lista | Cartões; a versão segue no «⋯». A 1024 px,
  com rascunho e «editar», o C11 da I1 continua passando.
- **A lateral lê os acervos guardados só quando está visível e algo mudou** (o aberto, quantos, a data). Ler a cada
  troca de origem trazia os acervos inteiros do banco e deixava o teste dos acervos instável.
- **Clicar no resto da linha também abre** o detalhe (o mouse); o teclado usa o título.
- **A faixa usada fica em cor suave, não transparente:** a transparência derrubaria o contraste dos botões da linha.

**O que a revisão visual pegou:** no celular, com o detalhe aberto, o aviso de baixo cobria os botões de copiar; ele
sobe para cima deles.

## Fora de escopo

- **A I3:** a alça ⋮⋮, o arrastar, as caixas de seleção e o lote, o «⋯» por faixa, «+ Novo álbum», soltar na lateral, o
  «Desfazer» e o fim do interruptor «editar». **A I4:** salvar no arquivo.
- **A gaveta da lateral no celular** (ponto 2). Volta se fizer falta.
- **Ordenar a lista por coluna,** a terceira visão em tabela (a opção C da análise) e busca dentro do detalhe. Se
  fizerem falta, viram ideia.

## Riscos

- **O hábito de clicar no título para copiá-lo.** Na Lista, o clique passa a abrir o detalhe. Mitigação: o título do
  cartão no detalhe continua copiando; na visão Cartões, nada muda; o aviso da primeira abertura diz onde está cada
  coisa.
- **Duas cópias do Style.** A linha e o cartão têm de copiar o mesmo texto. Os dois leem o mesmo estado da sessão na
  hora do clique (`App.activeModules`, `App.bpm`), e o C4 confere depois de mexer nos dois.
- **Fixo dentro de fixo:** a lateral, o cabeçalho do álbum e o detalhe ficam fixos abaixo do topo, que tem 48 ou 84 px
  conforme haja filtros. A altura vem de medir o `#top`, não de um número escrito no CSS: é o C3.
- **O endereço com `#faixa=`:** abrir pelo `file://` e pelo Pages tem de dar o mesmo; o «Voltar» não pode sair do app
  quando o detalhe foi aberto pelo endereço (aí, fechar só limpa o endereço). É o C9.
- **Tamanho do acervo:** a Lista desenha todas as linhas de uma vez. Com 300 faixas, o C15 mede; se passar do limite,
  desenhar por álbum à medida que aparece.

## Pontos para o dono decidir

**Decididos pelo dono em 2026-11-06, os três como recomendados** (DEC-031): Lista por padrão, celular sem gaveta,
o título da linha abre o detalhe.

1. **A visão que abre sem escolha guardada:** **Lista (recomendada)**, porque é o ganho da I2; ou Cartões, que é o
   costume.
2. **Celular sem a gaveta da lateral (recomendada):** a análise previa uma gaveta, mas o que ela teria (álbuns e
   acervos) já está em Filtros e no seletor, a um toque. A gaveta seria um terceiro caminho para o mesmo lugar e
   ocuparia um quinto botão numa barra de 390 px. Ou a gaveta, como na análise.
3. **Na Lista, o título da linha abre o detalhe (recomendado),** e copiar o título fica no cartão do detalhe; ou o título
   copia, como no cartão, e um botão «abrir» à parte abre o detalhe (mais um alvo por linha).
