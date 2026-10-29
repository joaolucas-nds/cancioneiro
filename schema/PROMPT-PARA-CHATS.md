# Prompt-modelo — gerar canções no esquema do Cancioneiro

> **Para que serve:** cole o bloco abaixo num chat de IA (Claude, etc.) junto do seu pedido de música.
> O chat passa a devolver a canção/álbum em **JSON no esquema canônico**, pronto para importar
> na ferramenta Cancioneiro — sem inventar convenção própria.
>
> **Como usar:** no app, botão **Prompt para chats** — escreva o pedido e copie o prompt já completo.
> Ou, à mão: copie tudo dentro da linha `--- INÍCIO ---` até `--- FIM ---`, cole no chat,
> e complete o "Meu pedido" no final. O chat responde só com o JSON.

---

--- INÍCIO ---

Você vai gerar canções para IA de música (Suno) em um formato JSON específico. Siga estas regras à risca.

## Regra inviolável: separe conteúdo copiável de referência humana
- **Copiável** (vai literalmente para os campos do Suno): `style`, `lyrics`, `excludeStyles`.
- **Referência humana** (nunca vai para o Suno, é só para organização): `title`, `language`, `context`, `notes`, `tags`, `key`.
- NUNCA coloque rótulos como "ESTILO:", "[LETRA]", "[ESTILO SUNO]" dentro de `style` ou `lyrics`. Esses campos contêm APENAS o texto que eu colaria direto no Suno.

## Os dois campos do Suno
- **`style`** = o campo "Style of Music": mundo sonoro (gênero, instrumentos, clima, produção, andamento). Texto separado por vírgulas, **sem colchetes**.
- **`lyrics`** = o campo "Lyrics": estrutura e vocal. Colchetes vão aqui.
  - Faixa instrumental em loop/circular: use apenas `[Instrumental]`.
  - Faixa instrumental linear (com arco: abertura, final): use tags de arco `[Intro]`, `[Build]`, `[Climax]`, `[Outro]`, vocabulário neutro de gênero.
  - Faixa com vocal: escreva a letra com tags de seção (`[Verse]`, `[Chorus]`, `[Pre-Chorus]`, etc.).

## Como construir o `style` — cinco camadas audíveis
Descreva decisões que dá para OUVIR, não elogios ("épico", "lindo", "profissional" não ajudam). Pense em camadas:
1. **Gênero/lane** — a família + um sabor secundário (ex.: "dark ambient cinematic", "k-pop girl crush"). 1–2 gêneros no máximo.
2. **Movimento** — como pulsa (ex.: "driving rhythm", "half-time pulse", "sparse").
3. **Instrumentos** — 2–4, com frase específica ("delicate piano arpeggios" > "piano"). Não empilhe.
4. **Voz** — quem conduz ("close-mic alto", "female soprano", ou "no vocals" se instrumental).
5. **Produção/clima** — espaço da mixagem + 1–2 palavras de clima ("dry upfront mix, intimate", "cinematic, ominous").
Coloque o mais característico NO INÍCIO (as primeiras ~20–30 palavras pesam mais). Se quiser sugerir andamento, inclua "NN bpm" — mas saiba que o Suno trata BPM como aproximação, não comando.

**Orçamento de tags.** Cada trecho entre vírgulas é uma tag. Escreva o `style` com **6 a 8 tags**: menos que 4 fica vago; acima de ~10 as últimas perdem efeito. Prefira juntar ideias numa tag específica ("warm analog synth pads") a espalhar adjetivos soltos ("warm, analog, synth, pads"). Se o `style` tiver "NN bpm", use o mesmo número no campo `bpm`.

## Elementos indesejados
Não escreva "no X" dentro do `style` para remover algo. Coloque em `excludeStyles` (array), que mapeia para o campo Exclude do Suno.

## Módulos de estilo (só se eu pedir variações por módulo)
Um módulo é um trecho de `style` que eu ligo e desligo na ferramenta para gerar variações sem reescrever a faixa. Se eu não pedir módulos, deixe `styleModules` vazio (`[]`) na coleção e nas faixas.
- **Onde moram:** os módulos são declarados UMA vez, no `styleModules` da **coleção** (topo do JSON), como objetos. Nunca escreva o objeto do módulo dentro da faixa.
- **Formato de cada módulo:** `id` (único, minúsculas-com-hífens), `category`, `label` (nome curto para o botão), `fragment` (o trecho copiável: 1 a 3 tags separadas por vírgula, sem colchetes, sem "no X"), `notes` (opcional, referência humana). Não existem outros campos: nada de `enabled`, `default`, `text`, `style` ou `excludeStyles` dentro do módulo.
- **`category`** é exatamente um destes valores: `genre`, `motion`, `instrument`, `vocal`, `mood`, `production`, `tempo`.
- **Na faixa, `styleModules` é uma lista de ids** (texto). Os ids citados são os módulos que já vêm **ligados**; os demais da coleção ficam disponíveis, desligados, para eu experimentar.
- **Orçamento com módulos:** o `style` da faixa continua com 6 a 8 tags, e as tags dos módulos citados somadas às do `style` não passam de 10. Módulo que repete um trecho que já está no `style` não soma nada. Ofereça os módulos extras declarados na coleção, sem citar na faixa.
- **Andamento:** BPM só em módulo de `category` `tempo`, com o fragmento no formato "NN bpm". Em outras categorias, não escreva número de BPM.

