# WO 0039 — Testes C5 do CI, as duas linhas do kit (carta 03 do KCM) e a 0.20.0 conferida

## Cabecalho

> **Tipo:** teste (o texto de 2 testes; o app nao muda), kit e meta. Sem versao nova: o app continua 0.20.0.
> **Config sugerida:** Sonnet · `/effort low` (aplicacao literal por script; 14 edicoes).
> **Pre-requisito:** commit `2372c10`, branch `main`, sincronizada com `origin/main`. O `git status --short` mostra exatamente: ` M logs/2026-11-14.md` e `?? meta/workorders/261114-wo0039-testes-c5-e-carta-03.md`.
> **Base:** relatorios `261114-1044` e `261114-1045` (CI vermelho em 2 testes); o dono conferiu a 0.20.0 na tela («roteiro das formulas na tela ok» `[relatado pelo dono, 2026-11-14 11:32]`); a carta 03 do KCM, respondida pela 04 (DEC-038); a ordem do backlog decidida pelo dono em 2026-11-14 `[relatado pelo dono]`.
> **Depende de:** `2372c10` (wrap da WO 0038).
>
> | arquivo | partida (sha1) | chegada (sha1) |
> |---|---|---|
> | `tests/test_formulas.py` | `83fcdb0d66ab0af63f25c99860850acadf9c5027` | `9bd3d48527ba404b311d565534f0b26cbc4887a4` |
> | `kit-musica/BLOCO-SUNO.md` | `26676916b5e39b659dcccda84c6deb754d8aaa9a` | `0b15f217d8f5b094d23cf88241a8e9c54235935e` |
> | `meta/STATUS.md` | `206f36049b060be0b9273e2efc0dacecde4b197f` | `40f98eb0d379b9e4aeaff45c2f900ab9d42b27c5` |
> | `meta/ROADMAP.md` | `4cd400f205f5305f1c108ca2bb7f911c88bddeef` | `a60dd592b561f524e00f5e4dc48b52648208f422` |
> | `meta/IDEAS.md` | `7e6e476c87b2a364a1445a46378497870806f72f` | `d0ab6dfd3908b3f8abaa2b03e5d3d73124679b9f` |
> | `meta/DECISIONS.md` | `07e0109ca662ed58d2d34ca861427d0fb6e3118b` | `e920568051fa545e00cd7c48d24982c048306e1e` |
> | `meta/CEREBRO.md` | `2fbaea98043cc68f64fef1ff885319d038bf522c` | `f780941fdd48928c4626c59391bc7354ce5a47a3` |
> | `logs/2026-11-14.md` | `bcc44e7694b9a6e9d23b8908a26632b067d43132` | o mesmo (gravado pelo chat; so versionar) |
>
> **Ancora semantica:** se um trecho-ancora nao bater EXATAMENTE, PARE e reporte.
> **Idempotencia:** antes de cada edicao, procure o texto NOVO INTEIRO; se ja estiver la, PULE e diga no relatorio.
> **Ancoras:** linhas inteiras (uma linha ou um bloco de linhas inteiras), cada uma 1 vez no arquivo no momento da edicao, na ordem abaixo. Toda edicao «substitui a ancora inteira».
> **Âncoras lidas em** (lidas pelo chat NESTE turno, de `2372c10` clonado do GitHub e conferido contra o disco do dono — os arquivos versionados com o mesmo sha1; aplicadas em ordem num clone, com a chegada medida):
> - E01 (`tests/test_formulas.py`, C5 só fórmulas: espera o aviso novo): bloco de 3 linhas, começando por `    page.click("#import-ok-btn")`
> - E02 (`tests/test_formulas.py`, C5 faixas e fórmulas: espera o aviso novo): linha `    page.wait_for_function("document.getElementById('toast').textContent.includes('impor…`
> - E03 (`kit-musica/BLOCO-SUNO.md`, Parte 2: tags de seção e direito de uso): bloco de 4 linhas, começando por `FAIXAS. Relato do dono é a única medida de som; registre-o com a data e a versão do Suno.`
> - E04 (`kit-musica/BLOCO-SUNO.md`, de onde vem: as duas linhas novas): bloco de 2 linhas, começando por `| '[Instrumental]' sozinho; arco só em faixa linear | HISTORY §2, §3 |`
> - E05 (`meta/STATUS.md`, versão e fase: 0.20.0 conferida, Fase 3 concluída): linha `**Versão atual:** 0.20.0 · **Fase:** 3a, 3a.2, o BPM da 3b, o prompt-modelo e as conveni…`
> - E06 (`meta/STATUS.md`, última conversa): bloco de 7 linhas, começando por `## Última conversa (2026-11-14, fórmulas de referência, WO 0038)`
> - E07 (`meta/STATUS.md`, quebrado: o CI do 39ff8d8): bloco de 2 linhas, começando por `- **CI do '790aa3a' verde** (run '43082294050', 4 passos success): o passo «Dependencias…`
> - E08 (`meta/STATUS.md`, pendências: sai a conferência da 0.20.0): bloco de 5 linhas, começando por `## Pendências do dono`
> - E09 (`meta/STATUS.md`, backlog na ordem do dono): bloco de 3 linhas, começando por `1. **Kit de música v2, leva 2** (i-039) — as skills 'escrever-letra-suno' e 'conceber-al…`
> - E10 (`meta/ROADMAP.md`, Fase 3 concluída): linha `## 🔨 Fase 3 — Qualidade de prompt e modularidade`
> - E11 (`meta/ROADMAP.md`, 3b concluída e conferida): linha `**3b — Modularidade (continuação):**`
> - E12 (`meta/IDEAS.md`, i-039: a carta 03 e a 04): bloco de 4 linhas, começando por `**O KCM leu a carta 01 (2026-10-31, aviso '../notas-arquivadas/261031-kcm-leu-01.md'):**…`
> - E13 (`meta/DECISIONS.md`, DEC-038): linha `**Consequências:** (+) As fórmulas validadas saem dos '.md' e ficam a um clique de copia…`
> - E14 (`meta/CEREBRO.md`, técnica: a ponte e o stagedPath repetido): bloco de 4 linhas, começando por `- **Contar por prefixo não é contar.** A spec da entrega 2 disse «7 chaves de outros pro…`
> **Canal dos meta neste ciclo = CODE:** STATUS, DECISIONS, ROADMAP e IDEAS pelo Code (DEC-010), com o texto abaixo; o CEREBRO, que e do chat, vai por WO por ser doc grande; o log ja esta gravado pelo chat. O kit (`BLOCO-SUNO.md`) muda por esta WO, como na leva 1.

