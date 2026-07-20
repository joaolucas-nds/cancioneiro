# GLOSSARY.md — Cancioneiro

> Termos próprios do projeto e do domínio (Suno / IA de música). Consultado sob demanda.

---

## Termos do projeto

**Acervo** — o conjunto de todas as canções descritas em JSON no esquema canônico. Vive em `data/`. É a fonte de verdade (DEC-004).

**Bloco / Canção** — a unidade individual: uma música com seus campos (style, lyrics, bpm, key, estado…). "Bloco" enfatiza a apresentação visual em cartão; "canção" enfatiza o dado.

**Coleção** — o container de topo do esquema: agrupa álbuns e a biblioteca de módulos.

**Álbum** — agrupamento de canções dentro da coleção. Serve para organizar e para o export seletivo.

**Módulo de estilo** — fragmento nomeado e reutilizável de descrição sonora (ex.: `melancholic`, `taiko-drums`). Referenciado por id numa canção; ligável/desligável na ferramenta para gerar variações. Ver `schema/style-modules.json`.

**Esquema canônico** — o contrato JSON único (`schema/*.json`) que todos os chats seguem ao gerar canções. Substitui as convenções livres dos álbuns antigos.

**Export** — geração de `.md` legível a partir do JSON, sob demanda (1 canção / álbum / tudo). Saída, nunca entrada.

**Conteúdo copiável vs. referência humana** — distinção inviolável do projeto. *Copiável* = o texto que vai literalmente para um campo do Suno (style, lyrics). *Referência humana* = título, contexto, idioma, rótulos — nunca vai para o Suno. No esquema são campos distintos; na ferramenta, o botão de copiar entrega só o copiável.

## Termos do Suno / domínio

**Style of Music (campo Style)** — campo do Suno que descreve o mundo sonoro: gênero, instrumentos, clima, tempo. Texto livre separado por vírgulas, **sem colchetes**. Mapeia para `style` no esquema.

**Lyrics (campo Lyrics)** — campo do Suno que controla estrutura e vocal (colchetes vão aqui). Para instrumental, recebe `[Instrumental]`. Mapeia para `lyrics` no esquema.

**Meta-tag / tag de estrutura** — instrução entre colchetes no campo Lyrics (`[Intro]`, `[Chorus]`, `[Build]`, `[Outro]`). Guia a arquitetura da faixa. São probabilísticas — o Suno segue "na maioria das vezes", não sempre.

**`[Instrumental]`** — tag que, sozinha no campo Lyrics, reduz o "vocal-fantasma" (voz cantarolando que aparece em faixas instrumentais mesmo com "no vocals" no style). Técnica central para OST instrumental.

**Vocal-fantasma** — voz indesejada que o Suno adiciona a uma faixa instrumental depois de ~15–20s. Mitigada por `[Instrumental]` + `no vocals` redundantes.

**Style de referência / prompt pronto** — um texto de style completo já validado (como os dos álbuns). No Cancioneiro, pode virar um módulo de estilo importável.

**Extend** — recurso do Suno que continua uma geração a partir de um ponto, para alongar a faixa. Nota de versão: v5.5 gera até ~8 min por geração (antes ~2 min), o que reduz a necessidade de Extend para faixas longas.

**Persona / Voices** — recursos de identidade vocal do Suno (salvar/clonar timbre). Só relevantes para faixas com vocal. Nomes e limites mudam por versão — ver HISTORY.

**Creative Sliders** — terceiro sistema de controle do Suno (além de style e meta-tags) introduzido nas versões recentes. Ajuste fino de características. Detalhe e disponibilidade variam por plano/versão.

**v5 / v5.5** — modelos atuais do Suno (jul/2026). O conhecimento técnico do projeto foi verificado contra essa geração; reconfirmar na conta antes de assumir comportamento, pois a interface muda com frequência.

**Custom Mode** — modo do Suno que separa os campos (Style / Lyrics) para controle fino, por oposição ao Simple Mode (descrição única). O Cancioneiro assume Custom Mode.
