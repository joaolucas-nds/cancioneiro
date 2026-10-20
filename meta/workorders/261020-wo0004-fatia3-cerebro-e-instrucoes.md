# WO 0004 — Versionar a fatia 3 do kit v1.127.0: CEREBRO, Instrucoes e o molde do log

## Cabecalho

> **Tipo:** WO de DOC (registro). Nenhum codigo muda.
> **Config sugerida:** Sonnet · `/effort low`. O julgamento (o que funde, o que fica) foi feito no chat; aqui e conferir, registrar e commitar.
> **Pre-requisito:** commit `db73211`, branch `main`, sincronizada com `origin/main`, arvore limpa fora do que esta listado abaixo.
> **Base:** WO 0003 (fatia 2) e os relatorios `../261020-0733-code-fatia2-kit-apply-wo0003.txt` e `../261020-0735-code-fatia2-kit-wrap-wo0003.txt`. Divisao de escrita: DEC-010.
> **Depende de:** WO 0003, ja aplicada.
>
> **Arquivos que o chat gravou no disco e esta WO versiona** (sha1sum medido pelo chat ao gravar, 2026-10-20):
> - `meta/CEREBRO.md` — `476eb129d22a3f4a77fe7d5b366682d35d6d93cf`
> - `INSTRUCOES-DO-PROJETO.md` — `3603588508425f971bac03e20310c1e67cd87425`
> - `meta/LOG-TEMPLATE.md` — `f6324c137ca2ac7e56a1e21cb1c219b80f6fc4d9`
>
> **Ancora semantica:** se um trecho-ancora nao bater EXATAMENTE, PARE e reporte.
> **Idempotencia:** antes de cada insercao, procure a frase-chave do texto NOVO; se ja existir, PULE e diga no relatorio.
>
> **Ancoras lidas em:** trechos lidos pelo chat no turno de 2026-10-20, direto do disco:
> - `meta/DECISIONS.md`, ultima linha do arquivo: `**Consequencias:** (+) `meta/workorders/_TEMPLATE.md` volta a subir ao Projeto; o corpo das WOs aplicadas, nao. (+) `.claude/settings.local.json` passa a ser ignorado pelo git, em vez de ficar untracked indefinidamente. (−) `meta/specs/` continua no disco com um `.gitkeep` orfao — remover e de uma fatia seguinte, junto com as citacoes a ela no `meta/CEREBRO.md` e no `meta/CONTEXT.md`.`
> - `meta/STATUS.md`, linha 10: `## Última sessão (2026-10-20, kit v1.127.0 — fatias 1 e 2)`
> - `meta/IDEAS.md`, linha 73: `## Feedback para o Kit`
> - `meta/IDEAS.md`, ultimo item da secao Feedback: `- **[2026-07-19] Raia chat×Code confirmada na prática.** Construí o v0 da ferramenta no chat (decisão de forma, com pesquisa de UI e design). A partir daqui, a iteração fina (ajustes pós-validação visual) vai melhor no Claude Code por spec. O ponto de virada chat→Code é "forma decidida → executar deltas".`

---

## 1. Por que, e o achado que muda a natureza desta fatia

O manifesto marca CEREBRO e INSTRUCOES como natureza `fusao` — «carregam comportamento que este projeto pode ter evoluido». **Medido, este projeto nao evoluiu o CEREBRO.** O chat comparou as 192 linhas nao-vazias do CEREBRO vivo (v1.74.0) contra o template v1.127.0, normalizando espaco em branco:

```
LINHAS DO VIVO SEM CORRESPONDENTE LITERAL NO TEMPLATE: 20 de 192
```

E as 20 nao sao conteudo deste projeto. Sao, uma a uma: 11 de cadencia «sessao» (linha revogada em v1.106.0), 4 do formato antigo (`meta/specs/`, `/apply-spec`, `AAMMDD-asuNNNN.yaml`), 1 do teto das Instrucoes sem o teto por configuracao, 1 do DECISIONS arquivado por tamanho em vez de por evento, 1 de cadencia na entrega, 1 titulo de secao e 1 o carimbo `v1.74.0`.

