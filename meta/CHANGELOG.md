# CHANGELOG.md — Cancioneiro

> Histórico de versões entregues. SemVer + Keep a Changelog. Cresce no topo.

---

## [0.9.1] — 2026-10-29

Ajustes de tela pedidos pelo dono depois de conferir a 0.9.0 (nota `261029-1618.txt`, DEC-025), vistos na tela. E o primeiro conversor dos guias antigos (i-008, DEC-026).

### Added
- **Conversor da familia BR (`scripts/convert_br.py`, DEC-026):** le os guias `..._VOL<n>_GUIA.md` da «Rainha da Preguiça» e grava uma colecao no esquema, um album por volume. Tira os rotulos `[ESTILO SUNO]` e `[LETRA]` do que e copiavel, leva as variantes `VAR A/B` e os campos de referencia (Conceito, Voz, Instrumentos, conversa de origem). Conversao fiel: letra longa e style com tags demais nao sao cortados, o relatorio conta. Teste com guia sintetico em `scripts/test_convert_br.py` (8 casos, sem letra real no repo). Medido no acervo do dono: 151 de 151 faixas, 10 albuns; o arquivo gerado fica fora do repo.

### Changed
- **Cabecalho:** a versao fica pequena abaixo do nome, sem o subtitulo; «Prompt», «Exemplo» (icone de baixar) e «Estrutura» (icone de camadas) ficam ao lado do nome; importar, baixar e exportar ficam na ponta direita.
- **Titulo:** clicar no nome da faixa copia o titulo, com «copiado ✓» ao lado; sai o botao «copiar titulo», que quebrava a linha.
- **Estrutura do cartao:** as linhas se arrastam para mudar a ordem (os ↑ ↓ ficam, para o teclado). O padrao passa a **esconder o Exclude** — o formulario gratuito do Suno v6 nao tem o campo; o aviso «no X → Exclude» some junto (D3). Quem tinha salvo o padrao antigo passa ao novo; estrutura personalizada fica como estava.

---

## [0.9.0] — 2026-10-29

Conveniencias de uso, conferidas na tela e retestadas pelo dono.

### Added
- **Estrutura do cartao (DEC-023, i-030):** ordem e mostrar/ocultar de seis blocos (Style, Lyrics, Exclude, Modulos, Variantes, Notas), guardada no navegador; «Restaurar padrao».
- **Copiar o titulo da faixa (i-033).**
- **Arrastar o `.json` para a tela importa (i-034)**, pelo mesmo caminho do botao.
- **O ultimo acervo importado volta ao abrir (DEC-022, i-035):** copia em cache no navegador; a barra mostra de onde veio e quando, com «esquecer». Vence a carga automatica do Pages.

### Changed
- **Prompt-modelo (DEC-023, i-036):** a «Saida» pede um `.json` para baixar; sem arquivo, o JSON num unico bloco de codigo. Reteste do dono com dois chats: 6 de 6 faixas no contrato e no orcamento; os arquivos vieram com o nome do `id` do album, como o prompt pede para o arquivo.
- **Importacao:** aceita a resposta do chat colada inteira — extrai o bloco de codigo (ou do primeiro `{` ao ultimo `}`) e avisa no toast.
- **Export de album e de acervo com o Style da tela (D5, i-037):** modulos ligados e BPM do controle, como o da faixa. Conferido no `.md` exportado pelo dono: 18 tags em ar-01, igual ao cartao.
- **Painel de qualidade:** com o Exclude oculto, nao sugere levar «no X» para ele.

---

## [0.8.0] — 2026-10-29

Prompt-modelo com contrato de modulos e o prompt pela interface do app, conferidos na tela e retestados pelo dono.

### Added
- **Botoes «Prompt para chats» e «Baixar exemplo» (DEC-021, i-031):** a janela do primeiro recebe o «Meu pedido» e copia o prompt-modelo inteiro com o pedido no lugar; o segundo baixa `cancioneiro-exemplo.json`. Os dois buscam `schema/PROMPT-PARA-CHATS.md` e `data/demo.json` no clique — o app nao guarda copia; falhando a busca, a janela mostra o link da versao publicada.
- **`scripts/validate.py` confere o prompt (sexta checagem):** reprova se sumirem as marcacoes que o botao le (`--- INÍCIO ---`, `--- FIM ---` e a linha entre parenteses abaixo de `## Meu pedido`).

