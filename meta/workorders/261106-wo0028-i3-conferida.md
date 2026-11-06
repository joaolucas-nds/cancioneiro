# WO 0028 — I3 conferida na tela: STATUS

## Cabecalho

> **Tipo:** registro — so `meta/STATUS.md` (4 edicoes literais) e o versionamento do log que o chat ja gravou.
> **Config sugerida:** Sonnet · `/effort low`.
> **Pre-requisito:** commit `8b8d8c0`, branch `main`, sincronizada com `origin/main`. O `git status` mostra **so** `M logs/2026-11-06.md` (Conversa 7, gravada pelo chat) e esta WO (`?? meta/workorders/...wo0028...`).
> **Base:** o dono relatou no chat, em 2026-11-06 15:37, «wo0027 aplicada, roteiro ok» — os 11 itens do roteiro de tela da I3 `[relatado pelo dono]`.
> **Depende de:** WO 0027 (`6a07bfd`, wrap `8b8d8c0`).
>
> | arquivo | partida (sha1) | chegada (sha1) |
> |---|---|---|
> | `meta/STATUS.md` | `1c5e9b42dfd83d595c8af93ab585eb8b2f296967` | `0803dda3bce5cd4aa8640d0f9b31e20d640560a5` |
> | `logs/2026-11-06.md` | `73996d880fe85c68fb7159c4dfb3fcdf171a5a0f` | `73996d880fe85c68fb7159c4dfb3fcdf171a5a0f` (gravado pelo chat; so versionar) |
>
> **Ancora semantica:** se um trecho-ancora nao bater EXATAMENTE, PARE e reporte.
> **Idempotencia:** antes de cada edicao, procure o texto NOVO INTEIRO; se ja estiver la, PULE e diga no relatorio.
> **Ancoras:** linhas inteiras, recortadas de `git show 8b8d8c0:meta/STATUS.md`, cada uma ocorrendo exatamente 1 vez no estado em que a edicao e aplicada, na ordem abaixo. A E03 e uma remocao: a ancora leva o titulo da secao e a linha seguinte, e o texto novo so as vizinhas.
> **Canal dos meta neste ciclo = CODE:** o STATUS e do Code (DEC-010); o log ja esta gravado pelo chat.

---

## 1. Por que

A I3 (0.16.0) foi conferida na tela pelo dono. A pendencia «Conferir a I3 na tela» sai do STATUS (rolante), e a
conferencia entra no cabecalho, na ultima conversa e na linha «Organizar». Nada de codigo; a versao continua 0.16.0.

## Edicao 0 — Conferencia de hash e de arvore

```
sha1sum meta/STATUS.md logs/2026-11-06.md
GIT_OPTIONAL_LOCKS=0 git status --short
```

Os dois batem com a coluna **partida**; o `git status` mostra exatamente as duas linhas do Pre-requisito. Qualquer outra coisa: **PARE e reporte**.

## Edicoes E01 a E04 (todas em `meta/STATUS.md`)

Na ordem. Copie o que esta ENTRE as linhas de quatro crases, sem elas.

### E01 — cabeçalho: a I3 conferida

**Ancora (linhas inteiras, 1 ocorrencia):**

````
**Versão atual:** 0.16.0 · **Fase:** 3a, 3a.2, o BPM da 3b, o prompt-modelo e as conveniências de uso concluídos e conferidos · os álbuns antigos convertidos (i-008, fora do repo) · curadoria no app concluída nas três entregas (DEC-028, DEC-029) · frente de interface na I3 de quatro (DEC-030 a DEC-032) · kit de música lido pelo KCM, à espera da resposta (i-039)
````

**Texto novo (substitui a ancora inteira):**

````
**Versão atual:** 0.16.0 · **Fase:** 3a, 3a.2, o BPM da 3b, o prompt-modelo e as conveniências de uso concluídos e conferidos · os álbuns antigos convertidos (i-008, fora do repo) · curadoria no app concluída nas três entregas (DEC-028, DEC-029) · frente de interface com a I3 conferida, a I4 é a próxima (DEC-030 a DEC-032) · kit de música lido pelo KCM, à espera da resposta (i-039)
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

### E03 — pendências do dono: sai «Conferir a I3 na tela»

**Ancora (linhas inteiras, 1 ocorrencia):**

````
## Pendências do dono

