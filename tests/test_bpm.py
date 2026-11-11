"""Rampa de BPM (0.19.0, i-042, DEC-036; criterios da spec meta/specs/261111-rampa-de-bpm.md).
Faixas sinteticas, feitas a partir do data/demo.json."""
import copy
import json
import os
import subprocess
import sys
import tempfile

from conftest import DEMO, ROOT, import_demo, write_tmp_collection

RAMP = "dream pop, soft female vocal, 95 BPM building to 115 BPM, warm synths"


def coll_with(styles, bpms=None, tempo_module=False):
    """Acervo de um album com uma faixa por style (ids r0, r1...)."""
    coll = copy.deepcopy(DEMO)
    base = copy.deepcopy(DEMO["albums"][0]["songs"][0])
    songs = []
    for i, st in enumerate(styles):
        s = copy.deepcopy(base)
        s.update(id=f"r{i}", title=f"Faixa {i + 1}", style=st)
        s.pop("bpm", None)
        s["styleModules"] = []
        if bpms and bpms[i] is not None:
            s["bpm"] = bpms[i]
        songs.append(s)
    coll["albums"] = [{"id": "a", "title": "A", "songs": songs}]
    if tempo_module:
        coll.setdefault("styleModules", []).append(
            {"id": "tempo-100", "label": "midtempo 100", "category": "tempo", "fragment": "midtempo 100 bpm"})
    return coll


def copied_style(page, sid):
    page.click(f'#main li.row[data-id="{sid}"] [data-role="row-style"]')
    page.wait_for_timeout(150)
    return page.evaluate("navigator.clipboard.readText()")


def test_c1_rampa_sai_byte_a_byte(open_app):
    page = open_app()
    import_demo(page, write_tmp_collection(coll_with([RAMP])))
    assert copied_style(page, "r0") == RAMP
    page.click('#main li.row[data-id="r0"] .row-open')
    assert page.text_content('#detail [data-role="style-block"]') == RAMP


def test_c2_formas_de_ligacao(open_app):
    yes = ["pop, 95 BPM to 118 BPM", "pop, 95 bpm building to 115 bpm", "pop, 90 bpm rising to 120 bpm",
           "pop, 90 bpm up to 120 bpm", "pop, 90 bpm climbing to 120 bpm", "pop, 90 → 120 bpm", "pop, 95 to 118 BPM"]
    no = ["pop, 95 bpm, 115 bpm", "pop, 95 bpm 115 bpm", "pop, 95 bpm"]
    page = open_app()
    got = page.evaluate("xs => xs.map(s => rampOf(s))", yes + no)
    assert all(got[: len(yes)]) and not any(got[len(yes):]), got


def test_c3_rotulo_chips_e_aviso(open_app):
    page = open_app()
    import_demo(page, write_tmp_collection(coll_with([RAMP], tempo_module=True)))
    page.click('#main li.row[data-id="r0"] .row-open')
    assert "rampa 95 → 115 bpm" in page.text_content("#detail .bpm-ramp")
    assert page.eval_on_selector_all("#detail .bpm-ctl input", "e => e.length") == 0
    page.evaluate("document.querySelectorAll('#detail details').forEach(d => d.open = true)")
    chip = page.locator('#detail button.chip[data-mid="tempo-100"]')
    assert chip.is_disabled()
    assert "rampa de BPM (95 → 115)" in page.text_content('#detail [data-role="style-quality"]')
    assert page.text_content('#main li.row[data-id="r0"]').count("95→115 bpm") == 1


def test_c4_bpm_unico_continua_controlado(open_app):
    """Falso positivo: faixa com um BPM, como na 0.18.0 (DEC-020)."""
    page = open_app()
    import_demo(page, write_tmp_collection(coll_with(["pop, 100 bpm, warm synths"])))
    page.click('#main li.row[data-id="r0"] .row-open')
    page.click('#detail .bpm-ctl button[aria-label="aumentar 5 BPM"]')
    assert page.text_content('#detail [data-role="style-block"]') == "pop, 105 bpm, warm synths"
    assert page.eval_on_selector_all("#detail .bpm-ramp", "e => e.length") == 0


def test_c5_export_md(open_app):
    page = open_app()
    import_demo(page, write_tmp_collection(coll_with([RAMP])))
    page.click('#main li.row[data-id="r0"] .row-more')
    with page.expect_download() as d:
        page.click("#tm-md")
    md = open(d.value.path(), encoding="utf-8").read()
    assert RAMP in md and "BPM: rampa 95 → 115" in md


def test_c6_validate(tmp_path):
    styles = ["pop, 95 BPM building to 115 BPM", "pop, 95 to 118 BPM", "pop, 90 → 120 bpm", "pop, 95 bpm, 115 bpm"]
    path = tmp_path / "rampas.json"
    path.write_text(json.dumps(coll_with(styles, [None, 95, 120, None]), ensure_ascii=False), encoding="utf-8")
    out = subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "validate.py"), str(path)],
                         capture_output=True, text=True).stdout
    assert "AVISO de BPM" in out and "[a > r0] rampa de BPM: 95 -> 115" in out
    assert "[a > r1]" not in out.split("ERRO de BPM")[-1]           # bpm = partida: passa
    assert "[a > r2] campo bpm 120, mas a rampa parte de 90" in out  # bpm = chegada: erro
    assert "[a > r3] o style tem 2 BPM diferentes: 95, 115" in out   # dois soltos: erro
    only_ramps = tmp_path / "so-rampas.json"
    only_ramps.write_text(json.dumps(coll_with(styles[:2], [None, 95]), ensure_ascii=False), encoding="utf-8")
    r = subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "validate.py"), str(only_ramps)],
                       capture_output=True, text=True)
    assert "ERRO de BPM" not in r.stdout
