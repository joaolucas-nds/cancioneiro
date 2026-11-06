# WO 0029 — I3 conferida e I4 em spec: STATUS, spec e log

## Cabecalho

> **Tipo:** registro — so `meta/STATUS.md` (6 edicoes literais) e o versionamento de dois arquivos que o chat gravou.
> **Config sugerida:** Sonnet · `/effort low`.
> **Pre-requisito:** commit `0142e55`, branch `main`, sincronizada com `origin/main`. O `git status --short` mostra exatamente tres linhas: ` M logs/2026-11-06.md`, `?? meta/specs/261106-salvar-no-arquivo.md` e `?? meta/workorders/261106-wo0029-i3-conferida-e-i4-spec.md`.
> **Base:** a WO 0028 foi recusada (`0142e55`, cabecalho sem «Ancoras lidas em»). Esta a substitui, com as quatro edicoes dela sobre o STATUS de agora, mais o registro da I4 (conversa 9 do chat, 2026-11-06). A conferencia da I3 e `[relatado pelo dono, 2026-11-06 15:37]`, ja no log (Conversa 7).
> **Depende de:** nada alem do pre-requisito. A WO 0028 NAO se aplica mais: fica versionada como registro da recusa.
>
> **Arquivos que o chat gravou no disco e esta WO versiona** (sha1 medido pelo chat ao gravar):
>
> | arquivo | partida (sha1) | chegada (sha1) |
> |---|---|---|
> | `meta/STATUS.md` | `706de2361cef94b73e513f53270a023efc02807d` | `ea2e69fbfaec3fe4a0b7848e0c1f8f8fda8fe9bf` |
> | `logs/2026-11-06.md` | `5ed3da14c9b0d23cc2da193dca5a8162f945b094` | o mesmo (Conversa 9 gravada pelo chat; so versionar) |
> | `meta/specs/261106-salvar-no-arquivo.md` | `d960032f197fa59d7f612e3cdae0c3faf1aca10d` | o mesmo (arquivo novo do chat; so versionar) |
>
> **Ancora semantica:** se um trecho-ancora nao bater EXATAMENTE, PARE e reporte.
> **Idempotencia:** antes de cada edicao, procure o texto NOVO INTEIRO; se ja estiver la, PULE e diga no relatorio.
> **Ancoras:** linhas inteiras, cada uma ocorrendo exatamente 1 vez no estado em que a edicao e aplicada, na ordem abaixo. A E04 leva o titulo da secao, a linha vazia e a linha que sai.
> **Âncoras lidas em** (lidas pelo chat NESTE turno, do disco, em `0142e55`; o chat aplicou as seis numa copia e mediu o sha1 de chegada acima):
> - E01: `meta/STATUS.md`, linha que começa `**Versão atual:** 0.16.0 · **Fase:**` e termina `à espera da resposta (i-039)`.
> - E02: `meta/STATUS.md`, linha `- **WO 0027 aplicada e empurrada** (`6a07bfd`, 0.16.0): validação verde; falta só a conferência da I3 na tela pelo dono.`.
> - E03: `meta/STATUS.md`, linha que começa `- **WO 0028 (I3 conferida, só STATUS) recusada pelo Code:**` e termina `segue no STATUS até lá.`.
> - E04: `meta/STATUS.md`, título `## Pendências do dono`, a linha vazia e a linha `- **Conferir a I3 na tela** — roteiro na conversa de 2026-11-06 (WO 0027), depois do push, no computador e no celular.`.
> - E05: `meta/STATUS.md`, linha que começa `- **Organizar** (0.16.0, DEC-030, DEC-032):` e termina `com o hash no `validate.py`.`.
> - E06: `meta/STATUS.md`, linha que começa `1. **I4 — Salvar no arquivo** (i-043, DEC-030) — protótipo no canvas, depois spec:` e termina `sem baixar e substituir à mão.`.
> **Canal dos meta neste ciclo = CODE:** o STATUS e do Code (DEC-010); o log e a spec ja estao gravados pelo chat.

---

## 1. Por que

A I3 (0.16.0) foi conferida na tela pelo dono, e a WO 0028, que registrava isso, foi recusada por falta do campo
«Ancoras lidas em». Na mesma conversa o chat fez o prototipo e a spec da I4. O STATUS (rolante) tira a pendencia da
I3, registra a recusa e a I4, e poe a sonda da I4 nas pendencias do dono. Nada de codigo; a versao continua 0.16.0.

