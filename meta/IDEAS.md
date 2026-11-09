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

### i-005 ✅ Controle de BPM por slider/roll
BPM como valor manipulável na ferramenta (slider ou stepper), refletindo no style copiado. Cuidado registrado no HISTORY: Suno trata BPM como aproximação, não comando exato — a ferramenta ajuda a *escrever* o BPM, não garante que o Suno obedeça. Fase 3.
**Implementada em 2026-10-28 (DEC-020)** — campo numérico no cartão, não slider (spec `meta/specs/261028-controle-de-bpm.md`, Decisão 3). Entregue em 0.7.0; os seis itens do roteiro de tela conferidos pelo dono em 2026-10-28 `[relatado pelo dono]`.

### i-006 ✅ Export MD seletivo (1 canção / 1 álbum / tudo)
Gerar `.md` legível sob demanda a partir do JSON, com o formato limpo (rótulo FORA do bloco copiável). Serve para colar num chat ou subir num Projeto. Fase 2/3.

### i-007 ✅ Estados de canção como no Cinzeiro (ideia→gerada→…→aprovada)
Adotar o ciclo de estados que o FAIXAS.md do Cinzeiro já usa, como campo `state` filtrável na ferramenta. Permite ver "o que falta gerar". Já no esquema; UI de filtro na Fase 2.

### i-008 ✅ Importar acervo existente convertendo por álbum
Converter os `ALBUM_*.md` e `album_guia_suno.md` para o esquema, um álbum por vez (semi-assistido por chat), populando `data/`. Começar pelo `album_guia_suno.md` (mais limpo). Backlog do STATUS.
**Desbloqueada em 2026-10-29:** o dono trouxe os álbuns para a pasta-pai — `../Album Rainha da Preguiça/` (11 arquivos: índice-mestre e 10 volumes) e `../Albuns/` (8 guias, entre eles o `album_guia_suno.md`), cerca de 44 mil linhas `[medido por instrumento: wc -l]`. Ainda não lidos: frente própria.
**Em trabalho (2026-10-29):** sonda e análise `meta/analises/261029-ANALISE-conversao-dos-albuns.md`, decidida 1A a 4A (DEC-026): conversor determinístico por família, acervo fora do repo. A família BR está convertida (0.9.1, `scripts/convert_br.py`, 151 faixas). `Albuns/` espera os grupos da i-038.
**Entregue (0.10.0, 2026-10-31):** os 19 guias convertidos — BR (151 faixas) e `Albuns/` (205 faixas, `scripts/convert_guides.py`), os dois acervos fora do repo.

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

### i-016 ✅ Rodar validate.py em pre-commit / CI
Já que `scripts/validate.py` existe e retorna código 1 em erro, plugá-lo num hook de pre-commit (ou GitHub Action) garante que nenhum dataset quebrado entre no repo. Baixo esforço, alta rede de segurança. Fase 2/3.
**Entregue (2026-11-09, DEC-034):** no GitHub Actions, a cada push e pull request na `main`, com `jsonschema`; junto dos testes do navegador (i-051). O pre-commit ficou de fora: pediria as dependências na máquina do dono.

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

### i-022 ✅ Skill que ensina a gerar o JSON do Cancioneiro
`[relatado pelo dono, 2026-08-22]` Uma skill do projeto que ensine um chat a produzir o JSON canonico seguindo o esquema a risca — estrutura, campos obrigatorios, a regra de dominio (rotulo fora do bloco copiavel). Hoje isso vive no `schema/PROMPT-PARA-CHATS.md`, que e um texto colavel: a skill seria a versao que o proprio Claude Code carrega. **Sobreposicao a resolver antes de construir:** i-002 (o prompt-modelo) ja cobre parte disto; decidir se a skill substitui o prompt-modelo ou se os dois convivem em canais diferentes (chat colavel × skill do repo).
**Resolvida em 2026-10-31 (i-039, DEC-027):** sem skill nova — o contrato fica no prompt-modelo, fonte única; o kit de música o leva ao projeto junto das skills.

