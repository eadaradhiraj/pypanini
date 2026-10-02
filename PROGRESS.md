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

## Done — this session (06) + 460-472 (10)
- 06: iterations 383-398, 442-458 → 173/174 modulo 06.0159 ceiling (see STATS.md).
- 460: verify pull 7738ab6 + fresh sweeps (csv refresh).
- 461: curAdi general aya-twins ktvA/tumun (293 improved, +99 pass-ups).
- 462: curAdi lyap/lyuw aya-twins (124 improved, +63 pass-ups).
- 463: curAdi liw aya-periphrastic paras table (57 improved, holds 312).
- 464: curAdi san aya-redup stems (20 improved, +1 pass-up).
- 465: curAdi san-yak twins (30 improved, +3 pass-ups).
- 466: curAdi san-kta grade extensions (30 improved, holds 316).
- 467: vowel-initial san + aya-less grades (6 improved, holds 316).
- 468: shared _curAdi_sanV_secs helper (zero-diff) + san-ktavatu V-secs (9 improved, holds 316).
- 469: san-Satf V-secs via helper (9 improved, holds 316).
- 470: san-tavya V-secs via helper (15 improved, 318/492: PASS 10.0014/0105).
- 471: san-SAnac V-secs via helper (9 improved, holds 318).
- 472: san-matrix V-secs via helper (51 improved-tokens, V-san probe 0, holds 318).
- Gates: every commit fid-diff 0 worsened; guards green throughout.

## Next
1. Gana-10: san-lyap pra+u sandhi (prorjijayizya) + yak + ting (pull before each iteration — shared tree; PYTHONHASHSEED=0).
2. Gana-04 ceiling audit (other session) → all-gana 100% modulo ceilings.
3. Cross-gana guards (01 + all-100% ganas) before every commit.
