# CONTEXT.md — Cancioneiro

> O que o projeto é: visão, stack, estrutura, como as peças críticas funcionam, armadilhas. **Estável** — muda pouco.
> Comportamento do assistente vive no CEREBRO.md; o agora vive no STATUS.md.

---

## Visão em uma frase

**Cancioneiro** é uma ferramenta local (HTML+JS, um arquivo, abre no navegador) para **organizar, gerenciar e copiar** prompts de música gerados por IA de texto-para-música (Suno hoje; potencialmente Udio/outros), a partir de um **acervo de canções descrito em JSON canônico** que os chats de IA produzem seguindo um esquema único.

O problema que resolve: hoje as canções vivem espalhadas em vários `.md` de álbum, cada um com convenção própria, e usar cada uma exige rolar um arquivo gigante procurando o bloco certo, copiar o campo de estilo, copiar a letra, e lembrar de cabeça o que já foi usado. Cancioneiro troca isso por: cada canção é um bloco visual num álbum, cada campo tem botão de copiar, o que já foi copiado fica marcado, e estilos/BPM são módulos que se trocam por menu para gerar variações — sem reescrever nada à mão.

## As duas metades do projeto

1. **O esquema (schema/) — o contrato.** Um formato JSON canônico único que descreve uma canção (campos de Suno + metadados) e uma coleção (álbuns, blocos, módulos de estilo). É o que os chats passam a gerar, no lugar dos `.md` de convenção livre. Resolve o problema de padronização na raiz. Ver `schema/song.schema.json`.

2. **A ferramenta (app/) — o leitor.** Um `index.html` autônomo (v0 já construído) que importa/carrega um JSON no esquema, renderiza cada canção como um cartão organizado por álbum, e oferece copy-por-campo com marcação de "já copiado"/"usei", troca modular de estilo por camada (recompõe o Style ao vivo), filtros e busca, e import/download de JSON. Export MD seletivo fica para a Fase 3. **Roda de dois modos** (ver DEC-006): servida por GitHub Pages (`https://`) ela carrega o acervo sozinha; aberta como arquivo local (`file://`) ela espera import manual — auto-detecta o ambiente.

## Por que estas escolhas (resumo — detalhe em DECISIONS)

- **JSON como fonte de verdade, MD como export** (DEC-001): a ferramenta precisa de campos discretos para copy-por-botão e troca modular; parsear MD de convenção livre é frágil (é a causa da bagunça atual). MD vira saída legível sob demanda, não entrada.
- **HTML+JS single-file** (DEC-002): zero setup no Windows, abre com duplo-clique, sem Node/Python, sem servidor. É o padrão das ferramentas concorrentes do nicho.
- **Nome "cancioneiro"** (DEC-003): português, evoca coletânea de canções, não amarra à marca "Suno" — sobrevive a troca de plataforma.
- **Dado canônico em arquivo versionado, não em `localStorage`** (DEC-004): o navegador é cache/rascunho; o JSON no repo é a verdade. Evita perder acervo ao limpar o navegador.

## Stack

| Camada | Escolha | Observação |
|---|---|---|
| Ferramenta | HTML5 + JS vanilla (sem framework, sem build) | Um arquivo `app/index.html`. CSS inline ou `<style>`. |
| Dados | JSON validável por JSON Schema (Draft 2020-12) | `schema/song.schema.json` + `schema/collection.schema.json`. |
| Export | Markdown gerado por JS | Formato limpo (rótulo FORA do bloco copiável). |
| Persistência de sessão | `localStorage` só para estado efêmero (marcações "copiado", filtros) | Nunca fonte de verdade — ver DEC-004. |
| Repositório | Git; desenvolvido no Claude Code + chat de planejamento | Ver seção "Raias" no CEREBRO. |

## Estrutura do repositório

```
cancioneiro/
├── INSTRUCOES-DO-PROJETO.md   # instruções curtas lidas em todo turno (raiz)
├── CLAUDE.md                  # guia do Claude Code (raiz, < 200 linhas)
├── README.md                  # apresentação do repo
├── .gitignore
├── .claude/                   # kit do Claude Code (settings + skills) — vem do zip
├── meta/                      # arquivos de contexto (o "cérebro" do projeto)
│   ├── CEREBRO.md   CONTEXT.md   STATUS.md   DECISIONS.md
│   ├── CHANGELOG.md   IDEAS.md   ROADMAP.md   GLOSSARY.md
│   ├── HISTORY.md   LOG-TEMPLATE.md
│   └── specs/                 # specs de doc para o Code aplicar (chat autora)
├── schema/                    # o contrato JSON
│   ├── song.schema.json       # uma canção
│   ├── collection.schema.json # a coleção (álbuns + módulos)
│   ├── style-modules.json     # biblioteca de módulos de estilo reutilizáveis
│   └── PROMPT-PARA-CHATS.md   # prompt colável p/ chats gerarem no esquema
├── scripts/
│   └── validate.py            # valida data/ contra o schema
├── data/                      # o acervo real, no esquema
│   └── exemplo-cinzeiro.json  # 1 faixa convertida como prova do esquema
├── index.html                 # redireciona para app/ (URL limpa no Pages)
├── app/
│   └── index.html             # a ferramenta (v0 pronto)
└── logs/                      # diários de sessão (fora do Projeto de chat)
```