### i-023 ✅ Skill com os macetes do Suno
`[relatado pelo dono, 2026-08-22]` Uma skill que consolide o que o projeto sabe sobre gerar musica com IA: como estruturar cada parte, onde cada coisa entra, possibilidades e exemplos. **O material ja existe** — e o `meta/HISTORY.md` §1-13, com nivel de confianca e fontes. A ideia e a FORMA, nao o conteudo: transformar conhecimento lido sob demanda em skill lida antes de trabalhar. Pesar contra o custo: skill e lida sempre, HISTORY so quando preciso.
**Entregue em 0.10.0 (2026-10-31):** `kit-musica/skills/macetes-suno/SKILL.md` — lida sob demanda, ao escrever style ou letra.

### i-024 💡 Molde para o projeto gerar skill de estilo proprio
`[relatado pelo dono, 2026-08-22]` Nao e uma skill, e um **molde que gera skills** — uma por estilo musical, capturando como manter o mesmo estilo, voz, idioma, forma de escrever letra, tom e melodia, e como guiar edicao, extend e cover. Serviria para replicar ou refinar um estilo ja estabelecido. E a ideia mais ambiciosa das tres e a mais dependente das outras duas; candidata a analise (`meta/analises/`) antes de qualquer spec, porque mexe no formato de um artefato que outra pessoa vai ler.

### i-025 ✅ Teste de round-trip automatizado (baixar → reimportar)
`[nascido do FIX-004, 2026-10-22]` O ciclo baixar→reimportar quebrou por meses sem ninguem notar, e so apareceu porque alguem abriu o app num navegador de verdade. Uma checagem que carregue um acervo, serialize como o `downloadCollection` serializa e reimporte, afirmando igualdade, capturaria a classe inteira — nao so o `_activeModules`. Hoje o `validate.py` valida arquivos parados; isto e o primeiro teste de COMPORTAMENTO do projeto, e exige decidir se entra um harness de navegador (headless) ou se a serializacao e extraida para uma funcao testavel sem DOM. Candidata a analise antes de spec.
**Entregue (2026-11-09, DEC-034):** `tests/test_roundtrip.py` baixa e reimporta um acervo sintético de 205 faixas, antes e depois de organizar, e compara com o original.

### i-026 ✅ Sugerir o que cortar quando ha tags demais (Fase 3a.2)
`[nascido da spec do painel, 2026-10-24]` O painel ja avisa quando o Style passa de ~10 tags, mas nao diz QUAIS cortar. O HISTORY §10 traz a ordem de prioridade (genero > clima > instrumento principal > vocal > BPM). Medido: 7 de 7 faixas do album de referencias passam de 10 tags so com os modulos da propria faixa (11 a 18) — o aviso ambar vai acender quase sempre, e aviso que sempre acende vira paisagem. A sugestao e o que transforma o aviso em acao. Exige classificar cada fragmento por camada, o que o recomposto nao carrega hoje: o fragmento do modulo sabe a camada, o do style base nao.

**Corrigido em 2026-10-27 (DEC-019).** A frase acima sobre classificar o base estava errada: medido, o style base nunca passa de 10 tags e o excesso vem todo dos modulos. E a lista de corte automatica erra em 2 de 7 faixas (manda cortar a voz de rap em rap-pop). A 3a.2 entrega o **custo de cada modulo no chip** e a folga do base, nao uma sugestao; aguarda a conferencia na tela.

**Entregue em 0.6.0, conferido na tela em 2026-10-27** — como custo no chip, nao como lista de corte.

### i-027 ✅ O app declarar a propria versao na tela
`[nascido da exploracao de 2026-10-21, candidato C4]` STATUS, CHANGELOG e README dizem a versao; o `app/index.html` publicado nao a declara em lugar nenhum. Consequencia observada: a captura de tela de 2026-10-17 nao permitia saber qual versao estava no ar. Uma linha discreta no rodape (ou no `title`) torna todo print do dono datavel, e um teste pode afirmar que ela bate com o topo do CHANGELOG. Pequeno; candidato a ir junto da proxima WO de codigo.

**Entregue em 0.6.0.** O cabecalho mostra `v0.6.0`, e o `scripts/validate.py` reprova (codigo 1) se o topo do CHANGELOG, o app, o README e o STATUS divergirem.