---

## 1. Por que

**CI:** os dois testes C5 da 0.20.0 esperavam um aviso que contivesse «importad», e o «Acervo importado» que o `import_demo` deixa no aviso ja satisfazia a espera antes do clique: no CI, o teste leu o aviso velho. O app esta certo; o texto do teste passa a esperar o aviso novo. **Kit:** a carta 03 do KCM pergunta onde nascem as duas linhas que o Album-Referencias pediu (tags de secao por genero; direito de uso e nome de artista). Nascem aqui (DEC-027, DEC-038), para o KCM copiar com carimbo. **Meta:** a 0.20.0 conferida, a Fase 3 concluida, o backlog na ordem do dono, a DEC-038.

## Edicao 0 — Conferencia de hash e de arvore

```
sha1sum tests/test_formulas.py kit-musica/BLOCO-SUNO.md meta/STATUS.md meta/ROADMAP.md meta/IDEAS.md meta/DECISIONS.md meta/CEREBRO.md logs/2026-11-14.md
GIT_OPTIONAL_LOCKS=0 git status --short
```

Todos batem com **partida**; o `git status` mostra exatamente as duas linhas do Pre-requisito. Qualquer outra coisa: **PARE e reporte**.

## Edicoes E01 a E14

Na ordem. Copie o que esta ENTRE as linhas de quatro crases, sem elas. Aplique por script, extraindo os blocos da WO; grave em UTF-8 com LF.

