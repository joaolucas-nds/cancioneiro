# ANALISE — Frente de interface: organizar, ler e editar o acervo (i-044 a i-048)

> **Status:** Em discussão
> **Data:** 2026-11-05 (data de criação; não muda depois)
> **Ideias de origem:** i-044 (a barra que não some), i-045 (cabeçalho compacto), i-046 (filtros que acompanham a
> rolagem, visões no estilo Notion e Airtable), i-047 (painel lateral com abas) e i-048 (edição e organização sem UX,
> arrastar onde for útil). Pedido do dono em 2026-11-05: interface «bonita, profissional, intuitiva», com estudo e
> planejamento antes.
> **Protótipo:** canvas «Cancioneiro: nova interface» (Design, claude.ai), com 5 telas:
> `https://claude.ai/artifact/Sk1Xf5Rpr26WfGLbZJ2GAD`.
> **Toca:** DEC-002 (um arquivo, sem build), DEC-023 (estrutura do cartão), DEC-025 (cabeçalho enxuto), DEC-028 e
> DEC-029 (curadoria e rascunho).

## Problema

O app cresceu por camadas e hoje faz três trabalhos na mesma peça: o cartão serve para **ler**, **copiar** e
**editar**. As ações ficam espalhadas por três faixas no topo: o cabeçalho, a barra de filtros e a linha de origem, que
já tem até sete botões. A curadoria da 0.13.0 funciona, mas é botão por botão e janela por janela, sem arrastar. O dono
achou isso pouco prático e pouco intuitivo.

**Medido em 2026-11-05** (Chromium, 0.13.0, acervo sintético de 10 álbuns e 150 faixas, do tamanho da Rainha da
Preguiça; capturas no protótipo, tela «Hoje»):

| | Computador (1366×720) | Celular (390×844) |
|---|---|---|
| Cabeçalho (fixo, `sticky`) | 86 px | 182 px |
| Barra de filtros e linha de origem (rolam junto) | 98 px | 287 px |
| Altura de um cartão | 722 px, mais que a janela | 704 px |
| Cartões visíveis por tela | 3 | 1 |
| Altura da página inteira | 38.154 px | 109.545 px |

O que isso quer dizer no uso:
- **Achar uma faixa é rolar.** Com 3 cartões por tela, as 150 faixas ocupam umas 50 telas no computador e 130 no
  celular.
- **Os filtros somem ao rolar,** e não há resumo do que está filtrado.
- **No celular, 469 px de controles** vêm antes da primeira faixa, mais da metade da tela.
- **Editar exige ligar um modo,** achar o botão no rodapé de um cartão de 722 px e passar por uma janela para cada
  movimento.

## Restrições

- **Um arquivo, sem build (DEC-002),** e precisa abrir offline por `file://`. Biblioteca externa só se for embutida no
  próprio `index.html`.
- **A regra de domínio continua:** o que se copia não leva rótulo. Toda saída nova reverifica isso.
- **O cartão de hoje precisa continuar existindo como visão:** a estrutura configurável (DEC-023) e o painel de
  qualidade são trabalho conferido.
- **A identidade visual fica:** papel, tinta e brasa, títulos com serifa. O pedido é de organização e de UX, não de
  marca nova.

## O que a pesquisa trouxe

| Fonte | O que vale para o Cancioneiro |
|---|---|
| Notion, «Views, filters, sorts & groups» | Um mesmo conjunto de dados em várias visões (tabela, lista, quadro, galeria). O item abre em **side peek**: à direita, com a lista ainda interativa à esquerda. É o padrão de tabela e lista. |
| Airtable, visões e registro expandido | Lista ou grade para varrer; o registro completo num painel. Kanban para arrastar entre colunas. |
| Baymard, «How to design applied filters» | Mostrar os filtros aplicados **como etiquetas removíveis**, com «limpar tudo». Usuários que não perceberam um filtro aplicado interpretaram mal o que estavam vendo. 28% dos sites não mostram nenhum resumo. No celular: uma fileira que rola, com a contagem. |
| W3C, WCAG 2.2, critério 2.5.7 (nível AA) | Tudo que se faz arrastando precisa ter um caminho com **um clique, sem arrastar**. Exemplo dado pela própria norma: botões de subir e descer ao lado do item. |
| Atlassian, diretrizes de arrastar acessível | Alça visível **e** um botão «⋯» com as ações de mover; o foco volta ao item depois da ação; anunciar a posição nova para leitor de tela. Evitar setas como único controle. |
| Smart Interface Design Patterns, arrastar e soltar | Alça; estados (pegar, em trânsito, soltar); o lugar de origem marcado; uma linha onde vai cair; **desfazer** a última ação. No celular, preferir «Mover para…». |
| SortableJS 1.15.7 (npm, 2026-02-11) | MIT, sem dependências, toque incluso, listas ligadas (arrastar entre álbuns), alça. **45.478 bytes** minificado (15.038 compactado), medido. |

