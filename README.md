# Cancioneiro

Ferramenta local para **organizar, copiar e variar** prompts de música gerados por IA (Suno hoje; agnóstica por design), a partir de um **acervo de canções em JSON canônico**.

> **Estado:** v0.1.0 — Fundação. O esquema e a documentação existem; a ferramenta (`app/index.html`) ainda será construída. Ver `meta/ROADMAP.md`.

## O problema

Canções geradas por chats vivem espalhadas em `.md` de álbum, cada um com convenção própria. Usar uma exige rolar um arquivo enorme, achar o bloco, copiar o estilo, copiar a letra, e lembrar de cabeça o que já foi usado. Pior: rótulos de referência (`[ESTILO SUNO]`, `[LETRA]`) acabam dentro dos blocos copiáveis e viram lixo no Suno.

## A solução

- **Um esquema JSON canônico** (`schema/`) que todos os chats seguem — campos separados para o que é copiável (`style`, `lyrics`) e o que é referência humana (`title`, `context`). Fim da bagunça de convenções.
- **Uma ferramenta** (`app/index.html`) que lê o acervo, mostra cada canção como um cartão dentro do seu álbum, com botão de copiar por campo, marcação de "já usei", troca modular de estilo/BPM, e export para `.md`.

## Estrutura

```
cancioneiro/
├── INSTRUCOES-DO-PROJETO.md   # instruções curtas (raiz)
├── CLAUDE.md                  # guia do Claude Code (raiz)
├── .claude/                   # kit do Claude Code (settings + skills)
├── meta/                      # contexto do projeto (CEREBRO, CONTEXT, STATUS, ...)
├── schema/                    # o contrato JSON (song, collection, style-modules)
├── data/                      # o acervo real, no esquema
├── app/                       # a ferramenta (index.html) — a construir
└── logs/                      # diários de sessão
```

## Como começar (quando a ferramenta existir)

1. Abra `app/index.html` no navegador (duplo-clique — sem instalar nada).
2. Importe um JSON de `data/` (ex.: `exemplo-cinzeiro.json`).
3. Navegue por álbuns, copie style/lyrics por botão, marque o que usou.
4. Exporte uma seleção para `.md` se precisar do formato legível.

## Fonte de verdade

O acervo canônico são os **arquivos JSON versionados** em `data/`. O navegador (localStorage) guarda só estado efêmero (marcações da sessão) — nunca o acervo. Ver `meta/DECISIONS.md` (DEC-004).

## Conhecimento do Suno

O que tem efeito nos campos do Suno (e o que é mito) está consolidado em `meta/HISTORY.md`, com datas e nível de confiança. A interface do Suno muda — reconfirme na conta.

---

*Projeto de hobby pessoal. Documentação e fluxo gerados com o Kit de Contexto Universal.*
