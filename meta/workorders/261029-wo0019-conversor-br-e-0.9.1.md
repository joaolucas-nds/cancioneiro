# WO 0019 — Conversor da familia BR, 0.9.1 e registro das frentes novas

## Cabecalho

> **Tipo:** WO de CODIGO (`scripts/`, versao do app) e de registro.
> **Config sugerida:** Sonnet · `/effort medium`. 15 edicoes literais e 4 arquivos inteiros (3 novos e o STATUS), todos aplicados e testados pelo chat numa copia; cada arquivo tem hash de chegada.
> **Pre-requisito:** commit `550fc3f`, branch `main`, sincronizada com `origin/main`. Arvore: **so** `?? meta/analises/261029-ANALISE-conversao-dos-albuns.md` (escrita pelo chat, versionada por esta WO) e esta WO como `??`.
> **Base:** decisoes do dono 1A, 2A, 3A, 4A da analise da conversao, e «os acervos convertidos nao sao versionados» (2026-10-29); ajustes da DEC-025 conferidos na tela pelo dono; nota `261029-1825.txt`.
> **Depende de:** WO 0018, ja aplicada (`2a20448`, wrap `550fc3f`).
>
> **Arquivos — partida e chegada, os dois medidos pelo chat** (partida conferida no disco do dono em 2026-10-29; chegada = resultado de aplicar literalmente as edicoes abaixo, em LF):
>
> | arquivo | partida (sha1) | chegada (sha1) |
> |---|---|---|
> | `app/index.html` | `847eb02a7c406b319774dd228aae22131b665a55` | `1bba24aa98ee575d98ffdb103e308a168f8b044e` |
> | `meta/CHANGELOG.md` | `f50cb2e4a94531ccdf9529411b34fbf8bc837fbc` | `7ee775b065e90cf6439a51f0ec3832e46f1b5f9c` |
> | `README.md` | `e1e398c1ed7f0f38c36d3a67ae09a19999ccfdd8` | `4ee8f90ffbb04f4611cdc1e4213f017f35fa58b9` |
> | `meta/CONTEXT.md` | `9452ee0c709c33cb90a48030cd0d840b63863e8c` | `c66682378c223edadda1f2e27c96e8a5bd525b0a` |
> | `meta/analises/261029-ANALISE-conversao-dos-albuns.md` | `5502d86a24c8265eb6eab66dd0715c2938dfe51f` | `f3cc98227eab129939ced75ad47f8db509be5bc5` |
> | `meta/IDEAS.md` | `2ff070a9b32b83bc68e78d05338f79a2d76fd817` | `8565acfdc0e9d818547e7f873124783cd2558a24` |
> | `meta/ROADMAP.md` | `d9dcadf05d61e3a37ac8a4c0b24e6e5c3692d666` | `2539ded2102f0f282a340d089e034f511936ee4b` |
> | `meta/DECISIONS.md` | `6c9188d523bbec4a3722214d9c7c06d804fb8c5b` | `7a011004f9ac99d31fc672c714ed7dd220716d04` |
> | `logs/2026-10-29.md` | `1228e5310cec2833c292def5b3b5b562cc4dca63` | `1365ba5950da449bedd90803e78d7eb43c3cfa74` |
> | `scripts/convert_br.py` | (nao existe) | `ec91466a05fc16f6a65e1e1b3cbb8fec95b0c158` |
> | `scripts/test_convert_br.py` | (nao existe) | `5b2e209ad296a1be9d5981f71451573ec3fa3206` |
> | `meta/analises/261029-ANALISE-kit-de-musica.md` | (nao existe) | `354f04adb7b04ca3f615591e79238bde1eb16f1a` |
> | `meta/STATUS.md` | `5e8cfdbb7fa2663f6c4e42a8240e8a32a17eb21a` | `243cd20dd22197f7eda429cd511a1fd6b48f8d2f` |
>
> **Ancora semantica:** se um trecho-ancora nao bater EXATAMENTE, PARE e reporte.
> **Idempotencia:** antes de cada edicao, procure o texto NOVO INTEIRO; se ja estiver la, PULE e diga no relatorio. Arquivo inteiro: se o hash ja for o de chegada, PULE.
>
> **Ancoras lidas em:** cada ancora foi extraida pelo chat do arquivo de partida (`git show 550fc3f:<arquivo>`, e a analise da conversao do disco do dono) e conferida como ocorrendo **exatamente 1 vez** no estado em que a edicao e aplicada, na ordem abaixo.

---

## 1. Por que

**i-008, familia BR.** O dono decidiu 1A a 4A: conversor deterministico por familia, acervo fora do repo, um
acervo com um album por volume, conversao fiel. O chat escreveu `scripts/convert_br.py` e o teste com guia
sintetico, rodou nos dez volumes e mediu: **151 de 151** faixas, 0 rotulos no copiavel, igual ao prototipo;
o acervo ja esta em `../acervos/rainha-da-preguica.json` e abre no app. O repo recebe so o conversor — nenhuma
letra (DEC-026).

**0.9.1:** os ajustes da DEC-025 que estavam em `[Unreleased]` (o dono conferiu na tela) e o conversor.

**Registro:** DEC-026; a analise da conversao com status e desfecho (inclui o erro de conta «11 albuns», que sao
10); a analise nova do kit de musica (i-039), em discussao; IDEAS i-038 a i-042 (grupos de `Albuns/`, kit de
musica, curadoria no app e mais de um acervo — da nota 1825 —, rampa de BPM) e a revisao da x-001; ROADMAP;
CONTEXT e README com `scripts/`; log; STATUS.

## Edicao 0 — Conferencia de hash e de arvore

```
sha1sum app/index.html meta/CHANGELOG.md README.md meta/CONTEXT.md meta/analises/261029-ANALISE-conversao-dos-albuns.md meta/IDEAS.md meta/ROADMAP.md meta/DECISIONS.md logs/2026-10-29.md meta/STATUS.md
ls scripts
GIT_OPTIONAL_LOCKS=0 git status --short
```

Os dez batem com a coluna **partida**; `scripts` tem so `validate.py`; o `git status` mostra so a analise da
conversao e esta WO como `??`. Qualquer outra coisa: **PARE e reporte**.

## Edicoes E01 a E19

Na ordem. **Todas as secoes de edicao tem o mesmo titulo, `### Exx — ...`**, inclusive as de arquivo inteiro.
Copie o que esta ENTRE as linhas de quatro crases, sem elas. **O bloco termina na linha de quatro crases, nunca
num titulo:** varios blocos trazem `## `, `### ` ou cercas de tres crases.

### E01 — app: versao (1) — `app/index.html`

**Ancora, literal:**

````
         que app, CHANGELOG, README e STATUS dizem a mesma (i-027). -->
    <span class="version" data-role="app-version">v0.9.0</span>
  </div>
````

**Texto novo, literal:**

````
         que app, CHANGELOG, README e STATUS dizem a mesma (i-027). -->
    <span class="version" data-role="app-version">v0.9.1</span>
  </div>
````

### E02 — CHANGELOG: [0.9.1] (1) — `meta/CHANGELOG.md`

**Ancora, literal:**

````

## [Unreleased]

Ajustes de tela pedidos pelo dono depois de conferir a 0.9.0 (nota `261029-1618.txt`, DEC-025). Viram 0.9.1 depois de vistos na tela.

````

**Texto novo, literal:**

````

## [0.9.1] — 2026-10-29

Ajustes de tela pedidos pelo dono depois de conferir a 0.9.0 (nota `261029-1618.txt`, DEC-025), vistos na tela. E o primeiro conversor dos guias antigos (i-008, DEC-026).

### Added
- **Conversor da familia BR (`scripts/convert_br.py`, DEC-026):** le os guias `..._VOL<n>_GUIA.md` da «Rainha da Preguiça» e grava uma colecao no esquema, um album por volume. Tira os rotulos `[ESTILO SUNO]` e `[LETRA]` do que e copiavel, leva as variantes `VAR A/B` e os campos de referencia (Conceito, Voz, Instrumentos, conversa de origem). Conversao fiel: letra longa e style com tags demais nao sao cortados, o relatorio conta. Teste com guia sintetico em `scripts/test_convert_br.py` (8 casos, sem letra real no repo). Medido no acervo do dono: 151 de 151 faixas, 10 albuns; o arquivo gerado fica fora do repo.

````

### E03 — README (1) — `README.md`

**Ancora, literal:**

````

> **Estado:** v0.9.0 — ferramenta em uso. Lê o acervo, copia por campo, troca módulos de estilo, ajusta o BPM, **mede cada prompt contra os limites do Suno**, exporta Markdown e **entrega o prompt para chats gerarem canções no esquema**. Publicada no GitHub Pages. Ver `meta/ROADMAP.md`.

