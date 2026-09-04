# Progress — Done / Next (overwritten each iteration, not appended)

Date: 2026-09-04T19:30:00Z
Sweep: 248/1166 100% (see `tests/STATS.md` + `tests/sweep_all.csv`)

## Done (this iteration)
- `yat` → `Ryat` vriddhi unless `I~` (`Kada~→KAdya` long, `yatI~→yatya` short, `3.1.124`).
  - Fixes `krut/yat + yangluk_krut/yat` 99.3% batch: `01.0052/0095/0128/0138/0179/0190/0192` etc. now `100%`.
  - No per-dhatu hardcoding (general `a/A→vriddhi` unless `I~` in `krdanta.py:yat`).
- Re-swept `--all --workers 8`: `247 → 248/1166`. Pilots `01.0001-01.0003` OK.
- `tests/STATS.md` rebuilt compact (248 table), `tests/sweep_all.csv` updated.

## Next
1. `nich/luN prathama eka` (`akAbayizwa`, 99.9%, 1 miss each: `01.0440` etc.) — same `e→i` aorist-base pattern as `tej→tij` (extend `_nijanta_aorist` if needed).
2. `san_krut/Satf` (`ciKAdezan`, 99.7%, 3 misses each) — sannanta `Satf` sec+iT+guna (same `sec` vs `guna` pattern as `Satf` fix).
3. Re-sweep `--all`, rebuild compact `STATS.md`, commit & push.
- Rule: fix generally via sutra, never `if clean=="x"`.