## Como as peças críticas funcionam

### O modelo de dados (o coração)
Uma **coleção** contém **álbuns**; um álbum contém **canções (blocos)**. Cada canção tem, no mínimo: `id`, `title`, `language`, `style` (o texto do campo Style of Music do Suno), `lyrics` (o texto do campo Lyrics), e `state` (ideia→gerada→…→aprovada). Campos opcionais capturam o que os guias já usavam: `bpm`, `key`, `variants[]` (estilos alternativos para a mesma letra), `styleModules[]` (referências a módulos reutilizáveis), `context`/`notes` (referência humana, nunca vai para o Suno).

**Separação inviolável (a lição dos álbuns antigos):** o que é *referência humana* (título, contexto, idioma, o rótulo "ESTILO SUNO") NUNCA se mistura com o que é *conteúdo copiável* (o texto de style, o texto de lyrics). No JSON são campos diferentes; na ferramenta, o botão de copiar entrega SÓ o conteúdo, sem rótulo. Foi a mistura desses dois no mesmo bloco de código que sujou os álbuns existentes.

### Módulos de estilo (a ideia de "troca por menu")
Um módulo de estilo é um fragmento nomeado e reutilizável de descrição sonora — ex.: `melancholic`, `taiko-drums`, `female-soprano`. Cada módulo pertence a uma das **cinco camadas audíveis** (modelo consolidado do guia usesuno + Cinzeiro, DEC-007): gênero/lane, movimento, instrumentos, voz, clima, produção, andamento. Uma canção referencia módulos por id; a ferramenta agrupa os chips por camada e permite ligar/desligar, recompondo o `style` ao vivo, gerando variações sem reescrever. Os "estilos construídos por chat" podem ser importados como módulos.

### Suno na prática (o que tem efeito, o que não)
Conhecimento destilado no GLOSSARY e no HISTORY (herdado do guia de produção do Cinzeiro + pesquisa 2026). Pontos que moldam o esquema:
- **Dois campos separados** no Suno: *Style of Music* (mundo sonoro, sem colchetes) e *Lyrics* (estrutura + vocal, colchetes aqui). O esquema espelha isso em `style` e `lyrics`.
- **`[Instrumental]`** sozinho no campo Lyrics é a técnica anti-vocal-fantasma para faixas instrumentais.
- **Tags de estrutura** (`[Intro]`, `[Build]`, `[Climax]`, `[Outro]`) só em faixas com arco linear; vocabulário neutro de gênero (evitar `[Drop]`/`[Verse]` fora do gênero certo).
- **Limite de tags:** 1–2 gêneros, 2–4 instrumentos, 1–2 de clima. As primeiras ~20–30 palavras pesam mais.
- **Rótulos de referência dentro do bloco copiável são lixo** — a razão de ser da separação de campos no esquema.

## Armadilhas conhecidas

- **Não parsear MD de convenção livre.** Os álbuns antigos (`ALBUM_*`, `album_guia_suno.md`) usam convenções diferentes entre si (`[ESTILO SUNO]`, `[LETRA]`, `[VAR A]`). A conversão para o esquema é semi-manual/assistida por chat, não um parser universal confiável.
- **`localStorage` não é backup.** Limpar o navegador apaga marcações. O acervo real está no JSON versionado.
- **A interface do Suno muda.** Nomes de botões/menus (Extend, Persona, Custom Mode, Creative Sliders) variam entre versões. O conhecimento no HISTORY tem data — reconfirmar na conta antes de assumir que algo sumiu.
- **Não competir com o gerador genérico.** Já existem builders de prompt (usesuno.com, sunobuilder). O diferencial do Cancioneiro é *organizar o acervo próprio por álbum/bloco com copy marcável e troca modular*, não gerar prompt do zero.

## Produto / uso

Ferramenta pessoal de hobby. Uso típico: abrir `index.html`, importar o JSON do acervo, escolher um álbum, copiar o style de uma faixa (botão), copiar a letra (botão), gerar no Suno, marcar a faixa como usada. Para levar uma seleção a um chat ou Projeto, exportar em `.md`.
