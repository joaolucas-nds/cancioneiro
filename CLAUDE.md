# Cancioneiro — guia para o Claude Code

> Arquivo-raiz lido pelo Claude Code em todo turno. Mantenha CURTO (< 200 linhas — custa token em todo turno).
> Regra prática: se remover uma linha e o Claude ainda acerta, ela não pertence aqui. Procedural detalhado → vira skill em `.claude/skills/`.
> O comportamento detalhado do assistente está em `meta/CEREBRO.md`.

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
- Edições nos meta/ são **append-only** pelo Code (STATUS, DECISIONS, CHANGELOG, log); curadoria que reescreve vem do chat (arquivo inteiro OU WO). Divisão completa em DEC-010.
- Ao aplicar uma WO de `meta/workorders/`: ache cada âncora exatamente; se não achar, PARE e reporte. Não mexa fora das edições nomeadas. `git diff` antes do commit.
- Mudança em `schema/` é decisão de arquitetura → registre DEC em DECISIONS.
- **Ao fechar a tarefa, RELATE o trabalho** — o que fez, achados e desvios do que a tarefa pedia, arquivos tocados, resultado do build/validação e o commit. **Não** copie o bloco de fecho do `meta/CEREBRO.md`: aquele é da raia de planejamento, e trocar relatório por formulário perde o que só você viu.

## Quando eu pedir medição
- Eu leio pela pasta vinculada; você lê o disco inteiro. Se eu pedir para **medir**, o pedido não tem âncora nem commit: não edite nada, não conserte nada, não sugira nada.
- Responda com o **número cru e o comando que o produziu**. Sem interpretação, sem recomendação — se você achar que o número indica um problema, diga o número primeiro e a suspeita depois, separada.
- `grep -c` conta LINHAS, não ocorrências. Para ocorrências use `grep -o ... | wc -l`, e diga qual dos dois você mediu.
- Se o alvo estiver fora da raiz do repositório, isso depende de `permissions.additionalDirectories` no `.claude/settings.json` (a mesma chave do relatório em arquivo). Se a leitura for negada, DIGA — não estime.

## Push e relatório — nesta ordem, sempre
- **Verde** (validação passou, ou WO só de doc com o `git diff` conferido) → `add`, `commit` e **`push`, sem perguntar.** Não peça permissão para o que já está decidido.
- **Vermelho** (validação falhou, âncora não encontrada, `git diff` com arquivo fora do previsto) → **não commite e não empurre.** E **não pergunte em prosa** («posso dar push?») — pergunta escrita no meio do texto passa despercebida. Feche com menu pela ferramenta `AskUserQuestion`, a recomendada em primeiro lugar e marcada `(Recomendado)`; sem a ferramenta, menu numerado em texto, dizendo que caiu no fallback.
- **O relatório é o ÚLTIMO passo** — só depois de resolvido o push. Ele diz o que de fato aconteceu: empurrado (com o hash), não empurrado (com o motivo), ou aguardando a escolha do menu. **Relatório escrito antes da decisão conta metade da história** e vira mentira assim que o push sai; se a escolha chegar depois, **reescreva o relatório**, não deixe a versão velha valendo.

## Relatório em arquivo (sempre, sem pedir)
- Ao fechar QUALQUER tarefa (`/apply-wo`, `/wrap`, `/sondar`), grave o MESMO relatório também em `../AAMMDD-HHMM-code-<slug>-<ato>-<alvo>.txt` — pasta-PAI do repo, fora do versionamento. **`<slug>`** = nome curto do projeto. **`<ato>`** = vocabulário FECHADO: `apply` · `wrap` · `probe` · `explore`. **`<alvo>`** = a WO (`wo0002`) quando houver uma; senão, duas ou três palavras com hífen. Exemplo: `261020-0718-code-fatia1-kit-apply-wo0002.txt`.
- O `HHMM` sai de `date +%y%m%d-%H%M`, rodado na hora — nunca de cabeça.
- Exige `permissions.additionalDirectories` no `.claude/settings.json`. Se a escrita for negada, DIGA e siga — o relatório no chat continua sendo a entrega.

## Config (modelo × esforço)
- WO com diff exato já validado, ou edição mecânica em JSON → **Sonnet**, esforço baixo/médio.
- Construir/refatorar a ferramenta, decisão de esquema, julgamento sem rede → **Opus**, esforço alto.
- Esforço proporcional à ambiguidade; `/effort low` para o trivial.
