#!/usr/bin/env python3
"""Valida os datasets de data/ contra o esquema canonico.

Uso:
    python3 scripts/validate.py              # valida todos os data/*.json
    python3 scripts/validate.py data/foo.json  # valida um arquivo

Checa duas coisas:
  1. Sintaxe JSON de todos os schemas e datasets.
  2. Conformidade estrutural de cada dataset contra collection.schema.json
     (requer o pacote 'jsonschema'; se ausente, faz so a checagem de sintaxe).

Rode antes de commitar mudanca em data/ ou schema/ (ver CLAUDE.md).
Saida: codigo 0 se tudo passou, 1 se houve erro.
"""
import json
import sys
import glob
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load(path):
    """Le e faz parse de um JSON, com mensagem clara em caso de erro."""
    with open(path, encoding="utf-8") as f:
        return json.load(f)


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

    print()
    if errors:
        print(f"FALHOU: {errors} arquivo(s) com erro.")
        return 1
    print("Tudo conforme ao esquema.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