**Consequencia pratica:** a fatia 3 nao e um merge parcial, e uma adocao do template v1.127.0 com tres especializacoes deste projeto. O conhecimento do Cancioneiro nunca morou no CEREBRO — mora no `CONTEXT`, no `HISTORY`, no `DECISIONS` e nas Instrucoes, todos intocados aqui. Nada foi perdido porque nao havia nada ali para perder.

## 2. O que o chat gravou, arquivo por arquivo

**`meta/CEREBRO.md`** — template v1.127.0 adotado (274 → 477 linhas; 36,9 KB → 104,2 KB), com tres edicoes cirurgicas:

1. **`## Técnicas específicas deste projeto`** — a secao que o template deixa vazia de proposito e declara «esta secao e sua; um template-update nunca a sobrescreve». Preenchida com seis itens operacionais deste projeto, cada um com o lugar onde vale: a base manda na recomposicao do Style e o dedup compara sequencias de palavras (FIX-002 → FIX-003); testar o falso positivo ao corrigir comparacao; `validate.py` sem `jsonschema` passa verde sem validar; saida nova reverifica a regra de dominio; o diferencial nao e gerar prompt; o truncamento do Suno e silencioso. **Nenhum deles duplica texto de outro arquivo** — sao gatilhos que apontam para `HISTORY` e `DECISIONS`, nao copias.
2. **Divisao de escrita** — o bullet «Um dono por documento, escrito» do template ganhou a remissao: «Neste projeto a divisao esta adotada e registrada em DEC-010, nos termos acima». O texto do template ja descrevia exatamente a divisao escolhida.
3. **Ambiente da raia Code** — acrescentado que neste projeto nao ha build (`app/index.html` autonomo) e que a validacao e `python3 scripts/validate.py`, obrigatoria em `data/` e `schema/`, dispensada em doc.

Saiu, por consequencia: as 4 referencias a `meta/specs/`, `/apply-spec` e ASU, e as 11 de cadencia. **O carimbo passa a `v1.127.0`** — linha do kit, que substitui e nao funde.

**`INSTRUCOES-DO-PROJETO.md`** — fusao real (49 → 71 linhas; 4.858 → **6.386 caracteres**). Preservado inteiro o que e deste projeto: `## O que é`, `## Regra de domínio inviolável`, `## Domínio (Suno) — sempre lembrar`, a lista compacta de arquivos de contexto (mais curta que a do template, e desvio legitimo pela regra «especialize o que se aplica»), e os caminhos com prefixo `meta/`. Adotado do template: ritual de **turno** com `git log -3`/`git status`/pasta-pai a cada turno; o bloco «Canal — pasta vinculada»; analise antes do compromisso; «arquivo nao lido nao se deduz»; «WO nunca vai sozinha»; «ao final da conversa, REGISTRE o que falta»; e a remissao ao esqueleto do bloco de fecho. Acrescentadas duas linhas deste projeto: a divisao de escrita (DEC-010) e o teste do falso positivo (FIX-003); e ao dominio Suno, o truncamento silencioso.

Saiu: «Nome de download» (o canal mudou — arquivo vai direto ao lugar definitivo), «Ao final de cada sessao, entregue arquivos completos» com «arquivo novo para baixar... nunca blocos soltos» (linha revogada em v1.106.0), «sempre que o usuario sinalizar upload» (revogada em v1.90.0), e `## Ritual de início de sessão` (revogada em v1.106.0).

**Teto:** 6.386 caracteres. O template v1.127.0 declara ~6.900 no padrao, +550 para o modo Code, e total de 7.600 com modos ligados. Dentro, com folga de ~1.060 sobre o teto aplicavel.