### Changed
- **Prompt-modelo (DEC-021, i-028):** ensina o contrato de modulo da DEC-016 (modulos no `styleModules` da colecao com `id`, `category`, `label`, `fragment`, `notes`; a faixa cita ids; citado = ligado), o orcamento (style com 6 a 8 tags; ate 10 com os modulos ligados) e que BPM em modulo so vai na camada `tempo`. Reteste do dono com dois chats: 6 de 6 faixas dentro do orcamento, 0 modulos fora do contrato, 0 rotulos — contra 0 de 3 chats no contrato antes.
- **Toast:** dura conforme o tamanho da mensagem (2,2 a 6 s), para os avisos longos darem tempo de ler.

### Fixed
- **FIX-009:** modulo declarado dentro da faixa sumia em silencio no app (painel com 0 chips) e derrubava o `validate.py` com traceback. Agora o validador reprova com mensagem por item, e a importacao — por arquivo ou pela carga automatica — diz quantos modulos citados nao existem na colecao.

---

## [0.7.0] — 2026-10-28

Fase 3b: o controle de BPM no cartao, conferido na tela pelo dono.

### Added
- **Controle de BPM (DEC-020, i-005):** o «128 BPM» da linha de metadados virou um campo (20 a 300, `−5`/`+5`, «voltar a N») que governa todo «NN bpm» do Style principal — base e modulos —, reescrito no lugar, antes da dedup. Botao copiar, linha de qualidade, recomposto e export MD («BPM: N» e o bloco) usam o valor do controle. Variantes e o «Baixar .json» nao mudam; o valor e so da sessao, como os modulos. Valor invalido nao chega ao Style.
- **Chip de andamento como atalho:** ligar um chip da camada Andamento move o controle para o numero dele e desliga o outro; no maximo um ligado. Antes, 49 de 49 cliques punham um segundo BPM no prompt.
- **`scripts/validate.py` confere o BPM (quinta checagem):** reprova faixa com dois BPM diferentes no style, ou com campo `bpm` diferente do numero do style (ou sem numero nele).

### Fixed
- **FIX-008:** filtro, busca e «marcar usei» religavam os chips do acervo enquanto o bloco de Style seguia com o clique — o botao copiar entregava um texto que os chips nao explicavam. O estado de sessao sobrevive ao re-render e so volta ao acervo ao importar de novo.

---

## [0.6.0] — 2026-10-27

Fase 3a.2: o custo de cada modulo no chip, conferido na tela. E a versao passa a aparecer no app.

### Added
- **Custo de cada modulo no chip (DEC-019):** com o painel de modulos aberto, cada chip mostra quantas tags ele muda no Style daquele cartao — `−N` ligado, `+N` desligado, `0` quando nao muda o prompt (o chip que antes acendia sem efeito nenhum). Recalculado em todos os chips a cada clique, so com o painel aberto. A linha de qualidade passa a dizer quanto o style base usa sozinho quando o recomposto passa de 10 tags. A lista de corte automatica foi descartada: medida, ela mandaria cortar a voz de rap em faixas de rap-pop.
- **A versao na tela (i-027):** o cabecalho do app mostra `v0.6.0`. Todo print passa a ser datavel.
- **`scripts/validate.py` confere a versao:** o topo do CHANGELOG, o app, o README e o STATUS tem de dizer a mesma; senao, codigo 1.

### Fixed
- O cabecalho do `scripts/validate.py` dizia «checa duas coisas» desde a WO 0006, que acrescentou a terceira; agora lista as quatro.

---

## [0.5.0] — 2026-10-27

Painel de qualidade do prompt (Fase 3a) e quatro correcoes que o tornaram confiavel. Tudo o que entrou no app desde a 0.4.1.

