# IDEAS.md — Cancioneiro

> Segundo cérebro. Nunca perde nada: ideia muda de status, não some.
> Status: 💡 aberta · 🔨 em desenvolvimento · ✅ concluída · ❌ descartada (com motivo).

---

## Ativas

### i-001 ✅ Cartões por álbum, não lista rolante
Renderizar cada canção como um **cartão** dentro de um **álbum** (seção colapsável ou aba), em vez de uma lista longa a rolar. Você bate o olho e vê o que é cada bloco; não procura. Núcleo da ferramenta. → vira trabalho na Fase 2 (ROADMAP).

### i-002 ✅ Prompt-modelo para chats gerarem JSON no esquema
Um texto pronto (guardado no repo, ex.: `schema/PROMPT-PARA-CHATS.md`) que você cola num chat novo junto do pedido, e o chat já entrega a canção/álbum **no esquema canônico**, sem inventar convenção. Fecha o ciclo "chat gera → ferramenta lê". Alta prioridade — sem isso, cada chat volta a improvisar formato. Ligado ao backlog do STATUS.

### i-003 ✅ Botão "copiar" por campo, com marcação de usado
Cada canção tem botões separados: copiar Style, copiar Lyrics. Ao copiar, o cartão marca visualmente (ex.: borda/checkmark "já usei este"). Estado efêmero em localStorage (DEC-004). Núcleo da ferramenta.

### i-004 ✅ Módulos de estilo trocáveis por menu (núcleo no v0)
Fragmentos de estilo nomeados (`melancholic`, `taiko-drums`, `female-soprano`, faixas de BPM) que se ligam/desligam por menu de contexto, recompondo o campo `style` final e gerando variações sem reescrever. Importar os "estilos construídos por chat" (prompts prontos dos álbuns) como módulos. Ver `schema/style-modules.json`. Fase 3.

### i-005 💡 Controle de BPM por slider/roll
BPM como valor manipulável na ferramenta (slider ou stepper), refletindo no style copiado. Cuidado registrado no HISTORY: Suno trata BPM como aproximação, não comando exato — a ferramenta ajuda a *escrever* o BPM, não garante que o Suno obedeça. Fase 3.
**Implementada em 2026-10-28 (DEC-020)** — campo numérico no cartão, não slider (spec `meta/specs/261028-controle-de-bpm.md`, Decisão 3). Vira ✅ depois da conferência na tela.

### i-006 ✅ Export MD seletivo (1 canção / 1 álbum / tudo)
Gerar `.md` legível sob demanda a partir do JSON, com o formato limpo (rótulo FORA do bloco copiável). Serve para colar num chat ou subir num Projeto. Fase 2/3.

### i-007 ✅ Estados de canção como no Cinzeiro (ideia→gerada→…→aprovada)
Adotar o ciclo de estados que o FAIXAS.md do Cinzeiro já usa, como campo `state` filtrável na ferramenta. Permite ver "o que falta gerar". Já no esquema; UI de filtro na Fase 2.

### i-008 💡 Importar acervo existente convertendo por álbum
Converter os `ALBUM_*.md` e `album_guia_suno.md` para o esquema, um álbum por vez (semi-assistido por chat), populando `data/`. Começar pelo `album_guia_suno.md` (mais limpo). Backlog do STATUS.

### i-009 ✅ Campo de exclusão de estilos ("exclude styles")
A pesquisa apontou que o Suno tem um campo de estilos a excluir que funciona melhor que "no X" no texto (reconfirmado em jul/2026: o campo dedicado é mais barato e confiável que negação no style). Implementado: `excludeStyles[]` no esquema + exibição e botão de copiar na ferramenta.

### i-010 💡 Duas camadas por faixa (exploração + combate) para OST de jogo
Herança do Cinzeiro (DEC-M-002/006 de lá): faixas de jogo podem ter duas versões sincronizadas. O esquema poderia suportar `layers[]` numa canção. Só relevante se o Cancioneiro for usado para OST de jogo — parquear até haver demanda real.

### i-011 💡 Combobox editável para módulos (superar a "janelinha" limitada)
Os concorrentes (usesuno builder) só mostram alguns chips por categoria na janelinha; para o resto, busca. Nosso menu de módulos pode ser um **combobox editável com autocomplete**: digita e filtra a biblioteca inteira, chips sugeridos como atalho, E permite criar valor fora da lista (nosso acervo é dono dos dados, ao contrário deles). Sem teto de "só os que cabem". Fase 3 (refino do painel de módulos).

