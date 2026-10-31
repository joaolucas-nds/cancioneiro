#!/usr/bin/env python3
"""Valida os datasets de data/ contra o esquema canonico.

Uso:
    python3 scripts/validate.py              # valida todos os data/*.json
    python3 scripts/validate.py data/foo.json  # valida um arquivo

Checa sete coisas:
  1. Sintaxe JSON de todos os schemas e datasets.
  2. Conformidade estrutural de cada dataset contra collection.schema.json
     (requer o pacote 'jsonschema'; se ausente, faz so a checagem de sintaxe
     e a ultima linha diz ESQUEMA NAO CONFERIDO).
  3. Integridade referencial: todo id em songs[].styleModules existe no
     styleModules[] da propria colecao (DEC-016). O schema nao alcanca isto.
  4. A versao e a mesma no topo do meta/CHANGELOG.md, no app, no README e no
     STATUS (i-027).
  5. O BPM de cada faixa e um so: o style nao tem dois numeros diferentes, e o
     campo bpm, quando existe, e o numero do style (DEC-020).
  6. O schema/PROMPT-PARA-CHATS.md tem as marcacoes que o botao «Prompt para
     chats» do app le: as linhas de INICIO e FIM e a linha entre parenteses
     abaixo de «## Meu pedido» (DEC-021).
  7. Os limites da skill kit-musica/skills/revisar-faixa sao os do painel de
     qualidade do app (QUALITY_LIMITS): o kit nao envelhece separado (DEC-027).

Rode antes de commitar mudanca em data/ ou schema/ (ver CLAUDE.md).
Saida: codigo 0 se tudo passou, 1 se houve erro.
"""
import json
import re
import sys
import glob
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load(path):
    """Le e faz parse de um JSON, com mensagem clara em caso de erro."""
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def check_module_refs(data, rel):
    """Todo id em songs[].styleModules resolve no styleModules[] da propria colecao.

    JSON Schema nao faz referencia cruzada: id orfao passa na validacao estrutural
    e vira fragmento silenciosamente ausente na ferramenta (ver DEC-016).
    """
    index = {m.get("id") for m in data.get("styleModules", []) if isinstance(m, dict)}
    orphans, not_ids = [], []
    for album in data.get("albums", []):
        for song in album.get("songs", []):
            for mid in song.get("styleModules", []) or []:
                where = (album.get("id", "?"), song.get("id", "?"))
                # Objeto no lugar do id: o chat declarou o modulo DENTRO da faixa.
                # Testado antes do `in`, porque dict nao e hashable e o `in` num set
                # quebrava o validador com traceback em vez de reprovar (FIX-009).
                if not isinstance(mid, str):
                    not_ids.append(where + (mid,))
                elif mid not in index:
                    orphans.append(where + (mid,))
    if not_ids:
        print(f"ERRO de referencia em {rel} ({len(not_ids)} item(ns) de styleModules nao sao id):")
        for a, s, mid in not_ids[:8]:
            print(f"   [{a} > {s}] styleModules: {type(mid).__name__} no lugar de um id — "
                  "declare o modulo em styleModules[] da colecao e cite so o id na faixa")
    if orphans:
        print(f"ERRO de referencia em {rel} ({len(orphans)} id(s) de modulo sem indice):")
        for a, s, mid in orphans[:8]:
            print(f"   [{a} > {s}] styleModules: '{mid}' nao existe em styleModules[]")
    return 1 if (orphans or not_ids) else 0


BPM_RE = re.compile(r"\b(\d{2,3})\s*-?\s*bpm\b", re.I)  # a mesma regra do app


def check_bpm(data, rel):
    """O BPM de cada faixa e um so (DEC-020).

    O app governa todo "NN bpm" do style a partir de um valor inicial; style com
    dois numeros, ou campo bpm que nao e o do style, e erro de autoria que o
    controle esconderia. Variantes ficam de fora: cada uma tem o andamento dela.
    """
    bad = []
    for album in data.get("albums", []):
        for song in album.get("songs", []):
            nums = sorted({int(n) for n in BPM_RE.findall(song.get("style", "") or "")})
            field = song.get("bpm")
            where = f"[{album.get('id', '?')} > {song.get('id', '?')}]"
            if len(nums) > 1:
                bad.append(f"{where} o style tem {len(nums)} BPM diferentes: {', '.join(map(str, nums))}")
            elif field is not None and not nums:
                bad.append(f"{where} campo bpm {field}, mas o style nao tem BPM")
            elif field is not None and nums[0] != field:
                bad.append(f"{where} campo bpm {field}, mas o style diz {nums[0]}")
    if bad:
        print(f"ERRO de BPM em {rel} ({len(bad)} faixa(s)):")
        for b in bad[:8]:
            print(f"   {b}")
        return 1
    return 0


