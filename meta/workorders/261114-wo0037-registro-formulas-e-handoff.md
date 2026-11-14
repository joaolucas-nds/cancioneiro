# WO 0037 — Registro: rampa conferida, fórmulas decididas (DEC-037), transferência de conversa

## Cabecalho

> **Tipo:** só registro — `meta/STATUS.md` (4 edicoes), `meta/ROADMAP.md`, `meta/IDEAS.md`, `meta/GLOSSARY.md` e `meta/DECISIONS.md` (1 cada), mais o versionamento de dois arquivos que o chat gravou. O app nao muda; a versao continua 0.19.0.
> **Config sugerida:** Sonnet · `/effort low`.
> **Pre-requisito:** commit `6c7a9d0`, branch `main`, sincronizada com `origin/main`. O `git status --short` mostra exatamente: ` M meta/specs/261111-formulas.md`, `?? logs/2026-11-14.md` e `?? meta/workorders/261114-wo0037-registro-formulas-e-handoff.md`.
> **Base:** «rampa ok» `[relatado pelo dono, 2026-11-11 16:20]`; «prompts prontos: D» `[relatado pelo dono, 2026-11-11 17:12]`; «pontos das formulas: os quatro como recomendados» `[relatado pelo dono, 2026-11-14 09:21]`; CI verde no `790aa3a` pelo relatorio `261111-1555` do Code.
> **Depende de:** `6c7a9d0` (spec das formulas).
>
> | arquivo | partida (sha1) | chegada (sha1) |
> |---|---|---|
> | `meta/DECISIONS.md` | `79fee7c60ff23f0d0366f9423d45e42ebcb6b644` | `0071d463b41f0a3d1054d1875ef39b87256427df` |
> | `meta/GLOSSARY.md` | `12934d47edff362d31ec265428bbbafe180a7197` | `551a43e7bf293e05c7bc3fce734e565bdfb3495e` |
> | `meta/IDEAS.md` | `c96eca6d41cdeb4f75b4ef33850159406890472d` | `a53fcd38d64e0e2e2cc7d45e85ed53b508557938` |
> | `meta/ROADMAP.md` | `86dcfe01d121ac85e3c51a17e4d7bf4f5342ee9f` | `73aa2d231dee311434418d65e04b6d9cb9f32574` |
> | `meta/STATUS.md` | `f5758d38260a1cfc9e57fb9b4e92a03002fcc30a` | `eaa45e8bad59ad2b7025249c7e99c0631f44ea03` |
> | `meta/specs/261111-formulas.md` | `9cfbd073363c33955c113190622bcd1a37b1a621` | o mesmo (gravado pelo chat; so versionar) |
> | `logs/2026-11-14.md` | `bbd97c0394332ddada480ebc782caa79c373be19` | o mesmo (gravado pelo chat; so versionar) |
>
> **Ancora semantica:** se um trecho-ancora nao bater EXATAMENTE, PARE e reporte.
> **Idempotencia:** antes de cada edicao, procure o texto NOVO INTEIRO; se ja estiver la, PULE e diga no relatorio. Na edicao de texto novo vazio, se a ancora ja nao estiver la, PULE.
> **Ancoras:** linhas inteiras (uma linha ou um bloco de linhas inteiras), cada uma 1 vez no arquivo, na ordem abaixo. Toda edicao «substitui a ancora inteira»; texto novo vazio = apagar a ancora.
> **Âncoras lidas em** (lidas pelo chat NESTE turno, do disco do dono em `6c7a9d0`; aplicadas em ordem numa copia, com a chegada medida):
> - E01 (`meta/STATUS.md`, cabeçalho: rampa conferida, fórmulas em spec): linha `**Versão atual:** 0.19.0 · **Fase:** 3a, 3a.2, o BPM da 3b, o prompt-modelo e as conveni…`
> - E02 (`meta/STATUS.md`, última conversa): bloco de 8 linhas, começando por `## Última conversa (2026-11-11, 0.18 conferida, CI e rampa de BPM, WO 0036)`
> - E03 (`meta/STATUS.md`, pendências: sai conferir a rampa): linha `- **Conferir a rampa de BPM na tela** — roteiro na conversa de 2026-11-11 (WO 0036), dep…`
> - E04 (`meta/STATUS.md`, backlog: as fórmulas): linha `1. **Importar prompts prontos dos álbuns como módulos** — o último ⬜ da 3b no ROADMAP; o…`
> - E05 (`meta/ROADMAP.md`, o ⬜ da 3b com o texto novo): linha `- ⬜ Importar prompts prontos dos álbuns como módulos.`
> - E06 (`meta/IDEAS.md`, i-052, a paleta de módulos): linha `**Entregue (2026-11-09, DEC-034):** tests/ com 32 testes (básico, organizar, salvar no a…`
> - E07 (`meta/GLOSSARY.md`, prompt pronto vira fórmula): linha `**Style de referência / prompt pronto** — um texto de style completo já validado (como o…`
> - E08 (`meta/DECISIONS.md`, DEC-037): linha `**Consequências:** (+) O que se copia é o que está escrito, também na rampa — a promessa…`
> **Canal dos meta neste ciclo = CODE:** STATUS, DECISIONS, ROADMAP, IDEAS e GLOSSARY pelo Code, com o texto abaixo (DEC-010; o GLOSSARY e do chat, e vai aqui para nao ter dois escritores no mesmo commit); a spec e o log de 2026-11-14 ja estao gravados pelo chat.