### E01 — C5 só fórmulas: espera o aviso novo

**Arquivo:** `tests/test_formulas.py`

**Ancora:**

````
    page.click("#import-ok-btn")
    page.wait_for_function("document.getElementById('toast').textContent.includes('importad')")
    assert ref_ids(page) == ["f-um", "f-dois", "f-dois-2", "f-nova"]
````

**Texto novo (substitui a ancora inteira):**

````
    page.click("#import-ok-btn")
    # o aviso NOVO: o «Acervo importado» deixado pelo import_demo tambem tem «importad»
    page.wait_for_function("document.getElementById('toast').textContent.includes('fórmulas importadas')")
    assert ref_ids(page) == ["f-um", "f-dois", "f-dois-2", "f-nova"]
````

### E02 — C5 faixas e fórmulas: espera o aviso novo

**Arquivo:** `tests/test_formulas.py`

**Ancora:**

````
    page.wait_for_function("document.getElementById('toast').textContent.includes('importad')")
````

**Texto novo (substitui a ancora inteira):**

````
    page.wait_for_function("document.getElementById('toast').textContent.includes('fórmula importada')")
````

### E03 — Parte 2: tags de seção e direito de uso

**Arquivo:** `kit-musica/BLOCO-SUNO.md`

**Ancora:**

````
FAIXAS. Relato do dono é a única medida de som; registre-o com a data e a versão do Suno.

**A interface do Suno muda.** Limites e campos vêm de fonte secundária (o Suno não publica os do v6).
Se o dono disser que um campo não existe na conta dele (o Exclude não aparece no v6-mini gratuito), acredite
````

**Texto novo (substitui a ancora inteira):**

````
FAIXAS. Relato do dono é a única medida de som; registre-o com a data e a versão do Suno.

**Tags de seção conforme o gênero.** Canção usa `[Verse]`, `[Chorus]`, `[Bridge]`; faixa de arco linear
(instrumental, trilha) usa `[Intro]`, `[Build]`, `[Climax]`, `[Outro]`; `[Drop]` só em eletrônica. Tag de outro
gênero puxa a faixa para ele: na dúvida, o vocabulário neutro.

**Direito de uso e nome de artista: pergunte, nunca suponha.** Antes de subir áudio ao Suno (Cover, Extend de
um áudio) ou de publicar uma faixa, pergunte ao dono se o áudio é dele, em que plano a faixa foi gerada (o uso
comercial depende do plano e dos termos do momento: confira na conta, `macetes-suno` §11) e com que nome de
artista ela sai. Registre a resposta no PROJETO. Isto não é conselho jurídico.

**A interface do Suno muda.** Limites e campos vêm de fonte secundária (o Suno não publica os do v6).
Se o dono disser que um campo não existe na conta dele (o Exclude não aparece no v6-mini gratuito), acredite
````

### E04 — de onde vem: as duas linhas novas

**Arquivo:** `kit-musica/BLOCO-SUNO.md`

**Ancora:**

````
| `[Instrumental]` sozinho; arco só em faixa linear | HISTORY §2, §3 |
| Exclude, não «no X»; v6-mini sem Exclude | HISTORY §5, §11 |
````

**Texto novo (substitui a ancora inteira):**

````
| `[Instrumental]` sozinho; arco só em faixa linear | HISTORY §2, §3 |
| Tags de seção conforme o gênero | HISTORY §3; pedido do Album-Referencias (carta 03 do KCM, 2026-11-14) |
| Direito de uso e nome de artista: perguntar | `macetes-suno` §11; pedido do Album-Referencias (carta 03 do KCM) |
| Exclude, não «no X»; v6-mini sem Exclude | HISTORY §5, §11 |
````

