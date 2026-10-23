# WO 0007 — FIX-006: sanear as chaves internas na importacao, avisando quantas removeu

## Cabecalho

> **Tipo:** WO de CODIGO (uma funcao e uma chamada em `app/index.html`) e de registro.
> **Config sugerida:** Sonnet · `/effort low`. Duas ancoras, texto literal, nenhuma decisao delegada.
> **Pre-requisito:** commit `a1ee1c8`, branch `main`, sincronizada com `origin/main`. **A arvore NAO esta limpa:** `meta/analises/261021-ANALISE-roundtrip-do-acervo.md` esta modificado (revisao escrita pelo chat neste turno). Nada mais deve aparecer no `git status`.
> **Base:** a secao «Revisao — 2026-10-23» de `meta/analises/261021-ANALISE-roundtrip-do-acervo.md`, e a conferencia na tela da WO 0006 (itens 1-4), que revelou a lacuna.
> **Depende de:** WO 0006, ja aplicada (`2c4dd36`). **Esta WO so faz sentido DEPOIS dela:** C sozinha conserta a entrada e deixa o app sujando a saida.
>
> **Arquivos que o chat gravou no disco e esta WO versiona** (sha1sum medido pelo chat ao gravar):
> - `meta/analises/261021-ANALISE-roundtrip-do-acervo.md` — `0cea07e74adc923fdd8986276b043164668b72e4`
>
> **Ancora semantica:** se um trecho-ancora nao bater EXATAMENTE, PARE e reporte.
> **Idempotencia:** antes de cada edicao, procure o texto NOVO INTEIRO no arquivo — frase-chave nao basta. Se o inteiro ja estiver la, **PULE** e diga no relatorio.
>
> **Ancoras lidas em:** trechos lidos pelo chat no turno de 2026-10-23, direto do disco:
> - `app/index.html`, o corpo de `importFromFile` apos a WO 0006, incluindo as duas linhas de comentario e os dois `try`
> - `app/index.html`, a linha `/** Valida minimamente e adota a colecao. */`
> - `meta/DECISIONS.md`, ultima linha do arquivo (fim de DEC-016), que comeca com `**Consequencias:** (+) Um acervo e reproduzivel sozinho`
> - `meta/STATUS.md` linha 10: `## Última conversa (2026-10-22, WO 0006 — round-trip do acervo)`

---

## 1. Por que — e o que a WO 0006 deixou de fora

A WO 0006 impediu o app de **criar** a chave `_activeModules`. Nao impediu o app de **devolver** a que
ja existe: ele le o JSON, nunca toca nela, e a serializa de volta no download. Medido depois de
aplicar, com o app corrigido:

```
demo.json              (entrada limpa)  ->  entrada: 0  |  baixado: 0
album-referencias.json (entrada suja)   ->  entrada: 7  |  baixado: 7
```

O `album-referencias.json` abre, funciona e exporta — mas carrega as 7 chaves de download em
download, e `song.schema.json` tem `additionalProperties: false`: ele reprovaria no `validate.py` se
fosse para `data/`.

A analise original considerou e **descartou** esta correcao (opcao C) com o argumento de que
saneamento silencioso apaga o sinal que permitiu achar o defeito. O argumento continua de pe; a
conclusao e que estava errada. **O remedio nao era descartar C, era dar voz a ela.**

## Edicao 0 — Conferencia de hash e de arvore

```
sha1sum meta/analises/261021-ANALISE-roundtrip-do-acervo.md
GIT_OPTIONAL_LOCKS=0 git status --short
```

O hash bate com o cabecalho, e o `git status` mostra **exatamente** `M meta/analises/261021-ANALISE-roundtrip-do-acervo.md` (mais esta WO, nao rastreada). Qualquer outra coisa: **PARE e reporte**.

## Edicao 1 — `app/index.html` · a funcao que saneia e conta

**Ancora**, a linha literal:

```js
/** Valida minimamente e adota a colecao. */
```

Insira ANTES dela o bloco abaixo, deixando uma linha em branco entre o fim do bloco e a linha-ancora.

**Texto novo, literal:**

```js
/* Remove as chaves internas (prefixo _) que versoes antigas da ferramenta
   vazaram para dentro do JSON salvo, e devolve quantas removeu.

   Por que CONTAR em vez de limpar calado: a chave `_activeModules` so foi
   descoberta porque alguem viu o arquivo quebrar. Saneamento silencioso
   conserta o sintoma e apaga o sinal — o proximo vazamento passaria
   despercebido pelo resto da vida do projeto (ver FIX-006 e a revisao da
   analise de 2026-10-21). O aviso e a metade que importa. */
function stripInternalKeys(node) {
  let n = 0;
  if (Array.isArray(node)) {
    node.forEach(item => { n += stripInternalKeys(item); });
  } else if (node && typeof node === "object") {
    Object.keys(node).forEach(k => {
      if (k.startsWith("_")) { delete node[k]; n++; }
      else n += stripInternalKeys(node[k]);
    });
  }
  return n;
}
```

