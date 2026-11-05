# SPEC — Curadoria pela tela (curadoria, entrega 3)

> **Status:** Pronta para WO (0.13.0) — com um desvio da análise para o dono ver (item 2, «fechar a aba»)
> **Decidida em:** 2026-11-02 pelo dono: F1 + G1, entregas 1 → 2 → 3, o `.json` curado manda sobre os conversores
> (análise `meta/analises/261102-ANALISE-curadoria-no-app.md`, DEC-028). As escolhas abaixo são técnicas, dentro dela.
> **Data:** 2026-11-05 (data de criação; não muda depois)
> **Ideia de origem:** i-040 (nota do dono `261029-1825.txt`: reorganizar álbuns, mudar a ordem, tirar e trazer
> faixas, inclusive de outros álbuns e de uma faixa exportada solta).
> **Depende de:** 0.12.0 (entrega 2, `e6663d8`).

---

## Problema

O dono quer mexer no acervo sem chat nem WO: tirar faixa, mudar a ordem, levar faixa de um álbum a outro, criar
álbum, trazer faixas de outro `.json` (inclusive uma exportada pela entrega 1). Hoje o app só lê, e o reagrupamento da
i-038 só existe por mapa e script. Com a entrega 2, cada acervo já tem uma cópia guardada no navegador. A entrega 3
faz dessa cópia um **rascunho**: o arquivo continua sendo a fonte, até o dono baixar o novo (F1).

## O que construir

### 1. Modo «editar»

Um botão **«editar»** na linha de origem liga e desliga a curadoria. É um interruptor (`aria-pressed`), guardado só na
sessão.

- **Desligado (padrão):** o cartão fica exatamente como na 0.12.0, com três botões no rodapé.
- **Ligado:**
  - o rodapé de cada cartão ganha **↑**, **↓**, **«mover…»** e **«excluir»**;
  - a linha de origem ganha **«importar faixas…»**.

**Por quê:** a leitura, que é o uso diário, continua limpa; a edição não acontece por um clique errado; e o rodapé
não passa de três para sete botões o tempo todo.

### 2. O rascunho

- **Onde mora:** o registro do acervo no IndexedDB (entrega 2) passa a ser o rascunho. Cada operação grava a coleção
  alterada no mesmo registro, com dois campos novos:
  - `changes`, o número de alterações desde a última importação ou o último «Baixar .json»;
  - `editedAt`, a hora da última alteração.
  No modo sem IndexedDB, o mesmo vale para a cópia do `localStorage`.
- **Marca sempre visível**, com o modo «editar» ligado ou não: com `changes > 0`, a linha de origem diz
  **«alterado: N alterações não baixadas»** e mostra o botão **«Baixar .json»** ali mesmo.
- **«Baixar .json»** (o do cabeçalho e o da marca):
  - O arquivo baixado leva o **nome do arquivo de origem** (`albuns-reagrupados.json`), não o título. Assim é só
    substituir o arquivo antigo.
  - Sem origem (o demo do Pages), o nome continua sendo o título.
  - O download zera `changes`.
  - O toast diz: «Baixado como X. Substitua o arquivo antigo por este: ele passa a ser a fonte. Se o navegador
    acrescentar "(1)" ao nome, tire ao substituir.»
- **Confirmação antes de perder alterações** (só com `changes > 0`), numa janela do app, sem `confirm()` do navegador:
  - **esquecer** o acervo: «as N alterações não baixadas se perdem»;
  - **reimportar** o mesmo nome: «o arquivo substitui o rascunho e as N alterações se perdem».
- **Fechar a aba não pede confirmação — desvio da análise.** A análise (F1) previa um aviso ao fechar a aba com
  alteração não baixada. Com a entrega 2, o rascunho já fica gravado no navegador a cada operação, e fechar a aba não
  perde nada. O aviso apareceria em todo fechamento, sem motivo, e ensinaria a ignorá-lo.
  - **Exceção:** se gravar uma alteração no navegador falhar, o app avisa na hora («não consegui guardar no
    navegador: baixe o .json para não perder») e passa a avisar ao fechar a aba até o próximo download.
  - **O dono pode pedir o aviso de volta** em toda situação; é uma linha.

