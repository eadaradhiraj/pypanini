# Phase 5: API Refactoring

## Goal
Expose the prefix support cleanly through the engine's public API.

## Tasks
1. **Update Signatures:** 
   Modify `TinantaDerivationEngine.derive()` and `KrdantaDerivationEngine.derive_krdanta()` to formally accept an `upasargas: List[str] = None` argument.

2. **Clean up Kṛdanta Hacks:**
   - In `pypanini/krdanta.py`, the `lyap` derivations currently have hardcoded test hacks (e.g., prepending `"pra"` or `"saM"` explicitly because `lyap` replaces `ktvā` in the presence of a compound/prefix).
   - Refactor this: `lyap` should correctly and naturally be selected when `upasargas` is non-empty, and the prefix sandhi engine (from Phase 2) should handle attaching the prefix to the `lyap` base, rather than generating random permutations to trick the test script.

3. **Final Validation:**
   - Run the updated test suite (from Phase 1) across all 10 gaṇas.
   - Achieve 100% on `sweep_prefixed_all.csv`.
