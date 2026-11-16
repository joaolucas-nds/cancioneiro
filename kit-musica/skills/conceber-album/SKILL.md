---
name: conceber-album
description: Como conceber ou reorganizar um álbum gerado no Suno para que as faixas soem do mesmo artista — o que une o álbum, o estilo-base fixo com Variety em Off, a voz, a faixa-piloto, o arco de energia e BPM, a bíblia do projeto e os ids no JSON do Cancioneiro. USE ao começar um álbum, ao reagrupar faixas soltas num álbum, e quando o dono disser que as faixas «não parecem da mesma cantora» ou «mudam de gênero». Para cada faixa, use a escrever-letra-suno e a macetes-suno; para conferir, a revisar-faixa.
---

# Conceber um álbum para o Suno

> Parte do kit de música do Cancioneiro (`kit-musica/`, leva 2 do kit v2). Escrita em 2026-11-15 e provada no
> mesmo dia no projeto Rainha da Preguiça (3 faixas, v6-mini; spec `meta/specs/261115-kit-v2-leva-2.md`). O que
> está marcado como medido foi medido naquele projeto, no plano gratuito, em 2026-11-15.

Cada geração do Suno começa do zero. Um álbum soa como álbum quando as faixas **repetem as mesmas escolhas**:
o mesmo som de base, a mesma voz, o mesmo tipo de história. A skill é sobre manter essas escolhas fixas, não
sobre gerar mais.

## 1. O que une o álbum, numa frase

Escolha **uma** coisa que todas as faixas compartilham, e escreva-a no PROJETO:

- **uma cena de uso** (onde e para que se ouve: «treino de corrida», «madrugada de estudo»), ou
- **uma personagem** (quem canta, para quem, com que humor).

Gênero sozinho não une: dez faixas de «pop» podem soar como dez artistas.

## 2. O estilo-base: um style fixo, Variety em Off

- **Escreva um style-base** de 6 a 8 tags (gênero, voz, dois ou três instrumentos, produção), a partir de uma
  faixa que o dono já aprovou ou de uma fórmula de referência do Cancioneiro.
- **Copie o mesmo style-base em todas as faixas, com Variety em Off** (`macetes-suno` §12). Com Variety acima de
  Off, o Suno reescreve o style a cada geração, e a unidade some. **Medido:** style fixo e Variety em Off
  repetiram a cantora e o gênero em quatro faixas, sem Voice.
- **O que muda por faixa vai no fim** e em poucas tags (clima, BPM, um instrumento a mais). Respeite o orçamento:
  base + o que muda até 8 tags, no máximo 10.
- **Modo de canto fica fora da base.** Uma tag como «fast rap verses» no style-base empurra o álbum inteiro para
  ela. **Medido:** com ela na base, as faixas saíram rápidas e longe da faixa-referência, que não tem rap. Ponha
  o modo de canto só na faixa que pede.
- **Famílias de som** (uma faixa mais íntima, um hino de fecho) são **variantes do estilo-base**, não styles
  soltos: troque uma ou duas tags, não o style inteiro.
- No Cancioneiro, a frase que se repete em várias faixas pode virar **módulo** da coleção; lembre que módulo
  só soma tags.

## 3. A voz

- **Sem plano pago:** a voz vem do estilo-base fixo (§2). Diga a voz em poucas palavras e sempre do mesmo jeito
  em todas as faixas; marque «Gênero vocal» se uma geração trouxer outra voz.
- **Cover de uma faixa aprovada** mantém a cantora no plano gratuito. **Medido:** um Cover a partir da faixa
  preferida do dono foi o que mais soou como ela. Bom para refazer uma faixa com outra letra; o Cover carrega a
  melodia e o arranjo da origem, então serve menos para faixas que pedem outro clima.
- **Com Voices** (planos pagos; o gratuito tem acesso limitado): use a Voice e **não** descreva a voz no style —
  as duas competem (`macetes-suno` §11).
- **Um cantor só por faixa**, salvo dueto decidido. Coro de apoio, só onde o projeto quiser.

## 4. Uma faixa-piloto antes do resto

Gere **uma** faixa até o dono aprovar o som e a voz. Só então copie o estilo-base para as outras. Mudar o
estilo-base no meio do álbum obriga a regerar o que veio antes.

## 5. O arco do álbum

- **Uma faixa de abertura e uma de fecho** com papel claro.
- **Ordem por energia e BPM:** sem dois vizinhos com a mesma energia e o mesmo BPM; um BPM por faixa
  (`macetes-suno` §5).
- **Álbum grande é acervo, não álbum:** com dezenas de faixas, decida se o álbum é o acervo inteiro ou uma
  seleção, e refaça a ordem depois da seleção.

## 6. A bíblia do projeto

Escreva no PROJETO, ou na LETRAS, o que todo chat novo precisa saber antes de escrever uma linha:

- quem fala, para quem, com que humor;
- os personagens recorrentes e o papel de cada um;
- **as regras que não se dobram** (a piada que não se faz, a palavra que não entra), com o porquê.

O Suno e o chat novo não conhecem o projeto: o que não está escrito, eles inventam.

## 7. No JSON do Cancioneiro

- **Ids estáveis** com a sigla do álbum (`<sigla>-01`, `<sigla>-02`…); o id não muda quando o título muda.
- Títulos e notas são referência, **fora do copiável**; o style-base vai em `style`, a letra em `lyrics`.
- O álbum é um `album` da coleção; as variantes de uma faixa vão em `variants[]`, não em faixas novas.

## 8. Registro

No FAIXAS do projeto, para cada geração: data, **modelo, Variety e Max Mode**, o que o dono ouviu e a próxima
mudança (uma por vez). Sem a configuração anotada, duas gerações diferentes não dizem o que mudou.
