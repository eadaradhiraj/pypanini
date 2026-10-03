# Phase 1: Test Infrastructure

## Goal
Establish a baseline for testing prefixed forms before writing engine logic.

## Tasks
1. **Update `tests/test_dhatu.py`:** 
   - Currently, the test script extracts `"conjugations"` and `"participles"` from the root level of the JSON.
   - Modify it to also iterate over the keys in `"upasarga_forms"` (if it exists).
   - For each prefix key (e.g., `"pra"`, `"sam;ud"`), parse it into a list of prefixes (e.g., `["sam", "ud"]`).
2. **Generate Sweep Files:**
   - Run the modified test script and output to new CSV sweep files (e.g., `tests/sweep_prefixed_01.csv`, `tests/sweep_prefixed_all.csv`).
   - Initially, accuracy will be very low since the engine ignores prefixes. This establishes a test-driven baseline.
