"""Fast whole-gana sweep — shared engines (no per-dhatu cache reload), threaded, detailed misses.
Usage:
  python tests/sweep_gana.py --from 01.0038 --to 01.0100 --workers 8
  python tests/sweep_gana.py --all --workers 8 --out sweep.csv
JSON is read-only cross-check, never used for generation.
"""
import argparse, glob, json, os, sys, time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from pypanini import TinantaDerivationEngine, KrdantaEngine
from tests.test_dhatu import DATA_ROOT, resolve_json_path, resolve_dhatu_slp, extract_all_text_tokens

TE = TinantaDerivationEngine()
KE = KrdantaEngine()
# warm caches once (loads 1166 metas a single time)
TE._load_cache()
KE._load_cache()

ANTA_MAP = {
    "ting": (None, "kartari"), "yak": (None, "karmani"),
    "san": ("sannanta", "kartari"), "san_yak": ("sannanta", "karmani"),
    "nich": ("nijanta", "kartari"), "nich_yak": ("nijanta", "karmani"),
    "yang": ("yananta", "kartari"), "yang_yak": ("yananta", "karmani"),
    "yangluk": ("yanluganta", "kartari"), "yangluk_yak": ("yanluganta", "karmani"),
}
LAKARAS = ["lw","liw","luw","lfw","low","laN","viDiliN","ASIrliN","luN","lfN"]
KRUT_MAP = {"krut": None, "san_krut": "sannanta", "nich_krut": "nijanta", "yang_krut": "yananta", "yangluk_krut": "yanluganta"}

def validate_one(fid: str):
    t0 = time.time()
    try:
        jp = resolve_json_path(fid)
        dhatu = resolve_dhatu_slp(jp, fid)
        data = json.load(open(jp, encoding="utf-8"))
        toks = extract_all_text_tokens(data)
        def hit(forms):
            return any(f in toks for f in forms)
        dhatu_id = jp.stem
        total = matched = 0
        misses = []  # (anta, lakara, purusha, vacana, sample)
        conjugations = data.get("conjugations", {})
        antas = [k for k in ANTA_MAP if k in conjugations] or ["ting"]
        for anta in antas:
            sanadi, prayoga = ANTA_MAP[anta]
            for code in LAKARAS:
                # yangluk only lw meaningful (mirrors test_dhatu verbose=True counting)
                if anta in ("yangluk","yangluk_yak") and code != "lw":
                    continue
                for p in ["prathama","madhyama","uttama"]:
                    for v in ["eka","dvi","bahu"]:
                        total += 1
                        try:
                            forms,_ = TE.derive(dhatu, code, p, v, prayoga=prayoga, sanadi=sanadi, dhatu_id=dhatu_id, json_path=str(jp))
                        except Exception:
                            forms = []
                        if forms and hit(forms):
                            matched += 1
                        else:
                            if len(misses) < 5:
                                misses.append(f"{anta}/{code}/{p}/{v}:{forms[0] if forms else '∅'}")
        # krdanta
        part = data.get("participles", {})
        kantas = [k for k in KRUT_MAP if k in part] or ["krut"]
        for kk in kantas:
            kd = KE.derive_all_krdantas(dhatu, sanadi=KRUT_MAP[kk], dhatu_id=dhatu_id)
            for code, item in kd.items():
                if "M" in item:
                    for g in ["M","F","N"]:
                        total += 1
                        if item[g] in toks: matched += 1
                        elif len(misses) < 12: misses.append(f"{kk}/{code}/{g}:{item[g]}")
                elif "avyaya" in item:
                    total += 1
                    cand = item["avyaya"] if isinstance(item["avyaya"], list) else [item["avyaya"]]
                    if hit(cand): matched += 1
                    elif len(misses) < 12: misses.append(f"{kk}/{code}:{cand[0] if cand else '∅'}")
                else:
                    total += 1
                    if item.get("form") in toks: matched += 1
                    elif len(misses) < 12: misses.append(f"{kk}/{code}:{item.get('form')}")
        dt = time.time()-t0
        return {"fid": fid, "matched": matched, "total": total, "pct": round(matched/total*100,1) if total else 0, "misses": misses, "secs": round(dt,1)}
    except Exception as e:
        return {"fid": fid, "matched": 0, "total": 0, "pct": 0, "misses": [f"ERR:{e}"[:120]], "secs": 0}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--from", dest="fro", default="01.0001")
    ap.add_argument("--to", dest="to", default="01.0100")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--out", default="")
    args = ap.parse_args()
    if args.all:
        fids = [f"01.{i:04d}" for i in range(1, 1167)]
    else:
        a = int(args.fro.split(".")[1]); b = int(args.to.split(".")[1])
        fids = [f"01.{i:04d}" for i in range(a, b+1)]
    print(f"sweep {len(fids)} dhatus, workers={args.workers} (shared engine cache, no reload)", flush=True)
    results = []
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = {ex.submit(validate_one, f): f for f in fids}
        for i, fu in enumerate(as_completed(futs)):
            r = fu.result()
            results.append(r)
            flag = "OK " if r["matched"]==r["total"] and r["total"] else "FAIL"
            print(f"{flag} {r['fid']} {r['matched']}/{r['total']} {r['pct']}% ({r['secs']}s) {' | '.join(r['misses'][:3])}", flush=True)
    results.sort(key=lambda r: r["fid"])
    ok = sum(1 for r in results if r["matched"]==r["total"] and r["total"])
    print(f"\nDONE passes {ok}/{len(results)}")
    # category summary for fails (which anta/lakara breaks most)
    from collections import Counter
    cat = Counter()
    for r in results:
        if r["matched"]!=r["total"]:
            for m in r["misses"]:
                cat[m.split(":")[0].split("/")[0]] += 1
    print("miss-by-anta:", dict(cat.most_common(15)))
    if args.out:
        import csv
        with open(args.out, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=["fid","matched","total","pct","secs","misses"])
            w.writeheader()
            for r in results:
                w.writerow({**r, "misses": " | ".join(r["misses"])})
        print(f"wrote {args.out}")

if __name__ == "__main__":
    main()
