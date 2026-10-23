# ANALISE — round-trip do acervo: o app estraga o JSON que ele mesmo baixa

> **Status:** Decidida
> **Data:** 2026-10-21 (data de criacao; nao muda depois)
> **Decidida em:** 2026-10-22 pelo dono — **A + E aprovadas, nesta ordem (E antes de A)**; C3 resolvido
> como **acervo autossuficiente (opcao 2)**. Aplicacao: `meta/workorders/261022-wo0006-roundtrip-e-refs.md`.
> O desfecho vira FIX-004, FIX-005 e DEC-016 no `meta/DECISIONS.md`; esta analise guarda o raciocinio.
> **REVISTA em 2026-10-23 — a recomendacao estava INCOMPLETA.** A conferencia na tela, depois de aplicada
> a WO 0006, mostrou que A impede o app de CRIAR a chave mas nao remove a que ja existe no arquivo lido:
> medido, entrada limpa → baixado com `0` ocorrencias; entrada ja suja → baixado com `7`. Logo o
> `album-referencias.json` abre e funciona, mas propaga as 7 chaves de download em download, e seguiria
> reprovando no esquema. O descarte da opcao C estava certo no argumento (saneamento silencioso apaga o
> sinal) e errado na conclusao: o certo era **C que AVISA**. Ver «Revisao» no fim deste documento e
> FIX-006 na WO `261023-wo0007-sanear-na-importacao.md`.

> Origem: a pergunta do dono em `../261017-2231.txt` («o que tem de errado com
> `album-referencias.json`, instrua corretamente para ensinar outro projeto, e veja o que podemos
> fazer para evitar que erros como esse nao continuem a acontecer») e a exploracao registrada em
> `../261021-1143-chat-cancioneiro-explore-app-schema-data.txt` (candidatos C1, C2 e C3).

---

## Problema

**O ciclo «Baixar .json» → «Importar .json», que a propria interface oferece em dois botoes lado a
lado, produz um arquivo que a ferramenta nao consegue mais ler.** Nao e um caso de borda: acontece
em 100% dos downloads, com qualquer acervo, sem depender de nenhuma interacao do usuario.

Quem dói: o dono, no fluxo que ele de fato usa — gerar o acervo num chat, abrir na ferramenta,
baixar, e voltar a abrir depois. O `album-referencias.json` (7 faixas, 50 modulos de estilo) e a
primeira vitima conhecida, e ficou quatro dias inutilizavel sem que a causa fosse sabida.

Pior que a falha: **a mensagem de erro aponta a causa errada.** O toast diz «Arquivo invalido: nao
e um JSON valido» sobre um arquivo cujo JSON e impecavel. Quem recebe essa mensagem vai procurar
defeito no arquivo — foi exatamente o que a pergunta de 17/10 fez — e nao no app. Esse e o segundo
problema, e e independente do primeiro: ele sobrevive a qualquer correcao do round-trip e vai
desviar a proxima investigacao tambem.

Se nada for feito: todo acervo que passar pela ferramenta vira um arquivo que so a ferramenta
produz e ninguem consome — nem ela mesma, nem o `scripts/validate.py`, nem um chat lendo o esquema.
O JSON deixa de ser o formato canonico que o DEC-001 estabeleceu e vira um despejo interno.

## Restricoes / o que foi medido

Tudo abaixo saiu de execucao real do `app/index.html` em Chromium headless (Playwright 1.56),
carregado por `file://`, acionando o `input[type=file]` do botao «Importar .json». Nada foi medido
de memoria e nada foi escrito no repositorio durante a medicao.

**A cadeia do defeito, linha por linha em `app/index.html`:**

| linha | codigo | efeito |
|---|---|---|
| 713 | `song._activeModules = active;` | grava um `Set` DENTRO do objeto da cancao, em runtime |
| 358 | `JSON.stringify(App.collection, null, 2)` | `Set` nao e serializavel: vira `{}` |
| 444 | `const active = song._activeModules \|\| new Set(...)` | `{}` e truthy: o fallback nao roda |
| 488 | `active.forEach(id => {` | `{}` nao tem `forEach` → `TypeError` |
| 316-325 | um `try` em volta de `JSON.parse` + `setCollection` + `toast` | o `TypeError` vira «nao e um JSON valido» |

**A excecao real, isolada rodando parse e carga separados dentro da pagina:**

```
JSON.parse(txt)      -> OK
setCollection(json)  -> TypeError: active.forEach is not a function
                        at recomposedStyle (app/index.html:488)
                        at renderCard      (app/index.html:637)
```

**O ciclo e completo e nao depende de interacao.** Carregando `data/demo.json` (limpo, `0/3`
faixas com a chave) e chamando o download:

