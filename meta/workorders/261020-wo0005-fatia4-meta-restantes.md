# WO 0005 — Fatia 4 do kit v1.127.0: os meta/ restantes, a pasta morta e as ideias paradas

## Cabecalho

> **Tipo:** mista (remocao de pasta + WO de DOC/registro).
> **Config sugerida:** Sonnet · `/effort low`.
> **Pre-requisito:** commit `bb3d18f`, branch `main`, sincronizada com `origin/main`, arvore limpa fora do que esta listado abaixo.
> **Base:** WO 0004 (fatia 3) e os relatorios `../261020-2028-code-fatia3-kit-apply-wo0004.txt` e `../261020-2048-code-fatia3-kit-wrap-wo0004.txt`. Divisao de escrita: DEC-010.
> **Depende de:** WO 0004, ja aplicada.
>
> **Arquivos que o chat gravou no disco e esta WO versiona** (sha1sum medido pelo chat ao gravar, 2026-10-20):
> - `meta/SPEC.md` — `26da596dcc346114c2b37a922c1b4c26294610d0` (arquivo NOVO)
> - `meta/CONTEXT.md` — `86697f48b547316a68213d6f34ed6435ef917979`
> - `README.md` — `9eed4e68fec8102c5427a053f44e2d13cc7527b0`
> - `meta/ROADMAP.md` — `03ed0dc6c2535ef7bfe1d94ad4158842f9cc0583`
>
> **Ancora semantica:** se um trecho-ancora nao bater EXATAMENTE, PARE e reporte.
> **Idempotencia:** antes de cada insercao, procure a frase-chave do texto NOVO; se ja existir, PULE e diga no relatorio.
>
> **Ancoras lidas em:** trechos lidos pelo chat no turno de 2026-10-20, direto do disco:
> - `meta/DECISIONS.md`, ultima linha do arquivo (fim de DEC-014), que comeca com `**Consequencias:** (+) O ritual passa a ser por turno`
> - `meta/STATUS.md`, linha 14: `- Pendente do kit: fatia 4 (demais \`meta/\`, \`meta/specs/\`, títulos \`## Última sessão\` deste arquivo).`
> - `meta/STATUS.md`, linha 16: `## Última sessão (2026-10-20, kit v1.127.0 — fatias 1 e 2)`
> - `meta/STATUS.md`, linha 23: `## Última sessão (2026-07-21, auditoria)`
> - `meta/IDEAS.md`, linha 71 (ultimo item das Ativas, i-021): `A API expõe pesos 0.00-1.00 para aderência ao estilo e desvio criativo (os Creative Sliders). Poderiam virar campos opcionais do esquema para registrar a configuração usada numa geração. Só vale se o fluxo passar a depender disso. Fase 4.`
> - `meta/GLOSSARY.md`, ultima linha do arquivo: `**Custom Mode** — modo do Suno que separa os campos (Style / Lyrics) para controle fino, por oposição ao Simple Mode (descrição única). O Cancioneiro assume Custom Mode.`

---

## 1. Por que esta fatia NAO e adocao de template

Nas fatias 1-3 o template do kit era mais novo que o arquivo vivo. Aqui e o contrario, e o proprio manifesto decide: **«template generico nao e candidato a substituir arquivo vivo refinado; os `meta/` ja especializados caem por padrao em (c)»**. Comparei os cabecalhos de todos os sete e o vivo ganha em todos:

