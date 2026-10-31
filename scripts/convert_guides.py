#!/usr/bin/env python3
"""Converte os guias de `Albuns/` (formatos mistos) para uma colecao no esquema (i-008, i-038).

Uso:
    python3 scripts/convert_guides.py SAIDA.json GUIA.md [GUIA.md ...] [--groups MAPA.json] [--title "Nome"]

Diferente do `convert_br.py` (uma familia, um molde), este le os oito guias de
`Albuns/`, que usam seis jeitos de marcar o que vai para o Suno. Uma faixa e um
cabecalho `## ` que tem um style; o resto do guia (indice, dicas, enredo) fica de
fora. Cada bloco de codigo e classificado pelo rotulo da primeira linha ou pela
linha em negrito logo antes dele:

    style       `[ESTILO SUNO]`, `[ESTILO SUNO — ORIGINAL]`, `[Estilo Suno]`, ou bloco
                depois de `**Style — Opção A:**`, `**Style Prompt:**`, `Campo "Style of Music"`
    variante    `[ESTILO SUNO — VAR A: rotulo]` (varias num bloco), `**Style — Opção B:**`,
                um segundo `[Estilo Suno]` (VERSAO B do guia completo) e as secoes
                «Variações para: *Titulo*», que viram variantes da faixa daquele titulo
    lyrics      `[LETRA]`, `[ESTRUTURA]`, ou bloco depois de `Lyrics (opcional):`,
                `Letra:`, `LETRA COMPLETA`; no guia completo a letra e Markdown fora
                de bloco (`**[Verse 1]**`) e sai sem os asteriscos
    titulo      `### "Titulo"`, `**Título:**`, bloco depois de `Campo "Title"`, aspas no
                cabecalho, `# Nome` do jogo, ou o proprio cabecalho

A regra de dominio vale igual: o rotulo nunca entra em `style` nem `lyrics`.
Conversao fiel (DEC-026): nada e cortado; o relatorio conta o que passa do limite.

Sem `--groups`, um album por arquivo. Com `--groups`, o mapa (JSON, fora do repo:
traz os titulos do dono) diz quais faixas vao para qual album:
    {"albums": [{"id": "...", "title": "...", "description": "...", "songs": ["v4-br-01", ...]}],
     "drop": {"gs-epica-1": "duplicata de epico-05"}}
Toda faixa convertida precisa estar em um album ou em `drop`; faixa citada que nao
existe tambem e erro. Saida: codigo 0 se tudo bateu; 1 se nao.
"""
import argparse
import json
import re
import sys
import unicodedata

# Prefixo de id por arquivo: o mesmo codigo (ROM-01) existe em dois guias.
PREFIX = {
    "ALBUM_EPICO_GUIA_SUNO": "epico", "ALBUM_VOL4_GUIA_SUNO": "v4", "ALBUM_VOL5_GUIA_SUNO": "v5",
    "ALBUM_VOL6_INSTRUMENTAL_SUNO": "v6", "ALBUM_VOL7_VIOLINO_ELETRONICO_SUNO": "v7",
    "album_guia_completo": "gc", "album_guia_suno": "gs", "guia_musicas_acao_gemini_suno": "ga",
}
# Codigo de faixa no cabecalho: BR-01, MÃE-02, CLK-EN-01, RITM-M-08, R-01, KP-05.
CODE = re.compile(r"(?<![\w-])([A-ZÃÉ]{1,5}(?:-[A-Z]{1,2})?-\d{2})(?![\w-])")
STYLE_LABEL = re.compile(r"^\[(?:ESTILO SUNO|Estilo Suno)\s*(?:—\s*(.*?))?\s*:?\s*(.*?)\]\s*$")
VAR_WORD = re.compile(r"^VAR(?:IAÇÃO)?\b\s*(.*)$", re.I)
LYRICS_LABEL = re.compile(r"^\[(LETRA|ESTRUTURA)\]\s*$")
BPM = re.compile(r"\b(\d{2,3})\s*-?\s*bpm\b", re.I)

