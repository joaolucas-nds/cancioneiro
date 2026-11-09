# WO 0032 — i-051: testes do navegador no GitHub Actions

## Cabecalho

> **Tipo:** mista — codigo novo (`tests/`, 7 arquivos, e `.github/workflows/testes.yml`) e registro (`.gitignore`, `CLAUDE.md`, README, DECISIONS, IDEAS e STATUS, 15 edicoes), mais o versionamento de dois arquivos que o chat gravou. O app nao muda; a versao continua 0.17.0.
> **Config sugerida:** Sonnet · `/effort medium`.
> **Pre-requisito:** commit `dfbb6f5`, branch `main`, sincronizada com `origin/main`. O `git status --short` mostra exatamente: ` M logs/2026-11-09.md`, `?? meta/analises/261109-ANALISE-kit-de-musica-v2.md` e `?? meta/workorders/261109-wo0032-testes-no-ci.md`.
> **Base:** decisao do dono em 2026-11-09, «i-051 com os testes no GitHub Actions» `[relatado pelo dono]` → DEC-034, inserida aqui. Testado pelo chat num clone de `dfbb6f5`: 32 de 32 testes, `validate.py` com esquema e os dois conversores OK.
> **Depende de:** WO 0031 (`dfbb6f5`).
>
> **Arquivos editados:**
>
> | arquivo | partida (sha1) | chegada (sha1) |
> |---|---|---|
> | `.gitignore` | `05331a787eed422dc41c8b85693d6ea93be1a9ae` | `0d11dd77d35df9d87f57dc4b569b604b287a7124` |
> | `CLAUDE.md` | `c81bd6949d144b043326e57fa00c5ff3cb200485` | `6c599f7b703452d513e6a7cbe112ae13b37ead21` |
> | `README.md` | `acea877d8ae4979bfa8ee9d18af177d17649b25c` | `4d485becd58c8f73a14db7e418d4b54168983025` |
> | `meta/DECISIONS.md` | `47a83de61af150faadcc095f1ef580a7dc0d92e5` | `129e9bab07c1979f395b971fe2b188923a34b113` |
> | `meta/IDEAS.md` | `b47de1dc4eeb9ce351defc19ba187aeecec9742e` | `f2f4e23341b2e698ecbed8a9cb138f03a496f69f` |
> | `meta/STATUS.md` | `33ec44ced1152b99ad41959012ce746821fd1f67` | `5b758145a4da743fa28a883467ec0b8138e32c18` |
>
> **Arquivos novos** (nao existem antes; a chegada e o sha1 do arquivo criado):
>
> | arquivo | chegada (sha1) |
> |---|---|
> | `.github/workflows/testes.yml` | `362c6c03fe4e74a477e7e6daf18f362b25f37fe9` |
> | `tests/requirements.txt` | `7b4b9f80131736ed0ccdc5eb73cf14327a50d011` |
> | `tests/conftest.py` | `5a64449bfeb90775e83771163fe0e20acdef9b0a` |
> | `tests/test_basico.py` | `775a165625988052a2aeeec723657ea65af93953` |
> | `tests/test_organizar.py` | `c9b711c7cfa884d68f58dfb61faad383b911d398` |
> | `tests/test_salvar.py` | `87ad005ac76dd24f665791a2bbafdcf9188540bc` |
> | `tests/test_roundtrip.py` | `326f35b28ec6e58535ea9caeba516f415c36d25b` |
> | `tests/test_celular.py` | `3be3665a5829d99cd71c33a3741ec1da82ee2361` |
>
> **Arquivos que o chat gravou no disco e esta WO so versiona** (partida = chegada):
>
> | arquivo | sha1 |
> |---|---|
> | `meta/analises/261109-ANALISE-kit-de-musica-v2.md` | `37c9a21b1981526d27728f78c31cf4cfcbddfbc2` |
> | `logs/2026-11-09.md` | `cb3e66d0eb5a51c5194c443cbb225f12824919d8` |
>
> **Ancora semantica:** se um trecho-ancora nao bater EXATAMENTE, PARE e reporte.
> **Idempotencia:** antes de cada edicao, procure o texto NOVO INTEIRO; se ja estiver la, PULE e diga no relatorio. Arquivo novo que ja existe com o sha1 de chegada: PULE; com outro sha1: PARE.
> **Ancoras:** linhas inteiras (ou blocos de linhas inteiras), cada uma 1 vez no arquivo no estado em que a edicao e aplicada, na ordem abaixo. Toda edicao «substitui a ancora inteira»; nas que acrescentam, o texto novo repete a ancora.
> **Âncoras lidas em** (todas lidas pelo chat NESTE turno, dos arquivos em `dfbb6f5` — sha1 de partida igual no disco do dono, conferido; o chat aplicou as edicoes e criou os arquivos num clone e mediu a chegada):
> - E01 (`.gitignore`, cache do Python e do pytest): linha `*.bak`
> - E02 (`CLAUDE.md`, os testes do navegador): linha `- Mudança só de doc (meta/) NÃO precisa de validação; a rede é o git diff.`
> - E03 (`README.md`, testes no README): linha `Checa todos os data/*.json contra o esquema e confere que a SortableJS embutida no app é…`
> - E04 (`meta/DECISIONS.md`, DEC-034): linha `**Consequências:** (+) Salvar custa um clique ou Ctrl+S, sem Downloads nem substituir à …`
> - E05 (`meta/IDEAS.md`, i-016 entregue (título)): linha `### i-016 💡 Rodar validate.py em pre-commit / CI`
> - E06 (`meta/IDEAS.md`, i-025 entregue (título)): linha `### i-025 💡 Teste de round-trip automatizado (baixar → reimportar)`
> - E07 (`meta/IDEAS.md`, i-051 entregue (título)): linha `### i-051 💡 Versionar os testes do navegador`
> - E08 (`meta/IDEAS.md`, i-016 entregue (linha)): linha `Já que scripts/validate.py existe e retorna código 1 em erro, plugá-lo num hook de pre-c…`
> - E09 (`meta/IDEAS.md`, i-025 entregue (linha)): linha `[nascido do FIX-004, 2026-10-22] O ciclo baixar→reimportar quebrou por meses sem ninguem…`
> - E10 (`meta/IDEAS.md`, i-051 entregue (linha)): linha `[capturada pelo chat, 2026-11-06, na I4] Os testes no Chromium headless de cada entrega …`
> - E11 (`meta/STATUS.md`, última conversa): linha `## Última conversa (2026-11-06, I4: sonda, pontos e implementação, WO 0030)`
> - E12 (`meta/STATUS.md`, funciona: testes no CI): linha `- **Validação** (scripts/validate.py): sintaxe, esquema (com jsonschema), integridade …`
> - E13 (`meta/STATUS.md`, pendências: o primeiro ✓ e o validador opcional): linha `- **Instalar o validador de esquema nesta máquina.** Sem jsonschema e referencing, o …`
> - E14 (`meta/STATUS.md`, backlog: o kit v2 no lugar da i-051): linha `2. **Versionar os testes do navegador** (i-051) — os testes de cada entrega ficaram fora d…`
> - E15 (`meta/STATUS.md`, em progresso: o kit v2): linha `- **Kit de música no KCM (i-039)** — o KCM leu a carta 01 e responde por carta, sem data. …`
> **Canal dos meta neste ciclo = CODE:** DECISIONS e STATUS sao do Code (DEC-010); IDEAS, README e `CLAUDE.md` mudam por esta WO; a analise e o log do chat ja estao gravados.

