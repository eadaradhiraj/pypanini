"""Full JSON -> search recall audit (grouped output).

Every unique single-word token from conjugations + participles +
upasarga_forms.conjugations/participles, across all 2259 JSONs, is run
through analyze() (no limit). Pass = the JSON provenance appears in the
matching per-dhatu group's readings list:

  tinanta: fid in ids (or dhatu string match) + lakara + (purusha, vacana)
           in expected slot set + upasarga match
  krdanta: fid in ids (or dhatu match) + pratyaya match + upasarga match

Provenance slots come from engine alignment (derive per slot, intersect
with the JSON key list) with a positional fallback for engine-uncovered
items (flagged src=json-only).

Usage:
  python tests/audit_search_full.py --gana 01
  python tests/audit_search_full.py --fid 01.0001
  python tests/audit_search_full.py --gana 01 --fid-list 01.0001,01.0002
  python tests/audit_search_full.py --all --jobs 8 --out tests/audit_search_all.csv
"""
import argparse
import csv
import glob
import json
import os
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

DATA_ROOT = Path(os.getenv("SKT_MORPH_DATA",
                           "/home/edhiraj/Documents/projs/skt-morph-data/data"))
if not DATA_ROOT.exists():
    alt = ROOT / "skt-morph-data"
    if alt.exists():
        DATA_ROOT = alt

ANTA_MAP = {
    "ting": (None, "kartari"),
    "yak": (None, "karmani"),
    "san": ("sannanta", "kartari"),
    "san_yak": ("sannanta", "karmani"),
    "nich": ("nijanta", "kartari"),
    "nich_yak": ("nijanta", "karmani"),
    "yang": ("yananta", "kartari"),
    "yang_yak": ("yananta", "karmani"),
    "yangluk": ("yanluganta", "kartari"),
    "yangluk_yak": ("yanluganta", "karmani"),
}
KRUT_MAP = {
    "krut": None,
    "san_krut": "sannanta",
    "nich_krut": "nijanta",
    "yang_krut": "yananta",
    "yangluk_krut": "yanluganta",
}
# engine pratyaya label -> search pratyaya label
PRAT_FAMILY = {"cAnaS": "SAnac", "BAvakarma-SAnac": "SAnac",
               "sya-SAnac": "SAnac", "sya-BAvakarma-SAnac": "SAnac",
               "sya-Satf": "Satf",
               "Ryat": "yat", "kyap": "yat", "vun": "Rvul",
               "zwran": "tfc"}
BASE_LAKARA = {"lat": "lw", "lang": "laN", "lot": "low",
               "vidhiling": "viDiliN", "lit": "liw", "lut": "luw",
               "rut": "lfw", "rung": "lfN", "ung": "luN",
               "ashirling": "ASIrliN", "shirling": "ASIrliN"}
SLOTS9 = [("prathama", "eka"), ("prathama", "dvi"), ("prathama", "bahu"),
          ("madhyama", "eka"), ("madhyama", "dvi"), ("madhyama", "bahu"),
          ("uttama", "eka"), ("uttama", "dvi"), ("uttama", "bahu")]
# lot 13-item table: idx -> slot
LOT13 = [0, 0, 0, 1, 2, 3, 3, 3, 4, 5, 6, 7, 8]


def split_variants(s):
    out = []
    for p in (s or "").split("/"):
        p = p.strip().strip(".,;")
        if p and p != "-" and " " not in p:
            out.append(p)
    return out


def decode_key(key):
    """(lakara, pada) from a JSON conjugation key like plat/alit/aashirling."""
    pada = "parasmaipada" if key.startswith("p") else "Atmanepada"
    base = key[1:] if key.startswith("p") else key[1:]
    # aashirling -> strip one leading 'a' gives 'ashirling'
    lakara = BASE_LAKARA.get(base)
    if lakara is None and base.startswith("a"):
        lakara = BASE_LAKARA.get(base[1:])
    return lakara, pada


def _strip_len(s):
    return s.replace("A", "a").replace("I", "i").replace("U", "u")


def _norm_slot(s):
    # orthographic noise invisible to slot identity: vowel length,
    # saM/sam anusvara, nich -ay- presence (BAvayiz vs BAviz),
    # retroflex/dental twin orthography (Q/D, W/T)
    return _strip_len(s).replace("M", "m").replace("ay", "").replace(
        "Ay", "").replace("Q", "D").replace("W", "T")


