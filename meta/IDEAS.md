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

### i-006 💡 Export MD seletivo (1 canção / 1 álbum / tudo)
Gerar `.md` legível sob demanda a partir do JSON, com o formato limpo (rótulo FORA do bloco copiável). Serve para colar num chat ou subir num Projeto. Fase 2/3.

### i-007 ✅ Estados de canção como no Cinzeiro (ideia→gerada→…→aprovada)
Adotar o ciclo de estados que o FAIXAS.md do Cinzeiro já usa, como campo `state` filtrável na ferramenta. Permite ver "o que falta gerar". Já no esquema; UI de filtro na Fase 2.

### i-008 💡 Importar acervo existente convertendo por álbum
Converter os `ALBUM_*.md` e `album_guia_suno.md` para o esquema, um álbum por vez (semi-assistido por chat), populando `data/`. Começar pelo `album_guia_suno.md` (mais limpo). Backlog do STATUS.

### i-009 💡 Campo de exclusão de estilos ("exclude styles")
A pesquisa apontou que o Suno tem um campo de estilos a excluir que funciona melhor que "no X" no texto. O esquema pode ter um campo `excludeStyles[]` que a ferramenta copia para esse campo do Suno. Avaliar na Fase 3.

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

## Feedback para o Kit

- **[2026-07-19] Nicho pediria uma variante "ferramenta+conteúdo".** Este projeto é dev, mas o "produto" é metade código (app) e metade dado curado (acervo JSON). O template de Desenvolvimento cobre bem a parte código; a parte "acervo de dados como entregável" ficou por conta do CONTEXT. Não faltou nada crítico, mas um nicho híbrido "ferramenta que consome conteúdo estruturado" seria útil.
- **[2026-07-19] Regra de domínio a considerar nas Instruções (DEC-005):** "conteúdo copiável para a ferramenta-alvo nunca leva rótulo de referência dentro do bloco". É a armadilha central deste domínio; virou princípio de projeto. Candidata a entrar nas Instruções no primeiro refino.

- **[2026-07-19] Raia chat×Code confirmada na prática.** Construí o v0 da ferramenta no chat (decisão de forma, com pesquisa de UI e design). A partir daqui, a iteração fina (ajustes pós-validação visual) vai melhor no Claude Code por spec. O ponto de virada chat→Code é "forma decidida → executar deltas".

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
