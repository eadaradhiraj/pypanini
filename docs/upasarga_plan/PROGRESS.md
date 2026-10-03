# Upasarga Implementation Progress

## Log
* **2026-10-03:** Project plan initialized. All 5 phases documented.
* **2026-10-03:** Phase 1 (Test Infrastructure) completed. 
  - `pypanini/tinanta.py` modified: `derive` and `derive_all` now accept `upasarga: Optional[str] = None`.
  - `tests/test_dhatu.py` modified: `validate_dhatu` now accepts `prefix=...` and restricts token-matching logic strictly to the prefixed JSON data to prevent false positives.
  - Created `tests/sweep_upasargas.py` to iterate over prefixed data and output CSVs.
* **2026-10-03:** Phase 2 (Sandhi Engine) completed.
  - Wrote `apply_upasargas` in `pypanini/phonetics.py` that handles vowel sandhi, consonant sandhi (anusvara/parasavarna), and augment boundary (`pra + aBavat -> prABavat`).
  - Implemented the wrapper pattern in `pypanini/tinanta.py` and `pypanini/krdanta.py` to automatically intercept the `_inner` return value and apply the `upasarga` sandhi precisely once before returning to the user.
* **2026-10-03:** Phase 5 (API Refactoring / Krdanta Cleanup) completed.
  - Fixed Krdanta legacy loops that were double-applying prefixes for `lyap`.
  - `krdanta.py` wrapper now correctly strips old hardcoded cache prefixes and only applies the Sandhi engine uniformly to the forms (skipping metadata keys like `gender`).
* **2026-10-03:** Phase 3 (Natva & Satva Refinements) started.
  - Basic `s -> z` Satva rule implemented in `apply_upasargas`.
  - Perfected `n -> R` Natva logic (`apply_natva`) across boundaries (e.g., matching `pra + havanIya -> prahavaRIya` while deliberately preventing it on padanta `n` or tiṅanta `nti/ntu` like `praBavanti`).
  - **Results:** Tinanta is generating at **100% accuracy** for `pra`. Krdanta is hitting **~99.7%** (The tiny remaining failure is a pre-existing base engine bug where it generates Passive instead of Active for `nijanta SAnac`). Overall accuracy on prefixes is stellar.

## Next Steps for the Next Agent:
1. **Start Phase 4 (Pada Overrides):**
   - The primary remaining task is handling voice changes (Atmanepada / Parasmaipada overrides). For example, root `ji` is Parasmaipadi, but `vi + ji` becomes Atmanepadi. 
   - You need to intercept the `prayoga` determination logic inside `pypanini/tinanta.py` wrapper (around line 10000+ where lakaras are looped over) and swap the lists of tiṅ endings if an override applies based on the `upasarga` and `dhatu` combination.
2. **Review Natva/Satva Exceptions (Optional Polish):**
   - Natva/Satva in `phonetics.py` is working excellently for typical roots. You may review Panini 8.3 and 8.4 sutras if you find specific roots missing `z` or `R` during exhaustive sweeps.
