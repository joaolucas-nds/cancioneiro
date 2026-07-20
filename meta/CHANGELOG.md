# CHANGELOG.md — Cancioneiro

> Histórico de versões entregues. SemVer + Keep a Changelog. Cresce no topo.

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