### E05 — versão e fase: 0.20.0 conferida, Fase 3 concluída

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
**Versão atual:** 0.20.0 · **Fase:** 3a, 3a.2, o BPM da 3b, o prompt-modelo e as conveniências de uso concluídos e conferidos · os álbuns antigos convertidos (i-008, fora do repo) · curadoria no app concluída nas três entregas (DEC-028, DEC-029) · frente de interface concluída e conferida nas quatro entregas (DEC-030 a DEC-033) · organizar os álbuns (0.18.0, DEC-035) conferido · rampa de BPM (0.19.0, DEC-036) conferida · fórmulas de referência (0.20.0, DEC-037) entregues, a conferir na tela · a Fase 3b concluída · kit de música lido pelo KCM, à espera da resposta (i-039)
````

**Texto novo (substitui a ancora inteira):**

````
**Versão atual:** 0.20.0 · **Fase:** 3a, 3a.2, o BPM da 3b, o prompt-modelo e as conveniências de uso concluídos e conferidos · os álbuns antigos convertidos (i-008, fora do repo) · curadoria no app concluída nas três entregas (DEC-028, DEC-029) · frente de interface concluída e conferida nas quatro entregas (DEC-030 a DEC-033) · organizar os álbuns (0.18.0, DEC-035) conferido · rampa de BPM (0.19.0, DEC-036) conferida · fórmulas de referência (0.20.0, DEC-037) conferidas na tela · a Fase 3 concluída · kit de música lido pelo KCM, à espera da resposta (i-039)
````

### E06 — última conversa

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
## Última conversa (2026-11-14, fórmulas de referência, WO 0038)

- **0.20.0 implementada pelo chat num clone** pela spec `meta/specs/261111-formulas.md`: o campo `styleReferences`, a janela «Fórmulas», excluir com «Desfazer», a seção «Fórmulas» na importação e o `validate.py`. 61 testes, duas vezes, no clone `[medido pelo chat]`; os 11 novos reprovam no app da 0.19.0.
- **`../acervos/formulas.json` escrito pelo chat** (18 fórmulas, `albums: []`), conferido contra os guias por `../acervos/conferir-formulas.py`: 18 de 18, com a Grand Anthem como única exceção. As linhas dos blocos que já terminam em vírgula não ganham outra.
- **Falta conferir na tela** e importar as fórmulas nos dois acervos (pendência do dono abaixo).
- **Aplicada pelo Code** (`39ff8d8`, empurrado): 12 hashes batem com a chegada; CI vermelho, 2 testes novos (ver «Quebrado»). Pytest local não rodado (trava).
- **Este bloco substitui o anterior** (rampa conferida, fórmulas decididas, WO 0037). O que ele dizia está no CHANGELOG [0.19.0], na DEC-037 e em `logs/2026-11-14.md`.
````

**Texto novo (substitui a ancora inteira):**

````
## Última conversa (2026-11-14, 0.20.0 conferida, carta 03 do KCM, WO 0039)

- **0.20.0 conferida na tela pelo dono** («roteiro das fórmulas na tela ok» `[relatado pelo dono, 2026-11-14 11:32]`), com as fórmulas importadas nos dois acervos. O chat conferiu os dois arquivos salvos `[medido pelo chat]`: BR com 10 álbuns, 151 faixas e as 10 fórmulas da BR; reagrupados com 12 álbuns, 205 faixas e as 8 dos `Albuns/`; as 18 idênticas às do `formulas.json`; esquema conforme e nenhuma chave `_`.
- **CI vermelho do `39ff8d8` era do texto do teste**, não do app: os dois testes C5 esperavam «importad», que o aviso velho «Acervo importado» já satisfazia. A WO 0039 faz esperar o aviso novo.
- **Carta 03 do KCM respondida pela carta 04** (na pasta-pai do KCM): as duas linhas novas nascem aqui, no `BLOCO-SUNO.md` (WO 0039); o prompt de faixa do KCM não pede fórmulas; desde 31/10 nenhum limite mudou (DEC-038).
- **Este bloco substitui o anterior** (0.20.0 implementada, WO 0038). O que ele dizia está no CHANGELOG [0.20.0] e em `logs/2026-11-14.md`.
````

