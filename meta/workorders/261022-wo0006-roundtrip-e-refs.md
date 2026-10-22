# WO 0006 — Conserta o round-trip do acervo, a mensagem de erro que mente, e as referencias de modulo

## Cabecalho

> **Tipo:** WO de CODIGO (app + instrumento) e de DADO. Os registros em `meta/` vao junto.
> **Config sugerida:** Sonnet · `/effort medium`. Edicoes ancoradas e medidas, mas mexem em codigo: o `git diff` e a validacao sao rede de verdade aqui, nao formalidade.
> **Pre-requisito:** commit `cb78583`, branch `main`, sincronizada com `origin/main`. **A arvore NAO esta limpa:** `meta/CONTEXT.md` esta modificado e `meta/analises/` e nova, ambos gravados pelo chat (ver abaixo). Nada mais deve aparecer no `git status`.
> **Base:** `meta/analises/261021-ANALISE-roundtrip-do-acervo.md`, Status **Decidida** em 2026-10-22. Exploracao de origem: `../261021-1143-chat-cancioneiro-explore-app-schema-data.txt`. Pergunta que disparou tudo: `../261017-2231.txt`.
> **Depende de:** WO 0005, ja aplicada.
>
> **Arquivos que o chat gravou no disco e esta WO versiona** (sha1sum medido pelo chat ao gravar):
> - `meta/analises/261021-ANALISE-roundtrip-do-acervo.md` — `2350fa349f54b27992f24e0af55340227a6b4696`
> - `meta/analises/_TEMPLATE.md` — `34bf231057d93f82c024cb073b16958de276788c`
> - `meta/CONTEXT.md` — `fb95d2a1e94e5663c596f302a0cc225745447aa2`
>
> **Ancora semantica:** se um trecho-ancora nao bater EXATAMENTE, PARE e reporte.
> **Idempotencia:** antes de cada insercao, procure a frase-chave do texto NOVO; se ja existir, PULE e diga no relatorio.
>
> **Ancoras lidas em:** trechos lidos pelo chat no turno de 2026-10-22, direto do disco:
> - `app/index.html` linha 252-256, o bloco `const App = {` ate `};`
> - `app/index.html` linha 444: `  const active = song._activeModules || new Set(song.styleModules || []);`
> - `app/index.html` linha 713: `  song._activeModules = active;`
> - `app/index.html` linhas 315-325, o `try`/`catch` de `importFromFile`
> - `scripts/validate.py` linhas 83-93, o bloco `errs = sorted(validator.iter_errors(data) ...)`
> - `data/exemplo-cinzeiro.json`, a linha `  "targetTool": "suno",` e a linha `  "albums": [`
> - `meta/DECISIONS.md`, ultima linha do arquivo (fim de DEC-015)
> - `meta/STATUS.md` linha 10: `## Última conversa (2026-10-20, kit v1.127.0 — fatias 1 a 4)`
> - `meta/IDEAS.md` linha 79, o item `### i-024 💡 Molde para o projeto gerar skill de estilo proprio`

---

## 1. Por que

O ciclo «Baixar .json» → «Importar .json», que a interface oferece em dois botoes lado a lado,
produz um arquivo que a ferramenta nao consegue mais ler. Acontece em **100% dos downloads**, com
qualquer acervo, sem depender de interacao. O `album-referencias.json` do dono (7 faixas, 50
modulos) ficou cinco dias inutilizavel por causa disso.

E a mensagem de erro aponta a causa errada: diz «nao e um JSON valido» sobre um arquivo cujo JSON e
impecavel — foi o que mandou a investigacao de 17/10 procurar defeito no arquivo em vez de no app.

Esta WO aplica as duas correcoes aprovadas (**E** antes de **A**, nesta ordem), conserta o dado que
a decisao do C3 tornou incompleto, e deixa a checagem determinista que impede a volta do terceiro.

## 2. Ordem das edicoes — e por que ela e a regra

