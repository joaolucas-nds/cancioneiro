# Cancioneiro

Ferramenta local para **organizar, copiar e variar** prompts de música gerados por IA (Suno hoje; agnóstica por design), a partir de um **acervo de canções em JSON canônico**.

> **Estado:** v0.7.0 — ferramenta em uso. Lê o acervo, copia por campo, troca módulos de estilo, ajusta o BPM, **mede cada prompt contra os limites do Suno** e exporta Markdown. Publicada no GitHub Pages. Ver `meta/ROADMAP.md`.

## O problema

Canções geradas por chats vivem espalhadas em `.md` de álbum, cada um com convenção própria. Usar uma exige rolar um arquivo enorme, achar o bloco, copiar o estilo, copiar a letra, e lembrar de cabeça o que já foi usado. Pior: rótulos de referência (`[ESTILO SUNO]`, `[LETRA]`) acabam dentro dos blocos copiáveis e viram lixo no Suno.

## A solução

- **Um esquema JSON canônico** (`schema/`) que todos os chats seguem — campos separados para o que é copiável (`style`, `lyrics`) e o que é referência humana (`title`, `context`). Fim da bagunça de convenções.
- **Uma ferramenta** (`app/index.html`) que lê o acervo, mostra cada canção como um cartão dentro do seu álbum, com botão de copiar por campo, marcação de "já usei", troca modular de estilo, **aviso quando o prompt vai ser truncado ou diluído**, e export para `.md`.

## Estrutura

```
cancioneiro/
├── INSTRUCOES-DO-PROJETO.md   # instruções curtas (raiz)
├── CLAUDE.md                  # guia do Claude Code (raiz)
├── .claude/                   # kit do Claude Code (settings + skills: apply-wo, wrap, sondar)
├── meta/                      # contexto do projeto (CEREBRO, CONTEXT, STATUS, ...)
├── schema/                    # o contrato JSON (song, collection, style-modules)
├── data/                      # o acervo real, no esquema
├── app/                       # a ferramenta (index.html)
└── logs/                      # diário do dia
```

## Como começar

1. **Pelo navegador (recomendado):** abra a versão publicada no GitHub Pages — o acervo carrega sozinho.
   **Ou local:** duplo-clique em `app/index.html` (modo `file://`) e clique em *Importar .json*.
2. Escolha um acervo de `data/` (ex.: `demo.json`).
3. Navegue por álbuns, copie style/lyrics por botão, marque o que usou.
4. Ligue/desligue **módulos de estilo** por camada para gerar variações — o Style recompõe ao vivo. Para mudar o andamento, use o campo de **BPM** do cartão (ou um chip da camada Andamento, que é atalho para ele): o número muda em todo o Style, nunca aparecem dois. O Suno trata BPM como aproximação.
5. Leia a linha embaixo de cada campo antes de copiar: **vermelho** = o Suno vai cortar o texto (passou do limite, ele trunca sem avisar); **âmbar** = vai funcionar, mas pior (tags demais, ou negação «no X» que rende mais no campo Exclude). Com os módulos abertos, cada chip mostra quantas tags ele põe ou tira (`+2`, `−2`, ou `0` quando não muda nada) — use isso para decidir o que desligar.
6. Exporte em `.md` (faixa, álbum ou acervo inteiro) se precisar do formato legível.

## Validar o acervo

```
pip install jsonschema referencing --break-system-packages
python3 scripts/validate.py
```
Checa todos os `data/*.json` contra o esquema. Rode antes de commitar mudança em `data/` ou `schema/`.

## Gerar canções com um chat

Cole o conteúdo de `schema/PROMPT-PARA-CHATS.md` num chat de IA junto do seu pedido — ele devolve JSON já no esquema, pronto para importar.

## Fonte de verdade

O acervo canônico são os **arquivos JSON versionados** em `data/`. O navegador (localStorage) guarda só estado efêmero (marcações da sessão) — nunca o acervo. Ver `meta/DECISIONS.md` (DEC-004).

## Conhecimento do Suno

O que tem efeito nos campos do Suno (e o que é mito) está consolidado em `meta/HISTORY.md`, com datas e nível de confiança. A interface do Suno muda — reconfirme na conta.

---

*Projeto de hobby pessoal. Documentação e fluxo gerados com o Kit de Contexto Universal.*