| Arquivo | Vivo | Template v1.127.0 | Veredito |
|---|---|---|---|
| `CONTEXT.md` | 13 secoes, incl. «As duas metades», «O modelo de dados (o coracao)», «Suno na pratica» | 10 secoes com `[Nome do Projeto]` e `[componente crítico]` | **(c)** — fica o vivo |
| `STATUS.md` | 9 secoes em portugues, sem emoji | 7 secoes com emoji | **(c)** — fica o vivo |
| `IDEAS.md` | 21 ideias com IDs `i-NNN`/`c-NNN`/`x-NNN`, rastreadas entre ROADMAP e STATUS | esqueleto por autor, com `[Título da ideia]` | **(c)** — e o CEREBRO v1.127.0 cita este caso nominalmente como **desvio legitimo**: «projeto cujo roadmap e registro de decisoes referenciam ideias por ID estavel organiza o IDEAS por status + ID, nao pela divisao por autor do template — adotar o template ali seria regressao» |
| `ROADMAP.md` | 4 fases reais, datadas, com marcos | `F1 — [Nome da fase]` | **(c)** — fica o vivo |
| `GLOSSARY.md` | 2 eixos, ~20 termos reais do dominio | 4 eixos vazios | **(c)** no conteudo; o eixo «Comandos / artefatos» e **(a)** util — ver Edicao 4 |
| `HISTORY.md` | 13 secoes com nivel de confianca e fontes | 5 slots `[Guia técnico consolidado]` | **(c)** — nem entra nesta WO |
| `CHANGELOG.md` | 5 versoes reais | `[0.1.0] — AAAA-MM-DD` | **(c)** — nem entra nesta WO |

**Entao a fatia 4 e outra coisa:** varrer a cadencia que sobrou, matar a pasta morta, adotar o unico arquivo que falta de verdade (`meta/SPEC.md`), e pagar uma divida de agosto no IDEAS.

## 2. O que o chat gravou

**`meta/SPEC.md`** — arquivo **novo**. Modelo de spec de feature do v1.127.0, natureza `template`: o projeto nao tinha. Ele fecha o funil que o CEREBRO novo descreve — exploracao → sonda → **analise/spec** → WO → DECISIONS — e a Fase 3 (painel de qualidade) e exatamente o tipo de frente que comeca por spec. Acrescentei tres linhas ao cabecalho: o caminho correto neste projeto (`meta/specs/`, nao `specs/`), a distincao spec × WO, e o aviso de que a pasta nasce no primeiro uso e **nao deve ser recriada para guardar este modelo** — que e justamente o erro que a Edicao 1 corrige.

**`meta/CONTEXT.md`** — tres correcoes na arvore do repositorio, que estava mentindo em tres pontos: `specs/` (pasta morta) vira `workorders/` com o `_TEMPLATE.md`; `SPEC.md` entra na lista do `meta/`; `.claude/` deixa de dizer «vem do zip» e passa a nomear as tres skills; e `logs/` vira «diario do dia». **Nao toquei em nada alem da arvore** — as 13 secoes de conteudo ficam como estao.

**`README.md`** — duas correcoes na arvore, mesmas razoes. O README e a cara publica e ja ficou tres versoes atras uma vez (FIX da auditoria de julho).

**`meta/ROADMAP.md`** — uma linha: «numa sessao de geracao no Suno» → «numa rodada de geracao no Suno». Caso de fronteira: «sessao de geracao» e meio dominio, meio cadencia, e num marco de roadmap ela **manda** (define quando a fase fecha). Trocada por um termo que nao colide com o vocabulario do kit.

## Edicao 0 — Conferencia de hash

```
sha1sum meta/SPEC.md meta/CONTEXT.md README.md meta/ROADMAP.md
```

Confira contra o cabecalho. Hash diferente = outro escritor mexeu depois do chat: **PARE e reporte**.

## Edicao 1 — `meta/specs/` · remover a pasta morta

Ela nasceu em 2026-07-20 (`.gitkeep`, 0 bytes) e **nunca recebeu uma spec**. A skill que a lia (`apply-spec`) saiu na fatia 1. Medido: `git ls-files meta/specs/` devolve so `meta/specs/.gitkeep`.

```
git rm meta/specs/.gitkeep
```

O `git rm` do unico arquivo remove a pasta. Se falhar por permissao de apagar, reporte — **nao contorne** movendo para outro lugar dentro do repo.