## Edicao 2 — `app/index.html` · chamar a funcao e avisar

**Ancora**, o bloco literal dentro de `importFromFile` (como ficou depois da WO 0006):

```js
    try {
      setCollection(json);
      toast("Acervo importado: " + (json.title || file.name));
    } catch (e) {
```

**Texto novo, literal:**

```js
    const removidas = stripInternalKeys(json);
    try {
      setCollection(json);
      toast("Acervo importado: " + (json.title || file.name)
            + (removidas ? " · " + removidas + " campo(s) interno(s) removido(s) — baixe de novo para gravar limpo" : ""));
    } catch (e) {
```

**O saneamento vai FORA do `try`, antes dele.** Dentro, uma falha de `setCollection` faria a mensagem
de erro engolir o aviso de saneamento — que e exatamente o defeito que o FIX-005 acabou de consertar
neste mesmo arquivo. A funcao nao lanca: percorre objeto ja parseado.

**E o aviso vai no toast de SUCESSO, nao num `console.log`.** O dono nao abre o console; se o aviso
so existir la, o saneamento e silencioso na pratica, e a Edicao 1 perde a razao de ser.

## Edicao 3 — `meta/DECISIONS.md` · FIX-006

**Ancora:** a ULTIMA linha do arquivo (fim de DEC-016), citada no cabecalho. Insira DEPOIS dela,
precedido de uma linha em branco e de `---`.

```
---

## FIX-006 — A correcao do round-trip nao limpava a sujeira que ja estava nos arquivos

**Data:** 2026-10-23
**Sintoma:** Depois do FIX-004, o `album-referencias.json` voltou a abrir e o ciclo baixar→reimportar passou a fechar. Mas a conferencia na tela mediu o arquivo baixado e achou as 7 chaves `_activeModules` ainda la — entrada limpa produzia saida com 0, entrada ja suja produzia saida com 7.

**Causa raiz:** O FIX-004 parou de GRAVAR a chave; nao removeu a que ja existia. O app lia o JSON, nunca tocava em `_activeModules`, e a serializava de volta no download. Arquivo contaminado por uma versao antiga da ferramenta propagava a chave indefinidamente — e seguiria reprovando em `song.schema.json`, que tem `additionalProperties: false`.

**Solucao:** `stripInternalKeys(json)` na importacao, removendo recursivamente as chaves com prefixo `_` e **devolvendo quantas removeu**, informadas no proprio toast de sucesso. A contagem e metade da correcao: a `_activeModules` so foi descoberta porque um arquivo quebrou visivelmente, e saneamento mudo teria consertado o sintoma apagando o sinal — o proximo vazamento passaria despercebido. O saneamento roda FORA do `try` da carga, para o aviso nao ser engolido por uma mensagem de erro (seria o FIX-005 de novo, no mesmo arquivo).

**Licao:** Corrigir a causa nao limpa os dados que a causa ja produziu, e as duas coisas parecem uma so quando se olha o sintoma. Ao fechar um defeito que escreveu dado errado, medir **duas** perguntas: «para de acontecer?» e «o que ja aconteceu fica limpo?». A analise de 2026-10-21 mediu as tres opcoes so contra a primeira — e a propria tabela dela mostrava a opcao C passando num caminho que a recomendada nao cobria, coluna que foi lida como redundante.
```

## Edicao 4 — `meta/STATUS.md`

A cargo do `/wrap`, em append. **Ancora:** a linha 10,
`## Última conversa (2026-10-22, WO 0006 — round-trip do acervo)` — esse bloco **tem de continuar no
arquivo**, e o de 2026-07-21 tambem (`## Última conversa (2026-07-21, auditoria)`). Conte os dois
antes e depois.

No bloco novo, registre tambem que a pergunta de 2026-10-17 (`../261017-2231.txt`) esta **fechada**:
as duas metades tem resposta — o que havia de errado com o arquivo (FIX-004 e FIX-006) e como evitar
que erros assim continuem (FIX-005, nas duas pontas: o `catch` do app e o rodape do `validate.py`).

## Fora de escopo

- O merge do kit **v1.131.0** (pacote em `../261023-kcm-update-v1.131.0/`). E outra fatia; nao toque.
- `tryAutoLoad` e o `catch` que so tenta o proximo caminho. Risco registrado na analise.
- Limpar o `album-referencias.json` por fora. Depois desta WO, basta importar e baixar de novo — e o
  toast dira quantas chaves sairam. **Nao rode script de limpeza:** o caminho pelo app e o teste.