````

**Texto novo, literal:**

````

> **Estado:** v0.9.1 — ferramenta em uso. Lê o acervo, copia por campo, troca módulos de estilo, ajusta o BPM, **mede cada prompt contra os limites do Suno**, exporta Markdown e **entrega o prompt para chats gerarem canções no esquema**. Publicada no GitHub Pages. Ver `meta/ROADMAP.md`.

````

### E04 — README (2) — `README.md`

**Ancora, literal:**

````
├── schema/                    # o contrato JSON (song, collection, style-modules)
├── data/                      # o acervo real, no esquema
├── app/                       # a ferramenta (index.html)
````

**Texto novo, literal:**

````
├── schema/                    # o contrato JSON (song, collection, style-modules)
├── scripts/                   # validador e conversores dos guias antigos
├── data/                      # exemplos no esquema (o acervo pessoal mora fora do repo)
├── app/                       # a ferramenta (index.html)
````

### E05 — README (3) — `README.md`

**Ancora, literal:**

````

## Gerar canções com um chat
````

**Texto novo, literal:**

````

## Converter guias antigos

Guias `.md` da família BR (`..._VOL<n>_GUIA.md`) viram um acervo no esquema com um comando — grave a saída **fora do repo**, porque letra e persona são suas:

```
python3 scripts/convert_br.py ../acervos/rainha-da-preguica.json "../Album Rainha da Preguiça/ALBUM_BR_VOL1_GUIA.md" "../Album Rainha da Preguiça/ALBUM_BR_VOL2_GUIA.md"
```

Liste quantos volumes quiser. O conversor tira os rótulos do que é copiável, não corta nada e diz no fim quantas letras e styles passam do limite do Suno — o painel do app marca as mesmas. Depois, arraste o `.json` gerado para o app. Outras famílias de guia pedem outro conversor (ver `meta/analises/`).

## Gerar canções com um chat
````

### E06 — README (4) — `README.md`

**Ancora, literal:**

````

O acervo canônico são os **arquivos JSON versionados** em `data/`. O navegador (localStorage) guarda as marcações, a estrutura do cartão e uma **cópia do último acervo importado** — cache, nunca a fonte: a linha de origem diz de onde ela veio e quando, e *esquecer* a apaga. Ver `meta/DECISIONS.md` (DEC-004, DEC-022).

````

**Texto novo, literal:**

````

O acervo canônico são **arquivos JSON** no esquema: os exemplos versionados em `data/`, e o acervo pessoal fora do repo (DEC-026). O navegador (localStorage) guarda as marcações, a estrutura do cartão e uma **cópia do último acervo importado** — cache, nunca a fonte: a linha de origem diz de onde ela veio e quando, e *esquecer* a apaga. Ver `meta/DECISIONS.md` (DEC-004, DEC-022).

````

### E07 — CONTEXT: estrutura (1) — `meta/CONTEXT.md`

**Ancora, literal:**

````
├── scripts/
│   └── validate.py            # valida data/ contra o schema
├── data/                      # o acervo real, no esquema
````

**Texto novo, literal:**

````
├── scripts/
│   ├── validate.py            # valida data/ contra o schema
│   ├── convert_br.py          # guias BR antigos -> colecao no esquema (DEC-026)
│   └── test_convert_br.py     # teste do conversor, com guia sintetico
├── data/                      # o acervo real, no esquema
````

### E08 — analise da conversao: status e desfecho (1) — `meta/analises/261029-ANALISE-conversao-dos-albuns.md`

**Ancora, literal:**

````

> **Status:** Em discussão — espera as decisões 1 a 4 do dono (fim deste arquivo).
> **Data:** 2026-10-29 (data de criação; não muda depois)
````

**Texto novo, literal:**

````

> **Status:** Implementada (0.9.1) — decidida pelo dono em 2026-10-29: 1A, 2A, 3A, 4A (ver Desfecho).
> **Data:** 2026-10-29 (data de criação; não muda depois)
````

### E09 — analise da conversao: status e desfecho (2) — `meta/analises/261029-ANALISE-conversao-dos-albuns.md`

**Ancora, literal:**

````
com a 0.9.1; o dono roda um comando para gerar o acervo dele (o arquivo fica na pasta-pai) e confere na tela.
````

**Texto novo, literal:**

````
com a 0.9.1; o dono roda um comando para gerar o acervo dele (o arquivo fica na pasta-pai) e confere na tela.

## Desfecho — 2026-10-29

**Decidido pelo dono: 1A, 2A, 3A, 4A**, e mais: os acervos convertidos são produtos para outros projetos e
álbuns, **não são versionados** neste repo (reforça a 2A). Registrado na DEC-026.

**Implementado (0.9.1):** `scripts/convert_br.py`, com teste em guia sintético (`scripts/test_convert_br.py`, 8
casos). Medido nos dez volumes `[medido por instrumento]`:
- **151 de 151** cabeçalhos viraram faixa; 0 rótulos em `style`/`lyrics`; 2 variantes em cada faixa; nenhuma
  diferença contra o protótipo nos campos copiáveis.
- **Dez álbuns, não onze:** a 3A dizia «11 álbuns (VOL1 a VOL10 + nada do índice)» — são dez volumes; o 11º
  arquivo é o índice, que não vira álbum. Erro de conta desta análise.
- Letras: **72 de 151 acima de 5.000** caracteres, 141 acima de 3.000. Styles: **138 de 151 com mais de 10 tags**.
- BPM: **três** faixas com rampa de andamento de propósito («95 BPM to 118 BPM», br2-09, br3-07, br4-07), não
  uma; ficam com `bpm` vazio e o `validate.py` as reprova (DEC-020) — ver i-042. Nenhum BPM em faixa
  («120–130 BPM») nos dez volumes.
- No app: 151 cartões, sem erro; cópia no navegador ~955 mil caracteres.
- Saída gravada em `../acervos/rainha-da-preguica.json`, fora do repo.

**O que fica:** `Albuns/` (oito arquivos, 172 faixas) espera a aprovação dos grupos (i-038); o índice-mestre segue
para o ⬜ «importar prompts prontos como módulos».
````

### E10 — IDEAS (1) — `meta/IDEAS.md`

**Ancora, literal:**

````
**Desbloqueada em 2026-10-29:** o dono trouxe os álbuns para a pasta-pai — `../Album Rainha da Preguiça/` (11 arquivos: índice-mestre e 10 volumes) e `../Albuns/` (8 guias, entre eles o `album_guia_suno.md`), cerca de 44 mil linhas `[medido por instrumento: wc -l]`. Ainda não lidos: frente própria.

````

**Texto novo, literal:**

````
**Desbloqueada em 2026-10-29:** o dono trouxe os álbuns para a pasta-pai — `../Album Rainha da Preguiça/` (11 arquivos: índice-mestre e 10 volumes) e `../Albuns/` (8 guias, entre eles o `album_guia_suno.md`), cerca de 44 mil linhas `[medido por instrumento: wc -l]`. Ainda não lidos: frente própria.
**Em trabalho (2026-10-29):** sonda e análise `meta/analises/261029-ANALISE-conversao-dos-albuns.md`, decidida 1A a 4A (DEC-026): conversor determinístico por família, acervo fora do repo. A família BR está convertida (0.9.1, `scripts/convert_br.py`, 151 faixas). `Albuns/` espera os grupos da i-038.

````

### E11 — IDEAS (2) — `meta/IDEAS.md`

**Ancora, literal:**

````

## Feedback para o Kit
````

**Texto novo, literal:**

````

### i-038 💡 Reagrupar as faixas de `Albuns/` em álbuns por cena de uso
`[relatado pelo dono, 2026-10-29]` Os oito guias de `Albuns/` misturam gêneros, idiomas e propósitos num arquivo só. O dono quer as faixas em álbuns mais relacionados, para depois ampliar cada um num projeto próprio. Proposta do chat em `../261029-PROPOSTA-grupos-albuns.md` (fora do repo: traz os títulos): 172 faixas em 12 álbuns (épico vocal, trilhas de jogo, romântico multilíngue, Brasil popular, pop asiático, latino, contagem e ritmo, matemática e física, código, foco e estudo, eletrônico instrumental, treino e ação). Um mapa faixa → álbum aplica a escolha por script. Espera a aprovação do dono; depois, conversores dos formatos de `Albuns/` (i-008).

### i-039 💡 Kit de música para os projetos do KCM
`[relatado pelo dono, 2026-10-29]` Criar projetos de música para o Suno já «profissionais» e adaptados ao Cancioneiro: levar ao nicho de música do KCM o que este projeto sabe. Junta i-022, i-023 e o feedback ao kit de 2026-10-28. Análise `meta/analises/261029-ANALISE-kit-de-musica.md`, em discussão: Instruções-modelo de projeto de música, skill de macetes do Suno, skill de revisão de faixa. A medida que motiva: nos guias antigos, 72 de 151 letras passam do limite em que o Suno corta.

