"""
Generative validation for any dhatu — JSON is only cross-check.

Usage:
  python tests/test_dhatu.py 01.0002          # by ID
  python tests/test_dhatu.py eD               # by SLP1 dhatu
  python tests/test_dhatu.py --id 01.0001     # explicit
  DHATU=01.0002 python -m pytest tests/test_dhatu.py -v
  python -m unittest tests.test_dhatu -v
  python -m unittest tests.test_dhatu.TestDhatuGenerative.test_cli  # uses DHATU env

The grammar itself is wholly generative — see pypanini/tinanta.py & krdanta.py.
JSON under skt-morph-data is read-only verification, never imported for generation.
"""
import argparse
import glob
import json
import os
import sys
import unittest
from pathlib import Path

# allow `python tests/test_dhatu.py` from any cwd
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from pypanini import TinantaDerivationEngine, KrdantaEngine, slp1_to_devanagari, devanagari_to_slp1

# default data root (absolute on dev machine, overridable via env)
DATA_ROOT = Path(os.getenv("SKT_MORPH_DATA", "/home/edhiraj/Documents/projs/skt-morph-data/data"))
# also try relative ./skt-morph-data if checked out next to pypanini
if not DATA_ROOT.exists():
    alt = ROOT.parent / "skt-morph-data" / "data"
    if alt.exists():
        DATA_ROOT = alt


def extract_all_text_tokens(obj):
    toks = set()
    if isinstance(obj, str):
        cleaned = obj.strip().strip("।,;-\n\t")
        if cleaned:
            toks.add(cleaned)
            toks.add(cleaned.replace("।", "").strip())
    elif isinstance(obj, list):
        for it in obj:
            toks.update(extract_all_text_tokens(it))
    elif isinstance(obj, dict):
        for k, v in obj.items():
            toks.update(extract_all_text_tokens(v))
    return toks


def resolve_json_path(arg: str) -> Path:
    """
    arg can be:
      - 01.0002
      - 01.002
      - eD / BU / sparD  (SLP1)
      - absolute path
    """
    p = Path(arg)
    if p.exists() and p.suffix == ".json":
        return p
    # id-like 01.0002
    if "." in arg and any(c.isdigit() for c in arg):
        # try exact
        candidates = [
            DATA_ROOT / "01" / f"{arg}.json",
            DATA_ROOT / f"{arg}.json",
            DATA_ROOT / "01" / f"{arg.zfill(7)}.json",  # 01.002 -> 01.0002
        ]
        # normalize 01.002 -> 01.0002
        if ".00" not in arg:
            # e.g. 01.002 -> 01.0002, 01.2 -> 01.0002
            try:
                gana, num = arg.split(".")
                num = num.zfill(4)
                candidates.append(DATA_ROOT / gana / f"{gana}.{num}.json")
            except Exception:
                pass
        for c in candidates:
            if c.exists():
                return c
        # fallback glob
        for jf in glob.glob(str(DATA_ROOT / "**" / f"{arg}.json"), recursive=True):
            return Path(jf)
    # SLP1 dhatu -> scan for OpadeSikasvarUpam
    arg_clean = arg.replace("~", "").strip()
    # also handle trailing 'a' stripping as engine does
    for jf in glob.glob(str(DATA_ROOT / "**" / "*.json"), recursive=True):
        try:
            d = json.load(open(jf, encoding="utf-8"))
            info = {x["name"]: x["value"] for x in d.get("info", [])}
            op = info.get("OpadeSikasvarUpam", "").replace("~", "").strip()
            # same cleaning as engine: strip f/F anubandha and trailing a
            raw = op
            if raw and raw[-1] in "fFxX" and len(raw) > 2:
                # crude: if ends with anubandha
                import re
                # only strip if preceding char not vowel
                if raw[-2] not in "aAiIuUfFxXeEoO":
                    raw = raw[:-1]
            clean = raw[:-1] if raw.endswith("a") and len(raw) > 1 else raw
            if arg_clean in (op, raw, clean):
                return Path(jf)
        except Exception:
            continue
    raise FileNotFoundError(f"Cannot resolve dhatu/id '{arg}' under {DATA_ROOT}")


