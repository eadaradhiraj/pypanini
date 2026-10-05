import sys
import multiprocessing
from test_dhatu import validate_dhatu

def test_one(item):
    fid, prefix = item
    try:
        matched, total = validate_dhatu(fid, verbose=False, prefix=prefix)
        return (fid, prefix, matched, total)
    except Exception as e:
        return (fid, prefix, 0, 1)

def main():
    with open("logs_misses.txt", "r") as f:
        lines = f.readlines()
        
    failures = []
    for line in lines:
        if "=>" in line:
            parts = line.split("=>")
            left = parts[0].strip()
            fid, prefix = left.split(" + ")
            failures.append((fid.strip(), prefix.strip()))
                
    print(f"Loaded {len(failures)} failures to re-test in parallel.")
    
    still_failing = []
    with multiprocessing.Pool() as pool:
        for res in pool.imap_unordered(test_one, failures):
            fid, prefix, matched, total = res
            if matched < total:
                still_failing.append(res)
            
    print(f"\nRemaining failures after recent patches: {len(still_failing)}")
    for fid, prefix, matched, total in still_failing[:20]:
        print(f"{fid} + {prefix} => {matched}/{total} ({(matched/total*100):.1f}%)")
        
    with open("logs_misses_current.txt", "w") as f:
        for fid, prefix, matched, total in still_failing:
            f.write(f"{fid} + {prefix} => {matched}/{total} ({(matched/total*100):.1f}%)\n")

if __name__ == "__main__":
    main()
