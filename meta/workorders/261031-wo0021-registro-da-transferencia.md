# WO 0021 — Registro da conferência do dono e da transferência da conversa

## Cabecalho

> **Tipo:** WO de REGISTRO (so `meta/` e `logs/`; nenhum codigo).
> **Config sugerida:** Sonnet · `/effort low`. 7 edicoes literais, testadas pelo chat numa copia; cada arquivo tem hash de chegada.
> **Pre-requisito:** commit `85105ef`, branch `main`, sincronizada com `origin/main`, **arvore limpa** (so esta WO aparece como `??`).
> **Base:** relato do dono no chat de 2026-10-31 («Álbuns conferidos no app; as duas Rise of the Eternal ficam») e o fecho da conversa.
> **Depende de:** WO 0020, ja aplicada (`322f6c4`, wrap `85105ef`).
>
> **Arquivos — partida e chegada, os dois medidos pelo chat** (partida = `git show 85105ef:<arquivo>`; chegada = resultado de aplicar literalmente as edicoes abaixo, em LF):
>
> | arquivo | partida (sha1) | chegada (sha1) |
> |---|---|---|
> | `meta/STATUS.md` | `e9711a05d6140ddac33ddd84b6429fe5f359f914` | `0d10525908ea29746e2b421c6593bede77c8a9f4` |
> | `meta/IDEAS.md` | `b4ee9da4a911a769146c0c8b0bd64446c7a75857` | `46b11df4e4079c766e66d1d5b871fa7bff0001fd` |
> | `meta/analises/261029-ANALISE-conversao-dos-albuns.md` | `3c750aa0a6244744731b45c48f02dbce37717ac9` | `23a49415aee153df51ccbc2f87054962b2c8488b` |
> | `meta/analises/261029-ANALISE-kit-de-musica.md` | `8f9298a3de8bd4e8036da1ec9e10dcd83e8a6d25` | `ebf41fe0c49f8c9eb2119c7d5b72a83fd422282d` |
> | `logs/2026-10-31.md` | `d77851f61fdca4cf85f44946c070ffd33ea44ca2` | `20f01ee8aedb3cd5ec31540dd16b11fc40d794ca` |
>
> **Ancora semantica:** se um trecho-ancora nao bater EXATAMENTE, PARE e reporte.
> **Idempotencia:** antes de cada edicao, procure o texto NOVO INTEIRO; se ja estiver la, PULE e diga no relatorio.
>
> **Ancoras lidas em:** cada ancora foi extraida pelo chat do arquivo de partida (`git show 85105ef:<arquivo>`) e conferida como ocorrendo **exatamente 1 vez** no estado em que a edicao e aplicada, na ordem abaixo.

---

## 1. Por que

O dono conferiu os 12 albuns no app e decidiu manter as duas «Rise of the Eternal» `[relatado pelo dono]` —
fato que so existia no chat. A conversa foi transferida (brief `../261031-HANDOFF-BRIEF.md`, fora do repo), e
a sonda dos albuns foi arquivada em `../notas-arquivadas/` (as analises passam a citar o caminho novo).
O STATUS perde as duas pendencias resolvidas; o log ganha a Conversa 3.

## Edicao 0 — Conferencia de hash e de arvore

```
sha1sum meta/STATUS.md meta/IDEAS.md meta/analises/261029-ANALISE-conversao-dos-albuns.md meta/analises/261029-ANALISE-kit-de-musica.md logs/2026-10-31.md
GIT_OPTIONAL_LOCKS=0 git status --short
```

Os cinco batem com a coluna **partida**, e o `git status` mostra **so** esta WO. Qualquer outra coisa: **PARE e reporte**.

## Edicoes E01 a E07

Na ordem. Todas com o titulo `### Exx — ...`. Copie o que esta ENTRE as linhas de quatro crases, sem elas. **O
bloco termina na linha de quatro crases, nunca num titulo:** o bloco do log traz `## ` e `### `.

### E01 — STATUS (1) — `meta/STATUS.md`

**Ancora, literal:**