def resolve_dhatu_slp(json_path: Path, arg: str) -> str:
    """Return SLP1 dhatu string to pass to engine. If arg is SLP1, use it cleaned; else read from JSON."""
    if "." not in arg and "/" not in arg and not Path(arg).exists():
        # assume SLP1
        s = arg.replace("~", "").strip()
        # engine will clean trailing a/f, but we try to return as-is for lookup
        # if it ends with 'a' and len>1, engine expects without 'a' for consonant roots
        # keep as provided; engine's _get_meta handles it
        return s
    # read from JSON
    d = json.load(open(json_path, encoding="utf-8"))
    info = {x["name"]: x["value"] for x in d.get("info", [])}
    op = info.get("OpadeSikasvarUpam", "")
    # mimic engine cleaning
    raw = op.replace("~", "").replace("`", "").strip()
    if raw and raw[-1] in "fFxX" and len(raw) > 2 and raw[-2] not in "aAiIuUfFxXeEoO":
        raw = raw[:-1]
    clean = raw[:-1] if raw.endswith("a") and len(raw) > 1 else raw
    return clean


def validate_dhatu(arg: str, verbose: bool = True) -> tuple[int, int]:
    """
    Generative vs JSON cross-check for one dhatu.
    Returns (matched, total). Raises AssertionError if not 100% (for CI).
    """
    json_path = resolve_json_path(arg)
    dhatu = resolve_dhatu_slp(json_path, arg)
    data = json.load(open(json_path, encoding="utf-8"))
    info = {x["name"]: x["value"] for x in data.get("info", [])}
    dhatu_label = info.get("OpadeSikasvarUpam", dhatu)
    artha = info.get("arTaH", "")

    raw_tokens = extract_all_text_tokens(data)
    all_tokens = set(raw_tokens)
    for t in raw_tokens:
        all_tokens.add(devanagari_to_slp1(t))
        all_tokens.add(slp1_to_devanagari(t))

    def check_slot(forms_slp):
        for f in forms_slp:
            if f in all_tokens or slp1_to_devanagari(f) in all_tokens:
                return True
        return False

    te = TinantaDerivationEngine()
    ke = KrdantaEngine()

    total = 0
    matched = 0

    if verbose:
        print("=" * 75)
        print(f"VALIDATION  {json_path}  |  dhatu={dhatu} ({dhatu_label} {artha})")
        print("=" * 75)
        print(f"✓ tokens: {len(all_tokens)}  engine: generative (no hardcoded dict)")

    lakaras = [
        ("lw", "lw"), ("liw", "liw"), ("luw", "luw"), ("lfw", "lfw"),
        ("low", "low"), ("laN", "laN"), ("viDiliN", "viDiliN"),
        ("ASIrliN", "ASIrliN"), ("luN", "luN"), ("lfN", "lfN"),
    ]

    if verbose:
        print("\n-- tinanta (10 lakaras, 9 purusha/vacana) --")
    for code, _title in lakaras:
        loc_tot = 0
        loc_mat = 0
        miss = []
        for p in ["prathama", "madhyama", "uttama"]:
            for v in ["eka", "dvi", "bahu"]:
                forms, _ = te.derive(dhatu, code, p, v)
                loc_tot += 1
                total += 1
                if check_slot(forms):
                    loc_mat += 1
                    matched += 1
                else:
                    miss.append((f"{p} {v}", forms[0]))
        if verbose:
            status = "✓" if loc_mat == loc_tot else "⚠"
            print(f"  {status} {code:8s} {loc_mat:2d}/{loc_tot:2d}" + ("" if loc_mat == loc_tot else f"  e.g. {miss[0]}"))

    # krdanta
    if verbose:
        print("\n-- krdanta (tri-linga + avyaya) --")
    krd = ke.derive_all_krdantas(dhatu)
    for code, item in krd.items():
        if "M" in item:
            for g in ["M", "F", "N"]:
                total += 1
                if check_slot([item[g]]):
                    matched += 1
                elif verbose:
                    print(f"  miss {code} {g}: {item[g]} ({slp1_to_devanagari(item[g])})")
                    total -= 0  # keep count
                    # don't increment matched
                else:
                    pass
                # we counted total already, need to adjust if miss
                # simpler: recount
                # actually we already counted, just need to not double
                # fix: we added total, now if miss we keep total but not matched
                # so we need to not double-count above
                # The above logic double counts: we do total+=1 then if miss we don't matched, correct.
                pass
        elif "avyaya" in item:
            total += 1
            cand = item["avyaya"] if isinstance(item["avyaya"], list) else [item["avyaya"]]
            if check_slot(cand):
                matched += 1
            elif verbose:
                print(f"  miss {code} avyaya: {cand}")
        else:
            total += 1
            if check_slot([item["form"]]):
                matched += 1
            elif verbose:
                print(f"  miss {code}: {item['form']}")

    # Recompute correctly for krdanta (the above incremental for M/F/N was messy, recompute cleanly)
    # To avoid double-count bug, recompute from scratch for krdanta part only if we printed misses
    # Instead just recompute total/matched for krdanta cleanly:
    # (We already have total/matched with tintana; now we need to correct krdanta counts)
    # Quick fix: recount krdanta separately and adjust
    # Let's recompute krdanta totals accurately
    k_tot = 0
    k_mat = 0
    for code, item in krd.items():
        if "M" in item:
            for g in ["M", "F", "N"]:
                k_tot += 1
                if check_slot([item[g]]):
                    k_mat += 1
        elif "avyaya" in item:
            k_tot += 1
            cand = item["avyaya"] if isinstance(item["avyaya"], list) else [item["avyaya"]]
            if check_slot(cand):
                k_mat += 1
        else:
            k_tot += 1
            if check_slot([item["form"]]):
                k_mat += 1
    # total already includes krdanta counts (with potential off-by), so correct:
    # total = tinanta_total (90) + k_tot ; matched = tinanta_matched + k_mat
    # We have tinanta total = 90, so derive:
    tinanta_total = 90
    # But if dhatu is Atmanepadi vs Parasmaipada, tinanta total still 90 (10*9)
    # So recompute:
    # Instead just set total/matched correctly:
    # tinanta part we computed correctly as 90, now replace krdanta part
    # total_tin = 90, matched_tin = sum of tinanta matches
    # For now just print final recomputed
    # To keep function return correct, recompute everything cleanly:
    total2 = 0
    matched2 = 0
    for code, _ in lakaras:
        for p in ["prathama", "madhyama", "uttama"]:
            for v in ["eka", "dvi", "bahu"]:
                forms, _ = te.derive(dhatu, code, p, v)
                total2 += 1
                if check_slot(forms):
                    matched2 += 1
    total2 += k_tot
    matched2 += k_mat
    total, matched = total2, matched2

    if verbose:
        print("-" * 75)
        print(f"GRAND  {matched}/{total}  ({matched/total*100:.1f}%)  {'✓ ALL MATCHED' if matched==total else '⚠ missing'}")
        print("=" * 75)

    return matched, total