---

## 1. Por que

A i-051 (DEC-034): os testes do navegador de cada entrega passam a morar em `tests/` e a rodar no GitHub Actions a
cada push na `main`, junto do `validate.py` com esquema e dos testes dos conversores. Dados so sinteticos: nenhum
acervo nem letra do dono entra no repositorio. Fecha tambem a i-016 e a i-025.

## Armadilhas

- **Crie os arquivos novos por script ou pela ferramenta de escrita, nunca redigitando.** Eles tem aspas «», ✓, ⋯ e expressoes regulares; um caractere trocado muda o sha1.
- **Os blocos dos arquivos novos terminam com quebra de linha.** O conteudo e o que esta entre as linhas de quatro crases, mais uma quebra de linha no fim.
- **Nao rode `pytest` aqui:** a maquina do dono nao tem Playwright. O teste roda no GitHub depois do push. O `validate.py` local continua (sem esquema nesta maquina, como antes).
- **O push pode ser recusado** com «refusing to allow an OAuth App to create or update workflow … without `workflow` scope»: a credencial Git desta maquina nao tem permissao para `.github/workflows/`. Se acontecer, **nao force, nao tire o arquivo**: o commit fica local, relate a mensagem crua e feche com o menu (`AskUserQuestion`), com a recomendada «o dono renova a credencial do GitHub nesta maquina (Gerenciador de Credenciais do Windows → apagar `git:https://github.com` → o proximo push pede login no navegador)».
- **`tests/__pycache__/`** nao deve aparecer: a E01 o ignora.
- **CRLF:** o dono tem `autocrlf=true`; os sha1 sao do arquivo em LF. Arquivo novo criado com CRLF por engano muda o sha1: confira com `git ls-files --eol` depois do `add` e relate.

## Edicao 0 — Conferencia de hash e de arvore

```
sha1sum .gitignore CLAUDE.md README.md meta/DECISIONS.md meta/IDEAS.md meta/STATUS.md meta/analises/261109-ANALISE-kit-de-musica-v2.md logs/2026-11-09.md
GIT_OPTIONAL_LOCKS=0 git status --short
ls tests .github 2>&1
```

Os seis editados batem com **partida**, os dois do chat com o sha1 deles; o `git status` mostra exatamente as tres linhas do Pre-requisito; `tests` e `.github` nao existem. Qualquer outra coisa: **PARE e reporte**.

## Edicoes E01 a E15

Na ordem. Copie o que esta ENTRE as linhas de quatro crases, sem elas. Cada edicao diz o arquivo.

### E01 — cache do Python e do pytest

**Arquivo:** `.gitignore`

**Ancora:**

````
*.bak
backups/
````

**Texto novo (substitui a ancora inteira):**

````
*.bak
backups/

# Testes (i-051): cache do Python e do pytest, gerados ao rodar tests/
__pycache__/
.pytest_cache/
````

### E02 — os testes do navegador

**Arquivo:** `CLAUDE.md`

**Ancora:**

````
- Mudança só de doc (meta/) NÃO precisa de validação; a rede é o `git diff`.
````

**Texto novo (substitui a ancora inteira):**

````
- **Testes do navegador** (`tests/`, DEC-034): rodam no GitHub Actions a cada push (`.github/workflows/testes.yml`), com o `validate.py` e os testes dos conversores. Nesta máquina não há Playwright: depois do push, confira o resultado com `gh run list --limit 1` se o `gh` existir; senão, diga no relatório que o ✓ é para o dono ver na aba Actions. Push vermelho no CI: relate a saída, não «conserte» sem WO.
- Mudança só de doc (meta/) NÃO precisa de validação; a rede é o `git diff`.
````

### E03 — testes no README

**Arquivo:** `README.md`

**Ancora:**

````
Checa todos os `data/*.json` contra o esquema e confere que a SortableJS embutida no app é a 1.15.7 sem mudança (pelo sha256). Rode antes de commitar mudança em `data/`, `schema/` ou `app/`.
````

**Texto novo (substitui a ancora inteira):**

````
Checa todos os `data/*.json` contra o esquema e confere que a SortableJS embutida no app é a 1.15.7 sem mudança (pelo sha256). Rode antes de commitar mudança em `data/`, `schema/` ou `app/`.

## Testes

A cada push na `main`, o GitHub Actions roda o `validate.py` (com o esquema), os testes dos conversores e os testes do navegador em `tests/`: o app aberto no Chromium sem tela, com dados só sintéticos (o `data/demo.json` e acervos gerados pelo próprio teste). O resultado aparece como ✓ ou ✗ no commit e na aba **Actions** do repositório. Para rodar na sua máquina:

```
pip install -r tests/requirements.txt
python -m playwright install chromium
python -m pytest tests
```
````

### E04 — DEC-034

**Arquivo:** `meta/DECISIONS.md`

**Ancora:**

````
**Consequências:** (+) Salvar custa um clique ou `Ctrl+S`, sem Downloads nem substituir à mão. (+) Editar o `.json` fora do app com um rascunho aberto não se perde em silêncio. (−) Uma permissão do navegador por sessão; se o «Permitir em todas as visitas» vale no `file://` não foi medido (a sonda não passou pelo fechar e reabrir). (−) O teste automático não abre a janela real: as janelas são trocadas por arquivos da pasta privada do navegador, em `http://127.0.0.1`, e, no headless, ler do IndexedDB um handle guardado derruba a aba fora de um perfil persistente. (−) Dois caminhos de salvar para manter: gravar e baixar.
````

**Texto novo (substitui a ancora inteira):**

````
**Consequências:** (+) Salvar custa um clique ou `Ctrl+S`, sem Downloads nem substituir à mão. (+) Editar o `.json` fora do app com um rascunho aberto não se perde em silêncio. (−) Uma permissão do navegador por sessão; se o «Permitir em todas as visitas» vale no `file://` não foi medido (a sonda não passou pelo fechar e reabrir). (−) O teste automático não abre a janela real: as janelas são trocadas por arquivos da pasta privada do navegador, em `http://127.0.0.1`, e, no headless, ler do IndexedDB um handle guardado derruba a aba fora de um perfil persistente. (−) Dois caminhos de salvar para manter: gravar e baixar.

## DEC-034 — Testes do navegador versionados em `tests/` e rodados no GitHub Actions a cada push, só com dados sintéticos

