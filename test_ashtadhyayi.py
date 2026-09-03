"""
Exhaustive Validation Test against scraped ashtadhyayi.com data:
Tests ALL Lakāras, ALL Antas, ALL Voices, and ALL Genders.
File: /home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0001.json
"""
import json
from pathlib import Path
from pypanini import TinantaDerivationEngine, KrdantaEngine, slp1_to_devanagari, devanagari_to_slp1

JSON_PATH = Path("/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0001.json")


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


def check_form(form_slp, dev_tokens, slp_tokens):
    dev_form = slp1_to_devanagari(form_slp)
    found = (dev_form in dev_tokens) or (form_slp in slp_tokens)
    return found, dev_form


def run_tinanta_suite(te, dev_tokens, slp_tokens, dhatu, lakara, title, prayoga="kartari", sanadi=None):
    total = 0
    matched = 0
    missing = []
    purushas = ["prathama", "madhyama", "uttama"]
    vacanas = ["eka", "dvi", "bahu"]

    for p in purushas:
        for v in vacanas:
            forms, _ = te.derive(dhatu, lakara, p, v, prayoga=prayoga, sanadi=sanadi)
            for form in forms:
                total += 1
                found, dev_form = check_form(form, dev_tokens, slp_tokens)
                if found:
                    matched += 1
                else:
                    missing.append((f"{p} {v}", form, dev_form))

    status = "✓ ALL MATCHED" if matched == total else f"⚠ {matched}/{total} matched"
    print(f"  • {title:<45} : {matched:2d}/{total:2d} -> {status}")
    if missing and len(missing) <= 3:
        for pos, slp, dev in missing:
            print(f"      [Missing in JSON: {pos} -> {slp} ({dev})]")
    return matched, total


def run_krdanta_suite(ke, dev_tokens, slp_tokens, sanadi, title):
    total = 0
    matched = 0
    missing = []
    all_krd = ke.derive_all_krdantas("BU", sanadi=sanadi)

    for code, item in all_krd.items():
        if "M" in item:
            # Test all 3 genders
            for g, form in [("M", item["M"]), ("F", item["F"]), ("N", item["N"])]:
                total += 1
                found, dev_form = check_form(form, dev_tokens, slp_tokens)
                if found:
                    matched += 1
                else:
                    missing.append((f"{code} ({g})", form, dev_form))
        elif "avyaya" in item:
            # avyaya may be list of variants (e.g., lyap with/without prefix)
            av = item["avyaya"]
            candidates = av if isinstance(av, list) else [av]
            total += 1
            found_any = False
            dev_form_first = ""
            for form in candidates:
                found, dev_form = check_form(form, dev_tokens, slp_tokens)
                dev_form_first = dev_form
                if found:
                    found_any = True
                    break
            if found_any:
                matched += 1
            else:
                missing.append((f"{code} (Avyaya)", candidates[0], dev_form_first))
        else:
            total += 1
            form = item["form"]
            found, dev_form = check_form(form, dev_tokens, slp_tokens)
            if found:
                matched += 1
            else:
                missing.append((f"{code} ({item['gender']})", form, dev_form))

    status = "✓ ALL MATCHED" if matched == total else f"⚠ {matched}/{total} matched"
    print(f"  • {title:<45} : {matched:2d}/{total:2d} -> {status}")
    if missing and len(missing) <= 4:
        for tag, slp, dev in missing:
            print(f"      [Missing in JSON: {tag} -> {slp} ({dev})]")
    return matched, total


