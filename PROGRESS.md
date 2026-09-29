# Progress — Done / Next (overwritten each iteration, not appended)

Date: 2026-09-29
Sweep-all: **1156/1156 100%** (raw 1156/1166, 10 skipped; GRAND 994971/994971 attested) — held, fid-diff gate 0/0.
Sweep-02: **77/77 100%** — complete (other session).
Sweep-03: **26/26 100%** — complete (other session).
Sweep-05: **38/38 100%** — complete (other session, GEN-05).
Sweep-07: **25/25 100%** — complete (other session).
Sweep-08: **10/10 100%** — complete (other session).
Sweep-09: **52/71** — held passes, +27 matched, 3 improved / 0 worsened (this iteration).
Sweep-04: 4/163, Sweep-06: 22/174, Sweep-10: 162/509 (per-gana csvs predate this iteration; untouched by construction — this iteration's code is kryAdiH-gated).

## Done — luw-trio sya-futures (iteration 230)
- mAsyati/kzezyati/grahIzyati (same A-stems as luw; z/s split by stem vowel; both padas banD-style).
- Gates: trio lfw 9/9 each; pilots 5/5; 09 fid-diff 3/0; 01 fid-diff 0/0.
- Prior (229): labial-F U-grade family (see STATS).
- KryAdi luw A-stems (mAtA/kzetA/grahItA) + banD Bantsyati future (HEAD code, ungated): gated via sweep_09 (+35, 4 improved, 0 worsened). Fixed kzetA stem (kze, not kzet) by probe.
- SrA/jYA san-iz repair: commit 8dd6aa6 had dropped load-bearing SiSriz/jijYiz stems (-360 in 01.0922/0923, hidden by stale sweep_all.csv). Restored as surveyed shape class (c + op + BvAdiH, both engines; per-fid dhatu_id removed). 01.1067 SrE exclusion proven live (op-gate required: krdanta remaps SrE→SrA).
- Gates: pilots 5/5; 01.0922/0923/1067 100%; full sweep 1156/1156, miss-by-anta {}; GRAND 994971/994971 reproduced exactly.
- Lesson recorded in STATS: re-sweep after every code commit before pushing; never trust csv newer-code-than-csv.

## Next
1. Gana-09 loop: trio luN/lfN/san/nich/yang + san/nich residuals + krut mUla grades — 19 fids remain (no passes yet for 0004/0042/0071).
2. Gana loop: 04 (divAdi ya) → 06 (tudAdi a) → 10 (curAdi aya) (02/03/05/07/08 done).
3. Cross-gana traits: nijanta-aorist gaps, mUla-aorist gaps.
4. cakz follow-ups; hardcoded "02.0055" fid in KyA/kSA block to revisit.
