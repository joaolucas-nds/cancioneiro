# WO 0050 — O Pages sem Jekyll (FIX-010)

## Cabecalho

> **Tipo:** correcao de publicacao — `.nojekyll` novo, CEREBRO e log ja gravados pelo chat; STATUS e DECISIONS aqui. O app nao muda (segue 0.23.1).
> **Config sugerida:** Sonnet · `/effort low` (3 edicoes; o que pesa e medir o deploy depois do push).
> **Pre-requisito:** commit `b5b3d1e`, branch `main`, sincronizada com `origin/main`. O `git status --short` mostra exatamente: ` M logs/2026-11-17.md`, ` M meta/CEREBRO.md`, `?? .nojekyll` e `?? meta/workorders/261117-wo0050-pages-sem-jekyll.md`.
> **Base:** as capturas do dono de 18:16 e 21:05 (o site em v0.22.0) e o `git grep` do primeiro `{{` em `.md`, no `c04bd78` (log de 2026-11-17, Conversa 3).
> **Depende de:** `b5b3d1e` (WO 0049).
>
> | arquivo | partida (sha1) | chegada (sha1) |
> |---|---|---|
> | `meta/STATUS.md` | `564a7caaea217731148a91bf5e8f23ff76167550` | `1b370c0f370eefd25a689547cc8fb57d20f37505` |
> | `meta/DECISIONS.md` | `5ebada216caa8ad731bbed96715e375761ee9015` | `8c5769969e7ab63e070f80bcec4e70e185173b0e` |
> | `.nojekyll` | `da39a3ee5e6b4b0d3255bfef95601890afd80709` | o mesmo (gravado pelo chat; so versionar) |
> | `meta/CEREBRO.md` | `d63bd87e68d92000ccab86046dd6968ff29889e8` | o mesmo (gravado pelo chat; so versionar) |
> | `logs/2026-11-17.md` | `e9db7b609cbae456ea867ab382d55fbccffe4faf` | o mesmo (gravado pelo chat; so versionar) |
>
> **Ancora semantica:** se um trecho-ancora nao bater EXATAMENTE, PARE e reporte.
> **Idempotencia:** antes de cada edicao, procure o texto NOVO INTEIRO; se ja estiver la, PULE e diga no relatorio.
> **Ancoras:** linhas inteiras (uma linha ou um bloco de linhas inteiras), cada uma 1 vez no arquivo no momento da edicao, na ordem abaixo. Toda edicao «substitui a ancora inteira».
> **Âncoras lidas em** (lidas pelo chat NESTE turno, de `b5b3d1e` clonado do GitHub e conferido contra o disco do dono — a lista dos versionados com o mesmo sha1; aplicadas em ordem num clone, por um extrator que le so esta WO, com a chegada medida byte a byte):
> - E01 (`meta/STATUS.md`, ultima conversa: o Pages parado): bloco de 2 linhas, começando por `- **0.23.0 aplicada** ('c04bd78', CI verde, run '44090505271', '[medido pelo Code]').…`
> - E02 (`meta/STATUS.md`, publicado: sem Jekyll): linha `- **Publicado no GitHub Pages** em 'https://joaolucas-nds.github.io/cancioneiro/app/i…`
> - E03 (`meta/DECISIONS.md`, FIX-010 (no fim do arquivo)): linha `**Consequências:** (+) Um gesto a menos para cada ação, sem nada novo para aprender. …`
> **Canal dos meta neste ciclo = CODE:** STATUS, DECISIONS, IDEAS e CHANGELOG pelo Code (DEC-010); o log do dia ja esta gravado pelo chat.

---

## 1. Por que

O site publicado parou na 0.22.0 desde o `c04bd78`: o Jekyll do Pages le os `.md` como template, e o `{{` de um teste dentro da WO 0048 derruba a montagem. O CI de testes nao monta o Pages, entao ficou verde. O `.nojekyll` vazio na raiz desliga o Jekyll; o app nao depende dele. **O ponto desta WO e a checagem 6:** medir que o site passou a servir a 0.23.1.

## Edicao 0 — Conferencia de hash e de arvore

```
sha1sum meta/STATUS.md meta/DECISIONS.md .nojekyll meta/CEREBRO.md logs/2026-11-17.md
GIT_OPTIONAL_LOCKS=0 git status --short
```