- Instalar `jsonschema`. Continua pendente, e a conformidade de esquema segue **NAO CONFERIDA**.

## Armadilhas desta WO

- **O saneamento fora do `try` nao e detalhe de estilo.** Dentro, um erro de carga engole o aviso. Se
  o `git diff` mostrar `const removidas` depois de `try {`, esta errado.
- **`stripInternalKeys` percorre a colecao inteira, inclusive `styleModules`.** Nenhuma chave legitima
  do esquema comeca com `_` (conferido: `song.schema.json` e `collection.schema.json` nao tem
  nenhuma), entao nao ha falso positivo possivel hoje. Se um dia houver, o aviso denuncia.
- **A mensagem do toast tem duas formas.** Sem chave removida, exatamente como era antes; com chave,
  o sufixo. A checagem 4 cobre as duas.
- **Mexe em `app/index.html`, nao em `data/`** — `validate.py` nao se aplica a esta mudanca, mas rode
  mesmo assim para confirmar que nada regrediu.

## Depois de aplicar — conferencia antes do commit

| # | Checagem | Comando | Esperado |
|---|---|---|---|
| 1 | A funcao existe, uma vez so | `grep -c "function stripInternalKeys" app/index.html` | `1` |
| 2 | E chamada, uma vez so | `grep -c "stripInternalKeys(json)" app/index.html` | `1` |
| 3 | **Chamada FORA do `try`** | `grep -n -A1 "const removidas" app/index.html` | a linha seguinte e `    try {` — e NAO o contrario |
| 4 | As duas formas do toast | `grep -c "campo(s) interno(s) removido(s)" app/index.html` e `grep -c "Acervo importado: " app/index.html` | `1` e `1` |
| 5 | O FIX-004 nao regrediu | `grep -c "_activeModules" app/index.html` | `0` |
| 6 | Nada regrediu no dado | `python3 scripts/validate.py; echo "exit=$?"` | `exit=0`; ultima linha ainda declara o modo (`ESQUEMA NAO CONFERIDO`, se `jsonschema` seguir ausente) |
| 7 | O registro entrou e os anteriores ficaram | `grep -c "^## FIX-006" meta/DECISIONS.md` e `grep -c "^## FIX-00[1-5]" meta/DECISIONS.md` | `1` e `5` |
| 8 | A revisao da analise esta versionada | `grep -c "^## Revisao — 2026-10-23" meta/analises/261021-ANALISE-roundtrip-do-acervo.md` | `1` |
| 9 | Os blocos antigos do STATUS sobreviveram | `grep -c "^## Última conversa" meta/STATUS.md` | `4` (o novo + os tres de antes) |
| 10 | Nenhum relatorio `.txt` dentro do repo | `GIT_OPTIONAL_LOCKS=0 git status --short \| grep -c '\.txt'` | `0` |

**Os tres campos de cada passo:** as dez sao rodadas por **quem aplica (o Code)**, na raiz do repo
(`C:\Users\alexk\Tools\cancioneiro\cancioneiro`), em Git Bash. **Chega no ramo?** As checagens 1-5 leem
o arquivo que a WO muda, nas duas funcoes que ela toca (`stripInternalKeys` e `importFromFile`). **Esta
e qual pergunta: «esta la?» ou «presta?»** Todas as dez respondem «esta la?» — nenhuma abre um
navegador. A pergunta «presta?» e o roteiro de tela, que o chat entrega ao dono no corpo da resposta
deste turno, **nao aqui**.

## Relatorio de aplicacao

Grave em `../261023-HHMM-code-cancioneiro-apply-wo0007.txt`, com o `HHMM` de `date +%y%m%d-%H%M`
rodado na hora. O roteiro de tela **nao e seu** — nao o reproduza nem o marque como pendente: ele foi
entregue ao dono no chat, fora desta WO. Registre apenas que a conferencia na tela e do dono.

**Proximo comando** (ultima linha do relatorio, cru e sozinho):

```
/wrap
```

## Commit

```
git add app/index.html meta/DECISIONS.md meta/STATUS.md meta/analises meta/workorders logs
```

```
git commit -m "fix: saneia chaves internas na importacao, avisando quantas removeu" -m "FIX-006: o FIX-004 impediu o app de criar _activeModules mas nao removia a que ja existia no arquivo lido, entao um acervo contaminado propagava a chave de download em download e seguiria reprovando no esquema. stripInternalKeys remove as chaves com prefixo _ na importacao e devolve a contagem, informada no toast de sucesso: saneamento silencioso consertaria o sintoma apagando o sinal. Revisa a analise de 2026-10-21, cuja recomendacao media so se o defeito parava de acontecer, nao se o dado existente ficava limpo."
```

```
git push
```