### i-028 ✅ O prompt-modelo pedir folga para os modulos
`[nascido da spec da 3a.2, 2026-10-27]` Em ar-01 e ar-04 o style base que o chat escreveu ja usa 10 de 10 tags: nenhum modulo cabe sem estourar. O painel agora diz isso, mas so depois. A regra que o evitaria mora em quem escreve o base — o `schema/PROMPT-PARA-CHATS.md` poderia pedir «style base com 6 a 8 tags, deixando folga para os modulos». Pesar contra: o base mais curto pode ficar vago (abaixo de 4 tags o painel ja avisa).
**Em trabalho (2026-10-28, DEC-021, WO 0015).** O teste base do prompt (tres chats, `meta/specs/261028-prompt-modelo-e-modulos.md`) confirmou o base no limite (10+ tags em 5 de 9 faixas) e mostrou um problema maior: o prompt nao ensinava o contrato de modulo, e os tres chats inventaram tres formatos. O prompt agora pede style com 6 a 8 tags e ate 10 com os modulos ligados. Fecha com o reteste do dono.
**Entregue em 0.8.0.** Reteste (2026-10-29, dois chats): base com 7 ou 8 tags e recomposto com 8 a 10 em 6 de 6 faixas.

### i-029 💡 Avisar quando a palavra de andamento contradiz o BPM
`[nascido da spec do BPM, 2026-10-28]` Com o controle, ar-04 vai a 140 e continua dizendo «downtempo» e «slow build». A linha de qualidade poderia avisar, em ambar, quando uma palavra de andamento do Style («downtempo», «slow», «uptempo», «fast») briga com o numero. Pesar contra: exige uma tabela palavra → faixa de BPM, conhecimento de dominio que muda com o Suno — o mesmo motivo que tirou a tabela de generos vocais da DEC-019. Se entrar, a tabela mora num objeto unico com fonte e data, como o `QUALITY_LIMITS`.

### i-030 ✅ Ordem dos campos no cartao: Lyrics acima do Style, como no Suno
`[relatado pelo dono, 2026-10-28]` O cartao mostra Style em cima e Lyrics embaixo; no Suno e o contrario, e copiar na ordem da tela agilizaria. O dono prefere que seja **configuravel**. A preferencia e estado de interface e pode morar no navegador (DEC-004). A decidir na spec: se o export MD segue a ordem escolhida, e onde fica o controle (cabecalho ou cartao).
`[relatado pelo dono, 2026-10-29, nota 1106]` **Refinado:** a ordem atual (titulo, Style, Lyrics) faz sentido para quem preenche o Suno de baixo para cima — o dono faz assim. O pedido e **controlar a estrutura na interface e salvar no navegador**, com a ordem atual como padrao. Medido nas capturas do dono (2026-10-29): o formulario do v6 e, de cima para baixo, Lyrics → Styles → opcoes → titulo, e **nao tem campo de Exclude** no v6-mini gratuito — o bloco Exclude do cartao fica sem destino para ele hoje. Candidato: mostrar/ocultar cada campo, alem da ordem.

### i-031 ✅ Prompt e exemplo pela interface do app
`[relatado pelo dono, 2026-10-28, notas 1813 e 1852]` O dono nao quer abrir as pastas do repositorio para pegar o prompt-modelo ou um exemplo: quer copiar o prompt ja com o «Meu pedido» e baixar um exemplo pelo app publicado, como o KCM faz. **Em trabalho (DEC-021, WO 0015):** botoes «Prompt para chats» e «Baixar exemplo», que buscam `schema/PROMPT-PARA-CHATS.md` e `data/demo.json` no clique — fonte unica, sem copia no app. Evolucao possivel: campos guiados para «estruturar» o pedido (quantidade, idioma, instrumental, BPM), so se o reteste mostrar que o texto livre nao basta.
**Entregue em 0.8.0**, conferido na tela pelo dono. O reteste com texto livre passou em 6 de 6 faixas: os campos guiados nao sao necessarios por ora.

### i-032 💡 Outras plataformas de musica por IA
`[relatado pelo dono, 2026-10-28]` Existem outros sites e apps de celular com estrutura parecida com a do Suno e diferente dela; o dono quer sugestoes para testar e, se valer, ampliar a estrutura do projeto para comporta-los. O esquema ja e agnostico no nome (`targetTool`), mas `style`/`lyrics`/`excludeStyles` espelham os campos do Suno. Proximo passo: um turno de pesquisa atual (plano gratuito, campos equivalentes, limites, API, app mobile) antes de qualquer mudanca de esquema. Pesar contra: generalizar o esquema antes de usar uma segunda plataforma de verdade e especular.

