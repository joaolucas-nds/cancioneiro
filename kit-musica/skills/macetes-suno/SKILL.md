---
name: macetes-suno
description: O que tem efeito no Suno e o que é mito — os dois campos, o style em camadas, o orçamento de tags, os limites que cortam em silêncio, BPM, instrumental, exclusão, o que fazer depois de ouvir, as ferramentas do Suno (Replace Section, Extend, Remaster, Cover, Voices, Letrista) e as configurações de geração do v6 (Variety, Max Mode). USE ao escrever ou reescrever o style ou a letra de uma faixa para o Suno, ao montar variantes, quando o dono relatar o que ouviu, e quando perguntar «por que saiu assim?» ou «como faço o Suno fazer X?». Para conferir uma faixa pronta, use a skill revisar-faixa.
---

# Macetes do Suno — o que tem efeito

> Parte do kit de música do Cancioneiro (`kit-musica/`). Fonte: `meta/HISTORY.md` do Cancioneiro, que
> traz cada item com data, fonte e nível de confiança. **Conferido em 2026-10, Suno v6; §10 e §11 em 2026-11; §12 em 2026-11-15 e 2026-11-16.** A interface
> do Suno muda: se o dono disser que um botão ou campo não existe na conta dele, acredite nele.

## 1. Dois campos, dois trabalhos

- **Style of Music** = o mundo sonoro: gênero, instrumentos, voz, clima, produção, andamento. Texto
  separado por vírgulas, **sem colchetes**.
- **Lyrics** = a arquitetura no tempo: seções e voz. **Colchetes moram aqui** (`[Verse]`, `[Chorus]`).

Ruim: `[ESTILO SUNO] k-pop, synth` no Style. O rótulo é texto que o Suno lê como pedido.
Bom: `k-pop girl crush, punchy synth bass, …` — só o que se cola.

**Regra que não se dobra:** rótulo de referência (título, «ESTILO SUNO», «LETRA», «VAR A», idioma, nota)
nunca entra no texto que vai para o Suno. No JSON do Cancioneiro isso já é estrutural: `style` e `lyrics`
de um lado; `title`, `context` e `notes` do outro.

## 2. O style em cinco camadas audíveis

1. **Gênero** — uma família e um sabor (`dark ambient cinematic`). No máximo dois gêneros.
2. **Movimento** — como pulsa (`driving rhythm`, `half-time pulse`, `sparse`).
3. **Instrumentos** — de 2 a 4, com frase específica (`delicate piano arpeggios` > `piano`).
4. **Voz** — quem conduz (`close-mic alto`, `male duo tenor and baritone`, `no vocals`).
5. **Produção e clima** — o espaço da mixagem e uma ou duas palavras de clima.

Descreva o que dá para **ouvir**. «Épico», «lindo», «profissional» não mudam nada.
**O começo pesa mais:** as primeiras ~20 a 30 palavras mandam. Gênero primeiro; detalhe depois.

## 3. Orçamento de tags

Cada trecho entre vírgulas é uma tag. **De 6 a 8 tags**; abaixo de 4 fica vago; **acima de ~10 as
últimas perdem efeito** e os sinais se anulam em resultado genérico.

Ruim: `warm, analog, synth, pads, dreamy, soft, lush, airy, nostalgic, retro, 80s, chill` (12 adjetivos
soltos).
Bom: `warm analog synth pads, dreamy 80s nostalgia, airy close vocal` (3 tags que dizem mais).

Precisa cortar? Em geral: gênero > clima > instrumento principal > voz > BPM. **Exceção:** em gênero
centrado na voz (rap, rap-pop) a voz é o gênero — não corte a voz primeiro.

## 4. Limites — o Suno corta em silêncio

| Campo | Limite | Na prática |
|---|---|---|
| Style | ~1.000 caracteres | sobra muito: o problema é o número de tags, não o tamanho |
| Lyrics | 5.000 caracteres | **a partir de ~3.000 o Suno corre**: pula seções, encurta |
| Título | 100 caracteres | — |

Passou do limite, o excedente **não chega** — sem erro, sem aviso. A letra longa é o defeito mais comum:
refrão repetido por extenso quatro vezes come mil caracteres. Escreva o refrão completo uma ou duas vezes
e marque as repetições com a tag (`[Chorus]`).

## 5. BPM é aproximação

