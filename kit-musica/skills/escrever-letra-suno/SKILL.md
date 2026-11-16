---
name: escrever-letra-suno
description: Como escrever (ou reescrever) a letra de uma faixa para o Suno em pt-BR — a cena antes das rimas, o orçamento de caracteres, o tamanho da linha, as tags de seção, os parênteses, a repetição que trava o Suno, a pronúncia e o refino sem estragar o que o dono gostou. USE ao escrever, reescrever ou limpar a letra de uma faixa, e ao receber uma letra reescrita pelo Letrista ou pelo «Ajustar a letra» do Suno. Para o style, use a macetes-suno; para conferir antes de entregar, a revisar-faixa.
---

# Escrever letra para o Suno

> Parte do kit de música do Cancioneiro (`kit-musica/`, leva 2 do kit v2). Escrita em 2026-11-15 e provada no
> mesmo dia no projeto Rainha da Preguiça (3 faixas, v6-mini; spec `meta/specs/261115-kit-v2-leva-2.md`). As
> regras de ouvido vêm do que o dono daquele projeto ouviu no v6 e v6-mini, em 2026-11; a interface do Suno
> muda: se o dono disser que algo não vale na conta dele, acredite.

A letra é metade do pedido. O Suno canta o que está escrito, no tempo que a letra pede: linha longa ele corre,
letra longa ele corta (§2), repetição ele trava. Esta skill ensina orçamento e cantabilidade, **não estilo
poético**: o gosto é do dono.

## 1. A cena antes da rima

Antes de escrever uma linha, responda em uma frase cada:

- **Qual é a cena?** Um acontecimento pequeno e concreto, contado como se fosse grande — não um desabafo geral.
- **O que avança de seção em seção?** Uma contagem, um relógio, uma lista que encolhe: algo que faz a música
  andar sem enchimento.
- **Qual é a virada?** Uma descoberta, uma piada no fim, uma frase que muda o sentido do refrão.

Letra que não responde às três vira repetição do conceito do álbum. Se o projeto tem uma «bíblia» (quem fala,
para quem, as regras que não se dobram), ela vale antes desta skill.

## 2. Orçamento: até ~3.000 caracteres

| Faixa | Caracteres da letra (com as tags) |
|---|---|
| alvo | até ~3.000 — acima disso o Suno tende a correr ou pular trechos |
| teto | 5.000 — o que passa disso é cortado em silêncio |

- **Refrão por inteiro uma ou duas vezes**; nas outras, só a tag (`[Chorus]`).
- **Conte com código, não de cabeça**: o script da `revisar-faixa` conta caracteres e tags.
- Para cortar, corte **enchimento e repetição**, nunca a cena (§1) nem o que o dono já aprovou (§8).

## 3. O tamanho da linha

- **Verso cantado ou de rap:** cerca de 10 a 13 sílabas poéticas. **Refrão:** cerca de 6 a 10.
- **Versos paralelos** (a mesma posição em estrofes diferentes) com o mesmo número de sílabas e a tônica no
  mesmo lugar. Em pt-BR, conte a sílaba poética até a última tônica.
- Linha longa demais faz o Suno correr; curta demais, arrastar.

## 4. Tags de seção: curtas, em inglês, do gênero certo

- `[Verse]`, `[Pre-Chorus]`, `[Chorus]`, `[Bridge]`, `[Outro]`; em faixa de arco linear, `[Intro]`, `[Build]`,
  `[Climax]`; `[Drop]` só em eletrônica (`BLOCO-SUNO.md`, Parte 2).
- **Uma pista curta, se ajudar**, descrevendo o que se ouve: `[Verse 2: quieter]`, `[Chorus: full band]`.
  **Nada de frase longa nem de descrição em português dentro do colchete**: ela compete com o style e às vezes
  é cantada.
- **Um gênero do começo ao fim:** tag que descreve outro gênero puxa a faixa para ele.

## 5. Os parênteses: fala por cima da batida

- No v6, o texto entre parênteses costuma sair como **fala, backing ou comentário** por cima da batida. É um
  recurso: usado com medida, dá personalidade.
- **Em linha própria ou no fim da linha**, nunca no meio da frase cantada.
- **Com medida:** dezenas de linhas entre parênteses viram fala demais para caber, e o Suno corre.

## 6. A repetição que trava o Suno

| Evite | Por quê | Faça |
|---|---|---|
| linhas quase iguais em sequência | o Suno trava e repete | varie a segunda linha ou corte uma |
| palavra repetida em coro («vai, vai, vai!») | soa genérico e puxa o gênero (no projeto Rainha, puxou funk e trouxe uma voz masculina) | break instrumental sem palavra |
| eco da mesma palavra («Fui! (Fui!)») | o Suno repete a palavra mais vezes | o parêntese responde com outra coisa: «Fui! (Tchau!)» |
| o mesmo bloco duas vezes seguidas | soa como erro de colagem | uma vez, ou a tag |

## 7. Pronúncia em pt-BR

- **Números e siglas por extenso** («vinte por cento», «dê-jota»), como se quer ouvir.
- **Palavra estrangeira e nome próprio:** teste num trecho curto antes da faixa inteira.
- **Sem acento gráfico «criativo»** para forçar pronúncia: o resultado é imprevisível.

## 8. Refinar sem estragar

- **Não mexa no que o dono já gostou.** Refinar é trocar o fraco, não o que funciona. Pergunte, se não souber.
- **Letra reescrita pelo Suno** (Letrista, «Ajustar a letra») passa por esta skill e pelas regras do projeto
  **antes** de valer: o Suno não conhece o projeto. Aproveite a ideia boa e refaça a linha que fere uma regra.
- **Uma mudança por rodada** depois de ouvir (`macetes-suno` §10).

## 9. O fim da faixa

O Suno às vezes segue tocando depois da última linha. **Medido no projeto Rainha (2026-11-15, v6-mini):** com e
sem `[End]` no fim da letra, a cauda não encurtou de forma visível. `[End]` não custa nada, mas não é solução:
**corte o fim no Suno (Recortar, no plano gratuito)** em vez de gerar de novo. A última linha sem repetir a
anterior continua valendo (§6).

## 10. Exemplo (sintético)

Ruim — sem cena, linhas longas, coro repetido, eco e rótulo dentro do colchete:
```
[Verso 1 - aqui ela fica triste e reflexiva sobre a vida dela inteira]
Eu fico pensando em tudo que aconteceu comigo nesses anos todos sem parar
Eu fico pensando em tudo que aconteceu comigo nesses anos todos de novo
[Refrão]
Vai, vai, vai! (Vai!)
```
Bom — uma cena (o ônibus que não vem), algo que avança (o horário), parêntese no fim da linha:
```
[Verse 1]
Seis e dez, o ponto cheio, o céu ameaçando
(Guarda-chuva? Ficou em casa.)
Seis e meia, o aplicativo jura que tá chegando
(Jura. Faz uma hora.)
[Chorus]
Eu não espero mais ninguém
Só o ônibus que nunca vem
```

## 11. Antes de entregar

Rode a `revisar-faixa`. Ela conta e aponta; o corte é decisão do dono.
