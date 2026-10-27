# DECISIONS.md — Cancioneiro

> Por que as coisas são como são. Decisões de arquitetura (DEC) e bugs graves resolvidos (FIX).
> Cresce devagar. Formato ADR: contexto, decisão, alternativas, consequências.

---

## DEC-001 — JSON canônico como fonte de verdade; Markdown como export

**Data:** 2026-07-19
**Contexto:** Os chats hoje entregam cada canção em `.md` com convenção livre, e cada álbum inventou a sua (`[ESTILO SUNO]`, `[LETRA]`, `[VAR A]`, emojis de bandeira, tabelas diferentes). Para a ferramenta fazer copy-por-campo, marcar "já copiado", trocar módulos de estilo e filtrar por bloco, ela precisa de **campos discretos e nomeados**, não de prosa formatada.

**Decisão:** O dado canônico do acervo é **JSON** validável por JSON Schema. Os chats passam a gerar nesse esquema. O **Markdown** deixa de ser entrada e vira **export** gerado pela ferramenta (uma canção, um álbum, ou tudo), para quem precisa do formato legível (colar num chat, subir num Projeto, ler humano).

**Alternativas consideradas:**
- *MD com front-matter YAML por canção:* legível, mas o corpo (style/lyrics) ainda seria texto livre a parsear, e o front-matter não cobre bem estruturas aninhadas (variantes, módulos). Meio-termo que herda a fragilidade do parser.
- *Parser universal de MD:* tentaria ler os álbuns antigos direto. Rejeitado: convenções divergentes tornam o parser um poço de exceções (é a causa da bagunça, não a solução).

**Consequências:** (+) Elimina ambiguidade na raiz; a ferramenta lê campos, não adivinha. (+) Um contrato único para todos os chats. (−) Converter o acervo existente é trabalho semi-manual/assistido, não automático. (−) JSON é menos amigável de editar à mão que MD — mitigado pela ferramenta e pelo export MD.

---

## DEC-002 — Ferramenta em HTML+JS single-file (sem framework, sem build)

**Data:** 2026-07-19
**Contexto:** Uso pessoal em Windows, copiar-colar rápido enquanto se gera música no Suno. O usuário não quer manter ambiente de dev (Node/Python) só para rodar a ferramenta.

**Decisão:** A ferramenta é **um único `app/index.html`** com JS vanilla e CSS embutido. Abre com duplo-clique no navegador, sem servidor, sem instalação, sem passo de build.

**Alternativas consideradas:**
- *Python (CLI/script):* exigiria Python instalado e não dá interface visual de cartões/botões naturalmente. Rejeitado para a ferramenta principal (pode voltar como utilitário de conversão em lote, se necessário).
- *App com framework (React/Vue) + build:* mais poder, mas introduz toolchain, `node_modules`, passo de build — contra o requisito de zero setup. Reavaliar só se a complexidade da UI crescer muito (ROADMAP).

**Consequências:** (+) Zero fricção de execução no Windows. (+) Portável (um arquivo). (−) Sem ecossistema de componentes; UI feita à mão. (−) Limite prático de complexidade antes de doer — aceitável para o escopo atual.

---

## DEC-003 — Nome "cancioneiro" (agnóstico de plataforma)

**Data:** 2026-07-19
**Contexto:** Nome vira raiz do repo e prefixo dos meta. O usuário pediu explicitamente algo não amarrado a "Suno", já que a ferramenta pode servir para outras plataformas de geração (Udio etc.) e o foco é *criar/compor/organizar canções*.

**Decisão:** **`cancioneiro`** — palavra portuguesa para coletânea de canções. Descreve o que a ferramenta faz (reúne e organiza canções) sem citar marca.

**Alternativas consideradas:** `suno-forge`, `suno-deck` (rejeitados: prendem à marca Suno); `cancioneiro` venceu por ser agnóstico e evocativo.

**Consequências:** (+) Sobrevive a troca de plataforma-alvo. (+) Nome curto e memorável. (−) Menos "descobrível" por quem busca "suno tool" — irrelevante para uso pessoal.

---

## DEC-004 — Dado canônico em arquivo versionado, nunca em localStorage

**Data:** 2026-07-19
**Contexto:** A pesquisa mostrou ferramentas concorrentes que guardam a biblioteca no `localStorage` do navegador. Isso significa perder tudo ao limpar o navegador ou trocar de máquina.

**Decisão:** O acervo real vive em **arquivo JSON versionado** (`data/`). A ferramenta **importa** o JSON e **exporta** o JSON/MD; o `localStorage` guarda apenas **estado efêmero** (marcações de "já copiei" da sessão, filtros ativos). Fonte de verdade = arquivo, sempre.

**Alternativas consideradas:** *localStorage como store principal* (rejeitado: frágil, não versionável, não compartilhável entre máquinas). *IndexedDB* (mais robusto que localStorage, mas ainda preso ao navegador; mesmo problema de fundo).

