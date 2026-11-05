# SPEC — Vários acervos guardados no navegador (curadoria, entrega 2)

> **Status:** Pronta para WO (0.12.0)
> **Decidida em:** 2026-11-02 pelo dono: F1 + G1, entregas 1 → 2 → 3 (análise
> `meta/analises/261102-ANALISE-curadoria-no-app.md`, DEC-028). As escolhas abaixo são técnicas, dentro dessa decisão.
> **Data:** 2026-11-04 (data de criação; não muda depois)
> **Ideia de origem:** i-041 (nota do dono `261029-1825.txt`), com a correção das marcas «usei» achada na análise.
> **Depende de:** 0.11.0 (entrega 1, `d3ad6f0`), conferida na tela pelo dono em 2026-11-04 (roteiro de 6 itens, tudo OK).

---

## Problema

O navegador guarda só o último acervo importado (DEC-022). O dono usa três: a Rainha da Preguiça, os 12 álbuns e o
de referências. Cada troca é uma nova importação, com seletor de arquivo. E as marcas «usei» são guardadas só pelo id
da faixa (`App.ui.used[id]`), sem dizer de qual acervo: `brv-04` existe na Rainha e no demo, `cinzeiro-01` no demo e
no exemplo, e marcar num marca no outro.

## O que a sonda mediu (2026-11-05 01:49 UTC, `../notas-arquivadas/261102-sonda-armazenamento-file.txt`)

No navegador do dono (Chrome 156, Windows), aberto por `file://`:

| Medida | Valor |
|---|---|
| `localStorage` total | 5.242.731 caracteres (livre 5.214.208, com precisão de 4.096) |
| `localStorage` já usado | 28.523 caracteres em 11 chaves, **7 delas de outros projetos** (`kit-state-*`, `kit-niche`, `base_v4`) |
| IndexedDB | grava e lê 1.500.000 caracteres |
| Cota (`storage.estimate`) | 10.737 MB |
| Armazenamento persistente | `false` (ainda não foi pedido) |
| Gravar direto no arquivo | as três APIs existem (`showSaveFilePicker`, `showOpenFilePicker`, `getAsFileSystemHandle`) |

O que isso muda no plano:
- **Some o risco principal da análise:** o IndexedDB funciona no `file://`. O ramo sem IndexedDB fica como
  defesa, não como caso comum.
- **No `file://`, todas as páginas locais são a mesma origem.** As chaves `kit-state-*` são das ferramentas do KCM
  abertas pelo mesmo navegador. Tudo do Cancioneiro precisa de nome próprio: o banco se chama `cancioneiro`, as chaves
  continuam com o prefixo `cancioneiro:`, e o app nunca lê, conta nem apaga o que não é dele.
- **A cota do `localStorage` é a maior das estimativas** (5,24 milhões), mas é dividida com essas outras páginas. G1
  continua: os três acervos (1.410.184 caracteres) ocupariam 27% de um espaço que não é só nosso.
- **A i-043 (gravar direto no arquivo) tem a API no navegador do dono.** O gatilho dela continua sendo depois da
  entrega 3.
- **Não medido:** o endereço do Pages (`https://`). Lá a origem é outra, o comportamento do IndexedDB é o padrão, e o
  armazenamento é separado do `file://` (já é assim hoje).

## O que construir

### 1. Onde mora cada coisa

| Dado | Lugar | Chave |
|---|---|---|
| Os acervos | IndexedDB, banco `cancioneiro`, depósito `acervos` | o **nome do arquivo** importado |
| Cada registro | `{ source, title, savedAt, json }` | `source` = nome do arquivo |
| O acervo aberto | `cancioneiro:ui`, campo `open` | o `source` |
| Marcas «usei» | `cancioneiro:ui`, campo `usedBy` | `usedBy[source][id] = true` |
| Estrutura do cartão | `cancioneiro:ui`, campo `layout` (sem mudança) | — |

O `json` gravado é a coleção como foi importada, depois do `stripInternalKeys`, igual à de hoje.

### 2. Importar

