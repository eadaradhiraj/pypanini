import os
import glob
import json
import time
import multiprocessing
from test_dhatu import validate_dhatu

def process_file(fpath):
    fname = os.path.basename(fpath)
    fid = fname.replace(".json", "")
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)
    upasarga_forms = data.get("upasarga_forms", {})
    
    results = []
    for prefix in upasarga_forms.keys():
        try:
            matched, total = validate_dhatu(fid, verbose=False, prefix=prefix)
            results.append((fid, prefix, matched, total))
        except Exception as e:
            results.append((fid, prefix, 0, 1))
    return results

def main():
    files = glob.glob("skt-morph-data/01/*.json")
    files.sort()
    
    print(f"Starting parallel sweep on {len(files)} Gaṇa 1 files...")
    start = time.time()
    
    total_matched = 0
    total_expected = 0
    processed = 0
    
    with open("logs_misses.txt", "w") as f_miss:
        with multiprocessing.Pool() as pool:
            for file_results in pool.imap_unordered(process_file, files):
                processed += 1
                for fid, prefix, matched, total in file_results:
                    total_matched += matched
                    total_expected += total
                    if matched < total:
                        f_miss.write(f"{fid} + {prefix} => {matched}/{total} ({(matched/total*100):.1f}%)\n")
                
                if processed % 10 == 0:
                    pct = (total_matched / total_expected * 100.0) if total_expected else 0.0
                    print(f"[{processed}/{len(files)}] Accuracy so far: {total_matched}/{total_expected} ({pct:.2f}%)", flush=True)

    pct_total = (total_matched / total_expected * 100.0) if total_expected else 0.0
    print(f"\nFinished in {time.time() - start:.1f}s")
    print(f"Total Accuracy: {total_matched}/{total_expected} ({pct_total:.2f}%)")

if __name__ == "__main__":
    main()