def main():
    print("=" * 75)
    print("EXHAUSTIVE TEST AGAINST ASHTADHYAYI.COM SCRAPED DATA")
    print(f"File: {JSON_PATH}")
    print("=" * 75)

    if not JSON_PATH.exists():
        print(f"\n❌ File not found at: {JSON_PATH}")
        return

    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    scraped_dev_tokens = extract_all_text_tokens(data)
    scraped_slp1_tokens = {devanagari_to_slp1(t) for t in scraped_dev_tokens}

    print(f"✓ Total unique tokens loaded from ashtadhyayi JSON: {len(scraped_dev_tokens)}\n")

    te = TinantaDerivationEngine()
    ke = KrdantaEngine()

    grand_total = 0
    grand_matched = 0

    # -------------------------------------------------------------------------
    # PART 1: PRIMITIVE TIṄANTA (Kartari & Karmaṇi)
    # -------------------------------------------------------------------------
    print("SECTION 1: PRIMITIVE ROOT 'BU' (MŪLA)")
    print("-" * 75)
    # 10 Lakāras Kartari
    for lak, name in [
        ("lw", "Kartari Present (लट्)"),
        ("liw", "Kartari Perfect (लिट्)"),
        ("luw", "Kartari First Future (लुट्)"),
        ("lfw", "Kartari Simple Future (लृट्)"),
        ("low", "Kartari Imperative with tātaṅ (लोट्)"),
        ("laN", "Kartari Imperfect Past (लङ्)"),
        ("viDiliN", "Kartari Optative (विधिलिङ्)"),
        ("ASIrliN", "Kartari Benedictive (आशीर्लिङ्)"),
        ("luN", "Kartari Aorist Past (लुङ्)"),
        ("lfN", "Kartari Conditional (लृङ्)"),
    ]:
        m, t = run_tinanta_suite(te, scraped_dev_tokens, scraped_slp1_tokens, "BU", lak, name)
        grand_matched += m
        grand_total += t

    # 4 Lakāras Karmaṇi
    for lak, name in [
        ("lw", "Karmaṇi Present (भूयते - लट्)"),
        ("laN", "Karmaṇi Past (अभूयत - लङ्)"),
        ("low", "Karmaṇi Imperative (भूयताम् - लोट्)"),
        ("viDiliN", "Karmaṇi Optative (भूयेत - विधिलिङ्)"),
    ]:
        m, t = run_tinanta_suite(te, scraped_dev_tokens, scraped_slp1_tokens, "BU", lak, name, prayoga="karmani")
        grand_matched += m
        grand_total += t

    # -------------------------------------------------------------------------
    # PART 2: SECONDARY ROOTS (Sanādyanta Tiṅanta)
    # -------------------------------------------------------------------------
    print("\nSECTION 2: SECONDARY ROOTS (SANĀDYANTA TIṄANTA)")
    print("-" * 75)

    # Ṇijanta
    m, t = run_tinanta_suite(te, scraped_dev_tokens, scraped_slp1_tokens, "BU", "lw", "Ṇijanta Kartari Present (भावयति - लट्)", sanadi="nijanta")
    grand_matched += m; grand_total += t
    m, t = run_tinanta_suite(te, scraped_dev_tokens, scraped_slp1_tokens, "BU", "laN", "Ṇijanta Kartari Past (अभावयत् - लङ्)", sanadi="nijanta")
    grand_matched += m; grand_total += t
    m, t = run_tinanta_suite(te, scraped_dev_tokens, scraped_slp1_tokens, "BU", "lfw", "Ṇijanta Kartari Future (भावयिष्यति - लृट्)", sanadi="nijanta")
    grand_matched += m; grand_total += t
    m, t = run_tinanta_suite(te, scraped_dev_tokens, scraped_slp1_tokens, "BU", "lw", "Ṇijanta Karmaṇi Present (भाव्यते - लट्)", prayoga="karmani", sanadi="nijanta")
    grand_matched += m; grand_total += t

    # Sannanta
    m, t = run_tinanta_suite(te, scraped_dev_tokens, scraped_slp1_tokens, "BU", "lw", "Sannanta Kartari Present (बुभूषति - लट्)", sanadi="sannanta")
    grand_matched += m; grand_total += t
    m, t = run_tinanta_suite(te, scraped_dev_tokens, scraped_slp1_tokens, "BU", "laN", "Sannanta Kartari Past (अबुभूषत् - लङ्)", sanadi="sannanta")
    grand_matched += m; grand_total += t
    m, t = run_tinanta_suite(te, scraped_dev_tokens, scraped_slp1_tokens, "BU", "lfw", "Sannanta Kartari Future (बुभूषिष्यति - लृट्)", sanadi="sannanta")
    grand_matched += m; grand_total += t
    m, t = run_tinanta_suite(te, scraped_dev_tokens, scraped_slp1_tokens, "BU", "lw", "Sannanta Karmaṇi Present (बुभूष्यते - लट्)", prayoga="karmani", sanadi="sannanta")
    grand_matched += m; grand_total += t

    # Yaṅanta
    m, t = run_tinanta_suite(te, scraped_dev_tokens, scraped_slp1_tokens, "BU", "lw", "Yaṅanta Present (बोभूयते - लट्)", sanadi="yananta")
    grand_matched += m; grand_total += t

    # Yaṅluganta
    m, t = run_tinanta_suite(te, scraped_dev_tokens, scraped_slp1_tokens, "BU", "lw", "Yaṅluganta Present (बोभवीति/बोभोति - लट्)", sanadi="yanluganta")
    grand_matched += m; grand_total += t

    # -------------------------------------------------------------------------
    # PART 3: KṚDANTA ACROSS ALL ANTAS & GENDERS (Tri-liṅga)
    # -------------------------------------------------------------------------
    print("\nSECTION 3: KṚDANTA ENGINE (ALL ANTAS ACROSS GENDERS)")
    print("-" * 75)
    m, t = run_krdanta_suite(ke, scraped_dev_tokens, scraped_slp1_tokens, None, "1. Primitive Kṛdantas (Mūla: भू)")
    grand_matched += m; grand_total += t

    m, t = run_krdanta_suite(ke, scraped_dev_tokens, scraped_slp1_tokens, "nijanta", "2. Ṇijanta Kṛdantas (भावि)")
    grand_matched += m; grand_total += t

    m, t = run_krdanta_suite(ke, scraped_dev_tokens, scraped_slp1_tokens, "sannanta", "3. Sannanta Kṛdantas (बुभूष)")
    grand_matched += m; grand_total += t

    m, t = run_krdanta_suite(ke, scraped_dev_tokens, scraped_slp1_tokens, "yananta", "4. Yaṅanta Kṛdantas (बोभूय)")
    grand_matched += m; grand_total += t

    # -------------------------------------------------------------------------
    # FINAL SUMMARY
    # -------------------------------------------------------------------------
    print("\n" + "=" * 75)
    print(f"GRAND TOTAL MATCHED: {grand_matched} / {grand_total} forms ({(grand_matched/grand_total)*100:.1f}%)")
    print("=" * 75)


if __name__ == "__main__":
    main()
