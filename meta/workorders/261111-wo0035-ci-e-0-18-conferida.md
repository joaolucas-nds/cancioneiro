# WO 0035 — 0.18.0 conferida, CI sem depender do apt, spec da rampa de BPM

## Cabecalho

> **Tipo:** registro e CI — `meta/STATUS.md` (5 edicoes) e `.github/workflows/testes.yml` (1 edicao), mais o versionamento de dois arquivos que o chat gravou. O app nao muda; a versao continua 0.18.0.
> **Config sugerida:** Sonnet · `/effort low`.
> **Pre-requisito:** commit `45312d5`, branch `main`, sincronizada com `origin/main`. O `git status --short` mostra exatamente: ` M logs/2026-11-11.md`, `?? meta/specs/261111-rampa-de-bpm.md` e `?? meta/workorders/261111-wo0035-ci-e-0-18-conferida.md`.
> **Base:** o dono relatou em 2026-11-11 12:06 «roteiro dos albuns ok» `[relatado pelo dono]`; o relatorio `261111-1157-code-cancioneiro-apply-wo0034.txt` mediu o CI caindo no `apt` (run 43036351737).
> **Depende de:** WO 0034 (`a67ee01`, wrap `45312d5`).
>
> | arquivo | partida (sha1) | chegada (sha1) |
> |---|---|---|
> | `meta/STATUS.md` | `7d64da20f19737119495faa1cd0f29714742c5b5` | `51f5eb84a39971c43a73115c8bb5ff1c27570d9d` |
> | `.github/workflows/testes.yml` | `362c6c03fe4e74a477e7e6daf18f362b25f37fe9` | `a0742d80416c6f8cbf5c9dfcdb68f11a1a1c2390` |
> | `meta/specs/261111-rampa-de-bpm.md` | `b75b1b1602cc37f16a7ad6bfec2df8b38322562c` | o mesmo (gravado pelo chat; so versionar) |
> | `logs/2026-11-11.md` | `7158063378c0661f074cf39dab90320e41c43482` | o mesmo (gravado pelo chat; so versionar) |
>
> **Ancora semantica:** se um trecho-ancora nao bater EXATAMENTE, PARE e reporte.
> **Idempotencia:** antes de cada edicao, procure o texto NOVO INTEIRO; se ja estiver la, PULE e diga no relatorio.
> **Ancoras:** linhas inteiras, cada uma 1 vez, na ordem abaixo. Toda edicao «substitui a ancora inteira».
> **Âncoras lidas em** (lidas pelo chat NESTE turno, do disco do dono em `45312d5`; aplicadas num clone, com a chegada medida):
> - E01 (`meta/STATUS.md`, cabeçalho: os álbuns conferidos): linha `**Versão atual:** 0.18.0 · **Fase:** 3a, 3a.2, o BPM da 3b, o prompt-modelo e as conveniên…`
> - E02 (`meta/STATUS.md`, última conversa: CI e conferência): linha `- **WO 0034 aplicada e empurrada (a67ee01, 2026-11-11):** 27 edições + tests/test_albun…`
> - E03 (`meta/STATUS.md`, pendência do CI: o passo novo): linha `- **CI do a67ee01 sem veredito** — falha de rede do runner no passo «Dependencias», duas…`
> - E04 (`meta/STATUS.md`, pendência: sai conferir os álbuns, entra decidir a rampa): linha `- **Conferir organizar os álbuns na tela** — roteiro na conversa de 2026-11-09 (WO 0034), …`
> - E05 (`meta/STATUS.md`, backlog: o defeito medido): linha `1. **Rampa de BPM** (i-042) — três faixas BR reprovam no validate.py por mudarem de anda…`
> - E06 (`.github/workflows/testes.yml`, instalar sem depender do apt): linha `          python -m playwright install --with-deps chromium`
> **Canal dos meta neste ciclo = CODE:** o STATUS e do Code (DEC-010); a spec e o log ja estao gravados pelo chat.

---

## 1. Por que

A 0.18.0 foi conferida na tela pelo dono; a pendencia sai do STATUS. O CI do `a67ee01` nao rodou teste nenhum: o
`playwright install --with-deps` depende do `apt` do runner, que ficou sem DNS. As bibliotecas do sistema ja vem no
runner do GitHub; o passo passa a instalar o navegador sozinho e a tentar as bibliotecas tres vezes, com limite de
tempo, sem derrubar o job — faltando biblioteca de verdade, o passo «Navegador» acusa. E a spec da rampa de BPM
(i-042) entra no repo, em rascunho.

