# Cancioneiro

Ferramenta local para **organizar, copiar e variar** prompts de música gerados por IA (Suno hoje; agnóstica por design), a partir de um **acervo de canções em JSON canônico**.

> **Estado:** v0.9.1 — ferramenta em uso. Lê o acervo, copia por campo, troca módulos de estilo, ajusta o BPM, **mede cada prompt contra os limites do Suno**, exporta Markdown e **entrega o prompt para chats gerarem canções no esquema**. Publicada no GitHub Pages. Ver `meta/ROADMAP.md`.

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
├── scripts/                   # validador e conversores dos guias antigos
├── data/                      # exemplos no esquema (o acervo pessoal mora fora do repo)
├── app/                       # a ferramenta (index.html)
└── logs/                      # diário do dia
```

## Como começar

1. **Pelo navegador (recomendado):** abra a versão publicada no GitHub Pages — o acervo carrega sozinho.
   **Ou local:** duplo-clique em `app/index.html` (modo `file://`) e clique em *Importar .json* — ou arraste o arquivo para a tela. O último acervo importado fica guardado no navegador e volta quando você reabre.
2. Escolha um acervo de `data/` (ex.: `demo.json`).
3. Navegue por álbuns, copie style e lyrics por botão e o título clicando nele, marque o que usou. Em *Estrutura*, arraste os blocos para mudar a ordem e esconda os que você não usa (o Exclude já vem oculto: o formulário gratuito do Suno v6 não tem o campo).
4. Ligue/desligue **módulos de estilo** por camada para gerar variações — o Style recompõe ao vivo. Para mudar o andamento, use o campo de **BPM** do cartão (ou um chip da camada Andamento, que é atalho para ele): o número muda em todo o Style, nunca aparecem dois. O Suno trata BPM como aproximação.
5. Leia a linha embaixo de cada campo antes de copiar: **vermelho** = o Suno vai cortar o texto (passou do limite, ele trunca sem avisar); **âmbar** = vai funcionar, mas pior (tags demais, ou negação «no X» que rende mais no campo Exclude). Com os módulos abertos, cada chip mostra quantas tags ele põe ou tira (`+2`, `−2`, ou `0` quando não muda nada) — use isso para decidir o que desligar.
6. Exporte em `.md` (faixa, álbum ou acervo inteiro) se precisar do formato legível.

## Validar o acervo

```
pip install jsonschema referencing --break-system-packages
python3 scripts/validate.py
```
Checa todos os `data/*.json` contra o esquema. Rode antes de commitar mudança em `data/` ou `schema/`.

## Converter guias antigos

Guias `.md` da família BR (`..._VOL<n>_GUIA.md`) viram um acervo no esquema com um comando — grave a saída **fora do repo**, porque letra e persona são suas:

```
python3 scripts/convert_br.py ../acervos/rainha-da-preguica.json "../Album Rainha da Preguiça/ALBUM_BR_VOL1_GUIA.md" "../Album Rainha da Preguiça/ALBUM_BR_VOL2_GUIA.md"
```

Liste quantos volumes quiser. O conversor tira os rótulos do que é copiável, não corta nada e diz no fim quantas letras e styles passam do limite do Suno — o painel do app marca as mesmas. Depois, arraste o `.json` gerado para o app. Outras famílias de guia pedem outro conversor (ver `meta/analises/`).

## Gerar canções com um chat

No app, clique em **Prompt**, escreva o seu pedido e copie: o prompt vai inteiro, com o pedido no lugar. Cole num chat novo: ele devolve um arquivo `.json` (ou, se não puder criar arquivo, o JSON num bloco de código, com botão de copiar). Arraste o arquivo para o app. O texto do prompt vive em `schema/PROMPT-PARA-CHATS.md` — o botão busca esse arquivo a cada clique, então o que está no repositório é o que você copia.

**Exemplo** baixa um acervo pronto (`data/demo.json`) para ver a estrutura.

## Fonte de verdade

O acervo canônico são **arquivos JSON** no esquema: os exemplos versionados em `data/`, e o acervo pessoal fora do repo (DEC-026). O navegador (localStorage) guarda as marcações, a estrutura do cartão e uma **cópia do último acervo importado** — cache, nunca a fonte: a linha de origem diz de onde ela veio e quando, e *esquecer* a apaga. Ver `meta/DECISIONS.md` (DEC-004, DEC-022).

## Conhecimento do Suno

O que tem efeito nos campos do Suno (e o que é mito) está consolidado em `meta/HISTORY.md`, com datas e nível de confiança. A interface do Suno muda — reconfirme na conta.

---

*Projeto de hobby pessoal. Documentação e fluxo gerados com o Kit de Contexto Universal.*
