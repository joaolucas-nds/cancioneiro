#!/usr/bin/env python3
"""Converte os guias da familia BR para uma colecao no esquema canonico (i-008).

Uso:
    python3 scripts/convert_br.py SAIDA.json GUIA.md [GUIA.md ...] [--title "Nome"]

Familia BR: um arquivo por volume (`..._VOL<n>_GUIA.md`), uma faixa por cabecalho
`## <emoji> BR<n>-NN — GENERO`, titulo em `### "Titulo" — voz`, campos de
referencia em `**Conceito:**`, `**Voz:**`, `**Instrumentos:**`, e tres blocos de
codigo por faixa: `[ESTILO SUNO]`, `[LETRA]` e as variantes
`[ESTILO SUNO — VAR X: rotulo]`. So esta familia: as outras tem outro formato e
pedem outro conversor (analise 261029, decisao 1A).

A regra de dominio guia tudo: o rotulo do bloco (`[ESTILO SUNO]`, `[LETRA]`) e
referencia humana e NUNCA entra em `style` ou `lyrics`; o resto do bloco vai
literal. A conversao e fiel (decisao 4A): letra longa demais ou style com tags
demais nao e cortado aqui — o relatorio conta, e o painel de qualidade do app mostra.

A colecao gerada e produto do dono e NAO e versionada no repo (decisao 2A):
grave a saida fora do repo, por exemplo na pasta-pai.

Saida: codigo 0 se todo cabecalho de faixa virou faixa; 1 se algum ficou para tras.
"""
import argparse
import json
import re
import sys
import unicodedata

# Cabecalho de faixa: "## 🎤 BR3-07 — K-POP GIRL CRUSH". O emoji e um token qualquer.
# BRV-N01 e BR10-15 aparecem nos guias; por isso o [V0-9]* e o N? (sonda de 2026-10-29).
CODE = re.compile(r"^## \S+\s+(BR[V0-9]*-N?\d{2})\s+—\s+(.+?)\s*$")
# Rotulo de variante: "[ESTILO SUNO — VAR A: mais cru]" ou "[ESTILO SUNO — VARIAÇÃO B]".
VAR = re.compile(r"^\[ESTILO SUNO\s*—\s*(VAR(?:IAÇÃO)?\s*[A-Z])\s*:?\s*(.*?)\]\s*$", re.I)
# Volume pelo nome do arquivo: ALBUM_BR_VOL7_GUIA.md -> 7.
VOL = re.compile(r"VOL(\d+)", re.I)
# Mesmo padrao de BPM do app e do validate.py, para o relatorio bater com eles.
BPM = re.compile(r"\b(\d{2,3})\s*-?\s*bpm\b", re.I)
BPM_RANGE = re.compile(r"\d{2,3}\s*[–-]\s*\d{2,3}\s*bpm", re.I)

# Limites do Suno usados so no relatorio (fonte e data em QUALITY_LIMITS, app/index.html).
LYRICS_LIMIT = 5000
TAGS_SOFT_LIMIT = 10


def slug(text):
    """Minusculas, sem acento, hifens no lugar do resto: 'BR3-07' -> 'br3-07'."""
    ascii_ = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", ascii_.lower()).strip("-")


def code_blocks(lines):
    """Lista o conteudo de cada bloco ``` ... ``` (sem as cercas)."""
    out, inside, buf = [], False, []
    for line in lines:
        if line.lstrip().startswith("```"):
            if inside:
                out.append(buf)
                buf = []
            inside = not inside
        elif inside:
            buf.append(line)
    return out


def join_style(lines):
    """Style em uma linha: junta as linhas do bloco, colapsa espacos, tira a virgula final."""
    text = " ".join(x.strip() for x in lines if x.strip())
    return re.sub(r"\s+", " ", text).strip().rstrip(",").strip()


def after_label(body):
    """Linhas do bloco depois da primeira nao vazia (o rotulo), sem brancas nas pontas."""
    first = next(i for i, x in enumerate(body) if x.strip())
    rest = body[first + 1:]
    while rest and not rest[0].strip():
        rest = rest[1:]
    while rest and not rest[-1].strip():
        rest = rest[:-1]
    return rest


def track_segment(lines, start, end):
    """Linhas da faixa: do cabecalho ate o proximo de codigo, um '# ' ou um '## ' sem codigo.

    Os guias intercalam secoes que nao sao faixa ("## Sobre o volume", notas de
    fechamento); sem o corte, o texto delas cairia nas notas da ultima faixa.
    """
    seg = lines[start:end]
    for k, line in enumerate(seg[1:], 1):
        if line.startswith("# ") or (line.startswith("## ") and not CODE.match(line)):
            return seg[:k]
    return seg