**Data:** 2026-11-09
**Status:** aceita
**Contexto:** Os testes no Chromium headless de cada entrega moravam só na sessão do chat que os escreveu; a regressão da I4 teve de ser por fumaça (i-051). A máquina do dono não tem Playwright, e o `validate.py` lá não confere o esquema (falta `jsonschema`). Decidido pelo dono em 2026-11-09: os testes no GitHub Actions `[relatado pelo dono]`; ele perguntou se seriam versionados os acervos — não: só dados sintéticos.
**Decisão:**
- **`tests/`** com pytest e Playwright (Python): básico (ler, buscar, detalhe, copiar sem rótulo, «usei», Cartões, exportar), organizar (I3), salvar no arquivo (I4, com as janelas do sistema trocadas por arquivos da pasta privada do navegador), ida e volta do acervo (i-025) e celular. O app é servido por um `http.server` em `127.0.0.1`, num perfil persistente do Chromium.
- **Dados só sintéticos:** o `data/demo.json` e acervos gerados por `make_collection()`. Nenhum acervo nem letra do dono entra no repositório.
- **`.github/workflows/testes.yml`** roda a cada push e pull request na `main` (e à mão): o `validate.py` com `jsonschema`, os testes dos dois conversores e o `pytest tests`. Versões fixas em `tests/requirements.txt`.
- **Desempenho fica fora do CI:** o tempo de abertura varia com a máquina; segue medido pelo chat, contra a versão anterior, nas mesmas rodadas.
**Alternativas consideradas:** testes só no chat (ninguém roda quando se mexe à mão); hook de pre-commit na máquina do dono (pede Python, Playwright e o navegador instalados lá); Node e `@playwright/test` (o projeto já tem os scripts em Python).
**Consequências:** (+) Toda mudança roda contra tudo o que já funcionava, inclusive o arrastar da I3; o esquema passa a ser conferido a cada push (fecha na prática a pendência do `jsonschema` e a i-016). (+) A ida e volta do acervo vira teste (i-025). (−) O teste não abre a janela real do sistema nem o aviso de permissão: isso continua no roteiro de tela do dono. (−) Trocar a versão do Playwright, do Chromium ou da SortableJS pode quebrar o teste de arrastar; o CI acusa. (−) Empurrar um arquivo em `.github/workflows/` exige que a credencial do Git tenha o escopo `workflow`.
````

### E05 — i-016 entregue (título)

**Arquivo:** `meta/IDEAS.md`

**Ancora:**

````
### i-016 💡 Rodar validate.py em pre-commit / CI
````

**Texto novo (substitui a ancora inteira):**

````
### i-016 ✅ Rodar validate.py em pre-commit / CI
````

### E06 — i-025 entregue (título)

**Arquivo:** `meta/IDEAS.md`

**Ancora:**

````
### i-025 💡 Teste de round-trip automatizado (baixar → reimportar)
````

**Texto novo (substitui a ancora inteira):**

````
### i-025 ✅ Teste de round-trip automatizado (baixar → reimportar)
````

### E07 — i-051 entregue (título)

**Arquivo:** `meta/IDEAS.md`

**Ancora:**

````
### i-051 💡 Versionar os testes do navegador
````

**Texto novo (substitui a ancora inteira):**

````
### i-051 ✅ Versionar os testes do navegador
````

### E08 — i-016 entregue (linha)

**Arquivo:** `meta/IDEAS.md`

**Ancora:**

````
Já que `scripts/validate.py` existe e retorna código 1 em erro, plugá-lo num hook de pre-commit (ou GitHub Action) garante que nenhum dataset quebrado entre no repo. Baixo esforço, alta rede de segurança. Fase 2/3.
````

**Texto novo (substitui a ancora inteira):**

````
Já que `scripts/validate.py` existe e retorna código 1 em erro, plugá-lo num hook de pre-commit (ou GitHub Action) garante que nenhum dataset quebrado entre no repo. Baixo esforço, alta rede de segurança. Fase 2/3.
**Entregue (2026-11-09, DEC-034):** no GitHub Actions, a cada push e pull request na `main`, com `jsonschema`; junto dos testes do navegador (i-051). O pre-commit ficou de fora: pediria as dependências na máquina do dono.
````

### E09 — i-025 entregue (linha)

**Arquivo:** `meta/IDEAS.md`

**Ancora:**

````
`[nascido do FIX-004, 2026-10-22]` O ciclo baixar→reimportar quebrou por meses sem ninguem notar, e so apareceu porque alguem abriu o app num navegador de verdade. Uma checagem que carregue um acervo, serialize como o `downloadCollection` serializa e reimporte, afirmando igualdade, capturaria a classe inteira — nao so o `_activeModules`. Hoje o `validate.py` valida arquivos parados; isto e o primeiro teste de COMPORTAMENTO do projeto, e exige decidir se entra um harness de navegador (headless) ou se a serializacao e extraida para uma funcao testavel sem DOM. Candidata a analise antes de spec.
````

**Texto novo (substitui a ancora inteira):**

````
`[nascido do FIX-004, 2026-10-22]` O ciclo baixar→reimportar quebrou por meses sem ninguem notar, e so apareceu porque alguem abriu o app num navegador de verdade. Uma checagem que carregue um acervo, serialize como o `downloadCollection` serializa e reimporte, afirmando igualdade, capturaria a classe inteira — nao so o `_activeModules`. Hoje o `validate.py` valida arquivos parados; isto e o primeiro teste de COMPORTAMENTO do projeto, e exige decidir se entra um harness de navegador (headless) ou se a serializacao e extraida para uma funcao testavel sem DOM. Candidata a analise antes de spec.
**Entregue (2026-11-09, DEC-034):** `tests/test_roundtrip.py` baixa e reimporta um acervo sintético de 205 faixas, antes e depois de organizar, e compara com o original.
````

### E10 — i-051 entregue (linha)

**Arquivo:** `meta/IDEAS.md`

**Ancora:**

````
`[capturada pelo chat, 2026-11-06, na I4]` Os testes no Chromium headless de cada entrega (curadoria 1 a 3, I1 a I4) moram só na sessão do chat que os escreveu: a conversa seguinte não os tem, e a regressão da I4 teve de ser por fumaça (importar, lista, detalhe, «⋯», Cartões). Guardar em `tests/` (Playwright, Python) e rodar antes de cada WO de código. Pede decidir onde roda (a máquina do dono não tem Playwright) e o custo de manter.
````

**Texto novo (substitui a ancora inteira):**

````
`[capturada pelo chat, 2026-11-06, na I4]` Os testes no Chromium headless de cada entrega (curadoria 1 a 3, I1 a I4) moram só na sessão do chat que os escreveu: a conversa seguinte não os tem, e a regressão da I4 teve de ser por fumaça (importar, lista, detalhe, «⋯», Cartões). Guardar em `tests/` (Playwright, Python) e rodar antes de cada WO de código. Pede decidir onde roda (a máquina do dono não tem Playwright) e o custo de manter.
**Entregue (2026-11-09, DEC-034):** `tests/` com 32 testes (básico, organizar, salvar no arquivo, ida e volta, celular) e o workflow `.github/workflows/testes.yml`, que roda a cada push. Só dados sintéticos: o dono perguntou se seriam versionados os acervos — não `[relatado pelo dono, 2026-11-09]`.
````

