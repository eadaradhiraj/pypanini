"""
Validation Test for 01.0002: eD (एध् वृद्धौ - आत्मनेपदी)
File: /home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0002.json
"""
import json
from pathlib import Path
from pypanini import TinantaDerivationEngine, KrdantaEngine, slp1_to_devanagari, devanagari_to_slp1

PATH_POSSIBLE = [
    Path("/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0002.json"),
    Path("/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.002.json"),
]
JSON_PATH = next((p for p in PATH_POSSIBLE if p.exists()), PATH_POSSIBLE[0])


def extract_all_text_tokens(obj):
    tokens = set()
    if isinstance(obj, str):
        cleaned = obj.strip().strip("।,;-\n\t")
        if cleaned:
            tokens.add(cleaned)
            tokens.add(cleaned.replace("।", "").strip())
    elif isinstance(obj, list):
        for item in obj:
            tokens.update(extract_all_text_tokens(item))
    elif isinstance(obj, dict):
        for k, v in obj.items():
            tokens.update(extract_all_text_tokens(v))
    return tokens


def check_slot(forms_slp, all_tokens):
    for f in forms_slp:
        dev_f = slp1_to_devanagari(f)
        if (f in all_tokens) or (dev_f in all_tokens):
            return True, f, dev_f
    return False, forms_slp[0], slp1_to_devanagari(forms_slp[0])


def main():
    print("=" * 75)
    print("VALIDATION TEST FOR 01.0002: eD (एध् वृद्धौ - भ्वादिः, आत्मनेपदी)")
    print(f"File: {JSON_PATH}")
    print("=" * 75)

    if not JSON_PATH.exists():
        print(f"\n❌ File not found at: {JSON_PATH}")
        return

    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    raw_tokens = extract_all_text_tokens(data)
    all_tokens = set(raw_tokens)
    for t in raw_tokens:
        all_tokens.add(devanagari_to_slp1(t))
        all_tokens.add(slp1_to_devanagari(t))

    print(f"✓ Total unique search tokens: {len(all_tokens)}\n")

    te = TinantaDerivationEngine()
    ke = KrdantaEngine()

    total_all = 0
    matched_all = 0

    lakaras = [
        ("lw", "1. Present: 'lw' (एधते)"),
        ("liw", "2. Perfect: 'liw' (एधाञ्चक्रे)"),
        ("luw", "3. First Future: 'luw' (एधिता)"),
        ("lfw", "4. Simple Future: 'lfw' (एधिष्यते)"),
        ("low", "5. Imperative: 'low' (एधताम्)"),
        ("laN", "6. Imperfect: 'laN' (ऐधत - Aw-Agama)"),
        ("viDiliN", "7. Optative: 'viDiliN' (एधेत)"),
        ("ASIrliN", "8. Benedictive: 'ASIrliN' (एधिषीष्ट)"),
        ("luN", "9. Aorist: 'luN' (ऐधिष्ट)"),
        ("lfN", "10. Conditional: 'lfN' (ऐधिष्यत)"),
    ]

    print("SECTION 1: ALL 10 LAKĀRAS (ĀTMANEPADA)")
    print("-" * 75)
    for code, title in lakaras:
        tot, mat = 0, 0
        missing = []
        for p in ["prathama", "madhyama", "uttama"]:
            for v in ["eka", "dvi", "bahu"]:
                tot += 1
                forms, _ = te.derive("eD", code, p, v)
                found, matched_slp, dev = check_slot(forms, all_tokens)
                if found:
                    mat += 1
                else:
                    missing.append((f"{p} {v}", matched_slp, dev))

        matched_all += mat
        total_all += tot
        status = "✓ ALL MATCHED" if mat == tot else f"⚠ {mat}/{tot} matched"
        print(f"  • {title:<48} : {mat:2d}/{tot:2d} -> {status}")
        if missing and len(missing) <= 3:
            for pos, slp, dev in missing:
                print(f"      [Missing: {pos} -> {slp} ({dev})]")

    print("\nSECTION 2: KṚDANTAS FOR 'eD'")
    print("-" * 75)
    krd_tot, krd_mat = 0, 0
    krd_res = ke.derive_all_krdantas("eD")
    for code, item in krd_res.items():
        if "M" in item:
            for g in ["M", "F", "N"]:
                krd_tot += 1
                found, _, _ = check_slot([item[g]], all_tokens)
                if found: krd_mat += 1
        elif "avyaya" in item:
            krd_tot += 1
            candidates = item["avyaya"] if isinstance(item["avyaya"], list) else [item["avyaya"]]
            found, _, _ = check_slot(candidates, all_tokens)
            if found: krd_mat += 1
        else:
            krd_tot += 1
            found, _, _ = check_slot([item["form"]], all_tokens)
            if found: krd_mat += 1

    matched_all += krd_mat
    total_all += krd_tot
    status_krd = "✓ ALL MATCHED" if krd_mat == krd_tot else f"⚠ {krd_mat}/{krd_tot} matched"
    print(f"  • Kṛdantas (Participles & Verbal Nouns)        : {krd_mat:2d}/{krd_tot:2d} -> {status_krd}")

    print("\n" + "=" * 75)
    print(f"GRAND TOTAL MATCHED: {matched_all} / {total_all} forms ({(matched_all/total_all)*100:.1f}%)")
    print("=" * 75)


if __name__ == "__main__":
    main()
