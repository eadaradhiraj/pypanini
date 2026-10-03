# Phase 2: External Sandhi Engine (Saṃhitā)

## Goal
Fusing the prefix to the derived word.

## Tasks
Create a new function in `pypanini/phonetics.py` (e.g., `apply_upasarga_sandhi(prefixes: List[str], form: str, has_augment: bool) -> str`).

### 1. The `aṬ` Augment Trap
For past tenses (laṅ, luṅ, lṛṅ), the augment `a` or `ā` is inserted **between** the prefix and the root.
- **Example:** `pra + (a + bhavat)` $\rightarrow$ `prābhavat` (not `pra-aBavat`).
- **Implementation:** The engine must know if the derived word starts with the `aṬ` augment to apply the correct sandhi at that boundary.

### 2. Vowel Sandhi (Ac Sandhi)
- **Savarṇa-dīrgha:** `a + a = ā`, `i + i = ī` (e.g., `api + i = apī`).
- **Guṇa:** `a + i = e`, `a + u = o` (e.g., `upa + i = upe`).
- **Vṛddhi:** `a + e = ai`, `a + o = au`. 
  - *Exception 1:* `pra + eti` $\rightarrow$ `preti` (eṅi pararūpam).
  - *Exception 2:* `pra + ṛcchati` $\rightarrow$ `prārcchati` (upasargād ṛti dhātau).
- **Yaṇ:** `i/u + vowel = y/v` (e.g., `vi + eti` $\rightarrow$ `vyeti`).

### 3. Consonant Sandhi (Hal Sandhi)
- **Anusvāra / Parasavarṇa:** `sam + gam` $\rightarrow$ `saṅgam`, `sam + car` $\rightarrow$ `sañcar`.