### E07 — quebrado: o CI do 39ff8d8

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
- **CI do `790aa3a` verde** (run `43082294050`, 4 passos success): o passo «Dependencias» novo segurou, e os testes rodaram no CI pela primeira vez desde a 0.18.0. Sem pendência de CI.
- **CI VERMELHO no `39ff8d8` (0.20.0, WO 0038)** — run `43601104563`, `2 failed, 59 passed` `[medido pelo Code]`: `test_c5_importar_so_formulas` e `test_c5_importar_faixas_e_formulas_soma` leem `#toast` e recebem «Acervo importado: Acervo de demonstracao» (o aviso do `import_demo`). Suspeita, não medida: o `wait_for_function(includes('importad'))` casa com o aviso velho; corrida no texto do teste, não no app. Pede WO de correção (esperar o aviso novo); o Code não corrige sem WO.
````

**Texto novo (substitui a ancora inteira):**

````
- **CI do `39ff8d8` vermelho em 2 testes da 0.20.0** (run `43601104563`, `[medido pelo Code]`): corrida no texto dos testes C5, não no app; a WO 0039 corrige. O veredito do CI sai no relatório dela.
````

### E08 — pendências: sai a conferência da 0.20.0

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
## Pendências do dono

- **Conferir a 0.20.0 na tela e importar as fórmulas** — roteiro na conversa de 2026-11-14 (WO 0038): no acervo BR, só as 10 da BR; no reagrupados, só as 8 dos `Albuns/`; salvar os dois.
- **Apagar à mão o `..\sonda-i4-teste.json`** — arquivo de teste da sonda, na pasta-pai (o chat não apaga arquivo seu).
- **Instalar o validador de esquema nesta máquina.** Sem `jsonschema` e `referencing`, o `validate.py` só confere sintaxe e diz `ESQUEMA NAO CONFERIDO` na última linha. Uma vez, no CMD: `pip install jsonschema referencing --break-system-packages`. Depois, `python3 scripts/validate.py` deve terminar em `Tudo conforme ao esquema.` Desde a DEC-034 o CI confere o esquema a cada push: instalar aqui passa a ser opcional.
````

**Texto novo (substitui a ancora inteira):**

````
## Pendências do dono

- **Apagar à mão o `..\sonda-i4-teste.json`** — arquivo de teste da sonda, na pasta-pai (o chat não apaga arquivo seu).
- **Instalar o validador de esquema nesta máquina.** Sem `jsonschema` e `referencing`, o `validate.py` só confere sintaxe e diz `ESQUEMA NAO CONFERIDO` na última linha. Uma vez, no CMD: `pip install jsonschema referencing --break-system-packages`. Depois, `python3 scripts/validate.py` deve terminar em `Tudo conforme ao esquema.` Desde a DEC-034 o CI confere o esquema a cada push: instalar aqui passa a ser opcional.
````

### E09 — backlog na ordem do dono

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
1. **Kit de música v2, leva 2** (i-039) — as skills `escrever-letra-suno` e `conceber-album`, com prova de campo num projeto de música do dono; depois, a carta 02 ao KCM.
2. **Pesquisar outras plataformas de música por IA** (i-032) — um turno de pesquisa antes de qualquer mudança de esquema.
3. **Avisar palavra de andamento que contradiz o BPM** (i-029) — pede uma tabela palavra → faixa de BPM, com fonte e data.
````

**Texto novo (substitui a ancora inteira):**

````
Ordem decidida pelo dono em 2026-11-14 `[relatado pelo dono]`: primeiro o kit no KCM e os projetos de música; depois a paleta e a leva 2; o resto depois de um recesso.