Todos batem com **partida** (o log, o CEREBRO e o `.nojekyll`, gravados pelo chat); o `git status` mostra exatamente as quatro linhas do Pre-requisito. Qualquer outra coisa: **PARE e reporte**.

## Edicoes E01 a E03

Na ordem. Copie o que esta ENTRE as linhas de quatro crases, sem elas. Aplique por script, extraindo os blocos da WO; grave em UTF-8 com LF.

### E01 — ultima conversa: o Pages parado

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
- **0.23.0 aplicada** (`c04bd78`, CI verde, run `44090505271`, `[medido pelo Code]`). O dono apontou, sem o roteiro, que as duas zonas do arraste deviam aparecer juntas `[relatado pelo dono, 2026-11-17]`; a 0.23.1 corrige (WO 0049). O roteiro da 0.23.0 não foi feito; vale o da 0.23.1, no log de 2026-11-17.
- **Este bloco substitui o anterior** (a 0.22.0 no clone). O que ele dizia está em `logs/2026-11-16.md`, Conversa 6.
````

**Texto novo (substitui a ancora inteira):**

````
- **0.23.0 aplicada** (`c04bd78`, CI verde, run `44090505271`, `[medido pelo Code]`). O dono apontou, sem o roteiro, que as duas zonas do arraste deviam aparecer juntas `[relatado pelo dono, 2026-11-17]`; a 0.23.1 corrige (WO 0049). O roteiro da 0.23.0 não foi feito; vale o da 0.23.1, no log de 2026-11-17.
- **0.23.1 aplicada** (`b5b3d1e`, CI verde, run `44201279713`, `[medido pelo Code]`). **O Pages parou na 0.22.0 desde o `c04bd78`** (FIX-010): o `{{` de um teste dentro da WO 0048 derrubava a montagem do Jekyll. As capturas do dono de 18:16 e 21:05 mostram «v0.22.0» `[medido pelo chat]`, então o que ele testou foi a 0.22.0. O `.nojekyll` (WO 0050) desliga o Jekyll; o roteiro da 0.23.1 se refaz depois do deploy.
- **Este bloco substitui o anterior** (a 0.22.0 no clone). O que ele dizia está em `logs/2026-11-16.md`, Conversa 6.
````

### E02 — publicado: sem Jekyll

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
- **Publicado no GitHub Pages** em `https://joaolucas-nds.github.io/cancioneiro/app/index.html` — o push em `main` publica.
````

**Texto novo (substitui a ancora inteira):**

````
- **Publicado no GitHub Pages** em `https://joaolucas-nds.github.io/cancioneiro/app/index.html` — o push em `main` publica. Sem Jekyll desde a WO 0050 (`.nojekyll`, FIX-010): os arquivos saem como estão.
````

### E03 — FIX-010 (no fim do arquivo)

**Arquivo:** `meta/DECISIONS.md`

**Ancora:**

````
**Consequências:** (+) Um gesto a menos para cada ação, sem nada novo para aprender. (+) A lista de acervos não some para baixo de uma lista longa de álbuns. (−) Com muitos acervos e pouca altura, a área deles mostra poucas linhas de cada vez. (−) O «Desvincular» do acervo só aparece no aberto, porque o vínculo vive no acervo aberto.
````

**Texto novo (substitui a ancora inteira):**

````
**Consequências:** (+) Um gesto a menos para cada ação, sem nada novo para aprender. (+) A lista de acervos não some para baixo de uma lista longa de álbuns. (−) Com muitos acervos e pouca altura, a área deles mostra poucas linhas de cada vez. (−) O «Desvincular» do acervo só aparece no aberto, porque o vínculo vive no acervo aberto.

## FIX-010 — O Pages parou de publicar na 0.22.0: um `{{` dentro de um `.md` derrubava o Jekyll

