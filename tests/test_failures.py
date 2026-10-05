import sys
import json
from test_dhatu import validate_dhatu

def main():
    with open("logs_misses.txt", "r") as f:
        lines = f.readlines()
        
    failures = []
    for line in lines:
        if "=>" in line:
            parts = line.split("=>")
            left = parts[0].strip()
            fid, prefix = left.split(" + ")
            fid = fid.strip()
            prefix = prefix.strip()
            # If accuracy was 100%, skip
            right = parts[1].strip()
            if "(100.0%)" not in right:
                failures.append((fid, prefix))
                
    print(f"Loaded {len(failures)} failures to re-test.")
    
    still_failing = []
    for fid, prefix in failures:
        try:
            matched, total = validate_dhatu(fid, verbose=False, prefix=prefix)
            if matched < total:
                still_failing.append((fid, prefix, matched, total))
        except Exception as e:
            still_failing.append((fid, prefix, 0, 1))
            
    print(f"\nRemaining failures after recent patches: {len(still_failing)}")
    for fid, prefix, matched, total in still_failing[:20]:
        print(f"{fid} + {prefix} => {matched}/{total} ({(matched/total*100):.1f}%)")
        
    with open("logs_misses_current.txt", "w") as f:
        for fid, prefix, matched, total in still_failing:
            f.write(f"{fid} + {prefix} => {matched}/{total} ({(matched/total*100):.1f}%)\n")

if __name__ == "__main__":
    main()