def check_version():
    """A versao declarada nos quatro lugares tem de ser a mesma (i-027).

    Fonte: o topo do meta/CHANGELOG.md. O README ja ficou tres versoes atras
    sem ninguem notar (auditoria de 2026-07-21); esta checagem impede a volta.
    """
    def first(path, pattern):
        try:
            with open(os.path.join(ROOT, path), encoding="utf-8") as f:
                m = re.search(pattern, f.read(), re.M)
            return m.group(1) if m else None
        except OSError:
            return None

    found = {
        "meta/CHANGELOG.md": first("meta/CHANGELOG.md", r"^## \[(\d+\.\d+\.\d+)\]"),
        "app/index.html": first("app/index.html", r'data-role="app-version">v(\d+\.\d+\.\d+)<'),
        "README.md": first("README.md", r"\*\*Estado:\*\* v(\d+\.\d+\.\d+)"),
        "meta/STATUS.md": first("meta/STATUS.md", r"\*\*Versão atual:\*\* (\d+\.\d+\.\d+)"),
    }
    ref = found["meta/CHANGELOG.md"]
    bad = {k: v for k, v in found.items() if v is None or v != ref}
    if bad:
        print(f"ERRO de versao: o topo do meta/CHANGELOG.md diz {ref or '(nada)'}, mas:")
        for k, v in bad.items():
            print(f"   {k}: {v or 'versao nao encontrada'}")
        return 1
    print(f"OK  versao {ref} igual em CHANGELOG, app, README e STATUS")
    return 0


PROMPT_START = "--- INÍCIO ---"
PROMPT_END = "--- FIM ---"


def check_prompt():
    """O prompt-modelo tem o que o botao «Prompt para chats» le (DEC-021).

    O app nao guarda copia do prompt: busca este arquivo no Pages e recorta entre
    as duas linhas de marcacao, trocando a linha entre parenteses abaixo de
    «## Meu pedido» pelo pedido digitado. Marcacao que some quebra o botao em
    producao sem nada falhar aqui — por isso a checagem. Mesma regra do app
    (`extractPrompt` em app/index.html): linha exata, sem espacos em volta.
    """
    path = "schema/PROMPT-PARA-CHATS.md"
    try:
        with open(os.path.join(ROOT, path), encoding="utf-8") as f:
            lines = [l.rstrip("\r\n") for l in f]
    except OSError as e:
        print(f"ERRO no prompt: nao consegui ler {path}: {e}")
        return 1
    bad = []
    starts = [i for i, l in enumerate(lines) if l == PROMPT_START]
    ends = [i for i, l in enumerate(lines) if l == PROMPT_END]
    if len(starts) != 1 or len(ends) != 1 or ends[0] < starts[0]:
        bad.append(f"precisa de uma linha '{PROMPT_START}' e depois uma '{PROMPT_END}' "
                   f"(achei {len(starts)} e {len(ends)})")
    else:
        body = lines[starts[0] + 1:ends[0]]
        heads = [i for i, l in enumerate(body) if l == "## Meu pedido"]
        nxt = [l for l in body[heads[0] + 1:] if l.strip()][:1] if len(heads) == 1 else []
        if not (nxt and nxt[0].startswith("(") and nxt[0].endswith(")")):
            bad.append("entre as marcacoes, '## Meu pedido' (uma vez) seguido de uma linha entre parenteses")
    if bad:
        print(f"ERRO no prompt {path}:")
        for b in bad:
            print(f"   {b}")
        return 1
    print(f"OK  prompt com as marcacoes que o app le ({path})")
    return 0


KIT_SKILL = "kit-musica/skills/revisar-faixa/SKILL.md"