### i-012 💡 Importar taxonomia de gênero do usesuno (10 categorias → subgêneros)
O usesuno organiza gênero em 10 categorias-mãe (Pop, Hip-Hop, EDM, Rock, R&B, Jazz, Folk, Classical/Cinematic, World, Experimental/Ambient) com subgêneros. Útil como submenu de gênero na troca modular e como vocabulário para ensinar os chats. Fase 3.

### i-013 💡 Método A/B de uma variável embutido na ferramenta
O guia do usesuno ensina testar uma variável por vez (muda uma frase, congela o resto, compara). A ferramenta poderia gerar pares A/B a partir de uma canção (baseline vs. um módulo ligado) e um espaço para anotar o veredito. Transforma o acervo em registro de experimentos. Fase 4.

### i-014 ✅ Prompt-modelo alinhado às cinco camadas
O texto que ensina os chats (i-002) deve pedir explicitamente as cinco camadas audíveis (lane/motion/sources/voice/production) + os dois campos separados + [Instrumental]. Assim o chat gera JSON já pensando em camadas. Liga i-002 ao aprendizado desta sessão.

### i-015 💡 "Exportar estado" das marcações (usei/filtros) para versionar
Bônus: botão que exporta as marcações de sessão (hoje em localStorage) para um pequeno JSON, para levar entre máquinas ou versionar. Não é canônico (DEC-004); é conveniência. Fase 4.

### i-016 💡 Rodar validate.py em pre-commit / CI
Já que `scripts/validate.py` existe e retorna código 1 em erro, plugá-lo num hook de pre-commit (ou GitHub Action) garante que nenhum dataset quebrado entre no repo. Baixo esforço, alta rede de segurança. Fase 2/3.

### i-017 ✅ Contador de caracteres do Style e do Lyrics
O Suno **trunca em silêncio** ao passar de ~1.000 caracteres no Style (5.000 no Lyrics, com ~3.000 como ponto doce). Sem aviso, sem erro — o excedente só não chega ao modelo. É um problema invisível que só uma ferramenta resolve. Mostrar contador ao vivo, com aviso ao aproximar do limite. Ver HISTORY §9. **Alta prioridade** — é exatamente o "consumir espaço desnecessário" da premissa original.

**Entregue em 0.5.0 (DEC-018), conferido na tela em 2026-10-27.** Mede tambem o Exclude (1.000) e mede o Style **recomposto** — a medicao mostrou que o risco mora nos modulos: nenhum style base passa de 174 caracteres, e todas as faixas do album passam de 1.000 com a biblioteca inteira ligada.

### i-018 ✅ Contador de tags com aviso de excesso
Acima de ~10 tags o Suno começa a ignorar as finais e a média dos sinais vira resultado genérico; o ponto doce fica entre 5 e 8. A ferramenta pode contar as vírgulas do Style e avisar quando passar, sugerindo o que cortar pela ordem de prioridade (gênero > clima > instrumento > vocal > BPM). Ver HISTORY §10.

**Entregue em 0.5.0 (DEC-018), sem a sugestao de corte** — que virou i-026. Ambar acima de ~10, nunca vermelho: diluir nao perde texto, e a fonte do v6 diz que acima de 10 «o ganho achata, nao quebra».

### i-019 ✅ Detectar "no X" no style e sugerir migrar para excludeStyles
O campo de exclusão dedicado é mais confiável e barato que negação dentro do texto. Quando houver "no alguma-coisa" no `style`, a ferramenta destaca e oferece mover para `excludeStyles` num clique. Ver HISTORY §11.

**Entregue em 0.5.0 (DEC-018), so avisando** — mover num clique seria a primeira escrita da ferramenta no acervo e ficou fora por decisao do dono. Deteccao por fronteira de palavra (substring casava pia-no e sopra-no); `no vocals` nao dispara em faixa instrumental (Lyrics sem nenhuma linha de letra).