## Esquema JSON de saída
Devolva um objeto de **coleção** com esta estrutura (campos obrigatórios marcados com *):

```json
{
  "schemaVersion": "1.0",              // * sempre "1.0"
  "title": "Nome do álbum ou acervo",  // *
  "description": "opcional",
  "targetTool": "suno",
  "styleModules": [                    // opcional — os módulos, declarados uma vez (ver seção acima)
    { "id": "mod-tape-warmth", "category": "production", "label": "Textura de fita",
      "fragment": "tape saturation, vintage warmth", "notes": "opcional, referência humana" }
  ],
  "albums": [                          // *
    {
      "id": "album-slug",              // * minúsculas, hífens
      "title": "Nome do Álbum",        // *
      "description": "opcional",
      "songs": [                       // *
        {
          "id": "faixa-slug",          // * único, minúsculas-com-hífens
          "title": "Título da Faixa",  // * referência humana
          "language": "pt-BR",         // * ou "instrumental", "ja", "en", etc.
          "state": "ideia",            // * um de: ideia | gerada | editada | loop-pronto | aprovada
          "style": "...",              // * COPIÁVEL — Style of Music, sem colchetes, 6 a 8 tags
          "lyrics": "...",             // * COPIÁVEL — Lyrics, com colchetes/tags
          "bpm": 120,                  // opcional, número ou null
          "key": "D minor",            // opcional, referência humana
          "excludeStyles": [],         // opcional, array de strings copiáveis p/ Exclude
          "variants": [                // opcional — mesma letra, style alternativo
            { "label": "Nome da variante", "style": "...", "excludeStyles": [] }
          ],
          "styleModules": ["mod-tape-warmth"], // opcional — SÓ ids da coleção; os citados vêm ligados
          "context": "cena/uso",       // opcional, referência humana
          "notes": "notas de produção",// opcional, referência humana
          "tags": []                   // opcional, etiquetas livres
        }
      ]
    }
  ]
}
```

## Saída
- **Se você consegue criar arquivos para download**, entregue um arquivo `.json` com o nome do `id` do álbum (ex.: `album-slug.json`), contendo só o JSON.
- **Se não consegue**, responda com o JSON inteiro dentro de **um único bloco de código** marcado como `json`, sem texto antes ou depois do bloco.
- JSON válido: aspas duplas, sem vírgula sobrando, sem comentários.
- Se eu pedir uma única faixa, ainda assim embrulhe em coleção→álbum→[faixa].

## Meu pedido
(descreva aqui as canções que você quer: tema, quantidade, idioma, clima, se instrumental ou com vocal, referências sonoras…)

--- FIM ---

---

## Notas para o mantenedor (não faz parte do prompt)

- Este prompt reflete o `song.schema.json` e `collection.schema.json` v1.0. Se o esquema mudar, **atualize este arquivo junto** (uma fonte por dado — o esquema é a fonte; este prompt é um espelho didático).
- **O app lê ESTE arquivo** (botão «Prompt para chats»): busca-o no Pages a cada clique e copia o que está entre as linhas `--- INÍCIO ---` e `--- FIM ---`, trocando a linha entre parênteses abaixo de `## Meu pedido` pelo pedido digitado. Não há segunda cópia do prompt. Mantenha as duas linhas de marcação e essa linha entre parênteses: o `scripts/validate.py` reprova se uma delas sumir.
- **Módulos (DEC-016, DEC-021):** a coleção carrega os próprios módulos; a faixa cita ids. O teste de 2026-10-28 (`meta/specs/261028-prompt-modelo-e-modulos.md`) mostrou que, sem a seção de módulos, três chats inventaram três formatos e aninharam o módulo na faixa — o app abria o painel com 0 chips. As sete `category` são as camadas do app (`LAYERS` em `app/index.html`); a de `tempo` vira atalho do controle de BPM (DEC-020).
- **Orçamento de tags (6 a 8 no style; até 10 com os módulos ligados):** mesma faixa do painel de qualidade (`QUALITY_LIMITS` em `app/index.html`, com fonte e data). Se o painel mudar, mude aqui.
- O prompt ensina as cinco camadas e a regra copiável/referência — é o principal contra a bagunça dos álbuns antigos.
- **Saída em arquivo ou em bloco de código (DEC-023):** o arquivo baixa pronto para arrastar no app; o bloco de código tem botão de copiar que entrega só o JSON. Se a resposta for colada inteira (com as cercas ou texto em volta), a importação extrai o JSON e avisa no toast — não é para depender disso, é rede de segurança.
- Teste ponta a ponta: copie o prompt pelo app, peça algo num chat novo fora de Projeto, baixe o arquivo (ou copie o bloco) e arraste/importe na ferramenta; depois `python3 scripts/validate.py <arquivo>`.
