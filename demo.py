"""Demo Runner: Displaying the Complete Matrix of Sanādyanta & Prayoga"""
from pypanini import TinantaDerivationEngine

def print_table(table, title):
    print(f"\n=== {title} ===")
    print(f"{'Puruṣa':<10} | {'Ekavacana':<14} | {'Dvivacana':<14} | {'Bahuvacana':<14}")
    print("-" * 58)
    for p in ["prathama", "madhyama", "uttama"]:
        print(f"{p:<10} | {table[(p, 'eka')]:<14} | {table[(p, 'dvi')]:<14} | {table[(p, 'bahu')]:<14}")

def main():
    engine = TinantaDerivationEngine()

    print("=" * 65)
    print("THE COMPLETE SANĀDYANTA & PRAYOGA MATRIX FOR 'BU' (in 'lw')")
    print("=" * 65)

    # 1. Primitive: Kartari vs Karmani
    print_table(engine.derive_all("BU", "lw", prayoga="kartari"), "1A. Primitive Kartari: 'Bavati' (भवति)")
    print_table(engine.derive_all("BU", "lw", prayoga="karmani"), "1B. Primitive Karmaṇi: 'BUyate' (भूयते)")

    # 2. Ṇijanta: Kartari vs Karmani
    print_table(engine.derive_all("BU", "lw", prayoga="kartari", sanadi="nijanta"), "2A. Ṇijanta Kartari: 'BAvayati' (भावयति)")
    print_table(engine.derive_all("BU", "lw", prayoga="karmani", sanadi="nijanta"), "2B. Ṇijanta Karmaṇi: 'BAvyate' (भाव्यते)")

    # 3. Sannanta: Kartari vs Karmani
    print_table(engine.derive_all("BU", "lw", prayoga="kartari", sanadi="sannanta"), "3A. Sannanta Kartari: 'buBUzati' (बुभूषति)")
    print_table(engine.derive_all("BU", "lw", prayoga="karmani", sanadi="sannanta"), "3B. Sannanta Karmaṇi: 'buBUzyate' (बुभूष्यते)")

    # 4. Yaṅanta (Intensive Ātmanepada)
    print_table(engine.derive_all("BU", "lw", sanadi="yananta"), "4. Yaṅanta: 'boBUyate' (बोभूयते)")

    # 5. Yaṅluganta (Intensive Parasmaipada)
    print_table(engine.derive_all("BU", "lw", sanadi="yanluganta"), "5. Yaṅluganta: 'boBavIti / boBoti' (बोभवीति/बोभोति)")

if __name__ == "__main__":
    main()