## Opções consideradas

### Arquitetura da tela

**A — Refino do que existe.** Cabeçalho e filtros numa faixa só, fixa; etiquetas de filtro; menu «⋯» para as ações
raras; cartão mais baixo.
- Resolve as i-044, i-045 e metade da i-046.
- Não resolve achar e organizar: continuam 3 cartões por tela, e editar continua no rodapé do cartão.

**B — Três painéis (recomendada).** É o protótipo, telas «Proposta · computador».
- **Barra única de 48 px**, fixa: seletor de acervo (substitui a janela «acervos»), busca, filtros, visão
  (Lista/Cartões), a marca de rascunho com «Salvar .json» e o «⋯» com o resto (importar, exportar .md, prompt,
  exemplo, estrutura).
- **Etiquetas de filtros aplicados** logo abaixo, só quando há filtro.
- **Lateral esquerda:** os álbuns com a contagem (clicar filtra; soltar uma faixa sobre um álbum a move) e os acervos
  guardados.
- **Centro em lista:** uma linha de 46 px por faixa, com alça, caixa de seleção, título, estado, idioma, BPM, o
  resumo do painel de qualidade, «Style», «Lyrics», «usei» e «⋯». Os cabeçalhos de álbum ficam fixos ao rolar.
- **Detalhe à direita** (o «side peek» do Notion): o cartão completo da faixa escolhida, com «Copiar Style» em
  destaque, os módulos, o BPM, a Lyrics e as ações.
- **«Cartões» continua como visão,** para quem prefere.
- No celular, a lateral vira gaveta, o detalhe vira tela própria com os botões de copiar fixos no pé, e as ações saem
  de uma folha que sobe (telas «Proposta · celular»).

**C — Tabela tipo planilha (estilo Airtable), com edição na célula.** É a mais densa e a melhor para editar estado e
BPM em massa. Descartada como base: o uso principal do dono é ler e copiar textos longos (Style, Lyrics), que não
cabem numa célula. E é a mais cara de fazer bem num arquivo só (edição na célula, teclado, colunas). Pode voltar como
uma terceira visão, se fizer falta.

### Arrastar

| Opção | A favor | Contra |
|---|---|---|
| **Arrastar nativo do HTML5** | 0 KB a mais | No celular, o suporte a toque é ruim ou ausente; a imagem que segue o cursor não se controla; arrastar entre listas e rolar sozinho exigem código à mão |
| **SortableJS embutido (recomendada)** | Toque, listas ligadas, alça, animação, rolagem automática; maduro e MIT | +45 KB no `index.html` (o app tem 113.128 bytes na 0.13.0, medido no disco em 2026-11-05: passaria a ~158 KB); é código de terceiro dentro do arquivo, com a licença no cabeçalho |
| **Código próprio com eventos de ponteiro** | Pequeno e só o que se usa | O mais caro de acertar: toque, rolagem automática, soltar entre listas, acessibilidade. Erra fácil e em silêncio, e o teste não pega tudo |

**Os caminhos sem arrastar continuam em todas as opções** (WCAG 2.5.7): o «⋯» de cada linha e do detalhe traz
«Mover para…», «Subir», «Descer», «Exportar» e «Excluir». No celular, é o caminho principal. Seleção em lote: as
caixas de seleção ligam uma barra no pé da tela com mover, exportar `.json`, marcar «usei» e excluir, para várias
faixas de uma vez.

### O interruptor «editar»

- **Manter o interruptor.** Protege contra o clique errado, mas esconde a organização atrás de um modo. Foi um dos
  pontos que o dono achou pouco intuitivo.
