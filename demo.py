"""Demo Runner: Tiṅanta, Kṛdanta (tri-liṅga) and Subanta (21 sup) showcase (SLP1)."""
from pypanini import TinantaDerivationEngine, KrdantaEngine
from pypanini.subanta import SubantaEngine

VIBHAKTI = {1: "prathamA", 2: "dvitIyA", 3: "tftIyA", 4: "caturTI",
            5: "paYcamI", 6: "zazWI", 7: "saptamI", 8: "sambodhana"}


def print_table(table, title):
    print(f"\n=== {title} ===")
    print(f"{'Puruṣa':<10} | {'Ekavacana':<22} | {'Dvivacana':<14} | {'Bahuvacana':<14}")
    print("-" * 68)
    for p in ["prathama", "madhyama", "uttama"]:
        print(f"{p:<10} | {table[(p, 'eka')]:<22} | "
              f"{table[(p, 'dvi')]:<14} | {table[(p, 'bahu')]:<14}")


def print_krdanta_gender_table(krd_dict, title):
    ke = KrdantaEngine()
    print(f"\n=== {title} ===")
    print(f"{'Affix':<8} | {'Description':<38} | {'Masculine':<14} | "
          f"{'Feminine':<16} | {'Neuter / Avyaya'}")
    print("-" * 95)
    for code, data in krd_dict.items():
        desc, kind = ke.krdanta_metadata[code]
        if kind == "participle" or (code == "Rvul" and "M" in data):
            m = data["M"]
            f = data["F"]
            n = data["N"]
            print(f"{code:<8} | {desc:<38} | {m:<14} | {f:<16} | {n}")
        elif kind == "avyaya":
            print(f"{code:<8} | {desc:<38} | {'-':<14} | {'-':<16} | {data['avyaya']}")
        else:
            g = data["gender"]
            form = data["form"]
            print(f"{code:<8} | {desc:<38} | {'-':<14} | {'-':<16} | {form} ({g})")


def print_subanta(stem, linga, title=None):
    e = SubantaEngine()
    d = e.decline(stem, linga)
    print(f"\n=== {title or (stem + ' (' + linga + ')')} ===")
    print(f"{'Vibhakti':<12} | {'eka':<16} | {'dvi':<16} | {'bahu'}")
    print("-" * 62)
    for v in range(1, 9):
        row = d.get((v, "eka"), []), d.get((v, "dvi"), []), d.get((v, "bahu"), [])
        fmt = lambda xs: "/".join(xs) if xs else "-"
        print(f"{VIBHAKTI[v]:<12} | {fmt(row[0]):<16} | {fmt(row[1]):<16} | {fmt(row[2])}")


def main():
    te = TinantaDerivationEngine()
    ke = KrdantaEngine()

    print("=" * 70)
    print("1. ALTERNATIVE TIṄANTA FORMS (VIKALPA / VIBHĀṢĀ)")
    print("=" * 70)
    print_table(te.derive_all("BU", "low"), "Imperative: 'low' with tātaṅ option (7.1.35)")
    print_table(te.derive_all("BU", "lw", sanadi="yanluganta"),
        "Yaṅluganta with Iq-Agama option (7.3.94)")

    print("\n" + "=" * 70)
    print("2. COMPLETE KṚDANTAS PER ANTA WITH FULL GENDERS (TRI-LIṄGA)")
    print("=" * 70)
    print_krdanta_gender_table(ke.derive_all_krdantas("BU"), "A. Primitive Kṛdantas: 'BU'")
    print_krdanta_gender_table(ke.derive_all_krdantas("BU", sanadi="sannanta"),
        "B. Sannanta overrides")

    print("\n" + "=" * 70)
    print("3. SUBANTA DECLENSION (21 sup, 8 vibhakti x 3 vacana, SLP1)")
    print("=" * 70)
    print_subanta("rAma", "puM", "a-stem masc: rAma")
    print_subanta("sItA", "strI", "A-stem fem: sItA")
    print_subanta("hari", "puM", "i-stem masc: hari (sambuddhi hare)")
    print_subanta("nadI", "strI", "I-stem fem NadI: nadI")
    print_subanta("vAri", "napuMsaka", "neuter i with num: vAri -> vAriRA/vArIRi")
    print_subanta("kartf", "puM", "f-stem agent: kartf -> kartAraH/kartrARAm")
    print_subanta("rAjan", "puM", "an-stem: rAjan -> rAjA/rAjYA (vs AtmanA heavy)")
    print_subanta("manas", "napuMsaka", "as-stem neut: manas -> manAMsi")
    print_subanta("vAc", "strI", "c-stem: vAc -> vAk/vAgBiH/vAkzu")
    print_subanta("go", "puM", "o-stem nipAtana: go -> gOH/gAm/gAH")
    print_subanta("tad", "puM", "pronoun: tad -> saH/te/tasmE (su-lopa external not shown)")
    print_subanta("asmad", "puM", "suppletion: asmad -> aham/maHyam/asmAkam")
    print_subanta("wramPa", "puM", "modern loan: wramPa Instr = wramPeRa (Natva 8.4.1-2)")
    print_subanta("gacCat", "puM", "Satf participle masc: gacCat -> gacCan")
    print_subanta("cakfvas", "puM", "kvasu participle: cakfvas -> cakfvAn/cakfuzaH")
    print_subanta("kftavat", "puM", "ktavatu participle: kftavat -> kftavAn")
    print_subanta("Bavat", "puM", "respect pronoun (3rd-person noun): Bavat -> BavAn")


def print_search(word):
    from pypanini.search import analyze
    print(f"\n=== search: {word} ===")
    for g in analyze(word, limit=6):
        if g["kind"] == "subanta":
            _r = "; ".join(f"{r['linga']}/{r['vibhakti']}/{r['vacana']}"
                           for r in g["readings"][:4])
            print(f"  subanta  stem={g['stem']} [{_r}] conf={g['confidence']}")
        elif g["kind"] == "krdanta":
            _r = "; ".join(f"{r['pratyaya']}/{r['stem']}"
                           for r in g["readings"][:4])
            print(f"  krdanta  dhatu={g.get('dhatu')} [{_r}] "
                  f"conf={g['confidence']}")
        else:
            _r = "; ".join(f"{r['lakara']}/{r['purusha']}/{r['vacana']}"
                           for r in g["readings"][:4])
            print(f"  tinanta  dhatu={g.get('dhatu')} [{_r}] "
                  f"conf={g['confidence']}")


def main_search_demo():
    print("\n" + "=" * 70)
    print("4. SEARCH (subanta / krdanta / tinanta / global)")
    print("=" * 70)
    for w in ["wrampeRa", "wramPa", "rAmaH", "Bavati", "kftaH", "kartavyaH"]:
        print_search(w)


if __name__ == "__main__":
    main()
    main_search_demo()