**Consequências:** (+) Acervo sobrevive a limpeza de navegador e é versionável no Git. (+) Portável entre máquinas. (−) Exige um passo explícito de import/export (não "salva sozinho") — mitigável com um botão de "baixar JSON atualizado" bem visível.

---

## DEC-005 — Adaptação das Instruções do Projeto ao nicho música/ferramenta

**Data:** 2026-07-19
**Contexto:** As Instruções do Projeto vêm do Kit no nicho "Desenvolvimento" genérico. Este projeto é dev, mas com um domínio específico (prompts de IA de música) que tem armadilhas próprias.

**Decisão:** Manter a base de Desenvolvimento (é um repositório de código real) e acrescentar, quando as Instruções forem refinadas, a regra específica do domínio: *"conteúdo copiável para o Suno nunca leva rótulo de referência dentro do bloco"*. Registrado também em «Feedback para o Kit» no IDEAS. Refino das Instruções fica para quando a ferramenta existir e o padrão de trabalho se firmar (evitar encurtar cedo demais).

**Consequências:** (+) Instruções permanecem fiéis ao processo enquanto o projeto amadurece. (−) Ainda genéricas por ora — aceitável na fundação.

---

## DEC-006 — Hospedagem em GitHub Pages + carregamento auto-detectado (fetch/import)

**Data:** 2026-07-19
**Contexto:** A ferramenta e um `index.html`. Aberta por duplo-clique (`file://`), o navegador PROIBE `fetch` de arquivos locais (trava de seguranca) — entao ela nao consegue ler `data/*.json` sozinha nesse modo. Servida por `http(s)://` (GitHub Pages), o `fetch` funciona. O usuario ja versiona no GitHub e quer o fluxo mais pratico.

**Decisao:** Publicar no **GitHub Pages** como fluxo principal (abrir um link, funciona em qualquer maquina, ate no celular). A ferramenta **auto-detecta o ambiente**: se servida por http(s), carrega `data/demo.json` sozinha (tenta `data/` e `../data/`); se em `file://`, pula o fetch e espera import manual. Em qualquer modo, os botoes "Importar .json" e "Baixar .json" estao sempre disponiveis. Um `index.html` na raiz redireciona para `app/index.html` (URL limpa no Pages).

**Alternativas consideradas:**
- *Vercel/Netlify:* servem para apps com build. Nosso HTML estatico nao precisa — seria toolchain a mais. Rejeitado.
- *So import manual (sem fetch):* funcionaria em file://, mas joga fora a conveniencia de "abrir o link e o acervo ja esta la" no Pages. O modo hibrido cobre os dois sem custo.