### i-040 💡 Curadoria no app: excluir, exportar e importar faixas
`[relatado pelo dono, 2026-10-29, nota 261029-1825.txt]` Exportar uma faixa como `.json` (além do `.md`); excluir uma faixa; importar faixas para o acervo aberto — todas ou as escolhidas de outro `.json` de álbum, ou uma faixa exportada solta; mudar a ordem e levar faixas de um álbum a outro. Leva o app de leitor a editor leve: pede análise antes de spec, porque mexe na fonte de verdade (DEC-004, DEC-022 — hoje a cópia no navegador é cache do arquivo; editar nela cria um acervo que só existe ali até «Baixar .json»). Ids repetidos e módulos citados na importação também. Faria o reagrupamento da i-038 pela tela.

### i-041 💡 Mais de um acervo guardado no navegador
`[relatado pelo dono, 2026-10-29, nota 261029-1825.txt]` Hoje a DEC-022 guarda só o último importado. Com os acervos convertidos (Rainha da Preguiça, os álbuns de `Albuns/`), trocar de acervo obriga a importar de novo. Medida: a Rainha da Preguiça ocupa ~955 mil caracteres na cópia; o `localStorage` costuma dar ~5 MB por site — dois ou três acervos grandes cabem, mais que isso pede IndexedDB. Anda junto com a i-040.

### i-042 💡 Rampa de BPM no style («95 BPM to 118 BPM»)
Achado na conversão BR: três faixas mudam de andamento de propósito. A DEC-020 reprova dois BPM no `validate.py`, e o controle de BPM do cartão igualaria os dois números. Decidir: o controle não aparecer (ou avisar) quando o style tem uma rampa, e o `validate.py` aceitar o par ligado por «to»/«building to», sem perder o erro de autoria que a DEC-020 pega.

## Feedback para o Kit
````

### E12 — IDEAS (3) — `meta/IDEAS.md`

**Ancora, literal:**

````
Descartado na fundação: as convenções divergentes entre álbuns tornariam o parser um poço de exceções. Conversão semi-assistida por chat é mais confiável. Ver DEC-001.

````

**Texto novo, literal:**

````
Descartado na fundação: as convenções divergentes entre álbuns tornariam o parser um poço de exceções. Conversão semi-assistida por chat é mais confiável. Ver DEC-001.
**Revista em 2026-10-29 (DEC-026):** o universal segue descartado; um conversor **por família**, medida como regular, entrou — a família BR, 151 de 151. A conversão por chat ficou para formatos pequenos e irregulares: copiar letra longa sem alterar é onde chat corta.

````

### E13 — ROADMAP (1) — `meta/ROADMAP.md`

**Ancora, literal:**

````
- ✅ Script de validação de acervo `scripts/validate.py`.
- ✅ Conveniências de uso: estrutura do cartão configurável, copiar título, arrastar o `.json`, acervo guardado no navegador, prompt que entrega arquivo, export de álbum com o Style da tela (DEC-022, DEC-023; i-030, i-033 a i-037) — 0.9.0, conferidas e retestadas pelo dono; ajustes de tela em [Unreleased] (DEC-025).
- ⬜ Converter `album_guia_suno.md` inteiro como segundo dataset (i-008).
**Marco:** conseguir usar a ferramenta de verdade numa rodada de geração no Suno.
````

**Texto novo, literal:**

````
- ✅ Script de validação de acervo `scripts/validate.py`.
- ✅ Conveniências de uso: estrutura do cartão configurável, copiar título, arrastar o `.json`, acervo guardado no navegador, prompt que entrega arquivo, export de álbum com o Style da tela (DEC-022, DEC-023; i-030, i-033 a i-037) — 0.9.0, conferidas e retestadas pelo dono; ajustes de tela na 0.9.1 (DEC-025), vistos pelo dono.
- 🔄 Converter os álbuns antigos (i-008, DEC-026): a família BR convertida por `scripts/convert_br.py` na 0.9.1 (151 faixas, acervo fora do repo); `Albuns/` espera os grupos (i-038).
**Marco:** conseguir usar a ferramenta de verdade numa rodada de geração no Suno.
````

### E14 — DEC-026 no fim (1) — `meta/DECISIONS.md`

**Ancora, literal:**

````
**Consequências:** (+) Menos ruído na tela de quem usa o plano gratuito. (−) Quem usa o Exclude (Pro, outra plataforma) precisa ligá-lo uma vez na estrutura. (−) O título passa a ter ação ao clicar — selecionar texto do título com o mouse copia em vez de selecionar.
````

**Texto novo, literal:**

````
**Consequências:** (+) Menos ruído na tela de quem usa o plano gratuito. (−) Quem usa o Exclude (Pro, outra plataforma) precisa ligá-lo uma vez na estrutura. (−) O título passa a ter ação ao clicar — selecionar texto do título com o mouse copia em vez de selecionar.

## DEC-026 — Guias antigos entram por conversor determinístico por família; o acervo convertido mora fora do repo

**Data:** 2026-10-29
**Status:** aceita
**Contexto:** A i-008 (converter os álbuns antigos) foi desbloqueada com 19 guias na pasta-pai. A fundação descartou o parser universal e apostou em conversão por chat (x-001, DEC-001). A sonda de 2026-10-29 mediu a família BR («Rainha da Preguiça», dez volumes) como regular — cada volume com cabeçalhos, blocos de letra e pares de variante em igual número — e letras longas: mediana perto de 5.000 caracteres, onde chat corta ou parafraseia. Análise `meta/analises/261029-ANALISE-conversao-dos-albuns.md`; o dono decidiu 1A, 2A, 3A, 4A.
**Decisão:** (1) Cada família de guia regular ganha um conversor em `scripts/`, que copia letra e estilo sem alterar, tira os rótulos do copiável e relata o que não entendeu em vez de adivinhar; o primeiro é `scripts/convert_br.py`, testado sobre guia sintético. (2) O acervo convertido é produto do dono para outros projetos: grava-se fora do repo (pasta-pai, `../acervos/`) e não é versionado — o repo guarda o conversor, nunca a letra. (3) Um acervo por família, um álbum por volume. (4) Conversão fiel: o que passa do limite do Suno não é cortado; o relatório conta e o painel de qualidade mostra.
**Alternativas consideradas:** conversão por chat, volume a volume (descartada para a BR: é onde o chat corta e não há como conferir sem comparar com o original); à mão (viável só para formatos pequenos); acervo em `data/`, publicado no Pages (perde a privacidade da letra e da persona); um arquivo por volume (obriga a trocar de acervo para mudar de volume); cortar no limite (perde texto em silêncio, o mesmo defeito do Suno).
**Consequências:** (+) 151 faixas no esquema com um comando, conferíveis contra o original; o painel passa a mostrar o que o Suno cortaria (72 letras). (+) O repo continua sem material pessoal. (−) Cada formato novo de guia pede o seu conversor, ou uma decisão de converter de outro jeito. (−) O acervo convertido não tem histórico no Git: regerar é rodar o conversor de novo.
````

### E15 — log: Conversa 7 no fim (1) — `logs/2026-10-29.md`

**Ancora, literal:**

````
i-008: sonda nos álbuns antigos; 0.9.1 na primeira WO dela.
````

**Texto novo, literal:**

````
i-008: sonda nos álbuns antigos; 0.9.1 na primeira WO dela.

## Conversa 7 — chat: conversão da família BR, grupos de `Albuns/` e kit de música (WO 0019)

### Objetivo do dia
Executar as decisões da conversão (1A a 4A), propor grupos para `Albuns/` e abrir a frente do kit de música para o KCM.

### Feito
- `scripts/convert_br.py` e `scripts/test_convert_br.py` (8 casos, guia sintético). Nos dez volumes: 151 de 151 faixas, 0 rótulos no copiável, 2 variantes por faixa, igual ao protótipo `[medido por instrumento]`. Acervo gravado em `../acervos/rainha-da-preguica.json` (fora do repo) e importado no app: 151 cartões, sem erro.
- Medidas para o dono: 72 de 151 letras acima de 5.000 caracteres; 138 de 151 styles acima de 10 tags; três rampas de BPM (br2-09, br3-07, br4-07).
- Inventário de `Albuns/`: 8 arquivos, 172 faixas; proposta de 12 álbuns por cena de uso em `../261029-PROPOSTA-grupos-albuns.md` (i-038).
- Análise `meta/analises/261029-ANALISE-kit-de-musica.md` (i-039), em discussão.
- Nota `261029-1825.txt` lida e fundida: i-040 (curadoria no app) e i-041 (mais de um acervo no navegador).
- WO 0019: 0.9.1 (ajustes de tela vistos pelo dono e o conversor), DEC-026, análise da conversão com desfecho.