```
chaves com _ no arquivo baixado : ["_activeModules"]  (nas 3 faixas)
reimportar esse arquivo         : TypeError: active.forEach is not a function
```

A linha 713 roda dentro de `renderModules`, que roda no render de **todo** cartao — nao e preciso
abrir o `<details>` dos modulos. (Isto corrige o relatorio de exploracao, que supunha a abertura do
painel como gatilho.)

**O arquivo do dono e um round-trip, nao um arquivo escrito por um chat:**

```
album-referencias.json       faixas com _activeModules: 7/7, todas com valor {}
data/demo.json                                          0/3
data/exemplo-cinzeiro.json                              0/1
```

E os dois limpos importam sem erro (toast «Acervo importado», 11 cartoes).

**A chave viola o proprio esquema do projeto.** `schema/song.schema.json` tem
`additionalProperties: false` e nao lista `_activeModules` (`grep -c "_activeModules"` nos dois
schemas → `0` e `0`). Ou seja: o arquivo que o app produz seria **reprovado pelo
`scripts/validate.py`** se estivesse em `data/`. O defeito so nao apareceu antes porque nenhum
arquivo baixado foi versionado.

**O auto-load por `https://` corre o mesmo risco, e pior.** `tryAutoLoad` chama o mesmo
`setCollection`, dentro de um `catch` que apenas «tenta o proximo caminho». Se um acervo
contaminado fosse commitado em `data/`, a versao publicada **nao mostraria erro nenhum** — a
pagina abriria vazia, em silencio. Nao reproduzi este caso (exigiria servir por HTTP e commitar um
arquivo sujo); fica como risco medido por leitura de codigo, nao por execucao.

**As tres correcoes candidatas, aplicadas numa copia fora do repositorio e medidas uma a uma:**

| | linhas de diff | download sai limpo | reimportar o proprio download | importar o arquivo JA sujo do dono |
|---|---|---|---|---|
| **A — estado fora da colecao** (`App.activeModules[song.id]`) | **5** | **sim** | **OK** | **OK — 22 cartoes** |
| B — `replacer` no `JSON.stringify` do download | 2 | sim | OK | **falha** (TypeError) |
| C — sanear na importacao (remove chaves `_`) | 9 | **nao** (continua sujando) | falha | OK — 22 cartoes |

**Teste do falso positivo em A**, porque a regra deste projeto manda testar o que NAO deve quebrar
(FIX-003): com `demo.json` carregado, 27 chips de modulo, o recomposto vai de 174 para 191
caracteres ao ligar um modulo e **continua 191 ao desligar** — identico ao original. O
«desligar nao encolhe» e o comportamento intencional («a base manda; modulos so somam»), nao
regressao. E `Object.keys(song).filter(k => k.startsWith('_'))` devolve `[]` em A contra
`["_activeModules"]` no original.

**Correcao de uma medicao minha:** na primeira rodada, C apareceu como «falha» nas tres colunas.
O teste chamava `setCollection` direto, sem passar pelo `importFromFile`, que e justamente onde C
atua — o teste media o caminho errado. Remedido pelo `input[type=file]`, C importa o arquivo do
dono normalmente. O numero errado era meu, nao da opcao.

## Opcoes consideradas

### A — Tirar o estado efemero de dentro da colecao

`App.activeModules[song.id]` em vez de `song._activeModules`. O estado dos modulos ligados passa a
viver ao lado da colecao, nunca dentro dela.

Ataca a **causa**: o dado efemero nunca entra no objeto que vai ser serializado, entao nao ha o que
limpar na saida nem o que tolerar na entrada. Alinha o codigo com o DEC-004, que ja diz que
`localStorage` guarda so estado efemero e **o arquivo e a fonte de verdade** — hoje o app faz o
contrario: mistura estado efemero no objeto canonico.

Custo: 5 linhas. Risco proprio: depende de `song.id` ser unico na colecao — medido, nenhuma
duplicata em `demo.json` nem no `album-referencias.json`, e `id` e `required` no esquema.

### B — `replacer` no `JSON.stringify` do download

Duas linhas, a menor de todas. **Descartada como correcao principal:** conserta so a saida. O
arquivo que ja esta no disco do dono continua quebrado, e qualquer outro caminho que serialize a
colecao no futuro (um export novo, um backup, um `postMessage`) volta a vazar a chave, porque a
causa — gravar estado efemero no objeto canonico — continua la. Resolve o sintoma na unica porta
que hoje existe.

### C — Sanear na importacao