### i-033 ✅ Copiar o titulo da faixa com um clique
`[relatado pelo dono, 2026-10-29, nota 1106]` Faltou copiar facil o nome da musica. O formulario do v6 tem campo de titulo (o ultimo, antes de «Save to»). Um botao «copiar» ao lado do titulo do cartao, com a mesma marcacao de copiado dos outros campos.

### i-034 ✅ Arrastar o .json para a tela e carregar
`[relatado pelo dono, 2026-10-29, nota 1106]` Soltar o arquivo em qualquer lugar da pagina = importar, pelo mesmo caminho do botao (saneamento e avisos iguais: FIX-006, FIX-009). Combina com o prompt que entrega arquivo (i-036): baixar do chat e arrastar para o app.

### i-035 ✅ O acervo continuar carregado depois de fechar o navegador
`[relatado pelo dono, 2026-10-29, nota 1106]` Hoje so as marcas «usei» sobrevivem; o acervo some ao fechar. Guardar uma copia do ultimo acervo importado no navegador e recarrega-la ao abrir. **Toca a DEC-004** (o navegador e cache, nunca fonte): uma copia do ultimo arquivo importado e cache legitimo, porque o app nao edita o acervo (FIX-004) — a copia e igual ao arquivo. Risco a tratar: o arquivo mudar fora (um chat gerou versao nova) e o app seguir mostrando a copia velha sem aviso; mitigacao: dizer na tela de onde veio o acervo e quando foi importado, e um botao para esquecer a copia. A carga automatica do Pages (`demo.json`) passa a valer so quando nao houver copia. Pede DEC propria.

### i-036 ✅ O prompt pedir o JSON como arquivo para baixar
`[relatado pelo dono, 2026-10-29, nota 1106]` Em vez de texto para copiar, o chat entregar um `.json` para download. Ganha: sem colar no Bloco de notas, sem erro de codificacao, nome de arquivo pronto — e casa com a i-034. Custa: depende de o chat conseguir criar arquivo (varia por produto e por recurso ligado), e o texto atual do prompt foi o que passou no reteste de 2026-10-29 — mudar exige retestar. Forma candidata: pedir arquivo **se o chat puder criar arquivos**, e manter «so o JSON, sem texto» como alternativa.

### i-037 ✅ Export de album e de acervo com o Style da tela
Achado em 2026-10-29 nos `.md` que o dono exportou: o export de **faixa** sai com o Style recomposto (modulos ligados, controle de BPM), o de **album** e o de **acervo** saem com o `style` base (`albumToMarkdown` chama `songToMarkdown(s, false)`), desde a 0.4.0. Em ar-01, 18 tags na faixa e 10 no album. Pode ser o certo — o album como documento do acervo, a faixa como «o que vou colar agora» —, mas a diferenca nao aparece na tela nem estava escrita. Decidir: os tres seguem a tela, ou o album/acervo continua base e o botao diz isso.

**Em trabalho (2026-10-29, WO 0017):** as i-030, i-033 a i-037 viraram uma frente so, `meta/specs/261029-conveniencias-de-uso.md` (DEC-022, DEC-023). Decisoes do dono: acervo guardado no navegador (D1), estrutura completa (D2), aviso de negacao some com o Exclude oculto (D3), prompt pede arquivo e, sem arquivo, o JSON em bloco de codigo (D4), export segue a tela (D5). Fecha na 0.9.0, depois da tela e do reteste curto do prompt.
**Entregues em 0.9.0** (2026-10-29), conferidas na tela e retestadas pelo dono. Ajustes pedidos em seguida (nota `261029-1618.txt`, DEC-025): o titulo copia ao clicar (sai o botao, que quebrava a linha), as linhas da estrutura se arrastam, o Exclude vem oculto por padrao e o cabecalho fica mais enxuto — em [Unreleased] ate o dono ver.

