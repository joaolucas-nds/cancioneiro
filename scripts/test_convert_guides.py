#!/usr/bin/env python3
"""Testa scripts/convert_guides.py com guias sinteticos (sem letra real no repo).

Uso:
    python3 scripts/test_convert_guides.py

So biblioteca padrao. Um caso por jeito de marcar o que vai para o Suno, mais os
de «nao deve» (CEREBRO, FIX-003): comentario `# ` dentro da letra nao abre faixa,
secao sem style nao vira faixa, e o mapa de grupos reprova faixa perdida.
"""
import json
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.dont_write_bytecode = True  # nao deixa scripts/__pycache__ na arvore do repo
import convert_guides  # noqa: E402

F = "```"

# Rotulado (VOL4/VOL5): codigo no cabecalho, VAR num bloco, ORIGINAL com sufixo.
LABELED = f"""# 🎵 ÁLBUM HOBBY — VOLUME 4

## ⚙️ COMO USAR

Dicas sem bloco de faixa.

## 🤠 BR-01 — SERTANEJO TESTE
### "Faixa Rotulada" — Dupla de teste

**Conceito:** cena de teste
**Voz:** dupla

{F}
[ESTILO SUNO — ORIGINAL adaptado]
sertanejo test, viola,
72 BPM,
{F}

{F}
[LETRA]

[Verse 1]
linha um
# comentario de codigo dentro da letra
## outro comentario
{F}

**🔄 VARIAÇÕES:**
{F}
[ESTILO SUNO — VAR A: mais animado]
festivo test
[ESTILO SUNO — VAR B: orquestral]
orquestra test
{F}

## 🎮 CODE-EN-01 — INGLÊS
### "Second Track"

{F}
[ESTILO SUNO]
synthwave test
{F}

{F}
[ESTRUTURA]
[Intro]
[Outro]
{F}
"""

# Opcao A/B (VOL6/VOL7): titulo entre aspas no cabecalho, Lyrics (opcional).
OPTIONS = f"""# 🎼 ÁLBUM HOBBY — VOLUME 6

## 🎹 CLS-01 — "Chuva Teste" (Piano Solo)

**Style — Opção A:**
{F}
solo piano test, 68 BPM
{F}

**Style — Opção B:**
{F}
solo piano test, hopeful
{F}

**Lyrics (opcional):**
{F}
[Instrumental]
{F}
"""

# Style Prompt + Letra + Titulo (guia_suno), e a secao de variacoes soltas.
PROMPT = f"""# 🎵 ÁLBUM COMPLETO

## 🇬🇧 ROMÂNTICA 5 — Inglês

**Título:** Under Test Sky *(Sob o Céu de Teste)*

**Style Prompt:**
{F}
indie pop test, female vocalist
{F}

**Letra:**

{F}
[Verse 1]
the sky and you and my heart
{F}

## 🔀 Variações para: *Under Test Sky* (Inglês — Romântica 5)

### Versão A — Soul
{F}
soul test
{F}
"""

# Estilo Suno + letra em Markdown fora de bloco + VERSAO B + roteiro de treino (guia_completo).
MARKDOWN = f"""# 🎵 ÁLBUM HOBBY — GUIA COMPLETO

## 🇰🇷 R-01 — Canção Teste — *Tradução Teste*

### VERSÃO A — Balada, Voz Masculina
{F}
[Estilo Suno]
k-ballad test, 68 BPM
{F}

**[Verse 1]**
linha de teste

*(Usar a mesma letra da Versão A)*

---

### VERSÃO B — Balada, Voz Feminina
{F}
[Estilo Suno]
k-ballad test, soprano
{F}

---

## TR-01 — PRIME TEST *(Instrumental — Sem Vocal)*

{F}
[Estilo Suno]
instrumental only test, 150 BPM
{F}

**[Estrutura]**
- **[0:00–0:30]** — Build up de teste
"""