1. **Kit de música no KCM** (i-039, DEC-038) — o dono decide os três pontos da análise do KCM; o KCM faz a WO dele copiando o `kit-musica/` com carimbo. Depois, o projeto da Rainha da Preguiça abre pelo nicho Música com o Suno ligado.
2. **Paleta de módulos do acervo** (i-052) — pede análise; depois dos primeiros projetos.
3. **Kit de música v2, leva 2** (i-039) — as skills `escrever-letra-suno` e `conceber-album`, com prova de campo no projeto da Rainha; depois, uma carta ao KCM.
4. **Depois de um recesso:** outras plataformas de música por IA (i-032), palavra de andamento contra o BPM (i-029) e arrastar faixa para outro acervo (i-050).
````

### E10 — Fase 3 concluída

**Arquivo:** `meta/ROADMAP.md`

**Ancora:**

````
## 🔨 Fase 3 — Qualidade de prompt e modularidade
````

**Texto novo (substitui a ancora inteira):**

````
## ✅ Fase 3 — Qualidade de prompt e modularidade (2026-11-14)
````

### E11 — 3b concluída e conferida

**Arquivo:** `meta/ROADMAP.md`

**Ancora:**

````
**3b — Modularidade (continuação):**
````

**Texto novo (substitui a ancora inteira):**

````
**3b — Modularidade (continuação) — ✅ concluída em 0.20.0, conferida na tela pelo dono em 2026-11-14:**
````

### E12 — i-039: a carta 03 e a 04

**Arquivo:** `meta/IDEAS.md`

**Ancora:**

````
**O KCM leu a carta 01 (2026-10-31, aviso `../notas-arquivadas/261031-kcm-leu-01.md`):** foi para a i-N25 deles, cujo próximo passo é analisar o eixo «Produção: tocada / gerada por IA» com o teto das Instruções medido; o feedback ao kit foi para a i-N76; o Cancioneiro entrou no livro de leitura. A resposta vem pela carta 02, sem data. O gatilho acima continua valendo.
**Kit v2 (análise `meta/analises/261109-ANALISE-kit-de-musica-v2.md`, decidida pelo dono em 2026-11-09):** leva 1 entregue em 2026-11-09 — o README na 0.17.0, a `macetes-suno` com «Depois de ouvir» (§10) e as ferramentas do Suno de 2026 (§11), o ciclo do bloco com elas. Leva 2 (skills `escrever-letra-suno` e `conceber-album`) espera um projeto de música para a prova de campo; a carta 02 ao KCM vai depois dela.

### i-040 ✅ Curadoria no app: excluir, exportar e importar faixas
````

**Texto novo (substitui a ancora inteira):**

````
**O KCM leu a carta 01 (2026-10-31, aviso `../notas-arquivadas/261031-kcm-leu-01.md`):** foi para a i-N25 deles, cujo próximo passo é analisar o eixo «Produção: tocada / gerada por IA» com o teto das Instruções medido; o feedback ao kit foi para a i-N76; o Cancioneiro entrou no livro de leitura. A resposta vem pela carta 02, sem data. O gatilho acima continua valendo.
**Kit v2 (análise `meta/analises/261109-ANALISE-kit-de-musica-v2.md`, decidida pelo dono em 2026-11-09):** leva 1 entregue em 2026-11-09 — o README na 0.17.0, a `macetes-suno` com «Depois de ouvir» (§10) e as ferramentas do Suno de 2026 (§11), o ciclo do bloco com elas. Leva 2 (skills `escrever-letra-suno` e `conceber-album`) espera um projeto de música para a prova de campo; a carta 02 ao KCM vai depois dela.
**Carta 03 do KCM (2026-11-14, `../notas-arquivadas/261114-kcm-para-cancioneiro-03-o-suno-no-nicho-musica.md`):** o KCM propõe um eixo «Produção» no nicho Música (análise `261114-ANALISE-musica-gerada-por-ia.md` deles) e copiar o bloco e as skills com carimbo. Respondida pela carta 04 (DEC-038): as duas linhas novas (tags de seção por gênero; direito de uso e nome de artista) nascem no `BLOCO-SUNO.md` (WO 0039); o prompt de faixa não pede fórmulas; nenhum limite mudou desde 31/10. A «carta 02» das linhas acima era o nome provisório da próxima carta; a 02 de fato foi a das chaves no `file://` (2026-11-05), e a próxima, de qualquer lado, é a 05.

