"""Fast prefixed-forms sweep — shared engines (no per-task cache reload), threaded.

Mirrors tests/test_dhatu.py::validate_dhatu(prefix=...) logic exactly, but reuses
module-level TinantaDerivationEngine / KrdantaEngine (warmed once) instead of
constructing fresh engines per call. Exact-match only, no fuzzy.

Usage:
  python tests/sweep_upasargas_fast.py --tasks "01.1096:vi,01.0003:vi" --workers 2 --out /tmp/prefix_tiny.csv
  python tests/sweep_upasargas_fast.py --gana 01 --workers 8
  python tests/sweep_upasargas_fast.py --fid 01.1096 --prefix vi

Output CSV schema matches tests/sweep_upasargas.py:
  fid,matched,total,pct,secs,misses,skipped
(misses truncated like tests/sweep_gana.py: first 5 tinanta, cap 12 total).

PYTHONHASHSEED-respecting: tasks sorted, results sorted, no set-order dependence
(token sets are membership-only).
"""
import argparse
import csv
import glob
import json
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from pypanini import TinantaDerivationEngine, KrdantaEngine
from tests.test_dhatu import DATA_ROOT, resolve_json_path, resolve_dhatu_slp, extract_all_text_tokens

TE = TinantaDerivationEngine()
KE = KrdantaEngine()
# warm caches once (no per-task reload)
TE._load_cache()
KE._load_cache()