### i-038 ✅ Reagrupar as faixas de `Albuns/` em álbuns por cena de uso
`[relatado pelo dono, 2026-10-29]` Os oito guias de `Albuns/` misturam gêneros, idiomas e propósitos num arquivo só. O dono quer as faixas em álbuns mais relacionados, para depois ampliar cada um num projeto próprio. Proposta do chat em `../261029-PROPOSTA-grupos-albuns.md` (fora do repo: traz os títulos): 172 faixas em 12 álbuns (épico vocal, trilhas de jogo, romântico multilíngue, Brasil popular, pop asiático, latino, contagem e ritmo, matemática e física, código, foco e estudo, eletrônico instrumental, treino e ação). Um mapa faixa → álbum aplica a escolha por script. Espera a aprovação do dono; depois, conversores dos formatos de `Albuns/` (i-008).
**Conferido no app pelo dono em 2026-10-31:** grupos, títulos e idiomas certos; as duas «Rise of the Eternal» (ÉPICO e guia_suno) ficam `[relatado pelo dono]`.
**Entregue em 0.10.0 (2026-10-31):** grupos aprovados; 205 faixas (não 172 — a contagem da proposta perdeu 33 do VOL5) em 12 álbuns, `../acervos/albuns-reagrupados.json`, mapa em `../acervos/albuns-grupos.json`.

### i-039 🔄 Kit de música para os projetos do KCM
`[relatado pelo dono, 2026-10-29]` Criar projetos de música para o Suno já «profissionais» e adaptados ao Cancioneiro: levar ao nicho de música do KCM o que este projeto sabe. Junta i-022, i-023 e o feedback ao kit de 2026-10-28. Análise `meta/analises/261029-ANALISE-kit-de-musica.md`, em discussão: Instruções-modelo de projeto de música, skill de macetes do Suno, skill de revisão de faixa. A medida que motiva: nos guias antigos, 72 de 151 letras passam do limite em que o Suno corta.
**Em trabalho (0.10.0, 2026-10-31, DEC-027):** as três peças em `kit-musica/` — `BLOCO-SUNO.md` (bloco para Instruções e CEREBRO, não Instruções inteiras: o KCM tem teto), `macetes-suno`, `revisar-faixa`. Carta 01 ao KCM com o mapa para o nicho Música. **Gatilho:** sem resposta do KCM até o primeiro projeto de música novo do dono, o projeto usa o kit à mão (`kit-musica/README.md`, «Como usar hoje») e o que faltar volta como feedback.
**O KCM leu a carta 01 (2026-10-31, aviso `../notas-arquivadas/261031-kcm-leu-01.md`):** foi para a i-N25 deles, cujo próximo passo é analisar o eixo «Produção: tocada / gerada por IA» com o teto das Instruções medido; o feedback ao kit foi para a i-N76; o Cancioneiro entrou no livro de leitura. A resposta vem pela carta 02, sem data. O gatilho acima continua valendo.
**Kit v2 (análise `meta/analises/261109-ANALISE-kit-de-musica-v2.md`, decidida pelo dono em 2026-11-09):** leva 1 entregue em 2026-11-09 — o README na 0.17.0, a `macetes-suno` com «Depois de ouvir» (§10) e as ferramentas do Suno de 2026 (§11), o ciclo do bloco com elas. Leva 2 (skills `escrever-letra-suno` e `conceber-album`) espera um projeto de música para a prova de campo; a carta 02 ao KCM vai depois dela.

### i-040 ✅ Curadoria no app: excluir, exportar e importar faixas
`[relatado pelo dono, 2026-10-29, nota 261029-1825.txt]` Exportar uma faixa como `.json` (além do `.md`); excluir uma faixa; importar faixas para o acervo aberto — todas ou as escolhidas de outro `.json` de álbum, ou uma faixa exportada solta; mudar a ordem e levar faixas de um álbum a outro. Leva o app de leitor a editor leve: pede análise antes de spec, porque mexe na fonte de verdade (DEC-004, DEC-022 — hoje a cópia no navegador é cache do arquivo; editar nela cria um acervo que só existe ali até «Baixar .json»). Ids repetidos e módulos citados na importação também. Faria o reagrupamento da i-038 pela tela.
**Decidida (2026-11-02, DEC-028):** análise `meta/analises/261102-ANALISE-curadoria-no-app.md`, F1 + G1 em três entregas. **Entrega 1 feita (0.11.0):** exportar faixa como `.json` (spec `meta/specs/261102-exportar-faixa-json.md`). A entrega 2 é a i-041; a 3 é o resto desta ideia (excluir, reordenar, mover, novo álbum, importar faixas), num rascunho marcado.
**Entregue (0.13.0, 2026-11-05):** a entrega 3, spec `meta/specs/261105-curadoria-pela-tela.md`, WO 0024 — modo «editar», ↑ ↓, mover, novo álbum, excluir, importar faixas, rascunho com «Baixar .json» pelo nome de origem. Fechar a aba não avisa (DEC-029).

