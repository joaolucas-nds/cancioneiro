# Prompt-modelo — gerar canções no esquema do Cancioneiro

> **Para que serve:** cole o bloco abaixo num chat de IA (Claude, etc.) junto do seu pedido de música.
> O chat passa a devolver a canção/álbum em **JSON no esquema canônico**, pronto para importar
> na ferramenta Cancioneiro — sem inventar convenção própria.
>
> **Como usar:** copie tudo dentro da linha `--- INÍCIO ---` até `--- FIM ---`, cole no chat,
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

## Elementos indesejados
Não escreva "no X" dentro do `style` para remover algo. Coloque em `excludeStyles` (array), que mapeia para o campo Exclude do Suno.

## Esquema JSON de saída
Devolva um objeto de **coleção** com esta estrutura (campos obrigatórios marcados com *):

```json
{
  "schemaVersion": "1.0",              // * sempre "1.0"
  "title": "Nome do álbum ou acervo",  // *
  "description": "opcional",
  "targetTool": "suno",
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
          "style": "...",              // * COPIÁVEL — Style of Music, sem colchetes, cinco camadas
          "lyrics": "...",             // * COPIÁVEL — Lyrics, com colchetes/tags
          "bpm": 120,                  // opcional, número ou null
          "key": "D minor",            // opcional, referência humana
          "excludeStyles": [],         // opcional, array de strings copiáveis p/ Exclude
          "variants": [                // opcional — mesma letra, style alternativo
            { "label": "Nome da variante", "style": "...", "excludeStyles": [] }
          ],
          "styleModules": [],          // opcional — deixe [] a menos que eu peça módulos
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
- Responda **APENAS com o JSON válido**, sem texto antes ou depois, sem cercas de ``` markdown.
- JSON válido: aspas duplas, sem vírgula sobrando, sem comentários.
- Se eu pedir uma única faixa, ainda assim embrulhe em coleção→álbum→[faixa].

## Meu pedido
(descreva aqui as canções que você quer: tema, quantidade, idioma, clima, se instrumental ou com vocal, referências sonoras…)

--- FIM ---

---

## Notas para o mantenedor (não faz parte do prompt)

- Este prompt reflete o `song.schema.json` e `collection.schema.json` v1.0. Se o esquema mudar, **atualize este arquivo junto** (uma fonte por dado — o esquema é a fonte; este prompt é um espelho didático).
- `styleModules` fica vazio por padrão: os ids de módulo são internos da nossa biblioteca; um chat externo não os conhece. Ligar módulos é trabalho da ferramenta, não do chat. Se quiser que o chat proponha módulos, cole também a lista de ids de `style-modules.json`.
- O prompt ensina as cinco camadas e a regra copiável/referência — é o principal contra a bagunça dos álbuns antigos.
- Teste rápido: cole num chat, peça "1 faixa instrumental de tensão", e valide o JSON de volta com a ferramenta (Importar) ou com `scripts/validate.py`.
