# ANALISE — Curadoria no app e mais de um acervo (i-040, i-041)

> **Status:** Decidida — pelo dono em 2026-11-02: F1 + G1, entregas 1 → 2 → 3, o `.json` curado manda sobre os
> conversores (DEC-028). Entrega 1: spec `meta/specs/261102-exportar-faixa-json.md`, WO 0022 (0.11.0).
> **Data:** 2026-11-02 (data de criação; não muda depois)
> **Ideias de origem:** i-040 (excluir, exportar, importar, reordenar e mover faixas) e i-041 (mais de um acervo
> guardado no navegador), da nota `../notas-arquivadas/261029-1825.txt`.
> **Toca:** DEC-004 (o arquivo é a fonte de verdade) e DEC-022 (o navegador guarda só o último acervo, como cache).

## Problema

O dono quer **curar o acervo pela tela**: tirar faixa, trazer faixa de outro álbum ou de outro `.json`, mudar a
ordem, mandar uma faixa sozinha como `.json`. Hoje o app é **leitor**: nada disso existe. O reagrupamento da i-038
foi feito por mapa e script (`scripts/convert_guides.py` + `../acervos/albuns-grupos.json`), o que só o Code roda.

O segundo atrito é trocar de acervo. São três em uso: a Rainha da Preguiça, os 12 álbuns e o de referências. O
navegador guarda só o último importado (DEC-022), então cada troca é uma nova importação.

Se nada for feito, cada mudança de curadoria vira pedido ao chat e WO ao Code. O acervo, que é o diferencial do
projeto (organizar o acervo próprio, `CONTEXT.md`), fica caro de mexer.

**O que torna isto não-trivial:** editar no app cria um acervo que, até o dono baixá-lo, **só existe no
navegador**. É exatamente o que a DEC-004 proíbe tratar como verdade. A consequência positiva da DEC-022, «o app
nunca edita o acervo, então a cópia é igual ao arquivo», deixa de valer.

## Restrições / o que foi medido

**Tamanho dos acervos** (`json.dumps` sem indentação, em caracteres, que é o formato que a cópia do navegador
grava; medido em 2026-11-02 na pasta-pai):

| Acervo | Álbuns | Faixas | Módulos | Caracteres |
|---|---|---|---|---|
| `acervos/rainha-da-preguica.json` | 10 | 151 | 0 | 959.619 |
| `acervos/albuns-reagrupados.json` | 12 | 205 | 0 | 428.136 |
| `album-referencias (1).json` | 1 | 7 | 50 | 22.429 |
| **Os três juntos** | | | | **1.410.184** |

**Cota do `localStorage`: não há número único.**
- Teste publicado em Chrome e Firefox: ~5,24 milhões de caracteres por origem.
- Outras fontes (Web Storage, cálculo em UTF-16): ~2,5 milhões.
- Safari: cerca de metade.

Com os três acervos (1,41 milhão), a folga vai de ~1,8× a ~3,7×. Não cabe um quarto acervo do tamanho da Rainha
no cenário pessimista. **A sonda mede o número real no navegador do dono** (abaixo).

**A origem no Pages é compartilhada.** `joaolucas-nds.github.io` é uma origem só para todos os repositórios desse
usuário publicados ali. Qualquer outro projeto dele no Pages gasta a mesma cota. No `file://`, a origem é outra
(o mesmo acervo não aparece nos dois modos; já é assim hoje).

**IndexedDB:** a cota é uma fração grande do disco livre, compartilhada com o cache. A API é assíncrona; a
abertura do app (`boot`) já tem ramo assíncrono (`tryAutoLoad`). Não está medido se funciona no `file://` no
navegador do dono: é a primeira pergunta da sonda.

**Gravar direto no arquivo (File System Access):** `showSaveFilePicker` existe no Chrome e no Edge desde a versão
86 e não existe no Firefox nem no Safari (web.dev, atualizado em 2026-07-29). Com ela, o app abriria o `.json` e
gravaria de volta no mesmo arquivo. Sem ela, salvar é sempre «Baixar», que cai em Downloads.