**A Edicao 1 (E) vem antes da Edicao 2 (A).** Invertido, a verificacao de A roda sob a mensagem de
erro que mente: se algo der errado no meio, o diagnostico volta a ser enganoso. Esta e a unica
ordenacao obrigatoria; o resto pode ser aplicado como fizer sentido.

## Edicao 0 — Conferencia de hash e de arvore

```
sha1sum meta/analises/261021-ANALISE-roundtrip-do-acervo.md meta/analises/_TEMPLATE.md meta/CONTEXT.md
GIT_OPTIONAL_LOCKS=0 git status --short
```

Os tres hashes batem com o cabecalho, e o `git status` mostra **exatamente** `M meta/CONTEXT.md` e
`?? meta/analises/`. Qualquer outra coisa: **PARE e reporte** — ha outro escritor.

## Edicao 1 (E) — `app/index.html` · separar o `try` do parse do `try` da carga

**Ancora** (em `importFromFile`, por volta da linha 315). Texto literal a substituir:

```js
    try {
      const json = JSON.parse(reader.result);
      setCollection(json);
      toast("Acervo importado: " + (json.title || file.name));
    } catch (e) {
      toast("Arquivo inválido: não é um JSON válido");
    }
```

**Texto novo, literal:**

```js
    // Dois try separados de proposito: um catch que nomeia uma causa especifica
    // so pode envolver a operacao que produz aquela causa (ver FIX-005).
    let json;
    try {
      json = JSON.parse(reader.result);
    } catch (e) {
      toast("Arquivo inválido: não é um JSON válido");
      return;
    }
    try {
      setCollection(json);
      toast("Acervo importado: " + (json.title || file.name));
    } catch (e) {
      toast("Não consegui carregar o acervo: " + e.message);
      console.error("[cancioneiro] falha em setCollection:", e);
    }
```

## Edicao 2 (A) — `app/index.html` · tirar o estado efemero de dentro da colecao

**2a — declarar o estado no `App`.** Ancora, linhas 252-256:

```js
const App = {
  collection: null,       // o acervo carregado (objeto do JSON)
```

Texto novo, literal (as duas linhas de comentario e a chave entram logo apos `const App = {`):

```js
const App = {
  // Estado efemero dos modulos ligados, por song.id. NUNCA dentro da colecao:
  // o que esta na colecao e serializado pelo "Baixar .json" (ver FIX-004).
  activeModules: {},
  collection: null,       // o acervo carregado (objeto do JSON)
```

**2b — ler de fora da colecao.** Ancora, linha 444, substituir a linha inteira:

```js
  const active = song._activeModules || new Set(song.styleModules || []);
```

por:

```js
  const active = App.activeModules[song.id] || new Set(song.styleModules || []);
```

**2c — gravar fora da colecao.** Ancora, linha 713, substituir a linha inteira:

```js
  song._activeModules = active;
```

por:

```js
  App.activeModules[song.id] = active;
```

**As tres subedicoes sao indivisiveis.** Aplicar 2b sem 2c (ou o contrario) faz o app perder o
estado dos modulos em silencio — ligar um chip nao muda mais o recomposto. Se uma das tres ancoras
nao bater, **PARE e nao aplique nenhuma das outras duas.** Medido: `grep -c "_activeModules"
app/index.html` deve dar `2` ANTES e `0` DEPOIS — nao ha terceiro ponto.

## Edicao 3 (C3) — `data/exemplo-cinzeiro.json` · os cinco modulos que faltam

Decisao do dono: **acervo autossuficiente**. O arquivo cita cinco modulos que nao existem nele; os
cinco entram, copiados de `schema/style-modules.json` sem alteracao.

**Ancora:** a linha `  "targetTool": "suno",`, seguida da linha `  "albums": [`. Insira o bloco
**entre as duas** (a ordem segue o `collection.schema.json`: `styleModules` antes de `albums`).

