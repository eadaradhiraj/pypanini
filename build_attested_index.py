"""Build the attested search index (one-time, background).

Every slash-split token from conjugations + participles +
upasarga_forms across all skt-morph-data JSONs, with its provenance
(fid, dhatu, kind, lakara/pratyaya, slots, prefix). Search consults
this SQLite index first (millisecond exact lookups) and falls back to
live grep only when the DB is absent.

Usage:
  python build_attested_index.py --jobs 8
  python build_attested_index.py --gana 01 --jobs 8 --out /tmp/att.db

Output default: pypanini/attested_index.db (gitignored).
"""
import argparse
import os
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

DATA_CANDS = [os.getenv("SKT_MORPH_DATA") or "",
              "/home/edhiraj/Documents/projs/skt-morph-data/data",
              str(ROOT / "skt-morph-data")]


def resolve_data_root() -> Path | None:
    for c in DATA_CANDS:
        if c and Path(c).exists():
            return Path(c)
    return None


def fid_rows(jpath: str):
    """All (surface, provenance) rows for one JSON file."""
    from tests.audit_search_full import fid_expectations
    try:
        exps = fid_expectations(jpath, te=None, ke=None, do_engine=False)
    except Exception:
        return []
    rows = []
    for e in exps:
        slots = ";".join(f"{p}.{v}" for (p, v) in (e.get("slots") or []))
        rows.append((e["surface"], e["fid"], e.get("dhatu", ""),
                     e.get("kind", ""), e.get("lakara", "") or "",
                     e.get("pratyaya", "") or "", slots,
                     e.get("prefix", "") or "", e.get("sanadi", "") or "",
                     e.get("prayoga", "") or "", e.get("pada", "") or "",
                     e.get("linga", "") or ""))
    return rows


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--jobs", type=int, default=8)
    ap.add_argument("--gana", default=None)
    ap.add_argument("--fid", default=None)
    ap.add_argument("--fid-list", default=None)
    ap.add_argument("--max-fids", type=int, default=0)
    ap.add_argument("--out", default=str(ROOT / "pypanini"
                                        / "attested_index.db"))
    args = ap.parse_args()
    data = resolve_data_root()
    if not data:
        print("no skt-morph-data checkout found", flush=True)
        return 2
    import glob
    if args.fid:
        files = [str(data / args.fid[:2] / f"{args.fid}.json")]
    elif args.fid_list:
        files = [str(data / f.strip()[:2] / f"{f.strip()}.json")
                 for f in args.fid_list.split(",")]
    elif args.gana:
        pat = str(data / args.gana / "*.json")
        files = sorted(glob.glob(pat))
    else:
        pat = str(data / "*/*.json")
        files = sorted(glob.glob(pat))
    if args.max_fids:
        files = files[:args.max_fids]
    print(f"fids: {len(files)} -> {args.out}", flush=True)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    if out.exists():
        out.unlink()
    con = sqlite3.connect(str(out))
    con.execute("PRAGMA journal_mode=WAL")
    con.execute("PRAGMA synchronous=OFF")
    con.execute("""CREATE TABLE attested (
        surface TEXT, fid TEXT, dhatu TEXT, kind TEXT,
        lakara TEXT, pratyaya TEXT, slots TEXT, prefix TEXT,
        sanadi TEXT, prayoga TEXT, pada TEXT, linga TEXT)""")
    total = 0
    if args.jobs > 1:
        from concurrent.futures import ProcessPoolExecutor
        batch: list = []

        def _flush(b):
            con.executemany(
                "INSERT INTO attested VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                b)
            con.commit()

        with ProcessPoolExecutor(max_workers=args.jobs) as ex:
            futs = {ex.submit(fid_rows, f): f for f in files}
            done = 0
            for fut in futs:
                try:
                    rows = fut.result()
                except Exception as e:
                    print(f"FID-ERROR {futs[fut]}: {e}", flush=True)
                    continue
                batch.extend(rows)
                total += len(rows)
                done += 1
                if len(batch) >= 20000:
                    _flush(batch)
                    batch = []
                if done % 100 == 0:
                    print(f"  {done}/{len(files)} fids rows={total}",
                          flush=True)
        if batch:
            _flush(batch)
    else:
        batch = []
        for i, f in enumerate(files):
            rows = fid_rows(f)
            batch.extend(rows)
            total += len(rows)
            if len(batch) >= 20000:
                con.executemany(
                    "INSERT INTO attested VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                    batch)
                con.commit()
                batch = []
            if (i + 1) % 100 == 0:
                print(f"  {i + 1}/{len(files)} fids rows={total}",
                      flush=True)
        if batch:
            con.executemany(
                "INSERT INTO attested VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                batch)
            con.commit()
    con.execute("CREATE INDEX idx_surface ON attested(surface)")
    con.execute("ANALYZE")
    con.commit()
    n = con.execute("SELECT COUNT(*) FROM attested").fetchone()[0]
    u = con.execute("SELECT COUNT(DISTINCT surface) FROM attested"
                    ).fetchone()[0]
    print(f"rows={n} unique_surfaces={u}", flush=True)
    con.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
