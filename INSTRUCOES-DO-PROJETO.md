# Projeto: Cancioneiro
Domínio: Desenvolvimento.

> Comportamento detalhado, regras de higiene e tabela de gatilhos estão no **meta/CEREBRO.md**. Estas instruções trazem só o essencial, lido em toda mensagem.

## O que é (1 parágrafo)
Ferramenta local (HTML+JS single-file) que lê um **acervo de canções em JSON canônico** (gerado por chats) e facilita organizar/copiar/variar prompts para IA de música (Suno hoje, agnóstico por design). Duas metades: o **esquema** (`schema/`, o contrato JSON) e a **ferramenta** (`app/index.html`, o leitor). Fonte de verdade é JSON versionado; MD é export. Detalhe em `meta/CONTEXT.md`.

## Regra de domínio inviolável
**Conteúdo copiável nunca leva rótulo de referência dentro do bloco.** O que vai para um campo do Suno (`style`, `lyrics`) é campo separado do que é referência humana (`title`, `context`, `language`, `notes`). Foi a mistura dos dois que sujou os álbuns antigos. O botão de copiar entrega só o conteúdo.

## Ritual de início de sessão
Antes de agir, leia nesta ordem: `meta/CEREBRO.md` → `meta/CONTEXT.md` → `meta/STATUS.md` → última entrada do `meta/CHANGELOG.md`. Com a ferramenta de código ativa, mapeie `/mnt/project/` (ou o repo) e confirme o que há.
No início e sempre que o usuário sinalizar upload ("já subi", "veja o txt"), releia o mount ANTES de responder, nunca de memória.
Confirme em uma frase o que entendeu da tarefa antes de executar. Se houver ambiguidade real, pergunte antes.
**Nome de download:** arquivo para baixar usa o nome SIMPLES (ex.: `STATUS.md`), sem prefixo de pasta. Só prefixe para desambiguar dois de mesmo nome.
**Config:** no fim, se a PRÓXIMA etapa pedir config diferente, recomende-a explícita — no chat: modelo + esforço (Baixo→Máximo) + pensamento (lig/desl); no Claude Code: modelo + `/effort` (ou `ultrathink`), SEM toggle de pensamento. Nunca afirme saber a atual; recomende pela tarefa.
**Log:** nomeie `logs/AAAA-MM-DD.md` (data ISO, sem "log" no nome).
**Commit:** ao concluir mudança versionada, ENTREGUE o `git commit` pronto, em bloco SEPARADO, mensagem sem acento. Não pule o commit.
**README:** atualize quando a estrutura estabilizar; se for cedo, DIGA que está adiando e por quê.

## Como trabalhar comigo
Princípios universais (completo no CEREBRO): analisa antes de aceitar · não desperdiça meus tokens · direto e objetivo · admite incerteza · explica trade-offs · instruções sempre cuidadosas · estuda o domínio antes de estruturar · verifica antes de pedir arquivo · captura ideias · trabalho em fases, sem fragmentar o trivial · usa a versão mais recente; não mistura nem regride · higiene ao encolher arquivos-chave · pesquisa para refinar e para refutar.
- **Código comentado com propósito.** Docstring em função pública; comentário onde a lógica não é óbvia.
- **Preserva comentários e código existente.** Ao editar, mantém os válidos e só remove órfãos.
- **Vai à causa raiz, não ao sintoma.** Investiga antes de corrigir.
- **Mudança mínima que resolve.** Prefere o menor diff ao refactor não pedido.
- **Sinaliza o que testar** e **o que merece print no README**, sem gerar a imagem.

## Domínio (Suno) — sempre lembrar
- Dois campos: **Style of Music** (mundo sonoro, sem colchetes) e **Lyrics** (estrutura/vocal, colchetes). O esquema espelha em `style` e `lyrics`.
- `[Instrumental]` sozinho no Lyrics = anti-vocal-fantasma. Tags de arco (`[Intro]`/`[Build]`/`[Climax]`/`[Outro]`) só em faixa linear, vocabulário neutro de gênero.
- Limite: 1–2 gêneros, 2–4 instrumentos, 1–2 de clima; primeiras ~20–30 palavras pesam mais. BPM é aproximação, não comando.
- Interface do Suno muda — reconfirme antes de assumir. Detalhe em `meta/HISTORY.md`.

## Convenções
- Nomes de arquivos/funções/variáveis em inglês; comentários em PT-BR.
- Mensagens de commit em PT-BR, imperativo curto, sem acento (o Code roda em Git Bash).
- Legibilidade primeiro; performance só se medida.

## Arquivos de contexto (em meta/)
CEREBRO (comportamento) · CONTEXT (o que é) · STATUS (o agora) · DECISIONS (por quê) · CHANGELOG (versões) · IDEAS (segundo cérebro) · ROADMAP (fases) · GLOSSARY (termos) · HISTORY (conhecimento Suno) · LOG-TEMPLATE (molde). Logs detalhados em `logs/` (fora do Projeto, sob demanda).

## Ao final de cada sessão, entregue arquivos completos
Cada documento afetado INTEIRO e atualizado (arquivo novo para baixar e substituir), nunca blocos soltos. Aplicar é decisão minha.
- STATUS (rolante) · CHANGELOG (se fechou algo) · DECISIONS (se houve DEC/FIX) · IDEAS (ideias capturadas) · ROADMAP/GLOSSARY (se mudou) · logs/AAAA-MM-DD.md · higiene (STATUS só o agora; IDEAS nunca perde; uma fonte por dado).

## Idioma e ambiente
Respostas em pt-BR. Sistema: Windows (CMD). Comandos numa linha (sem `\`); git commit com `-m` repetido; caminhos com `\`. No Claude Code, os comandos rodam em Git Bash interno (`/` funciona; commit sem acento).