**Consequencias:** (+) Fluxo principal e so abrir um link; funciona multiplataforma. (+) Modo local (offline, file://) segue funcionando via import. (−) Trocar o acervo padrao exige commit no repo (coerente com DEC-004: JSON versionado e a fonte). (−) O caminho do acervo padrao (`demo.json`) esta fixo no codigo — trocavel por import ou editando uma linha.

---

## DEC-007 — Categorias de modulo espelham as cinco camadas audiveis

**Data:** 2026-07-19
**Contexto:** O guia do usesuno.com consolida um modelo de prompt em **cinco camadas audiveis** (musical lane, motion, sound sources, voice/lead, production space) + andamento. E um modelo mais forte e testavel que as categorias ad-hoc que o esquema tinha na fundacao (mood/instrument/vocal/genre/tempo soltos).

**Decisao:** As `category` dos modulos de estilo passam a espelhar essas camadas: `genre` (lane), `motion` (movimento/pulso), `instrument` (fontes), `vocal` (voz/lead), `mood` (clima), `production` (espaco de mix), `tempo` (andamento). A ferramenta agrupa os chips por camada nessa ordem. A biblioteca-semente foi expandida de 14 para 27 modulos cobrindo as camadas.

**Alternativas consideradas:** *Manter categorias livres* (rejeitado: sem modelo, a biblioteca vira bag desorganizada). *Copiar a taxonomia de genero de 10 categorias do usesuno* (adiado: util para submenu de genero na Fase 3, nao para as camadas de composicao).

**Consequencias:** (+) Menu de troca organizado por decisao audivel, alinhado a um modelo testado. (+) Ensina o usuario (e os chats) a pensar em camadas. (−) Modulos antigos precisam de category valida — ja migrados.

---

## FIX-001 — Caminho relativo do fetch quebrava com o app em subpasta

**Data:** 2026-07-19
**Sintoma:** Teste local (http.server) mostrou que o app em `app/index.html` buscando `data/demo.json` resolvia para `app/data/demo.json` (inexistente) — o auto-load falhava no GitHub Pages, onde o app fica em `/app/`.
**Causa raiz:** Caminho relativo unico e fragil; nao considerava a profundidade da pasta do app.
**Solucao:** O auto-load tenta uma lista de caminhos candidatos (`data/demo.json` e `../data/demo.json`), adotando o primeiro que responder 200. Validado com servidor local nos dois layouts.
**Licao:** Testar o fetch no layout real de deploy (app em subpasta) antes de assumir que "funciona local". O teste pegou o bug antes da entrega.

---

## DEC-008 — Entrega sem duplicatas: os arquivos que mudaram, uma vez so

**Data:** 2026-07-19 (revisada 2026-07-21 apos falha real)
**Contexto:** Eu entregava o repo como .zip E TAMBEM repetia arquivos-chave soltos via present_files. Como os soltos ja estavam dentro do zip, viravam duplicata confusa. A primeira versao desta decisao dizia "entregar por git diff + commit, sem zip nem soltos" — e isso FALHOU na pratica: numa sessao seguinte implementei o export MD, commitei no repo do meu ambiente e nao entreguei arquivo nenhum, dizendo ao usuario para "sincronizar". Nao existe sincronizacao entre o ambiente do assistente e a maquina do usuario: o repo do ambiente e descartavel. O usuario ficou uma versao atras sem saber.

**Decisao:** Entregar SEMPRE os arquivos que mudaram, **uma vez so**:
- Poucos arquivos alterados -> entregar os arquivos direto (present_files), sem zip.
- Muitos arquivos / arvore nova -> entregar o zip, e NAO repetir arquivos soltos junto.
- Nunca os dois ao mesmo tempo. Nunca dizer "sincronize" ou "puxe do repo": o repo do ambiente NAO chega ao usuario sozinho.
- O comando de `git commit` continua sendo entregue, para o usuario aplicar no repo dele.

**Consequencias:** (+) O usuario sempre recebe o que foi produzido. (+) Sem duplicata confusa. (−) Exige julgar "poucos vs muitos" a cada entrega — regra simples: se cabe em ~4 arquivos, entrega direto.

**Licao:** uma regra de higiene (menos ruido) nunca pode custar a entrega em si. Verificar "o usuario consegue OBTER o que eu produzi?" antes de fechar a resposta.

---

## FIX-002 — Duplicacao de conceitos no Style recomposto

**Data:** 2026-07-21
**Sintoma:** Com modulos ligados, o Style recomposto terminava repetindo conceitos ja presentes na base. Visivel no print do usuario: `...no vocals, dark ambient cinematic, solo cello, dark` — sendo que a base ja dizia "dark ambient cinematic intro", "solo cello descending melody" e "ominous".
**Causa raiz:** O dedup comparava apenas strings IDENTICAS. Como o fragmento do modulo ("dark ambient cinematic") e um SUBCONJUNTO do item da base ("dark ambient cinematic intro"), a comparacao exata nao pegava, e o fragmento entrava de novo.
**Impacto:** Prompt poluido no Suno; desperdicio das primeiras ~20-30 palavras, que sao as que mais pesam.
**Solucao:** Dedup **por contencao**: um fragmento e descartado se ja esta contido em algum item presente, ou se contem algum. Validado com 8 checks, incluindo "nenhuma redundancia por contencao em nenhuma faixa" e "ligar modulo novo ainda adiciona".
**Licao:** Ver a ferramenta rodando (print do usuario) revelou em segundos um bug que os testes de logica nao pegavam, porque o teste checava duplicata EXATA — o mesmo criterio errado do codigo. Teste que espelha a premissa do bug nao encontra o bug.

---

## FIX-003 — Falso positivo no dedup do Style (substring vs palavra)

**Data:** 2026-07-21
**Sintoma:** O dedup por contencao introduzido no FIX-002 descartava fragmentos legitimos. Casos reais: com "male vocals" na base, o modulo "female vocals" era silenciosamente descartado (porque "male vocals" e substring de "female vocals"); com "harpsichord lead" na base, o modulo "harp" era barrado.
**Causa raiz:** A comparacao usava substring cru (`a.includes(b)`), que ignora fronteira de palavra. Duas palavras diferentes podem conter uma a outra como sequencia de caracteres sem terem relacao semantica.
**Impacto:** Silencioso e pior que o bug original — o usuario ligava um modulo e ele simplesmente nao aparecia, sem explicacao. Vocal feminino sendo barrado por vocal masculino e um caso que aconteceria na pratica.
**Solucao:** Comparar **sequencias de palavras**: um fragmento e redundante se sua sequencia de palavras aparece inteira e contigua em outro (ou vice-versa). Plural simples normalizado ("pads" ~ "pad") para nao reintroduzir duplicata por causa do -s. Validado com 14 checks: 3 de falso positivo corrigido, 4 de dedup legitimo preservado, 7 de regressao do FIX-002.
**Licao:** Ao corrigir um bug de comparacao, testar explicitamente o **falso positivo** (o que NAO deve ser barrado), nao so o caso que motivou a correcao. O FIX-002 so testava "nao duplica"; faltava "nao barra o que e diferente".

---

## DEC-009 — Pensamento estendido ligado nas sessoes de trabalho deste projeto

**Data:** 2026-07-21
**Contexto:** O dono identificou que as conversas anteriores rodaram com o pensamento estendido DESLIGADO, e observou que era a causa dos problemas de desenvolvimento `[relatado pelo dono, 2026-07-21]`. A evidencia apoia: com pensamento desligado ocorreram (a) a falha de entrega da 0.4.0 — implementei e commitei no ambiente do assistente sem entregar arquivo, mandando o dono "sincronizar" algo que nao sincroniza; (b) o FIX-002 introduzindo o falso positivo do FIX-003, com teste que espelhava a premissa errada do codigo.

**Decisao:** Sessoes de trabalho deste projeto rodam com **pensamento estendido LIGADO**. O projeto envolve decisao de arquitetura, analise de dominio (Suno) e correcao de logica com armadilhas sutis — as tres coisas degradam sem raciocinio explicito.

**Consequencias:** (+) Menos erro de reflexo e menos retrabalho. (+) Auditorias e correcoes de comparacao ficam confiaveis. (−) Respostas um pouco mais lentas — custo aceitavel diante do retrabalho evitado.

---

## DEC-010 — Divisao de escrita entre chat e Code (um dono por documento)

**Data:** 2026-10-20
**Contexto:** O fluxo mudou: o chat agora le e grava na pasta do projeto (pasta vinculada no app desktop), em vez de receber uma copia achatada. O meio deixou de impedir dois escritores no mesmo arquivo — antes o mount impedia; agora so a regra impede.

**Decisao:** Adotado o padrao do kit. O **chat** escreve inteiros: a analise, a WO, `meta/CONTEXT.md`, `meta/CEREBRO.md`, `INSTRUCOES-DO-PROJETO.md` e `meta/GLOSSARY.md`. O **Code** escreve: o codigo, `meta/STATUS.md`, `meta/DECISIONS.md`, `meta/CHANGELOG.md` e a sua secao do log do dia. `meta/IDEAS.md` e todo documento grande e vivo mudam por WO.

**Consequencias:** (+) Fim da ambiguidade sobre quem reescreve o que. (+) Commit e push ficam numa raia so (Code); o git pelo chat e apenas leitura, com `GIT_OPTIONAL_LOCKS=0`. (−) Mudanca em documento do Code passa a exigir WO, o que custa um artefato a mais por ciclo.

---

## DEC-011 — Merge do kit v1.127.0 em fatias; fatia 1 aplicada

**Data:** 2026-10-20
**Contexto:** O projeto estava no kit v1.74.0 contra um pacote v1.127.0. Aplicar 53 versoes de uma vez significa rodar o merge inteiro sob as regras velhas que o proprio pacote veio corrigir.

**Decisao:** O merge vai em fatias. **Fatia 1 (esta):** `.claude/settings.json` (as duas correcoes obrigatorias) e as tres skills do modo Code — `apply-wo`, `wrap`, `sondar` —, mais o modelo de WO. A `apply-spec` sai. Fatias seguintes: `CLAUDE.md` + arquivos de exclusao; depois `CEREBRO.md` + `INSTRUCOES-DO-PROJETO.md` (fusao); depois os `meta/` restantes e a varredura de linhas revogadas.

**Consequencias:** (+) `Write` e `additionalDirectories` consertados: criar log e gravar relatorio na pasta-pai param de pedir aprovacao a cada arquivo. (+) O carimbo de versao passa a dizer v1.127.0 nas skills e no modelo de WO. (−) O `meta/CEREBRO.md` continua carimbado v1.74.0 ate a fatia de fusao — divergencia conhecida e temporaria. (−) `CLAUDE.md` e `meta/CEREBRO.md` ainda citam `meta/specs/` e `/apply-spec`; corrigir e da fatia 2.

---

## DEC-012 — `.flatdropignore` na forma "pasta/*", e o canal achatado vira reserva

**Data:** 2026-10-20
**Contexto:** O `.flatdropignore` usava `logs/` e `meta/specs/` — a forma que PODA o diretorio antes de descer. Nessa forma um `!` dentro da pasta nunca chega a ser avaliado, entao o modelo de WO versionado na fatia 1 nao subia ao Projeto. A pasta `meta/specs/` tambem ficou morta quando a skill `apply-spec` saiu.

**Decisao:** Regra de exclusao usa `pasta/*` (o conteudo), nunca `pasta/` (a pasta), e modelo de pasta ignorada exige o PAR completo — a linha do conteudo seguida da linha `!pasta/_TEMPLATE.md`. As regras moram dentro do bloco do editor do FlatDrop; explicacao fica acima dele, nunca dentro. Fica registrado que o canal principal deste projeto e a pasta vinculada (o chat le e grava no disco) e que o `.flatdropignore` so vale no canal de reserva.

**Consequencias:** (+) `meta/workorders/_TEMPLATE.md` volta a subir ao Projeto; o corpo das WOs aplicadas, nao. (+) `.claude/settings.local.json` passa a ser ignorado pelo git, em vez de ficar untracked indefinidamente. (−) `meta/specs/` continua no disco com um `.gitkeep` orfao — remover e de uma fatia seguinte, junto com as citacoes a ela no `meta/CEREBRO.md` e no `meta/CONTEXT.md`.

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

---

## DEC-015 — Os meta/ especializados nao sao substituidos pelo template; a pasta `meta/specs/` morre

**Data:** 2026-10-20
**Contexto:** Fatia 4 do merge do kit v1.127.0. Ao contrario das fatias 1-3, onde o template era mais novo que o arquivo vivo, aqui o vivo e mais rico em todos os sete arquivos comparados — o template traz esqueletos com placeholders (`[Nome do Projeto]`, `F1 — [Nome da fase]`). O manifesto ja prevê este caso: «template generico nao e candidato a substituir arquivo vivo refinado; os meta/ ja especializados caem por padrao em (c)». O CEREBRO v1.127.0 cita nominalmente o caso do IDEAS organizado por ID estavel como desvio legitimo. Separadamente: `meta/specs/` existia vazia desde 2026-07-20 e a skill que a lia saiu na fatia 1.

**Decisao:** `CONTEXT`, `STATUS`, `IDEAS`, `ROADMAP`, `GLOSSARY`, `HISTORY` e `CHANGELOG` **permanecem na forma deste projeto**. Do template entram apenas: o arquivo novo `meta/SPEC.md` (modelo de spec de feature, que o projeto nao tinha) e o eixo «Comandos / artefatos» no `GLOSSARY`. A pasta `meta/specs/` e **removida**; o modelo de spec mora em `meta/SPEC.md` e a pasta renasce quando a primeira spec for escrita — pasta nunca nasce para receber um modelo.

**Alternativas consideradas:** (a) adotar os templates e reinjetar o conteudo — descartada: seria regressao de forma, e o CEREBRO do proprio kit diz isso; (b) manter `meta/specs/` vazia «porque pode servir» — descartada: pasta vazia versionada com `.gitkeep` orfao e exatamente o estado que faz um assistente futuro procurar spec onde nao ha nenhuma, e foi o que aconteceu nesta semana.

**Consequencias:** (+) O funil fica completo: exploracao → sonda → analise/spec → WO → DECISIONS, com modelo para cada peca. (+) O vocabulario novo do kit entra no glossario, que e onde se procura. (+) A arvore do repositorio no `CONTEXT` e no `README` para de mentir. (−) `meta/analises/` ainda nao existe e o modelo dela nao entra (natureza `modelo-em-espera`): quando a primeira analise nascer, ha de vir do pacote. (−) Duas pastas do projeto passam a ser «nascem no primeiro uso», o que so funciona se estiver escrito — por isso a nota no `meta/SPEC.md` e no glossario.

---

## FIX-004 — O app gravava estado de interface dentro da colecao, e o download o serializava

**Data:** 2026-10-22
**Sintoma:** Importar um acervo baixado pela propria ferramenta mostrava «Arquivo invalido: nao e um JSON valido», sobre um arquivo cujo JSON era impecavel. O `album-referencias.json` do dono ficou cinco dias inutilizavel.

**Causa raiz:** `renderModules` gravava `song._activeModules = active` — um `Set` — dentro do objeto da cancao (linha 713). `JSON.stringify` nao serializa `Set`: grava `{}`. Na importacao seguinte, `recomposedStyle` lia `song._activeModules || new Set(...)` (linha 444); `{}` e truthy, o fallback nao rodava, e `{}.forEach` lancava `TypeError: active.forEach is not a function`. O ciclo era completo: o app sujava o arquivo que ele mesmo baixava e depois nao conseguia le-lo. Rodava no render de TODO cartao, nao so ao abrir o painel de modulos.

**Solucao:** O estado efemero dos modulos ligados passa a viver em `App.activeModules[song.id]`, fora da colecao. Alinha o codigo com o DEC-004, que ja dizia que o arquivo e a fonte de verdade e o estado efemero mora a parte — o app fazia o contrario. Medido numa copia antes de aplicar: download sai sem chave interna, reimport do proprio download OK, e o arquivo ja sujo do dono importa (22 cartoes). Teste do falso positivo: 27 chips, recomposto 174 → 191 ao ligar e 191 ao desligar, identico ao original (desligar nao encolhe e intencional — a base manda).

**Licao:** Dado de interface gravado no objeto canonico vaza na primeira serializacao. `Set` e `Map` agravam porque viram `{}` em vez de falhar: o defeito nao aparece onde nasce.

---

## FIX-005 — Um `catch` largo atribuia a qualquer falha a causa da primeira operacao

**Data:** 2026-10-22
**Sintoma:** Todo erro de importacao era relatado como «nao e um JSON valido», inclusive os que nada tinham a ver com parse. A mensagem mandou a investigacao de 2026-10-17 procurar defeito no arquivo durante cinco dias, enquanto o defeito estava no app.

**Causa raiz:** `importFromFile` envolvia tres operacoes num unico `try` — `JSON.parse`, `setCollection` (que carrega E renderiza) e o `toast` de sucesso — com um `catch` que nomeava a causa da primeira. Qualquer excecao do render chegava ao usuario como JSON invalido. `setCollection` ate tinha a propria mensagem para quando falta `albums`, mas e `toast` + `return`, nao `throw`: por isso o unico caminho que o `catch` de fato cobria era o que ele descrevia errado.

**Solucao:** Dois `try` separados. O do parse mantem a mensagem, que ali e verdadeira (medido: JSON realmente malformado continua dizendo «nao e um JSON valido»); o da carga reporta `e.message` e loga a excecao no console.

**A mesma classe, achada em outro arquivo na auditoria desta WO:** `scripts/validate.py` imprimia «Tudo conforme ao esquema.» mesmo rodando sem o pacote `jsonschema`, isto e, sem ter conferido esquema nenhum — ele avisa na PRIMEIRA linha e afirma conformidade na ULTIMA, que e a que se le. Medido no disco do dono em 2026-10-22: o pacote nao esta instalado, entao todo «verde» do instrumento ate aqui foi verde de sintaxe. Corrigido na mesma entrega: a mensagem final declara o modo, e o aviso se repete no fim.

**Licao:** mensagem que nomeia um resultado so pode ser escrita pela operacao que produz aquele resultado — vale para `catch` e para rodape de relatorio. Mesma familia do FIX-003: la um criterio de comparacao errado falhava em silencio; aqui uma mensagem erra sobre o que foi medido. Mensagem errada custa mais que erro mudo, porque desvia quem investiga: foram cinco dias no app e, no instrumento, um numero indeterminado de «OK» lidos como conformidade.

---

## DEC-016 — Acervo autossuficiente: cada colecao carrega os proprios modulos de estilo

**Data:** 2026-10-22
**Contexto:** `data/exemplo-cinzeiro.json` referenciava cinco modulos (`genre-dark-ambient`, `instr-solo-cello`, `mood-ominous`, `tempo-slow-70`, `vocal-none`) que nao existiam nele — medido: `refs=5 · indice=0`. Os cinco existem em `schema/style-modules.json`, mas `setCollection` monta `App.modulesById` so a partir da colecao carregada, entao os ids nao resolviam para fragmento nenhum, em silencio. O arquivo fora escrito supondo uma biblioteca compartilhada que o app nao carrega. Duas leituras com consertos opostos: biblioteca compartilhada (o arquivo esta certo, falta codigo) ou acervo autossuficiente (o arquivo esta incompleto, falta dado).

**Decisao:** **Acervo autossuficiente.** Toda colecao traz em `styleModules[]` os modulos que suas faixas citam, como `data/demo.json` (27) e o `album-referencias.json` (50) ja faziam. `schema/style-modules.json` passa a ser **biblioteca de referencia para autoria** — de onde se copia ao montar um acervo —, nao indice carregado em tempo de execucao. Um `.json` sozinho basta para reproduzir o prompt.

**Alternativas consideradas:** biblioteca compartilhada carregada pelo app — descartada: tornaria o acervo dependente de um segundo arquivo, contra o espirito do DEC-001 (o JSON e o dado canonico, completo em si).

**Consequencias:** (+) Um acervo e reproduzivel sozinho, inclusive fora deste repositorio. (+) A checagem de integridade referencial ganha semantica definida e entra no `validate.py`. (−) A biblioteca se duplica em cada acervo; quando um fragmento for corrigido na biblioteca, os acervos ja montados nao mudam sozinhos. Mitigacao aceita: a biblioteca e de autoria, nao de runtime — divergencia e esperada e registrada no proprio acervo.

---

## FIX-006 — A correcao do round-trip nao limpava a sujeira que ja estava nos arquivos

**Data:** 2026-10-23
**Sintoma:** Depois do FIX-004, o `album-referencias.json` voltou a abrir e o ciclo baixar→reimportar passou a fechar. Mas a conferencia na tela mediu o arquivo baixado e achou as 7 chaves `_activeModules` ainda la — entrada limpa produzia saida com 0, entrada ja suja produzia saida com 7.

**Causa raiz:** O FIX-004 parou de GRAVAR a chave; nao removeu a que ja existia. O app lia o JSON, nunca tocava em `_activeModules`, e a serializava de volta no download. Arquivo contaminado por uma versao antiga da ferramenta propagava a chave indefinidamente — e seguiria reprovando em `song.schema.json`, que tem `additionalProperties: false`.

**Solucao:** `stripInternalKeys(json)` na importacao, removendo recursivamente as chaves com prefixo `_` e **devolvendo quantas removeu**, informadas no proprio toast de sucesso. A contagem e metade da correcao: a `_activeModules` so foi descoberta porque um arquivo quebrou visivelmente, e saneamento mudo teria consertado o sintoma apagando o sinal — o proximo vazamento passaria despercebido. O saneamento roda FORA do `try` da carga, para o aviso nao ser engolido por uma mensagem de erro (seria o FIX-005 de novo, no mesmo arquivo).

**Licao:** Corrigir a causa nao limpa os dados que a causa ja produziu, e as duas coisas parecem uma so quando se olha o sintoma. Ao fechar um defeito que escreveu dado errado, medir **duas** perguntas: «para de acontecer?» e «o que ja aconteceu fica limpo?». A analise de 2026-10-21 mediu as tres opcoes so contra a primeira — e a propria tabela dela mostrava a opcao C passando num caminho que a recomendada nao cobria, coluna que foi lida como redundante.

---

## DEC-017 — Kit v1.131.0: a pasta vinculada passa a ser o canal declarado, e o achatado vira reserva

**Data:** 2026-10-24
**Contexto:** Quatro versoes menores depois do v1.127.0, com a tabela de linhas revogadas inalterada — nenhuma varredura nova. O que o pacote muda e a LINGUAGEM do canal: o v1.127.0 ainda descrevia o mount e o upload como caminho normal, com a pasta vinculada como novidade; o v1.131.0 inverte, e o FlatDrop passa a ser reserva declarada, inclusive no titulo da secao de transferencia. Na pratica isso reescreve ~15 pontos do CEREBRO: a abertura de turno vira `git log -3 --oneline` + `git status --short` + listar a pasta-pai; «peca que o usuario suba o arquivo» vira «verifique na pasta do projeto, na pasta-pai, ou ja colado»; «arquivo novo para baixar» vira «grava direto no lugar».

**Decisao:** Merge aplicado numa fatia so. `meta/CEREBRO.md` adota o template v1.131.0 com as tres especializacoes deste projeto reinjetadas — a secao «Tecnicas especificas», agora com oito itens; a remissao a DEC-010; e a nota de que nao ha build. `INSTRUCOES-DO-PROJETO.md` permanece na forma deste projeto (DEC-014), com duas linhas adotadas do template. `CLAUDE.md` **nao e tocado**: as 34 linhas de diferenca sao placeholders contra conteudo real, e a unica frase com informacao nova ja esta no CEREBRO. Modelo de WO e as tres skills adotados inteiros. Os cinco carimbos passam a dizer `v1.131.0`.

**Alternativas consideradas:** (a) fatiar como no merge anterior — descartada: quatro versoes de distancia nao justificam quatro fatias, e o custo de coordenar supera o risco; (b) adotar o `CLAUDE.md` do template e reinjetar — descartada pela regra do proprio manifesto: template generico nao e candidato a substituir arquivo vivo refinado.

**Consequencias:** (+) O CEREBRO deixa de descrever como normal um canal que este projeto usa so por excecao. (+) A regra de idempotencia por «texto novo INTEIRO» entra no modelo de WO e na `apply-wo` — ela corrige um modo de falha real da forma «trocar». (+) As duas licoes do FIX-004/006 ficam gravadas na secao que nenhum update futuro sobrescreve. (−) `CLAUDE.md` passa a ser o unico arquivo do pacote deliberadamente fora de sincronia com o template; o motivo esta aqui, para a proxima leitura nao o tratar como esquecimento.

---

## FIX-007 — O botao copiar entregava o Style de antes do clique no modulo

**Data:** 2026-10-24
**Sintoma:** Ligar ou desligar um chip de modulo mudava o Style mostrado no cartao, mas o botao «copiar» do Style continuava entregando o texto anterior. Medido em headless em ar-01: bloco de 298 para 322 caracteres ao ligar um chip, e o botao entregando os 298 antigos. O que se via nao era o que se colava no Suno.

**Causa raiz:** `fieldBlock` registrava `copyText(content, btn)`, com `content` capturado por closure no momento em que o cartao era montado. O clique no chip atualizava `pre.textContent` do bloco, mas nunca o `content` da closure. O export MD nao era afetado porque recompoe na hora — e por isso a divergencia nunca apareceu em nenhuma conferencia de arquivo.

**Solucao:** O botao le `pre.textContent` no momento do clique. Para todo campo que nao muda depois de criado (Lyrics, variantes), o texto e identico ao de antes — conferido byte a byte nos 27 botoes do album e nos 11 do demo.

**Licao:** Estado que a interface atualiza depois de criada nao pode ser lido de uma copia feita na criacao. O defeito era invisivel a qualquer instrumento que le arquivo, e so apareceu porque o painel de qualidade precisava que o numero mostrado e o texto copiado fossem o mesmo — o painel foi o primeiro codigo deste projeto a exigir isso, e por isso o primeiro a revela-lo. A funcao central dos modulos (i-004) estava quebrada no caminho mais usado desde o v0.

---

## DEC-018 — Painel de qualidade: mede o recomposto, so avisa, e o vermelho e reservado a perda

**Data:** 2026-10-24
**Contexto:** Fase 3a (i-017 a i-019). A spec `meta/specs/261024-painel-de-qualidade.md` mediu o acervo real contra os limites do Suno — reconferidos na web, porque o Suno lancou o v6 em 2026-09-09 e a nota oficial nao documenta limite nenhum; os numeros vem de fonte secundaria, com a forca de cada um declarada na spec.

**Decisao:** O painel mede o **Style recomposto** (o mesmo texto que o botao copia), atualiza a cada clique em chip, e mede tambem Lyrics e Exclude Styles. Os limites vivem num unico objeto `QUALITY_LIMITS`, com fonte e data em comentario. Tres niveis: verde, ambar («vai funcionar, mas pior») e vermelho **so para truncamento**, o unico caso que perde informacao — passar de 10 tags e ambar, nunca vermelho, porque dilui sem perder, e um vermelho em 7 de 7 faixas viraria ruido que leva junto o vermelho que importa. «no X» detectado por **fronteira de palavra** (substring casaria pia-no e sopra-no) e **so avisa**: a ferramenta continua so-leitura, como o DEC-004 manda. `no vocals` nao dispara em faixa **instrumental**, definida como Lyrics sem nenhuma linha de letra — o que cobre `[Instrumental]` e a faixa linear com tags de arco. O painel nunca bloqueia a copia.

**Alternativas consideradas:** (a) migrar o «no X» para o Exclude num clique — descartada pelo dono: seria a primeira vez que a ferramenta escreve no acervo, e pede analise propria; (b) definir instrumental como «Lyrics contem `[Instrumental]`» — descartada na implementacao: era a redacao literal da opcao aprovada, mas mais estreita que a intencao («nao dispara no instrumental»), e faria cinzeiro-01, que e instrumental, avisar `no vocals`; (c) alerta modal na hora de copiar — descartada: interrompe o gesto e se aprende a fechar sem ler; (d) i-020, aviso de ordem — adiado pelo dono: dispara em 0 de 10 faixas reais, com a evidencia mais fraca das quatro.

**Consequencias:** (+) O truncamento silencioso passa a ser visivel no unico ponto em que ainda se pode evitar. (+) A funcao central dos modulos volta a funcionar no botao (FIX-007). (+) Mudar um limite e mudar uma linha, sabendo de onde veio a anterior. (−) Os limites dependem de uma fonte que vende produto concorrente; reconferir quando a nota oficial do Suno os documentar. (−) O aviso de tags vai acender ambar em quase todas as faixas do album — e informacao verdadeira, mas e a que mais rapido vira paisagem; se isso acontecer, o sinal e o dono deixar de ler a linha, e o remedio e a sugestao de corte (3a.2), nao baixar o aviso.

---

## DEC-019 — Fase 3a.2: o custo de cada modulo aparece no chip; a ferramenta nao sugere o corte

**Data:** 2026-10-27
**Contexto:** A i-026 pedia «sugerir o que cortar quando ha tags demais». A medicao no app real (`meta/specs/261027-custo-dos-modulos.md`) mostrou tres coisas. (1) O style base nunca passa de 10 tags (7 a 10 nas dez faixas): o excesso vem 100% dos modulos, e a classificacao do base por camada que a i-026 dava como requisito nao e necessaria em nenhum caso real. (2) Os modulos de genero e de andamento contribuem 0 tags em quase toda faixa, porque o fragmento ja esta no base — uma sugestao pela prioridade de camada mandaria desliga-los a toa. (3) A lista de corte automatica, pela prioridade do HISTORY §10 ou por menos cliques, chega ao mesmo resultado e manda cortar primeiro a voz de rap em ar-05 e ar-06, que sao rap-pop: a prioridade generica erra em 2 de 7 faixas reais.

**Decisao:** Cada chip mostra o seu custo marginal em tags para aquele cartao — `−N` ligado, `+N` desligado, `0` quando nao muda o prompt —, recalculado em todos os chips a cada clique e so com o painel aberto. Quando o recomposto passa de 10 tags, a linha de qualidade diz quanto o style base usa sozinho. A ferramenta mostra o custo; quem escolhe o corte e o dono.

**Alternativas consideradas:** (a) lista de corte automatica — descartada pela medicao acima; (c) a (b) com uma sugestao destacada pelo maior custo — descartada: esse criterio empata em 6 das 7 faixas, e um desempate arbitrario num destaque e lido como conselho; (d) corrigir a prioridade com uma tabela de generos centrados na voz — descartada: congelaria em codigo um conhecimento que muda com o Suno.

**Consequencias:** (+) O chip que acende sem mudar nada passa a dizer `0` — o defeito silencioso mais antigo do painel de modulos. (+) Em ar-01 e ar-04 a folga diz que o problema e o base, nao os chips. (+) 7-15 ms por cartao aberto. (−) A informacao e mais densa: 50 chips com numero. (−) O style base escrito no limite continua sendo gerado assim; a regra que o evitaria mora no prompt-modelo (i-028).