**`meta/LOG-TEMPLATE.md`** — **ampliacao de escopo deliberada, declarada aqui.** O usuario pediu CEREBRO e Instrucoes; o chat incluiu este terceiro arquivo por um motivo medido: ele tinha **6 ocorrencias de cadencia que MANDAM** («Ao final de cada sessao, o assistente entrega um arquivo novo», `## Objetivo da sessão`), e e o molde que a skill `/wrap` — instalada na fatia 1 — le ANTES de escrever o log do dia. Deixa-lo uma fatia atras significaria a skill nova lendo um molde que contradiz tanto a cadencia nova quanto a DEC-010. Template v1.127.0 adotado (5 diferencas, todas de cadencia), mais uma nota deste projeto: quem escreve o log e o Code, pelo `/wrap`; duas conversas no mesmo dia = o mesmo arquivo com `## Conversa N`; e criar nao e regenerar.

## Edicao 0 — Conferencia de hash (antes de tudo)

```
sha1sum meta/CEREBRO.md INSTRUCOES-DO-PROJETO.md meta/LOG-TEMPLATE.md
```

Confira contra a lista do cabecalho. Hash diferente = outro escritor mexeu depois do chat: **PARE e reporte**, nao commite por cima.

## Edicao 1 — `meta/DECISIONS.md` · duas DEC novas

**Ancora:** a ULTIMA linha do arquivo, citada no cabecalho. Insira DEPOIS dela, precedido de uma linha em branco e de `---`.

**Texto a inserir, literal:**

```
---

## DEC-013 — CEREBRO adotado do kit v1.127.0; o especifico do projeto vive nos outros meta/

**Data:** 2026-10-20
**Contexto:** O `meta/CEREBRO.md` estava no kit v1.74.0, 53 versoes atras. O manifesto marca o arquivo como `fusao`, o que pressupoe comportamento proprio a preservar. A comparacao linha a linha contra o template v1.127.0 mostrou outra coisa: das 192 linhas nao-vazias do arquivo vivo, 20 nao tinham correspondente no template, e todas as 20 eram texto do kit ANTIGO — cadencia «sessao», `meta/specs/`, `/apply-spec`, ASU, o teto das Instrucoes sem o teto por configuracao, o DECISIONS arquivado por tamanho e o carimbo de versao. Nenhuma linha era deste projeto.

**Decisao:** O CEREBRO passa a ser o template v1.127.0 adotado integralmente, com tres especializacoes: a secao «Tecnicas especificas deste projeto» preenchida com os seis itens operacionais do Cancioneiro; a remissao a DEC-010 na divisao de escrita; e a nota de que nao ha build e a validacao e o `validate.py`. Fica registrado o principio que isto confirma: **o conhecimento deste projeto mora no CONTEXT, no HISTORY, no DECISIONS e nas Instrucoes — nao no CEREBRO**, que e a camada generica e portanto a mais barata de atualizar.

**Alternativas consideradas:** (a) merge paragrafo a paragrafo preservando a redacao viva — descartada: a medicao mostrou que nao havia redacao propria a preservar, e o custo seria reescrever 104 KB para chegar ao mesmo texto; (b) adotar o template sem preencher «Tecnicas especificas» — descartada: e a unica secao que um template-update futuro nao sobrescreve, e deixa-la vazia joga o conhecimento operacional de volta para arquivos que o assistente nao le a cada turno.

**Consequencias:** (+) Os quatro carimbos do kit (CEREBRO, modelo de WO, skills) passam a dizer v1.127.0. (+) Entram no comportamento: medicao delegada, bloco de fecho com carimbo `Base:`, sonda e exploracao, analise antes do compromisso, canal da pasta vinculada, correspondencia entre projetos. (+) Atualizacao futura do CEREBRO fica barata, porque o especifico esta fora dele. (−) O arquivo quase triplicou (36,9 → 104,2 KB); e lido sob demanda, nao a cada turno, mas pesa quando lido. (−) `meta/CONTEXT.md` ainda cita `meta/specs/` na arvore (linha 50) e a pasta morta continua no disco — fatia 4.

---

## DEC-014 — Instrucoes do Projeto na forma v1.127.0, com o dominio preservado; a fonte e o arquivo do repo

**Data:** 2026-10-20
**Contexto:** As Instrucoes sao lidas em TODA mensagem e existem em duas copias: o arquivo do repositorio e o painel do Projeto no claude.ai. A versao viva estava em v1.74.0 e carregava tres linhas revogadas pelo kit — «sempre que o usuario sinalizar upload» (v1.90.0), «Ritual de inicio de sessao» (v1.106.0) e «arquivo novo para baixar... nunca blocos soltos» (v1.106.0) —, as tres dirigindo comportamento a cada turno.

**Decisao:** Adotada a forma v1.127.0, preservando integralmente o que e deste projeto: «O que e», a regra de dominio inviolavel, o bloco «Dominio (Suno)» e a lista compacta de arquivos de contexto. Fica registrado que **a fonte e o arquivo do repositorio**: mudanca nas Instrucoes muda primeiro o arquivo versionado, e o fecho do turno pede ao dono que cole o conteudo no painel do Projeto. O tamanho sai de `wc -m` medido no turno, nunca de numero gravado em documento.

**Consequencias:** (+) O ritual passa a ser por turno, com leitura barata e verificavel (`git log -3`, `git status`, pasta-pai). (+) A divisao de escrita (DEC-010) e o teste do falso positivo (FIX-003) ficam a vista em todo turno. (+) 6.386 caracteres, com folga de ~1.060 sobre o teto aplicavel de 7.450 (6.900 padrao + 550 do modo Code). (−) **As duas copias ficam divergentes ate o dono colar a nova no painel do Projeto** — e, enquanto isso, o painel continua mandando as tres linhas revogadas. E a pendencia mais urgente desta fatia. (−) A regra «entregue o git commit pronto» mudou de forma: havendo WO no turno, o bloco e de quem aplica.
```