def check_kit():
    """Os limites da skill revisar-faixa sao os do app (DEC-027).

    A skill copia os numeros do `QUALITY_LIMITS` para o script que o chat roda no
    projeto de musica. Se o app mudar um limite e a skill nao, o projeto passa a
    revisar contra o numero velho sem nada falhar — por isso a checagem.
    """
    def read(path):
        with open(os.path.join(ROOT, path), encoding="utf-8") as f:
            return f.read()

    try:
        app, skill = read("app/index.html"), read(KIT_SKILL)
    except OSError as e:
        print(f"ERRO no kit: nao consegui ler: {e}")
        return 1
    block = re.search(r"const QUALITY_LIMITS = \{(.*?)\n\};", app, re.S)
    lim = {}
    for name, body in re.findall(r"^\s*(\w+):\s*\{([^}]*)\}", block.group(1) if block else "", re.M):
        for key, val in re.findall(r"(\w+):\s*(\d+)", body):
            lim[f"{name}.{key}"] = int(val)
    want = {  # constante da skill -> chave do QUALITY_LIMITS
        "LYRICS_MAX": "lyrics.max", "LYRICS_WARN": "lyrics.warn", "STYLE_MAX": "style.max",
        "STYLE_WARN": "style.warn", "TAGS_VAGUE": "tags.vague", "TAGS_MANY": "tags.many",
    }
    got = {}
    for names, values in re.findall(r"^(\w+(?:,\s*\w+)*)\s*=\s*(\d+(?:,\s*\d+)*)", skill, re.M):
        for n, v in zip(re.split(r",\s*", names), re.split(r",\s*", values)):
            got[n] = int(v)
    bad = [f"{k} = {got.get(k, 'ausente')} na skill, {lim.get(v, 'ausente')} no app ({v})"
           for k, v in want.items() if got.get(k) is None or got.get(k) != lim.get(v)]
    if bad:
        print(f"ERRO no kit {KIT_SKILL}: limites diferentes do QUALITY_LIMITS do app:")
        for b in bad:
            print(f"   {b}")
        return 1
    print(f"OK  kit: limites da skill revisar-faixa iguais ao app ({len(want)})")
    return 0


def main(argv):
    targets = argv[1:] or sorted(glob.glob(os.path.join(ROOT, "data", "*.json")))
    if not targets:
        print("Nenhum dataset em data/ para validar.")
        return 0

    errors = 0

    # 1. sintaxe dos schemas
    schema_dir = os.path.join(ROOT, "schema")
    for name in ("song.schema.json", "collection.schema.json", "style-modules.json"):
        p = os.path.join(schema_dir, name)
        try:
            load(p)
        except Exception as e:  # noqa: BLE001
            print(f"ERRO de sintaxe em schema/{name}: {e}")
            errors += 1
    if errors:
        return 1

    # 2. tenta validacao estrutural
    validator = None
    try:
        from jsonschema import Draft202012Validator
        from referencing import Registry, Resource

        song = load(os.path.join(schema_dir, "song.schema.json"))
        coll = load(os.path.join(schema_dir, "collection.schema.json"))
        # registra ambos os schemas sob $id e sob nome relativo (o $ref usa "song.schema.json")
        registry = Registry().with_resources([
            (song["$id"], Resource.from_contents(song)),
            (coll["$id"], Resource.from_contents(coll)),
            ("song.schema.json", Resource.from_contents(song)),
            ("collection.schema.json", Resource.from_contents(coll)),
        ])
        validator = Draft202012Validator(coll, registry=registry)
    except ImportError:
        print("Aviso: pacote 'jsonschema' ausente — so checagem de sintaxe.")
        print("       Instale com: pip install jsonschema --break-system-packages")
        print("       ATE LA, 'OK' abaixo significa so JSON bem formado — nao conformidade.")

    for path in targets:
        rel = os.path.relpath(path, ROOT)
        try:
            data = load(path)
        except Exception as e:  # noqa: BLE001
            print(f"ERRO de sintaxe em {rel}: {e}")
            errors += 1
            continue

        if validator is None:
            print(f"OK (sintaxe)  {rel}")
            # o modo degradado tambem confere referencias (nao depende do pacote)
            errors += check_module_refs(data, rel)
            errors += check_bpm(data, rel)
            continue

        errs = sorted(validator.iter_errors(data), key=lambda e: list(e.path))
        if errs:
            print(f"ERRO de schema em {rel} ({len(errs)} problema(s)):")
            for e in errs[:8]:
                loc = " > ".join(str(x) for x in e.path) or "(raiz)"
                print(f"   [{loc}] {e.message}")
            errors += 1
        else:
            n_songs = sum(len(a.get("songs", [])) for a in data.get("albums", []))
            print(f"OK  {rel}  ({len(data.get('albums', []))} álbuns, {n_songs} faixas)")

        # referencia cruzada e BPM: o schema nao alcanca isto
        errors += check_module_refs(data, rel)
        errors += check_bpm(data, rel)

    # versao: a mesma nos quatro lugares (i-027)
    errors += check_version()
    # prompt-modelo: as marcacoes que o botao do app le (DEC-021)
    errors += check_prompt()
    # kit de musica: os limites da skill sao os do app (DEC-027)
    errors += check_kit()

    print()
    if errors:
        print(f"FALHOU: {errors} arquivo(s) com erro.")
        return 1
    if validator is None:
        print("Sintaxe OK. ESQUEMA NAO CONFERIDO (pacote 'jsonschema' ausente).")
    else:
        print("Tudo conforme ao esquema.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
