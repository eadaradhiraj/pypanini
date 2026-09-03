"""Demo Runner: Displaying Alternative Tiṅantas and Full-Gender Kṛdantas"""
from pypanini import TinantaDerivationEngine, KrdantaEngine

def print_table(table, title):
    print(f"\n=== {title} ===")
    print(f"{'Puruṣa':<10} | {'Ekavacana':<22} | {'Dvivacana':<14} | {'Bahuvacana':<14}")
    print("-" * 68)
    for p in ["prathama", "madhyama", "uttama"]:
        print(f"{p:<10} | {table[(p, 'eka')]:<22} | {table[(p, 'dvi')]:<14} | {table[(p, 'bahu')]:<14}")

def print_krdanta_gender_table(krd_dict, title):
    ke = KrdantaEngine()
    print(f"\n=== {title} ===")
    print(f"{'Affix':<8} | {'Description':<38} | {'Masculine (पुं)':<14} | {'Feminine (स्त्री)':<16} | {'Neuter / Avyaya'}")
    print("-" * 95)
    for code, data in krd_dict.items():
        desc, kind = ke.krdanta_metadata[code]
        if kind == "participle" or (code == "Rvul" and "M" in data):
            m = data["M"]
            f = data["F"]
            n = data["N"]
            print(f"{code:<8} | {desc:<38} | {m:<14} | {f:<16} | {n}")
        elif kind == "avyaya":
            print(f"{code:<8} | {desc:<38} | {'-':<14} | {'-':<16} | {data['avyaya']} (अव्यय)")
        else:
            g = data["gender"]
            form = data["form"]
            print(f"{code:<8} | {desc:<38} | {'-':<14} | {'-':<16} | {form} ({g})")

def main():
    te = TinantaDerivationEngine()
    ke = KrdantaEngine()

    print("=" * 70)
    print("1. ALTERNATIVE TIṄANTA FORMS (VIKALPA / VIBHĀṢĀ)")
    print("=" * 70)
    print_table(te.derive_all("BU", "low"), "Imperative: 'low' with tātaṅ option (7.1.35)")
    print_table(te.derive_all("BU", "lw", sanadi="yanluganta"), "Yaṅluganta with Iq-Agama option (7.3.94)")

    print("\n" + "=" * 70)
    print("2. COMPLETE KṚDANTAS PER ANTA WITH FULL GENDERS (TRI-LIṄGA)")
    print("=" * 70)
    print_krdanta_gender_table(ke.derive_all_krdantas("BU"), "A. Primitive Kṛdantas: 'BU' (भू)")
    print_krdanta_gender_table(ke.derive_all_krdantas("BU", sanadi="sannanta"), "B. Sannanta with Pāṇinian Overrides (बुभूषु & बुभूषा)")

if __name__ == "__main__":
    main()