- `NN bpm` no style ajuda a mirar o andamento; o Suno **não obedece com precisão**.
- **Um número por faixa.** Dois números («95 BPM to 118 BPM») viram ruído para o Suno e confusão para o
  controle de BPM do Cancioneiro. Para acelerar, descreva (`gradual build, accelerating`), não some números.
  Se a rampa for escolha consciente, escreva-a num trecho só (`95 BPM building to 115 BPM`): desde a 0.19.0 o
  Cancioneiro a reconhece, copia como está e avisa em âmbar; dois números soltos continuam sendo erro.
- O campo `bpm` do JSON repete o número do style.

## 6. Instrumental

- **Faixa em loop** (exploração, estudo): Lyrics só com `[Instrumental]`, nada mais; no style, `no
  vocals` como reforço. Sem isso, o Suno tende a cantarolar depois de ~15 a 20 segundos.
- **Faixa com arco** (abertura, final, trailer): tags de arco no Lyrics — `[Intro]`, `[Build]`,
  `[Climax]`, `[Outro]`, com descrição curta (`[Build: percussão entra]`). Vocabulário **neutro de
  gênero**: `[Drop]` é de EDM, não de orquestra.
- Roteiro de tempos («0:00–0:30 build») é nota para quem edita, não texto do Lyrics.

## 7. Tirar algo: Exclude, não «no X»

`no drums` dentro do style funciona mal; o campo **Exclude** funciona melhor. No JSON, vai em
`excludeStyles`. **O v6-mini (plano gratuito) não mostra o campo Exclude** — ali, uma ou duas negações no
style são o recurso que sobra; mais que isso dilui.

## 8. Mitos que circulam

- «O style caiu para 200 caracteres» — é o limite do v4, copiado para guias novos.
- «O BPM agora é respeitado com precisão» — não está em material oficial.
- «Tag X no fim da lista funciona melhor» — o começo pesa mais, não o fim.
- Números exatos de blog («9 em 10 gerações») são estimativa de quem vende curso.

## 9. O que o assistente não sabe

O assistente **não ouve** o resultado. Ele escreve o pedido e explica o porquê; o dono gera, ouve e diz o
que saiu. «Ficou bom» só quem ouviu pode dizer. Quando o resultado sair estranho, pergunte primeiro: passou
de algum limite? quantas tags? tinha rótulo no texto?

## 10. Depois de ouvir: uma variável por vez

O dono gerou e contou o que ouviu. Antes de reescrever, separe **o que ficou bom** do **que não ficou**,
e mude **uma coisa só** por rodada — duas mudanças juntas não dizem qual funcionou.

| O dono disse | Mude isto, e só isto |
|---|---|
| «o gênero/clima não é esse» | as primeiras tags do style (o começo pesa mais) |
| «tem instrumento sobrando/faltando» | uma tag de instrumento, ou o Exclude |
| «o style que aparece na faixa não é o que eu colei» | nada no texto: ponha **Variety em Off** e gere de novo (§12) |
| «a voz não é essa» | a tag de voz; para manter a mesma voz em várias faixas, style fixo com Variety em Off, ou Voices (§11) |
| «a faixa segue tocando depois que a letra acaba» | não peça de novo: **Recortar** o fim (plano gratuito). `[End]` no fim da letra não encurtou a cauda de forma visível no projeto Rainha da Preguiça (2026-11-15); a última linha sem repetir a anterior ainda ajuda (`escrever-letra-suno` §6, §9) |
| «correu / pulou parte da letra» | a letra: está acima de ~3.000? refrão por extenso repetido? (`revisar-faixa`) |
| «cantou onde era instrumental» | `[Instrumental]` sozinho no Lyrics (§6) |
| «está bom, mas um trecho ficou fraco» | não peça de novo: Replace Section ou Extend (§11) |

**Onde guardar a mudança, sem reescrever a faixa:** um style alternativo vai em `variants[]` da faixa; uma
frase que serve a várias faixas vira **módulo** da coleção (ligável no Cancioneiro). Registre o relato no
`FAIXAS.md` do projeto com a **data** e a **versão do Suno** — ele é a única medida de som que existe.

**Conte as gerações:** em geral são várias por resultado bom. Três rodadas sem melhorar com uma variável
de cada vez é sinal de que o pedido brigou consigo mesmo (sinais opostos no style, letra longa demais): volte
à `revisar-faixa` antes da quarta.

## 11. Ferramentas do Suno: quando usar em vez de pedir de novo

> Lido em 2026-11-09 na página de produtos e na central de ajuda do Suno, e num guia verificado em 2026-09
> (fontes no fim). Nomes, planos e limites mudam: se o dono disser que não existe na conta dele, acredite.