### i-020 💡 Aviso de ordem: gênero nas primeiras palavras
O Suno pesa mais as tags iniciais; gênero primeiro, clima em seguida. A ferramenta pode sinalizar quando o primeiro fragmento não parece um gênero (comparando com a camada `genre` da biblioteca de módulos). Sugestão leve, não imposição.

**Adiado em 2026-10-24 (Decisao 3 da spec do painel de qualidade).** Medido: dispara em **0 de 10** faixas reais (demo + album-referencias) — todas comecam com genero. Evidencia de dominio a mais fraca das quatro da Fase 3a (o Suno «parece» pesar mais as primeiras tags; um teste so), e a deteccao comparando com a camada `genre` e fragil: `dark ambient cinematic intro` so casou porque contem `dark ambient`. **Gatilho para reabrir:** a primeira faixa real cujo primeiro fragmento nao seja genero.

### i-021 💡 Campos de peso (styleWeight / desvio criativo)
A API expõe pesos 0.00-1.00 para aderência ao estilo e desvio criativo (os Creative Sliders). Poderiam virar campos opcionais do esquema para registrar a configuração usada numa geração. Só vale se o fluxo passar a depender disso. Fase 4.

### i-022 💡 Skill que ensina a gerar o JSON do Cancioneiro
`[relatado pelo dono, 2026-08-22]` Uma skill do projeto que ensine um chat a produzir o JSON canonico seguindo o esquema a risca — estrutura, campos obrigatorios, a regra de dominio (rotulo fora do bloco copiavel). Hoje isso vive no `schema/PROMPT-PARA-CHATS.md`, que e um texto colavel: a skill seria a versao que o proprio Claude Code carrega. **Sobreposicao a resolver antes de construir:** i-002 (o prompt-modelo) ja cobre parte disto; decidir se a skill substitui o prompt-modelo ou se os dois convivem em canais diferentes (chat colavel × skill do repo).

### i-023 💡 Skill com os macetes do Suno
`[relatado pelo dono, 2026-08-22]` Uma skill que consolide o que o projeto sabe sobre gerar musica com IA: como estruturar cada parte, onde cada coisa entra, possibilidades e exemplos. **O material ja existe** — e o `meta/HISTORY.md` §1-13, com nivel de confianca e fontes. A ideia e a FORMA, nao o conteudo: transformar conhecimento lido sob demanda em skill lida antes de trabalhar. Pesar contra o custo: skill e lida sempre, HISTORY so quando preciso.

### i-024 💡 Molde para o projeto gerar skill de estilo proprio
`[relatado pelo dono, 2026-08-22]` Nao e uma skill, e um **molde que gera skills** — uma por estilo musical, capturando como manter o mesmo estilo, voz, idioma, forma de escrever letra, tom e melodia, e como guiar edicao, extend e cover. Serviria para replicar ou refinar um estilo ja estabelecido. E a ideia mais ambiciosa das tres e a mais dependente das outras duas; candidata a analise (`meta/analises/`) antes de qualquer spec, porque mexe no formato de um artefato que outra pessoa vai ler.

### i-025 💡 Teste de round-trip automatizado (baixar → reimportar)
`[nascido do FIX-004, 2026-10-22]` O ciclo baixar→reimportar quebrou por meses sem ninguem notar, e so apareceu porque alguem abriu o app num navegador de verdade. Uma checagem que carregue um acervo, serialize como o `downloadCollection` serializa e reimporte, afirmando igualdade, capturaria a classe inteira — nao so o `_activeModules`. Hoje o `validate.py` valida arquivos parados; isto e o primeiro teste de COMPORTAMENTO do projeto, e exige decidir se entra um harness de navegador (headless) ou se a serializacao e extraida para uma funcao testavel sem DOM. Candidata a analise antes de spec.

### i-026 ✅ Sugerir o que cortar quando ha tags demais (Fase 3a.2)
`[nascido da spec do painel, 2026-10-24]` O painel ja avisa quando o Style passa de ~10 tags, mas nao diz QUAIS cortar. O HISTORY §10 traz a ordem de prioridade (genero > clima > instrumento principal > vocal > BPM). Medido: 7 de 7 faixas do album de referencias passam de 10 tags so com os modulos da propria faixa (11 a 18) — o aviso ambar vai acender quase sempre, e aviso que sempre acende vira paisagem. A sugestao e o que transforma o aviso em acao. Exige classificar cada fragmento por camada, o que o recomposto nao carrega hoje: o fragmento do modulo sabe a camada, o do style base nao.