## Edicao 2 — `meta/STATUS.md` · atualizar o agora

A cargo do `/wrap`, em **append**. **Ancora:** a linha 10, `## Última sessão (2026-10-20, kit v1.127.0 — fatias 1 e 2)` — o bloco das fatias 1 e 2 **tem de continuar no arquivo**, e o da auditoria de 2026-07-21 tambem (titulo: `## Última sessão (2026-07-21, auditoria)`). Conte os dois antes e depois.

**Dois valores ANTIGOS a atualizar no arquivo INTEIRO, nao so no bloco novo** (a skill `/wrap` manda procurar todas as ocorrencias):

- A linha 13 do STATUS diz `Pendente do kit: meta/CEREBRO.md + INSTRUCOES-DO-PROJETO.md (fatia 3, fusão — os dois ainda carimbados/escritos no v1.74.0)`. **Deixou de ser verdade.** Atualize para refletir que a fatia 3 foi aplicada.
- A linha 14 declara `52 ocorrências ... das quais 3 corrigidas nesta fatia`. Remedido pelo chat **depois** da fatia 3, com o mesmo comando:

```
grep -rnoiE "sess(ão|ao|ões|oes)" meta/ CLAUDE.md INSTRUCOES-DO-PROJETO.md README.md .claude/ .gitignore .flatdropignore logs/ | wc -l
-> 46
```

O total caiu de 52 para 46 — e as 46 incluem **13 ocorrencias novas**, criadas pelas proprias WOs 0002/0003/0004 e pelo `_TEMPLATE.md`, que sao relato e nao se corrigem. Excluindo `logs/`, `meta/workorders/` e `.claude/skills/` (todas relato, ou texto verbatim do kit v1.127.0), **restam 19 ocorrencias em 8 arquivos**, assim:

| Arquivo | Ocorrencias | Natureza |
|---|---|---|
| `meta/CEREBRO.md` | 3 | **Legitimas** — vem do kit v1.127.0 verbatim: duas de relato («custou uma sessao», «servidor esquecido entre sessoes») e uma de **contraste deliberado** («nao e cerimonia de inicio de SESSAO: e de TURNO»). |
| `meta/DECISIONS.md` | 4 | **Legitimas** — relato historico (DEC-008) e o texto de DEC-009, que e decisao registrada: reescrever falsificaria o registro. |
| `meta/STATUS.md` | 4 | 2 sao titulos `## Última sessão` (**a corrigir** — o template novo usa «Última conversa»); 2 sao relato. |
| `meta/CONTEXT.md` | 2 | **Legitimas** — dominio (`localStorage`, «persistencia de sessao» do navegador) e um comentario de arvore. |
| `meta/IDEAS.md` | 2 | **Legitimas** — relato datado. |
| `README.md` | 2 | **Legitimas** — dominio (marcacoes da sessao do navegador) e comentario de arvore. |
| `meta/ROADMAP.md` | 1 | **Legitima** — dominio («sessao de geracao no Suno»). |
| `meta/CHANGELOG.md` | 1 | **Legitima** — relato datado. |