### i-041 ✅ Mais de um acervo guardado no navegador
`[relatado pelo dono, 2026-10-29, nota 261029-1825.txt]` Hoje a DEC-022 guarda só o último importado. Com os acervos convertidos (Rainha da Preguiça, os álbuns de `Albuns/`), trocar de acervo obriga a importar de novo. Medida: a Rainha da Preguiça ocupa ~955 mil caracteres na cópia; o `localStorage` costuma dar ~5 MB por site — dois ou três acervos grandes cabem, mais que isso pede IndexedDB. Anda junto com a i-040.
**Decidida (2026-11-02, DEC-028):** IndexedDB, um acervo por nome de arquivo, marcas «usei» por acervo (hoje colidem: `brv-04`, `cinzeiro-01`). É a entrega 2 da curadoria; a sonda `../261102-sonda-armazenamento.html` mede o navegador do dono antes da spec.
**Entregue (0.12.0, 2026-11-05):** spec `meta/specs/261104-varios-acervos.md`, WO 0023. A sonda (Chrome 156, `file://`) mostrou o IndexedDB funcionando e a origem `file://` compartilhada com outras páginas locais. Janela «acervos (N)», reabre no último aberto, marcas por acervo com migração, ramo sem IndexedDB.

### i-042 💡 Rampa de BPM no style («95 BPM to 118 BPM»)
Achado na conversão BR: três faixas mudam de andamento de propósito. A DEC-020 reprova dois BPM no `validate.py`, e o controle de BPM do cartão igualaria os dois números. Decidir: o controle não aparecer (ou avisar) quando o style tem uma rampa, e o `validate.py` aceitar o par ligado por «to»/«building to», sem perder o erro de autoria que a DEC-020 pega.

### i-043 ✅ Gravar direto no arquivo do acervo (File System Access)
Achado na análise da curadoria (2026-11-02, opção F4): no Chrome e no Edge o app pode abrir o `.json` com permissão de gravar e «Salvar» no mesmo arquivo, sem passar por Downloads. Não existe no Firefox nem no Safari, e a permissão é pedida de novo a cada sessão. **Gatilho:** depois da entrega 3 da curadoria (DEC-028), se a sonda mostrar a API no navegador do dono — entra como «Salvar no arquivo» onde existir, com «Baixar» onde não.
**Medido (2026-11-04, sonda):** no Chrome 156 do dono existem as três APIs — `showSaveFilePicker`, `showOpenFilePicker` e `getAsFileSystemHandle` (arrastar com permissão de gravar). Falta só a entrega 3.
**Gatilho atingido (2026-11-05):** a entrega 3 está pronta (0.13.0). Com ela, o passo que sobra é baixar e substituir o arquivo; gravar direto tira esse passo.
**Planejada (DEC-030):** é a I4 da frente de interface (0.17.0), depois de a I3 deixar o «Salvar» fácil de achar.
**Entregue (0.17.0, I4, DEC-033):** «Salvar» grava no arquivo vinculado no Chrome e no Edge do computador; o vínculo nasce no primeiro «Salvar», ao importar pela janela ou ao soltar o arquivo; o app pergunta antes de gravar por cima de um arquivo mudado fora. Firefox, Safari e o celular baixam. Spec `meta/specs/261106-salvar-no-arquivo.md`.

### i-044 ✅ A barra de controles não some quando não há acervo
Achado no teste da entrega 2 (2026-11-05): o CSS `.controls { display: flex }` vence o atributo `hidden` que o `render()` põe na barra quando não há acervo, então os filtros vazios ficam na tela no estado inicial e depois de esquecer todos. Já era assim antes da 0.12.0. O conserto provável é uma linha (`.controls[hidden] { display: none; }`), mas muda o que o dono vê ao abrir o app vazio — conferir na tela antes.
**Entregue (0.14.0, I1, DEC-030):** a regra `[hidden] { display: none !important; }` vale para o app todo; sem acervo, nem a fileira de etiquetas nem o rascunho aparecem. Spec `meta/specs/261105-barra-unica.md`, WO 0025.