def _same_slot_variant(a, b):
    if a == b:
        return True
    na, nb = _norm_slot(a), _norm_slot(b)
    if na == nb:
        return True
    # twin-grade on normalized strings (BAvayizIQvam vs BAvizIDvam:
    # ay-pair + Q/D twin combined)
    if len(na) == len(nb) and na[:-1] == nb[:-1] and \
            {na[-1], nb[-1]} <= {"t", "d", "D", "Q", "T", "W", "s", "z"}:
        return True
    return False


def ending_slots(item, lakara, pada):
    """Exact slot set from the search ending tables (twins included).

    Formation-aware: t/d + D/Q + T/W twins, -a-ending collisions
    (baBUva is liT prath-eka + madh-bahu + utt-eka at once), dual-slot
    endings (low tAt). Returns None when no table ending fits.
    """
    from pypanini.search import _TIN_P, _TIN_A, _ensure_ready
    _ensure_ready()
    table = _TIN_P if pada == "parasmaipada" else _TIN_A
    cands = [(e, pur, vac) for (e, lak, pur, vac) in table
             if lak == lakara and item.endswith(e) and len(item) > len(e)]
    if not cands:
        return None
    maxlen = max(len(e) for (e, _, _) in cands)
    return {(pur, vac) for (e, pur, vac) in cands if len(e) == maxlen}


def positional_slots_list(items, lakara):
    """Slot per list item via dedupe-then-fixed-table.

    Adjacent same-slot variants (duplicates, a/A grades, saM/sam,
    nich -ay-, Q/D + W/T orthography) collapse first; the deduped
    length then selects an exact table: 9 -> slots, 13+low -> LOT13,
    13+laN -> yangluk root-aorist table, 10 with twin head -> twin
    table. Anything else falls back to sequential group assignment.
    """
    n = len(items)
    if n == 9:
        return [SLOTS9[i] for i in range(9)]
    if n == 13 and lakara == "low":
        return [SLOTS9[i] for i in LOT13]
    # dedupe adjacent norm-equal variants (NOT t/d twins: those keep
    # distinct items sharing slot 0 via the tables below)
    dedup = []
    for _t in items:
        if dedup and _norm_slot(_t) == _norm_slot(dedup[-1]):
            continue
        dedup.append(_t)
    # map deduped position -> original indices
    _pos_of = []
    _di = -1
    for _t in items:
        if _di >= 0 and _norm_slot(_t) == _norm_slot(dedup[_di]):
            _pos_of.append(_di)
        else:
            _di += 1
            _pos_of.append(_di)
    m = len(dedup)
    if m == 9:
        _patslots = [SLOTS9[i] for i in range(9)]
    elif m == 13 and lakara == "low":
        _patslots = [SLOTS9[i] for i in LOT13]
    elif m == 13 and lakara == "laN":
        # yangluk root-aorist paradigm (It/Id/ot/od + tAm/uH/...):
        # four prathama-eka formations share slot 0, tam/ta share
        # madh-bahu like lot tu/tAt
        _patslots = [SLOTS9[i] for i in (0, 0, 0, 0, 1, 2, 3, 4, 5, 5, 6, 7, 8)]
    elif m == 10 and _same_slot_variant(dedup[0], dedup[1]):
        _patslots = [SLOTS9[i] for i in (0, 0, 1, 2, 3, 4, 5, 6, 7, 8)]
    else:
        # sequential group assignment with overflow pin
        _patslots = [SLOTS9[min(i, 8)] for i in range(m)]
    return [_patslots[_pos_of[k]] for k in range(n)]


def positional_slot(items, idx, lakara):
    return positional_slots_list(items, lakara)[idx]


_AUX_SLOTS_CACHE = {}


def _aux_slots():
    """aux surface -> [(purusha, vacana, pada)] from engine perfects."""
    if _AUX_SLOTS_CACHE:
        return _AUX_SLOTS_CACHE
    from pypanini.tinanta import TinantaDerivationEngine
    from collections import defaultdict
    te = TinantaDerivationEngine()
    m = defaultdict(list)
    for rt in ("kf", "as", "BU"):
        for prayoga, _pada in (("kartari", "parasmaipada"),
                               ("karmani", "Atmanepada")):
            for pur in ("prathama", "madhyama", "uttama"):
                for vac in ("eka", "dvi", "bahu"):
                    try:
                        forms, _ = te.derive(rt, "liw", pur, vac,
                                             prayoga=prayoga)
                    except Exception:
                        continue
                    for f in forms:
                        if (pur, vac, _pada) not in m[f]:
                            m[f].append((pur, vac, _pada))
    # retroflex aux twins share slots
    for f, slots in list(m.items()):
        if "D" in f and f.replace("D", "Q") not in m:
            m[f.replace("D", "Q")] = list(slots)
    # data-attested aux outside engine liT inventory (Ahe <- Ase slots)
    if "Ase" in m and "Ahe" not in m:
        m["Ahe"] = list(m["Ase"])
    _AUX_SLOTS_CACHE.update(m)
    return _AUX_SLOTS_CACHE