## Edicao 0 — Conferencia de hash e de arvore

```
sha1sum meta/STATUS.md .github/workflows/testes.yml meta/specs/261111-rampa-de-bpm.md logs/2026-11-11.md
GIT_OPTIONAL_LOCKS=0 git status --short
```

Os quatro batem com **partida**; o `git status` mostra exatamente as tres linhas do Pre-requisito. Qualquer outra coisa: **PARE e reporte**.

## Edicoes E01 a E06

Na ordem. Copie o que esta ENTRE as linhas de quatro crases, sem elas. Aplique por script, extraindo os blocos da WO.

### E01 — cabeçalho: os álbuns conferidos

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
**Versão atual:** 0.18.0 · **Fase:** 3a, 3a.2, o BPM da 3b, o prompt-modelo e as conveniências de uso concluídos e conferidos · os álbuns antigos convertidos (i-008, fora do repo) · curadoria no app concluída nas três entregas (DEC-028, DEC-029) · frente de interface concluída e conferida nas quatro entregas (DEC-030 a DEC-033) · organizar os álbuns (0.18.0, DEC-035) à espera da conferência na tela · kit de música lido pelo KCM, à espera da resposta (i-039)
````

**Texto novo (substitui a ancora inteira):**

````
**Versão atual:** 0.18.0 · **Fase:** 3a, 3a.2, o BPM da 3b, o prompt-modelo e as conveniências de uso concluídos e conferidos · os álbuns antigos convertidos (i-008, fora do repo) · curadoria no app concluída nas três entregas (DEC-028, DEC-029) · frente de interface concluída e conferida nas quatro entregas (DEC-030 a DEC-033) · organizar os álbuns (0.18.0, DEC-035) conferido · rampa de BPM (i-042) em spec · kit de música lido pelo KCM, à espera da resposta (i-039)
````

### E02 — última conversa: CI e conferência

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
- **WO 0034 aplicada e empurrada (`a67ee01`, 2026-11-11):** 27 edições + `tests/test_albuns.py`, 9 sha1 de chegada conferidos, `validate.py` exit=0 (só sintaxe: `jsonschema` ausente nesta máquina). **CI vermelho, mas sem rodar teste algum:** o run `43036351737` caiu nas duas tentativas no passo «Dependencias» (`apt`: `Temporary failure resolving 'azure.archive.ubuntu.com'`); «Validar», «Conversores» e «Navegador» foram pulados `[medido por instrumento]`. Os 44 testes seguem sem veredito no CI.
````

**Texto novo (substitui a ancora inteira):**

````
- **WO 0034 aplicada e empurrada (`a67ee01`, 2026-11-11):** 27 edições + `tests/test_albuns.py`, 9 sha1 de chegada conferidos, `validate.py` exit=0 (só sintaxe: `jsonschema` ausente nesta máquina). **CI vermelho, mas sem rodar teste algum:** o run `43036351737` caiu nas duas tentativas no passo «Dependencias» (`apt`: `Temporary failure resolving 'azure.archive.ubuntu.com'`); «Validar», «Conversores» e «Navegador» foram pulados `[medido por instrumento]`. Os 44 testes seguem sem veredito no CI; a WO 0035 tira o `apt` do caminho do passo «Dependencias». **0.18.0 conferida na tela pelo dono** em 2026-11-11 (os 8 itens do roteiro OK `[relatado pelo dono]`).
- **Rampa de BPM (i-042):** medido que o app reescreve a rampa sem ninguém mexer no controle («95 BPM building to 115 BPM» copia como «95 BPM building to 95 bpm»); protótipo no canvas e spec `meta/specs/261111-rampa-de-bpm.md` em rascunho, com quatro pontos para o dono.
````

### E03 — pendência do CI: o passo novo

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
- **CI do `a67ee01` sem veredito** — falha de rede do runner no passo «Dependencias», duas vezes. Re-rodar (`gh run rerun 43036351737 --failed`) ou empurrar de novo; se repetir, WO para o passo de instalação do `testes.yml` (cache ou nova tentativa).
````

**Texto novo (substitui a ancora inteira):**

````
- **CI do `a67ee01` sem veredito** — falha de rede do runner no passo «Dependencias», duas vezes. A WO 0035 muda o passo de instalação (o navegador sozinho; as bibliotecas do sistema com três tentativas de 3 minutos, sem derrubar o job). Conferir o veredito no push dela.
````

