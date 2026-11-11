---
name: macetes-suno
description: O que tem efeito no Suno e o que é mito — os dois campos, o style em camadas, o orçamento de tags, os limites que cortam em silêncio, BPM, instrumental, exclusão, o que fazer depois de ouvir e as ferramentas do Suno (Replace Section, Extend, Remaster, Cover, Persona). USE ao escrever ou reescrever o style ou a letra de uma faixa para o Suno, ao montar variantes, quando o dono relatar o que ouviu, e quando perguntar «por que saiu assim?» ou «como faço o Suno fazer X?». Para conferir uma faixa pronta, use a skill revisar-faixa.
---

# Macetes do Suno — o que tem efeito

> Parte do kit de música do Cancioneiro (`kit-musica/`). Fonte: `meta/HISTORY.md` do Cancioneiro, que
> traz cada item com data, fonte e nível de confiança. **Conferido em 2026-10, Suno v6; §10 e §11 em 2026-11.** A interface
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
| «a voz não é essa» | a tag de voz; para manter a mesma voz em várias faixas, Persona (§11) |
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
| A mesma voz e o mesmo clima em várias faixas (um álbum) | **Persona** (vocal, estilo e clima salvos num perfil) | o style da faixa continua dizendo o que muda |
| Arranjo fino, stems, MIDI | **Studio** | aí o trabalho já é de produção, fora do pedido |

**Uso comercial:** o que sai de remix de faixa de outra pessoa pode ter uso só pessoal pelos termos de
setembro de 2026. Antes de publicar, o dono confere os termos; isto não é conselho jurídico.

Fontes da §11: [Suno — produtos](https://suno.com/pt-br/products) ·
[Suno — central de ajuda, «Making Music»](https://help.suno.com/en/categories/550017) ·
[Jack Righteous — Suno Remix Guide: Covers, Song Edits, Studio](https://jackrighteous.com/blogs/guides-using-suno-ai-music-creation/suno-remix-covers-edits-studio)