# Idioma pelo cabecalho; se nao disser, pela escrita da letra.
LANG_WORDS = [
    # \b no fim: «japonesa» (de «estética japonesa») nao e o idioma da letra
    (r"PT-BR|PORTUGU[ÊE]S\b|🇧🇷", "pt-BR"), (r"INGL[ÊE]S\b|🇺🇸|🇬🇧", "en"), (r"JAPON[ÊE]S\b|🇯🇵", "ja"),
    (r"COREANO\b|🇰🇷", "ko"), (r"CHIN[ÊE]S\b|MANDARIM|🇨🇳", "zh"), (r"ESPANHOL\b|🇪🇸", "es"),
    (r"FRANC[ÊE]S\b|🇫🇷", "fr"), (r"LATIM\b", "la"), (r"TELUGU\b|🇮🇳", "te"),
]
SCRIPTS = [(r"[가-힯]", "ko"), (r"[぀-ヿ]", "ja"), (r"[ఀ-౿]", "te"), (r"[一-鿿]", "zh")]
# Palavras que so uma das linguas usa (o, a, de, que sao das duas e nao contam).
WORDS = {
    "pt-BR": re.compile(r"\b(não|você|eu|mas|muito|até|aqui|sou|é|nós|com|pra|meu|minha)\b", re.I),
    "es": re.compile(r"\b(y|el|los|yo|pero|muy|hasta|aquí|soy|eres|mi|tú|corazón)\b", re.I),
    "en": re.compile(r"\b(the|and|you|my|is|of|I|we|your)\b"),
    "fr": re.compile(r"\b(je|tu|et|les|mon|ma|toujours|avec|nous|c'est)\b", re.I),
}


def slug(text):
    """Minusculas, sem acento, hifens no lugar do resto."""
    ascii_ = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", ascii_.lower()).strip("-")


def clean_md(text):
    """Tira emoji de abertura, asteriscos e espacos sobrando de um cabecalho."""
    text = re.sub(r"^#+\s*", "", text)
    text = re.sub(r"^[^\w\"'(«]+", "", text)  # emoji/simbolos no comeco
    return re.sub(r"\s+", " ", text.replace("*", "")).strip()


def join_style(lines):
    """Style em uma linha: junta as linhas, colapsa espacos, tira a virgula final."""
    text = " ".join(x.strip() for x in lines if x.strip())
    return re.sub(r"\s+", " ", text).strip().rstrip(",").strip()


def trim(lines):
    """Tira linhas em branco das pontas e espacos do fim de cada linha."""
    lines = [x.rstrip() for x in lines]
    while lines and not lines[0].strip():
        lines = lines[1:]
    while lines and not lines[-1].strip():
        lines = lines[:-1]
    return lines


def segments(lines):
    """Divide o guia nos cabecalhos `## ` que estao fora de bloco de codigo.

    Fora de bloco porque letras de codigo trazem `# ` e `## ` como comentario.
    Devolve (cabecalho, itens), onde item e ('text', i, linha) ou ('block', i, linhas).
    """
    out, cur, inside, buf = [], None, False, []
    for i, line in enumerate(lines):
        if line.lstrip().startswith("```"):
            if inside and cur is not None:
                cur[1].append(("block", i, buf))
            buf, inside = [], not inside
            continue
        if inside:
            buf.append(line)
        elif line.startswith("## "):
            cur = (line, [])
            out.append(cur)
        elif cur is not None:
            cur[1].append(("text", i, line))
    return out


def prev_text(items, k):
    """A ultima linha de texto nao vazia antes do item k (o 'rotulo de fora' do bloco)."""
    for kind, _, val in reversed(items[:k]):
        if kind == "text" and val.strip() and val.strip() != "---":
            return val.strip()
        if kind == "block":
            return ""
    return ""