## Edicao 0 — Conferencia de hash e de arvore

```
sha1sum meta/STATUS.md logs/2026-11-06.md meta/specs/261106-salvar-no-arquivo.md
GIT_OPTIONAL_LOCKS=0 git status --short
```

Os tres batem com a coluna **partida**; o `git status` mostra exatamente as tres linhas do Pre-requisito. Qualquer outra coisa: **PARE e reporte**.

## Edicoes E01 a E06 (todas em `meta/STATUS.md`)

Na ordem. Copie o que esta ENTRE as linhas de quatro crases, sem elas.

### E01 — cabeçalho: a I3 conferida, a I4 em spec

**Ancora (linhas inteiras, 1 ocorrencia):**

````
**Versão atual:** 0.16.0 · **Fase:** 3a, 3a.2, o BPM da 3b, o prompt-modelo e as conveniências de uso concluídos e conferidos · os álbuns antigos convertidos (i-008, fora do repo) · curadoria no app concluída nas três entregas (DEC-028, DEC-029) · frente de interface na I3 de quatro (DEC-030 a DEC-032) · kit de música lido pelo KCM, à espera da resposta (i-039)
````

**Texto novo (substitui a ancora inteira):**

````
**Versão atual:** 0.16.0 · **Fase:** 3a, 3a.2, o BPM da 3b, o prompt-modelo e as conveniências de uso concluídos e conferidos · os álbuns antigos convertidos (i-008, fora do repo) · curadoria no app concluída nas três entregas (DEC-028, DEC-029) · frente de interface com a I3 conferida e a I4 em spec (DEC-030 a DEC-032) · kit de música lido pelo KCM, à espera da resposta (i-039)
````

### E02 — última conversa: a conferência da I3

**Ancora (linhas inteiras, 1 ocorrencia):**

````
- **WO 0027 aplicada e empurrada** (`6a07bfd`, 0.16.0): validação verde; falta só a conferência da I3 na tela pelo dono.
````

**Texto novo (substitui a ancora inteira):**

````
- **WO 0027 aplicada e empurrada** (`6a07bfd`, 0.16.0): validação verde. **I3 conferida na tela pelo dono** (os 11 itens do roteiro OK `[relatado pelo dono, 2026-11-06]`): organizar está fechado.
````

### E03 — última conversa: a recusa da WO 0028 e a I4

**Ancora (linhas inteiras, 1 ocorrencia):**

````
- **WO 0028 (I3 conferida, só STATUS) recusada pelo Code:** o cabeçalho não traz «Âncoras lidas em». Nada aplicado; falta o chat reemitir a WO com o campo. A pendência «Conferir a I3 na tela» segue no STATUS até lá.
````

**Texto novo (substitui a ancora inteira):**

````
- **WO 0028 recusada pelo Code** (cabeçalho sem «Âncoras lidas em») e reemitida pelo chat como WO 0029, com o campo.
- **I4, salvar no arquivo:** protótipo no canvas (fileira da I4), spec `meta/specs/261106-salvar-no-arquivo.md` em rascunho, com cinco pontos para o dono, e a sonda `../261106-sonda-i4-salvar.html` para ele rodar no Chrome antes de decidir.
````

### E04 — pendências do dono: sai «Conferir a I3», entra a sonda

**Ancora (linhas inteiras, 1 ocorrencia):**

````
## Pendências do dono

- **Conferir a I3 na tela** — roteiro na conversa de 2026-11-06 (WO 0027), depois do push, no computador e no celular.
````

**Texto novo (substitui a ancora inteira):**

````
## Pendências do dono

- **Rodar a sonda da I4 e decidir os cinco pontos** — abrir `..\261106-sonda-i4-salvar.html` no Chrome, seguir os passos da página e salvar o relatório na pasta-pai; os pontos estão no fim de `meta/specs/261106-salvar-no-arquivo.md`.
````

### E05 — Funciona: «Organizar» conferido

**Ancora (linhas inteiras, 1 ocorrencia):**

````
- **Organizar** (0.16.0, DEC-030, DEC-032): arrastar pela alça ⋮⋮ na Lista (com filtro, antes da próxima visível) e para os álbuns da lateral ou «+ Novo álbum»; o «⋯» de cada faixa (linha, detalhe e cartão) com Mover, Subir, Descer, Exportar e Excluir, e `Alt+↑`/`Alt+↓`; caixas e barra de lote; «Desfazer» e `Ctrl+Z` da última operação; soltar o `.json` sobre um álbum importa faixas nele. Só com cópia guardada no navegador. A SortableJS 1.15.7 vai embutida, com o hash no `validate.py`.
````