- **Sempre editável, com «Desfazer» (recomendada).** A alça e o «⋯» ficam sempre ali; toda operação deixa um «Desfazer»
  no aviso até a próxima; excluir continua pedindo confirmação. O erro fica barato de reverter, o que o padrão de
  arrastar pede.
  - **Custo:** guardar a cópia anterior do álbum mexido (ou do acervo) para uma volta só.
  - O rascunho e o «Salvar .json» seguem como na DEC-028.

## Recomendação

**B (três painéis), com o SortableJS 1.15.7 embutido e sem o interruptor «editar», em quatro entregas.** Cada uma é
usável sozinha, e a de menor risco vem primeiro:

| Entrega | O que traz | Ideias |
|---|---|---|
| **I1 — Barra única** (0.14.0) | Barra de 48 px fixa, com o seletor de acervo, a busca, os filtros com etiquetas removíveis, o rascunho com «Salvar .json» e o «⋯»; a barra que não some corrigida; o celular sem os 469 px de controles. O cartão não muda. | i-044, i-045, i-046 (filtros) |
| **I2 — Lista e detalhe** (0.15.0) | A visão Lista com cabeçalhos de álbum fixos, o detalhe à direita (no celular, tela própria), a lateral de álbuns e acervos, e a escolha de visão guardada no navegador. «Cartões» continua. | i-046 (visões), i-047 |
| **I3 — Organizar** (0.16.0) | Arrastar pela alça (na lista, entre álbuns, sobre a lateral); o «⋯» por faixa; a seleção em lote; o «Desfazer»; o fim do interruptor «editar»; soltar um `.json` sobre um álbum para importar as faixas nele. | i-048 |
| **I4 — Salvar no arquivo** (0.17.0) | «Salvar» grava direto no `.json` de origem onde o navegador deixa (o Chrome do dono deixa); «Baixar» continua onde não deixa. | i-043 |

**Por que nessa ordem:**
- A I1 mexe só no topo e já dá o espaço de que as outras precisam.
- A I2 muda o miolo, mas sem mudar como se edita.
- A I3 é a que mais muda o hábito do dono, e chega com a lista pronta para receber a alça.
- A I4 fecha o «baixar e substituir», que só faz sentido depois que salvar ficou fácil de achar.

**Antes de cada spec:** um protótipo navegável da entrega, no mesmo canvas, para o dono julgar olhando. O desta
análise mostra o destino, não cada passo.

## Riscos

- **Peso do arquivo:** +45 KB de biblioteca. Sinal: o app abrir mais devagar no `file://`. Medir o tempo de abertura
  antes e depois da I3.
- **Código de terceiro dentro do app:** a versão fica fixa (1.15.7), com a licença MIT no cabeçalho e o hash
  registrado. Trocar de versão passa a ser decisão, não acidente.
- **Duas visões a manter** (Lista e Cartões): toda saída nova reverifica a regra de domínio nas duas. A estrutura do
  cartão (DEC-023) passa a valer para o detalhe e para a visão Cartões.
- **Sem o interruptor, o clique errado fica mais fácil.** É o «Desfazer» que segura isso, e o teste da I3 tem de medir
  o falso positivo: soltar no mesmo lugar não pode contar alteração.
- **No celular, arrastar é impreciso.** Por isso o caminho principal lá é o «⋯» e a seleção em lote; o arrastar no toque
  pede segurar antes de pegar.
- **A barra única tem de caber em 1366 px.** No protótipo ela cabe, com a busca limitada a 460 px `[desenhado, não
  medido no app]`. Em janelas menores, os itens descem para o «⋯»; a spec da I1 mede.

## Ponto de decisão

Quatro respostas para a frente virar spec. Cada uma já vem com a recomendada:

1. **Arquitetura:** B (três painéis), A (refino do que existe) ou C (tabela)? Recomendada: **B**.
2. **Arrastar:** SortableJS embutido, código próprio, ou só os caminhos sem arrastar? Recomendada: **SortableJS
   embutido**.
3. **O interruptor «editar»:** tirar, com «Desfazer» (recomendada), ou manter?
4. **Ordem:** I1 → I2 → I3 → I4 (recomendada), ou outra?