### Added
- **Painel de qualidade (DEC-018):** abaixo de Style, Lyrics e Exclude, uma linha que mede o que vai para o Suno — caracteres contra o limite do campo (Style e Exclude 1.000; Lyrics 5.000, com aviso a partir de ~3.000), tags do Style (ambar acima de ~10, nunca vermelho) e negacoes «no X» (por fronteira de palavra; so avisa; `no vocals` nao dispara em faixa instrumental). Mede o Style **recomposto** e se atualiza a cada clique num chip de modulo. Vermelho reservado ao truncamento, o unico caso que perde texto. Limites num objeto unico, com fonte e data.
- **`scripts/validate.py`:** checagem de integridade referencial (todo id em `songs[].styleModules` existe no `styleModules[]` da propria colecao — DEC-016), e a ultima linha passa a declarar se o esquema foi de fato conferido.
- `meta/specs/` (primeira spec: o painel) e `meta/analises/` (primeira analise: o round-trip do acervo).

### Fixed
- **FIX-004:** o «Baixar .json» gravava um `Set` serializado como `{}` em cada faixa, e o «Importar .json» quebrava nele — o app estragava o proprio arquivo. O estado dos modulos ligados saiu de dentro da colecao.
- **FIX-005:** a importacao relatava qualquer falha como «nao e um JSON valido», e o `validate.py` dizia «Tudo conforme ao esquema» sem ter conferido esquema nenhum. Mensagem que nomeia um resultado so pode vir da operacao que o produz.
- **FIX-006:** arquivos ja contaminados continuavam propagando a chave interna. A importacao saneia as chaves com prefixo `_` e **diz quantas removeu**.
- **FIX-007:** o botao «copiar» do Style entregava o texto de antes do clique no chip de modulo. O que se via nao era o que se colava no Suno; a troca de estilo por modulo so chegava ao Suno pelo export MD.

### Changed
- **DEC-016 — acervo autossuficiente:** cada colecao traz os modulos que suas faixas citam; `schema/style-modules.json` e biblioteca de referencia para autoria. `data/exemplo-cinzeiro.json` recebeu os 5 modulos que citava sem ter.
- Kit de contexto atualizado de v1.74.0 para v1.131.0 (DEC-010 a DEC-015, DEC-017) — processo e documentacao, nenhuma mudanca de produto.

---

## [0.4.1] — 2026-07-21

Auditoria: correção de bug no dedup e alinhamento da documentação.

### Fixed
- **FIX-003: falso positivo no dedup do Style.** A comparação por substring crua barrava fragmentos legítimos — "female vocals" era descartado quando a base tinha "male vocals" (uma é substring da outra), e "harp" era barrado por "harpsichord". Passou a comparar **sequências de palavras**, com normalização simples de plural. 14 checks, incluindo regressão do FIX-002.
- Documentação desalinhada com o código: README anunciava "v0.1.0 — ferramenta a construir" (estava em 0.4.0 e publicada); CONTEXT dizia que o export MD ficaria para a Fase 3 (já entregue); ROADMAP e IDEAS marcavam o campo de exclusão como pendente (já implementado); STATUS listava no backlog a publicação no Pages (já feita) e a validação visual (já ocorrida).

### Added
- **HISTORY §9-13:** limites de campo verificados (Style ~1.000 chars, Lyrics 5.000 com ponto doce em ~3.000, título 100) e o achado central de que **o Suno trunca em silêncio**; teto prático de tags (~5-10, acima de 10 o modelo ignora as finais); ordem de tags (gênero primeiro); campo de exclusão mais confiável que negação no texto; mudanças de interface de jul/2026 (Lyrics Editor, Lyricist); contexto do processo GEMA.
- README: seções de validação do acervo e de geração por chat.

---

## [0.4.0] — 2026-07-21

Export para Markdown e correção do Style recomposto.

### Added
- **Export MD** (i-006): botões para exportar em Markdown a faixa (rodapé do cartão), o álbum (cabeçalho do álbum) e o acervo inteiro (cabeçalho). O `.md` mantém a regra inviolável — rótulo fora, conteúdo copiável em bloco limpo. Export de faixa usa o Style recomposto com os módulos ligados.

### Fixed
- **FIX-002: duplicação no Style recomposto.** Ligar módulos repetia conceitos já presentes no style base (ex.: base "dark ambient cinematic intro" + módulo "dark ambient cinematic" → ambos no texto), poluindo o prompt e desperdiçando as primeiras palavras (as que mais pesam no Suno). O dedup passou a comparar **por contenção**, não só igualdade exata.

### Changed
- `downloadCollection` refatorado sobre helper genérico `downloadFile`; cabeçalho do álbum alinhado ao centro.
- DEC-008 revisada após falha real de entrega (ver DECISIONS).