**Nao recrie `meta/specs/` para guardar o `meta/SPEC.md`.** O modelo mora em `meta/`; a pasta nasce quando a primeira spec for escrita.

## Edicao 2 — `meta/STATUS.md` · os dois titulos e a higiene do rolante

**2a — os dois titulos.** Troque, exatamente:

- Linha 16: `## Última sessão (2026-10-20, kit v1.127.0 — fatias 1 e 2)` → `## Última conversa (2026-10-20, kit v1.127.0 — fatias 1 e 2)`
- Linha 23: `## Última sessão (2026-07-21, auditoria)` → `## Última conversa (2026-07-21, auditoria)`

Depois disso `grep -c "^## Última conversa" meta/STATUS.md` deve dar **3** e `grep -c "^## Última sessão" meta/STATUS.md` deve dar **0**.

**2b — o STATUS acumulou tres blocos de «ultima», e e rolante.** Isto nao e cadencia, e higiene: o proprio arquivo manda «item resolvido sai daqui e vai para o CHANGELOG». Os blocos das fatias 1-2 e da fatia 3 descrevem o MESMO trabalho (o merge do kit), em duas conversas do mesmo dia. **Funda os dois num so**, mantendo o titulo `## Última conversa (2026-10-20, kit v1.127.0 — fatias 1 a 4)`, com o estado consolidado; o bloco da auditoria de 2026-07-21 **fica como esta**, e o detalhe das conversas ja vive em `logs/2026-10-20.md`. Se preferir nao fundir, **diga no relatorio** e deixe os tres — mas aí registre que o STATUS esta acumulando.

**2c — atualizar a pendencia e a varredura.** A linha 14 (`Pendente do kit: fatia 4 ...`) deixou de ser verdade. E a contagem da varredura precisa do numero medido AGORA, que mudou de novo:

```
LC_ALL=C.UTF-8 grep -rnoiE "sess(ão|ao|ões|oes)" meta/ CLAUDE.md INSTRUCOES-DO-PROJETO.md README.md .claude/ .gitignore .flatdropignore logs/ | wc -l
```

O chat mediu **71** antes de escrever esta WO — e o relatorio da fatia 3 tambem mediu 71, contra os 67 previstos, pela mesma razao de sempre: as proprias WOs e DECs citam o termo para explica-lo. **Meça de novo depois de aplicar e escreva o numero medido, nao o previsto.** Classifique assim, que e o que o feedback ao kit desta fatia pede:

| Classe | Onde | Alvo |
|---|---|---|
| **Manda** (dirige comportamento) | nenhum arquivo restante | **zero — atingido nesta fatia** |
| **Relata** (fato historico datado) | `logs/*` (8), `DECISIONS` (6), `CHANGELOG` (1), `IDEAS` (2), `STATUS` (relato) | fica |
| **Dominio** (sessao do navegador / Suno) | `CONTEXT:34`, `README:53` | fica |
| **Contraste deliberado** (kit v1.127.0 verbatim) | `CEREBRO` (3), `.claude/skills/*` (5) | fica |
| **Meta-documentacao da propria correcao** | WOs 0002-0005, `_TEMPLATE.md` | fica, e cresce a cada fatia |

Com os dois titulos do STATUS trocados, **a classe «manda» chega a zero** e a varredura pode ser declarada **ENCERRADA na primeira classe** — dizendo com todas as letras que o total continua alto porque as outras quatro classes sao legitimas. Nao declare «encerrada» sem a unidade colada no numero.

## Edicao 3 — `meta/IDEAS.md` · tres ideias paradas desde agosto

Estao no `../260822-0435.txt`, na pasta-pai, **desde 2026-08-22** — o dono as escreveu e elas nunca entraram no IDEAS, contra o principio «captura ideias», que manda registrar na hora. Sao da frente de produto, nao do kit.

**Ancora:** o ULTIMO item das Ativas, a linha do i-021 citada no cabecalho. Insira DEPOIS dela, antes de `## Feedback para o Kit`.