def periphrastic_slot(token):
    """Exact (purusha, vacana) set for a periphrastic liT token via aux."""
    auxm = _aux_slots()
    for aux in sorted(auxm, key=len, reverse=True):
        if token.endswith(aux) and len(token) > len(aux) + 3:
            pre = token[:-len(aux)]
            if pre.endswith("Am") or pre.endswith("AY"):
                return set((p, v) for (p, v, _pa) in auxm[aux])
    return None


def fid_expectations(jpath, te=None, ke=None, do_engine=True):
    """All search-scored expectations for one JSON file."""
    with open(jpath, encoding="utf-8") as fh:
        data = json.load(fh)
    if data.get("skipped"):
        return []
    from pypanini import clean_dhatu_op
    info = {x["name"]: x["value"] for x in data.get("info", [])}
    dhatu = clean_dhatu_op(info.get("OpadeSikasvarUpam", ""))
    fid = Path(jpath).stem
    exps = []

    def _conj_exps(conj, prefix):
        for anta, (sanadi, prayoga) in ANTA_MAP.items():
            block = (conj or {}).get(anta)
            if not isinstance(block, dict):
                continue
            for key, lst in block.items():
                if not isinstance(lst, list) or not lst:
                    continue
                lakara, pada = decode_key(key)
                if lakara is None:
                    continue
                flat_items = []  # (surface, idx)
                for i, raw in enumerate(lst):
                    if not isinstance(raw, str):
                        continue
                    for v in split_variants(raw):
                        flat_items.append((v, i))
                # engine alignment: slot -> forms
                eng = defaultdict(set)
                if do_engine and te is not None:
                    for (pur, vac) in SLOTS9:
                        try:
                            forms, _ = te.derive(
                                dhatu, lakara, pur, vac, prayoga=prayoga,
                                sanadi=sanadi, dhatu_id=fid,
                                json_path=str(jpath),
                                upasarga=prefix)
                        except Exception:
                            continue
                        for f in forms:
                            eng[f].add((pur, vac))
                itemset = defaultdict(list)
                for (v, i) in flat_items:
                    itemset[v].append(i)
                try:
                    pos_slots = positional_slots_list(lst, lakara)
                except Exception:
                    pos_slots = None
                is_peri = (lakara == "liw" and len(lst) > 13)
                for v, idxs in itemset.items():
                    slots = set()
                    for f_slot in eng.get(v, set()):
                        slots.add(f_slot)
                    ended = ending_slots(v, lakara, pada)
                    _src = "engine-key" if v in eng else None
                    if ended:
                        slots |= ended
                        if _src is None:
                            _src = "ending"
                    if not slots and pos_slots is not None:
                        # exotic formation outside the ending tables:
                        # fall back to positional walk (flagged below)
                        for i in idxs:
                            if 0 <= i < len(pos_slots):
                                slots.add(pos_slots[i])
                        _src = "walk-fallback"
                    if is_peri:
                        auxs = periphrastic_slot(v)
                        if auxs:
                            slots |= auxs
                    exps.append({"surface": v, "fid": fid, "dhatu": dhatu,
                                 "kind": "tinanta", "anta": anta,
                                 "sanadi": sanadi, "prayoga": prayoga,
                                 "lakara": lakara, "pada": pada,
                                 "slots": sorted(slots),
                                 "prefix": prefix,
                                 "src": _src or "json-only"})

    def _part_exps(part, prefix):
        for kanta, sanadi in KRUT_MAP.items():
            pd = (part or {}).get(kanta)
            if not isinstance(pd, dict):
                continue
            for pratkey, entries in pd.items():
                if not isinstance(entries, list):
                    continue
                want = PRAT_FAMILY.get(pratkey, pratkey)
                for ent in entries:
                    if not isinstance(ent, dict):
                        continue
                    cands = []
                    for fld, lg in (("m", "puM"), ("f", "strI"),
                                    ("n", "napuMsaka")):
                        for v in split_variants(ent.get(fld, "")):
                            cands.append((v, lg))
                    base_vs = split_variants(ent.get("base", ""))
                    if base_vs and not cands:
                        for v in base_vs:
                            cands.append((v, None))
                    for (v, lg) in cands:
                        exps.append({"surface": v, "fid": fid,
                                     "dhatu": dhatu, "kind": "krdanta",
                                     "pratyaya": want, "raw_pratyaya": pratkey,
                                     "sanadi": sanadi, "linga": lg,
                                     "prefix": prefix, "src": "json"})

    _conj_exps(data.get("conjugations"), None)
    _part_exps(data.get("participles"), None)
    for prefix, pf in (data.get("upasarga_forms") or {}).items():
        if not isinstance(pf, dict):
            continue
        _conj_exps(pf.get("conjugations"), prefix)
        _part_exps(pf.get("participles"), prefix)
    return exps