````
- **Kit de música** (i-039, DEC-027): `kit-musica/` com o bloco para Instruções e CEREBRO, `macetes-suno` e `revisar-faixa`; o `validate.py` prende os limites da skill aos do app. Carta 01 ao KCM na pasta-pai.
- **Este bloco substitui o anterior, de 2026-10-29, sobre a família BR.** O que ele dizia está no CHANGELOG [0.9.1], na DEC-026 e em `logs/2026-10-29.md` (Conversas 7 e 8). O item da aplicação da WO 0019, que o `/wrap` anexou no fim do arquivo, saiu: está no log (Conversa 8).
````

**Texto novo, literal:**

````
- **Kit de música** (i-039, DEC-027): `kit-musica/` com o bloco para Instruções e CEREBRO, `macetes-suno` e `revisar-faixa`; o `validate.py` prende os limites da skill aos do app. Carta 01 ao KCM na pasta-pai.
- **Conferido pelo dono no app (2026-10-31):** os 12 álbuns estão certos e as duas «Rise of the Eternal» ficam `[relatado pelo dono]`. A carta 01 segue com o dono para levar ao KCM.
- **Conversa transferida (2026-10-31):** a próxima conversa arranca pelo `../261031-HANDOFF-BRIEF.md` (fora do repo) e pelo ritual; a frente sugerida é a análise da i-040 e i-041.
- **Este bloco substitui o anterior, de 2026-10-29, sobre a família BR.** O que ele dizia está no CHANGELOG [0.9.1], na DEC-026 e em `logs/2026-10-29.md` (Conversas 7 e 8). O item da aplicação da WO 0019, que o `/wrap` anexou no fim do arquivo, saiu: está no log (Conversa 8).
````

### E02 — STATUS (2) — `meta/STATUS.md`

**Ancora, literal:**

````
## Pendências do dono

- **Conferir os 12 álbuns no app** — arrastar `../acervos/albuns-reagrupados.json`; dizer se algum grupo, título ou idioma está errado (o idioma das faixas é deduzido do cabeçalho e da escrita da letra).
- **«Rise of the Eternal»:** as duas canções ficaram (ÉPICO, tenor; guia_suno, soprano). Se quiser só uma, é uma linha no mapa de grupos.
- **Levar a carta 01 ao KCM** — `../261031-cancioneiro-para-kcm-01-kit-de-musica-ia.md`, para a pasta-pai do KCM.
- **Instalar o validador de esquema nesta máquina.** Sem `jsonschema` e `referencing`, o `validate.py` só confere sintaxe e diz `ESQUEMA NAO CONFERIDO` na última linha. Uma vez, no CMD: `pip install jsonschema referencing --break-system-packages`. Depois, `python3 scripts/validate.py` deve terminar em `Tudo conforme ao esquema.`
````

**Texto novo, literal:**

````
## Pendências do dono

- **Levar a carta 01 ao KCM** — `../261031-cancioneiro-para-kcm-01-kit-de-musica-ia.md`, para a pasta-pai do KCM.
- **Instalar o validador de esquema nesta máquina.** Sem `jsonschema` e `referencing`, o `validate.py` só confere sintaxe e diz `ESQUEMA NAO CONFERIDO` na última linha. Uma vez, no CMD: `pip install jsonschema referencing --break-system-packages`. Depois, `python3 scripts/validate.py` deve terminar em `Tudo conforme ao esquema.`
````

### E03 — IDEAS: i-038 (1) — `meta/IDEAS.md`

**Ancora, literal:**

````
`[relatado pelo dono, 2026-10-29]` Os oito guias de `Albuns/` misturam gêneros, idiomas e propósitos num arquivo só. O dono quer as faixas em álbuns mais relacionados, para depois ampliar cada um num projeto próprio. Proposta do chat em `../261029-PROPOSTA-grupos-albuns.md` (fora do repo: traz os títulos): 172 faixas em 12 álbuns (épico vocal, trilhas de jogo, romântico multilíngue, Brasil popular, pop asiático, latino, contagem e ritmo, matemática e física, código, foco e estudo, eletrônico instrumental, treino e ação). Um mapa faixa → álbum aplica a escolha por script. Espera a aprovação do dono; depois, conversores dos formatos de `Albuns/` (i-008).
**Entregue em 0.10.0 (2026-10-31):** grupos aprovados; 205 faixas (não 172 — a contagem da proposta perdeu 33 do VOL5) em 12 álbuns, `../acervos/albuns-reagrupados.json`, mapa em `../acervos/albuns-grupos.json`.
````

