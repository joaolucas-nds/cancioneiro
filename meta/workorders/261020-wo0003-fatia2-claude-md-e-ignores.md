# WO 0003 — Versionar a fatia 2 do kit v1.127.0: CLAUDE.md e os dois arquivos de exclusao

## Cabecalho

> **Tipo:** WO de DOC (registro). Nenhum codigo muda.
> **Config sugerida:** Sonnet · `/effort low`. O julgamento ja foi feito no chat; aqui e conferir e commitar.
> **Pre-requisito:** commit `047eab5`, branch `main`, sincronizada com `origin/main`, arvore limpa fora do que esta listado abaixo.
> **Base:** WO 0002 (fatia 1) e o relatorio `../261020-0718-code-fatia1-kit-apply-wo0002.txt`.
> **Depende de:** WO 0002, ja aplicada.
>
> **Arquivos que o chat gravou no disco e esta WO versiona** (sha1sum medido pelo chat ao gravar, 2026-10-20):
> - `CLAUDE.md` — `c81bd6949d144b043326e57fa00c5ff3cb200485`
> - `.gitignore` — `05331a787eed422dc41c8b85693d6ea93be1a9ae`
> - `.flatdropignore` — `ea1dc35978c3a784ebd885df5708c904b08a69fc`
>
> **Ancora semantica:** se um trecho-ancora nao bater EXATAMENTE, PARE e reporte.
> **Idempotencia:** antes de cada insercao, procure a frase-chave do texto NOVO; se ja existir, PULE e diga no relatorio.
>
> **Ancoras lidas em:** trechos lidos pelo chat no turno de 2026-10-20, direto do disco:
> - `meta/DECISIONS.md`, ultima linha do arquivo: `**Consequencias:** (+) `Write` e `additionalDirectories` consertados: criar log e gravar relatorio na pasta-pai param de pedir aprovacao a cada arquivo. (+) O carimbo de versao passa a dizer v1.127.0 nas skills e no modelo de WO. (−) O `meta/CEREBRO.md` continua carimbado v1.74.0 ate a fatia de fusao — divergencia conhecida e temporaria. (−) `CLAUDE.md` e `meta/CEREBRO.md` ainda citam `meta/specs/` e `/apply-spec`; corrigir e da fatia 2.`
> - `meta/STATUS.md`, linha 6: `**Versão atual:** 0.4.1 · **Fase:** 2 concluída · Fase 3 (qualidade de prompt) a iniciar`
> - `meta/STATUS.md`, linha 10: `## Última sessão (2026-07-21, auditoria)`

---

## 1. Por que

A fatia 1 trocou as skills e deixou tres referencias orfas: o `CLAUDE.md` ainda mandava aplicar spec de `meta/specs/`, pasta que esta vazia e cuja skill foi removida. O `.flatdropignore` usava a forma podada (`pasta/`) e nao reincluia o modelo de WO — ou seja, o `_TEMPLATE.md` que a fatia 1 versionou nao subia ao Projeto. E o `.gitignore` nao cobria `.claude/settings.local.json`, que estava untracked desde agosto.

**Correcao de um desvio do relatorio anterior.** O relatorio da WO 0002, secao (3), afirma que `settings.local.json` estava IGNORADO (`!!`) e coberto pelo `.gitignore`. Reconferido pelo chat neste turno, com comando:

```
git check-ignore -v .claude/settings.local.json   -> exit 1, sem saida (NAO ignorado)
git status --short --ignored .claude              -> ?? .claude/settings.local.json
```

Ele estava **untracked**, nao ignorado. O `.gitignore` desta WO e o que de fato o cobre. Isto vira linha de correcao no log do dia.

## 2. O que mudou em cada arquivo

**`CLAUDE.md`** — fusao, nao substituicao. Preservado: «O que e», «Regra de dominio inviolavel», o bloco real de «Build / validacao» (`scripts/validate.py`, o `pip install`), nomes em ingles / comentarios em PT-BR, `schema/` → DEC, e a tabela de config mapeada a este projeto. Adotado do kit v1.127.0: «sessao» → «turno» no cabecalho; spec/`meta/specs/` → WO/`meta/workorders/`; a regra pratica de corte («se remover a linha e o Claude ainda acerta, ela nao pertence aqui»); e tres secoes novas — «Quando eu pedir medicao», «Push e relatorio — nesta ordem, sempre» e «Relatorio em arquivo». Acrescentada a remissao a DEC-010 na linha da divisao de escrita, e a nota de que `grep -c` conta linhas. 48 linhas, bem abaixo do teto de 200.

**`.gitignore`** — mantido inteiro (o vivo e mais completo que o template do kit: exports, backups, toolchain). Acrescentado um bloco so: `.claude/settings.local.json`.

**`.flatdropignore`** — reescrito na forma do kit. `logs/` → `logs/*`; `meta/specs/` sai (pasta morta); entra o PAR `meta/workorders/*` + `!meta/workorders/_TEMPLATE.md`; as regras passam a viver dentro do bloco do editor do FlatDrop, e a explicacao fica acima dele. Acrescentada uma nota deste projeto dizendo que o arquivo so vale no canal de reserva, ja que o canal principal hoje e a pasta vinculada.

