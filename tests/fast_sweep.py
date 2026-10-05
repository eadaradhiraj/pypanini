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
            results.append((fid, prefix, 0, 1)) # Count as failure
    return results

def main():
    files = glob.glob("skt-morph-data/01/*.json")
    files.sort()
    
    print(f"Starting multiprocessing sweep on {len(files)} files...")
    start = time.time()
    
    total_matched = 0
    total_expected = 0
    
    # Use all available CPU cores
    with multiprocessing.Pool() as pool:
        for file_results in pool.imap_unordered(process_file, files[:100]): # Test on first 100 for speed
            for fid, prefix, matched, total in file_results:
                total_matched += matched
                total_expected += total
                
    pct_total = (total_matched / total_expected * 100.0) if total_expected else 0.0
    print(f"Processed 100 files in {time.time() - start:.1f}s")
    print(f"Accuracy: {total_matched}/{total_expected} ({pct_total:.2f}%)")

if __name__ == "__main__":
    main()