# ---------- unittest / pytest entry ----------

class TestDhatuGenerative(unittest.TestCase):
    """One parametrized test — pass DHATU env or default to 01.0002."""

    def _check(self, arg: str):
        matched, total = validate_dhatu(arg, verbose=False)
        # 100% required for BvAdi; allow 95%+ for other ganas? For CI we enforce 100%
        self.assertEqual(matched, total, f"{arg}: {matched}/{total} — generative mismatch vs JSON")

    def test_01_0001_BU(self):
        self._check("01.0001")

    def test_01_0002_eD(self):
        self._check("01.0002")

    def test_01_0003_sparD(self):
        self._check("01.0003")

    def test_cli(self):
        arg = os.getenv("DHATU", "01.0002")
        self._check(arg)


# pytest will collect this too
def test_generative_via_env():
    arg = os.getenv("DHATU", "01.0002")
    matched, total = validate_dhatu(arg, verbose=False)
    assert matched == total, f"{arg}: {matched}/{total}"


def main():
    parser = argparse.ArgumentParser(description="Generative dhatu validation vs JSON")
    parser.add_argument("dhatu", nargs="?", default=os.getenv("DHATU", "01.0002"), help="ID 01.0002 or SLP1 dhatu eD/BU")
    parser.add_argument("--id", dest="dhatu_id", help="alias for dhatu positional")
    parser.add_argument("-v", "--verbose", action="store_true", default=True)
    parser.add_argument("-q", "--quiet", action="store_true")
    args = parser.parse_args()
    arg = args.dhatu_id or args.dhatu
    verbose = not args.quiet
    matched, total = validate_dhatu(arg, verbose=verbose)
    sys.exit(0 if matched == total else 1)


if __name__ == "__main__":
    main()
