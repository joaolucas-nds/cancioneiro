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