### Decisões
DEC-026 (conversor determinístico por família; acervo convertido fora do repo).

### Bugs
Nenhum no app. Erro de conta na análise da conversão: «11 álbuns» eram 10 (o 11º arquivo é o índice) — corrigido no desfecho.

### Aprendizados / armadilhas
- Conversor fiel transforma problema escondido em lista de trabalho: o que estava dentro dos guias (letras cortadas pelo Suno) aparece no painel e no relatório.
- Teste de script que importa o módulo deixa `scripts/__pycache__` na árvore; o teste desliga o bytecode.

### Onde parei
WO 0019 entregue. Esperam o dono: grupos de `Albuns/` (i-038) e as decisões do kit de música (i-039).

### Próximos passos
Com os grupos aprovados, conversores dos formatos de `Albuns/` e o mapa de grupos; com o kit decidido, as três peças.
````

### E16 — arquivo novo — `scripts/convert_br.py`

Arquivo novo: crie com este conteudo.

````
#!/usr/bin/env python3
"""Converte os guias da familia BR para uma colecao no esquema canonico (i-008).

Uso:
    python3 scripts/convert_br.py SAIDA.json GUIA.md [GUIA.md ...] [--title "Nome"]

Familia BR: um arquivo por volume (`..._VOL<n>_GUIA.md`), uma faixa por cabecalho
`## <emoji> BR<n>-NN — GENERO`, titulo em `### "Titulo" — voz`, campos de
referencia em `**Conceito:**`, `**Voz:**`, `**Instrumentos:**`, e tres blocos de
codigo por faixa: `[ESTILO SUNO]`, `[LETRA]` e as variantes
`[ESTILO SUNO — VAR X: rotulo]`. So esta familia: as outras tem outro formato e
pedem outro conversor (analise 261029, decisao 1A).

A regra de dominio guia tudo: o rotulo do bloco (`[ESTILO SUNO]`, `[LETRA]`) e
referencia humana e NUNCA entra em `style` ou `lyrics`; o resto do bloco vai
literal. A conversao e fiel (decisao 4A): letra longa demais ou style com tags
demais nao e cortado aqui — o relatorio conta, e o painel de qualidade do app mostra.

A colecao gerada e produto do dono e NAO e versionada no repo (decisao 2A):
grave a saida fora do repo, por exemplo na pasta-pai.

Saida: codigo 0 se todo cabecalho de faixa virou faixa; 1 se algum ficou para tras.
"""
import argparse
import json
import re
import sys
import unicodedata

# Cabecalho de faixa: "## 🎤 BR3-07 — K-POP GIRL CRUSH". O emoji e um token qualquer.
# BRV-N01 e BR10-15 aparecem nos guias; por isso o [V0-9]* e o N? (sonda de 2026-10-29).
CODE = re.compile(r"^## \S+\s+(BR[V0-9]*-N?\d{2})\s+—\s+(.+?)\s*$")
# Rotulo de variante: "[ESTILO SUNO — VAR A: mais cru]" ou "[ESTILO SUNO — VARIAÇÃO B]".
VAR = re.compile(r"^\[ESTILO SUNO\s*—\s*(VAR(?:IAÇÃO)?\s*[A-Z])\s*:?\s*(.*?)\]\s*$", re.I)
# Volume pelo nome do arquivo: ALBUM_BR_VOL7_GUIA.md -> 7.
VOL = re.compile(r"VOL(\d+)", re.I)
# Mesmo padrao de BPM do app e do validate.py, para o relatorio bater com eles.
BPM = re.compile(r"\b(\d{2,3})\s*-?\s*bpm\b", re.I)
BPM_RANGE = re.compile(r"\d{2,3}\s*[–-]\s*\d{2,3}\s*bpm", re.I)

# Limites do Suno usados so no relatorio (fonte e data em QUALITY_LIMITS, app/index.html).
LYRICS_LIMIT = 5000
TAGS_SOFT_LIMIT = 10


def slug(text):
    """Minusculas, sem acento, hifens no lugar do resto: 'BR3-07' -> 'br3-07'."""
    ascii_ = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", ascii_.lower()).strip("-")


def code_blocks(lines):
    """Lista o conteudo de cada bloco ``` ... ``` (sem as cercas)."""
    out, inside, buf = [], False, []
    for line in lines:
        if line.lstrip().startswith("```"):
            if inside:
                out.append(buf)
                buf = []
            inside = not inside
        elif inside:
            buf.append(line)
    return out


def join_style(lines):
    """Style em uma linha: junta as linhas do bloco, colapsa espacos, tira a virgula final."""
    text = " ".join(x.strip() for x in lines if x.strip())
    return re.sub(r"\s+", " ", text).strip().rstrip(",").strip()


def after_label(body):
    """Linhas do bloco depois da primeira nao vazia (o rotulo), sem brancas nas pontas."""
    first = next(i for i, x in enumerate(body) if x.strip())
    rest = body[first + 1:]
    while rest and not rest[0].strip():
        rest = rest[1:]
    while rest and not rest[-1].strip():
        rest = rest[:-1]
    return rest


def track_segment(lines, start, end):
    """Linhas da faixa: do cabecalho ate o proximo de codigo, um '# ' ou um '## ' sem codigo.

    Os guias intercalam secoes que nao sao faixa ("## Sobre o volume", notas de
    fechamento); sem o corte, o texto delas cairia nas notas da ultima faixa.
    """
    seg = lines[start:end]
    for k, line in enumerate(seg[1:], 1):
        if line.startswith("# ") or (line.startswith("## ") and not CODE.match(line)):
            return seg[:k]
    return seg


def parse_track(seg):
    """Uma faixa do guia -> (dict no esquema, lista de avisos) ou (None, [motivo])."""
    code, genre = CODE.match(seg[0]).groups()
    head = next((re.search(r'"([^"]+)"\s*(?:—\s*(.*))?', x) for x in seg[1:4] if x.startswith("### ")), None)
    title = head.group(1) if head else code
    voice_line = (head.group(2) or "").strip() if head else ""
    conversation = next((re.sub(r"[#*]", "", x).strip() for x in seg[1:5] if x.startswith("#### ")), "")

    def field(key):
        prefix = f"**{key}:**"
        return next((x[len(prefix):].strip() for x in seg if x.startswith(prefix)), "")

    style, lyrics, variants = None, None, []
    for body in code_blocks(seg):
        first = next((x.strip() for x in body if x.strip()), "")
        if first.startswith("[ESTILO SUNO") and not VAR.match(first):
            style = join_style(after_label(body))
        elif first.startswith("[LETRA]"):
            lyrics = "\n".join(x.rstrip() for x in after_label(body))
        elif VAR.match(first):
            # um bloco pode trazer mais de uma variante, cada uma com o seu rotulo
            current = None
            for x in body:
                m = VAR.match(x.strip())
                if m:
                    name = re.sub(r"(?i)VARIAÇÃO", "VAR", m.group(1).upper())
                    label = name + (" — " + m.group(2) if m.group(2) else "")
                    current = {"label": label, "lines": []}
                    variants.append(current)
                elif current is not None:
                    current["lines"].append(x)
    if style is None or lyrics is None:
        return None, [f"{code}: sem {'[ESTILO SUNO]' if style is None else '[LETRA]'} — faixa ignorada"]

    warnings = []
    numbers = sorted({int(n) for n in BPM.findall(style)})
    ranged = BPM_RANGE.search(style)
    if ranged:
        warnings.append(f"{code}: BPM em faixa ({ranged.group(0)}) — campo bpm vazio")
    elif len(numbers) > 1:
        warnings.append(f"{code}: style com {len(numbers)} BPM ({', '.join(map(str, numbers))}) — campo bpm vazio")
    notes = [
        f"Voz: {field('Voz') or voice_line}" if (field("Voz") or voice_line) else "",
        f"Instrumentos: {field('Instrumentos')}" if field("Instrumentos") else "",
        conversation,
        f"Gênero: {genre}",
    ]
    song = {
        "id": slug(code),
        "title": title,
        "language": "pt-BR",
        "state": "ideia",
        "style": style,
        "lyrics": lyrics,
        "bpm": numbers[0] if len(numbers) == 1 and not ranged else None,
        "variants": [{"label": v["label"], "style": join_style(v["lines"])} for v in variants],
        "context": field("Conceito"),
        "notes": "\n".join(x for x in notes if x),
        "tags": [code, genre.lower()],
    }
    return song, warnings


