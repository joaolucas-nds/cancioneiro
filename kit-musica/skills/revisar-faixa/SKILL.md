---
name: revisar-faixa
description: Revisão de faixa para o Suno antes de entregar — conta caracteres da letra e tags do style, procura rótulo dentro do que se copia, «no X» no style e dois BPM. USE SEMPRE antes de entregar uma faixa ou um álbum no JSON do Cancioneiro, e quando o dono colar um JSON e pedir «revisa», «confere», «está pronto para o Suno?». Não corta nada sozinha: aponta, e o corte é decisão do dono.
---

# Revisar faixa — o painel de qualidade antes do app

> Parte do kit de música do Cancioneiro (`kit-musica/`). Os números abaixo são os do painel de qualidade
> do app (`QUALITY_LIMITS` em `app/index.html`); o `scripts/validate.py` reprova se divergirem.

O Suno **corta em silêncio**: o que passa do limite do campo não chega ao modelo, sem aviso. E o que fica
dentro do limite pode render menos — tags demais se anulam, letra longa faz o Suno correr. Esta skill
mostra isso **antes** de a faixa sair, para o dono decidir o que cortar. Medido nos guias antigos do
dono, escritos sem esta revisão: 72 de 151 letras acima de 5.000 caracteres, 138 de 151 styles acima de
10 tags.

## Quando

- Antes de entregar qualquer faixa ou álbum.
- Quando o dono colar um JSON (ou um `.md` antigo) e perguntar se está pronto.
- Depois de mudar o style ou a letra de uma faixa já revisada.

## O que conferir (por faixa)

| # | Conferência | Vermelho (o Suno corta ou quebra) | Âmbar (funciona pior) |
|---|---|---|---|
| 1 | Caracteres da **letra** (`lyrics`) | acima de 5.000 | acima de 3.000 — o Suno começa a correr |
| 2 | Caracteres do **style** | acima de 1.000 | acima de 850 |
| 3 | **Tags** do style (trechos entre vírgulas) | — | acima de 10 (as últimas perdem efeito) ou abaixo de 4 (vago) |
| 4 | **Rótulo** dentro do copiável: `ESTILO SUNO`, `[LETRA]`, `Style:`, `Letra:` em `style`/`lyrics` | sempre | — |
| 5 | **Colchete** no style | sempre (colchete é do Lyrics) | — |
| 6 | **«no X»** no style | — | vai para `excludeStyles` (se o plano tiver o campo) |
| 7 | **BPM**: dois números no style, ou campo `bpm` diferente do style | — | um BPM por faixa; rampa («95 to 118 BPM») o app não controla |
| 8 | **Instrumental** com `[Instrumental]` e mais coisa no Lyrics, ou letra cantada com «no vocals» no style | — | sinais que brigam |

Variantes (`variants[].style`) passam pelas conferências 2 a 7.

## Como contar (não estime de cabeça)

Contar caracteres e tags «no olho» erra. Rode a conta. Se a conversa tiver execução de código, use o script
abaixo no JSON da coleção. Ele só lê e imprime:

```python
import json, re, sys

LYRICS_MAX, LYRICS_WARN = 5000, 3000   # = QUALITY_LIMITS.lyrics no app
STYLE_MAX, STYLE_WARN = 1000, 850      # = QUALITY_LIMITS.style
TAGS_VAGUE, TAGS_MANY = 4, 10          # = QUALITY_LIMITS.tags (vague, many)
LABEL = re.compile(r"ESTILO SUNO|\[LETRA\]|^\s*(Style|Letra|Lyrics)\s*:", re.I | re.M)
NEG = re.compile(r"(?<![a-z])no\s+[a-z][a-z-]*", re.I)
BPM = re.compile(r"\b(\d{2,3})\s*-?\s*bpm\b", re.I)

def check_style(style, where, out):
    tags = len([t for t in style.split(",") if t.strip()])
    if len(style) > STYLE_MAX: out.append(f"VERMELHO {where}: style com {len(style)} caracteres (limite {STYLE_MAX})")
    elif len(style) > STYLE_WARN: out.append(f"ambar {where}: style com {len(style)} caracteres")
    if tags > TAGS_MANY: out.append(f"ambar {where}: {tags} tags no style (acima de {TAGS_MANY})")
    elif tags < TAGS_VAGUE: out.append(f"ambar {where}: {tags} tags no style (vago)")
    if "[" in style: out.append(f"VERMELHO {where}: colchete no style")
    if NEG.search(style): out.append(f"ambar {where}: negacao no style: {NEG.search(style).group(0)!r}")
    if len(set(BPM.findall(style))) > 1: out.append(f"ambar {where}: {len(set(BPM.findall(style)))} BPM no style")

def review(coll):
    out = []
    for album in coll.get("albums", []):
        for s in album.get("songs", []):
            where = f"{album.get('id')} > {s.get('id')}"
            style, lyrics = s.get("style", ""), s.get("lyrics", "")
            if len(lyrics) > LYRICS_MAX: out.append(f"VERMELHO {where}: letra com {len(lyrics)} caracteres (limite {LYRICS_MAX})")
            elif len(lyrics) > LYRICS_WARN: out.append(f"ambar {where}: letra com {len(lyrics)} caracteres")
            for field, text in (("style", style), ("lyrics", lyrics)):
                if LABEL.search(text): out.append(f"VERMELHO {where}: rotulo dentro de {field}")
            check_style(style, where, out)
            nums = set(BPM.findall(style))
            if s.get("bpm") is not None and nums and str(s["bpm"]) not in nums:
                out.append(f"ambar {where}: campo bpm {s['bpm']}, style diz {', '.join(sorted(nums))}")
            sung = [l for l in lyrics.split("\n") if l.strip() and not re.fullmatch(r"\s*\[.*\]\s*", l)]
            if lyrics.strip().startswith("[Instrumental]") and sung: out.append(f"ambar {where}: [Instrumental] com letra")
            if sung and re.search(r"\bno vocals?\b", style, re.I): out.append(f"ambar {where}: letra cantada com 'no vocals' no style")
            for i, v in enumerate(s.get("variants", []) or []):
                check_style(v.get("style", ""), f"{where} variante {i + 1}", out)
    return out

coll = json.load(open(sys.argv[1], encoding="utf-8"))
problems = review(coll)
print("\n".join(problems) or "Nada a apontar nas oito conferencias.")
print(f"-- {sum(p.startswith('VERMELHO') for p in problems)} vermelho(s), {sum(p.startswith('ambar') for p in problems)} ambar(es)")
```

Sem execução de código: conte a letra por seção e some, e diga que a conta é estimada.

## Como apresentar

1. **Primeiro os vermelhos**, faixa por faixa, com o número medido e o limite. Vermelho é o que o Suno
   vai cortar ou receber quebrado.
2. Depois os âmbares, agrupados por tipo.
3. Para cada vermelho, **uma proposta concreta** — o trecho exato a tirar, ou as tags a juntar —, nunca
   «encurte a letra». Para letra longa: repetição de refrão é o primeiro candidato; ponte e outro falados,
   o segundo.
4. **Não corte sozinho.** Mostre e espere o dono escolher. Cortar letra é decisão de autor.

## O que esta skill não faz

- Não julga se a faixa **soa** bem: o assistente não ouve áudio. O dono gera no Suno e diz o que ouviu.
- Não garante obediência: passar nas oito conferências quer dizer que o Suno **recebe** tudo; o resultado
  continua variando a cada geração.
- Os limites são de fonte secundária (o Suno não publica os do v6); estão no app com fonte e data.