### 3. As operações

Uma operação = uma alteração na contagem. Depois de cada uma, o app grava o rascunho, redesenha a tela **mantendo a
posição da rolagem** e diz no toast o que fez.

| Operação | Como | Regras |
|---|---|---|
| **↑ / ↓** | troca a faixa com a vizinha do mesmo álbum | Na ordem completa do álbum, mesmo com filtro ou busca ligados. Na ponta, o botão fica desligado. A faixa movida continua visível na tela. |
| **mover…** | janela com os outros álbuns do acervo e **«novo álbum…»** (com campo de título) | A faixa vai para o fim do álbum de destino. O álbum novo ganha `id` pelo `slug` do título, com sufixo `-2`, `-3`… se já existir. |
| **excluir** | confirmação na janela do app, com o título da faixa | A faixa sai do rascunho. «Fica no arquivo até você baixar o novo.» A marca «usei» dela sai. |
| **importar faixas…** | escolhe um `.json` (o mesmo leitor da importação, que aceita resposta de chat colada); janela com as faixas por álbum, cada uma com caixa marcada, e o destino | Regras abaixo. |

**Álbum que fica vazio** (a última faixa saiu ou foi movida) é removido do rascunho, e o toast diz isso. A tela não
mostra álbum vazio, então mantê-lo criaria um álbum invisível.

**O estado da sessão segue a faixa:** os módulos ligados e o BPM ficam presos ao id dela, e mover não mexe nisso.

### 4. Importar faixas — as regras (da análise)

**Destino:**
- **Padrão, «manter os álbuns de origem»:** cada faixa vai para o álbum do acervo aberto que tem o mesmo `id` do
  álbum de onde ela veio; se não existir, é criado com o título de origem. Uma faixa exportada pela entrega 1 volta
  assim para o próprio álbum.
- **Alternativa:** um álbum escolhido, ou «novo álbum…».

**Id de faixa repetido:**
- **Conteúdo idêntico** (o objeto inteiro serializado, nunca só o título) pula, e a contagem diz «já estavam».
- **Conteúdo diferente** entra com o próximo sufixo livre (`-2`, `-3`…), e a contagem diz «renomeadas». É o caso «Rise
  of the Eternal»: mesmo título não é mesma canção.

**Módulos citados pelas faixas importadas:**

| Situação | O que acontece |
|---|---|
| Existe no arquivo de origem e não no acervo aberto | Entra no acervo. |
| Mesmo id e mesmo texto nos dois | Nada muda. |
| Mesmo id e texto diferente | O da origem entra com sufixo, e a faixa importada passa a citar o id novo. |
| Não existe nem na origem | A citação fica como está (conversão fiel), e a contagem diz «citados que não existem». |

**O toast conta cada caso:** «N faixas importadas · X já estavam · Y renomeadas · Z módulos trazidos · W módulos
renomeados · K citados que não existem». Sem saneamento mudo (FIX-006). O arquivo importado passa pelo
`stripInternalKeys`, como qualquer importação.

**Importar faixas não guarda o arquivo de origem como acervo:** ele é só a fonte das faixas.

### 5. O que não muda

- O cartão no modo leitura, os filtros, a busca, os módulos, o BPM, o painel de qualidade e o «exportar .md/.json».
- A marca «usei» continua por acervo e por id: mover não a tira; renomear na importação não a herda.
- O `.json` baixado passa pelo `stripInternalKeys` e no esquema.

## Critérios de pronto (o chat mede no Chromium headless, `file://`, antes da WO)