Escreva no STATUS: **ocorrencias varridas 46, corrigidas nesta fatia 20 (CEREBRO 11, Instrucoes 3, LOG-TEMPLATE 6), legitimas e justificadas 17, a corrigir 2** (os dois titulos `## Última sessão` do proprio STATUS, que viram `## Última conversa` na fatia 4). Declare a varredura **PENDENTE**, nao encerrada — e nao conserte os titulos agora: renomear titulo de bloco do STATUS enquanto esta WO insere outro bloco e justamente o caso que a skill `/wrap` manda contar antes.

Nao mexa na linha 6 (`**Versão atual:** 0.4.1 ...`): esta fatia nao muda a versao do produto.

## Edicao 3 — `meta/IDEAS.md` · tres itens de feedback ao kit

O CEREBRO manda registrar feedback ao kit **na hora**, e esta fatia produziu tres achados sobre o proprio KCM.

**Ancora:** o ULTIMO item da secao `## Feedback para o Kit`, citado no cabecalho (o que comeca com `- **[2026-07-19] Raia chat×Code confirmada na prática.**`). Insira DEPOIS dele.

**Texto a inserir, literal:**

```
- **[2026-10-20] O manifesto do v1.127.0 conta 4 carimbos de versao; sao 5.** O texto diz «o CEREBRO, o modelo de WO e as duas skills», mas o pacote traz carimbo tambem em `sondar.SKILL__template-update.md`. O texto nao acompanhou a chegada da terceira skill. Medido: `grep -o "Kit de Contexto Universal v[0-9.]*"` nos arquivos do pacote devolve 5.
- **[2026-10-20] Natureza `fusao` pode ser falso positivo, e custa caro quando e.** O manifesto marca CEREBRO e INSTRUCOES como `fusao`, o que faz o merge comecar pressupondo redacao propria a preservar. Neste projeto o CEREBRO nao tinha nenhuma: 20 das 192 linhas divergiam, todas texto do kit antigo. Sugestao ao kit: ensinar a **medir** a divergencia antes de escolher o metodo (comparacao normalizada linha a linha), porque o metodo de fusao paragrafo a paragrafo custa muito mais e, quando o arquivo nao evoluiu, chega ao mesmo resultado. O caso oposto tambem existe — as Instrucoes DESTE projeto eram fusao de verdade.
- **[2026-10-20] A varredura de linhas revogadas cria ocorrencias novas enquanto corrige as antigas.** As WOs e os relatorios que documentam a correcao citam o termo revogado para explica-lo, e entram na contagem seguinte como se fossem divida. A contagem total sobe ou cai pouco, e parece que o trabalho nao andou. Sugestao: o manifesto pedir a contagem **por natureza** (manda / relata / dominio / contraste / meta-documentacao da propria correcao), nao so o total — e dizer que o alvo e zero na primeira classe, nao no total.
```

## Fora de escopo

- `meta/CONTEXT.md` (linha 50 ainda cita `specs/`), `meta/CHANGELOG.md`, `meta/ROADMAP.md`, `meta/GLOSSARY.md`, `meta/HISTORY.md`, `README.md`, `meta/SPEC.md` (nao existe) — **fatia 4**.
- Apagar a pasta morta `meta/specs/` e seu `.gitkeep`.
- Renomear os dois titulos `## Última sessão` do STATUS para `## Última conversa` — fatia 4, pelo motivo dito na Edicao 2.
- As 17 ocorrencias classificadas como legitimas na tabela acima. **Nao as troque.**
- O `album-referencias.json` e a pergunta de 17/10.

## Armadilhas desta WO

