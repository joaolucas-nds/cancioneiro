# Bloco Suno — para um projeto de música do KCM que gera faixas no Suno

> Parte do kit de música do Cancioneiro (`kit-musica/`). O projeto nasce do nicho **Música** do KCM
> (PROJETO, FAIXAS, LETRAS, ARRANJO); este bloco acrescenta o que muda quando a faixa é **gerada por IA**
> e não tocada: o pedido ao Suno vira o artefato, e o Cancioneiro organiza e copia.
>
> **Como usar:** cole a **Parte 1** no fim das Instruções do projeto (cabe no teto do KCM: medir antes e
> depois) e a **Parte 2** no `meta/CEREBRO.md` do projeto. Suba ao projeto as duas skills de
> `kit-musica/skills/` e o prompt-modelo (`schema/PROMPT-PARA-CHATS.md`, ou o botão «Prompt» do app).

---

## Parte 1 — para as Instruções do projeto

```
## Suno (faixa gerada por IA)
- Toda faixa sai no JSON do Cancioneiro (prompt-modelo no projeto): arquivo .json; sem arquivo, um bloco de código.
- Copiável × referência: `style`/`lyrics` só com o que se cola no Suno; título, idioma, nota e rótulo vão nos campos de referência. Nunca «[ESTILO SUNO]» ou «LETRA» dentro do texto.
- Style: 6 a 8 tags, gênero primeiro; até 10 com módulos. Letra até ~3.000 caracteres (acima de 5.000 o Suno corta em silêncio). Um BPM por faixa.
- Antes de entregar faixa ou álbum, rode a skill `revisar-faixa`; ao escrever style ou letra, consulte `macetes-suno`.
- Não ouço o áudio: o dono gera, ouve e diz o que saiu; eu não digo que «ficou bom».
```

---

## Parte 2 — para o `meta/CEREBRO.md` do projeto

```
## Produção com IA de música (Suno)

**O artefato é o pedido.** Num projeto em que a faixa é gerada pelo Suno, o que se escreve não é a gravação,
é o pedido: o `style` (mundo sonoro) e a `lyrics` (arquitetura no tempo). O trabalho do assistente é escrever
esse pedido bem e explicar o porquê de cada escolha; o do dono é gerar, ouvir e decidir.

**Onde cada coisa mora.** O JSON do Cancioneiro (formato no prompt-modelo) é o catálogo copiável: uma coleção,
álbuns, faixas, módulos de estilo. O `FAIXAS.md` do projeto continua com o estado de cada faixa e o que falta;
o `LETRAS.md` guarda a letra em construção e a prosódia; a versão que vai ao Suno é a do JSON. Quando os dois
divergirem, o JSON é o que foi entregue; o `.md` registra por quê mudou.

**Orçamento, porque o Suno corta em silêncio.** Style com 6 a 8 tags (até 10 com módulos ligados), gênero nas
primeiras palavras; letra até ~3.000 caracteres, nunca acima de 5.000; um BPM por faixa, no style e no campo
`bpm`; instrumental em loop com `[Instrumental]` sozinho no Lyrics; tirar algo é `excludeStyles`, não «no X».
Os números são os do painel de qualidade do Cancioneiro, que os mantém com fonte e data.

**Revisão antes de entregar.** A skill `revisar-faixa` conta letra, tags, rótulos e BPM — com código quando a
conversa tiver execução, nunca de cabeça. Vermelho (o Suno corta) se resolve antes de entregar, com proposta
concreta de corte; cortar letra é decisão do dono.

**Ciclo de uma faixa.** Conceito (PROJETO) → letra com prosódia (LETRAS) → pedido ao Suno (JSON, revisado) →
o dono gera e relata o que ouviu → ajuste do pedido (variante ou módulo, sem reescrever a faixa) → estado em
FAIXAS. Relato do dono é a única medida de som; registre-o com a data e a versão do Suno.

**A interface do Suno muda.** Limites e campos vêm de fonte secundária (o Suno não publica os do v6).
Se o dono disser que um campo não existe na conta dele (o Exclude não aparece no v6-mini gratuito), acredite
e adapte.
```

---

## De onde vem cada regra

| Regra | Fonte no Cancioneiro |
|---|---|
| Dois campos, rótulo fora do copiável | `meta/HISTORY.md` §1; DEC-005 |
| Cinco camadas, começo pesa mais | HISTORY §4, §10; prompt-modelo |
| 6 a 8 tags, até 10 com módulos | HISTORY §10; DEC-018; DEC-021 |
| Letra ~3.000 / 5.000 | HISTORY §9; `QUALITY_LIMITS` no app |
| Um BPM por faixa | DEC-020 |
| `[Instrumental]` sozinho; arco só em faixa linear | HISTORY §2, §3 |
| Exclude, não «no X»; v6-mini sem Exclude | HISTORY §5, §11 |
| JSON canônico, módulos na coleção | DEC-016; DEC-021; DEC-023 |