**Ids colidem entre acervos, e as marcas «usei» são guardadas por id, sem acervo** (`cancioneiro:ui`,
`App.ui.used[id]`). Medido: `brv-04` existe na Rainha e no `data/demo.json`; `cinzeiro-01` existe no demo e no
`exemplo-cinzeiro`. Hoje, marcar `brv-04` num acervo já marca no outro. É um defeito latente que a i-041 tornaria
cotidiano.

**Módulos repetidos entre acervos têm o mesmo conteúdo** (medido: os 27 do demo e os 5 do Cinzeiro reaparecem no
de referências com o mesmo id e o mesmo texto; 0 conflitos). Importar faixa com módulo hoje não produz conflito
real; a regra de conflito é para o futuro.

**O esquema já comporta uma faixa sozinha:** coleção exige `schemaVersion`, `title` e `albums`; álbum exige `id`,
`title` e `songs`. Uma coleção com um álbum, uma faixa e os módulos que ela cita é um acervo válido e importa
sem nada novo. Já um campo `id` na coleção exigiria mudar o esquema (`additionalProperties: false`).

**Os acervos convertidos têm duas origens.** `albuns-reagrupados.json` é gerado de novo sempre que o
`convert_guides.py` roda sobre os guias e o mapa. Se o dono curar o `.json` no app e o conversor rodar depois, a
curadoria se perde.

## Opções consideradas

### Quem é a fonte de verdade quando o app edita

**F1 — O arquivo continua sendo a fonte; a edição vive num rascunho marcado no navegador.** (recomendada)
Cada operação de curadoria muda a cópia guardada, que passa a mostrar «alterado desde a importação · N mudanças ·
Baixar .json». Baixar zera a marca. «Esquecer», reimportar o mesmo arquivo ou fechar a aba com mudanças não
baixadas pedem confirmação. A DEC-004 continua de pé: o rascunho é rascunho, e o app diz isso o tempo todo.
- Contra: o dono ainda precisa baixar e pôr o arquivo no lugar.
- Contra: rascunho esquecido por meses some se o navegador limpar dados.

**F2 — Toda operação baixa o arquivo na hora, sem estado no navegador.** Descartada: dez exclusões dão dez
arquivos em Downloads, e o atrito que motivou a i-040 volta.

**F3 — O navegador vira a fonte (inverte a DEC-004).** Descartada pelo mesmo motivo da DEC-004, agora com 1,4
milhão de caracteres em jogo: limpar o navegador ou trocar de perfil apaga o acervo, e nada é versionável.

**F4 — Gravar direto no arquivo original (File System Access).** É a melhor experiência: abrir, editar, «Salvar»
e o arquivo na pasta já é o novo. Não serve como base agora:
- só funciona no Chrome e no Edge;
- a permissão é pedida de novo a cada sessão;
- nada está medido no `file://` do dono.

Entra **depois de F1, como melhoria**: um botão «Salvar no arquivo» onde a API existir, com «Baixar» onde não.
Gatilho: a sonda mostrar que a API existe no navegador do dono.

### Onde guardar mais de um acervo

**G1 — IndexedDB para os acervos; `localStorage` só para marcas e estrutura do cartão.** (recomendada)
- A favor: a cota folga e não é dividida com os outros projetos no Pages nos mesmos 5 MB.
- A favor: cada acervo é um registro, e o rascunho da F1 entra sem dobrar o espaço.
- A favor: `navigator.storage.persist()` pede ao navegador que não descarte os dados.
- Contra: a abertura passa a ser assíncrona, e há uma migração única da chave `cancioneiro:acervo`.

**G2 — Continuar no `localStorage`, um registro por acervo.** Descartada: os três de hoje já ocupam de 27% a 54%
da cota, que é dividida com o resto do Pages. A falha (`QuotaExceededError`) chegaria no quarto acervo e
apareceria como «não guardado» na importação.