**Texto a inserir, literal:**

```

### i-022 💡 Skill que ensina a gerar o JSON do Cancioneiro
`[relatado pelo dono, 2026-08-22]` Uma skill do projeto que ensine um chat a produzir o JSON canonico seguindo o esquema a risca — estrutura, campos obrigatorios, a regra de dominio (rotulo fora do bloco copiavel). Hoje isso vive no `schema/PROMPT-PARA-CHATS.md`, que e um texto colavel: a skill seria a versao que o proprio Claude Code carrega. **Sobreposicao a resolver antes de construir:** i-002 (o prompt-modelo) ja cobre parte disto; decidir se a skill substitui o prompt-modelo ou se os dois convivem em canais diferentes (chat colavel × skill do repo).

### i-023 💡 Skill com os macetes do Suno
`[relatado pelo dono, 2026-08-22]` Uma skill que consolide o que o projeto sabe sobre gerar musica com IA: como estruturar cada parte, onde cada coisa entra, possibilidades e exemplos. **O material ja existe** — e o `meta/HISTORY.md` §1-13, com nivel de confianca e fontes. A ideia e a FORMA, nao o conteudo: transformar conhecimento lido sob demanda em skill lida antes de trabalhar. Pesar contra o custo: skill e lida sempre, HISTORY so quando preciso.

### i-024 💡 Molde para o projeto gerar skill de estilo proprio
`[relatado pelo dono, 2026-08-22]` Nao e uma skill, e um **molde que gera skills** — uma por estilo musical, capturando como manter o mesmo estilo, voz, idioma, forma de escrever letra, tom e melodia, e como guiar edicao, extend e cover. Serviria para replicar ou refinar um estilo ja estabelecido. E a ideia mais ambiciosa das tres e a mais dependente das outras duas; candidata a analise (`meta/analises/`) antes de qualquer spec, porque mexe no formato de um artefato que outra pessoa vai ler.
```

## Edicao 4 — `meta/GLOSSARY.md` · o eixo que faltava

O template v1.127.0 tem quatro eixos; o vivo tem dois. O eixo **«Comandos / artefatos»** virou necessario nesta semana: o projeto ganhou `/apply-wo`, `/wrap`, `/sondar`, WO, relatorio de trabalho e carimbo de versao, e **nenhum desses termos esta no glossario** (medido: `grep -niE "apply-wo|/wrap|/sondar|\bWO\b" meta/GLOSSARY.md` devolve vazio).

**Ancora:** a ULTIMA linha do arquivo, citada no cabecalho (`**Custom Mode** — ...`). Insira DEPOIS dela.

**Texto a inserir, literal:**

```

---

## Comandos / artefatos

**WO (ordem de trabalho)** — instrucao de APLICACAO que o chat autora e o Code posiciona: ancora semantica mais o texto exato de cada edicao. Vive em `meta/workorders/AAMMDD-woNNNN-desc.md`. Diz **como aplicar**; a spec diz **o que construir**.

**Spec de feature** — o que construir e quando esta pronto: problema, criterios de aceite verificaveis, decisoes, fora de escopo. Modelo em `meta/SPEC.md`; as specs preenchidas vao para `meta/specs/`, pasta que nasce no primeiro uso.

**`/apply-wo`** — skill do Claude Code que aplica uma WO. Recusa a WO cujo cabecalho nao traz «Ancoras lidas em» preenchido, e PARA se uma ancora nao bater exatamente.

**`/wrap`** — skill que fecha a tarefa: confere o relatorio anterior contra o git, atualiza STATUS e DECISIONS, escreve o log do dia, commita e empurra.

**`/sondar`** — skill de exploracao: le o material sem hipotese previa e devolve CANDIDATOS a checagem, nunca veredito. Exploracao produz hipotese; instrumento produz evidencia.

**Relatorio de trabalho** — o que o Code grava ao fechar qualquer tarefa, em `../AAMMDD-HHMM-code-<slug>-<ato>-<alvo>.txt` (pasta-pai, fora do versionamento). O `<ato>` e vocabulario fechado: `apply` · `wrap` · `probe` · `explore`.

**Carimbo do kit** — a linha `Gerado pelo Kit de Contexto Universal vX.Y.Z` no fim do CEREBRO, do modelo de WO e das tres skills. Nao se funde: substitui-se pela do pacote mais recente. Os cinco devem concordar.

**Analise** — documento que precede o compromisso numa mudanca nao-trivial: problema, restricoes medidas, opcoes com o motivo do descarte, recomendacao, riscos, ponto de decisao. Vive em `meta/analises/`, pasta que nasce no primeiro uso. Nao decide nem abre trabalho sozinha.
```