**Texto a inserir, literal:**

```json
  "styleModules": [
    {
      "id": "genre-dark-ambient",
      "category": "genre",
      "label": "Dark ambient",
      "fragment": "dark ambient cinematic",
      "notes": "Atmosferico, sem pulso definido. Base de exploracao."
    },
    {
      "id": "instr-solo-cello",
      "category": "instrument",
      "label": "Cello solo",
      "fragment": "solo cello",
      "notes": "Cello sozinho, expressivo."
    },
    {
      "id": "mood-ominous",
      "category": "mood",
      "label": "Ameacador",
      "fragment": "ominous, dark",
      "notes": "Tensao/ameaca. Dark ambient, industrial."
    },
    {
      "id": "tempo-slow-70",
      "category": "tempo",
      "label": "Lento ~70 BPM",
      "fragment": "slow tempo 70 bpm",
      "notes": "Use junto do campo bpm. BPM e aproximacao no Suno."
    },
    {
      "id": "vocal-none",
      "category": "vocal",
      "label": "Sem vocal",
      "fragment": "no vocals",
      "notes": "Reforco redundante ao [Instrumental] no Lyrics. Sempre em faixa instrumental."
    }
  ],
```

Os cinco estao na ordem em que a faixa `cinzeiro-01` os cita. **Nao reformate o resto do arquivo**:
a indentacao e de 2 espacos e o arquivo termina com uma linha em branco.

## Edicao 4 — `scripts/validate.py` · integridade referencial

JSON Schema nao faz referencia cruzada: id orfao passa na validacao estrutural e vira fragmento
silenciosamente ausente na ferramenta. Esta e a checagem que captura a classe inteira.

**4a — a funcao.** Ancora: a linha `def main(argv):`. Insira ANTES dela, deixando uma linha em
branco entre o fim do bloco novo e o `def main(argv):`:

```python
def check_module_refs(data, rel):
    """Todo id em songs[].styleModules resolve no styleModules[] da propria colecao.

    JSON Schema nao faz referencia cruzada: id orfao passa na validacao estrutural
    e vira fragmento silenciosamente ausente na ferramenta (ver DEC-016).
    """
    index = {m.get("id") for m in data.get("styleModules", []) if isinstance(m, dict)}
    orphans = []
    for album in data.get("albums", []):
        for song in album.get("songs", []):
            for mid in song.get("styleModules", []) or []:
                if mid not in index:
                    orphans.append((album.get("id", "?"), song.get("id", "?"), mid))
    if orphans:
        print(f"ERRO de referencia em {rel} ({len(orphans)} id(s) de modulo sem indice):")
        for a, s, mid in orphans[:8]:
            print(f"   [{a} > {s}] styleModules: '{mid}' nao existe em styleModules[]")
        return 1
    return 0
```

**4b — chamar a funcao.** Ancora, no laco `for path in targets:`, o bloco literal:

```python
        else:
            n_songs = sum(len(a.get("songs", [])) for a in data.get("albums", []))
            print(f"OK  {rel}  ({len(data.get('albums', []))} álbuns, {n_songs} faixas)")
```

Texto novo, literal:

```python
        else:
            n_songs = sum(len(a.get("songs", [])) for a in data.get("albums", []))
            print(f"OK  {rel}  ({len(data.get('albums', []))} álbuns, {n_songs} faixas)")

        # referencia cruzada: o schema nao alcanca isto
        errors += check_module_refs(data, rel)
```

**Repare onde o `errors +=` fica:** FORA do `else`, no mesmo nivel do `if errs:` / `else:`. A
checagem de referencia roda **mesmo quando o schema reprovou** — sao defeitos independentes, e
esconder o segundo atras do primeiro e o que faz uma correcao revelar outra falha so na rodada
seguinte. Se a indentacao cair dentro do `else`, o comportamento muda em silencio: confira com a
checagem 9 abaixo, que e justamente o caso negativo.