---

## 1. Por que

A conversa do chat foi encerrada (pesada) e a proxima arranca do repo. Tres fatos relatados pelo dono so estavam no chat: a 0.19.0 conferida na tela, a escolha da opcao D para os prompts prontos e os quatro pontos da spec das formulas. Esta WO os registra, cria a DEC-037 e a i-052 (paleta de modulos), muda o texto do ultimo item da 3b e tira do STATUS a pendencia de conferir a rampa. A implementacao da 0.20.0 nao comecou.

## Edicao 0 — Conferencia de hash e de arvore

```
sha1sum meta/DECISIONS.md meta/GLOSSARY.md meta/IDEAS.md meta/ROADMAP.md meta/STATUS.md meta/specs/261111-formulas.md logs/2026-11-14.md
GIT_OPTIONAL_LOCKS=0 git status --short
```

Todos batem com **partida**; o `git status` mostra exatamente as tres linhas do Pre-requisito. Qualquer outra coisa: **PARE e reporte**.

## Edicoes E01 a E08

Na ordem. Copie o que esta ENTRE as linhas de quatro crases, sem elas. Aplique por script, extraindo os blocos da WO; grave em UTF-8 com LF.

### E01 — cabeçalho: rampa conferida, fórmulas em spec

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
**Versão atual:** 0.19.0 · **Fase:** 3a, 3a.2, o BPM da 3b, o prompt-modelo e as conveniências de uso concluídos e conferidos · os álbuns antigos convertidos (i-008, fora do repo) · curadoria no app concluída nas três entregas (DEC-028, DEC-029) · frente de interface concluída e conferida nas quatro entregas (DEC-030 a DEC-033) · organizar os álbuns (0.18.0, DEC-035) conferido · rampa de BPM (0.19.0, DEC-036) à espera da conferência na tela · kit de música lido pelo KCM, à espera da resposta (i-039)
````

**Texto novo (substitui a ancora inteira):**

````
**Versão atual:** 0.19.0 · **Fase:** 3a, 3a.2, o BPM da 3b, o prompt-modelo e as conveniências de uso concluídos e conferidos · os álbuns antigos convertidos (i-008, fora do repo) · curadoria no app concluída nas três entregas (DEC-028, DEC-029) · frente de interface concluída e conferida nas quatro entregas (DEC-030 a DEC-033) · organizar os álbuns (0.18.0, DEC-035) conferido · rampa de BPM (0.19.0, DEC-036) conferida · fórmulas de referência (0.20.0, DEC-037) com spec pronta, a implementar · kit de música lido pelo KCM, à espera da resposta (i-039)
````

### E02 — última conversa

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
## Última conversa (2026-11-11, 0.18 conferida, CI e rampa de BPM, WO 0036)