### i-040 ✅ Curadoria no app: excluir, exportar e importar faixas
````

### E13 — DEC-038

**Arquivo:** `meta/DECISIONS.md`

**Ancora:**

````
**Consequências:** (+) As fórmulas validadas saem dos `.md` e ficam a um clique de copiar, separadas do «por que funciona». (+) Nada muda para quem não tem fórmulas. (−) Um campo a mais no esquema e uma janela a mais. (−) Fórmula envelhece com o Suno; a linha de qualidade e o `source` mostram de onde e de quando ela veio.
````

**Texto novo (substitui a ancora inteira):**

````
**Consequências:** (+) As fórmulas validadas saem dos `.md` e ficam a um clique de copiar, separadas do «por que funciona». (+) Nada muda para quem não tem fórmulas. (−) Um campo a mais no esquema e uma janela a mais. (−) Fórmula envelhece com o Suno; a linha de qualidade e o `source` mostram de onde e de quando ela veio.

## DEC-038 — Carta 03 do KCM: as regras novas do Suno nascem no `kit-musica/`; o prompt de faixa não pede fórmulas; o carimbo é o commit

**Data:** 2026-11-14
**Status:** aceita
**Contexto:** A carta 03 do KCM (2026-11-14) anuncia o Suno no nicho Música, copiado do `kit-musica/` com carimbo de origem (a análise deles recomenda a opção B), e faz três perguntas antes da WO deles: onde nascem as duas linhas que o Album-Referencias pediu, se o prompt de faixa deles pede as fórmulas da 0.20.0, e o que mudou desde 31/10.
**Decisão:**
- **As duas linhas novas nascem aqui**, na Parte 2 do `BLOCO-SUNO.md` (WO 0039): tags de seção conforme o gênero (HISTORY §3) e direito de uso e nome de artista (perguntar ao dono, nunca supor). É a DEC-027: o KCM copia daqui, não o contrário; uma regra escrita só do lado deles derivaria sem fonte.
- **O prompt «Gerar faixa para o Suno» do KCM não pede fórmula.** Fórmula é acervo do dono, opcional, e o prompt-modelo não a ensina (DEC-037, ponto 4); pedir ao chat que invente uma seria gerar o que o dono já tem validado. Quem quer uma fórmula copia da janela «Fórmulas» e cola no pedido.
- **O carimbo é o commit e a data do Cancioneiro de onde o texto foi copiado.** Mudança de limite, de campo do JSON ou de regra do prompt-modelo chega por carta, com o commit.
**Alternativas consideradas:** o KCM acrescentar as linhas do lado dele (deriva); ensinar `styleReferences` ao prompt de faixa (o prompt cresce, e o chat inventaria fórmula sem validação).
**Consequências:** (+) Uma fonte só para as regras do Suno. (−) Toda regra nova do kit pede uma carta e uma WO do KCM.
````

### E14 — técnica: a ponte e o stagedPath repetido

**Arquivo:** `meta/CEREBRO.md`

**Ancora:**

````
- **Contar por prefixo não é contar.** A spec da entrega 2 disse «7 chaves de outros projetos» contando os `kit-state-*`; eram 9. Contagem que vai para documento sai do item por item, não do padrão que a maioria segue.
- **Checagem de WO não usa emoji no padrão do `grep`.** No shell do Code, `grep -c '🔨'` devolve 0 com o emoji presente (WO 0017, checagem 5). Conte pelo texto vizinho (`'^### i-03[03-7] '`) ou pelo hash.

