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
    
    print_table(engine.derive_all("BU", "lw"), "1. Present: 'lw' (भवति)")
    print_table(engine.derive_all("BU", "lfw"), "2. Simple Future: 'lfw' (भविष्यति)")
    print_table(engine.derive_all("BU", "laN"), "3. Past: 'laN' (अभवत्)")
    print_table(engine.derive_all("BU", "low"), "4. Imperative: 'low' (भवतु)")
    print_table(engine.derive_all("BU", "viDiliN"), "5. Optative: 'viDiliN' (भवेत्)")
    print_table(engine.derive_all("BU", "lfN"), "6. Conditional: 'lfN' (अभविष्यत्)")

if __name__ == "__main__":
    main()
