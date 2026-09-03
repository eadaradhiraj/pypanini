"""Demo Runner for PyPanini"""
from pypanini import TinantaDerivationEngine

def print_table(table, title):
    print(f"\n=== {title} ===")
    print(f"{'Puruṣa':<10} | {'Ekavacana':<12} | {'Dvivacana':<12} | {'Bahuvacana':<12}")
    print("-" * 52)
    for p in ["prathama", "madhyama", "uttama"]:
        print(f"{p:<10} | {table[(p, 'eka')]:<12} | {table[(p, 'dvi')]:<12} | {table[(p, 'bahu')]:<12}")

def main():
    engine = TinantaDerivationEngine()
    
    # 1. Present (lw)
    print_table(engine.derive_all("BU", "lw"), "1. Present: 'lw' (भवति)")

    # 2. Past (laN)
    print_table(engine.derive_all("BU", "laN"), "2. Past: 'laN' (अभवत्)")

    # 3. Imperative (low)
    print_table(engine.derive_all("BU", "low"), "3. Imperative: 'low' (भवतु)")

if __name__ == "__main__":
    main()