## Edicao 5 — `meta/DECISIONS.md` · dois FIX e uma DEC

**Ancora:** a ULTIMA linha do arquivo (fim de DEC-015). Insira DEPOIS dela, precedido de uma linha
em branco e de `---`.

```
---

## FIX-004 — O app gravava estado de interface dentro da colecao, e o download o serializava

**Data:** 2026-10-22
**Sintoma:** Importar um acervo baixado pela propria ferramenta mostrava «Arquivo invalido: nao e um JSON valido», sobre um arquivo cujo JSON era impecavel. O `album-referencias.json` do dono ficou cinco dias inutilizavel.

**Causa raiz:** `renderModules` gravava `song._activeModules = active` — um `Set` — dentro do objeto da cancao (linha 713). `JSON.stringify` nao serializa `Set`: grava `{}`. Na importacao seguinte, `recomposedStyle` lia `song._activeModules || new Set(...)` (linha 444); `{}` e truthy, o fallback nao rodava, e `{}.forEach` lancava `TypeError: active.forEach is not a function`. O ciclo era completo: o app sujava o arquivo que ele mesmo baixava e depois nao conseguia le-lo. Rodava no render de TODO cartao, nao so ao abrir o painel de modulos.

**Solucao:** O estado efemero dos modulos ligados passa a viver em `App.activeModules[song.id]`, fora da colecao. Alinha o codigo com o DEC-004, que ja dizia que o arquivo e a fonte de verdade e o estado efemero mora a parte — o app fazia o contrario. Medido numa copia antes de aplicar: download sai sem chave interna, reimport do proprio download OK, e o arquivo ja sujo do dono importa (22 cartoes). Teste do falso positivo: 27 chips, recomposto 174 → 191 ao ligar e 191 ao desligar, identico ao original (desligar nao encolhe e intencional — a base manda).

**Licao:** Dado de interface gravado no objeto canonico vaza na primeira serializacao. `Set` e `Map` agravam porque viram `{}` em vez de falhar: o defeito nao aparece onde nasce.

---

## FIX-005 — Um `catch` largo atribuia a qualquer falha a causa da primeira operacao

**Data:** 2026-10-22
**Sintoma:** Todo erro de importacao era relatado como «nao e um JSON valido», inclusive os que nada tinham a ver com parse. A mensagem mandou a investigacao de 2026-10-17 procurar defeito no arquivo durante cinco dias, enquanto o defeito estava no app.

**Causa raiz:** `importFromFile` envolvia tres operacoes num unico `try` — `JSON.parse`, `setCollection` (que carrega E renderiza) e o `toast` de sucesso — com um `catch` que nomeava a causa da primeira. Qualquer excecao do render chegava ao usuario como JSON invalido. `setCollection` ate tinha a propria mensagem para quando falta `albums`, mas e `toast` + `return`, nao `throw`: por isso o unico caminho que o `catch` de fato cobria era o que ele descrevia errado.

**Solucao:** Dois `try` separados. O do parse mantem a mensagem, que ali e verdadeira (medido: JSON realmente malformado continua dizendo «nao e um JSON valido»); o da carga reporta `e.message` e loga a excecao no console.

**A mesma classe, achada em outro arquivo na auditoria desta WO:** `scripts/validate.py` imprimia «Tudo conforme ao esquema.» mesmo rodando sem o pacote `jsonschema`, isto e, sem ter conferido esquema nenhum — ele avisa na PRIMEIRA linha e afirma conformidade na ULTIMA, que e a que se le. Medido no disco do dono em 2026-10-22: o pacote nao esta instalado, entao todo «verde» do instrumento ate aqui foi verde de sintaxe. Corrigido na mesma entrega: a mensagem final declara o modo, e o aviso se repete no fim.

**Licao:** mensagem que nomeia um resultado so pode ser escrita pela operacao que produz aquele resultado — vale para `catch` e para rodape de relatorio. Mesma familia do FIX-003: la um criterio de comparacao errado falhava em silencio; aqui uma mensagem erra sobre o que foi medido. Mensagem errada custa mais que erro mudo, porque desvia quem investiga: foram cinco dias no app e, no instrumento, um numero indeterminado de «OK» lidos como conformidade.

---

## DEC-016 — Acervo autossuficiente: cada colecao carrega os proprios modulos de estilo

**Data:** 2026-10-22
**Contexto:** `data/exemplo-cinzeiro.json` referenciava cinco modulos (`genre-dark-ambient`, `instr-solo-cello`, `mood-ominous`, `tempo-slow-70`, `vocal-none`) que nao existiam nele — medido: `refs=5 · indice=0`. Os cinco existem em `schema/style-modules.json`, mas `setCollection` monta `App.modulesById` so a partir da colecao carregada, entao os ids nao resolviam para fragmento nenhum, em silencio. O arquivo fora escrito supondo uma biblioteca compartilhada que o app nao carrega. Duas leituras com consertos opostos: biblioteca compartilhada (o arquivo esta certo, falta codigo) ou acervo autossuficiente (o arquivo esta incompleto, falta dado).

**Decisao:** **Acervo autossuficiente.** Toda colecao traz em `styleModules[]` os modulos que suas faixas citam, como `data/demo.json` (27) e o `album-referencias.json` (50) ja faziam. `schema/style-modules.json` passa a ser **biblioteca de referencia para autoria** — de onde se copia ao montar um acervo —, nao indice carregado em tempo de execucao. Um `.json` sozinho basta para reproduzir o prompt.

**Alternativas consideradas:** biblioteca compartilhada carregada pelo app — descartada: tornaria o acervo dependente de um segundo arquivo, contra o espirito do DEC-001 (o JSON e o dado canonico, completo em si).

**Consequencias:** (+) Um acervo e reproduzivel sozinho, inclusive fora deste repositorio. (+) A checagem de integridade referencial ganha semantica definida e entra no `validate.py`. (−) A biblioteca se duplica em cada acervo; quando um fragmento for corrigido na biblioteca, os acervos ja montados nao mudam sozinhos. Mitigacao aceita: a biblioteca e de autoria, nao de runtime — divergencia e esperada e registrada no proprio acervo.
```

