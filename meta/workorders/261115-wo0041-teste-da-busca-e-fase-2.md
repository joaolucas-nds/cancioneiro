# WO 0041 — O teste do Ctrl+Z na busca espera a descida; a Fase 2 fecha

## Cabecalho

> **Tipo:** um teste (o app nao muda) e meta. Sem versao nova: o app continua 0.20.0.
> **Config sugerida:** Sonnet · `/effort low` (aplicacao literal por script; 5 edicoes).
> **Pre-requisito:** commit `fb9cd70`, branch `main`, sincronizada com `origin/main`. O `git status --short` mostra exatamente: ` M logs/2026-11-15.md` e `?? meta/workorders/261115-wo0041-teste-da-busca-e-fase-2.md`.
> **Base:** relatorio `261115-1749` (CI vermelho no run `43760238300`); a corrida reproduzida pelo chat no clone (log de 2026-11-15, Conversa 3).
> **Depende de:** `fb9cd70` (WO 0040).
>
> | arquivo | partida (sha1) | chegada (sha1) |
> |---|---|---|
> | `tests/test_organizar.py` | `a69e87a11ccb43c572355d0fda87c517ab996051` | `f7bdc6428b9a8c3063465c6e2dbd727a6664cb2d` |
> | `meta/ROADMAP.md` | `a60dd592b561f524e00f5e4dc48b52648208f422` | `526c6116cdfa6e499b7c826d82bef056c68d07ff` |
> | `meta/STATUS.md` | `963e037506cb585b56eab80b6436e2102370c6d6` | `3926ee6420cf63d29df4a8e8dabd7b99258c532f` |
> | `logs/2026-11-15.md` | `75cb468b3f427bb8d98dea8248dcdf169079ad4c` | o mesmo (gravado pelo chat; so versionar) |
>
> **Ancora semantica:** se um trecho-ancora nao bater EXATAMENTE, PARE e reporte.
> **Idempotencia:** antes de cada edicao, procure o texto NOVO INTEIRO; se ja estiver la, PULE e diga no relatorio.
> **Ancoras:** linhas inteiras (uma linha ou um bloco de linhas inteiras), cada uma 1 vez no arquivo no momento da edicao, na ordem abaixo. Toda edicao «substitui a ancora inteira».
> **Âncoras lidas em** (lidas pelo chat NESTE turno, de `fb9cd70` clonado do GitHub e conferido contra o disco do dono — os arquivos versionados com o mesmo sha1; aplicadas em ordem num clone, com a chegada medida):
> - E01 (`tests/test_organizar.py`, o teste espera a descida antes de digitar): bloco de 2 linhas, começando por `    page.click("#tm-down")`
> - E02 (`meta/ROADMAP.md`, Fase 2 concluída): linha `## 🔨 Fase 2 — Ferramenta v0 (MVP de leitura + cópia)`
> - E03 (`meta/STATUS.md`, última conversa: a WO 0040 e o CI): bloco de 2 linhas, começando por `- **Cartas 01 e 02 do projeto Rainha respondidas** pela carta 01 do Cancioneiro (na past…`
> - E04 (`meta/STATUS.md`, quebrado: o CI do fb9cd70): linha `- **CI do '39ff8d8' vermelho em 2 testes da 0.20.0** (run '43601104563', '[medido pelo C…`
> - E05 (`meta/STATUS.md`, pendência: o comando do validador no Windows): linha `- **Instalar o validador de esquema nesta máquina.** Sem 'jsonschema' e 'referencing', o…`
> **Canal dos meta neste ciclo = CODE:** STATUS e ROADMAP pelo Code (DEC-010); o log ja esta gravado pelo chat.

---

## 1. Por que