def convert_file(path, vol):
    """Um guia -> (album, avisos, numero de cabecalhos de faixa)."""
    with open(path, encoding="utf-8") as f:
        lines = f.read().replace("\r\n", "\n").split("\n")
    # "# 🎵 ÁLBUM HOBBY — VOLUME BR · PARTE 2 | GUIA COMPLETO PARA SUNO AI" -> sem emoji e sem o "| GUIA ..."
    h1 = next((x for x in lines if x.startswith("# ")), "")
    original = re.sub(r"^#\s*\S+\s*", "", h1).split("|")[0].strip()
    starts = [i for i, x in enumerate(lines) if CODE.match(x)]
    songs, warnings = [], []
    for n, i in enumerate(starts):
        end = starts[n + 1] if n + 1 < len(starts) else len(lines)
        song, warn = parse_track(track_segment(lines, i, end))
        warnings += warn
        if song:
            songs.append(song)
    album = {"id": f"br-vol{vol}", "title": f"Parte {vol}", "description": original, "songs": songs}
    return album, warnings, len(starts)


def report(albums):
    """Linhas de relatorio sobre limites do Suno — conta, nao corta (decisao 4A)."""
    songs = [s for a in albums for s in a["songs"]]
    long_ = [s["id"] for s in songs if len(s["lyrics"]) > LYRICS_LIMIT]
    tags = [s["id"] for s in songs if len([t for t in s["style"].split(",") if t.strip()]) > TAGS_SOFT_LIMIT]
    return [
        f"letras acima de {LYRICS_LIMIT} caracteres (o Suno corta em silencio): {len(long_)} de {len(songs)}",
        f"styles com mais de {TAGS_SOFT_LIMIT} tags (as ultimas perdem efeito): {len(tags)} de {len(songs)}",
    ]