## Edicao 6 — `meta/STATUS.md` e `meta/IDEAS.md`

A cargo do `/wrap`, em append. Para o STATUS, o bloco da conversa de 2026-10-22: o round-trip
corrigido (FIX-004/005), o `exemplo-cinzeiro.json` completado, a checagem de referencia no
instrumento, e a pergunta de 2026-10-17 **fechada** — com o detalhe de que a resposta ao «como
evitar que erros como esse continuem» e o FIX-005, nao o FIX-004.

**Ancora do STATUS:** a linha 10, `## Última conversa (2026-10-20, kit v1.127.0 — fatias 1 a 4)`.
Esse bloco **tem de continuar no arquivo**, e o da auditoria de 2026-07-21 tambem.

Para o IDEAS, um item novo na secao Ativas, **depois** de `### i-024`:

```

### i-025 💡 Teste de round-trip automatizado (baixar → reimportar)
`[nascido do FIX-004, 2026-10-22]` O ciclo baixar→reimportar quebrou por meses sem ninguem notar, e so apareceu porque alguem abriu o app num navegador de verdade. Uma checagem que carregue um acervo, serialize como o `downloadCollection` serializa e reimporte, afirmando igualdade, capturaria a classe inteira — nao so o `_activeModules`. Hoje o `validate.py` valida arquivos parados; isto e o primeiro teste de COMPORTAMENTO do projeto, e exige decidir se entra um harness de navegador (headless) ou se a serializacao e extraida para uma funcao testavel sem DOM. Candidata a analise antes de spec.
```

## Edicao 7 — `scripts/validate.py` · a mensagem final nao pode afirmar o que nao foi medido