**Texto novo (substitui a ancora inteira):**

````
- **Organizar** (0.16.0, DEC-030, DEC-032): arrastar pela alça ⋮⋮ na Lista (com filtro, antes da próxima visível) e para os álbuns da lateral ou «+ Novo álbum»; o «⋯» de cada faixa (linha, detalhe e cartão) com Mover, Subir, Descer, Exportar e Excluir, e `Alt+↑`/`Alt+↓`; caixas e barra de lote; «Desfazer» e `Ctrl+Z` da última operação; soltar o `.json` sobre um álbum importa faixas nele. Só com cópia guardada no navegador. A SortableJS 1.15.7 vai embutida, com o hash no `validate.py`. Conferido na tela pelo dono em 2026-11-06.
````

### E06 — backlog: a I4 com protótipo e spec

**Ancora (linhas inteiras, 1 ocorrencia):**

````
1. **I4 — Salvar no arquivo** (i-043, DEC-030) — protótipo no canvas, depois spec: gravar o rascunho direto no `.json` de origem onde o navegador deixar, sem baixar e substituir à mão.
````

**Texto novo (substitui a ancora inteira):**

````
1. **I4 — Salvar no arquivo** (i-043, DEC-030) — protótipo e spec prontos (`meta/specs/261106-salvar-no-arquivo.md`); faltam a sonda e os cinco pontos do dono, depois a implementação pelo chat e a WO (0.17.0).
````

## Depois de aplicar — conferencia antes do commit

| # | Checagem | Comando | Esperado |
|---|---|---|---|
| 1 | Os tres arquivos sao os previstos | `sha1sum meta/STATUS.md logs/2026-11-06.md meta/specs/261106-salvar-no-arquivo.md` | a coluna **chegada**, os tres |
| 2 | A pendencia da I3 saiu | `grep -c '^- \*\*Conferir a I3 na tela' meta/STATUS.md` | `0` |
| 3 | A conferencia, a recusa e a sonda entraram | `grep -c 'Conferido na tela pelo dono em 2026-11-06' meta/STATUS.md`, `grep -c 'reemitida pelo chat como WO 0029' meta/STATUS.md` e `grep -c '^- \*\*Rodar a sonda da I4' meta/STATUS.md` | `1`, `1` e `1` (linhas) |
| 4 | O log tem a conversa do chat | `grep -c '^## Conversa 9 ' logs/2026-11-06.md` | `1` |
| 5 | Validacao | `python3 scripts/validate.py; echo "exit=$?"` | `exit=0`, com `OK  versao 0.16.0 igual em CHANGELOG, app, README e STATUS` |
| 6 | Nada alem do previsto | `GIT_OPTIONAL_LOCKS=0 git status --short --untracked-files=all` | os tres arquivos e esta WO |

As checagens 2 a 4 foram rodadas pelo chat na copia de chegada, no shell Linux dele; no Git Bash, **nao testado**. Se uma der diferente com a checagem 1 verde, relate o cru e nao pare: a 1 cobre os arquivos inteiros.
**Esta e qual pergunta?** «Esta la?». O «presta?» da I4 e a sonda e a decisao do dono, fora desta WO.

## Relatorio de aplicacao

Grave em `../AAMMDD-HHMM-code-cancioneiro-apply-wo0029.txt`, com o carimbo de `date +%y%m%d-%H%M` rodado na hora. Diga o resultado da checagem 1 em primeiro lugar. **Sem `/wrap` depois desta WO:** o log ja traz a conversa do chat. So acrescente a sua secao no log (Conversa 10, curta) se algo fugir do literal — e entao o sha1 de chegada do log muda, o que vai dito no relatorio.

## Commit

```
git add meta/STATUS.md logs/2026-11-06.md meta/specs/261106-salvar-no-arquivo.md meta/workorders/261106-wo0029-i3-conferida-e-i4-spec.md
```

```
git commit -m "docs: I3 conferida, spec e prototipo da I4, status e log de 2026-11-06" -m "Reemite a WO 0028 (recusada por falta de Ancoras lidas em) e registra a I4: spec em rascunho, sonda para o dono, log com a conversa 9 do chat."
```

```
git push
```
