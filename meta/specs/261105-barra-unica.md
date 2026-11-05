# SPEC — Barra única (frente de interface, entrega I1)

> **Status:** Pronta para WO (0.14.0)
> **Decidida em:** 2026-11-05 pelo dono. Na análise `meta/analises/261105-ANALISE-frente-de-interface.md`, ele aprovou:
> - a arquitetura B (três painéis);
> - o SortableJS embutido;
> - o fim do interruptor «editar» (na I3);
> - a ordem I1 → I2 → I3 → I4.
> Esta é a I1.
> **Data:** 2026-11-05 (data de criação; não muda depois)
> **Ideias de origem:** i-044, i-045 e a parte de filtros da i-046.
> **Protótipo:** telas «I1 · computador» e «I1 · celular» no canvas «Cancioneiro: nova interface»
> (`https://claude.ai/artifact/Sk1Xf5Rpr26WfGLbZJ2GAD`). A tela do computador é navegável: abre o seletor de acervo,
> os filtros e o «⋯», e tira etiquetas.
> **Depende de:** 0.13.0 (`f695f81`).

---

## Problema

O topo de hoje tem três faixas: o cabeçalho (86 px, fixo), a barra de filtros e a linha de origem (98 px, que rolam
junto). No celular, são 469 px antes da primeira faixa. Os filtros somem ao rolar e não deixam resumo do que está
filtrado. Achar «esquecer», «acervos» ou «editar» exige saber que eles moram numa linha de texto miúdo. A I1 junta tudo
numa barra só, fixa, e não mexe no cartão. O cartão é a I2.

## O que construir

### 1. A barra (fixa no topo, uma linha)

Da esquerda para a direita:

| Peça | O que é | Substitui |
|---|---|---|
| **Cancioneiro** v0.14.0 | o nome e a versão, menores | o título de 26 px |
| **Seletor de acervo** | botão com o título do acervo aberto, o nome do arquivo e a contagem («150 faixas»); abre um menu (item 2) | «acervos (N)», a janela de acervos, a linha de origem e a contagem da barra de filtros |
| **Busca** | o campo de hoje, até 460 px; a tecla `/` leva o foco a ele (fora de um campo de texto) | a busca da barra de filtros |
| **Filtros** | botão com o número de filtros ligados; abre um painel com Álbum, Estado e Uso (os mesmos selects de hoje) | os três selects |
| *(espaço)* | | |
| **Rascunho** | só com alterações: «● N alterações não salvas» com o botão **Salvar .json** (o mesmo «Baixar .json» da DEC-028, com o nome de origem) | a marca de rascunho e o «Baixar .json» da linha de origem |
| **editar** | o interruptor da 0.13.0, igual (`aria-pressed`). Fica só até a I3, que o tira. Ligado, aparece ao lado **importar faixas…** | os dois da linha de origem |
| **⋯** | menu com o resto (item 3) | os seis botões do cabeçalho |

**Altura:** 48 px no computador. Abaixo de 720 px de largura, 52 px, numa linha só (item 5).

### 2. O menu do seletor de acervo

Abre ancorado no botão, sem janela no meio da tela:
- **Uma linha por acervo guardado,** do importado mais recente ao mais antigo, com título, arquivo, data e contagem; o
  aberto marcado. Clicar abre o acervo, como o «abrir» de hoje.
- **No pé do menu:**
  - «Importar outro .json…», o seletor de arquivo de hoje;
  - «Esquecer este acervo», o «esquecer» de hoje, com a mesma confirmação quando há alterações (DEC-028);
  - a origem («importado de X em dd/mm hh:mm · guardado neste navegador»), em texto miúdo, que é o que a linha de origem
    dizia;
  - «Guardado de forma persistente: sim/não».
- **Esquecer outro acervo:** um «×» na linha dele, com a mesma regra.
- **Sem acervo aberto,** o botão diz «Abrir um acervo» e o menu traz «Importar .json…» e os guardados.

A janela «acervos» da 0.12.0 sai: o menu faz o mesmo, mais perto de onde se clica.

### 3. O menu «⋯»

Na ordem:
1. Importar .json…
2. Baixar .json
3. Exportar .md
4. *(separador)*
5. Prompt para chats
6. Baixar exemplo
7. *(separador)*
8. Estrutura do cartão

Cada item chama a mesma função de hoje. «Baixar .json» continua aqui mesmo sem alterações, porque é o caminho para
baixar a qualquer hora.

### 4. Filtros aplicados

- **Com pelo menos um filtro ou uma busca,** aparece logo abaixo da barra, fixa junto dela, uma fileira de 36 px com:
  - «N de M faixas»;
  - uma etiqueta por filtro ligado («Álbum Volume 3 ×», «Estado gerada ×», «Uso não usadas ×»);
  - a busca como etiqueta («“forja” ×»);
  - **Limpar tudo**.
- O «×» de cada etiqueta tira só aquele filtro (Baymard: remover direto no resumo).
- **Sem filtro nem busca, a fileira não existe.** Corrige a i-044 de passagem: a regra `[hidden] { display: none !important; }`
  vale para o app inteiro, e o que tem `hidden` some de fato.

### 5. Celular (largura abaixo de 720 px)

- A barra fica numa linha de 52 px, com botões de 44 px: o seletor de acervo (título truncado), o ícone de busca, os
  Filtros e o «⋯».
- O nome do app e a versão vão para o topo do «⋯».
- **A busca** abre um campo na largura toda, abaixo da barra, e o mesmo botão (ou `Esc`) fecha.
- **As etiquetas de filtro** viram uma fileira que rola na horizontal, com a contagem no começo.
- **O rascunho** sai da barra e vira um aviso fixo no pé da tela, com «Salvar .json».
- **Teto medido:** com um filtro ligado, os controles antes do primeiro cartão somam **no máximo 100 px** (hoje, 469).