**Achada pela auditoria desta WO, no disco do dono, antes de aplicar.** Rodando o instrumento como
ele esta hoje:

```
$ python3 scripts/validate.py
Aviso: pacote 'jsonschema' ausente — so checagem de sintaxe.
       Instale com: pip install jsonschema --break-system-packages
OK (sintaxe)  data/demo.json
OK (sintaxe)  data/exemplo-cinzeiro.json

Tudo conforme ao esquema.          <- MENTIRA: nenhum esquema foi conferido
exit=0
```

`jsonschema` **nao esta instalado nesta maquina**. O instrumento cai no modo degradado, avisa na
PRIMEIRA linha, e dezenas de linhas depois afirma conformidade ao esquema — e e a ultima linha que
quem roda le. E o mesmo defeito que o FIX-005 conserta no app, na outra ponta do projeto: uma
mensagem que nomeia um resultado que a operacao nao produziu. O `meta/CEREBRO.md` ja registra este
risco em «Tecnicas especificas deste projeto»; agora ele apareceu em campo.

**7a — a mensagem final.** Ancora, as duas linhas literais:

```python
    print("Tudo conforme ao esquema.")
    return 0
```

Texto novo, literal:

```python
    if validator is None:
        print("Sintaxe OK. ESQUEMA NAO CONFERIDO (pacote 'jsonschema' ausente).")
    else:
        print("Tudo conforme ao esquema.")
    return 0
```

**7b — o aviso no fim, nao so no comeco.** Ancora, a linha literal:

```python
        print("       Instale com: pip install jsonschema --break-system-packages")
```

Texto novo, literal (a linha original mais uma):

```python
        print("       Instale com: pip install jsonschema --break-system-packages")
        print("       ATE LA, 'OK' abaixo significa so JSON bem formado — nao conformidade.")
```

A checagem de integridade referencial da Edicao 4 **nao depende de `jsonschema`** e continua
valendo nos dois modos — e por isso ela entra fora do `else`, como a Edicao 4b ja manda.

## Fora de escopo

- A opcao C da analise (sanear chaves `_` na importacao). Descartada com motivo registrado: saneamento silencioso apaga o sinal que permitiu achar este defeito. **Nao a aplique por conta.**
- `tryAutoLoad` e o `catch` que apenas tenta o proximo caminho. Risco conhecido e registrado na analise; nao foi reproduzido e nao se conserta aqui.
- Limpar arquivos `.json` ja baixados que o dono tenha guardado fora do mount. Depois de A eles voltam a importar; so reprovariam no `validate.py` se fossem para `data/`.
- `schema/song.schema.json` e `schema/collection.schema.json` — nenhuma mudanca de esquema. A chave `_activeModules` deixa de existir; nao ha o que declarar.
- Qualquer coisa da Fase 3 (painel de qualidade).

## Armadilhas desta WO

- **A arvore NAO esta limpa ao comecar**, e isso e esperado: `meta/CONTEXT.md` e `meta/analises/` sao do chat, e entram no mesmo commit. Conferir na Edicao 0, nao estranhar depois.
- **A Edicao 2 tem tres pontos e e indivisivel.** Duas das tres aplicadas = estado de modulo perdido em silencio. `grep -c "_activeModules" app/index.html`: `2` antes, `0` depois.
- **A indentacao do `errors += check_module_refs(...)` muda o comportamento** e nenhum erro de sintaxe avisa. A checagem 9 e o caso negativo que a pega.
- **Mexe em `data/` — `python3 scripts/validate.py` e OBRIGATORIO** antes do commit. E ele mesmo mudou nesta WO: rode-o tambem para conferir que o instrumento novo nao quebrou o antigo.
- **A verificacao do round-trip exige olho humano num navegador.** Quem tem o disco mede; quem tem a tela ve. Os tres passos do roteiro abaixo sao do DONO, nao seus — nao os carimbe como feitos.
- **Fim de linha:** os arquivos do chat estao em LF. Avisos LF→CRLF no `add` ja apareceram nas quatro fatias anteriores; registre, nao conserte.