| # | Critério |
|---|---|
| C1 | Com «editar» desligado, o cartão e a linha de origem são idênticos à 0.12.0 (mesmos botões, na mesma ordem). |
| C2 | Ligado: ↑ ↓ «mover…» «excluir» em cada cartão e «importar faixas…» na linha de origem; ↑ desligado na primeira faixa de cada álbum e ↓ na última. |
| C3 | ↑/↓ troca a ordem no rascunho; com um filtro ligado, a troca segue a ordem completa do álbum; a posição da rolagem se mantém. |
| C4 | Mover para outro álbum: a faixa vai para o fim dele; a marca «usei» e os módulos ligados vão junto. |
| C5 | Mover para «novo álbum…»: cria o álbum com `id` pelo `slug`; título repetido ganha `-2`. |
| C6 | A última faixa que sai de um álbum remove o álbum, e o toast diz isso. |
| C7 | Excluir pede confirmação; «cancelar» não muda nada; «excluir» tira a faixa e a marca dela. |
| C8 | Importar faixas, destino padrão: uma faixa exportada pela entrega 1 volta ao álbum de origem; de outro acervo, os álbuns que não existem são criados. |
| C9 | Id repetido: idêntico pula («já estavam»); diferente entra como `-2` («renomeadas»). Falso positivo: mesmo id e mesmo título com letra diferente **não** pula. |
| C10 | Módulos: o que falta entra; o idêntico não duplica; o diferente entra com sufixo e a faixa passa a citar o id novo; o citado que não existe fica e é contado. |
| C11 | Desmarcar faixas na janela de importação importa só as marcadas; «cancelar» não muda nada. |
| C12 | Cada operação soma 1 alteração; a marca «alterado: N alterações não baixadas» aparece com o modo «editar» desligado também; recarregar a página mantém o rascunho e a contagem. |
| C13 | «Baixar .json» baixa com o nome de origem, zera a contagem, e o arquivo baixado, reimportado, é igual ao rascunho e passa no esquema. |
| C14 | Esquecer e reimportar com alterações pedem confirmação; «cancelar» não muda nada; sem alterações, não pedem. |
| C15 | Fechar a aba não avisa com o rascunho gravado; avisa quando a gravação falhou (simulado). |
| C16 | Sem IndexedDB (simulado), a curadoria funciona sobre a cópia do `localStorage`. |
| C17 | Nenhuma chave `_` no rascunho nem no `.json` baixado; as chaves de outros projetos seguem intactas. |
| C18 | O cabeçalho diz `v0.13.0`; nenhum erro de página; os testes das entregas 1 e 2 continuam passando (com a versão nova). |

**Prova de vida:** o mesmo teste no app da 0.12.0 reprova (no mínimo C2 e C12).

## Fora de escopo

- **Renomear ou reordenar álbuns, editar o texto de uma faixa** (Style, Lyrics, título). Não foi pedido; cada um é
  uma ideia nova.
- **Desfazer.** O arquivo baixado da última vez é o «desfazer» grosso; um «desfazer» fino é ideia nova, se fizer falta.
- **Arrastar cartões para reordenar.** ↑ ↓ resolvem; arrastar entra na frente de interface (abaixo).
- **Gravar direto no arquivo** (i-043): o gatilho dela é esta entrega pronta.
- **A frente de interface que o dono pediu em 2026-11-05** (topo mais compacto, filtros que acompanham a rolagem,
  visões de lista e tabela, painel lateral): vem depois das funcionalidades, por pedido dele. Entra na IDEAS pela WO
  desta entrega.

## Riscos

- **Baixar e não substituir:** a contagem zera, mas o arquivo antigo continua na pasta. O toast diz o que fazer; a
  i-043 elimina o passo.
- **`changes` e o rascunho em duas abas abertas ao mesmo tempo:** vale o que gravou por último, como já acontece com as
  marcas. É raro, e o arquivo baixado continua sendo a fonte.
- **Comparação de faixa idêntica na importação:** é comparação, então o falso positivo é critério (C9).
- **Chave `_` voltando à coleção:** a curadoria é a primeira vez que o app muda a coleção desde o FIX-004. O C17 confere.