class ConvertGuides(unittest.TestCase):
    """Casos do conversor dos guias de Albuns/."""

    def setUp(self):
        self.dir = tempfile.mkdtemp()

    def write(self, name, text):
        path = os.path.join(self.dir, name)
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        return path

    def run_main(self, *args):
        out = os.path.join(self.dir, "out.json")
        code = convert_guides.main([out, *args])
        with open(out, encoding="utf-8") as f:
            coll = json.load(f)
        return code, {s["id"]: s for a in coll["albums"] for s in a["songs"]}, coll

    def test_labeled(self):
        code, songs, _ = self.run_main(self.write("ALBUM_VOL4_GUIA_SUNO.md", LABELED))
        self.assertEqual(code, 0)
        self.assertEqual(sorted(songs), ["v4-br-01", "v4-code-en-01"])  # «COMO USAR» nao e faixa
        s = songs["v4-br-01"]
        self.assertEqual((s["title"], s["style"], s["bpm"], s["language"]), ("Faixa Rotulada", "sertanejo test, viola, 72 BPM", 72, "pt-BR"))
        self.assertIn("# comentario de codigo", s["lyrics"])  # comentario na letra nao abriu faixa
        self.assertEqual([v["label"] for v in s["variants"]], ["VAR A — mais animado", "VAR B — orquestral"])
        self.assertEqual(s["context"], "cena de teste")
        self.assertEqual(songs["v4-code-en-01"]["language"], "instrumental")  # [ESTRUTURA] so com tags

    def test_options(self):
        _, songs, _ = self.run_main(self.write("ALBUM_VOL6_INSTRUMENTAL_SUNO.md", OPTIONS))
        s = songs["v6-cls-01"]
        self.assertEqual((s["title"], s["style"], s["lyrics"]), ("Chuva Teste", "solo piano test, 68 BPM", "[Instrumental]"))
        self.assertEqual(s["variants"], [{"label": "Opção B", "style": "solo piano test, hopeful"}])

    def test_prompt_and_loose_variants(self):
        code, songs, _ = self.run_main(self.write("album_guia_suno.md", PROMPT))
        self.assertEqual(code, 0)
        s = songs["gs-01"]
        self.assertEqual((s["title"], s["style"], s["language"]), ("Under Test Sky (Sob o Céu de Teste)", "indie pop test, female vocalist", "en"))
        self.assertEqual(s["variants"], [{"label": "Versão A — Soul", "style": "soul test"}])

    def test_markdown_lyrics_and_version_b(self):
        _, songs, _ = self.run_main(self.write("album_guia_completo.md", MARKDOWN))
        s = songs["gc-r-01"]
        self.assertEqual(s["title"], "Canção Teste — Tradução Teste")  # a traducao fica; o descritor *(...)* sai (ver PRIME TEST)
        self.assertEqual(s["lyrics"], "[Verse 1]\nlinha de teste")  # sem ** e sem a nota *(...)*
        self.assertEqual([v["label"] for v in s["variants"]], ["VERSÃO B — Balada, Voz Feminina"])
        self.assertIn("Versão principal: VERSÃO A — Balada, Voz Masculina", s["notes"])

    def test_training_timing_goes_to_notes(self):
        """Nao deve: o roteiro de tempos («0:00–0:30») nao vai para o Lyrics."""
        _, songs, _ = self.run_main(self.write("album_guia_completo.md", MARKDOWN))
        s = songs["gc-tr-01"]
        self.assertEqual((s["title"], s["lyrics"]), ("PRIME TEST", "[Instrumental]"))
        self.assertIn("[0:00–0:30] — Build up de teste", s["notes"])

    def test_label_never_inside_copyable(self):
        """Regra de dominio: nenhum rotulo em style, lyrics ou variante."""
        paths = [self.write(n, t) for n, t in [("ALBUM_VOL4_GUIA_SUNO.md", LABELED), ("ALBUM_VOL6_INSTRUMENTAL_SUNO.md", OPTIONS),
                                              ("album_guia_suno.md", PROMPT), ("album_guia_completo.md", MARKDOWN)]]
        _, songs, _ = self.run_main(*paths)
        for s in songs.values():
            for text in [s["style"], s["lyrics"]] + [v["style"] for v in s["variants"]]:
                for label in ("ESTILO SUNO", "Estilo Suno", "[LETRA]", "[ESTRUTURA]", "**"):
                    self.assertNotIn(label, text, s["id"])

    def test_groups(self):
        guide = self.write("ALBUM_VOL4_GUIA_SUNO.md", LABELED)
        gmap = self.write("g.json", json.dumps({"albums": [{"id": "a", "title": "A", "songs": ["v4-code-en-01", "v4-br-01"]}]}))
        code, _, coll = self.run_main(guide, "--groups", gmap)
        self.assertEqual(code, 0)
        self.assertEqual([s["id"] for s in coll["albums"][0]["songs"]], ["v4-code-en-01", "v4-br-01"])  # ordem do mapa

    def test_groups_reject_lost_and_unknown(self):
        """Nao deve: faixa fora de todo album, ou id que nao existe, passar calado."""
        guide = self.write("ALBUM_VOL4_GUIA_SUNO.md", LABELED)
        lost = self.write("g1.json", json.dumps({"albums": [{"id": "a", "title": "A", "songs": ["v4-br-01"]}]}))
        self.assertEqual(self.run_main(guide, "--groups", lost)[0], 1)
        ghost = self.write("g2.json", json.dumps({"albums": [{"id": "a", "title": "A", "songs": ["v4-br-01", "v4-code-en-01", "x-99"]}]}))
        self.assertEqual(self.run_main(guide, "--groups", ghost)[0], 1)
        dropped = self.write("g3.json", json.dumps({"albums": [{"id": "a", "title": "A", "songs": ["v4-br-01"]}],
                                                    "drop": {"v4-code-en-01": "teste"}}))
        self.assertEqual(self.run_main(guide, "--groups", dropped)[0], 0)


if __name__ == "__main__":
    unittest.main()