**Corrigido em 2026-10-27 (DEC-019).** A frase acima sobre classificar o base estava errada: medido, o style base nunca passa de 10 tags e o excesso vem todo dos modulos. E a lista de corte automatica erra em 2 de 7 faixas (manda cortar a voz de rap em rap-pop). A 3a.2 entrega o **custo de cada modulo no chip** e a folga do base, nao uma sugestao; aguarda a conferencia na tela.

**Entregue em 0.6.0, conferido na tela em 2026-10-27** — como custo no chip, nao como lista de corte.

### i-027 ✅ O app declarar a propria versao na tela
`[nascido da exploracao de 2026-10-21, candidato C4]` STATUS, CHANGELOG e README dizem a versao; o `app/index.html` publicado nao a declara em lugar nenhum. Consequencia observada: a captura de tela de 2026-10-17 nao permitia saber qual versao estava no ar. Uma linha discreta no rodape (ou no `title`) torna todo print do dono datavel, e um teste pode afirmar que ela bate com o topo do CHANGELOG. Pequeno; candidato a ir junto da proxima WO de codigo.

**Entregue em 0.6.0.** O cabecalho mostra `v0.6.0`, e o `scripts/validate.py` reprova (codigo 1) se o topo do CHANGELOG, o app, o README e o STATUS divergirem.

### i-028 💡 O prompt-modelo pedir folga para os modulos
`[nascido da spec da 3a.2, 2026-10-27]` Em ar-01 e ar-04 o style base que o chat escreveu ja usa 10 de 10 tags: nenhum modulo cabe sem estourar. O painel agora diz isso, mas so depois. A regra que o evitaria mora em quem escreve o base — o `schema/PROMPT-PARA-CHATS.md` poderia pedir «style base com 6 a 8 tags, deixando folga para os modulos». Pesar contra: o base mais curto pode ficar vago (abaixo de 4 tags o painel ja avisa).

### i-029 💡 Avisar quando a palavra de andamento contradiz o BPM
`[nascido da spec do BPM, 2026-10-28]` Com o controle, ar-04 vai a 140 e continua dizendo «downtempo» e «slow build». A linha de qualidade poderia avisar, em ambar, quando uma palavra de andamento do Style («downtempo», «slow», «uptempo», «fast») briga com o numero. Pesar contra: exige uma tabela palavra → faixa de BPM, conhecimento de dominio que muda com o Suno — o mesmo motivo que tirou a tabela de generos vocais da DEC-019. Se entrar, a tabela mora num objeto unico com fonte e data, como o `QUALITY_LIMITS`.

## Feedback para o Kit

- **[2026-07-19] Nicho pediria uma variante "ferramenta+conteúdo".** Este projeto é dev, mas o "produto" é metade código (app) e metade dado curado (acervo JSON). O template de Desenvolvimento cobre bem a parte código; a parte "acervo de dados como entregável" ficou por conta do CONTEXT. Não faltou nada crítico, mas um nicho híbrido "ferramenta que consome conteúdo estruturado" seria útil.
- **[2026-07-19] Regra de domínio a considerar nas Instruções (DEC-005):** "conteúdo copiável para a ferramenta-alvo nunca leva rótulo de referência dentro do bloco". É a armadilha central deste domínio; virou princípio de projeto. Candidata a entrar nas Instruções no primeiro refino.