O `test_ctrl_z_na_busca_nao_mexe_no_acervo` reprovou no CI de um commit so de doc. A descida termina devolvendo o foco a linha; no CI lento, o `Ctrl+Z` do teste chegava antes, fora da busca, e desfazia. O chat reproduziu atrasando a descida em 400 ms: o teste velho reprova com o mesmo 0, o novo passa. O teste passa a esperar a descida. Junto: a Fase 2 fecha no ROADMAP (o marco veio com o projeto Rainha) e a pendencia do validador ganha o comando do Windows.

## Edicao 0 — Conferencia de hash e de arvore

```
sha1sum tests/test_organizar.py meta/ROADMAP.md meta/STATUS.md logs/2026-11-15.md
GIT_OPTIONAL_LOCKS=0 git status --short
```

Todos batem com **partida**; o `git status` mostra exatamente as duas linhas do Pre-requisito. Qualquer outra coisa: **PARE e reporte**.

## Edicoes E01 a E05

Na ordem. Copie o que esta ENTRE as linhas de quatro crases, sem elas. Aplique por script, extraindo os blocos da WO; grave em UTF-8 com LF.

### E01 — o teste espera a descida antes de digitar

**Arquivo:** `tests/test_organizar.py`

**Ancora:**

````
    page.click("#tm-down")
    page.fill("#search", "x")
````

**Texto novo (substitui a ancora inteira):**

````
    page.click("#tm-down")
    # espera a descida terminar: no fim ela devolve o foco a linha, e um Ctrl+Z
    # que chegue antes disso cai fora da busca e desfaz (CI do fb9cd70)
    page.wait_for_function("App.changes === 1")
    page.fill("#search", "x")
````

### E02 — Fase 2 concluída

**Arquivo:** `meta/ROADMAP.md`

**Ancora:**

````
## 🔨 Fase 2 — Ferramenta v0 (MVP de leitura + cópia)
````

**Texto novo (substitui a ancora inteira):**

````
## ✅ Fase 2 — Ferramenta v0 (MVP de leitura + cópia) (2026-11-15: o marco, usar numa rodada de geração de verdade, veio com o projeto Rainha da Preguiça)
````

### E03 — última conversa: a WO 0040 e o CI

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
- **Cartas 01 e 02 do projeto Rainha respondidas** pela carta 01 do Cancioneiro (na pasta-pai deles): a 02 entra na WO 0040; o fim de faixa (01) espera a medição deles (i-056). **Carta 05 ao KCM:** a `macetes-suno` e a `revisar-faixa` mudaram depois do `110e0ba`.
- **Este bloco substitui o anterior** (0.20.0 conferida, carta 03, WO 0039). O que ele dizia está na DEC-038 e em `logs/2026-11-14.md`.
````

**Texto novo (substitui a ancora inteira):**

````
- **Cartas 01 e 02 do projeto Rainha respondidas** pela carta 01 do Cancioneiro (na pasta-pai deles): a 02 entra na WO 0040; o fim de faixa (01) espera a medição deles (i-056). **Carta 05 ao KCM:** a `macetes-suno` e a `revisar-faixa` mudaram depois do `110e0ba`.
- **WO 0040 aplicada** (`fb9cd70`); o CI ficou vermelho num teste antigo, por corrida (Quebrado, abaixo); a WO 0041 corrige e fecha a Fase 2 no ROADMAP (o marco veio com o projeto Rainha).
- **Este bloco substitui o anterior** (0.20.0 conferida, carta 03, WO 0039). O que ele dizia está na DEC-038 e em `logs/2026-11-14.md`.
````

### E04 — quebrado: o CI do fb9cd70

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
- **CI do `39ff8d8` vermelho em 2 testes da 0.20.0** (run `43601104563`, `[medido pelo Code]`): corrida no texto dos testes C5, não no app; a WO 0039 corrige. **Corrigido em `110e0ba`: CI verde** (run `43607766930`, `completed success`) `[medido pelo Code]`. Sem pendência de CI.
````

**Texto novo (substitui a ancora inteira):**