def parse_track(seg):
    """Uma faixa do guia -> (dict no esquema, lista de avisos) ou (None, [motivo])."""
    code, genre = CODE.match(seg[0]).groups()
    head = next((re.search(r'"([^"]+)"\s*(?:—\s*(.*))?', x) for x in seg[1:4] if x.startswith("### ")), None)
    title = head.group(1) if head else code
    voice_line = (head.group(2) or "").strip() if head else ""
    conversation = next((re.sub(r"[#*]", "", x).strip() for x in seg[1:5] if x.startswith("#### ")), "")

    def field(key):
        prefix = f"**{key}:**"
        return next((x[len(prefix):].strip() for x in seg if x.startswith(prefix)), "")

    style, lyrics, variants = None, None, []
    for body in code_blocks(seg):
        first = next((x.strip() for x in body if x.strip()), "")
        if first.startswith("[ESTILO SUNO") and not VAR.match(first):
            style = join_style(after_label(body))
        elif first.startswith("[LETRA]"):
            lyrics = "\n".join(x.rstrip() for x in after_label(body))
        elif VAR.match(first):
            # um bloco pode trazer mais de uma variante, cada uma com o seu rotulo
            current = None
            for x in body:
                m = VAR.match(x.strip())
                if m:
                    name = re.sub(r"(?i)VARIAÇÃO", "VAR", m.group(1).upper())
                    label = name + (" — " + m.group(2) if m.group(2) else "")
                    current = {"label": label, "lines": []}
                    variants.append(current)
                elif current is not None:
                    current["lines"].append(x)
    if style is None or lyrics is None:
        return None, [f"{code}: sem {'[ESTILO SUNO]' if style is None else '[LETRA]'} — faixa ignorada"]

    warnings = []
    numbers = sorted({int(n) for n in BPM.findall(style)})
    ranged = BPM_RANGE.search(style)
    if ranged:
        warnings.append(f"{code}: BPM em faixa ({ranged.group(0)}) — campo bpm vazio")
    elif len(numbers) > 1:
        warnings.append(f"{code}: style com {len(numbers)} BPM ({', '.join(map(str, numbers))}) — campo bpm vazio")
    notes = [
        f"Voz: {field('Voz') or voice_line}" if (field("Voz") or voice_line) else "",
        f"Instrumentos: {field('Instrumentos')}" if field("Instrumentos") else "",
        conversation,
        f"Gênero: {genre}",
    ]
    song = {
        "id": slug(code),
        "title": title,
        "language": "pt-BR",
        "state": "ideia",
        "style": style,
        "lyrics": lyrics,
        "bpm": numbers[0] if len(numbers) == 1 and not ranged else None,
        "variants": [{"label": v["label"], "style": join_style(v["lines"])} for v in variants],
        "context": field("Conceito"),
        "notes": "\n".join(x for x in notes if x),
        "tags": [code, genre.lower()],
    }
    return song, warnings


def convert_file(path, vol):
    """Um guia -> (album, avisos, numero de cabecalhos de faixa)."""
    with open(path, encoding="utf-8") as f:
        lines = f.read().replace("\r\n", "\n").split("\n")
    # "# 🎵 ÁLBUM HOBBY — VOLUME BR · PARTE 2 | GUIA COMPLETO PARA SUNO AI" -> sem emoji e sem o "| GUIA ..."
    h1 = next((x for x in lines if x.startswith("# ")), "")
    original = re.sub(r"^#\s*\S+\s*", "", h1).split("|")[0].strip()
    starts = [i for i, x in enumerate(lines) if CODE.match(x)]
    songs, warnings = [], []
    for n, i in enumerate(starts):
        end = starts[n + 1] if n + 1 < len(starts) else len(lines)
        song, warn = parse_track(track_segment(lines, i, end))
        warnings += warn
        if song:
            songs.append(song)
    album = {"id": f"br-vol{vol}", "title": f"Parte {vol}", "description": original, "songs": songs}
    return album, warnings, len(starts)


def report(albums):
    """Linhas de relatorio sobre limites do Suno — conta, nao corta (decisao 4A)."""
    songs = [s for a in albums for s in a["songs"]]
    long_ = [s["id"] for s in songs if len(s["lyrics"]) > LYRICS_LIMIT]
    tags = [s["id"] for s in songs if len([t for t in s["style"].split(",") if t.strip()]) > TAGS_SOFT_LIMIT]
    return [
        f"letras acima de {LYRICS_LIMIT} caracteres (o Suno corta em silencio): {len(long_)} de {len(songs)}",
        f"styles com mais de {TAGS_SOFT_LIMIT} tags (as ultimas perdem efeito): {len(tags)} de {len(songs)}",
    ]


def main(argv=None):
    """Linha de comando: converte os guias dados e grava a colecao."""
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("output", help="arquivo .json de saida (fora do repo)")
    ap.add_argument("guides", nargs="+", help="guias ..._VOL<n>_GUIA.md")
    ap.add_argument("--title", default="Rainha da Preguiça", help="titulo da colecao")
    args = ap.parse_args(argv)

    albums, lost = [], 0
    for path in args.guides:
        m = VOL.search(path.replace("\\", "/").rsplit("/", 1)[-1])
        if not m:
            print(f"ERRO: sem VOL<n> no nome de {path} — pulado")
            lost += 1
            continue
        album, warnings, n = convert_file(path, int(m.group(1)))
        albums.append(album)
        lost += n - len(album["songs"])
        print(f"VOL{m.group(1)}: {n} cabecalhos -> {len(album['songs'])} faixas")
        for w in warnings:
            print(f"   aviso {w}")
    albums.sort(key=lambda a: int(a["id"].rsplit("vol", 1)[1]))
    collection = {
        "schemaVersion": "1.0",
        "title": args.title,
        "description": "Convertido dos guias BR por scripts/convert_br.py (i-008).",
        "targetTool": "suno",
        "albums": albums,
    }
    with open(args.output, "w", encoding="utf-8", newline="\n") as f:
        json.dump(collection, f, ensure_ascii=False, indent=1)
        f.write("\n")
    total = sum(len(a["songs"]) for a in albums)
    print(f"\n{len(albums)} album(ns), {total} faixa(s) -> {args.output}")
    for line in report(albums):
        print(f"   {line}")
    if lost:
        print(f"FALHOU: {lost} cabecalho(s) de faixa nao viraram faixa.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