- **[2026-07-19] Raia chat×Code confirmada na prática.** Construí o v0 da ferramenta no chat (decisão de forma, com pesquisa de UI e design). A partir daqui, a iteração fina (ajustes pós-validação visual) vai melhor no Claude Code por spec. O ponto de virada chat→Code é "forma decidida → executar deltas".
- **[2026-10-20] O manifesto do v1.127.0 conta 4 carimbos de versao; sao 5.** O texto diz «o CEREBRO, o modelo de WO e as duas skills», mas o pacote traz carimbo tambem em `sondar.SKILL__template-update.md`. O texto nao acompanhou a chegada da terceira skill. Medido: `grep -o "Kit de Contexto Universal v[0-9.]*"` nos arquivos do pacote devolve 5.
- **[2026-10-20] Natureza `fusao` pode ser falso positivo, e custa caro quando e.** O manifesto marca CEREBRO e INSTRUCOES como `fusao`, o que faz o merge comecar pressupondo redacao propria a preservar. Neste projeto o CEREBRO nao tinha nenhuma: 20 das 192 linhas divergiam, todas texto do kit antigo. Sugestao ao kit: ensinar a **medir** a divergencia antes de escolher o metodo (comparacao normalizada linha a linha), porque o metodo de fusao paragrafo a paragrafo custa muito mais e, quando o arquivo nao evoluiu, chega ao mesmo resultado. O caso oposto tambem existe — as Instrucoes DESTE projeto eram fusao de verdade.
- **[2026-10-20] A varredura de linhas revogadas cria ocorrencias novas enquanto corrige as antigas.** As WOs e os relatorios que documentam a correcao citam o termo revogado para explica-lo, e entram na contagem seguinte como se fossem divida. A contagem total sobe ou cai pouco, e parece que o trabalho nao andou. Sugestao: o manifesto pedir a contagem **por natureza** (manda / relata / dominio / contraste / meta-documentacao da propria correcao), nao so o total — e dizer que o alvo e zero na primeira classe, nao no total.
- **[2026-10-20] O carimbo de modos nao cobre o caso «o template e mais pobre que o vivo», e o manifesto resolve isso em prosa.** A natureza `template` diz «comparar e adotar novidade e seguro», e a regra que protege o arquivo vivo esta num paragrafo mais abaixo. Numa fatia em que SETE arquivos caem todos em (c), ler na ordem leva a propor substituicao sete vezes antes de chegar a regra que a proibe. Sugestao: o manifesto trazer, ao lado da natureza, qual das tres respostas e o DEFAULT esperado para aquele arquivo — `adotar`, `fundir` ou `(c) fica o vivo` —, que e informacao que quem gera o pacote tem e quem o recebe precisa descobrir lendo tudo.
- **[2026-10-24] Terceiro pacote seguido com a contagem de carriers errada.** O manifesto do v1.131.0 diz «Quatro arquivos deste pacote terminam em Gerado pelo Kit...» e sao **cinco**: CEREBRO, modelo de WO e as **tres** skills (`apply-wo`, `wrap`, `sondar`). Medido: `grep -h -o "Kit de Contexto Universal v[0-9.]*" *.md | sort | uniq -c` no pacote devolve 6 ocorrencias em 5 arquivos distintos. A frase nao acompanhou a chegada da `sondar` no v1.127.0 e segue igual quatro versoes depois. Sugestao: derivar o numero da propria geracao, em vez de escreve-lo na prosa — e o caso exato da regra «nao congele em documento estavel o que um artefato vivo ja responde», que o proprio CEREBRO ensina.
- **[2026-10-24] A forma do roteiro de tela chegou no v1.131.0, e a regra que ela formaliza ja era violavel no v1.127.0.** O modelo de WO novo prescreve cinco linhas de cabecalho, tres secoes e contrato de retorno — e diz com todas as letras que o roteiro «vai INTEIRO no corpo da resposta do chat, nunca "ver o fim da WO"». Neste projeto o roteiro foi parar dentro da WO uma vez, com a regra «quem tem a TELA ve» ja presente no CEREBRO vivo. O que faltava nao era a regra, era a FORMA: regra sem forma nao se cumpre sozinha, e a licao vale para o kit inteiro — todo principio que ja falhou em campo merece o molde junto, nao so o enunciado.

## Concluídas

### c-001 ✅ Escolher formato de dados (JSON vs MD) → JSON canônico
Decidido na fundação. Ver DEC-001.

### c-002 ✅ Escolher stack da ferramenta → HTML+JS single-file
Decidido na fundação. Ver DEC-002.

### c-003 ✅ Nomear o projeto → cancioneiro
Decidido na fundação. Ver DEC-003.

## Descartadas

### x-001 ❌ Parser universal de Markdown dos álbuns antigos
Descartado na fundação: as convenções divergentes entre álbuns tornariam o parser um poço de exceções. Conversão semi-assistida por chat é mais confiável. Ver DEC-001.

### x-002 ❌ localStorage como fonte de verdade do acervo
Descartado na fundação: frágil e não versionável. localStorage fica só para estado efêmero. Ver DEC-004.