## Depois de aplicar — conferencia antes do commit

| # | Checagem | Comando | Esperado |
|---|---|---|---|
| 1 | A chave interna sumiu do codigo | `grep -c "_activeModules" app/index.html` | `0` (era `2`) |
| 2 | O estado novo existe nos tres pontos | `grep -c "App.activeModules" app/index.html` | `3` (declaracao, leitura, escrita) |
| 3 | Os dois `try` da importacao | `grep -c "falha em setCollection" app/index.html` | `1` |
| 4 | A mensagem certa do parse sobreviveu | `grep -c "não é um JSON válido" app/index.html` | `1` |
| 5 | O dado ficou autossuficiente | `python3 -c "import json;d=json.load(open('data/exemplo-cinzeiro.json'));print(len(d['styleModules']))"` | `5` |
| 6 | O dado continua valido, e a mensagem final diz QUAL modo | `python3 scripts/validate.py; echo "exit=$?"` | exit `0`, e a ultima linha e **`Tudo conforme ao esquema.`** se `jsonschema` estiver instalado, ou **`Sintaxe OK. ESQUEMA NAO CONFERIDO...`** se nao estiver. **Medido no disco do dono em 2026-10-22: o pacote NAO esta instalado.** Se a ultima linha disser «Tudo conforme ao esquema» sem o pacote, a Edicao 7a nao foi aplicada. |
| 6b | Se possivel, conferir de verdade | `pip install jsonschema referencing --break-system-packages && python3 scripts/validate.py` | `Tudo conforme ao esquema.` — e **este** e o unico verde que vale para a Edicao 3. Se a instalacao falhar (rede, politica), **DIGA** e marque a conformidade de esquema como NAO CONFERIDA no relatorio; nao a declare pela saida do modo degradado. |
| 7 | A checagem roda nos dois datasets | `python3 scripts/validate.py \| grep -cE "^OK"` | `2`. **Atencao a forma:** sem `jsonschema` as linhas saem como `OK (sintaxe)  <arquivo>`; com o pacote, como `OK  <arquivo>  (N álbuns, M faixas)`. Ancorar em `^OK` casa as duas; `grep -c "OK"` sem ancora tambem casaria a palavra no meio de outra linha. |
| 8 | A funcao nova esta no instrumento | `grep -c "def check_module_refs" scripts/validate.py` | `1` |
| 9 | **Caso negativo — a checagem de fato reprova.** Com uma copia descartavel: `cp data/exemplo-cinzeiro.json /tmp/x.json && python3 -c "import json;d=json.load(open('/tmp/x.json'));d['styleModules']=[];json.dump(d,open('/tmp/x.json','w'))" && python3 scripts/validate.py /tmp/x.json; echo "exit=$?"` | imprime `ERRO de referencia ... (5 id(s) de modulo sem indice)` e **`exit=1`**. Se sair `exit=0`, o `errors +=` caiu dentro do `else` — corrija a indentacao. Apague `/tmp/x.json` depois. |
| 10 | Os registros entraram uma vez cada | `grep -c "^## FIX-004" meta/DECISIONS.md`, `FIX-005`, `^## DEC-016` | `1` cada |
| 11 | Os registros anteriores ficaram | `grep -c "^## DEC-01[0-5]" meta/DECISIONS.md` e `grep -c "^## FIX-00[1-3]" meta/DECISIONS.md` | `6` e `3` |
| 12 | A analise esta versionada e Decidida | `GIT_OPTIONAL_LOCKS=0 git ls-files meta/analises \| wc -l` e `grep -c "Status:\*\* Decidida" meta/analises/261021-ANALISE-roundtrip-do-acervo.md` | `2` e `1` |
| 13 | A ideia nova entrou | `grep -c "^### i-025" meta/IDEAS.md` | `1` |
| 14 | Os blocos antigos do STATUS sobreviveram | `grep -c "^## Última conversa" meta/STATUS.md` | `3` (o novo + os dois de antes) |
| 15 | Nenhum relatorio `.txt` dentro do repo | `GIT_OPTIONAL_LOCKS=0 git status --short \| grep -c '\.txt'` | `0` |