| Situação | Ferramenta | Ressalva |
|---|---|---|
| Um verso, ponte ou final fraco; o resto está bom | **Replace Section** (regenera só o trecho escolhido) | no guia, só planos pagos |
| Falta uma seção, um final, espaço para crescer | **Extend** (continua de um ponto escolhido) | quanto mais cedo o ponto, mais do resto muda |
| A faixa está certa; só o som (clareza, equilíbrio) | **Remaster** | variação sutil: não muda letra nem estrutura |
| A faixa funciona; quer outro gênero ou outra interpretação | **Cover** | é transformação grande; para polir, Remaster |
| A mesma voz e o mesmo clima em várias faixas (um álbum) | **Voices**: a Persona virou «Style Voice (legacy)», que guarda a essência de uma faixa (voz, estilo, clima); «Voice (new)» é a voz do próprio dono, gravada ou enviada, com verificação por frase falada | não copia o cantor de uma faixa gerada; plano gratuito, acesso limitado; descrever a voz em palavras compete com ela. Sem Voices, o style fixo com Variety em Off já repete cantora e gênero (§12) |
| Letras com o mesmo jeito de escrever | **Letrista** (nome, personalidade de até 240 caracteres, letras de referência) | é a escrita, não a voz; compare o mesmo pedido com e sem ele antes de gerar |
| Arranjo fino, stems, MIDI | **Studio** | aí o trabalho já é de produção, fora do pedido |

**Uso comercial:** o que sai de remix de faixa de outra pessoa pode ter uso só pessoal pelos termos de
setembro de 2026. Antes de publicar, o dono confere os termos; isto não é conselho jurídico.

Fontes da §11: [Suno — Voices](https://suno.com/voices) ·
[Suno — produtos](https://suno.com/pt-br/products) ·
[Suno — central de ajuda, «Making Music»](https://help.suno.com/en/categories/550017) ·
[Jack Righteous — Suno Remix Guide: Covers, Song Edits, Studio](https://jackrighteous.com/blogs/guides-using-suno-ai-music-creation/suno-remix-covers-edits-studio)

## 12. Configurações de geração do v6: Variety em Off

> Lido em 2026-11-15 no FAQ do v6 do Suno e numa referência aberta (CC0) atualizada em 2026-11-14; medido no
> mesmo dia pelo projeto Rainha da Preguiça, no plano gratuito (v6-mini). Fontes no fim.

- **Variety reescreve o style.** O FAQ do Suno diz que o controle introduz variedade «ajustando e atualizando os
  seus prompts de estilo», e que, para manter o controle total das tags, é preciso baixá-lo a 0. O padrão é
  Normal no v6 e no v6-mini: sem mexer, o style que aparece na faixa gerada já não é o que foi colado.
  **Style escrito à mão (ou copiado do Cancioneiro) = Variety em Off.** Com Variety em Off, «Personalizar» não
  liga (a tela diz «Aumente Variedade para usar Personalizar»): o perfil «Meu gosto» do dono não entra na geração.
  Ele ainda entra pela **varinha** do campo de estilos, com «Meus estilos» ligado: não use a varinha num style
  já escrito (capturas do dono, 2026-11-15).
- **Medido no campo** (Rainha da Preguiça, 2026-11-15, v6-mini): mesmo style e Variety em Off deram cantora
  parecida e o mesmo gênero em quatro faixas, sem Voice.
- **Max Mode** gasta o dobro de créditos para manter a faixa consistente do começo ao fim. É o que se
  recomenda para faixa acima de ~2 min, Cover e Voices (fonte secundária). No plano gratuito, pesa no limite diário.
- **Advanced, não Simple.** Pela fonte secundária, o modo Simple expande a letra dada em vez de cantá-la como
  está: letra pronta vai no Advanced.
- **Modelos:** v6-mini no plano gratuito; v6 e v6-wild no Pro e no Premier.
- **Registre o que usou:** modelo, Variety e Max Mode vão com o relato no `FAIXAS.md` — sem isso, duas gerações
  diferentes não dizem se mudou o pedido ou a configuração.

Fontes da §12: [Suno — FAQ do v6 e Variety](https://help.suno.com/en/articles/13924481) ·
[bitwize-music-studio/claude-ai-music-skills — creative-sliders e a issue #562 (CC0)](https://github.com/bitwize-music-studio/claude-ai-music-skills)
