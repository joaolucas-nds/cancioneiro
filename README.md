# Cancioneiro

Ferramenta local para **organizar, copiar e variar** prompts de música gerados por IA (Suno hoje; agnóstica por design), a partir de um **acervo de canções em JSON canônico**.

> **Estado:** v0.18.0 — ferramenta em uso. Lê, guarda e edita vários acervos, grava direto no arquivo do acervo (Chrome e Edge), copia por campo, troca módulos de estilo, ajusta o BPM, **mede cada prompt contra os limites do Suno**, exporta Markdown, exporta uma faixa como `.json` e **entrega o prompt para chats gerarem canções no esquema**. Publicada no GitHub Pages. Ver `meta/ROADMAP.md`.

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
├── kit-musica/                # o que o projeto sabe do Suno, para projetos de música (skills e bloco)
├── data/                      # exemplos no esquema (o acervo pessoal mora fora do repo)
├── app/                       # a ferramenta (index.html)
└── logs/                      # diário do dia
```

## Como começar

1. **Pelo navegador (recomendado):** abra a versão publicada no GitHub Pages — o acervo carrega sozinho.
   **Ou local:** duplo-clique em `app/index.html` (modo `file://`), clique em *Abrir um acervo*, no começo da barra, e em *Importar .json…* — ou arraste o arquivo para a tela. Cada acervo importado fica guardado no navegador, pelo nome do arquivo: o app reabre no último que você usou, e o seletor de acervo (o mesmo botão, que passa a mostrar o título do aberto) troca de um para outro sem procurar o arquivo.
2. Escolha um acervo de `data/` (ex.: `demo.json`).
3. As faixas aparecem numa **lista**, uma por linha, agrupadas por álbum: copie o Style ou a Lyrics pelos botões da linha, marque o que usou no ✓ e veja a saúde do prompt (● dentro, ▲ atenção, ■ o Suno vai cortar). Clique no título para abrir o **cartão** ao lado, com tudo o que ele tem; ‹ › e as setas ↑ ↓ andam de faixa, e o endereço guarda a aberta. *Cartões*, na barra, volta à grade de antes, onde clicar no título copia o título. Na lateral (em telas largas), clique num álbum para filtrar ou noutro acervo para abri-lo. *Filtros*, na barra, escolhe álbum, estado e uso; cada filtro ligado vira uma etiqueta com ×, e a tecla `/` leva à busca. Em *Estrutura do cartão* (no «⋯», à direita da barra), arraste os blocos para mudar a ordem e esconda os que você não usa (o Exclude já vem oculto: o formulário gratuito do Suno v6 não tem o campo).
4. Ligue/desligue **módulos de estilo** por camada para gerar variações — o Style recompõe ao vivo. Para mudar o andamento, use o campo de **BPM** do cartão (ou um chip da camada Andamento, que é atalho para ele): o número muda em todo o Style, nunca aparecem dois. O Suno trata BPM como aproximação.
5. Leia a linha embaixo de cada campo antes de copiar: **vermelho** = o Suno vai cortar o texto (passou do limite, ele trunca sem avisar); **âmbar** = vai funcionar, mas pior (tags demais, ou negação «no X» que rende mais no campo Exclude). Com os módulos abertos, cada chip mostra quantas tags ele põe ou tira (`+2`, `−2`, ou `0` quando não muda nada) — use isso para decidir o que desligar.
6. Exporte em `.md` (faixa, álbum ou acervo inteiro) se precisar do formato legível. Uma faixa também sai em `.json` (*exportar .json* no cartão): é um acervo de uma faixa só, com os módulos que ela usa, para mandar a um chat ou juntar a outro acervo.
7. Para reorganizar, não há nada a ligar: na Lista, arraste a faixa pela alça ⋮⋮ (para outra posição, outro álbum ou um álbum da lateral; durante o arrastar, a lateral oferece *+ Novo álbum*), ou use o «⋯» da faixa (*Mover para…*, *Subir*, *Descer*, *Excluir…*; `Alt+↑` e `Alt+↓` no título). Marque as caixas para mover, exportar, marcar ou excluir várias de uma vez. Os álbuns têm o próprio «⋯», no cabeçalho e na lateral: *Renomear…* (título e descrição), *Subir álbum*, *Descer álbum*, *Juntar com…* e *Excluir álbum…*; na lateral, a alça ⋮⋮ de cada álbum arrasta. Cada operação mostra *Desfazer* no aviso (ou `Ctrl+Z`), até a próxima. Para trazer faixas de outro `.json`, use *Importar faixas…* no «⋯» da barra, ou solte o arquivo sobre um álbum. As mudanças ficam num rascunho no navegador; a barra mostra quantas são. No Chrome e no Edge do computador, *Salvar* (ou `Ctrl+S`) grava no próprio `.json`: na primeira vez, a janela do sistema pede o arquivo, já com o nome; daí em diante grava direto, e avisa se o arquivo mudou fora do app. O ▾ ao lado tem *Salvar em outro arquivo…* e *Baixar .json*. No Firefox, no Safari e no celular, *Salvar .json* baixa com o nome do arquivo original — substitua o antigo por ele, e ele passa a ser a fonte. Só se organiza um acervo com cópia guardada no navegador (importado por arquivo); no exemplo que o Pages carrega sozinho, o «⋯» só exporta.