---

## [0.3.0] — 2026-07-19

Fecha o ciclo chat→ferramenta e adiciona validação de acervo.

### Added
- **`schema/PROMPT-PARA-CHATS.md`**: prompt-modelo colável que instrui qualquer chat a gerar canções no esquema canônico (ensina as cinco camadas audíveis, a regra copiável/referência, os dois campos do Suno e a saída em JSON puro). Fecha o ciclo "chat gera → ferramenta lê" (i-002/i-014).
- **`scripts/validate.py`**: valida `data/*.json` contra o schema (sintaxe + conformidade estrutural via jsonschema/referencing). Retorna código 1 em erro. Testado com caso negativo (id inválido, state fora do enum, campo faltando).

### Changed
- CLAUDE.md: passo de validação agora aponta para `scripts/validate.py`.

### Notas
- Verificação de integridade do repo confirmada: datasets conformes ao schema, lógica 11/11, HTML íntegro.

---

## [0.2.0] — 2026-07-19

Ferramenta v0 construída. Modelo das cinco camadas audíveis incorporado. Hospedagem definida.

### Added
- **Ferramenta `app/index.html`** (single-file, sem build): cartões por álbum; copiar Style/Lyrics/Exclude por botão; marcação "usei" automática (ao copiar) e manual (toggle); filtros por álbum/estado/uso; busca textual; painel de módulos de estilo por camada que recompõe o Style ao vivo; variantes e notas recolhíveis; importar/baixar JSON.
- **`index.html` raiz** que redireciona para o app (URL limpa no GitHub Pages).
- **`data/demo.json`**: 2 álbuns (instrumental + vocal), 3 faixas, com a biblioteca de módulos embutida.
- Biblioteca de módulos expandida para **27 módulos** nas cinco camadas audíveis (genre/motion/instrument/vocal/mood/production/tempo).

### Changed
- Categorias de módulo agora espelham as cinco camadas audíveis do modelo usesuno (DEC-007).

### Fixed
- FIX-001: auto-load do acervo tenta múltiplos caminhos (`data/` e `../data/`), corrigindo o fetch com o app em subpasta no GitHub Pages.

### Decisões (ver DECISIONS.md)
- DEC-006: GitHub Pages + carregamento auto-detectado (fetch/import).
- DEC-007: categorias de módulo = cinco camadas audíveis.
- FIX-001: caminho relativo do fetch.

### Notas
- Validação visual da ferramenta ainda pendente (screenshot bloqueado pela rede do container; lógica testada com 11/11 checks headless).

---

## [0.1.0] — 2026-07-19

Fundação do projeto. Arquitetura definida, esquema JSON canônico criado, documentação de contexto completa.

### Added
- Repositório inicial com estrutura de pastas (`meta/`, `schema/`, `data/`, `app/`, `logs/`).
- **Esquema JSON canônico:** `schema/song.schema.json` (canção), `schema/collection.schema.json` (coleção/álbuns), `schema/style-modules.json` (biblioteca de módulos de estilo reutilizáveis).
- **Dataset de prova:** `data/exemplo-cinzeiro.json` — faixa "Abertura das Forjas" (Cinzeiro-OST) convertida para o esquema, validando cobertura dos campos.
- Documentação de contexto completa: CONTEXT, STATUS, DECISIONS, CHANGELOG, IDEAS, ROADMAP, GLOSSARY, HISTORY, LOG-TEMPLATE.
- Arquivos-raiz: INSTRUCOES-DO-PROJETO.md, CLAUDE.md, README.md, .gitignore.
- Log de sessão `logs/2026-07-19.md`.

### Decisões (ver DECISIONS.md)
- DEC-001: JSON canônico como fonte de verdade, MD como export.
- DEC-002: ferramenta em HTML+JS single-file.
- DEC-003: nome "cancioneiro" (agnóstico de plataforma).
- DEC-004: dado canônico em arquivo versionado, não em localStorage.
- DEC-005: adaptação das Instruções ao domínio música/ferramenta.

### Notas
- A ferramenta (`app/index.html`) ainda não existe — é o marco da próxima fase.
- Conhecimento técnico do Suno herdado do guia de produção do Cinzeiro-OST e refinado com pesquisa de jul/2026 (v5.5) — consolidado em HISTORY.md.