def main(argv=None):
    """Linha de comando: converte os guias dados e grava a colecao."""
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("output", help="arquivo .json de saida (fora do repo)")
    ap.add_argument("guides", nargs="+", help="guias ..._VOL<n>_GUIA.md")
    ap.add_argument("--title", default="Rainha da Preguiça", help="titulo da colecao")
    args = ap.parse_args(argv)

    albums, lost = [], 0
    for path in args.guides:
        m = VOL.search(path.replace("\\", "/").rsplit("/", 1)[-1])
        if not m:
            print(f"ERRO: sem VOL<n> no nome de {path} — pulado")
            lost += 1
            continue
        album, warnings, n = convert_file(path, int(m.group(1)))
        albums.append(album)
        lost += n - len(album["songs"])
        print(f"VOL{m.group(1)}: {n} cabecalhos -> {len(album['songs'])} faixas")
        for w in warnings:
            print(f"   aviso {w}")
    albums.sort(key=lambda a: int(a["id"].rsplit("vol", 1)[1]))
    collection = {
        "schemaVersion": "1.0",
        "title": args.title,
        "description": "Convertido dos guias BR por scripts/convert_br.py (i-008).",
        "targetTool": "suno",
        "albums": albums,
    }
    with open(args.output, "w", encoding="utf-8", newline="\n") as f:
        json.dump(collection, f, ensure_ascii=False, indent=1)
        f.write("\n")
    total = sum(len(a["songs"]) for a in albums)
    print(f"\n{len(albums)} album(ns), {total} faixa(s) -> {args.output}")
    for line in report(albums):
        print(f"   {line}")
    if lost:
        print(f"FALHOU: {lost} cabecalho(s) de faixa nao viraram faixa.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
````

### E17 — arquivo novo — `scripts/test_convert_br.py`

Arquivo novo: crie com este conteudo.

````
#!/usr/bin/env python3
"""Testa scripts/convert_br.py com um guia sintetico (sem letra real no repo).

Uso:
    python3 scripts/test_convert_br.py

So biblioteca padrao. Cada caso cobre uma regra do conversor; os de «nao deve»
testam o falso positivo (CEREBRO, FIX-003): o que NAO pode virar faixa nem vazar.
"""
import json
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.dont_write_bytecode = True  # nao deixa scripts/__pycache__ na arvore do repo
import convert_br  # noqa: E402

FENCE = "```"
GUIDE = f"""# 🎵 ÁLBUM TESTE — VOLUME BR · PARTE 9 | GUIA COMPLETO PARA SUNO AI

> Cole o **[ESTILO SUNO]** no campo Style.

## 🎤 BR9-01 — K-POP TESTE
### "Faixa Um" — voz de teste
#### *Da Conversa: um dia qualquer*

**Conceito:** cena de teste
**Voz:** alto, perto do microfone
**Instrumentos:** baixo, bateria

{FENCE}
[ESTILO SUNO]
k-pop test, punchy bass,
bright synths, 120 BPM,
{FENCE}

{FENCE}
[LETRA]

[Verse 1]
linha um
linha dois

{FENCE}

{FENCE}
[ESTILO SUNO — VAR A: mais cru]
lo-fi test, dusty drums
[ESTILO SUNO — VARIAÇÃO B]
big room test
{FENCE}

## 🎤 BR9-02 — FUNK TESTE
### "Faixa Dois"

{FENCE}
[ESTILO SUNO]
funk test, 100–110 BPM
{FENCE}

{FENCE}
[LETRA]
[Chorus]
refrao
{FENCE}

## Sobre o volume

Texto que nao e faixa e nao deve cair nas notas da BR9-02.
"""

NO_LYRICS = f"""# 🎵 ÁLBUM TESTE — PARTE 3

## 🎤 BR3-01 — SEM LETRA
### "Incompleta"

{FENCE}
[ESTILO SUNO]
so estilo
{FENCE}
"""


class ConvertBR(unittest.TestCase):
    """Casos do conversor BR."""

    def setUp(self):
        self.dir = tempfile.mkdtemp()

    def write(self, name, text, crlf=False):
        path = os.path.join(self.dir, name)
        with open(path, "w", encoding="utf-8", newline="\r\n" if crlf else "\n") as f:
            f.write(text)
        return path

    def run_main(self, *guides):
        out = os.path.join(self.dir, "out.json")
        code = convert_br.main([out, *guides])
        with open(out, encoding="utf-8") as f:
            return code, json.load(f)

    def test_track_fields(self):
        code, coll = self.run_main(self.write("ALBUM_BR_VOL9_GUIA.md", GUIDE))
        self.assertEqual(code, 0)
        album = coll["albums"][0]
        self.assertEqual((album["id"], album["title"]), ("br-vol9", "Parte 9"))
        self.assertEqual(album["description"], "ÁLBUM TESTE — VOLUME BR · PARTE 9")
        one = album["songs"][0]
        self.assertEqual(one["id"], "br9-01")
        self.assertEqual(one["title"], "Faixa Um")
        self.assertEqual(one["style"], "k-pop test, punchy bass, bright synths, 120 BPM")
        self.assertEqual(one["lyrics"], "[Verse 1]\nlinha um\nlinha dois")
        self.assertEqual(one["bpm"], 120)
        self.assertEqual(one["context"], "cena de teste")
        self.assertIn("Voz: alto, perto do microfone", one["notes"])
        self.assertIn("Da Conversa: um dia qualquer", one["notes"])
        self.assertEqual(one["tags"], ["BR9-01", "k-pop teste"])

    def test_label_never_inside_copyable(self):
        """Regra de dominio: o rotulo do bloco nao entra em style nem lyrics."""
        _, coll = self.run_main(self.write("ALBUM_BR_VOL9_GUIA.md", GUIDE))
        for s in coll["albums"][0]["songs"]:
            for text in [s["style"], s["lyrics"]] + [v["style"] for v in s["variants"]]:
                self.assertNotIn("ESTILO SUNO", text)
                self.assertNotIn("[LETRA]", text)

    def test_variants(self):
        _, coll = self.run_main(self.write("ALBUM_BR_VOL9_GUIA.md", GUIDE))
        variants = coll["albums"][0]["songs"][0]["variants"]
        self.assertEqual(variants, [
            {"label": "VAR A — mais cru", "style": "lo-fi test, dusty drums"},
            {"label": "VAR B", "style": "big room test"},
        ])

    def test_bpm_range_leaves_field_empty(self):
        _, coll = self.run_main(self.write("ALBUM_BR_VOL9_GUIA.md", GUIDE))
        self.assertIsNone(coll["albums"][0]["songs"][1]["bpm"])

    def test_section_without_code_does_not_leak(self):
        """Nao deve: a secao «## Sobre o volume» nao vira faixa nem nota."""
        _, coll = self.run_main(self.write("ALBUM_BR_VOL9_GUIA.md", GUIDE))
        songs = coll["albums"][0]["songs"]
        self.assertEqual(len(songs), 2)
        self.assertNotIn("nao e faixa", songs[1]["notes"] + songs[1]["lyrics"])

    def test_crlf_input(self):
        """Arquivo salvo no Windows (CRLF) da o mesmo resultado."""
        _, lf = self.run_main(self.write("ALBUM_BR_VOL9_GUIA.md", GUIDE))
        _, crlf = self.run_main(self.write("ALBUM_BR_VOL9_GUIA.md", GUIDE, crlf=True))
        self.assertEqual(lf, crlf)

    def test_missing_block_fails(self):
        """Faixa sem [LETRA] fica de fora e o comando sai com 1."""
        code, coll = self.run_main(self.write("ALBUM_BR_VOL3_GUIA.md", NO_LYRICS))
        self.assertEqual(code, 1)
        self.assertEqual(coll["albums"][0]["songs"], [])

    def test_albums_ordered_by_volume(self):
        """VOL10 vem depois de VOL9, nao antes (ordem numerica, nao alfabetica)."""
        g9 = self.write("ALBUM_BR_VOL9_GUIA.md", GUIDE)
        g10 = self.write("ALBUM_BR_VOL10_GUIA.md", GUIDE.replace("BR9-", "BR10-"))
        _, coll = self.run_main(g10, g9)
        self.assertEqual([a["id"] for a in coll["albums"]], ["br-vol9", "br-vol10"])


if __name__ == "__main__":
    unittest.main()
````

### E18 — arquivo novo — `meta/analises/261029-ANALISE-kit-de-musica.md`

Arquivo novo: crie com este conteudo.

````
# ANALISE — Kit de música para os projetos do KCM (i-022, i-023, i-024)

> **Status:** Em discussão — espera as decisões 1 a 3 do dono (fim deste arquivo).
> **Data:** 2026-10-29 (data de criação; não muda depois)
> **Ideias de origem:** i-022 (skill que ensina o JSON), i-023 (skill com os macetes do Suno), i-024 (molde de
> skill de estilo próprio) e o feedback ao kit de 2026-10-28 («o nicho de música do KCM ainda não carrega o que
> este projeto aprendeu»). Pedido do dono em 2026-10-29: criar projetos de música para o Suno já «profissionais»
> e adaptados ao Cancioneiro.

## Problema

Os projetos de música que o dono monta com o KCM nascem sem o que este projeto aprendeu sobre o Suno. O custo
está medido no acervo dele: os guias antigos foram escritos por chats sem essas regras, e mesmo a família mais
regular, a «Rainha da Preguiça», chega ao Suno assim:

- **72 de 151 letras passam de 5.000 caracteres**, onde o Suno corta em silêncio; 141 passam de 3.000, onde ele
  começa a correr `[medido por instrumento: scripts/convert_br.py, 2026-10-29]`;
- **138 de 151 styles passam de 10 tags**, onde as últimas perdem efeito (mesma medida);
- **todos os oito formatos** de `Albuns/` e os dez volumes BR põem o rótulo dentro do bloco copiável ou fora de
  qualquer padrão (sonda `../261029-SONDA-albuns-antigos.md`).

Do outro lado, o que o projeto ensina funciona quando é dito: com o contrato do prompt-modelo, dois chats
entregaram 6 de 6 faixas no formato e no orçamento; sem ele, três chats inventaram três formatos de módulo
(spec `meta/specs/261028-prompt-modelo-e-modulos.md`, reteste de 2026-10-29). Conhecimento que não chega ao chat
que escreve a música não vale nada na hora de escrever.

## Restrições / o que foi medido

**O que este projeto sabe e um projeto de música precisaria saber** (cada item com a fonte que o sustenta):

| # | ensinamento | fonte |
|---|---|---|
| 1 | Dois campos: Style (mundo sonoro, sem colchetes) e Lyrics (estrutura e voz, com colchetes) | HISTORY §1 |
| 2 | Rótulo de referência nunca dentro do que vai para o Suno | DEC-005, regra de domínio |
| 3 | Style em cinco camadas audíveis, o mais característico nas primeiras ~20 a 30 palavras | HISTORY §4, §10; prompt-modelo |
| 4 | Orçamento: 6 a 8 tags no style, até 10 com módulos; acima disso as últimas perdem efeito | HISTORY §10, DEC-018 |
| 5 | Letra até ~3.000 caracteres; acima de 5.000 o Suno corta sem avisar | HISTORY §9, `QUALITY_LIMITS` |
| 6 | BPM é aproximação; um número por faixa (rampa «95 to 118 BPM» confunde o controle do app) | DEC-020 |
| 7 | Instrumental: `[Instrumental]` sozinho em loop; tags de arco só em faixa linear | HISTORY §2, §3 |
| 8 | Remover algo vai no Exclude, não em «no X»; o v6-mini gratuito não tem Exclude | HISTORY §5, §11 |
| 9 | A saída é o JSON canônico, em arquivo; módulos na coleção, faixa cita ids | DEC-016, DEC-021, DEC-023 |
| 10 | Um projeto por cena de uso: álbum coerente rende faixas parecidas; arquivo-mistura vira bagunça | proposta de grupos de 2026-10-29 |
| 11 | A interface do Suno muda: limites com fonte e data, e reconferir na conta | HISTORY §12 |

**O que existe pronto:** o prompt-modelo (`schema/PROMPT-PARA-CHATS.md`) já é o item 9 e boa parte do 3 e do 4,
testado; o HISTORY tem o resto, mas é longo e escrito para quem mantém o Cancioneiro, não para quem compõe.

**O que não sei:** o formato do nicho de música do KCM hoje — o que ele gera (Instruções? skills? arquivos de
contexto?) e onde. A pasta do KCM (`C:\Users\alexk\Arquiteturas\Contexto\contexto-modular`) não está ligada a
esta conversa `[não lido]`.

## Opções consideradas

**Decisão 1 — O que entregar.**
- **A (recomendada): um pacote de três peças**, cada uma com um papel:
  1. **Instruções-modelo de projeto de música** — o que um projeto do claude.ai carrega sempre: a regra de
     domínio, o orçamento (4, 5), o contrato de saída (9) e a cena do álbum (10), em uma página.
  2. **Skill «macetes do Suno»** (i-023) — os itens 1 a 8 e 11 em forma de consulta, com exemplos bons e ruins,
     lida quando o chat vai escrever ou revisar uma faixa. É o HISTORY reescrito para quem compõe.
  3. **Skill «revisar faixa»** — checklist que o chat roda antes de entregar: conta caracteres da letra e tags
     do style, procura rótulo no copiável, «no X», dois BPM. É o painel de qualidade do app, antes do app.
  O contrato JSON (i-022) não vira peça nova: as Instruções apontam para o prompt-modelo, que já é a fonte.
- B: só uma carta ao KCM com o resumo, e o KCM constrói. Barato, mas o conhecimento passa a viver em dois lugares
  e o KCM não tem as medidas para conferir.
- C: uma skill só, juntando tudo. Mais simples de instalar; mistura o que se lê sempre (orçamento, saída) com o
  que se consulta (macetes), e paga em contexto a cada conversa.
- **Fora agora:** i-024 (molde de skill por estilo próprio) — depende das três peças estarem em uso; reabre
  quando um projeto de álbum tiver estilo firmado.

**Decisão 2 — Onde mora a fonte.**
- **A (recomendada): neste repo**, numa pasta `kit-musica/`, e o KCM copia de lá. Aqui estão as medidas, o
  validador e o app que confere o resultado; uma regra que muda aqui (limite do Suno, contrato) muda no kit na
  mesma WO.
- B: no KCM. Fica junto dos outros nichos, mas cada mudança de regra do Suno precisa de duas WOs em dois repos.

**Decisão 3 — Como chego ao formato do KCM.**
- **A (recomendada): o dono libera a pasta do KCM nesta conversa** (um pedido de acesso, só leitura do nicho de
  música) e o chat adapta as três peças ao molde dele.
- B: o dono traz para a pasta-pai só o molde do nicho de música.
- C: o chat escreve no formato do Cancioneiro e o KCM adapta.

## Recomendação

**1A, 2A, 3A.** O que decide é a medida do problema: 72 letras cortadas e 138 styles diluídos vieram de chats
que não sabiam as regras, e as regras já estão escritas aqui. Três peças pequenas, cada uma lida no momento em que
serve, custam menos contexto que uma grande e chegam a quem escreve a música.

## Riscos

- **Peça que repete o HISTORY e envelhece separada.** Sinal: um limite muda no `QUALITY_LIMITS` e não muda no
  kit. Mitigação: o `validate.py` conferir os números do kit contra o app, como já confere a versão.
- **Skill grande demais para ser lida.** Sinal: passar de ~2 páginas. Mitigação: exemplo curto por regra, e o
  resto fica no HISTORY.
- **O formato do KCM mudar** depois de adaptado. Sinal: o KCM subir de versão no nicho de música.

## Ponto de decisão

Decisões **1, 2 e 3** (recomendadas **A, A, A**). Com elas: o chat escreve as três peças numa WO, testa a skill
«revisar faixa» contra o acervo da Rainha da Preguiça (deve achar as 72 e as 138) e um projeto-piloto de álbum
(um dos grupos da proposta de `Albuns/`) mede se as faixas novas já saem dentro do orçamento.
````

### E19 — STATUS inteiro — `meta/STATUS.md`

Sem ancora: substitua o arquivo inteiro.

````
# STATUS.md — Cancioneiro

> **O agora.** O que funciona, o que está em progresso, o que está quebrado, backlog curto.
> Rolante: item resolvido sai daqui e vai para o CHANGELOG. Médio/longo prazo vive no ROADMAP.

**Versão atual:** 0.9.1 · **Fase:** 3a, 3a.2, o BPM da 3b, o prompt-modelo e as conveniências de uso concluídos e conferidos · i-008 em andamento: família BR convertida (fora do repo), `Albuns/` à espera dos grupos
---

## Última conversa (2026-10-29, conversão da família BR, WO 0019)

- **Decisões da conversão: 1A, 2A, 3A, 4A** (DEC-026) — conversor determinístico por família; o acervo convertido é produto do dono e fica fora do repo.
- **Família BR convertida:** `scripts/convert_br.py` nos dez volumes, 151 de 151 faixas, gravada em `../acervos/rainha-da-preguica.json` e importada no app sem erro. O relatório mede 72 letras acima de 5.000 caracteres e 138 styles acima de 10 tags `[medido por instrumento]` — trabalho para o projeto de refino da Rainha da Preguiça, que o dono vai abrir à parte.
- **0.9.1:** os ajustes de tela da DEC-025 (vistos pelo dono) e o conversor.
- **Abertas:** grupos de `Albuns/` (i-038, proposta na pasta-pai) e o kit de música para o KCM (i-039, análise em discussão). A nota `261029-1825.txt` virou i-040 e i-041.
- **Este bloco substitui o anterior, de 2026-10-29, que fechava a 0.9.0.** O que ele dizia está no CHANGELOG [0.9.0] e [0.9.1], na DEC-025 e em `logs/2026-10-29.md` (Conversas 5 e 6).

## Funciona (pronto)

- **Ferramenta `app/index.html`:** importa/carrega JSON, cartões por álbum, copiar Style/Lyrics/Exclude por botão (o botão entrega o texto que está na tela — FIX-007), marca «usei», filtros por álbum/estado/uso, busca, módulos de estilo que recompõem o Style ao vivo, variantes e notas recolhíveis, «Baixar .json» limpo e «Importar .json» que saneia chaves internas e diz quantas removeu (FIX-004/006). A versão aparece no cabeçalho. A importação avisa quantos módulos citados não existem na coleção (FIX-009).
- **Painel de qualidade (0.5.0, DEC-018):** linha abaixo de Style, Lyrics e Exclude com caracteres contra o limite do campo, tags do Style e negações «no X». Vermelho só para truncamento.
- **Custo de cada módulo no chip (0.6.0, DEC-019):** com o painel de módulos aberto, cada chip mostra `−N`, `+N` ou `0` tags; a linha de qualidade diz quanto o style base usa sozinho quando o recomposto passa de 10.
- **Controle de BPM no cartão (0.7.0, DEC-020):** campo 20-300 com `−5`/`+5` e «voltar a N» governa todo «NN bpm» do Style principal; o chip de andamento é atalho (no máximo um ligado); variantes e «Baixar .json» não mudam; o valor é só da sessão.
- **Esquema JSON canônico** (`schema/`). Biblioteca de referência para autoria em `schema/style-modules.json` (27 módulos, sete camadas); cada acervo traz os seus (DEC-016).
- **Datasets:** `data/exemplo-cinzeiro.json` (1 faixa, com os 5 módulos que cita) e `data/demo.json` (2 álbuns, 3 faixas). Os acervos do dono moram fora do repo (DEC-026): `../album-referencias (1).json` (7 faixas, 50 módulos) e `../acervos/rainha-da-preguica.json` (10 álbuns, 151 faixas, gerado pelo conversor).
- **Conversor da família BR** (`scripts/convert_br.py`, 0.9.1, DEC-026): guias `..._VOL<n>_GUIA.md` → coleção no esquema, um álbum por volume, rótulos fora do copiável, variantes e referência levadas; relata o que passa do limite do Suno sem cortar. Teste: `python3 scripts/test_convert_br.py`.
- **Validação** (`scripts/validate.py`): sintaxe, esquema (com `jsonschema`), integridade referencial dos módulos (id ausente ou objeto no lugar do id, sem traceback — FIX-009), versão igual nos quatro lugares, um BPM só por faixa (DEC-020) e as marcações do prompt que o app lê (DEC-021); código 1 se falhar; a última linha diz se o esquema foi de fato conferido.
- **Export MD** (faixa / álbum / acervo), com o rótulo fora do bloco e o Style da tela nos três (0.9.0, D5).
- **Prompt-modelo** (`schema/PROMPT-PARA-CHATS.md`, DEC-021, DEC-023): contrato de módulo, style com 6 a 8 tags e até 10 com os módulos ligados; pede o JSON como arquivo e, sem arquivo, em bloco de código. Dois retestes em 2026-10-29: 6 de 6 faixas dentro do contrato e do orçamento, nos dois.
- **Botões «Prompt» e «Exemplo»** (0.8.0, DEC-021): buscam o prompt e o `data/demo.json` do repositório no clique; a janela do prompt recebe o «Meu pedido».
- **Conveniências (0.9.0, DEC-022, DEC-023):** «Estrutura» do cartão (ordem e blocos visíveis, no navegador); copiar o título; arrastar o `.json` para importar; o último acervo importado volta ao abrir, com origem, data e «esquecer»; a importação aceita a resposta do chat colada inteira e avisa.
- **Publicado no GitHub Pages** em `https://joaolucas-nds.github.io/cancioneiro/app/index.html` — o push em `main` publica.

## Em progresso

- **Álbuns antigos (i-008, DEC-026).** Família BR feita. `Albuns/` (8 arquivos, 172 faixas): proposta de 12 álbuns por cena de uso em `../261029-PROPOSTA-grupos-albuns.md` (i-038); com os grupos aprovados, conversores dos formatos e um mapa faixa → álbum.
- **Kit de música para o KCM (i-039)** — `meta/analises/261029-ANALISE-kit-de-musica.md`, em discussão: três peças (Instruções-modelo, skill de macetes, skill de revisão de faixa), fonte neste repo, adaptadas ao molde do nicho de música do KCM.

## Quebrado / pendências que travam

- (nada quebrado)

## Pendências do dono

- **Aprovar ou ajustar os grupos de `Albuns/`** — `../261029-PROPOSTA-grupos-albuns.md`, três pontos no fim.
- **Decidir o kit de música** — decisões 1 a 3 da análise; a 3 pede acesso de leitura à pasta do KCM (`C:\Users\alexk\Arquiteturas\Contexto\contexto-modular`) ou o molde do nicho trazido para a pasta-pai.
- **Instalar o validador de esquema nesta máquina.** Sem `jsonschema` e `referencing`, o `validate.py` só confere sintaxe e diz `ESQUEMA NAO CONFERIDO` na última linha. Uma vez, no CMD: `pip install jsonschema referencing --break-system-packages`. Depois, `python3 scripts/validate.py` deve terminar em `Tudo conforme ao esquema.`

## Backlog curto (próximas ações concretas)

1. **Converter `Albuns/`** (i-008, i-038) — depois dos grupos aprovados.
2. **Kit de música** (i-039) — depois das decisões; testar a skill de revisão contra a Rainha da Preguiça (deve achar as 72 e as 138).
3. **Curadoria no app e mais de um acervo** (i-040, i-041) — análise antes de spec: o app passaria de leitor a editor leve.
4. **Rampa de BPM** (i-042) — três faixas BR reprovam no `validate.py` por mudarem de andamento de propósito.
5. **Pesquisar outras plataformas de música por IA** (i-032) — um turno de pesquisa antes de qualquer mudança de esquema.
6. **Avisar palavra de andamento que contradiz o BPM** (i-029) — pede uma tabela palavra → faixa de BPM, com fonte e data.
7. **Importar prompts prontos dos álbuns como módulos** — o último ⬜ da 3b no ROADMAP; o índice-mestre da BR traz fórmulas de estilo.

## Notas de estado

- **Repo local do dono:** `C:\Users\alexk\Tools\cancioneiro\cancioneiro` (Windows). O chat lê e grava na pasta vinculada; commit e push são do Code (DEC-010). A pasta-pai guarda relatórios, notas e o acervo do dono, fora do Git; o lido vai para `../notas-arquivadas/`.
- **Canal:** pasta vinculada é o padrão; a cópia achatada (FlatDrop) é reserva (DEC-017).
- **Limites do Suno:** o v6 saiu em 2026-09-09 e a nota oficial não documenta limite de campo; os números do painel vêm de fonte secundária, com fonte e data no `QUALITY_LIMITS` (DEC-018). Outra fonte secundária (2026-08) põe o ideal em 4 a 7 descritores; o prompt usa 6 a 8. Reconferir quando houver documentação oficial. O `meta/HISTORY.md` §5 ganhou a interface do v6 vista na conta (2026-10-29); o resto do arquivo ainda descreve o v5.5.
- **Exclude no v6-mini:** o formulário gratuito não tem o campo (capturas de 2026-10-29). Desde a 0.9.1 (DEC-025) o bloco vem oculto por padrão, com o aviso «no X → Exclude» junto (D3); o dado continua no JSON e no export. Quem usa o campo liga em «Estrutura».
- **Navegador (DEC-004, DEC-022):** guarda as marcas «usei», a estrutura do cartão e a cópia do último acervo importado. A cópia é cache: se o arquivo mudou fora, importe de novo; a linha de origem diz quando a cópia foi feita.
- **Botões «Prompt» e «Exemplo»:** dependem de rede e do Pages. No `file://`, só funcionam se o Pages aceitar o `fetch` de uma página local — não conferido (o dono abriu o `file://` em 2026-10-29, sem relatar o resultado do botão); sem isso, a janela mostra o link para a versão publicada (DEC-021).
- **Estado de sessão** (módulos ligados e BPM escolhido) sobrevive a filtro, busca e «marcar usei»; volta ao acervo ao recarregar a página ou importar de novo (FIX-008, DEC-020).
- **Limite conhecido:** `tryAutoLoad` (carregamento automático pelo Pages) não saneia chaves internas — só a importação por arquivo faz isso. Inócuo enquanto nenhum acervo contaminado for para `data/`.
- **Pendência de contexto — ASU:** o dono perguntou se o «modo ASU» do KCM seria melhor que o modo Code para este projeto; ficou pendente até ele trazer a descrição do ASU `[relatado pelo dono, sem material de apoio]`.
- Design: na recomposição do Style a base manda — desligar um módulo não remove o que já está no style base; módulos só somam. O dedup compara sequências de palavras (FIX-003). Os módulos de gênero e de andamento costumam custar 0 tag por isso (DEC-019). O chip de andamento é atalho do controle de BPM, no máximo um ligado (DEC-020).
````

## Fora de escopo

- **O acervo convertido** (`../acervos/`) — fora do repo por decisao (DEC-026). Nao copie para `data/`.
- **`Albuns/`** — espera os grupos do dono (i-038).
- **App alem da versao** — nada muda no comportamento; i-040, i-041 e i-042 sao ideias.

## Armadilhas desta WO

- **Aplique uma vez, edicao por edicao.** Na WO 0018, um script com `|| fallback` reexecutou tudo e duplicou
  edicoes cujo texto novo contem a ancora. Se algo falhar a meio, PARE: a idempotencia pelo texto novo inteiro
  deixa retomar do ponto, sem reexecutar o que passou.
- **Tres arquivos novos e o STATUS vem como arquivo inteiro**, sob o mesmo titulo `### Exx` das outras edicoes.
  Os blocos de `scripts/` trazem cercas de tres crases dentro (o teste monta um guia com elas): delimite pelas
  **quatro**.
- **`autocrlf=true` nesta maquina:** crie os arquivos novos em LF (o hash de chegada e de LF). Se um hash divergir,
  rode `file <arquivo>` antes de concluir que uma edicao errou; volte com `sed -i 's/\r$//'`.
- **`__pycache__`:** o teste desliga o bytecode; se aparecer `scripts/__pycache__/` mesmo assim, apague e nao
  versione.
- **Nenhuma checagem abaixo usa emoji nem conta caracteres.**

## Depois de aplicar — conferencia antes do commit

| # | Checagem | Comando | Esperado |
|---|---|---|---|
| 1 | **Os treze arquivos sao os testados** | `sha1sum app/index.html meta/CHANGELOG.md README.md meta/CONTEXT.md meta/analises/261029-ANALISE-conversao-dos-albuns.md meta/IDEAS.md meta/ROADMAP.md meta/DECISIONS.md logs/2026-10-29.md scripts/convert_br.py scripts/test_convert_br.py meta/analises/261029-ANALISE-kit-de-musica.md meta/STATUS.md` | a coluna **chegada** do cabecalho, os treze. **Prova as 19 edicoes.** |
| 2 | O teste do conversor passa | `python3 scripts/test_convert_br.py 2>&1 \| tail -3` | `Ran 8 tests` e `OK` |
| 3 | O conversor no acervo real reproduz o do chat | `python3 scripts/convert_br.py ../acervos/teste-wo0019.json "../Album Rainha da Preguiça/"ALBUM_BR_VOL*_GUIA.md; echo "exit=$?"` e depois `sha1sum ../acervos/teste-wo0019.json ../acervos/rainha-da-preguica.json` | `10 album(ns), 151 faixa(s)`, `exit=0`, e os **dois hashes iguais** (`4d1a69ef9ed23f56d7810888092f7decf943d8c2`). Depois: `rm ../acervos/teste-wo0019.json` |
| 4 | A versao | `grep -c 'data-role="app-version">v0.9.1<' app/index.html`, `grep -m1 '^## \[' meta/CHANGELOG.md`, `grep -c '^## \[Unreleased\]' meta/CHANGELOG.md` | `1`, `## [0.9.1] — 2026-10-29`, `0` |
| 5 | Os registros | `grep -c '^## DEC-026 ' meta/DECISIONS.md`, `grep -c '^## Conversa 7' logs/2026-10-29.md`, `grep -c 'Status:\*\* Implementada (0.9.1)' meta/analises/261029-ANALISE-conversao-dos-albuns.md`, `grep -cE '^### i-0(38\|39\|40\|41\|42) ' meta/IDEAS.md` | `1`, `1`, `1`, `5` |
| 6 | Validacao passa, com a versao nova | `python3 scripts/validate.py; echo "exit=$?"` | `exit=0`, com `OK  versao 0.9.1 igual em CHANGELOG, app, README e STATUS` |
| 7 | Nenhuma letra entra no repo | `GIT_OPTIONAL_LOCKS=0 git status --short --untracked-files=all \| grep -cE '\.json\|pycache\|\.txt'` | `0` |
| 8 | Nada de dados | `GIT_OPTIONAL_LOCKS=0 git status --short data` | saida **vazia** |

**Os tres campos de cada passo:** as oito sao rodadas por **quem aplica (o Code)**, na raiz do repo
(`C:\Users\alexk\Tools\cancioneiro\cancioneiro`), em Git Bash, com `LC_ALL=C.UTF-8`. **Chega no ramo?**
A checagem 1 cobre os treze arquivos inteiros; a 3 roda o conversor de chegada nos guias reais. **Esta e qual
pergunta?** A 2 e a 3 respondem «funciona?»; as outras, «esta la?». A tela (versao 0.9.1 no Pages) e do dono.

## Relatorio de aplicacao

Grave em `../261029-HHMM-code-cancioneiro-apply-wo0019.txt`, com o `HHMM` de `date +%y%m%d-%H%M` rodado na
hora. Diga o resultado da checagem 1 em primeiro lugar, e o da 3 em segundo.

**Proximo comando** (ultima linha do relatorio, cru e sozinho):

```
/wrap
```

## Commit

```
git add app/index.html meta/CHANGELOG.md README.md meta/CONTEXT.md meta/analises meta/IDEAS.md meta/ROADMAP.md meta/DECISIONS.md logs/2026-10-29.md scripts/convert_br.py scripts/test_convert_br.py meta/STATUS.md meta/workorders
```

```
git commit -m "feat: conversor dos guias BR e versao 0.9.1" -m "scripts/convert_br.py converte os guias da familia BR para o esquema, com rotulos fora do copiavel e relatorio de limites do Suno, e teste com guia sintetico (DEC-026). 151 de 151 faixas no acervo do dono, que fica fora do repo. 0.9.1 fecha os ajustes de tela da DEC-025. Registra as analises da conversao (implementada) e do kit de musica (em discussao) e as ideias i-038 a i-042."
```

```
git push
```