- **0.18.0 conferida na tela pelo dono** em 2026-11-11 (os 8 itens do roteiro OK `[relatado pelo dono]`): organizar os álbuns está fechado.
- **WO 0035 recusada** na Edição 0 (o HEAD andou para `0d639f7` depois da leitura do chat); o conteúdo dela foi para a WO 0036.
- **CI:** o passo «Dependencias» deixa de depender do `apt` do runner (o navegador sozinho; as bibliotecas do sistema com três tentativas de 3 minutos, sem derrubar o job). Os testes não rodavam no CI desde a 0.18.0; o push da WO 0036 (`790aa3a`) fechou verde.
- **Rampa de BPM (0.19.0, DEC-036):** o app copiava «95 BPM building to 115 BPM» como «95 BPM building to 95 bpm», desde a 0.7.0; agora a rampa sai como foi escrita, com rótulo no lugar do controle, aviso âmbar e AVISO no `validate.py`. Os quatro pontos decididos pelo dono como recomendados; 7 de 7 critérios e 6 testes novos (`tests/test_bpm.py`), testados pelo chat. Falta a conferência na tela pelo dono.
- **Este bloco substitui o anterior, da WO 0034** (organizar os álbuns). O que ele dizia está no CHANGELOG [0.18.0], na spec `meta/specs/261109-organizar-os-albuns.md` e em `logs/2026-11-09.md` e `logs/2026-11-11.md`.
````

**Texto novo (substitui a ancora inteira):**

````
## Última conversa (2026-11-11 a 2026-11-14, rampa conferida, fórmulas decididas, WO 0037)

- **0.19.0 conferida na tela pelo dono** («rampa ok» `[relatado pelo dono, 2026-11-11 16:20]`): a rampa de BPM está fechada. CI verde no `790aa3a` (run `43082294050`, `[medido pelo Code, relatório 261111-1555]`).
- **Prompts prontos — análise** `meta/analises/261111-ANALISE-prompts-prontos.md`: os dois acervos reais têm 0 módulos e styles de 10 a 17 tags; uma fórmula tem de 5 a 14 tags, contra 1 a 3 de um módulo. O dono escolheu a opção D, fórmula de referência copiável inteira `[relatado pelo dono, 2026-11-11 17:12]` (DEC-037).
- **Spec da 0.20.0** `meta/specs/261111-formulas.md`, com protótipo na fileira «0.20» do canvas; os quatro pontos como recomendados `[relatado pelo dono, 2026-11-14 09:21]`. **A implementação não começou:** nenhum código e nenhum `../acervos/formulas.json` escrito.
- **Conversa do chat encerrada** em 2026-11-14 a pedido do dono (pesada); a próxima arranca pelo `../261114-HANDOFF-BRIEF.md`.
- **Este bloco substitui o anterior, da WO 0036** (rampa de BPM). O que ele dizia está no CHANGELOG [0.19.0], na spec `meta/specs/261111-rampa-de-bpm.md` e em `logs/2026-11-11.md`.
````

### E03 — pendências: sai conferir a rampa

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
- **Conferir a rampa de BPM na tela** — roteiro na conversa de 2026-11-11 (WO 0036), depois do push, com uma das três faixas BR com rampa.
````

**Texto novo:** vazio — apague a ancora inteira (a linha e a sua quebra).

### E04 — backlog: as fórmulas

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
1. **Importar prompts prontos dos álbuns como módulos** — o último ⬜ da 3b no ROADMAP; o índice-mestre da BR e os «estilos originais» do VOL5 trazem fórmulas de estilo.
````

**Texto novo (substitui a ancora inteira):**

````
1. **Fórmulas de referência (0.20.0, DEC-037)** — spec `meta/specs/261111-formulas.md` pronta, com os pontos decididos: implementar num clone (chat), escrever `../acervos/formulas.json` com as 18 fórmulas conferidas contra os guias, WO para o Code. Fecha a 3b.
````

### E05 — o ⬜ da 3b com o texto novo

**Arquivo:** `meta/ROADMAP.md`

**Ancora:**

````
- ⬜ Importar prompts prontos dos álbuns como módulos.
````

**Texto novo (substitui a ancora inteira):**

````
- ⬜ Fórmulas de referência dos álbuns, copiáveis inteiras (0.20.0, DEC-037). Era «importar prompts prontos como módulos»: a análise `meta/analises/261111-ANALISE-prompts-prontos.md` mediu que como módulo não serve.
````

### E06 — i-052, a paleta de módulos

**Arquivo:** `meta/IDEAS.md`

**Ancora:**

````
**Entregue (2026-11-09, DEC-034):** `tests/` com 32 testes (básico, organizar, salvar no arquivo, ida e volta, celular) e o workflow `.github/workflows/testes.yml`, que roda a cada push. Só dados sintéticos: o dono perguntou se seriam versionados os acervos — não `[relatado pelo dono, 2026-11-09]`.
````