**Identidade do acervo, sem mudar o esquema:** a chave é o **nome do arquivo** importado. Reimportar
`albuns-reagrupados.json` substitui o acervo do mesmo nome, com confirmação se houver rascunho não baixado; não
cria um segundo. O título vai na lista só para leitura. Um `id` no esquema foi descartado: muda o contrato que os
chats seguem por um ganho que o nome do arquivo já dá.

**Marcas «usei» por acervo:** a chave passa a ser acervo + id. Migração: cada marca antiga é copiada para todo
acervo guardado que tem aquele id. Nos dois ids que colidem hoje, a marca vai para os dois, que é o comportamento
atual; nada se perde.

### As operações de curadoria

| Operação | Como | Regra que precisa existir |
|---|---|---|
| Exportar faixa como `.json` | Botão ao lado do «.md» da faixa | Coleção com um álbum (id e título do álbum de origem), a faixa e **os módulos que ela cita**. Grava o dado guardado, não o Style da tela (igual ao «Baixar .json»). Não toca a fonte de verdade. |
| Excluir faixa | Botão no cartão, com confirmação | Entra no rascunho. A marca «usei» da faixa sai junto. |
| Reordenar | ↑ ↓ no cartão (arrastar fica para depois) | Entra no rascunho. |
| Mover para outro álbum | Menu «mover para…» com os álbuns do acervo e «novo álbum» | Novo álbum pede título; o id sai do título (`slug`) e, se já existir, ganha sufixo. |
| Importar faixas | «Importar faixas…» abre outro `.json`, lista as faixas com caixa de seleção (todas marcadas) e pergunta o álbum de destino | **Id repetido:** se o conteúdo for idêntico, pula e conta; se for diferente, entra com sufixo (`-2`) e o aviso diz quantas foram renomeadas. **Módulo citado:** o que falta entra; mesmo id e mesmo texto, pula; mesmo id e texto diferente, entra com sufixo e a faixa importada passa a citar o novo id. O toast conta cada caso (sem saneamento mudo, FIX-006). |

O reagrupamento da i-038 passa a ser possível pela tela (mover + novo álbum). O mapa de grupos continua valendo
para quem regenera pelos guias. Depois da primeira curadoria no app, quem manda é o `.json`.

### Fazer pela tela ou continuar por script

**S0 — Não fazer; seguir curando por mapa e script.** Descartada: tudo depende do Code, e o próprio dono pediu
para fazer pela tela. A ideia não empurra o projeto para gerador genérico de prompt (armadilha do `CONTEXT.md`):
curar o acervo próprio é o diferencial.

## Recomendação

**F1 + G1, em três entregas, nesta ordem:**

1. **Exportar faixa como `.json`** (inclui os módulos citados). Não mexe na fonte de verdade nem no armazenamento.
   É útil sozinha já (mandar uma faixa para um chat ou outro acervo), e o formato que ela define é o que o
   «Importar faixas» da entrega 3 vai ler.
2. **Mais de um acervo (i-041):**
   - IndexedDB para os acervos;
   - lista «Acervos neste navegador» (abrir, esquecer um, data de importação);
   - chave pelo nome do arquivo;
   - marcas «usei» por acervo, com a migração;
   - `storage.persist()`.
   Corrige de passagem a colisão das marcas. Ainda sem edição.
3. **Curadoria (i-040):** rascunho marcado (F1) com excluir, reordenar, mover, novo álbum e importar faixas, com as
   regras da tabela. Aviso ao fechar a aba com mudança não baixada.

**Gravar direto no arquivo (F4)** fica como ideia com gatilho, para depois da entrega 3.

**Por que esta ordem:** cada entrega é usável sozinha e a de menor risco vem primeiro. A 2 cria o lugar onde o
rascunho da 3 mora. Juntar 2 e 3 numa WO só misturaria a migração do armazenamento com a mudança de papel do app:
se algo der errado, não daria para saber qual das duas causou.

**Registro que a decisão gera:** uma DEC que amplia a DEC-004 e substitui a consequência «o app nunca edita» da
DEC-022. O texto dela: «o app edita um rascunho; o arquivo baixado é a fonte; depois da primeira curadoria pela
tela, o `.json` manda e os conversores não rodam mais sobre aquele acervo».