````
- **CI do `fb9cd70` vermelho em 1 teste antigo** (run `43760238300`, `test_ctrl_z_na_busca_nao_mexe_no_acervo`, `[medido pelo Code]`), num commit só de doc: corrida no teste, não no app. A descida devolve o foco à linha no fim, e no CI lento o `Ctrl+Z` chegava antes, fora da busca, e desfazia. O chat reproduziu atrasando a descida em 400 ms: o teste velho reprova com o mesmo 0, o novo passa. A WO 0041 faz o teste esperar a descida.
````

### E05 — pendência: o comando do validador no Windows

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
- **Instalar o validador de esquema nesta máquina.** Sem `jsonschema` e `referencing`, o `validate.py` só confere sintaxe e diz `ESQUEMA NAO CONFERIDO` na última linha. Uma vez, no CMD: `pip install jsonschema referencing --break-system-packages`. Depois, `python3 scripts/validate.py` deve terminar em `Tudo conforme ao esquema.` Desde a DEC-034 o CI confere o esquema a cada push: instalar aqui passa a ser opcional.
````

**Texto novo (substitui a ancora inteira):**

````
- **Instalar o validador de esquema nesta máquina.** Sem `jsonschema` e `referencing`, o `validate.py` só confere sintaxe e diz `ESQUEMA NAO CONFERIDO` na última linha. Uma vez, no CMD: `python -m pip install jsonschema referencing` (no Windows, `python3` é o atalho da loja, não o Python instalado — relatório da WO 0040). Depois, `python scripts\validate.py` deve terminar em `Tudo conforme ao esquema.` Desde a DEC-034 o CI confere o esquema a cada push: instalar aqui passa a ser opcional.
````

## Depois de aplicar — conferencia antes do commit

| # | Checagem | Comando | Esperado |
|---|---|---|---|
| 1 | Os arquivos sao os previstos | `sha1sum tests/test_organizar.py meta/ROADMAP.md meta/STATUS.md logs/2026-11-15.md` | a coluna **chegada** |
| 2 | O teste espera a descida | `grep -c 'wait_for_function("App.changes === 1")' tests/test_organizar.py` | `1` |
| 3 | A Fase 2 fechada | `grep -c '^## ✅ Fase 2' meta/ROADMAP.md` | `1` |
| 4 | Validacao | `python scripts/validate.py; echo "exit=$?"` | `exit=0` |
| 5 | Nada alem do previsto | `GIT_OPTIONAL_LOCKS=0 git status --short --untracked-files=all` | os 4 arquivos da tabela e esta WO |
| 6 | Depois do push: o CI | `gh run list --limit 1`, em laco com `gh run view <id> --json status,conclusion` ate `completed` | `success`; se vermelho, o passo e as ultimas 30 linhas de `gh run view <id> --log-failed` |

As checagens 2 a 4 rodaram no clone do chat; no Git Bash, **nao testado**. O chat rodou os 61 testes duas vezes no clone (cerca de 43 s). O veredito e o CI (checagem 6).
**Esta e qual pergunta?** A 1 responde «esta la?»; a 6, «o CI volta ao verde?».

## Relatorio de aplicacao

Grave em `../AAMMDD-HHMM-code-cancioneiro-apply-wo0041.txt`, com o carimbo de `date +%y%m%d-%H%M` rodado na hora. Checagem 1 em primeiro lugar e o estado final do CI. **Sem `/wrap` depois desta WO**, e sem secao sua no log, salvo se algo fugir do literal.

## Commit

```
git add tests/test_organizar.py meta/ROADMAP.md meta/STATUS.md logs/2026-11-15.md meta/workorders/261115-wo0041-teste-da-busca-e-fase-2.md
```

```
git commit -m "test: o Ctrl+Z na busca espera a descida; Fase 2 concluida" -m "O teste lia o foco antes da descida terminar e desfazia no CI lento (run 43760238300). ROADMAP fecha a Fase 2; STATUS com o comando do validador no Windows."
```

```
git push
```