- **O `meta/CEREBRO.md` triplicou de tamanho.** O `git diff` vai ser enorme e isso e esperado: o arquivo foi substituido, nao editado. Confira a forma pelos marcadores de modo e pelo carimbo (checagens 1-4), nao lendo o diff inteiro.
- **As Instrucoes tem DUAS copias e esta WO versiona so uma.** O arquivo do repo e a fonte; o painel do Projeto no claude.ai continua com a versao v1.74.0 ate o dono colar a nova. **Registre isso no relatorio como pendencia do dono**, com estas palavras: «o painel do Projeto ainda manda as tres linhas revogadas». Nao e algo que o Code resolve.
- **O `meta/LOG-TEMPLATE.md` esta no `git add` e nao foi pedido pelo usuario.** Ampliacao declarada na secao 2. Se o dono preferir reverte-lo, e `git checkout meta/LOG-TEMPLATE.md` antes do commit — mas aí a skill `/wrap` fica lendo um molde que contradiz a DEC-010.
- **Fim de linha:** os tres arquivos foram gravados em LF pelo chat. Os relatorios anteriores viram avisos LF→CRLF no `add`; se voltarem, registre, nao conserte.
- **O `grep` de cadencia precisa de `LC_ALL=C.UTF-8`** no shell do chat para a classe acentuada casar. Se a sua contagem divergir de 46, confira o locale antes de concluir divergencia — foi um falso negativo real no inicio deste merge.

## Depois de aplicar — conferencia antes do commit

| # | Checagem | Comando | Esperado |
|---|---|---|---|
| 1 | Carimbo do CEREBRO atualizado | `grep -o "Kit de Contexto Universal v[0-9.]*" meta/CEREBRO.md` | `v1.127.0` |
| 2 | Os quatro carimbos do projeto concordam | `grep -rho "Kit de Contexto Universal v[0-9.]*" meta/CEREBRO.md meta/workorders/_TEMPLATE.md .claude/skills/ \| sort \| uniq -c` | `5 ... v1.127.0` (CEREBRO + modelo de WO + 3 skills) |
| 3 | Marcador do modo Code presente | `grep -c "^## Ao final da conversa, o assistente REGISTRA o que falta" meta/CEREBRO.md` | `1` |
| 4 | Marcadores de ASU e compartilhado ausentes | `grep -c "Saida de codigo via ASU\|Projeto em grupo (HUB compartilhado)" meta/CEREBRO.md` | `0` |
| 5 | A secao propria do projeto esta preenchida | `grep -c "^## Técnicas específicas deste projeto" meta/CEREBRO.md` e `grep -c "_(vazio —" meta/CEREBRO.md` | `1` e `0` |
| 6 | As tres especializacoes entraram | `grep -c "registrada em DEC-010" meta/CEREBRO.md`, `grep -c "scripts/validate.py" meta/CEREBRO.md`, `grep -c "FIX-002 → FIX-003" meta/CEREBRO.md` | `1`, **`2`**, `1`. O `validate.py` aparece duas vezes de proposito — em «Tecnicas especificas» e em «Ambiente» da raia Code. **A previsao inicial desta celula dizia `1` e estava errada**, pelo motivo que o modelo de WO descreve: contagem simulada de cabeca sobre texto que a propria edicao insere. |
| 7 | Nenhuma referencia ao formato antigo | `grep -c "apply-spec\|meta/specs\|asuNNNN" meta/CEREBRO.md INSTRUCOES-DO-PROJETO.md meta/LOG-TEMPLATE.md` | `0` em cada |
| 8 | Instrucoes: o dominio sobreviveu | `grep -c "^## Regra de domínio inviolável" INSTRUCOES-DO-PROJETO.md`, `grep -c "^## Domínio (Suno) — sempre lembrar" INSTRUCOES-DO-PROJETO.md`, `grep -c "^## O que é" INSTRUCOES-DO-PROJETO.md` | `1` cada |
| 9 | Instrucoes: teto medido | `wc -m INSTRUCOES-DO-PROJETO.md` | `6386` (teto aplicavel 7.450) |
| 10 | Instrucoes: linhas revogadas foram | `grep -ciE "sess(ão\|ao)\|nome de download\|blocos soltos\|sinalizar upload" INSTRUCOES-DO-PROJETO.md` | `0` |
| 11 | LOG-TEMPLATE sem cadencia, com a nota do projeto | `grep -ciE "sess(ão\|ao)" meta/LOG-TEMPLATE.md` e `grep -c "DEC-010" meta/LOG-TEMPLATE.md` | `0` e `1` |
| 12 | Varredura geral, total | `LC_ALL=C.UTF-8 grep -rnoiE "sess(ão\|ao\|ões\|oes)" meta/ CLAUDE.md INSTRUCOES-DO-PROJETO.md README.md .claude/ .gitignore .flatdropignore logs/ \| wc -l` | **`67`**, medido pelo chat com esta WO ja no disco. Dos 67, **21 estao DENTRO desta WO** (ela cita o termo para explica-lo) — confira com `grep -oiE ... meta/workorders/261020-wo0004-*.md \| wc -l` → `21`, e `67 - 21 = 46` e o estado do resto do repo. **O numero previsto era 46 e estava errado pela razao que o modelo de WO descreve:** a contagem foi simulada antes de a propria WO existir, e `grep -c` (15 linhas) nao e `grep -o` (21 ocorrencias). O log do dia pode ainda somar algumas. |
| 13 | As DEC entraram uma vez so, e as anteriores ficaram | `grep -c "^## DEC-013" meta/DECISIONS.md`, `grep -c "^## DEC-014" meta/DECISIONS.md`, `grep -c "^## DEC-01[0-2]" meta/DECISIONS.md` | `1`, `1`, `3` |
| 14 | Os tres itens de feedback entraram | `grep -c "^- \*\*\[2026-10-20\]" meta/IDEAS.md` | `3` |
| 15 | Os dois blocos antigos do STATUS sobreviveram | `grep -c "^## Última sessão (2026-07-21, auditoria)" meta/STATUS.md` e `grep -c "^## Última sessão (2026-10-20, kit v1.127.0" meta/STATUS.md` | `1` e `1` |
| 16 | Nenhum relatorio `.txt` dentro do repo | `GIT_OPTIONAL_LOCKS=0 git status --short \| grep -c '\.txt'` | `0` |