def guess_language(header, lyrics):
    """Idioma: palavra-chave no cabecalho; senao, escrita da letra; instrumental se so tags."""
    words = [x for x in lyrics.split("\n") if x.strip() and not re.fullmatch(r"\s*\[.*\]\s*", x)]
    if not words:
        return "instrumental"
    hits = [(m.start(), code) for pattern, code in LANG_WORDS for m in [re.search(pattern, header, re.I)] if m]
    if hits:
        return min(hits)[1]
    body = "\n".join(words)
    # letra com mais de uma escrita (coreano com trechos em japones): a que mais aparece
    counts = {code: len(re.findall(pattern, body)) for pattern, code in SCRIPTS}
    best = max(counts, key=counts.get)
    if counts[best] > 20:
        return best
    scores = {code: len(rx.findall(body)) for code, rx in WORDS.items()}
    return max(scores, key=scores.get)


def parse_segment(header, items, prefix, ordinal):
    """Um cabecalho `## ` -> dict de faixa, ou None se nao tem style."""
    texts = [val for kind, _, val in items if kind == "text"]
    style, lyrics, variants, title = None, None, [], None
    main_version = ""
    md_lyrics_from = None  # indice do item depois do qual a letra vem em Markdown (guia completo)
    for k, (kind, _, val) in enumerate(items):
        if kind != "block":
            continue
        body = val
        first_i = next((j for j, x in enumerate(body) if x.strip()), None)
        if first_i is None:
            continue
        first = body[first_i].strip()
        before = prev_text(items, k)
        if STYLE_LABEL.match(first):
            # Um bloco pode ter varios rotulos; cada um abre um trecho. O primeiro trecho
            # sem VAR, enquanto nao ha style, e o style principal (o sufixo — ORIGINAL,
            # «ORIGINAL adaptado», «RÉPLICA ...» — e so referencia); o resto vira variante.
            chunks = []
            for x in body:
                mm = STYLE_LABEL.match(x.strip())
                if mm:
                    chunks.append([" ".join(y for y in mm.groups() if y).strip(), []])
                elif chunks:
                    chunks[-1][1].append(x)
            for sfx, chunk in chunks:
                vv = VAR_WORD.match(sfx) if sfx else None
                if style is None and not vv:
                    style = join_style(chunk)
                    md_lyrics_from = k  # guia completo: a letra vem em Markdown depois deste bloco
                    if before.startswith("### "):  # VERSAO A do guia completo
                        main_version = clean_md(before)
                elif sfx:
                    label = ("VAR " + re.sub(r"^([A-Z])\s*:\s*", r"\1 — ", vv.group(1).strip())) if vv else sfx
                    variants.append({"label": re.sub(r"\s+", " ", label).strip(" :—"), "lines": chunk})
                else:  # segundo [Estilo Suno] sem sufixo: VERSAO B do guia completo
                    variants.append({"label": clean_md(before) or "VERSÃO B", "lines": chunk})
            continue
        if LYRICS_LABEL.match(first):
            lyrics = "\n".join(trim(body[first_i + 1:]))
        elif re.search(r"Style\s*—\s*Opção\s*A|Style Prompt|Style of Music", before, re.I) and style is None:
            style = join_style(body)
        elif re.search(r"Style\s*—\s*Opção\s*([B-Z])", before, re.I):
            letter = re.search(r"Opção\s*([B-Z])", before, re.I).group(1).upper()
            variants.append({"label": f"Opção {letter}", "lines": body})
        elif re.search(r"Lyrics|Letra:|LETRA COMPLETA", before, re.I) and lyrics is None:
            lyrics = "\n".join(trim(body))
        elif re.search(r'Campo "Title"', before):
            title = join_style(body)
    if style is None:
        return None

    # Letra em Markdown fora de bloco (guia completo): do bloco da VERSAO A ate o proximo ### ou ---.
    timing = ""
    if lyrics is None and md_lyrics_from is not None:
        buf = []
        for kind, _, val in items[md_lyrics_from + 1:]:
            if kind == "block" or val.startswith("### ") or val.strip() == "---":
                break
            if re.match(r"^\*\(.*\)\*\s*$", val.strip()):  # «*(Usar a mesma letra...)*» e referencia
                continue
            buf.append(val.replace("**", ""))
        buf = trim(buf)
        if buf and buf[0].strip().lower() == "[estrutura]":
            # faixa de treino: roteiro de tempos para quem edita, nao letra para o Suno
            timing = "\n".join(buf[1:]).strip()
            lyrics = "[Instrumental]"
        else:
            lyrics = "\n".join(buf) or None
    if lyrics is None:
        return {"_skip": "sem letra"}

    head = clean_md(header)
    bare = clean_md(re.sub(r"\s*—?\s*\*\(.*?\)\*", "", header))  # sem «*(K-pop, Grupo...)*»
    code_m = CODE.search(header)
    code = code_m.group(1) if code_m else None
    if title is None:
        q = next((re.search(r'"([^"]+)"', x) for x in texts[:4] if x.startswith("### ") and '"' in x), None)
        t = next((x.split(":**", 1)[1].strip() for x in texts if x.startswith("**Título:**")), None)
        game = next((x[2:].strip() for x in texts[:3] if x.startswith("# ")), None)
        bgm = next((clean_md(x).split("—", 1)[-1].strip() for x in texts if x.startswith("### ") and "BGM" in x), None)
        hq = re.search(r'"([^"]+)"', header)
        if q:
            title = q.group(1)
        elif t:
            title = clean_md(t)
        elif game:
            title = clean_md(game) + (f" — {bgm.capitalize()}" if bgm else "")
        elif hq:
            title = hq.group(1)
        else:
            title = bare.split("—", 1)[1].strip() if code and "—" in bare else bare
    title = re.sub(r"\s+", " ", title).strip()

    def field(key):
        prefix_ = f"**{key}:**"
        return next((x.strip()[len(prefix_):].strip() for x in texts if x.strip().startswith(prefix_)), "")

    sid = f"{prefix}-{slug(code)}" if code else f"{prefix}-{ordinal:02d}"
    voice = next((x.split("—", 1)[1].strip() for x in texts[:4] if x.startswith("### ") and '"' in x and "—" in x), "")
    numbers = sorted({int(n) for n in BPM.findall(style)})
    notes = [
        f"Versão principal: {main_version}" if main_version else "",
        f"Voz: {field('Voz') or voice}" if (field("Voz") or voice) else "",
        f"Instrumentos: {field('Instrumentos')}" if field("Instrumentos") else "",
        f"Roteiro de tempos:\n{timing}" if timing else "",
        f"Origem: {head}",
    ]
    return {
        "id": sid,
        "title": title,
        "language": guess_language(header + " " + " ".join(texts[:4]), lyrics),
        "state": "ideia",
        "style": style,
        "lyrics": lyrics,
        "bpm": numbers[0] if len(numbers) == 1 else None,
        "variants": [{"label": v["label"], "style": join_style(v["lines"])} for v in variants if join_style(v["lines"])],
        "context": field("Conceito") or field("Para"),
        "notes": "\n".join(x for x in notes if x),
        "tags": [x for x in [code, prefix] if x],
    }