**Data:** 2026-11-17
**Status:** resolvida (WO 0050)
**Sintoma:** depois do push da 0.23.0 (`c04bd78`) e da 0.23.1 (`b5b3d1e`), o site publicado continuava na 0.22.0. O dono testou duas vezes e viu o desenho antigo do arraste (capturas de 18:16 e 21:05, com «v0.22.0» no cabeçalho) `[relatado pelo dono]`. O CI de testes ficou verde nos dois commits: ele não monta o Pages.
**Causa raiz:** o GitHub Pages monta o site com Jekyll, que lê todo `.md` em busca de template Liquid. A WO 0048 (`meta/workorders/261117-wo0048-…`) trazia um teste em Python com `{{` (chaves dobradas de f-string). Era o primeiro `{{` em `.md` do repositório: `git grep` no `a6aa20a` não acha nenhum, no `c04bd78` acha esse. O Liquid falha nesse trecho, a montagem inteira falha, e o Pages segue servindo a última que deu certo. Nem o chat nem o Code olhavam o deploy: o «push publica» do STATUS era suposição.
**Solução:** um `.nojekyll` vazio na raiz. O Pages passa a servir os arquivos como estão, sem Jekyll. Nada no app dependia dele: o app busca `schema/PROMPT-PARA-CHATS.md` e `data/demo.json` como arquivos simples, servidos do mesmo jeito.
**Lição:** CI verde não é site publicado. Toda WO que muda o app confere, depois do push, a versão no cabeçalho do site publicado; é a checagem da WO 0050. O roteiro do dono abre conferindo a versão no cabeçalho, antes de qualquer passo.
````

## Depois de aplicar — conferencia antes do commit

| # | Checagem | Comando | Esperado |
|---|---|---|---|
| 1 | Os arquivos sao os previstos | `sha1sum meta/STATUS.md meta/DECISIONS.md .nojekyll meta/CEREBRO.md logs/2026-11-17.md` | a coluna **chegada** |
| 2 | O `.nojekyll` vazio na raiz | `wc -c < .nojekyll` | `0` |
| 3 | Nenhum `{{` resolvido a mao | `git grep -c -E '\{\{' -- '*.md'` | o `.md` da WO 0048 continua com 1 (nao mexa: com o `.nojekyll`, ele deixa de importar) |
| 4 | Validacao | `python scripts/validate.py; echo "exit=$?"` | `exit=0`, versao 0.23.1 |
| 5 | Nada alem do previsto | `GIT_OPTIONAL_LOCKS=0 git status --short --untracked-files=all` | os 5 arquivos da tabela e esta WO |
| 6 | **Depois do push: o site publicado** | em laco (ate ~10 min): `gh api repos/joaolucas-nds/cancioneiro/pages/builds/latest --jq '.status + " " + .commit[0:7] + " " + (.error.message // "")'` ate `built <commit do push>`; depois `curl -s https://joaolucas-nds.github.io/cancioneiro/app/index.html | grep -o 'app-version">v[0-9.]*'` | `built` com o commit novo, e `app-version">v0.23.1`. Se der `errored`, a mensagem de erro inteira no relatorio, e PARE |

| 7 | O CI de testes | `gh run list --limit 1` e `gh run view <id> --json status,conclusion` ate `completed` | `success` |

As checagens 2 a 4 rodaram no clone do chat; no Git Bash, **nao testado**. A 6 o chat nao consegue rodar: o endereco do Pages e a API de builds estao barrados para ele. Se a sua tambem nao alcancar, diga isso no relatorio (nao suponha).
**Esta e qual pergunta?** A 1 responde «esta la?»; a 6, «o site serve a versao nova?» — a pergunta que ninguem fazia (FIX-010). Nenhuma responde «funciona na tela?»: isso e o roteiro do dono (log de 2026-11-17, Conversa 3).

## Relatorio de aplicacao

Grave em `../AAMMDD-HHMM-code-cancioneiro-apply-wo0050.txt`, com o carimbo de `date +%y%m%d-%H%M` rodado na hora. Checagem 1 em primeiro lugar, e a saida crua da 6 (o status do build, o commit e a versao que o site serve). **Sem `/wrap` depois desta WO**, e sem secao sua no log, salvo se algo fugir do literal.

## Commit

```
git add meta/STATUS.md meta/DECISIONS.md .nojekyll meta/CEREBRO.md logs/2026-11-17.md meta/workorders/261117-wo0050-pages-sem-jekyll.md
```

```
git commit -m "fix: publicar o Pages sem Jekyll (FIX-010)" -m "Um {{ dentro da WO 0048 derrubava a montagem do Jekyll e o site ficou na 0.22.0 desde c04bd78. O .nojekyll serve os arquivos como estao; o app nao depende do Jekyll."
```

```
git push
```
