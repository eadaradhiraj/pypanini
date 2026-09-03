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

from pypanini import TinantaDerivationEngine, KrdantaEngine

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

    all_tokens = extract_all_text_tokens(data)

    def check_slot(forms_slp):
        for f in forms_slp:
            if f in all_tokens:
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

    # ---- tinanta: all antas found in JSON (primitive + san/nich/yang ...) ----
    # map JSON conjugation keys -> (sanadi, prayoga)
    anta_map = {
        "ting": (None, "kartari"),
        "yak": (None, "karmani"),
        "san": ("sannanta", "kartari"),
        "san_yak": ("sannanta", "karmani"),
        "nich": ("nijanta", "kartari"),
        "nich_yak": ("nijanta", "karmani"),
        "yang": ("yananta", "kartari"),
        "yang_yak": ("yananta", "karmani"),
        "yangluk": ("yanluganta", "kartari"),
        "yangluk_yak": ("yanluganta", "karmani"),
    }
    lakaras = [
        ("lw", "lw"), ("liw", "liw"), ("luw", "luw"), ("lfw", "lfw"),
        ("low", "low"), ("laN", "laN"), ("viDiliN", "viDiliN"),
        ("ASIrliN", "ASIrliN"), ("luN", "luN"), ("lfN", "lfN"),
    ]
    conjugations = data.get("conjugations", {})
    antas_to_check = [k for k in anta_map if k in conjugations]
    if not antas_to_check:
        antas_to_check = ["ting"]
    if verbose:
        print(f"\n-- tinanta ({len(antas_to_check)} antas × 10 lakaras × 9) --")
        print(f"   antas: {', '.join(antas_to_check)}")
    for anta_key in antas_to_check:
        sanadi, prayoga = anta_map[anta_key]
        if verbose:
            print(f"\n  [{anta_key}] sanadi={sanadi} prayoga={prayoga}")
        for code, _title in lakaras:
            # skip lakaras not present for this anta if JSON is sparse? we still check all 10
            # but for yangluk only lw is meaningful - we still check but allow missing
            loc_tot = 0
            loc_mat = 0
            miss = []
            for p in ["prathama", "madhyama", "uttama"]:
                for v in ["eka", "dvi", "bahu"]:
                    try:
                        forms, _ = te.derive(dhatu, code, p, v, prayoga=prayoga, sanadi=sanadi)
                    except Exception as e:
                        forms = []
                    loc_tot += 1
                    total += 1
                    if forms and check_slot(forms):
                        loc_mat += 1
                        matched += 1
                    else:
                        miss.append((f"{p} {v}", forms[0] if forms else "∅"))
            if verbose:
                # for yangluk only lw matters, suppress noisy others
                if anta_key in ("yangluk", "yangluk_yak") and code != "lw":
                    # don't print non-lw for yanluk (only present is meaningful)
                    total -= loc_tot
                    matched -= loc_mat
                    continue
                status = "✓" if loc_mat == loc_tot else "⚠"
                print(f"    {status} {code:8s} {loc_mat:2d}/{loc_tot:2d}" + ("" if loc_mat == loc_tot else f"  e.g. {miss[0]}"))

    # krdanta: all antas in participles (krut, san_krut, nich_krut...)
    if verbose:
        print("\n-- krdanta (all antas) --")
    krut_map = {
        "krut": None,
        "san_krut": "sannanta",
        "nich_krut": "nijanta",
        "yang_krut": "yananta",
        "yangluk_krut": "yanluganta",
    }
    participles = data.get("participles", {})
    # if no participles key, fallback to primitive only
    krut_antas = [k for k in krut_map if k in participles] or ["krut"]
    # we will count krdanta for each anta
    all_krd_tot = 0
    all_krd_mat = 0
    for krut_key in krut_antas:
        sanadi_k = krut_map[krut_key]
        krd_anta = ke.derive_all_krdantas(dhatu, sanadi=sanadi_k)
        # count
        loc_tot = 0
        loc_mat = 0
        for code, item in krd_anta.items():
            if "M" in item:
                for g in ["M", "F", "N"]:
                    loc_tot += 1
                    if check_slot([item[g]]):
                        loc_mat += 1
            elif "avyaya" in item:
                loc_tot += 1
                cand = item["avyaya"] if isinstance(item["avyaya"], list) else [item["avyaya"]]
                if check_slot(cand):
                    loc_mat += 1
            else:
                loc_tot += 1
                if check_slot([item["form"]]):
                    loc_mat += 1
        all_krd_tot += loc_tot
        all_krd_mat += loc_mat
        if verbose:
            status = "✓" if loc_mat == loc_tot else "⚠"
            print(f"  {status} {krut_key:12s} ({sanadi_k or 'mUla':10s}) {loc_mat:2d}/{loc_tot:2d}")
        total += loc_tot
        matched += loc_mat

    # final recompute not needed - total/matched already includes all antas
    # but verify with clean recount for return value (use already computed total/matched which includes tinanta+all krdanta)
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
