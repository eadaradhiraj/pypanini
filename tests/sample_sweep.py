import os
import glob
import json
import random
import time
from test_dhatu import validate_dhatu

def run_sample():
    files = glob.glob("skt-morph-data/01/*.json")
    files.sort()
    
    # Collect all valid (fid, prefix) pairs
    pairs = []
    for fpath in files:
        fname = os.path.basename(fpath)
        fid = fname.replace(".json", "")
        with open(fpath, "r", encoding="utf-8") as f:
            data = json.load(f)
        upasarga_forms = data.get("upasarga_forms", {})
        for prefix in upasarga_forms.keys():
            pairs.append((fid, prefix))
            
    # Randomly select 20 pairs
    random.seed(42) # For reproducibility
    sample = random.sample(pairs, 20)
    
    print(f"Total prefix combinations found: {len(pairs)}")
    print(f"Running random sample of {len(sample)} combinations...\n")
    
    total_matched = 0
    total_expected = 0
    start = time.time()
    
    for fid, prefix in sample:
        try:
            matched, total = validate_dhatu(fid, verbose=False, prefix=prefix)
            pct = (matched / total * 100.0) if total else 0.0
            print(f"{fid} + {prefix} => {matched}/{total} ({pct:.1f}%)")
            total_matched += matched
            total_expected += total
        except Exception as e:
            print(f"{fid} + {prefix} => ERROR: {e}")
            
    pct_total = (total_matched / total_expected * 100.0) if total_expected else 0.0
    print(f"\nSample Sweep Finished in {time.time() - start:.1f}s")
    print(f"Total Accuracy: {total_matched}/{total_expected} ({pct_total:.2f}%)")

if __name__ == "__main__":
    run_sample()