### E04 — pendência: sai conferir os álbuns, entra decidir a rampa

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
- **Conferir organizar os álbuns na tela** — roteiro na conversa de 2026-11-09 (WO 0034), depois do push, no computador e no celular.
````

**Texto novo (substitui a ancora inteira):**

````
- **Decidir os quatro pontos da rampa de BPM** — no fim de `meta/specs/261111-rampa-de-bpm.md`; o protótipo está no canvas «Cancioneiro: nova interface», tela «0.19 · rampa de BPM».
````

### E05 — backlog: o defeito medido

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
1. **Rampa de BPM** (i-042) — três faixas BR reprovam no `validate.py` por mudarem de andamento de propósito.
````

**Texto novo (substitui a ancora inteira):**

````
1. **Rampa de BPM** (i-042) — três faixas BR reprovam no `validate.py` por mudarem de andamento de propósito, e o app copia a rampa com o segundo número trocado pelo primeiro; spec em rascunho.
````

### E06 — instalar sem depender do apt

**Arquivo:** `.github/workflows/testes.yml`

**Ancora:**

````
          python -m playwright install --with-deps chromium
````

**Texto novo (substitui a ancora inteira):**

````
          python -m playwright install chromium
          # As bibliotecas do sistema ja vem no runner do GitHub. O apt do runner as vezes
          # fica sem DNS (2026-11-11, run 43036351737): tres tentativas de 3 minutos, e o job
          # segue se falharem. Faltando biblioteca de verdade, o passo «Navegador» acusa.
          for i in 1 2 3; do
            timeout 180 python -m playwright install-deps chromium && break
            echo "install-deps falhou ($i de 3)"; sleep 15
          done
````

## Depois de aplicar — conferencia antes do commit

| # | Checagem | Comando | Esperado |
|---|---|---|---|
| 1 | Os quatro sao os previstos | `sha1sum meta/STATUS.md .github/workflows/testes.yml meta/specs/261111-rampa-de-bpm.md logs/2026-11-11.md` | a coluna **chegada** |
| 2 | A pendencia saiu | `grep -c '^- \*\*Conferir organizar os álbuns' meta/STATUS.md` | `0` (linhas) |
| 3 | O passo novo | `grep -c 'with-deps' .github/workflows/testes.yml` | `0` |
| 4 | Validacao | `python3 scripts/validate.py; echo "exit=$?"` | `exit=0`, versao 0.18.0 |
| 5 | Nada alem do previsto | `GIT_OPTIONAL_LOCKS=0 git status --short --untracked-files=all` | os quatro e esta WO |
| 6 | Depois do push: o CI | `gh run list --limit 1`, em laco com `gh run view <id> --json status,conclusion` ate `completed` (o `gh run watch` passa dos 300 s) | relate o estado cru e, se vermelho, o passo que caiu (`gh run view <id> --log-failed`, as ultimas 30 linhas) |

As checagens 2 e 3 rodaram no clone do chat, shell Linux; no Git Bash, **nao testado**. O workflow nao pode ser testado fora do GitHub: o chat conferiu o YAML e a sintaxe do bash; o veredito e o da checagem 6.
**Esta e qual pergunta?** A 1 responde «esta la?»; a 6 e a primeira vez que os 44 testes rodam no CI desde a 0.18.0.

## Relatorio de aplicacao

Grave em `../AAMMDD-HHMM-code-cancioneiro-apply-wo0035.txt`, com o carimbo de `date +%y%m%d-%H%M` rodado na hora. Checagem 1 em primeiro lugar e o estado final do CI. **Sem `/wrap` depois desta WO**, e sem secao sua no log, salvo se algo fugir do literal.

## Commit

```
git add meta/STATUS.md .github/workflows/testes.yml meta/specs/261111-rampa-de-bpm.md logs/2026-11-11.md meta/workorders/261111-wo0035-ci-e-0-18-conferida.md
```

```
git commit -m "ci: instalar o navegador sem depender do apt; 0.18.0 conferida" -m "O passo Dependencias instala o Chromium e tenta as bibliotecas do sistema tres vezes, sem derrubar o job. STATUS com a conferencia da 0.18.0; spec da rampa de BPM (i-042) em rascunho; log de 2026-11-11."
```

```
git push
```