**Os tres campos de cada passo:** as checagens 1-15 sao rodadas por **quem aplica (o Code)**, na raiz
do repo (`C:\Users\alexk\Tools\cancioneiro\cancioneiro`), em Git Bash. **O que nenhuma delas
responde:** se o app de fato importa e renderiza — `grep` e `validate.py` leem arquivos parados e
nenhum deles abre um navegador. Essa metade e o roteiro abaixo, e e do dono.

## Roteiro de conferencia na tela — para o DONO, nao para o executor

Cada item diz o que se ve quando esta certo. Abra `app/index.html` com duplo-clique (modo `file://`).

1. **O arquivo que estava quebrado volta a abrir.** Clique «Importar .json» e escolha
   `C:\Users\alexk\Tools\cancioneiro\album-referencias.json`.
   **Certo:** a mensagem embaixo diz **«Acervo importado: Album-Referencias»** e aparecem os cartoes
   das 7 faixas (ar-01 a ar-07). **Errado:** «Arquivo invalido» ou tela vazia.
2. **O download deixa de sujar o arquivo.** Com o acervo acima aberto, clique «Baixar .json». Abra o
   arquivo baixado no Bloco de Notas e procure por `_activeModules`.
   **Certo:** **nenhuma ocorrencia**. **Errado:** qualquer linha com `"_activeModules": {}`.
3. **O ciclo fecha.** Clique «Importar .json» e escolha o arquivo que voce acabou de baixar.
   **Certo:** «Acervo importado» e os mesmos 7 cartoes. **Errado:** qualquer mensagem de erro.
4. **O que nao devia mudar nao mudou.** Em qualquer faixa, abra «modulos de estilo (ligar/desligar)»
   e clique um chip apagado.
   **Certo:** o chip acende e o texto recomposto embaixo **cresce**, ganhando o fragmento. Clicando
   um chip aceso, ele apaga e o texto **nao encolhe** — isso e o comportamento correto («a base
   manda; modulos so somam»), nao um bug.

Se qualquer item der errado, **nao e para consertar na hora**: diga qual item e o que apareceu.

## Relatorio de aplicacao

Grave em `../261022-HHMM-code-cancioneiro-apply-wo0006.txt`, com o `HHMM` de
`date +%y%m%d-%H%M` rodado na hora. Deixe os quatro itens do roteiro do dono explicitamente
marcados como **pendentes de conferencia na tela** — nao como feitos.

**Proximo comando** (ultima linha do relatorio, cru e sozinho):

```
/wrap
```

## Commit

```
git add app/index.html scripts/validate.py data/exemplo-cinzeiro.json meta/DECISIONS.md meta/STATUS.md meta/IDEAS.md meta/CONTEXT.md meta/analises meta/workorders logs
```

```
git commit -m "fix: corrige o round-trip do acervo e duas mensagens que afirmavam o que nao mediram" -m "FIX-004: o estado dos modulos ligados sai de dentro da colecao e passa a App.activeModules[song.id]; o Baixar .json gravava um Set serializado como {} em cada faixa e o Importar .json quebrava nele. FIX-005: separa o try do parse do try da carga, para o catch parar de atribuir a qualquer falha a causa da primeira operacao, e conserta a mesma classe de defeito no validate.py, que dizia Tudo conforme ao esquema no modo sem jsonschema. DEC-016: acervo autossuficiente; exemplo-cinzeiro.json recebe os cinco modulos que citava, e o validate.py ganha checagem de integridade referencial."
```

```
git push
```