## Edicao 0 — Conferencia de hash (antes de tudo)

```
sha1sum CLAUDE.md .gitignore .flatdropignore
```

Confira contra a lista do cabecalho. Hash diferente = outro escritor mexeu depois do chat: **PARE e reporte**, nao commite por cima.

## Edicao 1 — `meta/DECISIONS.md` · uma DEC nova

**Ancora:** a ULTIMA linha do arquivo, citada no cabecalho. Insira DEPOIS dela, precedido de uma linha em branco e de `---`.

**Texto a inserir, literal:**

```
---

## DEC-012 — `.flatdropignore` na forma "pasta/*", e o canal achatado vira reserva

**Data:** 2026-10-20
**Contexto:** O `.flatdropignore` usava `logs/` e `meta/specs/` — a forma que PODA o diretorio antes de descer. Nessa forma um `!` dentro da pasta nunca chega a ser avaliado, entao o modelo de WO versionado na fatia 1 nao subia ao Projeto. A pasta `meta/specs/` tambem ficou morta quando a skill `apply-spec` saiu.

**Decisao:** Regra de exclusao usa `pasta/*` (o conteudo), nunca `pasta/` (a pasta), e modelo de pasta ignorada exige o PAR completo — a linha do conteudo seguida da linha `!pasta/_TEMPLATE.md`. As regras moram dentro do bloco do editor do FlatDrop; explicacao fica acima dele, nunca dentro. Fica registrado que o canal principal deste projeto e a pasta vinculada (o chat le e grava no disco) e que o `.flatdropignore` so vale no canal de reserva.

**Consequencias:** (+) `meta/workorders/_TEMPLATE.md` volta a subir ao Projeto; o corpo das WOs aplicadas, nao. (+) `.claude/settings.local.json` passa a ser ignorado pelo git, em vez de ficar untracked indefinidamente. (−) `meta/specs/` continua no disco com um `.gitkeep` orfao — remover e de uma fatia seguinte, junto com as citacoes a ela no `meta/CEREBRO.md` e no `meta/CONTEXT.md`.
```

## Edicao 2 — `meta/STATUS.md` · atualizar o agora (pendencia herdada da WO 0002)

A Edicao 3 da WO 0002 nao foi aplicada: ela foi atribuida ao `/wrap`, que nao rodou, e o relatorio registra `STATUS.md intocado`. **Esta WO assume essa pendencia.** Faca pelo `/wrap`, em append.

**Ancora:** a linha 10, `## Última sessão (2026-07-21, auditoria)`. O bloco dela **tem de continuar no arquivo** depois da sua edicao — procure o titulo antes e depois.

Conteudo para o bloco novo da conversa de 2026-10-20:

- Kit: fatias 1 e 2 do v1.127.0 aplicadas. Skills `apply-wo`, `wrap`, `sondar` instaladas e `apply-spec` removida; `.claude/settings.json` com `Write` e `additionalDirectories`; `CLAUDE.md`, `.gitignore` e `.flatdropignore` atualizados.
- Pendente do kit: `meta/CEREBRO.md` + `INSTRUCOES-DO-PROJETO.md` (fatia 3, fusao — os dois ainda carimbados/escritos no v1.74.0); os demais `meta/` (fatia 4); a pasta morta `meta/specs/`.
- Pendente de varredura: cadencia «sessao→turno» — **52 ocorrencias medidas em 18 arquivos** (`grep -rnoiE` em `meta/ CLAUDE.md INSTRUCOES-DO-PROJETO.md README.md .claude/ .gitignore .flatdropignore logs/`), das quais **3 corrigidas nesta fatia** (as do `CLAUDE.md` e do `.flatdropignore`) e ~22 ja justificadas como relato/dominio. Declarada **PENDENTE**, nao encerrada.
- Pendente de produto: a pergunta de 2026-10-17 sobre o `album-referencias.json` (pasta-pai) continua aberta.

Nao mexa na linha 6 (`**Versão atual:** 0.4.1 ...`): esta fatia nao muda a versao do produto.

## Fora de escopo

- `meta/CEREBRO.md` e `INSTRUCOES-DO-PROJETO.md` — fatia 3. **Nao toque**, mesmo nas citacoes a `meta/specs/` que ainda existem la (CEREBRO linhas 250, 252, 270) e no `meta/CONTEXT.md` linha 50.
- Apagar a pasta `meta/specs/`.
- `meta/CHANGELOG.md` — esta fatia nao entrega versao de produto.
- A varredura geral de «sessao→turno» fora dos tres arquivos desta fatia.
- O `album-referencias.json` e a pergunta de 17/10.

## Armadilhas desta WO

- **O `.flatdropignore` tem um bloco delimitado que o editor do FlatDrop reescreve inteiro.** Nao mova as linhas marcadoras, nao escreva nada depois da que fecha o bloco, e nao reproduza os marcadores em comentario — o editor os procura por substring e um exemplo vira um segundo bloco.
- **O relatorio anterior errou sobre o `settings.local.json`** (ver secao 1). Se voce reconferir e discordar da minha reconferencia, **remida e diga o comando** — nao conclua sem medir.
- **Fim de linha:** `git ls-files --eol` diz `i/lf w/lf` para os tres arquivos, e `git config --show-origin --get core.autocrlf` nao retornou nada do shell do chat. O relatorio anterior viu avisos LF→CRLF em 7 arquivos, o que sugere `autocrlf` ligado do SEU lado. **Nao reconferi isso daqui** — se os avisos voltarem, registre, nao conserte nesta WO.

## Depois de aplicar — conferencia antes do commit

| # | Checagem | Comando | Esperado |
|---|---|---|---|
| 1 | `CLAUDE.md` nao cita mais spec nem `meta/specs/` | `grep -c "meta/specs\|apply-spec" CLAUDE.md` | `0` |
| 2 | `CLAUDE.md` nao usa mais «sessao» | `grep -ciE "sess(ão\|ao)" CLAUDE.md` | `0` |
| 3 | `CLAUDE.md` cabe no teto | `wc -l CLAUDE.md` | `48` (teto: 200) |
| 4 | As tres secoes novas entraram | `grep -c "^## Quando eu pedir medição" CLAUDE.md`, idem `"^## Push e relatório"` e `"^## Relatório em arquivo"` | `1` cada |
| 5 | O conteudo proprio do projeto sobreviveu | `grep -c "^## Regra de domínio inviolável" CLAUDE.md` e `grep -c "scripts/validate.py" CLAUDE.md` | `1` e `1` |
| 6 | `settings.local.json` agora e ignorado | `git check-ignore -v .claude/settings.local.json` | aponta `.gitignore`, linha 12 |
| 7 | O par do modelo de WO esta completo e na ordem | `grep -n "^!\?meta/workorders" .flatdropignore` | exatamente duas linhas, 37 e 38: `meta/workorders/*` e, logo depois, `!meta/workorders/_TEMPLATE.md`. **Ancorado em `^` de proposito:** sem a ancora o grep tambem casa os dois comentarios explicativos (linhas 27-28) e devolve 4. |
| 8 | Nenhuma regra ficou na forma podada | `grep -cE "^(logs\|meta/[a-z]+)/$" .flatdropignore` | `0` |
| 9 | Nada depois do fecho do bloco do editor | ultima linha nao vazia do `.flatdropignore` e a que fecha o bloco | verdadeiro |
| 10 | O `.gitignore` nao perdeu nada do que ja tinha | `grep -c "export/" .gitignore` e `grep -c "backups/" .gitignore` | `1` e `1` |
| 11 | A DEC entrou uma vez so, e as anteriores ficaram | `grep -c "^## DEC-012" meta/DECISIONS.md` e `grep -c "^## DEC-01[01]" meta/DECISIONS.md` | `1` e `2` |
| 12 | O bloco antigo do STATUS sobreviveu ao append | `grep -c "^## Última sessão (2026-07-21, auditoria)" meta/STATUS.md` | `1` |
| 13 | Nenhum relatorio `.txt` ficou dentro do repo | `GIT_OPTIONAL_LOCKS=0 git status --short \| grep -c '\.txt'` | `0` |

**Os tres campos de cada passo:** todos sao rodados por **quem aplica (o Code)**, na raiz do repo (`C:\Users\alexk\Tools\cancioneiro\cancioneiro`), em Git Bash. **O que nenhum deles responde:** se o FlatDrop de fato passa a subir o `_TEMPLATE.md` — isso so a proxima geracao de copia achatada mostra, e o canal principal hoje nem a usa.

## Relatorio de aplicacao

Grave em `../261020-HHMM-code-fatia2-kit-apply-wo0003.txt`, com o `HHMM` de `date +%y%m%d-%H%M` rodado na hora. Inclua a linha de correcao sobre o `settings.local.json` tambem no log do dia.

**Proximo comando** (ultima linha do relatorio, cru e sozinho):

```
/sondar meta/CEREBRO.md INSTRUCOES-DO-PROJETO.md meta/CONTEXT.md
```

## Commit

```
git add CLAUDE.md .gitignore .flatdropignore meta/DECISIONS.md meta/STATUS.md meta/workorders logs
```

```
git commit -m "docs: aplica fatia 2 do kit v1.127.0" -m "CLAUDE.md funde o guia novo com o conteudo deste projeto: spec/meta/specs vira WO/meta/workorders, sessao vira turno, entram as secoes de medicao, push-antes-do-relatorio e relatorio em arquivo. .gitignore passa a cobrir .claude/settings.local.json. .flatdropignore adota a forma pasta/* com o par que reinclui o modelo de WO. Registra DEC-012."
```

```
git push
```