### E11 — última conversa

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
## Última conversa (2026-11-06, I4: sonda, pontos e implementação, WO 0030)

- **WO 0029 aplicada e empurrada** (`24b1fc0`, wrap `a9efdef`): a I3 conferida, a recusa da WO 0028 e a I4 em spec ficaram registradas.
- **Sonda da I4 no Chrome 156 do dono** (`file://`): janela de salvar, gravar de novo sem janela, vínculo guardado no IndexedDB, janela de abrir e handle ao arrastar, todos OK `[medido por instrumento]`. Não mediu o fechar e reabrir nem o arquivo mudado fora: a página não foi reaberta e o arquivo de teste não foi editado.
- **I4, salvar no arquivo (0.17.0):** os cinco pontos decididos pelo dono como recomendados (DEC-033); 14 de 14 critérios no Chromium headless, testados pelo chat. **Conferida na tela pelo dono** em 2026-11-09 (os 10 itens do roteiro OK `[relatado pelo dono]`): salvar no arquivo está fechado.
- **Este bloco substitui o anterior, da WO 0029** (I3 conferida e a I4 em spec). O que ele dizia está no CHANGELOG [0.16.0], nas specs `meta/specs/261106-organizar.md` e `meta/specs/261106-salvar-no-arquivo.md` e em `logs/2026-11-06.md` (Conversas 4 a 10).

````

**Texto novo (substitui a ancora inteira):**

````
## Última conversa (2026-11-09, I4 conferida, i-051 e o kit de música v2)

- **I4 conferida na tela pelo dono** (os 10 itens do roteiro OK `[relatado pelo dono]`, WO 0031): salvar no arquivo (0.17.0) está fechado, e a frente de interface, com as quatro entregas.
- **i-051, testes do navegador no CI** (DEC-034, WO 0032): `tests/` com 32 testes, só com dados sintéticos, e o GitHub Actions a cada push, com o `validate.py` com esquema e os testes dos conversores. Fecha também a i-016 e a i-025. Falta ver o primeiro ✓ no GitHub.
- **Kit de música v2:** análise `meta/analises/261109-ANALISE-kit-de-musica-v2.md`, decidida pelo dono como recomendada; a leva 1 (o kit na 0.17.0, os recursos do Suno de 2026 e «Depois de ouvir») vem depois da i-051.
- **Este bloco substitui o anterior, da WO 0030** (I4). O que ele dizia está no CHANGELOG [0.17.0], na spec `meta/specs/261106-salvar-no-arquivo.md` e em `logs/2026-11-06.md` (Conversas 11 e 12).

````

### E12 — funciona: testes no CI

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
- **Validação** (`scripts/validate.py`): sintaxe, esquema (com `jsonschema`), integridade referencial dos módulos (id ausente ou objeto no lugar do id, sem traceback — FIX-009), versão igual nos quatro lugares, um BPM só por faixa (DEC-020) e as marcações do prompt que o app lê (DEC-021) e os limites da skill `revisar-faixa` contra o app (DEC-027); código 1 se falhar; a última linha diz se o esquema foi de fato conferido.
````

**Texto novo (substitui a ancora inteira):**

````
- **Validação** (`scripts/validate.py`): sintaxe, esquema (com `jsonschema`), integridade referencial dos módulos (id ausente ou objeto no lugar do id, sem traceback — FIX-009), versão igual nos quatro lugares, um BPM só por faixa (DEC-020) e as marcações do prompt que o app lê (DEC-021) e os limites da skill `revisar-faixa` contra o app (DEC-027); código 1 se falhar; a última linha diz se o esquema foi de fato conferido.
- **Testes do navegador no CI** (DEC-034): `tests/` (pytest e Playwright, 32 testes, dados só sintéticos) e `.github/workflows/testes.yml`, que roda o `validate.py` com esquema, os testes dos conversores e o `pytest tests` a cada push na `main`. O resultado é o ✓ ou ✗ no commit e a aba Actions.
````

### E13 — pendências: o primeiro ✓ e o validador opcional

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
- **Instalar o validador de esquema nesta máquina.** Sem `jsonschema` e `referencing`, o `validate.py` só confere sintaxe e diz `ESQUEMA NAO CONFERIDO` na última linha. Uma vez, no CMD: `pip install jsonschema referencing --break-system-packages`. Depois, `python3 scripts/validate.py` deve terminar em `Tudo conforme ao esquema.`
````

**Texto novo (substitui a ancora inteira):**

````
- **Ver o primeiro ✓ do CI** — em `https://github.com/joaolucas-nds/cancioneiro/actions`, depois do push da WO 0032: a execução «testes» do commit dela, verde.
- **Instalar o validador de esquema nesta máquina.** Sem `jsonschema` e `referencing`, o `validate.py` só confere sintaxe e diz `ESQUEMA NAO CONFERIDO` na última linha. Uma vez, no CMD: `pip install jsonschema referencing --break-system-packages`. Depois, `python3 scripts/validate.py` deve terminar em `Tudo conforme ao esquema.` Desde a DEC-034 o CI confere o esquema a cada push: instalar aqui passa a ser opcional.
````

### E14 — backlog: o kit v2 no lugar da i-051

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
2. **Versionar os testes do navegador** (i-051) — os testes de cada entrega ficaram fora do repositório; a regressão da I4 foi por fumaça.
````

**Texto novo (substitui a ancora inteira):**

````
2. **Kit de música v2, leva 1** (i-039, análise `meta/analises/261109-ANALISE-kit-de-musica-v2.md`) — o kit na 0.17.0, os recursos do Suno de 2026 e «Depois de ouvir» na `macetes-suno`; uma WO só de documento.
````

### E15 — em progresso: o kit v2

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
- **Kit de música no KCM (i-039)** — o KCM leu a carta 01 e responde por carta, sem data. Gatilho: sem resposta até o primeiro projeto de música novo, o projeto usa o kit à mão (`kit-musica/README.md`).
````

**Texto novo (substitui a ancora inteira):**

````
- **Kit de música no KCM (i-039)** — o KCM leu a carta 01 e responde por carta, sem data. Gatilho: sem resposta até o primeiro projeto de música novo, o projeto usa o kit à mão (`kit-musica/README.md`). Kit v2 decidido pelo dono em 2026-11-09 (análise `meta/analises/261109-ANALISE-kit-de-musica-v2.md`): leva 1 depois da i-051, leva 2 com prova de campo, carta 02 no fim.
````

## Arquivos novos N01 a N08

Crie cada um com o conteudo entre as linhas de quatro crases, mais a quebra de linha final.

### N01 — `.github/workflows/testes.yml`