- Importar (botão ou arrastar) grava o acervo no IndexedDB sob o nome do arquivo e o abre.
- **Mesmo nome já guardado:** substitui o registro e diz no toast «substituiu a cópia de dd/mm hh:mm». Não pede
  confirmação: nesta entrega a cópia ainda não tem edição, então o arquivo importado é sempre a versão mais nova.
- Na primeira gravação que der certo, o app chama `navigator.storage.persist()` uma vez. O resultado aparece na
  janela de acervos (item 4), não no toast.
- **Não coube** (`QuotaExceededError`): o acervo abre na sessão, e o toast diz «não coube no navegador: ao fechar,
  ele não volta», como hoje.

### 3. Abrir o app

1. **Migração, uma vez:** se existir `cancioneiro:acervo` (o formato da 0.9.0 a 0.11.0), o app grava esse acervo no
   IndexedDB, lê de volta e compara com o original. **Só depois de bater** apaga `cancioneiro:acervo`. Se a gravação
   ou a leitura falhar, a chave antiga fica onde está e o app segue como na 0.11.0.
2. **Marcas:** se `cancioneiro:ui` tiver o campo antigo `used`, cada marca é copiada para **todo acervo guardado que
   tenha uma faixa com aquele id**. Uma marca cujo id não existe em nenhum acervo guardado vai para `usedBy["demo.json"]`.
   Nos dois ids que colidem hoje, a marca vai para os dois acervos: é o que a tela já mostra, então ninguém perde
   nada. Depois disso, `used` sai.
3. Abre o acervo de `open`. Se ele não estiver guardado, abre o importado mais recente. Se não houver nenhum, faz a
   carga automática do Pages (`data/demo.json`), como hoje.

A abertura passa a ser assíncrona. Enquanto o IndexedDB responde, a tela mostra o estado vazio de hoje, sem aviso
novo.

### 4. Trocar de acervo

A linha de origem, na barra de controles, ganha um botão **«acervos (N)»** entre o texto e o «esquecer». O cabeçalho
não cresce (DEC-025). O botão abre uma janela:

- **Uma linha por acervo guardado, do importado mais recente para o mais antigo:** título, nome do arquivo, data da
  importação, e contagem de álbuns e faixas. Botões «abrir» e «esquecer».
- O acervo aberto vem marcado «aberto», sem o botão «abrir».
- No rodapé da janela: «Guardado de forma persistente: sim/não». Com «não», o navegador pode apagar os acervos
  quando faltar espaço no disco, e o arquivo continua sendo a fonte.

Abrir troca o acervo sem seletor de arquivo, grava `open` e zera os módulos ligados e o BPM da sessão, como uma
importação faz hoje (FIX-008).

### 5. Esquecer

- «esquecer» (na linha de origem ou na janela) apaga **só aquele acervo** do IndexedDB. Se ele era o aberto, abre o
  importado mais recente que sobrou; se não sobrou nenhum, volta ao estado inicial (no Pages, o demo).
- **As marcas «usei» daquele acervo ficam:** ocupam pouco, e reimportar o mesmo arquivo as traz de volta. O toast diz
  isso. O arquivo no computador nunca é tocado.

### 6. Marcas por acervo

`isUsed` e `toggleUsed` passam a ler e gravar em `usedBy[<acervo aberto>]`. O acervo do Pages, que não é importado,
usa a chave `demo.json`, a mesma de quem importa o `demo.json` à mão. O filtro «Uso» segue o acervo aberto.

### 7. Sem IndexedDB

Se o banco não abrir (navegador que bloqueia ou modo privado restrito), o app segue exatamente como a 0.11.0: um
acervo no `localStorage`, sem o botão «acervos». Avisa uma vez por sessão: «este navegador não deixou guardar vários
acervos; guardo só o último». As marcas continuam por acervo, porque moram no `localStorage`.

## Escolhas técnicas e por quê

- **A chave é o nome do arquivo, não o título nem um id no esquema** (análise, G1). Reimportar `albuns-reagrupados.json`
  regerado substitui, em vez de criar um segundo.
