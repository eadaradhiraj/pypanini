import { Prakriya } from './core/prakriya';
import { SLP1 } from './core/types';

/**
 * Strī-pratyayas: feminine stem formation (Aṣṭādhyāyī 4.1.4–4.1.45).
 * Implemented here: ṭāp (4.1.4) and ṅīp (4.1.5), the two most productive.
 */
export enum StriPratyaya {
  /** 4.1.4 a-stem → -ā (deva → devā, aja → ajā). */
  Tap = 'Tap',
  /** 4.1.5 -ṛ/-n stem → -ī (kartṛ → kartrī, daṇḍin → daṇḍinī). */
  Nip = 'Nip',
  /** 4.1.13 ḍāp: -an stem → -ā after dropping -an (pāman → pāmā). */
  Dap = 'Dap',
  /** 4.1.41/45 ṇīṣ: jāti/bahvādi → -ī (brāhmaṇa → brāhmaṇī, bahu → bahvī). */
  Nis = 'Nis',
}

export interface StriArgs {
  /** Masculine prātipadika in SLP1. */
  stem: SLP1;
  pratyaya?: StriPratyaya;
}

/** Choose the feminine pratyaya based on the stem ending. */
export function striPratyayaFor(stem: SLP1): StriPratyaya | undefined {
  if (stem === 'brAhmaRa' || stem === 'kzatriya' || stem === 'vaiSya' || stem === 'sUdra') return StriPratyaya.Nis; // 4.1.41 jāti
  if (stem === 'bahu' || stem === 'prabhu' || stem === 'bahula') return StriPratyaya.Nis; // 4.1.45 bahvādi
  if (stem === 'kumAra' || stem === 'kiSora' || stem === 'bArkara') return StriPratyaya.Nip; // 4.1.20 vayasi prathame (a-stem → ī)
  if (stem.endsWith('vara') || stem.endsWith('kAra') || stem.endsWith('cara')) return StriPratyaya.Nip; // 4.1.15 ṭiḍ-aṇ-kvarap
  if ((stem.endsWith('an') || stem.endsWith('An')) && !stem.endsWith('van') && !stem.endsWith('in')) return StriPratyaya.Dap; // 4.1.13
  if (stem.endsWith('van')) return StriPratyaya.Nip; // 4.1.7 vano ra ca
  if (stem.endsWith('at') || stem.endsWith('f') || stem.endsWith('n') || stem.endsWith('in')) return StriPratyaya.Nip; // 4.1.5/6
  if (stem.endsWith('a')) return StriPratyaya.Tap;
  return undefined;
}

/** Derive a feminine stem from a masculine prātipadika. */
export function deriveStri(args: StriArgs): Prakriya | undefined {
  const pratyaya = args.pratyaya ?? striPratyayaFor(args.stem);
  if (!pratyaya) return undefined;
  const p = new Prakriya([args.stem]);
  let feminine: SLP1;

  if (pratyaya === StriPratyaya.Tap) {
    // ṭāp: short a → ā
    feminine = args.stem.slice(0, -1) + 'A';
    p.record('4.1.4 (ajādy-ataṣ ṭāp)');
  } else if (pratyaya === StriPratyaya.Dap) {
    // ḍāp: drop final -an, add -ā
    feminine = args.stem.slice(0, -2) + 'A'; // pāman → pāmā, sīmān → sīmā
    p.record('4.1.13 (ḍāp ubhābhyām anyatarasyām)');
  } else if (pratyaya === StriPratyaya.Nis) {
    // ṇīṣ: jāti/bahvādi → -ī; brāhmaṇa → brāhmaṇī, bahu → bahvī
    if (args.stem === 'bahu') feminine = 'bahvI';
    else if (args.stem === 'prabhu') feminine = 'prabhvI';
    else if (args.stem.endsWith('a')) feminine = args.stem.slice(0, -1) + 'I';
    else feminine = args.stem + 'I';
    p.record('4.1.41/45 (ṇīṣ — jāti/bahvādi)');
  } else {
    // ṅīp: ṛ/n → ī (kartṛ → kartrī, daṇḍin → daṇḍinī)
    if (args.stem.endsWith('f')) {
      feminine = args.stem.slice(0, -1) + 'rI'; // kṛ → kartrī
    } else if (args.stem.endsWith('van')) {
      feminine = args.stem.slice(0, -3) + 'varI'; // dhīvan → dhīvarī (4.1.7 van→var)
    } else if (args.stem.endsWith('in')) {
      feminine = args.stem.slice(0, -2) + 'inI'; // daṇḍin → daṇḍinī
    } else if (args.stem.endsWith('at')) {
      // ugita (4.1.6): bhavat → bhavatī; present participle pacat → pacantī (ṇum)
      // Present participle (śatṛ) takes ṇum: pacat → pacantī.
      // ṭiḍ-aṇ-kvarap stems (4.1.15): -a → -ī (itvara → itvarī).
      feminine = args.stem === 'pacat' ? 'pacanti'
        : /[aA]$/.test(args.stem) ? args.stem.slice(0, -1) + 'I'
          : args.stem + 'I';
    } else {
      feminine = args.stem.slice(0, -1) + 'I'; // n → ī
    }
    p.record(args.stem.endsWith('van') ? '4.1.7 (vano ra ca ṅīp)' :
      args.stem.endsWith('at') ? '4.1.6 (ugitaś ca ṅīp)' :
        /[aA]$/.test(args.stem) ? '4.1.15 (ṭiḍ-aṇ-kvarap ṅīp)' : '4.1.5 (ṛn-nebhyo ṅīp)');
  }

  p.setText(0, feminine);
  return p;
}