def extra_variants(header, items):
    """Secao «Variações para: *Titulo*»: (titulo, [variantes]) — cada ### Versão X com o seu bloco."""
    m = re.search(r"Variações para:\s*\*([^*]+)\*", header)
    if not m:
        return None
    out = []
    for k, (kind, _, val) in enumerate(items):
        if kind == "block":
            label = clean_md(prev_text(items, k))
            out.append({"label": label, "style": join_style(val)})
    return m.group(1).strip(), out


def convert_file(path):
    """Um guia -> (faixas, variantes soltas por titulo, avisos)."""
    name = re.sub(r"\.md$", "", path.replace("\\", "/").rsplit("/", 1)[-1])
    prefix = PREFIX.get(name, slug(name)[:6])
    with open(path, encoding="utf-8") as f:
        lines = f.read().replace("\r\n", "\n").split("\n")
    songs, loose, warnings, n = [], [], [], 0
    for header, items in segments(lines):
        ev = extra_variants(header, items)
        if ev:
            loose.append(ev)
            continue
        n += 1
        song = parse_segment(header, items, prefix, n)
        if song is None:
            n -= 1
            continue
        if "_skip" in song:
            warnings.append(f"{name}: {clean_md(header)} — {song['_skip']}, ignorada")
            continue
        songs.append(song)
    return name, songs, loose, warnings