def check_exp(exp, groups):
    """(hit, reason) for one expectation against grouped analyze() output."""
    if exp["kind"] == "tinanta":
        tins = [g for g in groups if g.get("kind") == "tinanta"]
        if not tins:
            return False, "no_tinanta_group"
        # dhatu groups matching fid or clean string
        cands = [g for g in tins
                 if (exp["fid"] in (g.get("ids") or [])
                     or (g.get("dhatu") and g.get("dhatu") == exp["dhatu"]))]
        if not cands:
            return False, "dhatu_missing"
        pre = exp.get("prefix")
        if pre is not None:
            # compound prefixes (a;b): search splits the outermost level only;
            # score on the full string when present, else outer head
            c2 = [g for g in cands if g.get("upasarga") == pre]
            if not c2:
                head = pre.split(";")[0] if ";" in pre else None
                c2 = ([g for g in cands if g.get("upasarga") == head]
                      if head else [])
                if not c2:
                    # prefix sandhi may also surface under a different split;
                    # accept any group whose upasarga is a member of the compound
                    members = set(pre.split(";"))
                    c2 = [g for g in cands
                          if g.get("upasarga") in members]
            if not c2 and pre == "AN":
                # AN routinely surfaces as bare A (ABo... for AN + consonant
                # in the data, ABu... before vowels): accept the A split
                c2 = [g for g in cands if g.get("upasarga") == "A"]
            cands = c2
            if not cands:
                return False, "upasarga_missing"
        for g in cands:
            for r in g.get("readings", []):
                if r.get("lakara") != exp["lakara"]:
                    continue
                if (r.get("purusha"), r.get("vacana")) in exp["slots"]:
                    return True, "hit"
        # distinguish lakara miss vs slot miss
        if any(r.get("lakara") == exp["lakara"] for g in cands
               for r in g.get("readings", [])):
            return False, "slot_missing"
        return False, "lakara_missing"
    else:
        krds = [g for g in groups if g.get("kind") == "krdanta"]
        if not krds:
            return False, "no_krdanta_group"
        cands = [g for g in krds
                 if (exp["fid"] in (g.get("ids") or [])
                     or (g.get("dhatu") and g.get("dhatu") == exp["dhatu"]))]
        if not cands:
            return False, "dhatu_missing"
        pre = exp.get("prefix")
        if pre is not None:
            c2 = [g for g in cands if g.get("upasarga") == pre]
            if not c2:
                members = set(pre.split(";"))
                c2 = [g for g in cands if g.get("upasarga") in members]
            if not c2 and pre == "AN":
                # AN routinely surfaces as bare A (ABo... for AN + consonant
                # in the data, ABu... before vowels): accept the A split
                c2 = [g for g in cands if g.get("upasarga") == "A"]
            cands = c2
            if not cands:
                return False, "upasarga_missing"
        for g in cands:
            for r in g.get("readings", []):
                if r.get("pratyaya") == exp["pratyaya"]:
                    return True, "hit"
        return False, "pratyaya_missing"


