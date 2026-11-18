import { SLP1 } from './core/types';

/**
 * Pāṇini 1.4.58 `prā-ādayaḥ` — the traditional list of upasargas (prefixes),
 * which become upasargas when joined to a verb (1.4.59 `upasargāḥ kriyāyoge`)
 * and are then called gati (1.4.60 `gatiś ca`).
 */
export const UPASARGAS: ReadonlyArray<{ slp1: SLP1; iast: string }> = [
  { slp1: 'pra', iast: 'pra' },
  { slp1: 'parA', iast: 'parā' },
  { slp1: 'ava', iast: 'ava' },
  { slp1: 'sam', iast: 'sam' },
  { slp1: 'anu', iast: 'anu' },
  { slp1: 'nis', iast: 'nis' },
  { slp1: 'dus', iast: 'dus' },
  { slp1: 'vi', iast: 'vi' },
  { slp1: 'AN', iast: 'āṅ' },
  { slp1: 'ni', iast: 'ni' },
  { slp1: 'aDi', iast: 'adhi' },
  { slp1: 'api', iast: 'api' },
  { slp1: 'ati', iast: 'ati' },
  { slp1: 'su', iast: 'su' },
  { slp1: 'ut', iast: 'ut' },
  { slp1: 'aBi', iast: 'abhi' },
  { slp1: 'prati', iast: 'prati' },
  { slp1: 'pari', iast: 'pari' },
  { slp1: 'upa', iast: 'upa' },
];

export function isUpasarga(s: SLP1): boolean {
  return UPASARGAS.some((u) => u.slp1 === s);
}

/**
 * 8.3.65 `upasargāt sunoti-suvati-…`: after an upasarga, the initial `s` of
 * these roots becomes `ṣ` (SLP1 `z`).
 */
const SATVA_ROOTS = new Set(['su', 'stu', 'stuB', 'sTA', 'sic', 'saYj', 'svaYj', 'senaya', 'sidh']);

export function needsSatva(upasarga: SLP1, root: SLP1): boolean {
  return isUpasarga(upasarga) && SATVA_ROOTS.has(root);
}

/**
 * 8.2.19 `upasargasya ayatau`: the `r`/`ā` of parā/pari/pra becomes `l`
 * before the root ay "go" (ayati/ayate).
 *   parā + ayate → palāyate, pari + ayate → palyayate, pra + ayate → plāyate.
 */
export function applyAyatiSandhi(upasarga: SLP1, root: SLP1): { upasarga: SLP1; root: SLP1 } {
  if (root !== 'ay' && root !== 'i') return { upasarga, root };
  const map: Record<string, string> = { parA: 'palA', pari: 'pali', pra: 'pla' };
  return { upasarga: map[upasarga] ?? upasarga, root };
}

/**
 * Apply the phonological effect of an upasarga on the following root.
 * 8.4.14 `upasargād asamāse'pi ṇopadeśasya`: a dental `n` at the start of the
 * root becomes retroflex `ṇ` (SLP1 `R`) after an upasarga.
 *   pra + nayati → praṇayati  (SLP1: pra + na... → praRa...)
 */
export function applyUpasargaSandhi(upasarga: SLP1, root: SLP1): SLP1 {
  if (!isUpasarga(upasarga)) return root;
  // 8.3.66 sadir aprateḥ: √sad → sīd after an upasarga in i/u (not prati),
  // with ṣa for the initial s. ni+sad → niṣīdati, vi+sad → viṣīdati.
  if (root === 'sad') {
    const satva = /[iu]$/.test(upasarga) && upasarga !== 'prati';
    return (satva ? 'z' : 's') + 'Id';
  }
  if (root.startsWith('n')) return 'R' + root.slice(1); // 8.4.14 ṇatva
  if (needsSatva(upasarga, root)) return 'z' + root.slice(1); // 8.3.65 ṣatva
  return root;
}