**Texto novo (substitui a ancora inteira):**

````
**Entregue (2026-11-09, DEC-034):** `tests/` com 32 testes (básico, organizar, salvar no arquivo, ida e volta, celular) e o workflow `.github/workflows/testes.yml`, que roda a cada push. Só dados sintéticos: o dono perguntou se seriam versionados os acervos — não `[relatado pelo dono, 2026-11-09]`.

### i-052 💡 Paleta de módulos do acervo
`[capturada pelo chat, 2026-11-11, na análise dos prompts prontos]` Os dois acervos reais têm 0 módulos: o painel de módulos fica vazio com dado real. Uma paleta por acervo poderia vir de duas fontes: (1) as tags que se repetem nas faixas (medido em 2026-11-11: 25 tags aparecem em 10 faixas ou mais na BR, 34 nos reagrupados) e (2) as fórmulas decompostas, uma tag por módulo, mais as 3 listas de voz do `album_guia_suno` que ficaram fora das fórmulas (DEC-037). Limite medido: os styles das faixas já têm de 10 a 17 tags (mediana 12), e módulo só soma — ligar um piora o orçamento. Classificar cada tag numa das sete camadas pede julgamento. Pede análise antes da spec.
````

### E07 — prompt pronto vira fórmula

**Arquivo:** `meta/GLOSSARY.md`

**Ancora:**

````
**Style de referência / prompt pronto** — um texto de style completo já validado (como os dos álbuns). No Cancioneiro, pode virar um módulo de estilo importável.
````

**Texto novo (substitui a ancora inteira):**

````
**Style de referência / prompt pronto / fórmula** — um texto de style completo já validado (como os dos álbuns). No Cancioneiro é uma **fórmula** (`styleReferences` na coleção, 0.20.0, DEC-037): copiada inteira para começar uma faixa nova. Não é módulo: módulo é um trecho de 1 a 3 tags numa camada.
````

### E08 — DEC-037

**Arquivo:** `meta/DECISIONS.md`

**Ancora:**

````
**Consequências:** (+) O que se copia é o que está escrito, também na rampa — a promessa da DEC-020. (+) As três faixas passam no `validate.py` com aviso. (−) Uma forma de ligação fora da lista cai na DEC-020 e o validador reprova: falha alta, não silenciosa. (−) A lista de formas mora em dois lugares (app e validador), com um comentário apontando um para o outro.
````

**Texto novo (substitui a ancora inteira):**

````
**Consequências:** (+) O que se copia é o que está escrito, também na rampa — a promessa da DEC-020. (+) As três faixas passam no `validate.py` com aviso. (−) Uma forma de ligação fora da lista cai na DEC-020 e o validador reprova: falha alta, não silenciosa. (−) A lista de formas mora em dois lugares (app e validador), com um comentário apontando um para o outro.

## DEC-037 — Prompts prontos viram fórmulas de referência copiáveis inteiras (`styleReferences`), não módulos

