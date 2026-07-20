# Cancioneiro — guia para o Claude Code

> Arquivo-raiz lido pelo Claude Code em toda sessão. CURTO (< 200 linhas — custa token todo turno).
> Comportamento detalhado do assistente está em `meta/CEREBRO.md`.

## O que é
Ferramenta local (HTML+JS single-file) que lê um acervo de canções em JSON canônico e facilita organizar/copiar/variar prompts para Suno (agnóstico por design). Esquema em `schema/`; ferramenta em `app/index.html`; acervo em `data/`. Fonte de verdade = JSON versionado; MD = export.

## Ritual de início
Leia `meta/CEREBRO.md` → `meta/CONTEXT.md` → `meta/STATUS.md` antes de agir. Confirme em uma frase o que entendeu.

## Regra de domínio inviolável
Conteúdo copiável (`style`, `lyrics`) é campo separado de referência humana (`title`, `context`, `notes`). Nunca misture rótulo dentro do bloco copiável — é a razão de ser do esquema.

## Build / validação
- **Sem build:** a ferramenta é um `app/index.html` autônomo. Abra no navegador para testar.
- **Validar datasets:** `python3 scripts/validate.py` (valida todos os `data/*.json` contra o schema). Rode antes de commitar mudança em `data/` ou `schema/`. Requer `pip install jsonschema referencing --break-system-packages` (sem eles, faz só checagem de sintaxe).
- Mudança só de doc (meta/) NÃO precisa de validação; a rede é o `git diff`.

## Convenções
- Nomes de arquivos/funções/variáveis em inglês; comentários em PT-BR.
- Mensagens de commit **sem acento**.
- Edições nos meta/ são **append-only** pelo Code (STATUS, DECISIONS); curadoria que reescreve vem do chat (arquivo inteiro OU spec de `meta/specs/`).
- Ao aplicar spec de `meta/specs/`: ache cada âncora exatamente; se não achar, PARE e reporte. Não mexa fora das edições nomeadas. `git diff` antes do commit.
- Mudança em `schema/` é decisão de arquitetura → registre DEC em DECISIONS.

## Config (modelo × esforço)
- Spec/diff exato já validado, ou edição mecânica em JSON → **Sonnet**, esforço baixo/médio.
- Construir/refatorar a ferramenta, decisão de esquema, julgamento sem rede → **Opus**, esforço alto.
- Esforço proporcional à ambiguidade; `/effort low` para o trivial.