Remove recursivamente as chaves com prefixo `_` ao importar. Funciona para o arquivo do dono
(medido: 22 cartoes), mas **o app continua produzindo arquivo sujo** — e o proximo consumidor nao
e o app: e o `validate.py`, um chat lendo o esquema, ou a proxima ferramenta. Descartada como
correcao principal pela mesma razao que B, do outro lado do cano.

### D — Aceitar `_activeModules` no esquema

Considerada e descartada sem medicao, por contradizer o DEC-001 e o DEC-004: tornaria canonico um
dado de interface, e o valor serializado (`{}`) nem sequer carrega a informacao que o campo
pretende guardar. Seria legitimar o defeito.

### E — Separar o `try` do parse do `try` da carga

**Nao concorre com as outras: e o segundo problema, e e independente.** Hoje:

```js
try {
  const json = JSON.parse(reader.result);
  setCollection(json);                       // todo o render mora aqui dentro
  toast("Acervo importado: " + ...);
} catch (e) {
  toast("Arquivo inválido: não é um JSON válido");
}
```

Tres operacoes, um `catch`, uma mensagem que nomeia a causa da primeira. Qualquer excecao vinda do
render e relatada como JSON invalido. Nota: `setCollection` ate tem a propria mensagem para quando
falta `albums`, mas ela e `toast` + `return`, nao `throw` — por isso o unico caminho que o `catch`
de fato cobre e o que ele descreve errado.

E a resposta direta a segunda metade da pergunta de 17/10. A regra generalizavel, candidata a virar
armadilha no CONTEXT: **`catch` que escreve uma causa especifica so pode envolver a operacao que
produz aquela causa.** E a mesma familia do FIX-003 — ali um criterio de comparacao errado falhava
em silencio; aqui uma mensagem erra sobre onde o erro nasce.

## Recomendacao

**A + E, na mesma entrega.** A conserta a causa e, de quebra, destrava o arquivo que ja esta no
disco; E faz o proximo erro se identificar sozinho em vez de mandar o dono investigar o arquivo
errado. Juntas sao ~10 linhas, todas em `app/index.html`, sem tocar esquema nem dados.

**Nao recomendo C junto.** Seria cinto e suspensorio, e tem um custo escondido: com o saneamento
silencioso na importacao, um vazamento futuro de chave interna passa a ser corrigido sem ninguem
saber que houve vazamento — some justamente o sinal que esta analise usou para achar o defeito. Se
o dono quiser a protecao assim mesmo, ela deve **avisar** («removi N campos internos deste
arquivo»), nao limpar calado.

**Pela ordem de entrega:** E primeiro, A depois. Invertido, a verificacao de A roda sob a mensagem
de erro que mente — e se algo der errado no meio, o diagnostico volta a ser enganoso.

## Riscos

- **`song.id` duplicado entre albuns** quebraria A em silencio (dois cartoes compartilhando
  estado). Medido como inexistente hoje; o sinal cedo e uma checagem no `validate.py` afirmando
  unicidade de `id` em toda a colecao — hoje o esquema exige o campo, nao a unicidade.
- **Outros pontos que leem `song._activeModules`:** medido, sao so as linhas 444 e 713. Se a
  correcao passar por uma delas e nao pela outra, o app silenciosamente perde o estado dos
  modulos. O sinal cedo e o teste do toggle: ligar um chip tem de mudar o recomposto (174 → 191).
- **Arquivos ja baixados que o dono tenha guardado fora do mount** continuam com a chave. Com A
  eles voltam a importar normalmente, mas seguem reprovando no `validate.py` se forem para
  `data/`. Vale um comando de limpeza de uma linha no relatorio da WO, nao codigo no app.
- **O auto-load por `https://` nao foi reproduzido.** Se um acervo sujo chegar a `data/`, a pagina
  publicada abre vazia sem erro. Depois de A isso deixa de poder acontecer pela via do download,
  mas a fragilidade do `catch` em `tryAutoLoad` permanece e nao esta no escopo desta analise.

## Ponto de decisao

**Aprova A + E (~10 linhas em `app/index.html`, sem mexer em esquema nem em dados), nesta ordem — E
antes de A?**

Se sim, isto vira uma WO com as duas edicoes ancoradas, mais os tres passos de verificacao ja
escritos acima (download limpo, reimport do proprio download, import do `album-referencias.json`) e
o teste do falso positivo (toggle 174 → 191). Entra como FIX-004 e FIX-005 no DECISIONS.

### Pergunta separada, que nao depende desta decisao (candidato C3)

`data/exemplo-cinzeiro.json` referencia **5 modulos que nao existem nele**
(`genre-dark-ambient`, `instr-solo-cello`, `mood-ominous`, `tempo-slow-70`, `vocal-none`):
`refs=5 · indice=0`. Os cinco existem em `schema/style-modules.json`, mas `setCollection` monta
`App.modulesById` **so** a partir da colecao carregada — entao hoje esses ids nao resolvem para
fragmento nenhum, em silencio.