ANTA_MAP = {
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
LAKARAS = ["lw", "liw", "luw", "lfw", "low", "laN", "viDiliN", "ASIrliN", "luN", "lfN"]
KRUT_MAP = {
    "krut": None,
    "san_krut": "sannanta",
    "nich_krut": "nijanta",
    "yang_krut": "yananta",
    "yangluk_krut": "yanluganta",
}


def validate_one_prefixed(task: str):
    """task is 'FID:prefix' (prefix may contain ';', never ':')."""
    t0 = time.time()
    try:
        fid, prefix = task.rsplit(":", 1)
        jp = resolve_json_path(fid)
        dhatu = resolve_dhatu_slp(jp, fid)
        data = json.load(open(jp, encoding="utf-8"))
        if "upasarga_forms" not in data or prefix not in data["upasarga_forms"]:
            return {"fid": task, "matched": 0, "total": 0, "pct": "0.0",
                    "secs": 0.0, "misses": "SKIPPED:no_data", "skipped": 0}
        # restrict tokens to this prefix block only (mirrors validate_dhatu)
        toks = extract_all_text_tokens(data["upasarga_forms"][prefix])

        def hit(forms):
            return any(f in toks for f in forms)

        dhatu_id = jp.stem
        total = matched = 0
        misses = []
        # ---- tinanta ----
        conjugations = data["upasarga_forms"][prefix].get("conjugations", {})
        antas = [k for k in ANTA_MAP if k in conjugations] or ["ting"]
        for anta in antas:
            sanadi, prayoga = ANTA_MAP[anta]
            for code in LAKARAS:
                loc_tot = loc_mat = 0
                loc_miss = []
                for p in ["prathama", "madhyama", "uttama"]:
                    for v in ["eka", "dvi", "bahu"]:
                        try:
                            forms, _ = TE.derive(dhatu, code, p, v, prayoga=prayoga,
                                                sanadi=sanadi, upasarga=prefix,
                                                dhatu_id=dhatu_id, json_path=str(jp))
                        except Exception:
                            forms = []
                        loc_tot += 1
                        total += 1
                        if forms and hit(forms):
                            loc_mat += 1
                            matched += 1
                        else:
                            loc_miss.append(f"{anta}/{code}/{p}/{v}:{forms[0] if forms else '∅'}")
                # yangluk only lw meaningful (mirrors validate_dhatu rollback)
                if anta in ("yangluk", "yangluk_yak") and code != "lw":
                    total -= loc_tot
                    matched -= loc_mat
                    continue
                for m in loc_miss:
                    if len(misses) < 5:
                        misses.append(m)
        # ---- krdanta (attested-only scoring, mirrors validate_dhatu) ----
        participles = data["upasarga_forms"][prefix].get("participles", {})
        kantas = [k for k in KRUT_MAP if k in participles] or ["krut"]
        skipped = 0
        for kk in kantas:
            kd = KE.derive_all_krdantas(dhatu, sanadi=KRUT_MAP[kk], upasarga=prefix,
                                       dhatu_id=dhatu_id)
            attested = participles.get(kk, {})
            for code, item in kd.items():
                if code not in attested:
                    skipped += 1 if "M" not in item and "avyaya" not in item else (3 if "M" in item else 1)
                    continue
                if "M" in item:
                    for g in ["M", "F", "N"]:
                        if g not in item:
                            continue
                        total += 1
                        cand = item[g] if isinstance(item[g], list) else [item[g]]
                        if hit(cand):
                            matched += 1
                        elif len(misses) < 12:
                            misses.append(f"{kk}/{code}/{g}:{item[g]}")
                elif "avyaya" in item:
                    total += 1
                    cand = item["avyaya"] if isinstance(item["avyaya"], list) else [item["avyaya"]]
                    if hit(cand):
                        matched += 1
                    elif len(misses) < 12:
                        misses.append(f"{kk}/{code}:{cand[0] if cand else '∅'}")
                elif "F" in item:
                    total += 1
                    cand = item["F"] if isinstance(item["F"], list) else [item["F"]]
                    if hit(cand):
                        matched += 1
                    elif len(misses) < 12:
                        misses.append(f"{kk}/{code}:{cand[0] if cand else '∅'}")
                    if "N" in item:
                        total += 1
                        cand = item["N"] if isinstance(item["N"], list) else [item["N"]]
                        if hit(cand):
                            matched += 1
                        elif len(misses) < 12:
                            misses.append(f"{kk}/{code}:{cand[0] if cand else '∅'}")
                elif "N" in item:
                    total += 1
                    cand = item["N"] if isinstance(item["N"], list) else [item["N"]]
                    if hit(cand):
                        matched += 1
                    elif len(misses) < 12:
                        misses.append(f"{kk}/{code}:{cand[0] if cand else '∅'}")
                else:
                    total += 1
                    _f = item.get("form")
                    _c = _f if isinstance(_f, list) else [_f]
                    if hit(_c):
                        matched += 1
                    elif len(misses) < 12:
                        misses.append(f"{kk}/{code}:{(_c[0] if _c else '∅')}")
        dt = time.time() - t0
        pct = (matched / total * 100.0) if total else 0.0
        return {"fid": task, "matched": matched, "total": total,
                "pct": f"{pct:.1f}", "secs": round(dt, 1),
                "misses": " | ".join(misses) if misses else ("SKIPPED:no_data" if total == 0 else ""),
                "skipped": skipped}
    except Exception as e:
        return {"fid": task, "matched": 0, "total": 0, "pct": "0.0",
                "secs": 0.0, "misses": f"ERROR:{e}"[:300], "skipped": 0}


def gather_tasks(gana: str):
    """All fid:prefix tasks for a gana dir (sorted; mirrors sweep_upasargas.py)."""
    pats = [ROOT / "skt-morph-data" / gana / "*.json",
            Path("skt-morph-data") / gana / "*.json"]
    files = []
    for pat in pats:
        files.extend(glob.glob(str(pat)))
    # dedupe by stem, sorted for determinism
    seen = sorted({Path(f).stem for f in files})
    tasks = []
    for fid in seen:
        for pat in pats:
            pass
        jp = next((p for p in [ROOT / "skt-morph-data" / gana / f"{fid}.json",
                               Path("skt-morph-data") / gana / f"{fid}.json"] if Path(p).exists()), None)
        if jp is None:
            continue
        try:
            data = json.load(open(jp, encoding="utf-8"))
        except Exception:
            continue
        for prefix in sorted(data.get("upasarga_forms", {}).keys()):
            tasks.append(f"{fid}:{prefix}")
    return tasks


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gana", default="01")
    ap.add_argument("--tasks", default="", help="comma-separated fid:prefix list")
    ap.add_argument("--fid", default="")
    ap.add_argument("--prefix", default="")
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--out", default="")
    args = ap.parse_args()
    if args.tasks:
        tasks = sorted({t.strip() for t in args.tasks.split(",") if t.strip()})
        if not args.out:
            args.out = "tests/sweep_prefixed_tasks_fast.csv"
    elif args.fid:
        if args.prefix:
            tasks = [f"{args.fid}:{args.prefix}"]
        else:
            tasks = [t for t in gather_tasks(args.gana) if t.startswith(f"{args.fid}:")]
        if not args.out:
            args.out = "tests/sweep_prefixed_tasks_fast.csv"
    else:
        tasks = gather_tasks(args.gana)
        if not args.out:
            args.out = f"tests/sweep_prefixed_{args.gana}_fast.csv"
    print(f"prefix sweep {len(tasks)} tasks, workers={args.workers} (shared engine cache, no reload)", flush=True)
    results = []
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = {ex.submit(validate_one_prefixed, t): t for t in tasks}
        for fu in as_completed(futs):
            r = fu.result()
            results.append(r)
            print(f"{r['fid']} => {r['matched']}/{r['total']} ({r['pct']}%) [{r['secs']}s]"
                  + (f" misses: {r['misses'][:200]}" if r["misses"] else ""), flush=True)
    results.sort(key=lambda r: r["fid"])
    tm = sum(r["matched"] for r in results)
    tt = sum(r["total"] for r in results)
    pct = (tm / tt * 100.0) if tt else 0.0
    print(f"Total: {tm}/{tt} ({pct:.2f}%)")
    with open(args.out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["fid", "matched", "total", "pct", "secs", "misses", "skipped"])
        w.writeheader()
        for r in results:
            w.writerow(r)
    print(f"wrote {args.out}")


if __name__ == "__main__":
    main()
