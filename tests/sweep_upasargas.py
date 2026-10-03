import os
import sys
import glob
import json
import csv
import time
from test_dhatu import validate_dhatu

def run_sweep(gaṇa_prefix: str, out_file: str):
    start = time.time()
    
    # gather all JSONs
    if gaṇa_prefix == "all":
        files = glob.glob(f"skt-morph-data/*/*.json")
    else:
        files = glob.glob(f"skt-morph-data/{gaṇa_prefix}/*.json")
    
    files.sort()
    
    results = []
    total_matched = 0
    total_expected = 0
    
    for fpath in files:
        fname = os.path.basename(fpath)
        fid = fname.replace(".json", "")
        
        with open(fpath, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        upasarga_forms = data.get("upasarga_forms", {})
        if not upasarga_forms:
            continue
            
        for prefix in upasarga_forms.keys():
            try:
                matched, total = validate_dhatu(fid, verbose=False, prefix=prefix)
                pct = (matched / total * 100.0) if total else 0.0
                misses = ""
                if total == 0:
                    misses = "SKIPPED:no_data"
                results.append({
                    "fid": f"{fid}:{prefix}",
                    "matched": matched,
                    "total": total,
                    "pct": f"{pct:.1f}",
                    "misses": misses
                })
                total_matched += matched
                total_expected += total
                
                print(f"{fid}:{prefix} => {matched}/{total} ({pct:.1f}%)")
            except Exception as e:
                print(f"ERROR on {fid}:{prefix} - {e}")
                results.append({
                    "fid": f"{fid}:{prefix}",
                    "matched": 0,
                    "total": 0,
                    "pct": 0.0,
                    "misses": f"ERROR:{str(e)}"
                })

    if not results:
        print(f"No prefixed forms found for {gaṇa_prefix}")
        return

    # Write to CSV
    with open(out_file, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["fid", "matched", "total", "pct", "secs", "misses", "skipped"])
        writer.writeheader()
        for r in results:
            writer.writerow(r)
            
    pct_total = (total_matched / total_expected * 100.0) if total_expected else 0.0
    print(f"Finished {gaṇa_prefix} -> {out_file}")
    print(f"Total: {total_matched}/{total_expected} ({pct_total:.2f}%)")
    print(f"Time: {time.time() - start:.1f}s")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("gana", nargs="?", default="01", help="Gana prefix e.g. 01, 02, or all")
    args = parser.parse_args()
    
    run_sweep(args.gana, f"tests/sweep_prefixed_{args.gana}.csv")