def main(argv=None):
    """Linha de comando: converte, aplica as variantes soltas e o mapa de grupos, grava."""
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("output", help="arquivo .json de saida (fora do repo)")
    ap.add_argument("guides", nargs="+", help="guias .md de Albuns/")
    ap.add_argument("--groups", help="mapa de grupos .json (fora do repo)")
    ap.add_argument("--title", default="Álbuns reagrupados", help="titulo da colecao")
    args = ap.parse_args(argv)

    by_file, loose_all, errors = [], [], 0
    for path in args.guides:
        name, songs, loose, warnings = convert_file(path)
        by_file.append((name, songs))
        loose_all += [(name, title, variants) for title, variants in loose]
        print(f"{name}: {len(songs)} faixas" + (f", {len(loose)} secao(oes) de variantes" if loose else ""))
        for w in warnings:
            print(f"   aviso {w}")
    index = {s["id"]: s for _, songs in by_file for s in songs}
    dup = len(index) != sum(len(s) for _, s in by_file)
    if dup:
        print("ERRO: id repetido entre faixas")
        errors += 1

    # «Variações para: *Titulo*» -> variantes da(s) faixa(s) com esse titulo
    # Prefere a faixa do mesmo guia: «Rise of the Eternal» existe em dois guias e sao
    # duas cancoes diferentes (letra e voz), nao uma duplicata.
    base = lambda x: re.sub(r"\s*\(.*\)\s*$", "", x).strip().lower()
    for name, title, variants in loose_all:
        same = dict(by_file)[name]
        hits = [s for s in same if base(s["title"]) == base(title)]
        hits = hits or [s for s in index.values() if base(s["title"]) == base(title)]
        if not hits:
            print(f"ERRO: variantes para «{title}» sem faixa com esse titulo")
            errors += 1
        for s in hits:
            s["variants"] += variants

    if args.groups:
        with open(args.groups, encoding="utf-8") as f:
            gmap = json.load(f)
        used = {}
        albums = []
        for g in gmap["albums"]:
            songs = []
            for sid in g["songs"]:
                if sid not in index:
                    print(f"ERRO: o mapa cita '{sid}', que nao existe")
                    errors += 1
                elif sid in used:
                    print(f"ERRO: '{sid}' esta em '{used[sid]}' e em '{g['id']}'")
                    errors += 1
                else:
                    used[sid] = g["id"]
                    songs.append(index[sid])
            albums.append({"id": g["id"], "title": g["title"], "description": g.get("description", ""), "songs": songs})
        drop = gmap.get("drop", {})
        for sid in drop:
            if sid not in index:
                print(f"ERRO: o mapa descarta '{sid}', que nao existe")
                errors += 1
        loose_ids = [sid for sid in index if sid not in used and sid not in drop]
        if loose_ids:
            print(f"ERRO: {len(loose_ids)} faixa(s) fora de qualquer album: {', '.join(loose_ids[:10])}")
            errors += 1
    else:
        albums = [{"id": slug(name), "title": name, "description": "", "songs": songs} for name, songs in by_file]

    collection = {"schemaVersion": "1.0", "title": args.title,
                  "description": "Convertido dos guias de Albuns/ por scripts/convert_guides.py (i-008, i-038).",
                  "targetTool": "suno", "albums": albums}
    with open(args.output, "w", encoding="utf-8", newline="\n") as f:
        json.dump(collection, f, ensure_ascii=False, indent=1)
        f.write("\n")
    songs = [s for a in albums for s in a["songs"]]
    print(f"\n{len(albums)} album(ns), {len(songs)} faixa(s) -> {args.output}")
    print(f"   letras acima de 5000 caracteres: {sum(len(s['lyrics']) > 5000 for s in songs)} de {len(songs)}")
    print(f"   styles com mais de 10 tags: {sum(len([t for t in s['style'].split(',') if t.strip()]) > 10 for s in songs)} de {len(songs)}")
    if errors:
        print(f"FALHOU: {errors} erro(s).")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