## Edicao 5 — `meta/DECISIONS.md` · uma DEC

**Ancora:** a ULTIMA linha do arquivo (fim de DEC-014), citada no cabecalho. Insira DEPOIS dela, precedido de uma linha em branco e de `---`.

```
---

## DEC-015 — Os meta/ especializados nao sao substituidos pelo template; a pasta `meta/specs/` morre

**Data:** 2026-10-20
**Contexto:** Fatia 4 do merge do kit v1.127.0. Ao contrario das fatias 1-3, onde o template era mais novo que o arquivo vivo, aqui o vivo e mais rico em todos os sete arquivos comparados — o template traz esqueletos com placeholders (`[Nome do Projeto]`, `F1 — [Nome da fase]`). O manifesto ja prevê este caso: «template generico nao e candidato a substituir arquivo vivo refinado; os meta/ ja especializados caem por padrao em (c)». O CEREBRO v1.127.0 cita nominalmente o caso do IDEAS organizado por ID estavel como desvio legitimo. Separadamente: `meta/specs/` existia vazia desde 2026-07-20 e a skill que a lia saiu na fatia 1.

**Decisao:** `CONTEXT`, `STATUS`, `IDEAS`, `ROADMAP`, `GLOSSARY`, `HISTORY` e `CHANGELOG` **permanecem na forma deste projeto**. Do template entram apenas: o arquivo novo `meta/SPEC.md` (modelo de spec de feature, que o projeto nao tinha) e o eixo «Comandos / artefatos» no `GLOSSARY`. A pasta `meta/specs/` e **removida**; o modelo de spec mora em `meta/SPEC.md` e a pasta renasce quando a primeira spec for escrita — pasta nunca nasce para receber um modelo.

**Alternativas consideradas:** (a) adotar os templates e reinjetar o conteudo — descartada: seria regressao de forma, e o CEREBRO do proprio kit diz isso; (b) manter `meta/specs/` vazia «porque pode servir» — descartada: pasta vazia versionada com `.gitkeep` orfao e exatamente o estado que faz um assistente futuro procurar spec onde nao ha nenhuma, e foi o que aconteceu nesta semana.

**Consequencias:** (+) O funil fica completo: exploracao → sonda → analise/spec → WO → DECISIONS, com modelo para cada peca. (+) O vocabulario novo do kit entra no glossario, que e onde se procura. (+) A arvore do repositorio no `CONTEXT` e no `README` para de mentir. (−) `meta/analises/` ainda nao existe e o modelo dela nao entra (natureza `modelo-em-espera`): quando a primeira analise nascer, ha de vir do pacote. (−) Duas pastas do projeto passam a ser «nascem no primeiro uso», o que so funciona se estiver escrito — por isso a nota no `meta/SPEC.md` e no glossario.
```

## Edicao 6 — `meta/IDEAS.md` · um feedback ao kit

**Ancora:** o ultimo dos tres itens `[2026-10-20]` inseridos pela WO 0004, na secao `## Feedback para o Kit`. Insira DEPOIS dele.

