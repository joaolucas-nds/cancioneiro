# WO 0031 — I4 conferida na tela: STATUS

## Cabecalho

> **Tipo:** registro — so `meta/STATUS.md` (4 edicoes literais) e o versionamento do log novo que o chat gravou.
> **Config sugerida:** Sonnet · `/effort low`.
> **Pre-requisito:** commit `dc99fb0`, branch `main`, sincronizada com `origin/main`. O `git status --short` mostra exatamente: `?? logs/2026-11-09.md` e `?? meta/workorders/261109-wo0031-i4-conferida.md`.
> **Base:** o dono relatou no chat, em 2026-11-09 09:51, «roteiro da I4 ok» — os 10 itens do roteiro de tela da WO 0030 `[relatado pelo dono]`.
> **Depende de:** WO 0030 (`dc99fb0`).
>
> | arquivo | partida (sha1) | chegada (sha1) |
> |---|---|---|
> | `meta/STATUS.md` | `3a5a1eae0f3fab5f98a783bb6b4b7fe26404133e` | `33ec44ced1152b99ad41959012ce746821fd1f67` |
> | `logs/2026-11-09.md` | `abb8d19e47919eca9015cc3cc87ee618607ed8ca` | o mesmo (arquivo novo do chat; so versionar) |
>
> **Ancora semantica:** se um trecho-ancora nao bater EXATAMENTE, PARE e reporte.
> **Idempotencia:** antes de cada edicao, procure o texto NOVO INTEIRO; se ja estiver la, PULE e diga no relatorio.
> **Ancoras:** linhas inteiras, cada uma 1 vez no estado em que a edicao e aplicada, na ordem abaixo. A E03 leva o titulo da secao, a linha vazia e a linha que sai.
> **Âncoras lidas em** (lidas pelo chat NESTE turno, do disco, em `dc99fb0`; o chat aplicou as quatro numa copia e mediu o sha1 de chegada):
> - E01: `meta/STATUS.md`, linha que comeca `**Versão atual:** 0.17.0 · **Fase:**`.
> - E02: `meta/STATUS.md`, linha que comeca `- **I4, salvar no arquivo (0.17.0):**` e termina `falta a conferência na tela pelo dono.`
> - E03: `meta/STATUS.md`, titulo `## Pendências do dono`, a linha vazia e a linha que comeca `- **Conferir a I4 na tela**`.
> - E04: `meta/STATUS.md`, linha que comeca `- **Salvar no arquivo** (0.17.0, DEC-033)` e termina `O «Desfazer» continua depois de salvar.`
> **Canal dos meta neste ciclo = CODE:** o STATUS e do Code (DEC-010); o log ja esta gravado pelo chat.

---

## 1. Por que

A I4 (0.17.0) foi conferida na tela pelo dono. A pendencia «Conferir a I4 na tela» sai do STATUS; entra no lugar dela
apagar o arquivo de teste da sonda, que ficou na pasta-pai. Nada de codigo; a versao continua 0.17.0.

## Edicao 0 — Conferencia de hash e de arvore

```
sha1sum meta/STATUS.md logs/2026-11-09.md
GIT_OPTIONAL_LOCKS=0 git status --short
```

Os dois batem com a coluna **partida**; o `git status` mostra exatamente as duas linhas do Pre-requisito. Qualquer outra coisa: **PARE e reporte**.

## Edicoes E01 a E04 (todas em `meta/STATUS.md`)

Na ordem. Copie o que esta ENTRE as linhas de quatro crases, sem elas.

### E01 — cabeçalho: a frente de interface fechada

**Ancora (linhas inteiras, 1 ocorrencia):**

````
**Versão atual:** 0.17.0 · **Fase:** 3a, 3a.2, o BPM da 3b, o prompt-modelo e as conveniências de uso concluídos e conferidos · os álbuns antigos convertidos (i-008, fora do repo) · curadoria no app concluída nas três entregas (DEC-028, DEC-029) · frente de interface nas quatro entregas, a I4 à espera da conferência na tela (DEC-030 a DEC-033) · kit de música lido pelo KCM, à espera da resposta (i-039)
````

**Texto novo (substitui a ancora inteira):**

````
**Versão atual:** 0.17.0 · **Fase:** 3a, 3a.2, o BPM da 3b, o prompt-modelo e as conveniências de uso concluídos e conferidos · os álbuns antigos convertidos (i-008, fora do repo) · curadoria no app concluída nas três entregas (DEC-028, DEC-029) · frente de interface concluída e conferida nas quatro entregas (DEC-030 a DEC-033) · kit de música lido pelo KCM, à espera da resposta (i-039)
````

### E02 — última conversa: a I4 conferida

**Ancora (linhas inteiras, 1 ocorrencia):**

