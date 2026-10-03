# Progress — Done / Next (overwritten each iteration, not appended)

Date: 2026-10-02
Sweep-01: **1156/1156 100%** — held, fid-diff 0/0.
Sweep-02: **76/76 zero-miss** — held.
Sweep-03: **26/26 100%** — held. Sweep-05: **38/38 100%** — held.
Sweep-07: **25/25 100%** — held. Sweep-08: **10/10 100%** — held.
Sweep-09: **71/71 100%** — held.
Sweep-04: **151/161** (other session) — ceiling audit in progress.
Sweep-06: **173/174 + 1 ceiling fid (06.0159 viC, 42 dataless slots)** — held.
Sweep-10: **316/492 scored** (17 skipped) — held (V-initial san + aya-less, 6 improved, 0 worsened; this iteration).
Landscape: 04 + 10 remain (06 modulo ceiling).

## Done — this session (06) + 460-467 + 585-656 (10)
- 06: iterations 383-398, 442-458 → 173/174 modulo 06.0159 ceiling (see STATS.md).
- 460: verify pull 7738ab6 + fresh sweeps (csv refresh).
- 461: curAdi general aya-twins ktvA/tumun (293 improved, +99 pass-ups).
- 462: curAdi lyap/lyuw aya-twins (124 improved, +63 pass-ups).
- 463: curAdi liw aya-periphrastic paras table (57 improved, holds 312).
- 464: curAdi san aya-redup stems (20 improved, +1 pass-up).
- 465: curAdi san-yak twins (30 improved, +3 pass-ups).
- 466: curAdi san-kta grade extensions (30 improved, holds 316).
- 467: vowel-initial san + aya-less grades (6 improved, holds 316).
- 585: shared _curAdi_sanV_secs helper (zero-diff) + san-ktavatu V-secs (9 improved, holds 316).
- 586: san-Satf V-secs via helper (9 improved, holds 316).
- 587: san-tavya V-secs via helper (15 improved, 318/492: PASS 10.0014/0105).
- 588: san-SAnac V-secs via helper (9 improved, holds 318).
- 589: san-matrix V-secs via helper (51 improved-tokens, V-san probe 0, holds 318).
- 590: vowel-final-i AY-presents (197 improved-tokens, holds 318).
- 591: f-grade yak twins (216 improved-tokens, 319/492: PASS 10.0028).
- 592: kta a+nD retention twins (12 improved-tokens, holds 319).
- 593: kta vowel-final-u Av-twins (9 improved-tokens, holds 319).
- 594: kta vowel-final-i twins (15 improved-tokens, holds 319).
- 595: kta a+nh Ng-twins (6 improved-tokens, holds 319).
- 596: ktavatu a+nD retention twins (12 improved-tokens, 320/492: PASS 10.0021).
- 597: tavya vowel-final-i AY-twins (6 improved-tokens, holds 320).
- 598: tavya short-i twins for I-final (3 improved-tokens, holds 320).
- 599: kta jYA jYAp-stem twins (3 improved-tokens, holds 320).
- 600: ktavatu jYAp-stem twins (3 improved-tokens, holds 320).
- 601: jYAp stem in 7 stem-lists (21 improved-tokens, holds 320).
- 602: jYAp present stem (304 improved-tokens, holds 320).
- 603: ktvA jYA union (1 improved-token, holds 320).
- 604: jYAp yak twins (36 improved-tokens, holds 320).
- 605: SAnac AY dedicated twins (9 improved-tokens, holds 320).
- 606: kta n→N velar twins (24 improved-tokens, holds 320).
- 607: ktavatu n→N velar twins (24 improved-tokens, holds 320).
- 608: kta plain meta-clean triple (6 improved-tokens, holds 320).
- 609: kta a+s plain+vriddhi twins (6 improved-tokens, holds 320).
- 610: generalized z-devoice (58 improved-tokens, 322/492: PASS 10.0038/0242).
- 611: N-grade stems batch (161 improved-tokens, holds 322).
- 612: lambda N-widening (1021 improved-tokens, holds 322).
- 613: san N-roots tavya+matrix (55 improved-tokens, holds 322).
- 614: z-grade machinery (315 improved-tokens, 323/492: PASS 10.0190).
- 615: ktavatu AY dedicated twins (9 improved-tokens, holds 323).
- 616: tfc AY dedicated twins (6 improved-tokens, holds 323).
- Gates: every commit fid-diff 0 worsened; guards green throughout.

## Next
1. Gana-10: yak + ting + yangluk-redup + luN-aorist (pull before each iteration — shared tree; PYTHONHASHSEED=0). Queued irregular: sad Asad-suppletion (Asanna/Asatta/AsIda), ci-cap extras. Failed hypotheses (no commit): (a) lyap pra+V sandhi twins — correct forms, zero gain (bare stems cover slots), reverted; (b) tavya bare e-grade twins (jretavya/metavya) — correct forms, zero gain, reverted (kept AY + short-i); (c) tumun/lyap jYAp twins — correct forms, zero gain, reverted; (d) san jYAp grade — correct form, zero gain (slot already hit), reverted.
2. Gana-04 ceiling audit (other session) → all-gana 100% modulo ceilings.
3. Cross-gana guards (01 + all-100% ganas) before every commit.
