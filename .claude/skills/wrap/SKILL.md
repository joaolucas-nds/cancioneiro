---
name: wrap
description: Encerra a tarefa — append em STATUS/DECISIONS, git diff e comando de commit. Use quando o usuário pedir /wrap ou para fechar a sessão de trabalho.
disable-model-invocation: true
---
Encerre a tarefa: atualize `meta/STATUS.md` (append, não reescreva), acrescente `DEC-`/`FIX-` em `meta/DECISIONS.md` se houve decisão/bug,
e me mostre o `git diff` e o comando de commit (uma linha por comando, mensagem SEM acento).