def audit_fid(jpath, do_engine=True):
    from pypanini import TinantaDerivationEngine
    te = TinantaDerivationEngine()
    exps = fid_expectations(jpath, te=te, do_engine=do_engine)
    # one search per unique surface
    by_surf = defaultdict(list)
    for e in exps:
        by_surf[e["surface"]].append(e)
    from pypanini.search import analyze
    rows = []
    for surf, es in by_surf.items():
        try:
            groups = analyze(surf)
        except Exception as ex:
            groups = []
            for e in es:
                rows.append((e, False, f"search_error:{ex}"))
            continue
        for e in es:
            hit, reason = check_exp(e, groups)
            rows.append((e, hit, reason))
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gana", default=None)
    ap.add_argument("--fid", default=None)
    ap.add_argument("--fid-list", default=None)
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--jobs", type=int, default=1)
    ap.add_argument("--out", default=None)
    ap.add_argument("--no-engine", action="store_true")
    ap.add_argument("--max-fids", type=int, default=0)
    args = ap.parse_args()

    if args.fid:
        files = [str(DATA_ROOT / args.fid[:2] / f"{args.fid}.json")]
    elif args.fid_list:
        files = [str(DATA_ROOT / f.strip()[:2] / f"{f.strip()}.json")
                 for f in args.fid_list.split(",")]
    elif args.gana:
        files = sorted(glob.glob(str(DATA_ROOT / args.gana / "*.json")))
    elif args.all:
        files = sorted(glob.glob(str(DATA_ROOT / "*/*.json")))
    else:
        files = sorted(glob.glob(str(DATA_ROOT / "01/*.json")))[:5]
    if args.max_fids:
        files = files[:args.max_fids]
    files = [f for f in files if os.path.exists(f)]
    print(f"fids: {len(files)}", flush=True)

    do_engine = not args.no_engine
    tot = 0
    hit = 0
    miss_counter = Counter()
    kind_counter = Counter()
    kind_hit_counter = Counter()
    miss_rows = []

    def _handle(rows):
        nonlocal tot, hit
        for (e, h, r) in rows:
            tot += 1
            _kk = e["kind"] + (f":{e.get('prefix') is not None}")
            kind_counter[_kk] += 1
            if h:
                hit += 1
                kind_hit_counter[_kk] += 1
            else:
                miss_counter[r] += 1
                miss_rows.append((e, h, r))

    if args.jobs > 1:
        from concurrent.futures import ProcessPoolExecutor
        with ProcessPoolExecutor(max_workers=args.jobs) as ex:
            futs = {ex.submit(audit_fid, f, do_engine): f for f in files}
            for i, fut in enumerate(futs):
                try:
                    _handle(fut.result())
                except Exception as e:
                    print(f"FID-ERROR {futs[fut]}: {e}", flush=True)
                    continue
                if (i + 1) % 10 == 0:
                    print(f"  {i + 1}/{len(files)} fids "
                          f"recall-so-far {hit}/{tot}", flush=True)
    else:
        for i, f in enumerate(files):
            try:
                _handle(audit_fid(f, do_engine))
            except Exception as e:
                print(f"FID-ERROR {f}: {e}", flush=True)
                continue
            if (i + 1) % 10 == 0:
                print(f"  {i + 1}/{len(files)} fids "
                      f"recall-so-far {hit}/{tot}", flush=True)

    print(f"\nRECALL {hit}/{tot} = {hit / max(tot, 1):.3%}")
    print("miss reasons:", dict(miss_counter.most_common(20)))
    for k in sorted(kind_counter):
        print(f"  {k}: {kind_hit_counter[k]}/{kind_counter[k]} "
              f"= {kind_hit_counter[k] / kind_counter[k]:.1%}")

    if args.out:
        with open(args.out, "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            w.writerow(["surface", "fid", "kind", "dhatu", "lakara",
                        "purusha", "vacana", "pratyaya", "sanadi",
                        "pada", "prayoga", "prefix", "src", "hit",
                        "reason"])
            for (e, h, r) in miss_rows:
                slots = ";".join(f"{p}.{v}" for (p, v) in e.get("slots", [])
                                  ) if e.get("slots") else ""
                # purusha/vacana columns carry the slot set for tinanta
                w.writerow([e["surface"], e["fid"], e["kind"], e["dhatu"],
                            e.get("lakara", ""), slots, "",
                            e.get("pratyaya", ""), e.get("sanadi", ""),
                            e.get("pada", ""), e.get("prayoga", ""),
                            e.get("prefix", ""), e.get("src", ""),
                            int(h), r])
        print(f"wrote {args.out} ({len(miss_rows)} miss rows)")
    return 0 if tot == 0 else (0 if hit == tot else 1)


if __name__ == "__main__":
    sys.exit(main())