````
# Testes do Cancioneiro (i-051, DEC-034): a cada push e pull request na main,
# o validate.py com o esquema, os testes dos conversores e os testes do
# navegador (tests/, Chromium sem tela). Dados so sinteticos: nenhum acervo
# do dono entra no repositorio. Resultado: o ✓ ou ✗ no commit, e a aba Actions.
name: testes

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read

jobs:
  testes:
    runs-on: ubuntu-24.04
    timeout-minutes: 15
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.13"
          cache: pip
          cache-dependency-path: tests/requirements.txt
      - name: Dependencias
        run: |
          python -m pip install -r tests/requirements.txt
          python -m playwright install --with-deps chromium
      - name: Validar acervos, versao e biblioteca
        run: python scripts/validate.py
      - name: Conversores
        run: |
          python scripts/test_convert_br.py
          python scripts/test_convert_guides.py
      - name: Navegador
        run: python -m pytest tests -q
````

### N02 — `tests/requirements.txt`

````
# Dependencias dos testes (i-051). O CI instala estas; o validate.py usa as duas ultimas.
playwright==1.63.0
pytest==9.1.1
jsonschema==4.26.0
referencing==0.37.0
````

### N03 — `tests/conftest.py`

````
"""Infraestrutura dos testes do navegador (i-051, DEC-034).

O app e aberto no Chromium sem tela, servido por um http.server local em
127.0.0.1 (a pasta privada do navegador, que os testes da I4 usam no lugar das
janelas do sistema, e recusada no file://). Dados SO sinteticos: o
data/demo.json, que ja e publico, e acervos gerados por make_collection().
Nenhum acervo do dono entra aqui.

Rodar: python -m pytest tests  (precisa de: pip install -r tests/requirements.txt
e python -m playwright install chromium).
"""
import copy
import functools
import http.server
import json
import os
import re
import socketserver
import tempfile
import threading

import pytest
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEMO_PATH = os.path.join(ROOT, "data", "demo.json")
with open(DEMO_PATH, encoding="utf-8") as fh:
    DEMO_TEXT = fh.read()
DEMO = json.loads(DEMO_TEXT)


def changelog_version():
    """A versao do topo do CHANGELOG, a mesma fonte do validate.py."""
    with open(os.path.join(ROOT, "meta", "CHANGELOG.md"), encoding="utf-8") as fh:
        return re.search(r"^## \[(\d+\.\d+\.\d+)\]", fh.read(), re.M).group(1)


