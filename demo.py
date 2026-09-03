"""Demo Runner: Displaying Sannanta, Nijanta, and Karmani across multiple tenses"""
from pypanini import TinantaDerivationEngine

def print_table(table, title):
    print(f"\n=== {title} ===")
    print(f"{'Puruṣa':<10} | {'Ekavacana':<12} | {'Dvivacana':<12} | {'Bahuvacana':<12}")
    print("-" * 52)
    for p in ["prathama", "madhyama", "uttama"]:
        print(f"{p:<10} | {table[(p, 'eka')]:<12} | {table[(p, 'dvi')]:<12} | {table[(p, 'bahu')]:<12}")

def main():
    engine = TinantaDerivationEngine()

    print("=" * 60)
    print("1. SANNANTA (DESIDERATIVE: BU + san -> buBUza 'desires to be')")
    print("=" * 60)
    print_table(engine.derive_all("BU", "lw", sanadi="sannanta"), "Sannanta Present: 'lw' (बुभूषति)")
    print_table(engine.derive_all("BU", "laN", sanadi="sannanta"), "Sannanta Past: 'laN' (अबुभूषत्)")
    print_table(engine.derive_all("BU", "lfw", sanadi="sannanta"), "Sannanta Future: 'lfw' (बुभूषिष्यति)")

    print("\n" + "=" * 60)
    print("2. ṆIJANTA (CAUSATIVE: BU + Ric -> BAvaya 'causes to be')")
    print("=" * 60)
    print_table(engine.derive_all("BU", "lw", sanadi="nijanta"), "Ṇijanta Present: 'lw' (भावयति)")
    print_table(engine.derive_all("BU", "laN", sanadi="nijanta"), "Ṇijanta Past: 'laN' (अभावयत्)")
    print_table(engine.derive_all("BU", "lfw", sanadi="nijanta"), "Ṇijanta Future: 'lfw' (भावयिष्यति)")

    print("\n" + "=" * 60)
    print("3. KARMAṆI PRAYOGA (PASSIVE VOICE: BU + yak -> BUya 'is become')")
    print("=" * 60)
    print_table(engine.derive_all("BU", "lw", prayoga="karmani"), "Karmaṇi Present: 'lw' (भूयते)")
    print_table(engine.derive_all("BU", "laN", prayoga="karmani"), "Karmaṇi Past: 'laN' (अभूयत)")
    print_table(engine.derive_all("BU", "low", prayoga="karmani"), "Karmaṇi Imperative: 'low' (भूयताम्)")
    print_table(engine.derive_all("BU", "viDiliN", prayoga="karmani"), "Karmaṇi Optative: 'viDiliN' (भूयेत)")

if __name__ == "__main__":
    main()