**Texto novo, literal:**

````
`[relatado pelo dono, 2026-10-29]` Os oito guias de `Albuns/` misturam gêneros, idiomas e propósitos num arquivo só. O dono quer as faixas em álbuns mais relacionados, para depois ampliar cada um num projeto próprio. Proposta do chat em `../261029-PROPOSTA-grupos-albuns.md` (fora do repo: traz os títulos): 172 faixas em 12 álbuns (épico vocal, trilhas de jogo, romântico multilíngue, Brasil popular, pop asiático, latino, contagem e ritmo, matemática e física, código, foco e estudo, eletrônico instrumental, treino e ação). Um mapa faixa → álbum aplica a escolha por script. Espera a aprovação do dono; depois, conversores dos formatos de `Albuns/` (i-008).
**Conferido no app pelo dono em 2026-10-31:** grupos, títulos e idiomas certos; as duas «Rise of the Eternal» (ÉPICO e guia_suno) ficam `[relatado pelo dono]`.
**Entregue em 0.10.0 (2026-10-31):** grupos aprovados; 205 faixas (não 172 — a contagem da proposta perdeu 33 do VOL5) em 12 álbuns, `../acervos/albuns-reagrupados.json`, mapa em `../acervos/albuns-grupos.json`.
````

### E04 — analise da conversao (1) — `meta/analises/261029-ANALISE-conversao-dos-albuns.md`

**Ancora, literal:**

````

