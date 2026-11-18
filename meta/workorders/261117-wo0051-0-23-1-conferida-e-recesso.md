# WO 0051 — A 0.23.1 conferida e o recesso

## Cabecalho

> **Tipo:** registro — STATUS; a Conversa 4 do log ja gravada pelo chat. Nada de codigo.
> **Config sugerida:** Sonnet · `/effort low` (3 edicoes num arquivo).
> **Pre-requisito:** commit `786749d`, branch `main`, sincronizada com `origin/main`. O `git status --short` mostra exatamente: ` M logs/2026-11-17.md` e `?? meta/workorders/261117-wo0051-0-23-1-conferida-e-recesso.md`.
> **Base:** o relatorio da WO 0050 (o site serve a v0.23.1) e o roteiro da 0.23.1 ok `[relatado pelo dono, 2026-11-17 21:25]` (log de 2026-11-17, Conversa 4).
> **Depende de:** `786749d` (WO 0050).
>
> | arquivo | partida (sha1) | chegada (sha1) |
> |---|---|---|
> | `meta/STATUS.md` | `1b370c0f370eefd25a689547cc8fb57d20f37505` | `4281f2f67539fa89c805d32e6e177994be3b0574` |
> | `logs/2026-11-17.md` | `f0cfe92a12a0d898379caa1e31452d5657206eb2` | o mesmo (gravado pelo chat; so versionar) |
>
> **Ancora semantica:** se um trecho-ancora nao bater EXATAMENTE, PARE e reporte.
> **Idempotencia:** antes de cada edicao, procure o texto NOVO INTEIRO; se ja estiver la, PULE e diga no relatorio.
> **Ancoras:** linhas inteiras (uma linha ou um bloco de linhas inteiras), cada uma 1 vez no arquivo no momento da edicao, na ordem abaixo. Toda edicao «substitui a ancora inteira».
> **Âncoras lidas em** (lidas pelo chat NESTE turno, de `786749d` clonado do GitHub e conferido contra o disco do dono — a lista dos versionados com o mesmo sha1; aplicadas em ordem num clone, por um extrator que le so esta WO, com a chegada medida byte a byte):
> - E01 (`meta/STATUS.md`, fase e titulo da ultima conversa): bloco de 5 linhas, começando por `**Versão atual:** 0.23.1 · **Fase:** 3a, 3a.2, o BPM da 3b, o prompt-modelo e as conv…`
> - E02 (`meta/STATUS.md`, a 0.23.1 publicada e conferida): bloco de 2 linhas, começando por `- **0.23.1 aplicada** ('b5b3d1e', CI verde, run '44201279713', '[medido pelo Code]').…`
> - E03 (`meta/STATUS.md`, backlog: o recesso): linha `1. **Conferir a 0.23.1 na tela** (dono): o roteiro do log de 2026-11-17, Conversa 2 (…`
> **Canal dos meta neste ciclo = CODE:** STATUS, DECISIONS, IDEAS e CHANGELOG pelo Code (DEC-010); o log do dia ja esta gravado pelo chat.

---

## 1. Por que

A 0.23.1 esta publicada (o Pages montou o `786749d`) e foi conferida na tela pelo dono. O STATUS registra isso e o recesso; o log ja tem a Conversa 4.

## Edicao 0 — Conferencia de hash e de arvore

```
sha1sum meta/STATUS.md logs/2026-11-17.md
GIT_OPTIONAL_LOCKS=0 git status --short
```

Todos batem com **partida** (o log, gravado pelo chat); o `git status` mostra exatamente as duas linhas do Pre-requisito. Qualquer outra coisa: **PARE e reporte**.

## Edicoes E01 a E03

Na ordem. Copie o que esta ENTRE as linhas de quatro crases, sem elas. Aplique por script, extraindo os blocos da WO; grave em UTF-8 com LF.

### E01 — fase e titulo da ultima conversa

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
**Versão atual:** 0.23.1 · **Fase:** 3a, 3a.2, o BPM da 3b, o prompt-modelo e as conveniências de uso concluídos e conferidos · os álbuns antigos convertidos (i-008, fora do repo) · curadoria no app concluída nas três entregas (DEC-028, DEC-029) · frente de interface concluída e conferida nas quatro entregas (DEC-030 a DEC-033) · organizar os álbuns (0.18.0, DEC-035) conferido · rampa de BPM (0.19.0, DEC-036) conferida · fórmulas de referência (0.20.0, DEC-037) conferidas na tela · importar vários `.json` (0.22.0, DEC-040) conferido na tela · clique direito e lateral em duas áreas (0.23.0, DEC-041) e as duas zonas do arraste juntas (0.23.1) à espera da conferência na tela · a Fase 3 concluída · kit de música lido pelo KCM, à espera da resposta (i-039)

---

## Última conversa (2026-11-16 a 2026-11-17, 0.22.0 e 0.23.0, WO 0047 e 0048)
````

**Texto novo (substitui a ancora inteira):**

