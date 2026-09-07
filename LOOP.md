# pypanini autonomous sweep loop — proper prompt

Use with exactly ONE driver (see Loop hygiene). Suggested start:

```
/loop stop 16
/loop "$(cat LOOP.md | sed -n '/^> /s/^> //p' | tr '\n' ' ')" --every 15m --max-fires 100
```

Or paste the quoted block below as the `/loop` prompt directly.

> Work toward 1166/1166 100% for skt-morph-data/01, wholly generative: no per-dhatu hardcoding, no per-dhatu lists, no JSON import for generation. Derive only from pada / sew / gana / antargana / vowel-initial / shape / onset-coda / sanadi / prayoga. Engine scope: pypanini/tinanta.py + pypanini/krdanta.py only (phonetics/pratyahara stay pure); pilots 01.0001, 01.0002, 01.0003 must stay 100%. Each iteration does all of: (1) pick ONE batch of 5-10 failing dhatus sharing a single shape trait (query tests/sweep_all.csv for smallest matched-gap or a shared miss signature); (2) prove the rule with data, not anecdotes — survey every dataset root matching the shape for expected-token conflicts and require zero conflicts before coding; (3) implement ONE narrow general rule; (4) verify cheap first: unittest pilots + tests/test_dhatu.py on touched dhatus + guard dhatus from PROGRESS.md; (5) full sweep tests/sweep_gana.py --all --workers 8 --out tests/sweep_all.csv; (6) gate on fid-diff vs HEAD with the script below — passes up, or passes held with improved>0 and worsened==0: rebuild tests/STATS.md from true sweep numbers, overwrite PROGRESS.md (done/next, never append), commit and push; passes down or worsened>0: git checkout the code + csv (revert), no commit, record the failed hypothesis in PROGRESS.md Next and move on; (7) never run two sweeps concurrently. Miss-by-anta sampled counts are misleading (miss lists are capped per dhatu) — fid-level improved/worsened is the only truth. Known divergences, do not re-learn: krdanta Natva and loT Ri differ (s-final+r roots: pras krdanta dental but loT ARi; h-final+r roots: garh krdanta R but loT dental); R-final uppercase (GuR/pER) stays dental everywhere; sparD stays dental; sannanta krdanta is always-R (hardcoded, passing, do not touch); harness keeps "-" as a token (scoring only).

Fid-diff gate script (run after every sweep):

```bash
PYTHONIOENCODING=utf-8 python -c "
import csv,subprocess
cur={r['fid']:(int(r['matched']),int(r['total'])) for r in csv.DictReader(open('tests/sweep_all.csv',encoding='utf-8'))}
old=subprocess.run(['git','show','HEAD:tests/sweep_all.csv'],capture_output=True,text=True).stdout.splitlines()
old={r['fid']:(int(r['matched']),int(r['total'])) for r in csv.DictReader(old)}
up=[(f,om,m) for f,(m,t) in cur.items() for om,ot in [old.get(f,(m,0))] if m>om]
dn=[(f,om,m) for f,(m,t) in cur.items() for om,ot in [old.get(f,(m,0))] if m<om]
print('improved:',len(up),up)
print('worsened:',len(dn),dn)
"
```

## Loop hygiene (read this, it bit us before)

- One driver only. A full sweep takes ~10 minutes; a 5-minute cron overlaps itself and two concurrent sweeps corrupt the shared `tests/sweep_all.csv`. Use `--every 15m` cron, or self-paced (`schedule_loop_wakeup` after the push, small delay) — never both, never 5m-or-less cron.
- If a turn finds the tree dirty from a killed overlapping run, `git status` first; do not commit mixed-iteration state.
- `tests/STATS.md` numbers must always come from the latest sweep output, never from memory or prior iterations (stale STATS caused false alarms twice).