**Sonda** (`../261029-sonda-albuns.py`, relatório `../261029-SONDA-albuns-antigos.md`, fora do repo; 19 arquivos,
44.083 linhas, 1.038 blocos de código; 0 alarmes na segunda execução, depois de corrigidos dois defeitos do
````

**Texto novo, literal:**

````

**Sonda** (`../notas-arquivadas/261029-sonda-albuns.py`, relatório `../notas-arquivadas/261029-SONDA-albuns-antigos.md`, fora do repo, arquivados em 2026-10-31; 19 arquivos,
44.083 linhas, 1.038 blocos de código; 0 alarmes na segunda execução, depois de corrigidos dois defeitos do
````

### E05 — analise da conversao (2) — `meta/analises/261029-ANALISE-conversao-dos-albuns.md`

**Ancora, literal:**

````
  e o mapa descarta uma em uma linha (`drop`) se ele quiser. As «Variações para» desse título ficam na do guia_suno.
````

**Texto novo, literal:**

````
  e o mapa descarta uma em uma linha (`drop`) se ele quiser. As «Variações para» desse título ficam na do guia_suno.
  **Decidido pelo dono em 2026-10-31: as duas ficam** `[relatado pelo dono]`.
````

### E06 — analise do kit: caminho da sonda (1) — `meta/analises/261029-ANALISE-kit-de-musica.md`

**Ancora, literal:**

````
- **todos os oito formatos** de `Albuns/` e os dez volumes BR põem o rótulo dentro do bloco copiável ou fora de
  qualquer padrão (sonda `../261029-SONDA-albuns-antigos.md`).

````

**Texto novo, literal:**

````
- **todos os oito formatos** de `Albuns/` e os dez volumes BR põem o rótulo dentro do bloco copiável ou fora de
  qualquer padrão (sonda `../notas-arquivadas/261029-SONDA-albuns-antigos.md`).

````

### E07 — log: Conversa 3 no fim (1) — `logs/2026-10-31.md`

**Ancora, literal:**

````
WO 0020 entregue e empurrada. O dono confere os 12 álbuns no app e leva a carta 01 ao KCM.
````

**Texto novo, literal:**

````
WO 0020 entregue e empurrada. O dono confere os 12 álbuns no app e leva a carta 01 ao KCM.

## Conversa 3 — chat: conferência do dono e transferência da conversa (WO 0021)

### Objetivo do dia
Registrar o que o dono conferiu e preparar a conversa nova.

### Feito
- Relatórios da WO 0020 (`322f6c4`) e do `/wrap` (`85105ef`) conferidos contra o `git log`: batem.
- O dono conferiu os 12 álbuns no app e manteve as duas «Rise of the Eternal» `[relatado pelo dono]`.
- `../261031-HANDOFF-BRIEF.md` escrito na pasta-pai (fora do repo).
- Arquivados em `../notas-arquivadas/`: os dois relatórios da WO 0020 e a sonda dos álbuns (`261029-SONDA-albuns-antigos.md`, `261029-sonda-albuns.py`); as análises passam a citar o caminho novo.
- WO 0021, só de registro: STATUS (sai a pendência de conferir os álbuns e a da Rise; entra a conferência e a transferência), IDEAS (i-038), análises (caminho da sonda, decisão da Rise), este log.

### Decisões
Nenhuma DEC nova. Do dono: as duas «Rise of the Eternal» ficam.

### Bugs
Nenhum.

### Aprendizados / armadilhas
- O `/wrap` anexa o seu item no fim do STATUS (depois de «Notas de estado»), não no bloco da última conversa; aconteceu nas WOs 0019 e 0020. Inócuo, mas quem reescreve o STATUS deve recolher esse item.

### Onde parei
Conversa transferida. A próxima arranca pelo brief e pelo ritual.

### Próximos passos
Análise da curadoria no app e de mais de um acervo (i-040, i-041).
````

## Fora de escopo

- Codigo, `data/`, `kit-musica/`: nada muda.
- O brief e a carta 01: fora do repo.

## Armadilhas desta WO

- **E05 (log) acrescenta no FIM** de `logs/2026-10-31.md`, depois da Conversa 2 que o `/wrap` escreveu. Se o seu
  `/wrap` desta WO acrescentar uma Conversa 4, ela vem depois desta.
- **Fim de linha:** os arquivos sao LF; `autocrlf=true` so converte no `add`. O hash vale no disco antes do `add`.
- **Nenhuma checagem abaixo usa emoji nem conta caracteres.**

## Depois de aplicar — conferencia antes do commit

| # | Checagem | Comando | Esperado |
|---|---|---|---|
| 1 | **Os cinco arquivos sao os testados** | `sha1sum meta/STATUS.md meta/IDEAS.md meta/analises/261029-ANALISE-conversao-dos-albuns.md meta/analises/261029-ANALISE-kit-de-musica.md logs/2026-10-31.md` | a coluna **chegada**, os cinco. **Prova as 7 edicoes.** |
| 2 | Os registros | `grep -c '^## Conversa 3' logs/2026-10-31.md`, `grep -c 'Conferir os 12' meta/STATUS.md`, `grep -c 'notas-arquivadas/261029-SONDA' meta/analises/261029-ANALISE-conversao-dos-albuns.md meta/analises/261029-ANALISE-kit-de-musica.md` | `1`, `0`, `1` em cada |
| 3 | Validacao passa | `python3 scripts/validate.py; echo "exit=$?"` | `exit=0`, com `OK  versao 0.10.0 igual em CHANGELOG, app, README e STATUS` |
| 4 | Nada fora de `meta/` e `logs/` | `GIT_OPTIONAL_LOCKS=0 git status --short \| grep -vcE ' (meta\|logs)/'` | `0` |

**Os tres campos de cada passo:** as quatro sao rodadas por **quem aplica (o Code)**, na raiz do repo, em Git
Bash, com `LC_ALL=C.UTF-8`. **Chega no ramo?** A checagem 1 cobre os cinco arquivos inteiros. **Esta e qual
pergunta?** As quatro respondem «esta la?».

## Relatorio de aplicacao

Grave em `../261031-HHMM-code-cancioneiro-apply-wo0021.txt`, com o `HHMM` de `date +%y%m%d-%H%M` rodado na
hora. Diga o resultado da checagem 1 em primeiro lugar, e confirme o push com a saida do `git status -sb`.

**Proximo comando** (ultima linha do relatorio, cru e sozinho):

```
/wrap
```

## Commit

```
git add meta/STATUS.md meta/IDEAS.md meta/analises logs/2026-10-31.md meta/workorders
```

```
git commit -m "docs: registra a conferencia do dono e a transferencia da conversa" -m "O dono conferiu os 12 albuns no app e manteve as duas Rise of the Eternal (relatado pelo dono). STATUS sem as duas pendencias resolvidas, IDEAS i-038 e analise com a decisao, caminho da sonda arquivada nas analises, log com a Conversa 3."
```

```
git push
```