## Riscos

- **Rascunho perdido.** O dono edita, não baixa e o navegador limpa os dados. Sinais e defesas: a marca
  «alterado · N mudanças» visível o tempo todo, o aviso ao fechar a aba e o `storage.persist()`. A spec deve dizer
  o que acontece quando a persistência é negada.
- **Conversor sobrescreve curadoria.** Rodar `convert_guides.py` de novo apaga o que foi curado no app. Defesa: a
  DEC acima, mais uma linha no `kit-musica/README.md` ou no cabeçalho do conversor dizendo que ele é para a
  primeira geração.
- **Renomear id na importação quebra a marca «usei»** da faixa importada. É aceitável: é outra faixa até prova em
  contrário. O aviso conta as renomeadas.
- **Comparação de «conteúdo idêntico» na importação.** É comparação, então vale a regra do projeto: testar o
  falso positivo. Duas faixas com o mesmo id e o mesmo título, mas letras diferentes, **não** podem ser puladas
  (é o caso «Rise of the Eternal»). A comparação é do objeto inteiro serializado, nunca do título.
- **Chave `_` voltando à coleção.** A edição mexe na coleção pela primeira vez desde o FIX-004. O rascunho e o
  «Baixar» passam pelo `stripInternalKeys`, e o teste da entrega 3 confere que o `.json` baixado não tem chave
  `_`.
- **Migração do `localStorage` para o IndexedDB.** A cópia antiga só é apagada depois que a nova for lida de
  volta com sucesso. Se o IndexedDB falhar (por exemplo, no `file://`), o app segue no modo de hoje, um acervo no
  `localStorage`, e avisa. A sonda diz se esse ramo vai ser o comum.

**Comando que audita a entrega 2 (para a spec):** no console do navegador,
`indexedDB.databases().then(console.log)` mostra o banco do Cancioneiro, e
`Object.keys(localStorage).filter(k => k.startsWith("cancioneiro:"))` não deve mais listar `cancioneiro:acervo`
depois da migração.

## Sonda (antes da spec da entrega 2)

`../261102-sonda-armazenamento.html` (pasta-pai, fora do Git). Abrir com duplo clique, clicar em «Medir» e em
«Baixar relatório», e mover o `.txt` de Downloads para a pasta-pai. Ela mede no navegador do dono:
- o protocolo;
- o `localStorage` usado, livre e total, em caracteres;
- se o IndexedDB grava e lê 1,5 milhão de caracteres;
- a cota estimada;
- se o armazenamento é persistente;
- se a gravação direta no arquivo existe.

Usa só chaves `sonda:` e apaga o que gravou. A entrega 1 não depende dela.

## Ponto de decisão

**Aprova F1 + G1 nas três entregas, na ordem 1 → 2 → 3, com a regra de que o `.json` curado no app passa a mandar
sobre os conversores?**

Se sim, o próximo passo é a spec da entrega 1, que é curta, e a WO dela. A sonda pode rodar em paralelo.
Alternativas que mudam o plano:
- (b) ir direto à F4, gravar no arquivo, aceitando só Chrome/Edge;
- (c) parar na entrega 2, sem edição pela tela.

## Desfecho — 2026-11-02

Decidida pelo dono como recomendada: **F1 + G1, nas três entregas, na ordem 1 → 2 → 3, com o `.json` curado
mandando sobre os conversores**. Registrada na DEC-028, que amplia a DEC-004 e revê a consequência «a cópia é
igual ao arquivo» da DEC-022. A F4 (gravar direto no arquivo) virou a i-043, com gatilho depois da entrega 3.

- **Entrega 1 — exportar faixa como `.json`:** spec `meta/specs/261102-exportar-faixa-json.md`, aplicada pela
  WO 0022 (0.11.0). 15 de 15 critérios no Chromium headless.
- **Entrega 2 — vários acervos:** espera o relatório da sonda `../261102-sonda-armazenamento.html` para a spec.
- **Entrega 3 — curadoria pela tela:** depois da 2.