### i-045 ✅ Cabeçalho compacto
`[relatado pelo dono, 2026-11-05]` A barra do topo está «muito folgada»; deixá-la quase colada às bordas dos botões. Medido nas capturas dele (Chrome, janela de 720 px de altura): o cabeçalho é fixo (`position: sticky`) e ocupa uns 85 px. Objetivo dito por ele: uma interface «bonita, profissional, intuitiva». Faz parte da frente de interface (i-044 a i-047), que vem **depois** das funcionalidades em curso, por pedido dele, e começa por um turno de pesquisa.
**Entregue (0.14.0, I1, DEC-030):** uma barra única, fixa, de 48 px (no celular, 51), no lugar do cabeçalho, da barra de filtros e da linha de origem.

### i-046 ✅ Filtros que acompanham a rolagem, e visões do acervo
`[relatado pelo dono, 2026-11-05]` A barra «Álbum · Estado · Uso · buscar» some ao rolar uma lista grande (nas capturas, só o cabeçalho fica fixo). Ele quer que ela fique fixa ou que se possa chamá-la. Inspirações citadas: o controle e a organização de e-commerce e de tabelas, e de Notion e Airtable, com visões (lista, tabela) e opções melhores. Pede pesquisa antes de spec.
**Entregue (DEC-030, DEC-031):** os filtros fixos, num painel, com etiquetas removíveis e «N de M», entraram na I1 (0.14.0); as visões Lista e Cartões, com o detalhe à direita, na I2 (0.15.0). A tabela no estilo Airtable (opção C da análise) e ordenar por coluna ficaram de fora; voltam como ideia se fizerem falta.

### i-047 🔨 Painel lateral com abas
`[relatado pelo dono, 2026-11-05]` Painéis que abrem pela lateral direita, com etiquetas no estilo de «bookmarks». Exemplo dele: os acervos da entrega 2 também numa barra lateral, além da janela. Junto da i-046 na pesquisa. O arrastar cartões para reordenar (fora da entrega 3) entra nesta frente.
**Em andamento (DEC-030, DEC-031):** a lateral de álbuns e acervos entrou na I2 (0.15.0), à esquerda e sem abas, a partir de 1280 px; o detalhe da faixa é o painel da direita. Em aberto: as abas no estilo de «bookmarks» do pedido e a lateral no celular (sem gaveta, por decisão do dono).

### i-048 ✅ Edição e organização com UX de verdade, arrastando onde for útil
`[relatado pelo dono, 2026-11-05]` A estrutura para «edição, controle e organização das faixas, acervos e tudo mais» não está prática nem intuitiva, e falta muito UX/UI. Ele pede estudo e planejamento antes, e praticidades como **arrastar objetos** onde for possível, útil e interessante: cartões entre posições e álbuns, faixas para um acervo, arquivos para a tela. Junta-se às i-044 a i-047, numa frente só (análise `meta/analises/261105-ANALISE-frente-de-interface.md`).
**Entregue (DEC-030, DEC-032):** a I3 (0.16.0): arrastar pela alça, com a SortableJS embutida; o «⋯» por faixa como caminho sem arrastar; seleção em lote; «Desfazer»; o fim do interruptor «editar»; soltar o `.json` sobre um álbum. Ficaram de fora e viraram ideias próprias: organizar os álbuns (i-049) e arrastar uma faixa para outro acervo (i-050).

### i-049 💡 Organizar os álbuns
`[capturada pelo chat, 2026-11-06, na spec da I3]` Renomear um álbum, reordenar os álbuns arrastando na lateral e juntar dois. A I3 organiza as faixas; os álbuns só nascem (pelo «+ Novo álbum» ou pelo «Mover para…») e somem quando esvaziam. Fora da I3 por escopo.

### i-050 💡 Arrastar uma faixa para outro acervo
`[relatado pelo dono, 2026-11-05, na i-048]` Soltar uma faixa sobre outro acervo da lateral para copiá-la ou movê-la para ele. Mexe em dois rascunhos de uma vez (e em dois arquivos a salvar), e pede uma análise própria antes da spec. Hoje o caminho é exportar a faixa em `.json` e importá-la no outro acervo.