O arquivo foi escrito supondo uma biblioteca compartilhada que o app nao carrega. Duas leituras, com
consertos opostos:

1. **A biblioteca e compartilhada** e o app deveria carregar `schema/style-modules.json` junto de
   qualquer acervo. Entao `exemplo-cinzeiro.json` esta CERTO e falta codigo. Vantagem: uma
   biblioteca so, curada, e acervos menores. Custo: o acervo deixa de ser autocontido — um `.json`
   sozinho nao basta para reproduzir o prompt.
2. **Cada colecao traz os seus modulos** (como `demo.json` e o `album-referencias.json` fazem, com
   27 e 50). Entao `exemplo-cinzeiro.json` esta INCOMPLETO e falta dado. Vantagem: o arquivo e
   autossuficiente, que e o espirito do DEC-001. Custo: duplicacao da biblioteca em cada acervo.

**Nao recomendo nenhuma das duas aqui** — e decisao de arquitetura do esquema, nao conserto de bug,
e muda o que «um acervo» significa. Em qualquer dos dois caminhos, a checagem determinista que
captura isto e a mesma e cabe no `validate.py`: **todo id em `songs[].styleModules` resolve em
algum indice**. Ela nao existe hoje porque JSON Schema nao faz referencia cruzada — e e o exemplo
exato do que «a validacao nao faz».

**Pergunta:** biblioteca compartilhada carregada pelo app (1), ou cada acervo autossuficiente (2)?

**RESPONDIDA em 2026-10-22: opcao 2 — cada acervo e autossuficiente.** Logo,
`data/exemplo-cinzeiro.json` esta **incompleto**, e o conserto e de DADO, nao de codigo: os cinco
modulos entram no proprio arquivo, copiados de `schema/style-modules.json`, que passa a ser
**biblioteca de referencia para autoria** (de onde se copia ao montar um acervo), nao indice que o
app carrega em tempo de execucao. A checagem determinista entra no `scripts/validate.py` com a
semantica agora definida: todo id em `songs[].styleModules` resolve no `styleModules[]` da PROPRIA
colecao. Medida antes e depois numa copia, fora do repositorio:

```
antes:  ERRO de referencia em data/exemplo-cinzeiro.json (5 id(s) de modulo sem indice)  -> exit 1
depois: OK (refs)  data/exemplo-cinzeiro.json                                            -> exit 0
```

---

## Revisao — 2026-10-23: a lacuna que a conferencia na tela revelou

**O que a recomendacao original nao previu.** A + E foram aplicadas e funcionam: o app nao grava mais
`_activeModules`, o arquivo quebrado voltou a abrir (22 cartoes), o ciclo baixar→reimportar fecha, e o
toggle de modulo continua igual. O que faltou perguntar foi o que acontece com a sujeira **que ja
existia no arquivo**. Medido depois de aplicar, com o app corrigido:

```
demo.json              (entrada limpa)  ->  entrada: 0  |  baixado: 0
album-referencias.json (entrada suja)   ->  entrada: 7  |  baixado: 7
```

O app le o JSON, nunca toca na chave, e a serializa de volta. Nao quebra mais — mas o arquivo carrega
as 7 chaves indefinidamente, e `song.schema.json` tem `additionalProperties: false`, entao ele
reprovaria no `validate.py` se fosse para `data/`.

**Por que o erro aconteceu, para nao repetir:** a analise mediu as tres opcoes contra «o ciclo volta a
funcionar?» e nenhuma contra «o dado existente fica limpo?». As duas perguntas parecem a mesma quando se
olha so o sintoma. E a prova disso esta na propria tabela de medicao original: a coluna «importar o
arquivo JA sujo do dono» marcava **C como a unica que passava** por um caminho que A nao cobria — o
dado ficou certo, a leitura dele foi que juntou as duas colunas numa so.

**Revisao da recomendacao:** acrescentar **C que avisa** — sanear as chaves com prefixo `_` na
importacao, **dizendo quantas removeu**, nunca em silencio. O argumento original contra C continua de
pe: saneamento mudo apaga o sinal que permitiu achar este defeito. O remedio nao era descartar C, era
dar voz a ela. Vira **FIX-006**.

**O que isto NAO muda:** FIX-004 e FIX-005 continuam corretos e necessarios. C sozinha nunca teria sido
suficiente — ela conserta a entrada, nao a causa, e o app continuaria sujando todo arquivo que tocasse.
A ordem A → C e a certa; invertida, so se trocaria um defeito pelo outro.