def make_collection(n_tracks, n_albums=12):
    """Acervo sintetico com n_tracks faixas, copiadas das tres do demo."""
    songs = [s for a in DEMO["albums"] for s in a["songs"]]
    coll = copy.deepcopy(DEMO)
    coll["albums"] = []
    per = -(-n_tracks // n_albums)
    for k in range(n_albums):
        album = {"id": f"al-{k:02d}", "title": f"Álbum {k + 1}", "songs": []}
        for _ in range(per):
            i = sum(len(a["songs"]) for a in coll["albums"]) + len(album["songs"])
            if i >= n_tracks:
                break
            s = copy.deepcopy(songs[i % len(songs)])
            s["id"], s["title"] = f"f-{i:03d}", f"Faixa {i + 1}"
            album["songs"].append(s)
        if album["songs"]:
            coll["albums"].append(album)
    return coll


class _Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


@pytest.fixture(scope="session")
def base_url():
    """Serve a raiz do repositorio numa porta livre, durante a sessao de testes."""
    handler = functools.partial(_Quiet, directory=ROOT)
    httpd = socketserver.ThreadingTCPServer(("127.0.0.1", 0), handler)
    httpd.daemon_threads = True
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    yield f"http://127.0.0.1:{httpd.server_address[1]}"
    httpd.shutdown()


@pytest.fixture(scope="session")
def pw():
    with sync_playwright() as p:
        yield p


# As janelas do sistema da I4 sao trocadas por arquivos da pasta privada do
# navegador (OPFS); a permissao de gravar, por __fs.perm / __fs.req.
FS_STUB = """
window.__fs = { cancel: false, openName: 'demo-acervo.json', saveName: null, perm: null, req: 'granted', calls: [] };
const P = FileSystemHandle.prototype;
P.queryPermission = async function () { __fs.calls.push('query'); return __fs.perm || 'granted'; };
P.requestPermission = async function () { __fs.calls.push('request'); return __fs.req; };
window.showSaveFilePicker = async o => { __fs.calls.push('save:' + (o && o.suggestedName));
  if (__fs.cancel) throw new DOMException('aborted', 'AbortError');
  const d = await navigator.storage.getDirectory(); return d.getFileHandle(__fs.saveName || o.suggestedName, { create: true }); };
window.showOpenFilePicker = async () => { __fs.calls.push('open');
  if (__fs.cancel) throw new DOMException('aborted', 'AbortError');
  const d = await navigator.storage.getDirectory(); return [await d.getFileHandle(__fs.openName)]; };
window.__keys = []; window.addEventListener('keydown', e => window.__keys.push(e), true);
"""
NO_FS_API = "delete window.showSaveFilePicker; delete window.showOpenFilePicker;"


@pytest.fixture
def open_app(pw, base_url):
    """Abre o app num perfil novo e persistente (no contexto anonimo, ler do
    IndexedDB um handle guardado derruba a aba: medido na I4). Devolve a pagina;
    page.errors guarda os erros de pagina, conferidos no fim de cada teste."""
    opened = []

    def _open(width=1366, height=800, mobile=False, init="", fs_api=True):
        kw = dict(viewport={"width": width, "height": height}, accept_downloads=True)
        if mobile:
            kw.update(is_mobile=True, has_touch=True)
        ctx = pw.chromium.launch_persistent_context(tempfile.mkdtemp(prefix="canc-"), **kw)
        ctx.grant_permissions(["clipboard-read", "clipboard-write"], origin=base_url)
        page = ctx.new_page()
        page.errors = []
        page.on("pageerror", lambda e: page.errors.append(str(e)))
        page.add_init_script(FS_STUB + ("" if fs_api else NO_FS_API) + init)
        page.goto(base_url + "/app/index.html")
        page.evaluate("bootDone")
        opened.append(page)
        return page

    yield _open
    for page in opened:
        errs = list(page.errors)
        page.context.close()
        assert not errs, f"erro de pagina: {errs}"


def import_demo(page, path=DEMO_PATH):
    """Importa um acervo pelo <input type=file> (o caminho de sempre)."""
    page.set_input_files("#file-input", path)
    page.wait_for_function("App.saved && App.collection")


def write_tmp_collection(coll):
    fd, path = tempfile.mkstemp(suffix=".json", prefix="acervo-")
    with os.fdopen(fd, "w", encoding="utf-8") as fh:
        json.dump(coll, fh, ensure_ascii=False, indent=2)
    return path


def rows(page):
    return page.eval_on_selector_all("#main li.row", "e => e.map(x => x.dataset.id)")


def album_ids(page, k=0):
    return page.evaluate(f"App.collection.albums[{k}].songs.map(s => s.id)")


def changes(page):
    return page.evaluate("App.changes")
````

### N04 — `tests/test_basico.py`

````
"""Ler, buscar, filtrar, copiar e exportar (fase 2, I1 e I2). Dados: data/demo.json."""
import json
import re

from conftest import DEMO, DEMO_TEXT, changelog_version, import_demo, rows

TITLES = [s["title"] for a in DEMO["albums"] for s in a["songs"]]
IDS = [s["id"] for a in DEMO["albums"] for s in a["songs"]]


def test_versao_na_tela_e_igual_ao_changelog(open_app):
    page = open_app()
    assert page.text_content('[data-role="app-version"]') == "v" + changelog_version()


def test_importar_mostra_lista_e_lateral(open_app):
    page = open_app()
    import_demo(page)
    assert rows(page) == IDS
    side = page.eval_on_selector_all("#side-albums .side-item:not(.side-new)", "e => e.length")
    assert side == len(DEMO["albums"]) + 1  # «Todas as faixas» e os álbuns


def test_busca_filtra_e_limpa(open_app):
    page = open_app()
    import_demo(page)
    alvo = TITLES[1]
    page.fill("#search", alvo)
    page.wait_for_timeout(300)
    assert rows(page) == [IDS[1]]
    page.fill("#search", "")
    page.wait_for_timeout(300)
    assert rows(page) == IDS


def test_detalhe_abre_com_endereco_e_navega(open_app):
    page = open_app()
    import_demo(page)
    page.click(f'#main li.row[data-id="{IDS[0]}"] .row-open')
    assert page.is_visible("#detail")
    assert page.evaluate("location.hash") == "#faixa=" + IDS[0]
    page.click("#detail-next")
    assert page.evaluate("App.detailId") == IDS[1]


def test_copiar_style_da_linha_sem_rotulo(open_app):
    page = open_app()
    import_demo(page)
    song = DEMO["albums"][0]["songs"][0]
    page.click(f'#main li.row[data-id="{song["id"]}"] [data-role="row-style"]')
    page.wait_for_timeout(200)
    got = page.evaluate("navigator.clipboard.readText()")
    assert got.startswith(song["style"].split(",")[0])
    assert not re.search(r"estilo suno|style:|\[letra\]", got, re.I)


def test_usei_sobrevive_a_recarregar(open_app):
    page = open_app()
    import_demo(page)
    page.click(f'#main li.row[data-id="{IDS[0]}"] .row-used')
    page.reload()
    page.evaluate("bootDone")
    assert page.get_attribute(f'#main li.row[data-id="{IDS[0]}"] .row-used', "aria-pressed") == "true"


def test_cartoes_mostram_todas_as_faixas(open_app):
    page = open_app()
    import_demo(page)
    page.click("#view-cards")
    assert page.eval_on_selector_all("#main .card", "e => e.length") == len(IDS)


def test_exportar_md_da_faixa_deixa_rotulo_fora_do_bloco(open_app):
    page = open_app()
    import_demo(page)
    song = DEMO["albums"][0]["songs"][0]
    page.click(f'#main li.row[data-id="{song["id"]}"] .row-more')
    with page.expect_download() as d:
        page.click("#tm-md")
    md = open(d.value.path(), encoding="utf-8").read()
    blocks = re.findall(r"```[^\n]*\n(.*?)```", md, re.S)
    assert any(song["style"].split(",")[0] in b for b in blocks)
    for b in blocks:
        assert not re.search(r"estilo suno|^style:|^lyrics:", b, re.I | re.M), b


def test_baixar_json_sem_chaves_internas(open_app):
    page = open_app()
    import_demo(page)
    page.click("#more-btn")
    with page.expect_download() as d:
        page.click("#download-btn")
    out = json.load(open(d.value.path(), encoding="utf-8"))
    assert out == json.loads(DEMO_TEXT)
````

### N05 — `tests/test_organizar.py`

````
"""Organizar (I3, DEC-032): «⋯», arrastar, lote, excluir, mover e «Desfazer»."""
from conftest import DEMO, album_ids, changes, import_demo, rows

A0 = [s["id"] for s in DEMO["albums"][0]["songs"]]


def menu(page, song_id):
    page.click(f'#main li.row[data-id="{song_id}"] .row-more')


def test_descer_pelo_menu_e_desfazer(open_app):
    page = open_app()
    import_demo(page)
    menu(page, A0[0])
    page.click("#tm-down")
    assert album_ids(page)[:2] == [A0[1], A0[0]] and changes(page) == 1
    page.click("#toast button")  # «Desfazer»
    assert album_ids(page) == A0 and changes(page) == 0


def test_arrastar_pela_alca_muda_a_ordem(open_app):
    page = open_app()
    import_demo(page)
    src = page.locator(f'#main li.row[data-id="{A0[0]}"] .row-grip')
    dst = page.locator(f'#main li.row[data-id="{A0[1]}"]')
    src.evaluate("e => e.scrollIntoView({block: 'center'})")
    a, b = src.bounding_box(), dst.bounding_box()
    page.mouse.move(a["x"] + a["width"] / 2, a["y"] + a["height"] / 2)
    page.mouse.down()
    for k in range(1, 11):
        page.mouse.move(a["x"] + a["width"] / 2, b["y"] + b["height"] * (0.2 + 0.07 * k))
        page.wait_for_timeout(30)
    page.mouse.up()
    page.wait_for_timeout(300)
    assert album_ids(page)[:2] == [A0[1], A0[0]] and changes(page) == 1


def test_soltar_no_mesmo_lugar_nao_conta(open_app):
    page = open_app()
    import_demo(page)
    src = page.locator(f'#main li.row[data-id="{A0[0]}"] .row-grip')
    a = src.bounding_box()
    page.mouse.move(a["x"] + 5, a["y"] + 5)
    page.mouse.down()
    page.mouse.move(a["x"] + 8, a["y"] + 9)
    page.mouse.move(a["x"] + 5, a["y"] + 5)
    page.mouse.up()
    page.wait_for_timeout(300)
    assert album_ids(page) == A0 and changes(page) == 0


def test_lote_seleciona_e_esc_limpa(open_app):
    page = open_app()
    import_demo(page)
    for i in A0[:2]:
        page.click(f'#main li.row[data-id="{i}"] .row-sel input')
    assert "2 faixas selecionadas" in page.text_content("#batch-count")
    page.keyboard.press("Escape")
    assert page.is_hidden("#batch")


def test_excluir_confirma_e_ctrl_z_volta(open_app):
    page = open_app()
    import_demo(page)
    menu(page, A0[0])
    page.click("#tm-delete")
    page.click("#confirm-ok-btn")
    assert A0[0] not in rows(page) and changes(page) == 1
    page.click("body", position={"x": 5, "y": 400})
    page.keyboard.press("Control+z")
    page.wait_for_timeout(200)
    assert A0[0] in rows(page) and changes(page) == 0


def test_ctrl_z_na_busca_nao_mexe_no_acervo(open_app):
    page = open_app()
    import_demo(page)
    menu(page, A0[0])
    page.click("#tm-down")
    page.fill("#search", "x")
    page.focus("#search")
    page.keyboard.press("Control+z")
    page.wait_for_timeout(200)
    assert changes(page) == 1


def test_mover_para_outro_album(open_app):
    page = open_app()
    import_demo(page)
    alvo = DEMO["albums"][1]
    menu(page, A0[0])
    page.click("#tm-move")
    page.select_option("#move-target", alvo["id"])
    page.click("#move-ok-btn")
    assert page.evaluate("App.collection.albums[1].songs.map(s => s.id)")[-1] == A0[0]


def test_sem_copia_guardada_nao_ha_alca(open_app):
    """O exemplo que o Pages carrega sozinho nao tem rascunho (C9 da I3)."""
    page = open_app()
    page.evaluate("d => { setCollection(d); App.saved = false; render(); }", DEMO)
    assert page.eval_on_selector_all("#main .row-grip", "e => e.length") == 0
````

### N06 — `tests/test_salvar.py`

````
"""Salvar no arquivo (I4, DEC-033; criterios da spec meta/specs/261106-salvar-no-arquivo.md).
As janelas do sistema sao arquivos da pasta privada do navegador (FS_STUB no conftest)."""
import json

from conftest import DEMO_TEXT, changes, import_demo


def opfs_write(page, name, text):
    page.evaluate("""async ([n, t]) => { const d = await navigator.storage.getDirectory();
      const h = await d.getFileHandle(n, { create: true }); const w = await h.createWritable();
      await w.write(t); await w.close(); }""", [name, text])


def opfs_read(page, name):
    return page.evaluate("""async n => { const d = await navigator.storage.getDirectory();
      try { return await (await (await d.getFileHandle(n)).getFile()).text(); } catch (e) { return null; } }""", name)


def record(page, src="demo-acervo.json"):
    return page.evaluate("""async s => { const r = await dbGet(s); return r ? { link: !!r.fileHandle,
      name: r.fileHandle && r.fileHandle.name } : null; }""", src)


def calls(page):
    return page.evaluate("__fs.calls.splice(0)")


def change(page):
    page.evaluate("moveSongBy(App.collection.albums[0].songs[0].id, 1)")
    page.wait_for_timeout(150)


def import_by_picker(page, text=DEMO_TEXT):
    opfs_write(page, "demo-acervo.json", text)
    page.click("#more-btn")
    page.click("#menu-import")
    page.wait_for_function("App.source === 'demo-acervo.json' && App.saved")


def save(page):
    page.click("#draft-save")
    page.wait_for_timeout(300)


def collection_text(page):
    return page.evaluate("JSON.stringify(App.collection, null, 2)") + "\n"


def test_c1_sem_api_baixa_como_antes(open_app):
    page = open_app(fs_api=False)
    import_demo(page)
    change(page)
    assert page.text_content("#draft-save") == "Salvar .json" and page.is_hidden("#save-wrap")
    with page.expect_download() as d:
        page.click("#draft-save")
    assert d.value.suggested_filename == "demo.json"
    page.wait_for_timeout(200)
    assert changes(page) == 0


def test_c1_c5_c3_importar_vincula_e_salvar_grava_sem_janela(open_app):
    page = open_app()
    import_by_picker(page)
    assert record(page) == {"link": True, "name": "demo-acervo.json"}
    change(page)
    assert page.text_content("#draft-save") == "Salvar" and page.is_visible("#save-wrap")
    calls(page)
    save(page)
    assert calls(page) == ["query"] and changes(page) == 0
    assert opfs_read(page, "demo-acervo.json") == collection_text(page)
    assert page.text_content("#draft-text").startswith("✓ Salvo no arquivo às")


def test_c2_sem_vinculo_pede_janela_e_cancelar_nao_grava(open_app):
    page = open_app()
    import_demo(page)  # pelo <input>: sem vinculo
    change(page)
    page.evaluate("__fs.cancel = true")
    calls(page)
    save(page)
    assert calls(page) == ["save:demo.json"] and changes(page) == 1 and record(page, "demo.json")["link"] is False
    page.evaluate("__fs.cancel = false")
    save(page)
    assert changes(page) == 0 and record(page, "demo.json")["link"] is True
    assert opfs_read(page, "demo.json") == collection_text(page)


def test_c4_reabrir_pede_permissao(open_app):
    page = open_app()
    import_by_picker(page)
    page.reload()
    page.evaluate("bootDone")
    assert page.evaluate("App.link && App.link.handle.name") == "demo-acervo.json"
    change(page)
    page.evaluate("__fs.perm = 'prompt'; __fs.req = 'denied'")
    calls(page)
    save(page)
    assert calls(page) == ["query", "request"] and changes(page) == 1
    page.evaluate("__fs.req = 'granted'")
    save(page)
    assert changes(page) == 0


def test_c6_arquivo_mudado_fora_pergunta(open_app):
    page = open_app()
    import_by_picker(page)
    change(page)
    save(page)
    change(page)
    save(page)  # falso positivo: duas gravacoes seguidas pelo app nao perguntam
    assert not page.evaluate("document.getElementById('choice-dialog').open") and changes(page) == 0
    change(page)
    page.wait_for_timeout(1100)
    opfs_write(page, "demo-acervo.json", DEMO_TEXT.replace('"title"', '"title" ', 1))
    page.click("#draft-save")
    page.wait_for_selector("#choice-dialog[open]")
    assert page.eval_on_selector_all("#choice-actions button", "e => e.map(x => x.dataset.value)") == ["cancel", "other", "replace"]
    page.click('#choice-actions [data-value="cancel"]')
    page.wait_for_timeout(200)
    assert changes(page) == 1
    page.click("#draft-save")
    page.wait_for_selector("#choice-dialog[open]")
    page.click('#choice-actions [data-value="replace"]')
    page.wait_for_timeout(300)
    assert changes(page) == 0 and opfs_read(page, "demo-acervo.json") == collection_text(page)


def test_c7_arquivo_sumiu(open_app):
    page = open_app()
    import_by_picker(page)
    change(page)
    page.evaluate("async () => (await navigator.storage.getDirectory()).removeEntry('demo-acervo.json')")
    page.click("#draft-save")
    page.wait_for_selector("#choice-dialog[open]")
    assert "não foi encontrado" in page.text_content("#choice-text")
    page.click('#choice-actions [data-value="cancel"]')
    assert changes(page) == 1


def test_c8_baixar_com_vinculo_nao_zera(open_app):
    page = open_app()
    import_by_picker(page)
    change(page)
    page.click("#draft-more")
    with page.expect_download():
        page.click("#save-download")
    page.wait_for_timeout(200)
    assert changes(page) == 1 and json.loads(opfs_read(page, "demo-acervo.json")) == json.loads(DEMO_TEXT)


def test_c9_ctrl_s_na_busca_salva(open_app):
    page = open_app()
    import_by_picker(page)
    change(page)
    page.focus("#search")
    page.evaluate("__keys = []")
    page.keyboard.press("Control+s")
    page.wait_for_timeout(400)
    assert changes(page) == 0 and page.evaluate("__keys.some(e => e.key === 's' && e.defaultPrevented)")


def test_c10_desfazer_depois_de_salvar(open_app):
    page = open_app()
    import_by_picker(page)
    change(page)
    save(page)
    page.click("body", position={"x": 5, "y": 400})
    page.keyboard.press("Control+z")
    page.wait_for_timeout(200)
    assert changes(page) == 1 and page.text_content("#draft-text") == "1 alteração não salva"


def test_c11_desvincular_e_esquecer(open_app):
    page = open_app()
    import_by_picker(page)
    page.click("#acervo-btn")
    assert "Vinculado a demo-acervo.json" in page.text_content("#link-note")
    page.click("#unlink-btn")
    page.wait_for_timeout(200)
    assert record(page)["link"] is False
    page.evaluate("forgetAcervo('demo-acervo.json')")
    page.wait_for_timeout(200)
    assert record(page) is None


def test_c12_celular_baixa(open_app):
    page = open_app(width=390, height=844, mobile=True)
    import_demo(page)
    change(page)
    assert page.text_content("#draft-save") == "Salvar .json" and page.is_hidden("#save-wrap")
    calls(page)
    with page.expect_download():
        page.click("#draft-save")
    assert calls(page) == []
````

### N07 — `tests/test_roundtrip.py`

````
"""Ida e volta do acervo (i-025): baixar e reimportar devolve o mesmo acervo,
antes e depois de organizar. Acervo sintetico de 205 faixas."""
import json

from conftest import import_demo, make_collection, rows, write_tmp_collection


def download_json(page):
    page.click("#more-btn")
    with page.expect_download() as d:
        page.click("#download-btn")
    return d.value.path()


def test_baixar_e_reimportar_e_identico(open_app):
    coll = make_collection(205)
    path = write_tmp_collection(coll)
    page = open_app()
    import_demo(page, path)
    assert len(rows(page)) == 205
    out = download_json(page)
    assert json.load(open(out, encoding="utf-8")) == coll


def test_organizado_volta_igual_ao_baixado(open_app):
    page = open_app()
    import_demo(page, write_tmp_collection(make_collection(30, 3)))
    page.evaluate("moveSongBy(App.collection.albums[0].songs[0].id, 2)")
    page.wait_for_timeout(150)
    out = download_json(page)
    first = json.load(open(out, encoding="utf-8"))
    page.evaluate("App.changes = 0")  # o baixar zerou; reimportar nao pede confirmacao
    page.set_input_files("#file-input", out)
    page.wait_for_timeout(500)
    assert page.evaluate("App.collection") == first
````

### N08 — `tests/test_celular.py`

````
"""Celular, 390x844 (I2 e I3): detalhe em tela propria, folha do «⋯», selecionar varias."""
from conftest import DEMO, import_demo

ID0 = DEMO["albums"][0]["songs"][0]["id"]


def test_detalhe_em_tela_propria_e_voltar(open_app):
    page = open_app(width=390, height=844, mobile=True)
    import_demo(page)
    page.click(f'#main li.row[data-id="{ID0}"] .row-open')
    assert page.is_visible("#detail-back")
    page.click("#detail-back")
    assert page.is_visible(f'#main li.row[data-id="{ID0}"]')


def test_selecionar_varias_pelo_menu_do_detalhe(open_app):
    page = open_app(width=390, height=844, mobile=True)
    import_demo(page)
    page.click(f'#main li.row[data-id="{ID0}"] .row-open')
    page.click("#detail-more")
    page.click("#tm-select")
    page.wait_for_timeout(200)
    assert page.evaluate("[...App.selection]") == [ID0]
    assert page.is_visible("#batch")
````

## Depois de aplicar — conferencia antes do commit

| # | Checagem | Comando | Esperado |
|---|---|---|---|
| 1 | Os seis editados e os oito novos sao os previstos | `sha1sum .gitignore CLAUDE.md README.md meta/DECISIONS.md meta/IDEAS.md meta/STATUS.md .github/workflows/testes.yml tests/requirements.txt tests/conftest.py tests/test_basico.py tests/test_organizar.py tests/test_salvar.py tests/test_roundtrip.py tests/test_celular.py` | as colunas **chegada**, os quatorze |
| 2 | Os dois do chat nao mudaram | `sha1sum meta/analises/261109-ANALISE-kit-de-musica-v2.md logs/2026-11-09.md` | os sha1 da terceira tabela |
| 3 | Validacao | `python3 scripts/validate.py; echo "exit=$?"` | `exit=0`, com `OK  versao 0.17.0 igual em CHANGELOG, app, README e STATUS` |
| 4 | Os registros | `grep -c '^## DEC-034 ' meta/DECISIONS.md` e `grep -c '^### i-051 ' meta/IDEAS.md` | `1` e `1` (linhas) |
| 5 | Nada alem do previsto | `GIT_OPTIONAL_LOCKS=0 git status --short --untracked-files=all` | os seis editados, os oito novos, os dois do chat e esta WO |
| 6 | Depois do push: o CI | `gh run list --limit 1` (se o `gh` existir) | a execucao «testes» do commit desta WO; relate o estado cru (`in_progress`, `completed success` ou `failure`). Sem `gh`, diga isso |

A checagem 4 foi rodada pelo chat no clone, no shell Linux; no Git Bash, **nao testado** — com a 1 verde, relate o cru e nao pare. A 6 e informativa: **CI vermelho nao desfaz o push**; relate a saida e o chat le o log pela API publica.
**Esta e qual pergunta?** A 1 responde «esta la?». O «presta?» e o proprio CI (32 testes); o chat ja os rodou no clone, 32 de 32.

## Relatorio de aplicacao

Grave em `../AAMMDD-HHMM-code-cancioneiro-apply-wo0032.txt`, com o carimbo de `date +%y%m%d-%H%M` rodado na hora. Diga o resultado da checagem 1 em primeiro lugar e o do push (aceito ou recusado, com a mensagem crua). **Sem `/wrap` depois desta WO**, e sem secao sua no log, salvo se algo fugir do literal.

## Commit

```
git add .gitignore CLAUDE.md README.md meta/DECISIONS.md meta/IDEAS.md meta/STATUS.md tests .github meta/analises/261109-ANALISE-kit-de-musica-v2.md logs/2026-11-09.md meta/workorders/261109-wo0032-testes-no-ci.md
```

```
git commit -m "test: testes do navegador no GitHub Actions" -m "i-051 (DEC-034): tests/ com 32 testes em Playwright e pytest, so com dados sinteticos, e o workflow que roda o validate.py com esquema, os conversores e os testes a cada push. Fecha i-016 e i-025. Analise do kit de musica v2 decidida."
```

```
git push
```