### i-051 ✅ Versionar os testes do navegador
`[capturada pelo chat, 2026-11-06, na I4]` Os testes no Chromium headless de cada entrega (curadoria 1 a 3, I1 a I4) moram só na sessão do chat que os escreveu: a conversa seguinte não os tem, e a regressão da I4 teve de ser por fumaça (importar, lista, detalhe, «⋯», Cartões). Guardar em `tests/` (Playwright, Python) e rodar antes de cada WO de código. Pede decidir onde roda (a máquina do dono não tem Playwright) e o custo de manter.
**Entregue (2026-11-09, DEC-034):** `tests/` com 32 testes (básico, organizar, salvar no arquivo, ida e volta, celular) e o workflow `.github/workflows/testes.yml`, que roda a cada push. Só dados sintéticos: o dono perguntou se seriam versionados os acervos — não `[relatado pelo dono, 2026-11-09]`.

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
- **[2026-10-28] Bloco literal da WO com linha de titulo dentro quebra o aplicador por script.** Duas WOs seguidas (0012 e 0013) pararam no meio: o Code aplica lendo os blocos por expressao regular, e um texto novo que contem `## Desfecho` (ou o STATUS inteiro, cheio de `## `) foi lido como o inicio da secao seguinte. As duas se recuperaram so porque a idempotencia pelo texto novo inteiro deixou reexecutar sem duplicar — a regra da idempotencia pagou ali o seu custo. Sugestao ao kit: o modelo de WO dizer que o bloco literal termina na linha de quatro crases e nunca num titulo, e o `apply-wo` delimitar por crases, nao por cabecalho.
- **[2026-10-28] O nicho de musica do KCM ainda nao carrega o que este projeto aprendeu sobre o Suno** `[relatado pelo dono]`. Os projetos de musica que o KCM monta nascem sem o conhecimento destilado aqui: `meta/HISTORY.md` §1-13 (o que tem efeito no Suno, com fonte e confianca), a regra de dominio (rotulo fora do copiavel) e o contrato prompt -> JSON. E o teste base de 2026-10-28 mostra o custo de calar: pedido o que o prompt nao ensinava (modulos), tres chats inventaram tres formatos. Sugestao ao kit: o nicho de musica trazer um resumo desse material como ponto de partida — candidato natural e a i-023 (skill com os macetes do Suno), que ja tem o conteudo pronto.
- **[2026-10-29] O fecho de turno nao tem lugar para o comando que o dono cola, e o rodape e o pior lugar.** O esqueleto do CEREBRO tem Proximo, Estado, Arquivar/Manter, Config e Handoff; a linha `/apply-wo` ficou sem endereco, e uma regra escrita so num brief a mandou para o fim da mensagem — o dono rolava ate o fundo a cada WO `[relatado pelo dono]`. Sugestao ao kit: o esqueleto trazer um item «Aplicar» (o comando a colar, num bloco de codigo) **antes** do divisor e do Proximo, e dizer que todo comando que o dono copia vai em bloco de codigo, inclusive a resposta que um chat externo devolve (aqui: o JSON do prompt-modelo, DEC-023). Adotado neste projeto na DEC-024.
- **[2026-10-31] O nicho Música é de música tocada; música gerada por IA pede outro eixo.** O `src/niches/music.js` (v1.133.0) fala de DAW, mix e master; num projeto em que a faixa sai do Suno, o artefato é o pedido (style e letra), com limites que cortam em silêncio. Proposta e material em `kit-musica/` (DEC-027), enviados na carta 01 (`261031-cancioneiro-para-kcm-01-kit-de-musica-ia.md`); casa com o i-N25 do KCM. Seção deste feedback para o livro de leitura do KCM: `meta/IDEAS.md`, «Feedback para o Kit».

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
**Revista em 2026-10-29 (DEC-026):** o universal segue descartado; um conversor **por família**, medida como regular, entrou — a família BR, 151 de 151. A conversão por chat ficou para formatos pequenos e irregulares: copiar letra longa sem alterar é onde chat corta.

### x-002 ❌ localStorage como fonte de verdade do acervo
Descartado na fundação: frágil e não versionável. localStorage fica só para estado efêmero. Ver DEC-004.