- **Abre o último aberto, não o último importado.** Quem trocou de acervo espera reabrir no mesmo lugar.
- **Esquecer não apaga as marcas.** É o que a DEC-022 já fazia, e as marcas são o dado mais caro de refazer.
- **O botão fica na linha de origem.** É ela que já diz qual acervo está na tela.
- **Uma faixa exportada (entrega 1) e importada vira um acervo guardado como qualquer outro.** Fica na lista até ser
  esquecida. Não tratar como caso especial mantém uma regra só.

## Critérios de pronto (o chat mede no Chromium headless, `file://`, antes da WO)

Acervos sintéticos do tamanho dos reais: os do dono ficam fora do repo e fora do ambiente do chat (DEC-026).

| # | Critério |
|---|---|
| C1 | **Migração:** com `cancioneiro:acervo` e marcas antigas no `localStorage`, abrir o app mostra o mesmo acervo e as mesmas marcas; o IndexedDB tem 1 registro; `cancioneiro:acervo` não existe mais. |
| C2 | **Migração que falha** (gravação simulada com erro): `cancioneiro:acervo` continua lá; o app abre como na 0.11.0. |
| C3 | **Três acervos importados:** a janela lista os três, com título, arquivo, data e contagem; «abrir» troca sem seletor; o aberto vem marcado. |
| C4 | **Recarregar** abre o último aberto, mesmo que outro tenha sido importado depois. |
| C5 | **Reimportar o mesmo nome:** continua 1 registro, com a data nova; o toast diz «substituiu». |
| C6 | **Marcas por acervo:** marcar `brv-04` num acervo não marca `brv-04` no outro; o filtro «Uso» segue o aberto. |
| C7 | **Marca antiga com id em dois acervos guardados** migra para os dois. |
| C8 | **Esquecer:** só aquele sai; se era o aberto, abre o mais recente que sobrou; reimportar o arquivo traz as marcas de volta. |
| C9 | **Sem IndexedDB** (simulado): o comportamento da 0.11.0, sem o botão, com o aviso. |
| C10 | **Não coube** (simulado): o acervo abre na sessão e o toast avisa. |
| C11 | **Tamanho real:** três acervos sintéticos de 960 mil, 430 mil e 22 mil caracteres, gravados, trocados e reabertos, saem idênticos ao importado (`JSON.stringify` igual). |
| C12 | «Baixar .json» do acervo aberto continua igual ao importado. |
| C13 | Sem nada guardado, a carga automática do Pages continua; as marcas do demo vão para `demo.json`. |
| C14 | As chaves de outros projetos no `localStorage` (`kit-state-*`, por exemplo) continuam intactas depois de tudo. |
| C15 | `storage.persist()` é chamado uma vez, e a janela mostra o resultado. |
| C16 | O cabeçalho diz `v0.12.0`; nenhum erro de página; a entrega 1 (exportar faixa como `.json`) continua passando no teste dela. |

**Prova de vida:** o mesmo teste no app da 0.11.0 reprova (no mínimo C1, C3, C6 e C16).

## Fora de escopo

- Excluir, reordenar, mover faixa, novo álbum, importar faixas, o rascunho marcado (entrega 3).
- Gravar direto no arquivo (i-043, depois da entrega 3).
- Apagar marcas órfãs, ou uma janela para gerenciar as marcas.
- Juntar acervos.

## Riscos

- **Dois arquivos diferentes com o mesmo nome**, vindos de pastas diferentes: o segundo substitui o primeiro. O
  toast «substituiu» é o aviso. É raro: os nomes de hoje são todos distintos.
- **Duas abas abertas ao mesmo tempo:** `cancioneiro:ui` fica com o que a última aba gravou, como já acontece hoje
  com as marcas.
- **Abertura assíncrona:** um clique durante a abertura não pode cair num acervo pela metade. Os botões que
  dependem do acervo só ligam depois de `setCollection`, como hoje.
- **A migração é o único ponto que apaga dado** (`cancioneiro:acervo`), e só apaga depois de ler de volta e comparar.
  É o C1 e o C2.