**Os tres campos de cada passo:** todos sao rodados por **quem aplica (o Code)**, na raiz do repo (`C:\Users\alexk\Tools\cancioneiro\cancioneiro`), em Git Bash. **O que nenhum deles responde:** se o CEREBRO novo de fato dirige melhor o trabalho — isso so os proximos turnos mostram —, e se o painel do Projeto foi atualizado, que e gesto do dono e nao esta no disco.

## Relatorio de aplicacao

Grave em `../261020-HHMM-code-fatia3-kit-apply-wo0004.txt`, com o `HHMM` de `date +%y%m%d-%H%M` rodado na hora. Inclua a pendencia do painel do Projeto como item proprio, nao como nota de rodape.

**Proximo comando** (ultima linha do relatorio, cru e sozinho):

```
/sondar meta/CONTEXT.md meta/STATUS.md meta/IDEAS.md meta/ROADMAP.md README.md
```

## Commit

```
git add meta/CEREBRO.md INSTRUCOES-DO-PROJETO.md meta/LOG-TEMPLATE.md meta/DECISIONS.md meta/STATUS.md meta/IDEAS.md meta/workorders logs
```

```
git commit -m "docs: aplica fatia 3 do kit v1.127.0 (CEREBRO e Instrucoes)" -m "CEREBRO adotado do template v1.127.0 com tres especializacoes: secao Tecnicas especificas deste projeto preenchida, remissao a DEC-010 na divisao de escrita, e a nota de que nao ha build. Instrucoes fundidas preservando O que e, a regra de dominio inviolavel e o bloco Dominio (Suno); saem as tres linhas revogadas. LOG-TEMPLATE alinhado a cadencia de turno e a DEC-010. Registra DEC-013 e DEC-014 e tres itens de feedback ao kit."
```

```
git push
```