## Princípios de trabalho
````

**Texto novo (substitui a ancora inteira):**

````
- **Contar por prefixo não é contar.** A spec da entrega 2 disse «7 chaves de outros projetos» contando os `kit-state-*`; eram 9. Contagem que vai para documento sai do item por item, não do padrão que a maioria segue.
- **Checagem de WO não usa emoji no padrão do `grep`.** No shell do Code, `grep -c '🔨'` devolve 0 com o emoji presente (WO 0017, checagem 5). Conte pelo texto vizinho (`'^### i-03[03-7] '`) ou pelo hash.
- **Ponte · `device_commit_files` com o mesmo `stagedPath` pode gravar o conteúdo velho.** Em 2026-11-14 o chat regravou o log pelo mesmo nome em `outputs/` e o disco recebeu a versão de horas antes, apagando a seção do Code (recuperada do Git no mesmo turno). Grave cada entrega com um nome novo em `outputs/` e confira o `sha1sum` no disco do dono depois de gravar.

## Princípios de trabalho
````

## Depois de aplicar — conferencia antes do commit

| # | Checagem | Comando | Esperado |
|---|---|---|---|
| 1 | Os arquivos sao os previstos | `sha1sum tests/test_formulas.py kit-musica/BLOCO-SUNO.md meta/STATUS.md meta/ROADMAP.md meta/IDEAS.md meta/DECISIONS.md meta/CEREBRO.md logs/2026-11-14.md` | a coluna **chegada** |
| 2 | Os testes esperam o aviso novo | `grep -c "includes('importad')" tests/test_formulas.py` | `0` |
| 3 | As duas linhas no kit | `grep -c '^\*\*Tags de seção conforme o gênero' kit-musica/BLOCO-SUNO.md` e `grep -c '^## DEC-038' meta/DECISIONS.md` | `1` e `1` |
| 4 | Validacao | `python3 scripts/validate.py; echo "exit=$?"` | `exit=0`, versao 0.20.0 |
| 5 | Nada alem do previsto | `GIT_OPTIONAL_LOCKS=0 git status --short --untracked-files=all` | os 8 arquivos da tabela e esta WO |
| 6 | Depois do push: o CI | `gh run list --limit 1`, em laco com `gh run view <id> --json status,conclusion` ate `completed` | `success`; se vermelho, o passo e as ultimas 30 linhas de `gh run view <id> --log-failed` |

As checagens 2 a 4 rodaram no clone do chat; no Git Bash, **nao testado**. O chat rodou os 61 testes tres vezes seguidas no clone (cerca de 46 s). O pytest local do Code nao roda: o veredito e o CI (checagem 6).
**Esta e qual pergunta?** A 1 responde «esta la?»; a 6 responde «o CI volta ao verde?».

## Relatorio de aplicacao

Grave em `../AAMMDD-HHMM-code-cancioneiro-apply-wo0039.txt`, com o carimbo de `date +%y%m%d-%H%M` rodado na hora. Checagem 1 em primeiro lugar e o estado final do CI. **Sem `/wrap` depois desta WO**, e sem secao sua no log, salvo se algo fugir do literal.

## Commit

```
git add tests/test_formulas.py kit-musica/BLOCO-SUNO.md meta/STATUS.md meta/ROADMAP.md meta/IDEAS.md meta/DECISIONS.md meta/CEREBRO.md logs/2026-11-14.md meta/workorders/261114-wo0039-testes-c5-e-carta-03.md
```

```
git commit -m "fix: testes das formulas esperam o aviso novo; kit com tags de secao e direito de uso" -m "Os testes C5 liam o aviso velho do import_demo no CI. BLOCO-SUNO ganha as duas linhas pedidas pela carta 03 do KCM (DEC-038). 0.20.0 conferida, Fase 3 concluida, backlog na ordem do dono."
```

```
git push
```