```
- **[2026-10-20] O carimbo de modos nao cobre o caso «o template e mais pobre que o vivo», e o manifesto resolve isso em prosa.** A natureza `template` diz «comparar e adotar novidade e seguro», e a regra que protege o arquivo vivo esta num paragrafo mais abaixo. Numa fatia em que SETE arquivos caem todos em (c), ler na ordem leva a propor substituicao sete vezes antes de chegar a regra que a proibe. Sugestao: o manifesto trazer, ao lado da natureza, qual das tres respostas e o DEFAULT esperado para aquele arquivo — `adotar`, `fundir` ou `(c) fica o vivo` —, que e informacao que quem gera o pacote tem e quem o recebe precisa descobrir lendo tudo.
```

## Fora de escopo

- `meta/HISTORY.md` e `meta/CHANGELOG.md` — **(c)** inteiro, nao entram.
- O conteudo (nao a arvore) de `CONTEXT`, `STATUS`, `IDEAS`, `ROADMAP`, `GLOSSARY`, `README`.
- Criar `meta/analises/` ou `meta/specs/`. As duas nascem no primeiro uso.
- As ocorrencias de «sessao» classificadas como relato, dominio, contraste e meta-documentacao. **Nao as troque.**
- **O `album-referencias.json` e a captura de tela.** O chat abriu a captura neste turno e tem um achado — vai como candidato no relatorio ao dono, nao nesta WO. Nao mexa no app.

## Armadilhas desta WO

- **O STATUS tem tres blocos `## Última ...` e esta WO troca dois titulos E pode fundir dois blocos.** A skill `/wrap` manda contar a estrutura antes do commit justamente por isto: `grep -c "^## Última"` antes e depois, e o bloco de 2026-07-21 **tem de sobreviver**. Mover tem duas metades e a que some e sempre a de apagar.
- **A Edicao 3 insere texto DENTRO da secao «Ativas», antes de «Feedback para o Kit».** Confira que `## Feedback para o Kit` continua depois, uma vez so.
- **`git rm meta/specs/.gitkeep` apaga.** Se a permissao de apagar estiver negada, o comando falha — reporte, nao contorne.
- **O `grep` de cadencia precisa de `LC_ALL=C.UTF-8`.** Sem isso a classe acentuada nao casa e a contagem vem zerada — falso negativo real no inicio deste merge.
- **Nao preveja o total da varredura: meça depois.** Tres fatias seguidas erraram esse numero, inclusive esta WO ao ser escrita.

## Depois de aplicar — conferencia antes do commit

