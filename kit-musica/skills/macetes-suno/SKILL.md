---
name: macetes-suno
description: O que tem efeito no Suno e o que é mito — os dois campos, o style em camadas, o orçamento de tags, os limites que cortam em silêncio, BPM, instrumental e exclusão. USE ao escrever ou reescrever o style ou a letra de uma faixa para o Suno, ao montar variantes, e quando o dono perguntar «por que saiu assim?» ou «como faço o Suno fazer X?». Para conferir uma faixa pronta, use a skill revisar-faixa.
---

# Macetes do Suno — o que tem efeito

> Parte do kit de música do Cancioneiro (`kit-musica/`). Fonte: `meta/HISTORY.md` do Cancioneiro, que
> traz cada item com data, fonte e nível de confiança. **Conferido em 2026-10, Suno v6.** A interface
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