````
**Versão atual:** 0.23.1 · **Fase:** 3a, 3a.2, o BPM da 3b, o prompt-modelo e as conveniências de uso concluídos e conferidos · os álbuns antigos convertidos (i-008, fora do repo) · curadoria no app concluída nas três entregas (DEC-028, DEC-029) · frente de interface concluída e conferida nas quatro entregas (DEC-030 a DEC-033) · organizar os álbuns (0.18.0, DEC-035) conferido · rampa de BPM (0.19.0, DEC-036) conferida · fórmulas de referência (0.20.0, DEC-037) conferidas na tela · importar vários `.json` (0.22.0, DEC-040) conferido na tela · clique direito e lateral em duas áreas (0.23.0, DEC-041) e as duas zonas do arraste juntas (0.23.1) conferidos na tela · Pages sem Jekyll (FIX-010) · **em recesso** desde 2026-11-17 · a Fase 3 concluída · kit de música lido pelo KCM, à espera da resposta (i-039)

---

## Última conversa (2026-11-16 a 2026-11-17, 0.22.0 a 0.23.1, WO 0047 a 0051)
````

### E02 — a 0.23.1 publicada e conferida

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
- **0.23.1 aplicada** (`b5b3d1e`, CI verde, run `44201279713`, `[medido pelo Code]`). **O Pages parou na 0.22.0 desde o `c04bd78`** (FIX-010): o `{{` de um teste dentro da WO 0048 derrubava a montagem do Jekyll. As capturas do dono de 18:16 e 21:05 mostram «v0.22.0» `[medido pelo chat]`, então o que ele testou foi a 0.22.0. O `.nojekyll` (WO 0050) desliga o Jekyll; o roteiro da 0.23.1 se refaz depois do deploy.
- **Este bloco substitui o anterior** (a 0.22.0 no clone). O que ele dizia está em `logs/2026-11-16.md`, Conversa 6.
````

**Texto novo (substitui a ancora inteira):**

````
- **0.23.1 aplicada** (`b5b3d1e`, CI verde, run `44201279713`, `[medido pelo Code]`). **O Pages parou na 0.22.0 desde o `c04bd78`** (FIX-010): o `{{` de um teste dentro da WO 0048 derrubava a montagem do Jekyll. As capturas do dono de 18:16 e 21:05 mostram «v0.22.0» `[medido pelo chat]`, então o que ele testou foi a 0.22.0. O `.nojekyll` (WO 0050) desliga o Jekyll; o roteiro da 0.23.1 se refaz depois do deploy.
- **0.23.1 publicada e conferida:** o Pages montou o `786749d` sem erro e o site serve a v0.23.1 (WO 0050, `[medido pelo Code]`); o roteiro da 0.23.1 deu ok `[relatado pelo dono, 2026-11-17 21:25]`. Começa o recesso decidido pelo dono.
- **Este bloco substitui o anterior** (a 0.22.0 no clone). O que ele dizia está em `logs/2026-11-16.md`, Conversa 6.
````

### E03 — backlog: o recesso

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
1. **Conferir a 0.23.1 na tela** (dono): o roteiro do log de 2026-11-17, Conversa 2 (com `Ctrl+F5` antes, para o navegador largar a versão em cache). Depois dela, o recesso decidido pelo dono.
````

**Texto novo (substitui a ancora inteira):**

````
1. **Recesso** (decidido pelo dono): nada do app em andamento. Na volta, os itens abaixo.
````

## Depois de aplicar — conferencia antes do commit

| # | Checagem | Comando | Esperado |
|---|---|---|---|
| 1 | Os arquivos sao os previstos | `sha1sum meta/STATUS.md logs/2026-11-17.md` | a coluna **chegada** |
| 2 | O recesso no backlog | `grep -c '^1. \*\*Recesso\*\*' meta/STATUS.md` | `1` |
| 3 | Validacao | `python scripts/validate.py; echo "exit=$?"` | `exit=0`, versao 0.23.1 |
| 4 | Nada alem do previsto | `GIT_OPTIONAL_LOCKS=0 git status --short --untracked-files=all` | o STATUS, o log e esta WO |
| 5 | Depois do push: o CI | `gh run list --limit 1` e `gh run view <id> --json status,conclusion` ate `completed` | `success` |


As checagens 2 e 3 rodaram no clone do chat; no Git Bash, **nao testado**. O site nao muda (so documentos), entao nao ha deploy a medir.
**Esta e qual pergunta?** A 1 responde «esta la?»; a 5, «o CI segue verde?». Nada aqui muda o que se ve na tela.

## Relatorio de aplicacao

Grave em `../AAMMDD-HHMM-code-cancioneiro-apply-wo0051.txt`, com o carimbo de `date +%y%m%d-%H%M` rodado na hora. **Sem `/wrap` depois desta WO**, e sem secao sua no log, salvo se algo fugir do literal.

## Commit

```
git add meta/STATUS.md logs/2026-11-17.md meta/workorders/261117-wo0051-0-23-1-conferida-e-recesso.md
```

```
git commit -m "docs: 0.23.1 conferida na tela e inicio do recesso"
```

```
git push
```