````
- **I4, salvar no arquivo (0.17.0):** os cinco pontos decididos pelo dono como recomendados (DEC-033); 14 de 14 critérios no Chromium headless, testados pelo chat; falta a conferência na tela pelo dono.
````

**Texto novo (substitui a ancora inteira):**

````
- **I4, salvar no arquivo (0.17.0):** os cinco pontos decididos pelo dono como recomendados (DEC-033); 14 de 14 critérios no Chromium headless, testados pelo chat. **Conferida na tela pelo dono** em 2026-11-09 (os 10 itens do roteiro OK `[relatado pelo dono]`): salvar no arquivo está fechado.
````

### E03 — pendências do dono: sai «Conferir a I4 na tela»

**Ancora (linhas inteiras, 1 ocorrencia):**

````
## Pendências do dono

- **Conferir a I4 na tela** — roteiro na conversa de 2026-11-06 (WO 0030), depois do push, no Chrome do computador (com fechar e reabrir o app) e no celular. Apagar à mão o `..\sonda-i4-teste.json`.
````

**Texto novo (substitui a ancora inteira):**

````
## Pendências do dono

- **Apagar à mão o `..\sonda-i4-teste.json`** — arquivo de teste da sonda, na pasta-pai (o chat não apaga arquivo seu).
````

### E04 — Funciona: «Salvar no arquivo» conferido

**Ancora (linhas inteiras, 1 ocorrencia):**

````
- **Salvar no arquivo** (0.17.0, DEC-033): no Chrome e no Edge do computador, «Salvar» (ou `Ctrl+S`) grava no próprio `.json`; o primeiro «Salvar» de um acervo pede o arquivo na janela do sistema, e importar pela janela ou soltar o arquivo já vinculam. Antes de gravar, confere se o arquivo mudou fora. O ▾ tem «Salvar em outro arquivo…» e «Baixar .json»; o seletor de acervo mostra o vínculo e «Desvincular». Firefox, Safari e o celular baixam. O «Desfazer» continua depois de salvar.
````

**Texto novo (substitui a ancora inteira):**

````
- **Salvar no arquivo** (0.17.0, DEC-033): no Chrome e no Edge do computador, «Salvar» (ou `Ctrl+S`) grava no próprio `.json`; o primeiro «Salvar» de um acervo pede o arquivo na janela do sistema, e importar pela janela ou soltar o arquivo já vinculam. Antes de gravar, confere se o arquivo mudou fora. O ▾ tem «Salvar em outro arquivo…» e «Baixar .json»; o seletor de acervo mostra o vínculo e «Desvincular». Firefox, Safari e o celular baixam. O «Desfazer» continua depois de salvar. Conferido na tela pelo dono em 2026-11-09.
````

## Depois de aplicar — conferencia antes do commit

| # | Checagem | Comando | Esperado |
|---|---|---|---|
| 1 | Os dois arquivos sao os previstos | `sha1sum meta/STATUS.md logs/2026-11-09.md` | a coluna **chegada**, os dois |
| 2 | A pendencia saiu | `grep -c '^- \*\*Conferir a I4 na tela' meta/STATUS.md` | `0` |
| 3 | A conferencia entrou | `grep -c 'Conferido na tela pelo dono em 2026-11-09' meta/STATUS.md` | `1` (linhas) |
| 4 | Validacao | `python3 scripts/validate.py; echo "exit=$?"` | `exit=0`, com `OK  versao 0.17.0 igual em CHANGELOG, app, README e STATUS` |
| 5 | Nada alem do previsto | `GIT_OPTIONAL_LOCKS=0 git status --short --untracked-files=all` | os dois arquivos e esta WO |

As checagens 2 e 3 foram rodadas pelo chat na copia, no shell Linux; no Git Bash, **nao testado** — com a 1 verde, relate o cru e nao pare.
**Esta e qual pergunta?** «Esta la?»; o «presta?» da I4 o dono ja respondeu na tela.

## Relatorio de aplicacao

Grave em `../AAMMDD-HHMM-code-cancioneiro-apply-wo0031.txt`, com o carimbo de `date +%y%m%d-%H%M` rodado na hora. Diga o resultado da checagem 1 em primeiro lugar. **Sem `/wrap` depois desta WO**, e sem secao sua no log, salvo se algo fugir do literal (entao diga no relatorio que o sha1 do log mudou).

## Commit

```
git add meta/STATUS.md logs/2026-11-09.md meta/workorders/261109-wo0031-i4-conferida.md
```

```
git commit -m "docs: I4 conferida na tela, status e log de 2026-11-09" -m "O dono conferiu a I4 (0.17.0) pelo roteiro de tela; a frente de interface fecha nas quatro entregas."
```

```
git push
```