### 6. Popovers

O seletor de acervo, os Filtros e o «⋯» abrem um painel ancorado no botão:
- **Fecham** com `Esc`, com clique fora ou quando se escolhe um item, e o foco volta ao botão que abriu.
- **Só um fica aberto** por vez.
- **Cada botão** tem `aria-expanded` e `aria-haspopup`.
- **Teclado:** o painel recebe o foco no primeiro item, e as setas não são exigidas (Atlassian: botões e menus, sem
  depender de setas).

### O que não muda

- O cartão, a visão, o arrastar `.json` para a tela, a curadoria da 0.13.0 (com o interruptor) e o rascunho.
- O painel de qualidade, os módulos, o BPM, as marcas e a estrutura do cartão.
- Nenhum dado do acervo muda. No navegador, só um campo novo em `cancioneiro:ui`: o aviso de primeira abertura (Riscos).

## Inventário: para onde vai cada controle de hoje (15 controles e 1 texto)

| Hoje | Onde estava | Na I1 |
|---|---|---|
| Prompt | cabeçalho | ⋯ › Prompt para chats |
| Exemplo | cabeçalho | ⋯ › Baixar exemplo |
| Estrutura | cabeçalho | ⋯ › Estrutura do cartão |
| Importar .json | cabeçalho | ⋯ › Importar .json… e o seletor de acervo › Importar outro .json… |
| Baixar .json | cabeçalho | ⋯ › Baixar .json, e «Salvar .json» quando há alterações |
| Exportar .md | cabeçalho | ⋯ › Exportar .md |
| Álbum, Estado, Uso | barra de filtros | o painel Filtros e as etiquetas |
| busca | barra de filtros | a busca da barra |
| contagem («X · N/M faixas») | barra de filtros | o seletor de acervo (total) e a fileira de filtros («N de M») |
| texto de origem e data | linha de origem | o pé do menu do seletor de acervo |
| marca de rascunho e Baixar .json | linha de origem | o rascunho da barra |
| editar | linha de origem | a barra (até a I3) |
| importar faixas… | linha de origem | a barra, com editar ligado |
| acervos (N) | linha de origem | o seletor de acervo |
| esquecer | linha de origem | o seletor de acervo › Esquecer este acervo |

**A conta tem de fechar:** cada linha da tabela tem um destino. O C2 confere isso clicando em cada destino.

## Critérios de pronto (o chat mede no Chromium headless, `file://`, antes da WO)

| # | Critério |
|---|---|
| C1 | No computador (1366×720), a barra tem **no máximo 48 px**, numa linha, e continua fixa ao rolar a página até o fim. |
| C2 | Cada uma das 15 linhas do inventário chega à função de hoje pelo destino novo (clicado no teste), com o mesmo efeito que tinha na 0.13.0. |
| C3 | O seletor de acervo lista os guardados em ordem, marca o aberto e abre outro; «Esquecer este acervo» com alterações pede confirmação. |
| C4 | Filtros: o número no botão bate com os filtros ligados; cada etiqueta tira só o seu filtro; «Limpar tudo» tira todos e a busca; «N de M» bate com os cartões na tela. |
| C5 | Sem filtro nem busca, a fileira de etiquetas não aparece (`hidden` e altura 0); a regra `[hidden]` vale para o app todo (i-044). |
| C6 | A tecla `/` leva o foco à busca, mas não quando o foco já está num campo de texto (o falso positivo). |
| C7 | Popovers: `Esc` e o clique fora fecham; o foco volta ao botão; abrir um fecha o outro; `aria-expanded` acompanha. |
| C8 | Rascunho: com alterações, «● N alterações não salvas» e «Salvar .json» na barra; sem alterações, nada. «Salvar» baixa com o nome de origem e zera (DEC-028). |
| C9 | No celular (390×844): a barra tem no máximo 52 px, numa linha; os botões têm pelo menos 44 px; a busca abre e fecha; o rascunho fica no pé da tela. |
| C10 | No celular, com um filtro ligado, a distância do topo da página ao primeiro cartão é de **no máximo 100 px** (hoje, 469). |
| C11 | A 1024 px de largura, a barra continua numa linha (a busca encolhe até 160 px). |
| C12 | O cartão é idêntico ao da 0.13.0: o mesmo HTML no `<main>` para o mesmo acervo, com filtros e editar desligados. |
| C13 | O cabeçalho diz `v0.14.0`; nenhum erro de página; os testes das entregas 1 a 3 continuam passando, com os seletores dos botões que mudaram de lugar ajustados. |

**Prova de vida:** o mesmo teste no app da 0.13.0 reprova (no mínimo C1, C5 e C10).

## Fora de escopo

- A lista, o detalhe e a lateral de álbuns (I2). O arrastar, o «⋯» por faixa, o lote e o fim do interruptor (I3).
  Salvar no arquivo (I4).
- O tema escuro além do que as variáveis de cor já fazem.

## Riscos

- **Achar o que mudou de lugar.** Os seis botões do cabeçalho passam para o «⋯». Mitigação: na primeira abertura da
  0.14.0, um aviso de uma linha («Prompt, Exemplo, Importar e Exportar estão em ⋯») que some ao clicar, guardado no
  navegador (campo `tour14` em `cancioneiro:ui`). É o único dado novo, e é de interface.
- **Popover feito à mão:** foco, `Esc` e clique fora são o tipo de coisa que quebra em silêncio. É o C7.
- **O botão «Baixar .json» do cabeçalho** está nos testes das entregas 1 a 3: eles mudam de seletor junto (C13), sem
  mudar o que medem.