- **Conferir a I3 na tela** — roteiro na conversa de 2026-11-06 (WO 0027), depois do push, no computador e no celular.
- **Instalar o validador de esquema nesta máquina.** Sem `jsonschema` e `referencing`, o `validate.py` só confere sintaxe e diz `ESQUEMA NAO CONFERIDO` na última linha. Uma vez, no CMD: `pip install jsonschema referencing --break-system-packages`. Depois, `python3 scripts/validate.py` deve terminar em `Tudo conforme ao esquema.`
````

**Texto novo (substitui a ancora inteira):**

````
## Pendências do dono

- **Instalar o validador de esquema nesta máquina.** Sem `jsonschema` e `referencing`, o `validate.py` só confere sintaxe e diz `ESQUEMA NAO CONFERIDO` na última linha. Uma vez, no CMD: `pip install jsonschema referencing --break-system-packages`. Depois, `python3 scripts/validate.py` deve terminar em `Tudo conforme ao esquema.`
````

### E04 — Funciona: «Organizar» conferido

**Ancora (linhas inteiras, 1 ocorrencia):**

````
- **Organizar** (0.16.0, DEC-030, DEC-032): arrastar pela alça ⋮⋮ na Lista (com filtro, antes da próxima visível) e para os álbuns da lateral ou «+ Novo álbum»; o «⋯» de cada faixa (linha, detalhe e cartão) com Mover, Subir, Descer, Exportar e Excluir, e `Alt+↑`/`Alt+↓`; caixas e barra de lote; «Desfazer» e `Ctrl+Z` da última operação; soltar o `.json` sobre um álbum importa faixas nele. Só com cópia guardada no navegador. A SortableJS 1.15.7 vai embutida, com o hash no `validate.py`.
````

**Texto novo (substitui a ancora inteira):**

````
- **Organizar** (0.16.0, DEC-030, DEC-032): arrastar pela alça ⋮⋮ na Lista (com filtro, antes da próxima visível) e para os álbuns da lateral ou «+ Novo álbum»; o «⋯» de cada faixa (linha, detalhe e cartão) com Mover, Subir, Descer, Exportar e Excluir, e `Alt+↑`/`Alt+↓`; caixas e barra de lote; «Desfazer» e `Ctrl+Z` da última operação; soltar o `.json` sobre um álbum importa faixas nele. Só com cópia guardada no navegador. A SortableJS 1.15.7 vai embutida, com o hash no `validate.py`. Conferido na tela pelo dono em 2026-11-06.
````

## Depois de aplicar — conferencia antes do commit

| # | Checagem | Comando | Esperado |
|---|---|---|---|
| 1 | Os dois arquivos sao os previstos | `sha1sum meta/STATUS.md logs/2026-11-06.md` | a coluna **chegada**, os dois |
| 2 | A pendencia saiu | `grep -c 'Conferir a I3 na tela' meta/STATUS.md` | `0` |
| 3 | A conferencia entrou | `grep -c 'Conferido na tela pelo dono em 2026-11-06' meta/STATUS.md` e `grep -c '^## Conversa 7 ' logs/2026-11-06.md` | `1` e `1` |
| 4 | Validacao | `python3 scripts/validate.py; echo "exit=$?"` | `exit=0`, com `OK  versao 0.16.0 igual em CHANGELOG, app, README e STATUS` |
| 5 | Nada alem do previsto | `GIT_OPTIONAL_LOCKS=0 git status --short --untracked-files=all` | os dois arquivos e esta WO |

**Chega no ramo?** Nao ha codigo: a checagem 1 cobre os dois arquivos inteiros. **Esta e qual pergunta?** «Esta la?»; o «presta?» da I3 o dono ja respondeu na tela.

## Relatorio de aplicacao

Grave em `../261106-HHMM-code-cancioneiro-apply-wo0028.txt`, com o `HHMM` de `date +%y%m%d-%H%M` rodado na hora. Diga o resultado da checagem 1 em primeiro lugar. **Sem `/wrap` depois desta WO:** ela ja e o fecho do dia, e o log ja traz a conversa do chat. So acrescente a sua secao no log (Conversa 8, curta) se algo fugir do literal — e entao inclua o log no mesmo commit.

## Commit

```
git add meta/STATUS.md logs/2026-11-06.md meta/workorders
```

```
git commit -m "docs: I3 conferida na tela, status e log de 2026-11-06" -m "O dono conferiu a I3 (0.16.0) pelo roteiro de tela. Sai a pendencia do STATUS; log com a conversa 7 do chat (transferencia para conversa nova)."
```

```
git push
```
