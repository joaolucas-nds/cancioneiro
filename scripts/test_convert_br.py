#!/usr/bin/env python3
"""Testa scripts/convert_br.py com um guia sintetico (sem letra real no repo).

Uso:
    python3 scripts/test_convert_br.py

So biblioteca padrao. Cada caso cobre uma regra do conversor; os de «nao deve»
testam o falso positivo (CEREBRO, FIX-003): o que NAO pode virar faixa nem vazar.
"""
import json
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.dont_write_bytecode = True  # nao deixa scripts/__pycache__ na arvore do repo
import convert_br  # noqa: E402

FENCE = "```"
GUIDE = f"""# 🎵 ÁLBUM TESTE — VOLUME BR · PARTE 9 | GUIA COMPLETO PARA SUNO AI

> Cole o **[ESTILO SUNO]** no campo Style.

## 🎤 BR9-01 — K-POP TESTE
### "Faixa Um" — voz de teste
#### *Da Conversa: um dia qualquer*

**Conceito:** cena de teste
**Voz:** alto, perto do microfone
**Instrumentos:** baixo, bateria

{FENCE}
[ESTILO SUNO]
k-pop test, punchy bass,
bright synths, 120 BPM,
{FENCE}

{FENCE}
[LETRA]

[Verse 1]
linha um
linha dois

{FENCE}

{FENCE}
[ESTILO SUNO — VAR A: mais cru]
lo-fi test, dusty drums
[ESTILO SUNO — VARIAÇÃO B]
big room test
{FENCE}

## 🎤 BR9-02 — FUNK TESTE
### "Faixa Dois"

{FENCE}
[ESTILO SUNO]
funk test, 100–110 BPM
{FENCE}

{FENCE}
[LETRA]
[Chorus]
refrao
{FENCE}

## Sobre o volume

Texto que nao e faixa e nao deve cair nas notas da BR9-02.
"""

NO_LYRICS = f"""# 🎵 ÁLBUM TESTE — PARTE 3

## 🎤 BR3-01 — SEM LETRA
### "Incompleta"

{FENCE}
[ESTILO SUNO]
so estilo
{FENCE}
"""


class ConvertBR(unittest.TestCase):
    """Casos do conversor BR."""

    def setUp(self):
        self.dir = tempfile.mkdtemp()

    def write(self, name, text, crlf=False):
        path = os.path.join(self.dir, name)
        with open(path, "w", encoding="utf-8", newline="\r\n" if crlf else "\n") as f:
            f.write(text)
        return path

    def run_main(self, *guides):
        out = os.path.join(self.dir, "out.json")
        code = convert_br.main([out, *guides])
        with open(out, encoding="utf-8") as f:
            return code, json.load(f)

    def test_track_fields(self):
        code, coll = self.run_main(self.write("ALBUM_BR_VOL9_GUIA.md", GUIDE))
        self.assertEqual(code, 0)
        album = coll["albums"][0]
        self.assertEqual((album["id"], album["title"]), ("br-vol9", "Parte 9"))
        self.assertEqual(album["description"], "ÁLBUM TESTE — VOLUME BR · PARTE 9")
        one = album["songs"][0]
        self.assertEqual(one["id"], "br9-01")
        self.assertEqual(one["title"], "Faixa Um")
        self.assertEqual(one["style"], "k-pop test, punchy bass, bright synths, 120 BPM")
        self.assertEqual(one["lyrics"], "[Verse 1]\nlinha um\nlinha dois")
        self.assertEqual(one["bpm"], 120)
        self.assertEqual(one["context"], "cena de teste")
        self.assertIn("Voz: alto, perto do microfone", one["notes"])
        self.assertIn("Da Conversa: um dia qualquer", one["notes"])
        self.assertEqual(one["tags"], ["BR9-01", "k-pop teste"])

    def test_label_never_inside_copyable(self):
        """Regra de dominio: o rotulo do bloco nao entra em style nem lyrics."""
        _, coll = self.run_main(self.write("ALBUM_BR_VOL9_GUIA.md", GUIDE))
        for s in coll["albums"][0]["songs"]:
            for text in [s["style"], s["lyrics"]] + [v["style"] for v in s["variants"]]:
                self.assertNotIn("ESTILO SUNO", text)
                self.assertNotIn("[LETRA]", text)

    def test_variants(self):
        _, coll = self.run_main(self.write("ALBUM_BR_VOL9_GUIA.md", GUIDE))
        variants = coll["albums"][0]["songs"][0]["variants"]
        self.assertEqual(variants, [
            {"label": "VAR A — mais cru", "style": "lo-fi test, dusty drums"},
            {"label": "VAR B", "style": "big room test"},
        ])

    def test_bpm_range_leaves_field_empty(self):
        _, coll = self.run_main(self.write("ALBUM_BR_VOL9_GUIA.md", GUIDE))
        self.assertIsNone(coll["albums"][0]["songs"][1]["bpm"])

    def test_section_without_code_does_not_leak(self):
        """Nao deve: a secao «## Sobre o volume» nao vira faixa nem nota."""
        _, coll = self.run_main(self.write("ALBUM_BR_VOL9_GUIA.md", GUIDE))
        songs = coll["albums"][0]["songs"]
        self.assertEqual(len(songs), 2)
        self.assertNotIn("nao e faixa", songs[1]["notes"] + songs[1]["lyrics"])

    def test_crlf_input(self):
        """Arquivo salvo no Windows (CRLF) da o mesmo resultado."""
        _, lf = self.run_main(self.write("ALBUM_BR_VOL9_GUIA.md", GUIDE))
        _, crlf = self.run_main(self.write("ALBUM_BR_VOL9_GUIA.md", GUIDE, crlf=True))
        self.assertEqual(lf, crlf)

    def test_missing_block_fails(self):
        """Faixa sem [LETRA] fica de fora e o comando sai com 1."""
        code, coll = self.run_main(self.write("ALBUM_BR_VOL3_GUIA.md", NO_LYRICS))
        self.assertEqual(code, 1)
        self.assertEqual(coll["albums"][0]["songs"], [])

    def test_albums_ordered_by_volume(self):
        """VOL10 vem depois de VOL9, nao antes (ordem numerica, nao alfabetica)."""
        g9 = self.write("ALBUM_BR_VOL9_GUIA.md", GUIDE)
        g10 = self.write("ALBUM_BR_VOL10_GUIA.md", GUIDE.replace("BR9-", "BR10-"))
        _, coll = self.run_main(g10, g9)
        self.assertEqual([a["id"] for a in coll["albums"]], ["br-vol9", "br-vol10"])


if __name__ == "__main__":
    unittest.main()