## Validar o acervo

```
pip install jsonschema referencing --break-system-packages
python3 scripts/validate.py
```
Checa todos os `data/*.json` contra o esquema e confere que a SortableJS embutida no app é a 1.15.7 sem mudança (pelo sha256). Rode antes de commitar mudança em `data/`, `schema/` ou `app/`.

## Testes

A cada push na `main`, o GitHub Actions roda o `validate.py` (com o esquema), os testes dos conversores e os testes do navegador em `tests/`: o app aberto no Chromium sem tela, com dados só sintéticos (o `data/demo.json` e acervos gerados pelo próprio teste). O resultado aparece como ✓ ou ✗ no commit e na aba **Actions** do repositório. Para rodar na sua máquina:

```
pip install -r tests/requirements.txt
python -m playwright install chromium
python -m pytest tests
```

## Converter guias antigos

Guias `.md` da família BR (`..._VOL<n>_GUIA.md`) viram um acervo no esquema com um comando — grave a saída **fora do repo**, porque letra e persona são suas:

```
python3 scripts/convert_br.py ../acervos/rainha-da-preguica.json "../Album Rainha da Preguiça/ALBUM_BR_VOL1_GUIA.md" "../Album Rainha da Preguiça/ALBUM_BR_VOL2_GUIA.md"
```

Liste quantos volumes quiser. O conversor tira os rótulos do que é copiável, não corta nada e diz no fim quantas letras e styles passam do limite do Suno — o painel do app marca as mesmas. Depois, arraste o `.json` gerado para o app. O conversor é para a primeira geração: se você mudar o `.json` depois — à mão ou, quando a curadoria chegar, no app —, rodar de novo por cima apaga a mudança (DEC-028).

Os guias de formatos mistos (`Albuns/`) vão pelo `scripts/convert_guides.py`, que aceita um mapa de grupos para reagrupar as faixas em álbuns:

```
python3 scripts/convert_guides.py ../acervos/albuns-reagrupados.json ../Albuns/*.md --groups ../acervos/albuns-grupos.json
```

## Kit de música

`kit-musica/` leva o que este projeto sabe sobre o Suno para os projetos de música do Kit de Contexto Modular: um bloco para as Instruções e o CEREBRO do projeto, e duas skills — `macetes-suno` (o que tem efeito) e `revisar-faixa` (conta letra, tags, rótulos e BPM antes de entregar). Instruções de uso em `kit-musica/README.md`.

## Gerar canções com um chat

No app, abra o «⋯» da barra, clique em **Prompt para chats**, escreva o seu pedido e copie: o prompt vai inteiro, com o pedido no lugar. Cole num chat novo: ele devolve um arquivo `.json` (ou, se não puder criar arquivo, o JSON num bloco de código, com botão de copiar). Arraste o arquivo para o app. O texto do prompt vive em `schema/PROMPT-PARA-CHATS.md` — o botão busca esse arquivo a cada clique, então o que está no repositório é o que você copia.

**Baixar exemplo**, no mesmo «⋯», baixa um acervo pronto (`data/demo.json`) para ver a estrutura.

## Fonte de verdade

O acervo canônico são **arquivos JSON** no esquema: os exemplos versionados em `data/`, e o acervo pessoal fora do repo (DEC-026). O navegador guarda **cópias dos acervos importados** (IndexedDB) e, no localStorage, as marcações por acervo e a estrutura do cartão — cache, nunca a fonte: o menu do seletor de acervo diz de onde a cópia veio e quando, e *Esquecer este acervo* a apaga sem tocar no arquivo. Ao organizar, a cópia vira rascunho até você salvar: no Chrome e no Edge do computador, «Salvar» grava no próprio arquivo, vinculado à cópia; nos outros, baixa o `.json` para substituir o antigo. Ver `meta/DECISIONS.md` (DEC-004, DEC-022, DEC-028, DEC-029, DEC-030, DEC-031, DEC-032, DEC-033).

## Conhecimento do Suno

O que tem efeito nos campos do Suno (e o que é mito) está consolidado em `meta/HISTORY.md`, com datas e nível de confiança. A interface do Suno muda — reconfirme na conta.

---

*Projeto de hobby pessoal. Documentação e fluxo gerados com o Kit de Contexto Universal.*