**Data:** 2026-11-14
**Status:** aceita — implementação pendente (0.20.0)
**Contexto:** O último ⬜ da Fase 3b dizia «importar prompts prontos dos álbuns como módulos». A análise `meta/analises/261111-ANALISE-prompts-prontos.md` mediu em 2026-11-11: os dois acervos reais têm 0 módulos; os styles das faixas têm de 10 a 17 tags (mediana 12), acima do orçamento da DEC-021; um prompt pronto tem de 5 a 14 tags e atravessa camadas, contra 1 a 3 tags numa camada de um módulo; 100 das 151 faixas da BR não têm nenhuma fórmula do índice-mestre a ≥ 25%. O dono escolheu a opção D em 2026-11-11 `[relatado pelo dono]` e os quatro pontos da spec `meta/specs/261111-formulas.md` como recomendados em 2026-11-14 `[relatado pelo dono]`.
**Decisão:**
- **Campo opcional `styleReferences[]` na coleção:** `id`, `label`, `style` (só o copiável, sem colchetes nem rótulo), `notes` e `source` opcionais; nenhum outro campo. Faixas e módulos não mudam.
- **Uma janela «Fórmulas»**, aberta pela lateral (≥ 1280 px) e pelo «⋯», só quando o acervo tem fórmulas; agrupada por `source`, com a linha de qualidade do cartão, «Copiar Style», as notas recolhidas e «Excluir» com «Desfazer». Editar, no arquivo.
- **Entram pela janela de importar faixas**, que aceita `albums: []` com fórmulas; idêntica pula, mesmo id e conteúdo diferente entra com sufixo.
- **As 18 do dono** (índice-mestre BR 6, BR VOL1 4, VOL5 4, `album_guia_suno` 4 de clima) num `../acervos/formulas.json` escrito pelo chat e conferido por script contra os guias; as 3 listas de voz ficam de fora (i-052). O `[SILENCE - 4 beats] antes do drop final` da Grand Anthem é instrução de Lyrics e vai para `notes`.
- **O prompt-modelo não muda.**
**Alternativas consideradas:** cada fórmula como um módulo (fura o contrato de 1 a 3 tags e o orçamento); decompor em módulos de 1 tag (a fórmula deixa de ser copiável inteira — fica na i-052); paleta pelas tags repetidas (outra coisa, i-052); as fórmulas como um álbum de faixas comuns (contam como faixa, e o esquema exige `lyrics`); fechar o item sem fazer; uma vista no lugar da lista em vez da janela; editar no app; as 21 com as listas de voz; ensinar o campo no prompt-modelo.
**Consequências:** (+) As fórmulas validadas saem dos `.md` e ficam a um clique de copiar, separadas do «por que funciona». (+) Nada muda para quem não tem fórmulas. (−) Um campo a mais no esquema e uma janela a mais. (−) Fórmula envelhece com o Suno; a linha de qualidade e o `source` mostram de onde e de quando ela veio.
````

## Depois de aplicar — conferencia antes do commit

| # | Checagem | Comando | Esperado |
|---|---|---|---|
| 1 | Os arquivos sao os previstos | `sha1sum meta/DECISIONS.md meta/GLOSSARY.md meta/IDEAS.md meta/ROADMAP.md meta/STATUS.md meta/specs/261111-formulas.md logs/2026-11-14.md` | a coluna **chegada** |
| 2 | A pendencia saiu | `grep -c '^- \*\*Conferir a rampa' meta/STATUS.md` | `0` |
| 3 | A decisao entrou | `grep -c '^## DEC-037' meta/DECISIONS.md` e `grep -c '^### i-052' meta/IDEAS.md` | `1` e `1` |
| 4 | Validacao | `python3 scripts/validate.py; echo "exit=$?"` | `exit=0`, versao 0.19.0 |
| 5 | Nada alem do previsto | `GIT_OPTIONAL_LOCKS=0 git status --short --untracked-files=all` | os 7 arquivos da tabela e esta WO |
| 6 | Depois do push: o CI | `gh run list --limit 1`, em laco com `gh run view <id> --json status,conclusion` ate `completed` | relate o estado cru; vermelho num commit so de docs e achado: o passo que caiu e as ultimas 30 linhas de `gh run view <id> --log-failed` |

As checagens 2 e 3 rodaram na copia do chat, shell Linux; no Git Bash, **nao testado**. **Esta e qual pergunta?** A 1 responde «esta la?»; a 5 responde «a proxima conversa le um repo limpo?».

## Relatorio de aplicacao

Grave em `../AAMMDD-HHMM-code-cancioneiro-apply-wo0037.txt`, com o carimbo de `date +%y%m%d-%H%M` rodado na hora. Checagem 1 em primeiro lugar e o estado final do CI. **Sem `/wrap` depois desta WO** (o log de 2026-11-14 ja tem a conversa do chat), salvo se algo fugir do literal.

## Commit

```
git add meta/DECISIONS.md meta/GLOSSARY.md meta/IDEAS.md meta/ROADMAP.md meta/STATUS.md meta/specs/261111-formulas.md logs/2026-11-14.md meta/workorders/261114-wo0037-registro-formulas-e-handoff.md
```

```
git commit -m "docs: rampa conferida, formulas decididas (DEC-037), i-052 e log de 2026-11-14" -m "Registra tres fatos relatados pelo dono (0.19.0 conferida, opcao D, os quatro pontos da spec das formulas). STATUS, ROADMAP, IDEAS, GLOSSARY e DECISIONS. Sem codigo."
```

```
git push
```
