with open("tests/parallel_sweep.py", "r") as f:
    k = f.read()
k = k.replace("print(f\"[{processed}/{len(files)}] Accuracy so far: {total_matched}/{total_expected} ({pct:.2f}%)\")", "print(f\"[{processed}/{len(files)}] Accuracy so far: {total_matched}/{total_expected} ({pct:.2f}%)\", flush=True)")
with open("tests/parallel_sweep.py", "w") as f: f.write(k)