| # | Checagem | Comando | Esperado |
|---|---|---|---|
| 1 | A pasta morta sumiu | `ls meta/specs 2>&1` e `GIT_OPTIONAL_LOCKS=0 git ls-files meta/specs` | «No such file or directory» e saida vazia |
| 2 | O modelo de spec esta em `meta/`, nao em `meta/specs/` | `ls meta/SPEC.md` | existe |
| 3 | Nenhum titulo «Última sessão» restou | `grep -c "^## Última sessão" meta/STATUS.md` | `0` |
| 4 | Os blocos de «Última conversa» | `grep -c "^## Última conversa" meta/STATUS.md` | `2` se fundiu os dois de 2026-10-20, `3` se nao fundiu — **diga qual** |
| 5 | O bloco da auditoria sobreviveu | `grep -c "2026-07-21, auditoria" meta/STATUS.md` | `1` |
| 6 | Classe «manda» zerada | `LC_ALL=C.UTF-8 grep -rniE "sess(ão\|ao)" meta/STATUS.md \| grep -c "^meta/STATUS.md:[0-9]*:## "` | `0` |
| 7 | As tres ideias entraram, uma vez cada | `grep -c "^### i-022" meta/IDEAS.md`, `i-023`, `i-024` | `1` cada |
| 8 | As Ativas nao engoliram o Feedback | `grep -c "^## Feedback para o Kit" meta/IDEAS.md` | `1` |
| 9 | i-021 continua sendo o ultimo antes das novas | `grep -n "^### i-02[1-4]" meta/IDEAS.md` | i-021, i-022, i-023, i-024 nesta ordem |
| 10 | O eixo novo do glossario | `grep -c "^## Comandos / artefatos" meta/GLOSSARY.md` | `1` |
| 11 | Os termos novos estao la | `grep -c "apply-wo" meta/GLOSSARY.md` e `grep -c "sondar" meta/GLOSSARY.md` | `≥1` cada |
| 12 | A DEC entrou e as anteriores ficaram | `grep -c "^## DEC-015" meta/DECISIONS.md` e `grep -c "^## DEC-01[0-4]" meta/DECISIONS.md` | `1` e `5` |
| 13 | O feedback ao kit | `grep -c "^- \*\*\[2026-10-20\]" meta/IDEAS.md` | `4` |
| 14 | A arvore do CONTEXT nao cita mais a pasta morta | `grep -c "specs/" meta/CONTEXT.md` | `0` |
| 15 | O CONTEXT cita o que existe | `grep -c "workorders/" meta/CONTEXT.md` e `grep -c "SPEC.md" meta/CONTEXT.md` | `1` cada |
| 16 | Os cinco carimbos seguem concordes | `grep -rho "Kit de Contexto Universal v[0-9.]*" meta/CEREBRO.md meta/workorders/_TEMPLATE.md .claude/skills/ \| sort \| uniq -c` | `5 ... v1.127.0` |
| 17 | Varredura geral — MEDIDA, nao prevista | `LC_ALL=C.UTF-8 grep -rnoiE "sess(ão\|ao\|ões\|oes)" meta/ CLAUDE.md INSTRUCOES-DO-PROJETO.md README.md .claude/ .gitignore .flatdropignore logs/ \| wc -l` | o chat mediu **82** com esta WO ja no disco (`48` dentro de `meta/workorders/`, `34` fora). Antes de escreve-la eram 71. **Meça e escreva o seu numero**, separando dentro/fora de `meta/workorders/` — o relatorio e o log que voce vai escrever somam mais. Previsao de total aqui seria o quarto erro seguido; por isso a celula pede medicao, nao numero. |
| 18 | Nenhum relatorio `.txt` dentro do repo | `GIT_OPTIONAL_LOCKS=0 git status --short \| grep -c '\.txt'` | `0` |

**Os tres campos de cada passo:** todos sao rodados por **quem aplica (o Code)**, na raiz do repo (`C:\Users\alexk\Tools\cancioneiro\cancioneiro`), em Git Bash. **O que nenhum deles responde:** se as tres ideias novas (i-022 a i-024) tem sobreposicao real com i-002 — isso e analise, e esta anotada dentro da propria i-022 como pergunta a resolver antes de construir.

## Relatorio de aplicacao

Grave em `../261020-HHMM-code-fatia4-kit-apply-wo0005.txt`, com o `HHMM` de `date +%y%m%d-%H%M` rodado na hora. Diga explicitamente se fundiu ou nao os dois blocos de 2026-10-20 no STATUS (checagem 4).

**Proximo comando** (ultima linha do relatorio, cru e sozinho):

```
/sondar app/index.html schema/ data/
```

## Commit

```
git add meta/SPEC.md meta/CONTEXT.md README.md meta/ROADMAP.md meta/STATUS.md meta/IDEAS.md meta/GLOSSARY.md meta/DECISIONS.md meta/workorders logs
```

```
git commit -m "docs: aplica fatia 4 do kit v1.127.0 e encerra a varredura de cadencia" -m "Os meta/ especializados ficam na forma do projeto (DEC-015); do template entram so o modelo de spec (meta/SPEC.md, novo) e o eixo Comandos/artefatos no glossario. Remove a pasta morta meta/specs/. Troca os dois titulos Ultima sessao por Ultima conversa, zerando a classe manda da varredura. Corrige a arvore do repo no CONTEXT e no README. Captura as ideias i-022 a i-024, paradas na pasta-pai desde 2026-08-22."
```

```
git push
```
