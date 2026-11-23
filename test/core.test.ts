import test from 'node:test';
import assert from 'node:assert/strict';

import { gunafy, vrddhify, isSLP1, toDevanagari } from '../src/core/slp1';
import {
  Lakara,
  Pada,
  Prayoga,
  Purusha,
  Sanadi,
  Vacana,
} from '../src/core/types';
import { deriveTinantas, deriveLatParadigm } from '../src/tinanta';
import { deriveKrdantas } from '../src/krdanta';
import { deriveSubantas } from '../src/subanta';
import { Krt, Linga, Vibhakti } from '../src/core/types';
import { Vyakarana } from '../src/core/engine';
import { analyzeSubanta } from '../src/analyze';
import { heavyReduplicate } from '../src/sanadi';
import { DHATUPATHA, findDhatu, searchDhatus } from '../src/data/dhatupatha';
import { SUTRAS } from '../src/data/sutras';
import { deriveNamadhatus, NamadhatuPratyaya } from '../src/namadhatu';
import { derivePrecative } from '../src/aorist';
import { deriveParadigm, formatParadigm } from '../src/paradigm';
import { deriveStri } from '../src/stri';
import { applyNatva, applyAnusvara } from '../src/core/slp1';
import { UPASARGAS, isUpasarga, applyUpasargaSandhi, applyAyatiSandhi } from '../src/upasarga';

const baseArgs = {
  lakara: Lakara.Lat,
  prayoga: Prayoga.Kartari,
  pada: Pada.Parasmai,
  purusha: Purusha.Prathama,
  vacana: Vacana.Eka,
};

test('SLP1 helpers', () => {
  assert.deepEqual(gunafy('BU'), { text: 'Bo', changed: true });
  assert.deepEqual(gunafy('pac'), { text: 'pac', changed: false });
  assert.equal(vrddhify('ki').text, 'kE');
  assert.equal(toDevanagari('BU'), 'भू');
  assert.ok(isSLP1('Bavati'));
  assert.ok(!isSLP1('भवति'));
});

test('golden derivation: bhū → bhavati with full prakriyā', () => {
  const p = deriveTinantas({ ...baseArgs, dhatu: 'BU' })[0];
  assert.equal(p.text(), 'Bavati');

  const results = p.history.map((s) => s.result);
  assert.ok(results.includes('BU'));
  assert.ok(results.includes('BU + la~w'));
  assert.ok(results.includes('BU + l'));
  assert.ok(results.includes('BU + tip'));
  assert.ok(results.includes('BU + Sap + ti'));
  assert.ok(results.includes('Bo + a + ti'));
  assert.ok(results.includes('Bav + a + ti'));

  const codes = p.history.map((s) => s.rule);
  for (const code of ['1.3.1', '3.2.123', '1.3.9', '3.4.78', '3.1.68', '7.3.84', '6.1.78', '8.4.68']) {
    assert.ok(codes.includes(code), `missing rule ${code}`);
  }
});

test('golden trace preserved exactly after condition/mutation refactor', () => {
  const p = deriveTinantas({ ...baseArgs, dhatu: 'BU' })[0];
  assert.deepEqual(p.history.map((s) => `${s.rule}|${s.result}`), [
    '1.4.99 (laḥ parasmaipadam — parasmai-pada), 1.4.101 (tiṇas trīṇi), 1.4.102 (ekavacanādi)|BU',
    '1.3.1|BU',
    '3.1.1/3.1.2 (pratyayaḥ paraś ca), 3.1.91 (dhātoḥ), 3.1.93 (kṛdatiṅ)|BU',
    '3.2.123|BU + la~w',
    '1.3.2|BU + la~w',
    '1.3.3|BU + la~w',
    '1.3.9|BU + l',
    '1.3.78|BU + l',
    '3.4.78|BU + tip',
    '1.3.3|BU + tip',
    '1.3.9|BU + ti',
    '3.4.113|BU + ti',
    '3.1.68|BU + Sap + ti',
    '1.3.9|BU + a + ti',
    '3.4.113|BU + a + ti',
    '7.3.84|Bo + a + ti',
    '1.4.14|Bo + a + ti',
    '6.1.78|Bav + a + ti',
    '7.3.101|Bav + a + ti',
    '6.1.84 (ekādeśa: a + a/e/A → a/e/A)|Bav + a + ti',
    '8.4.68|Bavati',
  ]);
});

test('bhū lat parasmai paradigm (nine forms)', () => {
  const forms = deriveLatParadigm('BU').map((r) => r.text);
  assert.deepEqual(forms, [
    'Bavati', 'BavataH', 'Bavanti',
    'Bavasi', 'BavathaH', 'Bavatha',
    'BavAmi', 'BavAvaH', 'BavAmaH',
  ]);
});

test('tiṅanta: all lakāras for bhū (3rd singular, parasmai)', () => {
  const cases: Array<[Lakara, string]> = [
    [Lakara.Lat, 'Bavati'],    // bhavati — present
    [Lakara.Lit, 'baBUva'],    // babhūva — perfect
    [Lakara.Lut, 'BavitA'],    // bhavitā — periphrastic future
    [Lakara.Lrt, 'Bavizyati'], // bhaviṣyati — future
    [Lakara.Lot, 'Bavatu'],    // bhavatu — imperative
    [Lakara.Lan, 'aBavat'],    // abhavat — imperfect
    [Lakara.Lng, 'aBavizyat'], // abhaviṣyat — conditional
    [Lakara.Lin, 'Bavet'],     // bhavet — optative
  ];
  for (const [lakara, expected] of cases) {
    const p = deriveTinantas({ ...baseArgs, dhatu: 'BU', lakara })[0];
    assert.equal(p.text(), expected, `${lakara}`);
  }
});

test('ātmanepada endings audited (lat/lit)', () => {
  const form = (lakara: Lakara, purusha: Purusha, vacana: Vacana) =>
    deriveTinantas({
      ...baseArgs, dhatu: 'BU', lakara, pada: Pada.Atmane, purusha, vacana,
    })[0].text();

  // lat: bhavāvahe / bhavāmahe (not *bhavāvāhe / *bhavāmāhe)
  assert.equal(form(Lakara.Lat, Purusha.Uttama, Vacana.Dvi), 'BavAvahe');
  assert.equal(form(Lakara.Lat, Purusha.Uttama, Vacana.Bahu), 'BavAmahe');
  // lit: babhūviṣe / babhūvadhve / babhūvahe
  assert.equal(form(Lakara.Lit, Purusha.Madhyama, Vacana.Eka), 'baBUvise');
  assert.equal(form(Lakara.Lit, Purusha.Madhyama, Vacana.Bahu), 'baBUvaDve');
  assert.equal(form(Lakara.Lit, Purusha.Uttama, Vacana.Dvi), 'baBUvahe');
});

test('perfect (liṭ): strong/weak stems and endings', () => {
  const f = (d: string, p: Purusha, v: Vacana) =>
    deriveTinantas({ ...baseArgs, dhatu: d, lakara: Lakara.Lit, purusha: p, vacana: v })[0].text();
  // strong stems (root-vowel vṛddhi) in 3s/3d/2s/1s
  assert.equal(f('kf', Purusha.Prathama, Vacana.Eka), 'cakAra');   // cakāra
  assert.equal(f('pac', Purusha.Prathama, Vacana.Eka), 'papAca');  // papāca
  assert.equal(f('gam', Purusha.Prathama, Vacana.Eka), 'jagAma');  // jagāma
  assert.equal(f('ni', Purusha.Prathama, Vacana.Eka), 'ninAya');   // nināya
  assert.equal(f('yaj', Purusha.Prathama, Vacana.Eka), 'yayAja');  // yayāja
  assert.equal(f('vid', Purusha.Prathama, Vacana.Eka), 'veda');    // veda (perfect of √vid)
  assert.equal(f('han', Purusha.Prathama, Vacana.Eka), 'jaghAna'); // jaghāna
  assert.equal(f('car', Purusha.Prathama, Vacana.Eka), 'cacAra');  // cacāra
  // weak stems in 3p / 1d / 1p
  assert.equal(f('kf', Purusha.Prathama, Vacana.Bahu), 'cakruH');  // cakruḥ
  assert.equal(f('pac', Purusha.Uttama, Vacana.Dvi), 'papacva');   // papaciva
  assert.equal(f('kf', Purusha.Uttama, Vacana.Bahu), 'cakrma');    // cakṛma
});

test('luṭ (periphrastic future) audited — parasmai + atmane', () => {
  const form = (p: Purusha, v: Vacana, pada = Pada.Parasmai) =>
    deriveTinantas({ ...baseArgs, dhatu: 'BU', lakara: Lakara.Lut, purusha: p, vacana: v, pada })[0].text();
  // 3rd person = -tṛ noun nominative; 1st/2nd = sg. noun + "as"
  assert.equal(form(Purusha.Prathama, Vacana.Eka), 'BavitA');
  assert.equal(form(Purusha.Prathama, Vacana.Dvi), 'BavitArau');
  assert.equal(form(Purusha.Prathama, Vacana.Bahu), 'BavitAraH');
  assert.equal(form(Purusha.Madhyama, Vacana.Eka), 'BavitAsi');
  assert.equal(form(Purusha.Madhyama, Vacana.Dvi), 'BavitAsTaH');
  assert.equal(form(Purusha.Madhyama, Vacana.Bahu), 'BavitAsTa');
  assert.equal(form(Purusha.Uttama, Vacana.Eka), 'BavitAsmi');
  assert.equal(form(Purusha.Uttama, Vacana.Dvi), 'BavitAsvaH');
  assert.equal(form(Purusha.Uttama, Vacana.Bahu), 'BavitAsmaH');
  // ātmane (rare)
  assert.equal(form(Purusha.Madhyama, Vacana.Eka, Pada.Atmane), 'BavitAse');
  assert.equal(form(Purusha.Uttama, Vacana.Bahu, Pada.Atmane), 'BavitAmahe');
  // root-specific -tṛ stems (no spurious -i-, proper sandhi)
  const stem = (d: string) =>
    deriveTinantas({ ...baseArgs, dhatu: d, lakara: Lakara.Lut,
      purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text();
  assert.equal(stem('dA'), 'dAtA');   // dātā (not *dāitā)
  assert.equal(stem('kf'), 'kartA');  // kartā (not *karitā)
  assert.equal(stem('gam'), 'gantA'); // gantā
  assert.equal(stem('pac'), 'paktA'); // paktā (c → k)
  assert.equal(stem('yaj'), 'yaStA'); // yaṣṭā (j → ṣ, ṣṭ)
});

test('laṅ/lṛṅ ātmanepada 1st person dīrgha', () => {
  const form = (lakara: Lakara, vacana: Vacana) =>
    deriveTinantas({
      ...baseArgs, dhatu: 'BU', lakara, pada: Pada.Atmane,
      purusha: Purusha.Uttama, vacana,
    })[0].text();
  assert.equal(form(Lakara.Lan, Vacana.Dvi), 'aBavAvahi');
  assert.equal(form(Lakara.Lan, Vacana.Bahu), 'aBavAmahe');
  assert.equal(form(Lakara.Lng, Vacana.Dvi), 'aBavizyAvahi');
  assert.equal(form(Lakara.Lng, Vacana.Bahu), 'aBavizyAmahe');
  // root-specific future stems (no spurious -i-, proper ṣatva / jhal→k)
  const fut = (lakara: Lakara, d: string) =>
    deriveTinantas({ ...baseArgs, dhatu: d, lakara,
      purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text();
  assert.equal(fut(Lakara.Lrt, 'dA'), 'dAsyati');  // dāsyati
  assert.equal(fut(Lakara.Lrt, 'pac'), 'pakzyati'); // pakṣyati
  assert.equal(fut(Lakara.Lrt, 'yaj'), 'yakzyati'); // yakṣyati
  assert.equal(fut(Lakara.Lng, 'dA'), 'adAsyat');  // adāsyat
  assert.equal(fut(Lakara.Lrt, 'vid'), 'vedizyati'); // vediṣyati
  assert.equal(fut(Lakara.Lrt, 'diS'), 'dekzyati');  // dekṣyati
  // √han future stem is haṃsya- throughout (8.3.23), not a mix of
  // haṃsyati / haniṣyanti.
  assert.equal(fut(Lakara.Lrt, 'han'), 'haMsyati'); // haṃsyati
  assert.equal(deriveTinantas({ ...baseArgs, dhatu: 'han', lakara: Lakara.Lrt,
    purusha: Purusha.Prathama, vacana: Vacana.Bahu })[0].text(), 'haMsyanti'); // haṃsyanti
  assert.equal(deriveTinantas({ ...baseArgs, dhatu: 'han', lakara: Lakara.Lng,
    purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text(), 'ahaMsyat'); // ahaṃsyat
});

test('aorist (luN): root / a / s / iṣ varieties', () => {
  const aorist = (dhatu: string, p: Purusha, v: Vacana) =>
    deriveTinantas({
      ...baseArgs, dhatu, lakara: Lakara.LatN, purusha: p, vacana: v,
    })[0]?.text();
  // root aorist (bhū): abhūt, abhūvān ...
  assert.equal(aorist('BU', Purusha.Prathama, Vacana.Eka), 'aBUt');
  assert.equal(aorist('BU', Purusha.Madhyama, Vacana.Eka), 'aBUH');
  assert.equal(aorist('BU', Purusha.Prathama, Vacana.Bahu), 'aBUvan');
  assert.equal(aorist('BU', Purusha.Uttama, Vacana.Eka), 'aBUm');
  // a-aorist: apacat, asicat, agamat
  assert.equal(aorist('pac', Purusha.Prathama, Vacana.Eka), 'apacat');
  assert.equal(aorist('sic', Purusha.Prathama, Vacana.Eka), 'asicat');
  // s-aorist: anaiṣīt, iṣ-aorist: abodhīt
  assert.equal(aorist('ni', Purusha.Prathama, Vacana.Eka), 'anEzIt');
  assert.equal(aorist('budh', Purusha.Prathama, Vacana.Eka), 'aboDizIt');
});

test('rare aorists (reduplicating / siṣ / sa / passive) + precative', () => {
  const aorist = (dhatu: string, p: Purusha, v: Vacana) =>
    deriveTinantas({ ...baseArgs, dhatu, lakara: Lakara.LatN, purusha: p, vacana: v })[0]?.text();
  // reduplicating aorist (jan → ajījanat)
  assert.equal(aorist('jan', Purusha.Prathama, Vacana.Eka), 'ajIjanat');
  assert.equal(aorist('jan', Purusha.Uttama, Vacana.Bahu), 'ajIjanAma');
  assert.equal(aorist('jan', Purusha.Prathama, Vacana.Bahu, ), 'ajIjanan');
  // siṣ-aorist (yā → ayāsīt)
  assert.equal(aorist('yA', Purusha.Prathama, Vacana.Eka), 'ayAsIt');
  // sa-aorist (diś → adikṣat)
  assert.equal(aorist('diS', Purusha.Prathama, Vacana.Eka), 'adikzat');
  // s-aorist of kṛ (akārṣīt) — full parasmai paradigm
  assert.equal(aorist('kf', Purusha.Prathama, Vacana.Eka), 'akArzIt');  // akārṣīt
  assert.equal(aorist('kf', Purusha.Prathama, Vacana.Bahu), 'akArzuH'); // akārṣuḥ (3.4.109 jus)
  assert.equal(aorist('kf', Purusha.Uttama, Vacana.Eka), 'akArzm');    // akārṣam
  // 3.1.57 bhid a-aorist; 3p ekādeśa and 1d/1p dīrgha
  assert.equal(aorist('bhid', Purusha.Prathama, Vacana.Eka), 'abhidat');
  assert.equal(aorist('bhid', Purusha.Prathama, Vacana.Bahu), 'abhidan');
  assert.equal(aorist('bhid', Purusha.Uttama, Vacana.Dvi), 'abhidAva');
  assert.equal(aorist('pac', Purusha.Prathama, Vacana.Bahu), 'apacan');
  // √vac a-aorist (3.1.52) — avocat; root aorist 3s of dā — adāt
  assert.equal(aorist('vac', Purusha.Prathama, Vacana.Eka), 'avocat');  // avocat
  assert.equal(aorist('vac', Purusha.Prathama, Vacana.Bahu), 'avocan'); // avocan
  assert.equal(aorist('dA', Purusha.Prathama, Vacana.Eka), 'adAt');  // adāt
  assert.equal(aorist('dA', Purusha.Prathama, Vacana.Bahu), 'aduH');  // aduḥ
  // precative active (bhū → bhūyāt)
  assert.equal(derivePrecative({ root: 'BU', pada: Pada.Parasmai, purusha: Purusha.Prathama, vacana: Vacana.Eka })?.text(), 'BUyAt');
});

test('aorist ātmanepada (s/iṣ-aorist middle)', () => {
  const aor = (d: string, p: Purusha, v: Vacana) =>
    deriveTinantas({ ...baseArgs, dhatu: d, lakara: Lakara.LatN, pada: Pada.Atmane, purusha: p, vacana: v })[0]?.text();
  // s-aorist middle of nī: guṇa (ne), ṣṭ, 3pl -ata
  assert.equal(aor('ni', Purusha.Prathama, Vacana.Eka), 'anezTa');   // aneṣṭa
  assert.equal(aor('ni', Purusha.Prathama, Vacana.Bahu), 'anezata'); // aneṣata
  assert.equal(aor('ni', Purusha.Uttama, Vacana.Eka), 'anezi');     // aneṣi
  // iṣ-aorist middle of budh
  assert.equal(aor('budh', Purusha.Prathama, Vacana.Eka), 'abozizTa'); // abodhiṣṭa
  assert.equal(aor('budh', Purusha.Uttama, Vacana.Eka), 'abozizi');   // abodhiṣi
});

test('precative (āśīrliṅ) middle of bhū', () => {
  assert.equal(derivePrecative({ root: 'BU', pada: Pada.Atmane, purusha: Purusha.Prathama, vacana: Vacana.Eka })?.text(), 'BavizIza'); // bhaviṣīṣṭa
  assert.equal(derivePrecative({ root: 'BU', pada: Pada.Atmane, purusha: Purusha.Uttama, vacana: Vacana.Eka })?.text(), 'BavizIya');  // bhaviṣīya
});

test('athematic present forms (classes 2/3/5)', () => {
  const f = (d: string, lk: Lakara, p: Purusha) =>
    deriveTinantas({ ...baseArgs, dhatu: d, lakara: lk, purusha: p, vacana: Vacana.Eka })[0].text();
  // √as (2P)
  assert.equal(f('as', Lakara.Lat, Purusha.Prathama), 'asti');
  assert.equal(f('as', Lakara.Lat, Purusha.Uttama), 'asmi');
  assert.equal(f('as', Lakara.Lin, Purusha.Prathama), 'syAt');  // syāt
  assert.equal(f('as', Lakara.Lot, Purusha.Madhyama), 'ehi');
  // √dā (3P)
  assert.equal(f('dA', Lakara.Lat, Purusha.Prathama), 'dadAti'); // dadāti
  assert.equal(f('dA', Lakara.Lot, Purusha.Madhyama), 'dehi');
  // √kṛ (5P/8P)
  assert.equal(f('kf', Lakara.Lat, Purusha.Prathama), 'karoti');
  assert.equal(f('kf', Lakara.Lot, Purusha.Madhyama), 'kuru');
  // √han (2P)
  assert.equal(f('han', Lakara.Lat, Purusha.Prathama), 'hanti');
  assert.equal(f('han', Lakara.Lot, Purusha.Madhyama), 'jahi');
  // √kṛ ātmane (8P/5Ā), √i (2P), √yā (2P)
  const a = (d: string, p: Purusha) =>
    deriveTinantas({ ...baseArgs, dhatu: d, pada: Pada.Atmane,
      purusha: p, vacana: Vacana.Eka })[0].text();
  assert.equal(a('kf', Purusha.Prathama), 'kurute');
  assert.equal(a('kf', Purusha.Uttama), 'kurvE');    // kurve
  assert.equal(f('i', Lakara.Lat, Purusha.Prathama), 'eti');
  assert.equal(f('i', Lakara.Lat, Purusha.Madhyama), 'ezi');  // eṣi
  assert.equal(f('yA', Lakara.Lat, Purusha.Prathama), 'yAti');
  // √dā full athematic paradigm (class 3)
  assert.equal(f('dA', Lakara.Lat, Purusha.Prathama), 'dadAti');
  assert.equal(deriveTinantas({ ...baseArgs, dhatu: 'dA', purusha: Purusha.Prathama, vacana: Vacana.Dvi })[0].text(), 'dattaH');
  assert.equal(f('dA', Lakara.Lan, Purusha.Prathama), 'adadAt');
  assert.equal(f('dA', Lakara.Lit, Purusha.Prathama), 'dadau');
  assert.equal(a('dA', Purusha.Prathama), 'datte'); // √dā middle present
  // √hi (5P, śnu): hinoti; with upasarga 8.4.15 ṇatva
  assert.equal(f('hi', Lakara.Lat, Purusha.Prathama), 'hinoti');
  assert.equal(deriveTinantas({ ...baseArgs, dhatu: 'hi', upasarga: 'pra',
    purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text(), 'prahiRoti'); // prahiṇoti
  // class 7 (śnam): bhinatti, chinatti
  assert.equal(f('bhid', Lakara.Lat, Purusha.Prathama), 'bhinatti');
  assert.equal(f('Cid', Lakara.Lat, Purusha.Prathama), 'chinatti');
});

test('karmani passive: pac → pacyate', () => {
  const p = deriveTinantas({
    ...baseArgs,
    dhatu: 'pac',
    prayoga: Prayoga.Karmani,
    pada: Pada.Atmane,
  })[0];
  assert.equal(p.text(), 'pacyate');
  // special passive stems (samprasāraṇa / ā→ī)
  const passive = (d: string) => deriveTinantas({
    ...baseArgs, dhatu: d, prayoga: Prayoga.Karmani, pada: Pada.Atmane,
  })[0].text();
  assert.equal(passive('kf'), 'kriyate');  // kṛ → kriyate
  assert.equal(passive('dA'), 'dIyate');   // dā → dīyate
  assert.equal(passive('ni'), 'nIyate');   // nī → nīyate
  // bhāve (impersonal passive) = passive stem + 3s -te
  const bhave = (d: string) => deriveTinantas({
    ...baseArgs, dhatu: d, prayoga: Prayoga.Bhave, pada: Pada.Atmane,
  })[0].text();
  assert.equal(bhave('kf'), 'kriyate');
  assert.equal(bhave('dA'), 'dIyate');
  assert.equal(bhave('BU'), 'Bavyate');
});

test('karmani passive paradigm: pac (9 ātmane forms)', () => {
  const forms: string[] = [];
  for (const purusha of [Purusha.Prathama, Purusha.Madhyama, Purusha.Uttama]) {
    for (const vacana of [Vacana.Eka, Vacana.Dvi, Vacana.Bahu]) {
      forms.push(
        deriveTinantas({
          ...baseArgs,
          dhatu: 'pac',
          prayoga: Prayoga.Karmani,
          pada: Pada.Atmane,
          purusha,
          vacana,
        })[0].text(),
      );
    }
  }
  assert.deepEqual(forms, [
    'pacyate', 'pacyete', 'pacyante',
    'pacyase', 'pacyethe', 'pacyaDve',
    'pacye', 'pacyAvahe', 'pacyAmahe',
  ]);
});

test('ṇic causative: bhū → bhāvayati (BAvayati)', () => {
  const p = deriveTinantas({ ...baseArgs, dhatu: 'BU', sanadi: Sanadi.Nic })[0];
  assert.equal(p.text(), 'BAvayati');
  // vṛddhi (7.2.116) and special stems
  const c = (d: string) => deriveTinantas({ ...baseArgs, dhatu: d, sanadi: Sanadi.Nic })[0].text();
  assert.equal(c('pac'), 'pAcayati');  // pācayati
  assert.equal(c('kf'), 'kArayati');   // kārayati
  assert.equal(c('ni'), 'nAyayati');   // nāyayati
  assert.equal(c('dA'), 'dApayati');   // dāpayati (puk)
  assert.equal(c('han'), 'GAtayati');  // ghātayati
});

test('saṇādi: yaṅ / yāṅ (thematic intensive, ātmanepada)', () => {
  assert.equal(
    deriveTinantas({ ...baseArgs, dhatu: 'BU', sanadi: Sanadi.Yan })[0].text(),
    'BoBUyate', // bobhūyate
  );
  assert.equal(
    deriveTinantas({ ...baseArgs, dhatu: 'pac', sanadi: Sanadi.Yang })[0].text(),
    'pApacyate', // pāpacyate
  );
});

test('saṇādi: yaṅluk (athematic intensive, parasmaipada)', () => {
  assert.equal(
    deriveTinantas({ ...baseArgs, dhatu: 'BU', sanadi: Sanadi.YangLuk })[0].text(),
    'BoBavIti', // bobhavīti
  );
  assert.equal(
    deriveTinantas({ ...baseArgs, dhatu: 'pac', sanadi: Sanadi.YangLuk })[0].text(),
    'pApacIti', // pāpacīti
  );
});

test('saṇādi: san (desiderative, 3.1.7)', () => {
  const desiderative = (dhatu: string) =>
    deriveTinantas({ ...baseArgs, dhatu, sanadi: Sanadi.San })[0].text();
  assert.equal(desiderative('BU'), 'buBUzati');  // bubhūṣati
  assert.equal(desiderative('pac'), 'pipakzati'); // pipakṣati
  assert.equal(desiderative('kf'), 'cikIzati');   // cikīrṣati
  assert.equal(desiderative('gam'), 'jigamizati'); // jigamiṣati
  assert.equal(desiderative('vid'), 'vividizati'); // vividiṣati
  assert.equal(desiderative('nI'), 'ninIzati');    // ninīṣati
  assert.equal(desiderative('ji'), 'jijIzati');    // jijīṣati
  assert.equal(desiderative('zru'), 'zuzrUzati');  // śuśrūṣati
  assert.equal(desiderative('yaj'), 'yiyakzati');  // yiyakṣati
  assert.equal(desiderative('han'), 'jighAmsati'); // jighāṃsati
  assert.equal(desiderative('dA'), 'dIdAsati');    // dīdāsati (3.1.6 dīrgha)
  assert.equal(desiderative('mA'), 'mImAMsati');   // mīmāṃsati (3.1.6)
});

test('8.2.1 asiddha: desiderative -ṣa- keeps dental n of the tiṅ ending', () => {
  // The ṣ of -ṣa- is created by a later rule, so 8.4.1 ṇatva cannot see it.
  const desid3p = (dhatu: string) => deriveTinantas({
    ...baseArgs, dhatu, sanadi: Sanadi.San, purusha: Purusha.Prathama, vacana: Vacana.Bahu,
  })[0].text();
  assert.equal(desid3p('BU'), 'buBUzanti');   // bubhūṣanti (not *bubhūṣaṇti)
  assert.equal(desid3p('kf'), 'cikIzanti');   // cikīrṣanti
  assert.equal(desid3p('gam'), 'jigamizanti'); // jigamiṣanti
  assert.equal(desid3p('ji'), 'jijIzanti');   // jijīṣanti
});

test('heavy reduplication', () => {
  assert.equal(heavyReduplicate('BU'), 'BoBU');
  assert.equal(heavyReduplicate('pac'), 'pApac');
  assert.equal(heavyReduplicate('lup'), 'lolup'); // lo-lup
  assert.throws(() => heavyReduplicate('2pac'));
});

test('saṇādi: ṛ-final root kṛ', () => {
  assert.equal(
    deriveTinantas({ ...baseArgs, dhatu: 'kf', sanadi: Sanadi.Yan })[0].text(),
    'cekrIyate', // cekrīyate
  );
  assert.equal(
    deriveTinantas({ ...baseArgs, dhatu: 'kf', sanadi: Sanadi.YangLuk })[0].text(),
    'cakArti', // cakārti
  );
});

test('kṛdanta: karmani -ta and kartari -tṛ', () => {
  assert.equal(deriveKrdantas({ dhatu: 'kf', krt: Krt.Tac })[0].text(), 'kfta');
  assert.equal(deriveKrdantas({ dhatu: 'kf', krt: Krt.Tfc })[0].text(), 'kartf');
  // 8.2.36 j/ś → ṣ, 8.4.41 ṣṭ: yaj → yaṣṭa, diś → diṣṭa
  assert.equal(deriveKrdantas({ dhatu: 'yaj', krt: Krt.Tac })[0].text(), 'izwa');  // iṣṭa (6.1.15)
  assert.equal(deriveKrdantas({ dhatu: 'diS', krt: Krt.Tac })[0].text(), 'dizwa');  // diṣṭa
  assert.equal(deriveKrdantas({ dhatu: 'yaj', krt: Krt.KtvA })[0].text(), 'yazwvA'); // yaṣṭvā
  assert.equal(deriveKrdantas({ dhatu: 'mfj', krt: Krt.Tfc })[0].text(), 'mArzwf'); // mārṣṭṛ
  assert.equal(deriveKrdantas({ dhatu: 'sfj', krt: Krt.Tfc })[0].text(), 'sfzwf');  // sraṣṭṛ
  // 6.1.84 ekādeśa: dā + anīya → dānīya (ā + a → ā)
  assert.equal(deriveKrdantas({ dhatu: 'dA', krt: Krt.Ani })[0].text(), 'dAnIya');
  assert.equal(deriveKrdantas({ dhatu: 'gam', krt: Krt.KtvA })[0].text(), 'gatvA'); // gatvā (nasal lopa)
  // dā: datta/dattavān/dattvā (6.4.64 ā-lopa), but dātavya (gerundive)
  assert.equal(deriveKrdantas({ dhatu: 'dA', krt: Krt.Tac })[0].text(), 'datta');
  assert.equal(deriveKrdantas({ dhatu: 'dA', krt: Krt.KtvA })[0].text(), 'dattvA');
  assert.equal(deriveKrdantas({ dhatu: 'dA', krt: Krt.Tavya })[0].text(), 'dAtavya');
  // gam: m→n before dentals, m-lopa before kta, retained before -aka
  assert.equal(deriveKrdantas({ dhatu: 'gam', krt: Krt.Tac })[0].text(), 'gata');   // gata
  assert.equal(deriveKrdantas({ dhatu: 'gam', krt: Krt.Tum })[0].text(), 'gantum'); // gantum
  assert.equal(deriveKrdantas({ dhatu: 'gam', krt: Krt.Nvul })[0].text(), 'gamaka');// gamaka
});

test('kṛdanta: full kṛ paradigm', () => {
  const kf: Array<[Krt, string]> = [
    [Krt.Tac, 'kfta'], [Krt.Tfc, 'kartf'], [Krt.Satr, 'kurvat'],
    [Krt.Ani, 'karaRIya'], [Krt.Tum, 'kartum'], [Krt.Tavya, 'kartavya'],
    [Krt.LyuT, 'karaRa'], [Krt.KtvA, 'kftvA'], [Krt.Nvul, 'kAraka'],
    [Krt.Ktavatu, 'kftavAn'], [Krt.SanaC, 'kurvARa'], [Krt.Yat, 'kArya'],
    [Krt.Ktin, 'kfti'],
  ];
  for (const [krt, expected] of kf) {
    assert.equal(deriveKrdantas({ dhatu: 'kf', krt })[0].text(), expected, `kf + ${krt}`);
  }
});

test('kṛdanta: ktin (-ti) and 8.2.30 palatal → guttural', () => {
  // kṛ → kṛti, stu → stuti, ci → citi
  assert.equal(deriveKrdantas({ dhatu: 'kf', krt: Krt.Ktin })[0].text(), 'kfti');
  assert.equal(deriveKrdantas({ dhatu: 'stu', krt: Krt.Ktin })[0].text(), 'stuti');
  assert.equal(deriveKrdantas({ dhatu: 'ci', krt: Krt.Ktin })[0].text(), 'citi');
  // pac + ktin → pakti (c → k before the consonant-initial suffix)
  assert.equal(deriveKrdantas({ dhatu: 'pac', krt: Krt.Ktin })[0].text(), 'pakti');
  assert.ok(deriveKrdantas({ dhatu: 'pac', krt: Krt.Ktin })[0].history.some(s => s.rule.includes('8.2.30')));
});

test('kṛdanta: ṇini (-in) with vṛddhi and y-glide', () => {
  assert.equal(deriveKrdantas({ dhatu: 'kf', krt: Krt.Nini })[0].text(), 'kAriR'); // kāriṇ (8.4.1 ṇatva: r…n → ṇ)
  assert.equal(deriveKrdantas({ dhatu: 'dA', krt: Krt.Nini })[0].text(), 'dAyin'); // dāyin (no r/ṣ trigger)
  assert.equal(deriveKrdantas({ dhatu: 'pac', krt: Krt.Nini })[0].text(), 'pAcin'); // pācin
  assert.equal(deriveKrdantas({ dhatu: 'yaj', krt: Krt.Nini })[0].text(), 'yAjin'); // yājin
  assert.equal(deriveKrdantas({ dhatu: 'BU', krt: Krt.Nini })[0].text(), 'BAvin'); // bhāvin
  assert.equal(deriveKrdantas({ dhatu: 'vid', krt: Krt.Nini })[0].text(), 'vedin'); // vedin
  assert.equal(deriveKrdantas({ dhatu: 'car', krt: Krt.Nini })[0].text(), 'cAriR'); // cāriṇ
  assert.equal(deriveKrdantas({ dhatu: 'pac', krt: Krt.Nvul })[0].text(), 'pAcaka'); // pācaka
  assert.equal(deriveKrdantas({ dhatu: 'yaj', krt: Krt.Nvul })[0].text(), 'yAjaka'); // yājaka
  assert.equal(deriveKrdantas({ dhatu: 'dA', krt: Krt.Nvul })[0].text(), 'dAyaka');  // dāyaka
  assert.equal(deriveKrdantas({ dhatu: 'vaha', krt: Krt.Nvul })[0].text(), 'vAhaka'); // vāhaka
});

test('kṛdanta: śānan (-māna, 3.2.128)', () => {
  assert.equal(deriveKrdantas({ dhatu: 'pU', krt: Krt.Sanan })[0].text(), 'pavamAna'); // pavamāna
  assert.equal(deriveKrdantas({ dhatu: 'yaj', krt: Krt.Sanan })[0].text(), 'yajamAna'); // yajamāna
  assert.equal(deriveKrdantas({ dhatu: 'BU', krt: Krt.Sanan })[0].text(), 'BavamAna'); // bhavamāna
});

test('kṛdanta: ṣṭran (-tra instrument nouns, 3.2.182)', () => {
  assert.equal(deriveKrdantas({ dhatu: 'dA', krt: Krt.STran })[0].text(), 'dAtra'); // dātra
  assert.equal(deriveKrdantas({ dhatu: 'ni', krt: Krt.STran })[0].text(), 'netra'); // netra
  assert.equal(deriveKrdantas({ dhatu: 'stu', krt: Krt.STran })[0].text(), 'stotra'); // stotra
  assert.equal(deriveKrdantas({ dhatu: 'yu', krt: Krt.STran })[0].text(), 'yotra'); // yotra
  assert.equal(deriveKrdantas({ dhatu: 'hu', krt: Krt.STran })[0].text(), 'hotra'); // hotra
  assert.equal(deriveKrdantas({ dhatu: 'as', krt: Krt.STran })[0].text(), 'astra'); // astra
});

test('kṛdanta: tṛn (-tṛ habitual agent, 3.2.135)', () => {
  assert.equal(deriveKrdantas({ dhatu: 'kf', krt: Krt.TRn })[0].text(), 'kartf'); // kartṛ
  assert.equal(deriveKrdantas({ dhatu: 'hu', krt: Krt.TRn })[0].text(), 'hotf');  // hotṛ
  assert.equal(deriveKrdantas({ dhatu: 'ni', krt: Krt.TRn })[0].text(), 'nezTf');  // neṣṭṛ (8.2.36 ś→ṣ)
  assert.equal(deriveKrdantas({ dhatu: 'tviz', krt: Krt.TRn })[0].text(), 'tvazTf'); // tvaṣṭṛ
});

test('kṛdanta: kyap (-yā feminine, 3.3.99)', () => {
  assert.equal(deriveKrdantas({ dhatu: 'vid', krt: Krt.Kyap })[0].text(), 'vidyA'); // vidyā
  assert.equal(deriveKrdantas({ dhatu: 'man', krt: Krt.Kyap })[0].text(), 'manyA'); // manyā
  assert.equal(deriveKrdantas({ dhatu: 'i', krt: Krt.Kyap })[0].text(), 'ityA');   // ityā
  assert.equal(deriveKrdantas({ dhatu: 'zi', krt: Krt.Kyap })[0].text(), 'zayyA'); // śayyā
});

test('kṛdanta: śa (-ā/-iyā feminine) and 3.3.97 ktin variants', () => {
  // śa (3.3.100/101): kṛ → kriyā, iṣ → icchā
  assert.equal(deriveKrdantas({ dhatu: 'kf', krt: Krt.Sa })[0].text(), 'kriyA');
  assert.equal(deriveKrdantas({ dhatu: 'iz', krt: Krt.Sa })[0].text(), 'icCA');
  // 3.3.97 irregular ktin forms
  assert.equal(deriveKrdantas({ dhatu: 'av', krt: Krt.Ktin })[0].text(), 'Uti');   // ūti
  assert.equal(deriveKrdantas({ dhatu: 'han', krt: Krt.Ktin })[0].text(), 'heti'); // heti
  assert.equal(deriveKrdantas({ dhatu: 'san', krt: Krt.Ktin })[0].text(), 'sAti'); // sāti
});

test('kṛdanta: uḥ (-u) and ghaḥ (-a) suffixes', () => {
  assert.equal(deriveKrdantas({ dhatu: 'Bikz', krt: Krt.uH })[0].text(), 'Bikzu');  // bhikṣu
  assert.equal(deriveKrdantas({ dhatu: 'AzaMs', krt: Krt.uH })[0].text(), 'AzaMsu'); // āśaṃsu
  assert.equal(deriveKrdantas({ dhatu: 'CAd', krt: Krt.ghaH })[0].text(), 'Cada');  // chada
  assert.equal(deriveKrdantas({ dhatu: 'pac', krt: Krt.ghaH })[0].text(), 'pAka');  // pāka (vṛddhi + jhal→k)
  assert.equal(deriveKrdantas({ dhatu: 'tyj', krt: Krt.ghaH })[0].text(), 'tyAja'); // tyāga
  assert.equal(deriveKrdantas({ dhatu: 'BU', krt: Krt.ghaH })[0].text(), 'BAva');  // bhāva
  assert.equal(deriveKrdantas({ dhatu: 'car', krt: Krt.ghaH })[0].text(), 'cAra');  // cāra
  assert.equal(deriveKrdantas({ dhatu: 'ji', krt: Krt.ghaH })[0].text(), 'jaya');   // jaya
  assert.equal(deriveKrdantas({ dhatu: 'vid', krt: Krt.ghaH })[0].text(), 'veda');  // veda
  assert.equal(deriveKrdantas({ dhatu: 'nam', krt: Krt.ghaH })[0].text(), 'nAma');  // nāma
  assert.equal(deriveKrdantas({ dhatu: 'vid', krt: Krt.LyuT })[0].text(), 'vedana'); // vedana (guṇa)
  assert.equal(deriveKrdantas({ dhatu: 'gam', krt: Krt.Ktin })[0].text(), 'gati');  // gati (nasal lopa)
});

test('kṛdanta: raḥ (-ra) and kru (-ru) suffixes', () => {
  assert.equal(deriveKrdantas({ dhatu: 'nam', krt: Krt.raH })[0].text(), 'namra');  // namra
  assert.equal(deriveKrdantas({ dhatu: 'dIp', krt: Krt.raH })[0].text(), 'dIpra');  // dīpra
  assert.equal(deriveKrdantas({ dhatu: 'smi', krt: Krt.raH })[0].text(), 'smera');  // smera
  assert.equal(deriveKrdantas({ dhatu: 'Bi', krt: Krt.kru })[0].text(), 'Biru');   // bhīru
});

test('kṛdanta: āruḥ (-āru) and icchu suffix variants', () => {
  assert.equal(deriveKrdantas({ dhatu: 'vand', krt: Krt.AruH })[0].text(), 'vandAru'); // vandāru
  assert.equal(deriveKrdantas({ dhatu: 'iz', krt: Krt.uH })[0].text(), 'icCu');       // icchu
});

test('kṛdanta: varac (-vara, 3.2.175)', () => {
  assert.equal(deriveKrdantas({ dhatu: 'sTA', krt: Krt.varac })[0].text(), 'sTAvara'); // sthāvara
  assert.equal(deriveKrdantas({ dhatu: 'IS', krt: Krt.varac })[0].text(), 'ISvara');   // īśvara
});

test('kṛdanta: kvip zero-suffix agent nouns (3.2.178)', () => {
  assert.equal(deriveKrdantas({ dhatu: 'yuj', krt: Krt.kvip })[0].text(), 'yuk');      // yuk
  assert.equal(deriveKrdantas({ dhatu: 'cid', krt: Krt.kvip })[0].text(), 'cit');      // chit
  assert.equal(deriveKrdantas({ dhatu: 'Bid', krt: Krt.kvip })[0].text(), 'Bit');      // bhit
  assert.equal(deriveKrdantas({ dhatu: 'vac', krt: Krt.kvip })[0].text(), 'vAk');      // vāk
  assert.equal(deriveKrdantas({ dhatu: 'gam', krt: Krt.kvip })[0].text(), 'jagat');    // jagat
  assert.equal(deriveKrdantas({ dhatu: 'dyut', krt: Krt.kvip })[0].text(), 'vidyut');  // vidyut
  assert.equal(deriveKrdantas({ dhatu: 'dfSir', krt: Krt.kvip })[0].text(), 'dfk');    // dṛk (3.2.94)
  assert.equal(deriveKrdantas({ dhatu: 'BAs', krt: Krt.kvip })[0].text(), 'BAs');      // bhāḥ (3.2.177)
});

test('kṛdanta: ḍu (-u after upasarga+bhū, 3.2.180)', () => {
  assert.equal(deriveKrdantas({ dhatu: 'viBU', krt: Krt.Du })[0].text(), 'viBu');  // vibhu
  assert.equal(deriveKrdantas({ dhatu: 'praBU', krt: Krt.Du })[0].text(), 'praBu'); // prabhu
  assert.equal(deriveKrdantas({ dhatu: 'samBU', krt: Krt.Du })[0].text(), 'samBu'); // sambhu
});

test('kṛdanta: knu (-nu habitual agent, 3.2.140)', () => {
  assert.equal(deriveKrdantas({ dhatu: 'tras', krt: Krt.knu })[0].text(), 'trasnu');
  assert.equal(deriveKrdantas({ dhatu: 'gFDi', krt: Krt.knu })[0].text(), 'gFdnu');
  assert.equal(deriveKrdantas({ dhatu: 'DFzi', krt: Krt.knu })[0].text(), 'DFzRu'); // dhṛṣṇu (8.4.1 ṇatva)
  assert.equal(deriveKrdantas({ dhatu: 'kzip', krt: Krt.knu })[0].text(), 'kziNRu'); // kṣiṇṇu (ṇ + ṇ)
});

test('kṛdanta: kṣnu (-snu/-ṣṇu, 3.2.139)', () => {
  assert.equal(deriveKrdantas({ dhatu: 'glA', krt: Krt.kSnu })[0].text(), 'glAsnu');
  assert.equal(deriveKrdantas({ dhatu: 'ji', krt: Krt.kSnu })[0].text(), 'jizRu');
  assert.equal(deriveKrdantas({ dhatu: 'sTA', krt: Krt.kSnu })[0].text(), 'sTAsnu');
  assert.equal(deriveKrdantas({ dhatu: 'BU', krt: Krt.kSnu })[0].text(), 'BUzRu');
});

test('kṛdanta: iṣṇuc (-iṣṇu, 3.2.136/138)', () => {
  assert.equal(deriveKrdantas({ dhatu: 'BU', krt: Krt.izNuc })[0].text(), 'BavizRu'); // bhaviṣṇu
  assert.equal(deriveKrdantas({ dhatu: 'ruc', krt: Krt.izNuc })[0].text(), 'rocizRu'); // rociṣṇu
  assert.equal(deriveKrdantas({ dhatu: 'saha', krt: Krt.izNuc })[0].text(), 'sahizRu'); // sahiṣṇu
  assert.equal(deriveKrdantas({ dhatu: 'car', krt: Krt.izNuc })[0].text(), 'carizRu'); // cariṣṇu
});

test('kṛdanta: yuc (-ana) and ruḥ (-ru) suffixes', () => {
  assert.equal(deriveKrdantas({ dhatu: 'kruD', krt: Krt.yuc })[0].text(), 'kroDana');
  assert.equal(deriveKrdantas({ dhatu: 'As', krt: Krt.yuc })[0].text(), 'Asana');
  assert.equal(deriveKrdantas({ dhatu: 'vid', krt: Krt.yuc })[0].text(), 'vedana');
  assert.equal(deriveKrdantas({ dhatu: 'cal', krt: Krt.yuc })[0].text(), 'calana');
  assert.equal(deriveKrdantas({ dhatu: 'Sabd', krt: Krt.yuc })[0].text(), 'Sabdana');
  assert.equal(deriveKrdantas({ dhatu: 'dA', krt: Krt.ruH2 })[0].text(), 'dAru');
  assert.equal(deriveKrdantas({ dhatu: 'si', krt: Krt.ruH2 })[0].text(), 'saru');
  assert.equal(deriveKrdantas({ dhatu: 'sad', krt: Krt.ruH2 })[0].text(), 'sadru');
});

test('kṛdanta: kurac (-ura, 3.2.162)', () => {
  assert.equal(deriveKrdantas({ dhatu: 'vid', krt: Krt.kurac })[0].text(), 'vidura');
  assert.equal(deriveKrdantas({ dhatu: 'Bid', krt: Krt.kurac })[0].text(), 'Bidura');
  assert.equal(deriveKrdantas({ dhatu: 'cid', krt: Krt.kurac })[0].text(), 'cidura');
});

test('kṛdanta: ghurac (-ura, 3.2.161)', () => {
  assert.equal(deriveKrdantas({ dhatu: 'baNj', krt: Krt.ghurac })[0].text(), 'baNgura');
  assert.equal(deriveKrdantas({ dhatu: 'BAs', krt: Krt.ghurac })[0].text(), 'BAsura');
  assert.equal(deriveKrdantas({ dhatu: 'mid', krt: Krt.ghurac })[0].text(), 'medura');
});

test('kṛdanta: kvarap (-vara with ṭuk, 3.2.163)', () => {
  assert.equal(deriveKrdantas({ dhatu: 'iR', krt: Krt.kvarap })[0].text(), 'itvara'); // 6.1.71 ṭuk: iṇ → it
  assert.equal(deriveKrdantas({ dhatu: 'naS', krt: Krt.kvarap })[0].text(), 'naSvara');
  assert.equal(deriveKrdantas({ dhatu: 'ji', krt: Krt.kvarap })[0].text(), 'jitvara');
  assert.equal(deriveKrdantas({ dhatu: 'sf', krt: Krt.kvarap })[0].text(), 'sfvara');
});

test('kṛdanta: vuñ (-aka, 3.2.146)', () => {
  assert.equal(deriveKrdantas({ dhatu: 'nind', krt: Krt.vuN })[0].text(), 'nindaka');
  assert.equal(deriveKrdantas({ dhatu: 'hiMs', krt: Krt.vuN })[0].text(), 'hiMsaka');
  assert.equal(deriveKrdantas({ dhatu: 'KAd', krt: Krt.vuN })[0].text(), 'KAdaka');
});

test('kṛdanta: ghinuṇ (-ī, 3.2.143/145)', () => {
  assert.equal(deriveKrdantas({ dhatu: 'vikaS', krt: Krt.ghinuN })[0].text(), 'vikASI');
  assert.equal(deriveKrdantas({ dhatu: 'vilas', krt: Krt.ghinuN })[0].text(), 'vilAsI');
  assert.equal(deriveKrdantas({ dhatu: 'pralap', krt: Krt.ghinuN })[0].text(), 'pralApI');
  assert.equal(deriveKrdantas({ dhatu: 'duz', krt: Krt.ghinuN })[0].text(), 'dozI');
  assert.equal(deriveKrdantas({ dhatu: 'dviS', krt: Krt.ghinuN })[0].text(), 'dvezI');
  assert.equal(deriveKrdantas({ dhatu: 'yuj', krt: Krt.ghinuN })[0].text(), 'yogI');
});

test('kṛdanta: cānaś (-āna, 3.2.129)', () => {
  assert.equal(deriveKrdantas({ dhatu: 'buJ', krt: Krt.cAnaS })[0].text(), 'buJjAna');
  assert.equal(deriveKrdantas({ dhatu: 'biF', krt: Krt.cAnaS })[0].text(), 'bibRAna');
});

test('kṛdanta: aṇ (-ā feminine, 3.3.105)', () => {
  assert.equal(deriveKrdantas({ dhatu: 'cint', krt: Krt.aN })[0].text(), 'cintA');
  assert.equal(deriveKrdantas({ dhatu: 'pUj', krt: Krt.aN })[0].text(), 'pUjA');
  assert.equal(deriveKrdantas({ dhatu: 'kath', krt: Krt.aN })[0].text(), 'kathA');
});

test('kṛdanta: ghañ (-a action noun, 3.3.18)', () => {
  assert.equal(deriveKrdantas({ dhatu: 'pac', krt: Krt.gaNa })[0].text(), 'pAka');
  assert.equal(deriveKrdantas({ dhatu: 'tyaj', krt: Krt.gaNa })[0].text(), 'tyAga');
  assert.equal(deriveKrdantas({ dhatu: 'rAj', krt: Krt.gaNa })[0].text(), 'rAga');
});

test('kṛdanta: ap (-a action noun, 3.3.61/62)', () => {
  assert.equal(deriveKrdantas({ dhatu: 'svan', krt: Krt.ap })[0].text(), 'svAna');
  assert.equal(deriveKrdantas({ dhatu: 'has', krt: Krt.ap })[0].text(), 'hAsa');
  // 3.3.57 ṛdor ap: kara/śara/yava/lava
  assert.equal(deriveKrdantas({ dhatu: 'kf', krt: Krt.ap })[0].text(), 'kara');
  assert.equal(deriveKrdantas({ dhatu: 'sf', krt: Krt.ap })[0].text(), 'sara');
  assert.equal(deriveKrdantas({ dhatu: 'yu', krt: Krt.ap })[0].text(), 'yava');
});

test('kṛdanta: yat gerundive roots (3.1.97/99/102)', () => {
  assert.equal(deriveKrdantas({ dhatu: 'zak', krt: Krt.Yat })[0].text(), 'zakya');
  assert.equal(deriveKrdantas({ dhatu: 'sah', krt: Krt.Yat })[0].text(), 'sahya');
  assert.equal(deriveKrdantas({ dhatu: 'vah', krt: Krt.Yat })[0].text(), 'vahya');
});

test('kṛdanta: kañ (-śa, 3.2.60)', () => {
  assert.equal(deriveKrdantas({ dhatu: 'tad', krt: Krt.kaN })[0].text(), 'tAdfza');
  assert.equal(deriveKrdantas({ dhatu: 'yad', krt: Krt.kaN })[0].text(), 'yAdfza');
  assert.equal(deriveKrdantas({ dhatu: 'sa', krt: Krt.kaN })[0].text(), 'sadfza');
});

test('kṛdanta: kvin irregular agent nouns (3.2.59)', () => {
  assert.equal(deriveKrdantas({ dhatu: 'ftu', krt: Krt.kvin })[0].text(), 'ftvik');
  assert.equal(deriveKrdantas({ dhatu: 'DFz', krt: Krt.kvin })[0].text(), 'dadfzk');
  assert.equal(deriveKrdantas({ dhatu: 'sfj', krt: Krt.kvin })[0].text(), 'srak');
  assert.equal(deriveKrdantas({ dhatu: 'dfS', krt: Krt.kvin })[0].text(), 'dik');
});

test('kṛdanta: khukañ (-uka, 3.2.57)', () => {
  assert.equal(deriveKrdantas({ dhatu: 'BU', krt: Krt.khuKN })[0].text(), 'bAvuka');
});

test('kṛdanta: khyun (-ana instrument, 3.2.56)', () => {
  assert.equal(deriveKrdantas({ dhatu: 'kf', krt: Krt.khyun })[0].text(), 'karaRa'); // karaṇa (ṇ = R)
});

test('kṛdanta: ki/kin (-i with reduplication, 3.2.171)', () => {
  assert.equal(deriveKrdantas({ dhatu: 'dA', krt: Krt.kiN })[0].text(), 'dadi');  // dadiḥ
  assert.equal(deriveKrdantas({ dhatu: 'kf', krt: Krt.kiN })[0].text(), 'cakri'); // cakriḥ
  assert.equal(deriveKrdantas({ dhatu: 'gam', krt: Krt.kiN })[0].text(), 'jagmi'); // jagmiḥ
});

test('kṛdanta: najiṅ (-na habitual agent, 3.2.172)', () => {
  assert.equal(deriveKrdantas({ dhatu: 'svap', krt: Krt.najiN })[0].text(), 'svapna');  // svapna (dream)
  assert.equal(deriveKrdantas({ dhatu: 'tfza', krt: Krt.najiN })[0].text(), 'tfzRa'); // tṛṣṇa
  assert.equal(deriveKrdantas({ dhatu: 'Dfza', krt: Krt.najiN })[0].text(), 'DfzRa'); // dhṛṣṇa
});

test('kṛdanta: ac (-a action noun after i/ī roots, 3.3.56)', () => {
  assert.equal(deriveKrdantas({ dhatu: 'ci', krt: Krt.ac })[0].text(), 'caya');  // caya
  assert.equal(deriveKrdantas({ dhatu: 'ji', krt: Krt.ac })[0].text(), 'jaya');  // jaya
  assert.equal(deriveKrdantas({ dhatu: 'kzi', krt: Krt.ac })[0].text(), 'kzaya'); // kṣaya
});

test('kṛdanta: ṇa (3.3.90 yajña/praśna)', () => {
  assert.equal(deriveKrdantas({ dhatu: 'yaj', krt: Krt.naN })[0].text(), 'yajYa');  // yajña
  assert.equal(deriveKrdantas({ dhatu: 'praS', krt: Krt.naN })[0].text(), 'praSna'); // praśna (8.4.44 n stays dental)
  // 3.3.104 aṇ (masculine -a, vṛddhi): bhid → bheda
  assert.equal(deriveKrdantas({ dhatu: 'bhid', krt: Krt.aN })[0].text(), 'bheda');
});

test('kṛdanta: bhū forms with iṭ', () => {
  assert.equal(deriveKrdantas({ dhatu: 'BU', krt: Krt.Tum })[0].text(), 'Bavitum');
  assert.equal(deriveKrdantas({ dhatu: 'BU', krt: Krt.Tavya })[0].text(), 'Bavitavya');
  assert.equal(deriveKrdantas({ dhatu: 'BU', krt: Krt.Satr })[0].text(), 'Bavat');
  assert.equal(deriveKrdantas({ dhatu: 'BU', krt: Krt.Nvul })[0].text(), 'Bavaka');
  assert.equal(deriveKrdantas({ dhatu: 'BU', krt: Krt.LyuT })[0].text(), 'Bavana');
  assert.equal(deriveKrdantas({ dhatu: 'BU', krt: Krt.SanaC })[0].text(), 'BavamAna');
  assert.equal(deriveKrdantas({ dhatu: 'BU', krt: Krt.Yat })[0].text(), 'Bavya');
});

test('trace codes are audited (no TODO markers)', () => {
  const p = deriveTinantas({ ...baseArgs, dhatu: 'BU' })[0];
  const codes = p.history.map((s) => s.rule).join(' ');
  assert.ok(!codes.includes('TODO'));
  const k = deriveKrdantas({ dhatu: 'kf', krt: Krt.Tum })[0];
  assert.ok(!k.history.map((s) => s.rule).join(' ').includes('TODO'));
  assert.ok(k.history.some((s) => s.rule.includes('3.3.10')));
});

test('subanta: a-stem napumsaka instrumental plural', () => {
  const p = deriveSubantas({
    pratipadika: 'bala',
    linga: Linga.Napumsaka,
    vibhakti: Vibhakti.Trtiya,
    vacana: Vacana.Bahu,
  })[0];
  assert.equal(p.text(), 'balEH'); // balaiḥ, 7.1.9 ato bhisa ais
});

test('subanta: i-, u-, ā- and ī-stems', () => {
  const form = (pratipadika: string, linga: Linga, vibhakti: Vibhakti, vacana: Vacana) =>
    deriveSubantas({ pratipadika, linga, vibhakti, vacana })[0].text();

  // agni (m), i-stem
  assert.equal(form('agni', Linga.Pumsaka, Vibhakti.Prathama, Vacana.Eka), 'agniH');
  assert.equal(form('agni', Linga.Pumsaka, Vibhakti.Prathama, Vacana.Bahu), 'agnayaH');
  assert.equal(form('agni', Linga.Pumsaka, Vibhakti.Trtiya, Vacana.Bahu), 'agniBiH');
  assert.equal(form('agni', Linga.Pumsaka, Vibhakti.Saptami, Vacana.Bahu), 'agnizu');

  // guru (m), u-stem
  assert.equal(form('guru', Linga.Pumsaka, Vibhakti.Prathama, Vacana.Bahu), 'guravaH');
  assert.equal(form('guru', Linga.Pumsaka, Vibhakti.Trtiya, Vacana.Eka), 'guruRA');

  // vāri (n), i-stem
  assert.equal(form('vAri', Linga.Napumsaka, Vibhakti.Prathama, Vacana.Bahu), 'vArIRi');

  // sītā (f), ā-stem
  assert.equal(form('sItA', Linga.Stri, Vibhakti.Trtiya, Vacana.Eka), 'sItayA');
  assert.equal(form('sItA', Linga.Stri, Vibhakti.Caturthi, Vacana.Eka), 'sItAyE'); // sītāyai
  assert.equal(form('sItA', Linga.Stri, Vibhakti.Sasti, Vacana.Bahu), 'sItAnAm');

  // nadī (f), ī-stem
  assert.equal(form('nadI', Linga.Stri, Vibhakti.Prathama, Vacana.Bahu), 'nadyaH');
  assert.equal(form('nadI', Linga.Stri, Vibhakti.Caturthi, Vacana.Eka), 'nadyE');  // nadyai
  assert.equal(form('nadI', Linga.Stri, Vibhakti.Sasti, Vacana.Eka), 'nadyAH');   // nadyāḥ
  assert.equal(form('nadI', Linga.Stri, Vibhakti.Dvitiya, Vacana.Bahu), 'nadIH');  // nadīḥ
  assert.equal(form('nadI', Linga.Stri, Vibhakti.Saptami, Vacana.Bahu), 'nadizu'); // nadīṣu

  // mati (f), short-i stem
  assert.equal(form('mati', Linga.Stri, Vibhakti.Prathama, Vacana.Eka), 'matiH');
  assert.equal(form('mati', Linga.Stri, Vibhakti.Trtiya, Vacana.Eka), 'matyA');  // matyā
  assert.equal(form('mati', Linga.Stri, Vibhakti.Caturthi, Vacana.Eka), 'matyai'); // matyai
  assert.equal(form('mati', Linga.Stri, Vibhakti.Saptami, Vacana.Eka), 'matyAm'); // matyām

  // dātṛ (f), ṛ-stem
  assert.equal(form('dAtf', Linga.Stri, Vibhakti.Prathama, Vacana.Eka), 'dAtA');  // dātā
  assert.equal(form('dAtf', Linga.Stri, Vibhakti.Trtiya, Vacana.Eka), 'dAtrA');  // dātrā
});

test('subanta: feminine u-stem and -as neuter consonant stem', () => {
  const form = (pratipadika: string, linga: Linga, vibhakti: Vibhakti, vacana: Vacana) =>
    deriveSubantas({ pratipadika, linga, vibhakti, vacana })[0].text();

  // dhenu (f), u-stem
  assert.equal(form('Denu', Linga.Stri, Vibhakti.Prathama, Vacana.Eka), 'DenuH');
  assert.equal(form('Denu', Linga.Stri, Vibhakti.Trtiya, Vacana.Eka), 'DenvA');
  assert.equal(form('Denu', Linga.Stri, Vibhakti.Sasti, Vacana.Bahu), 'DenUnAm');
  assert.equal(form('vadhu', Linga.Stri, Vibhakti.Caturthi, Vacana.Eka), 'vadhvai'); // vadhvai
  assert.equal(form('vadhu', Linga.Stri, Vibhakti.Saptami, Vacana.Eka), 'vadhvAm'); // vadhvām

  // consonant stems (marut, vāc)
  assert.equal(form('marut', Linga.Pumsaka, Vibhakti.Prathama, Vacana.Eka), 'marut');
  assert.equal(form('marut', Linga.Pumsaka, Vibhakti.Trtiya, Vacana.Eka), 'marutA');
  assert.equal(form('vAc', Linga.Stri, Vibhakti.Trtiya, Vacana.Eka), 'vAcA');

  // manas (n), -as consonant stem
  assert.equal(form('manas', Linga.Napumsaka, Vibhakti.Prathama, Vacana.Eka), 'manas');
  assert.equal(form('manas', Linga.Napumsaka, Vibhakti.Trtiya, Vacana.Bahu), 'manoBiH');
  assert.equal(form('manas', Linga.Napumsaka, Vibhakti.Saptami, Vacana.Eka), 'manasi');
  assert.equal(form('manas', Linga.Napumsaka, Vibhakti.Prathama, Vacana.Bahu), 'manAMsi');
});

test('subanta: n-, t- and ṛ-stem consonants', () => {
  const form = (pratipadika: string, vibhakti: Vibhakti, vacana: Vacana) =>
    deriveSubantas({
      pratipadika, linga: Linga.Pumsaka, vibhakti, vacana,
    })[0].text();

  // rājan (m), -an stem
  assert.equal(form('rAjan', Vibhakti.Prathama, Vacana.Eka), 'rAjA');
  assert.equal(form('rAjan', Vibhakti.Trtiya, Vacana.Eka), 'rAjYA');
  assert.equal(form('rAjan', Vibhakti.Sasti, Vacana.Bahu), 'rAjYAm');

  // ātman (m): the n stays dental after m — only rājñā-type palatals take ñ.
  assert.equal(form('atman', Vibhakti.Trtiya, Vacana.Eka), 'atmanA');   // ātmanā
  assert.equal(form('atman', Vibhakti.Caturthi, Vacana.Eka), 'atmane'); // ātmane
  assert.equal(form('atman', Vibhakti.Sasti, Vacana.Dvi), 'atmanoH');   // ātmanoḥ
  assert.equal(form('atman', Vibhakti.Sasti, Vacana.Bahu), 'atmanAm');  // ātmanām
  assert.equal(form('mahAtman', Vibhakti.Trtiya, Vacana.Eka), 'mahAtmanA'); // mahātmanā

  // bhavat (m), -at stem
  assert.equal(form('Bavat', Vibhakti.Dvitiya, Vacana.Eka), 'Bavantam');
  assert.equal(form('Bavat', Vibhakti.Trtiya, Vacana.Bahu), 'BavadBiH');
  assert.equal(form('Bavat', Vibhakti.Saptami, Vacana.Bahu), 'Bavatsu');

  // pitṛ (m), -ṛ stem
  assert.equal(form('pitf', Vibhakti.Prathama, Vacana.Eka), 'pitA');
  assert.equal(form('pitf', Vibhakti.Sasti, Vacana.Bahu), 'pitFRAm'); // pitṝṇām
  assert.equal(form('pitf', Vibhakti.Saptami, Vacana.Bahu), 'pitfzu');
});

test('subanta: rare consonant stems (-an/-at neuter)', () => {
  const form = (pratipadika: string, vibhakti: Vibhakti, vacana: Vacana) =>
    deriveSubantas({
      pratipadika, linga: Linga.Napumsaka, vibhakti, vacana,
    })[0].text();
  // nāman (n), -an stem
  assert.equal(form('nAman', Vibhakti.Prathama, Vacana.Eka), 'nAma');
  assert.equal(form('nAman', Vibhakti.Trtiya, Vacana.Eka), 'nAmnA');
  assert.equal(form('nAman', Vibhakti.Prathama, Vacana.Bahu), 'nAmAni');
  assert.equal(form('nAman', Vibhakti.Saptami, Vacana.Bahu), 'nAmasu');
  // bhavat (n), -at stem
  assert.equal(form('Bavat', Vibhakti.Prathama, Vacana.Bahu), 'Bavanti');
  assert.equal(form('Bavat', Vibhakti.Saptami, Vacana.Bahu), 'Bavatsu');
});

test('reverse declension across stem classes', () => {
  const check = (word: string, expectedStem: string, expectedVibhakti: Vibhakti) => {
    const r = analyzeSubanta(word);
    assert.ok(r.length > 0, `no analysis for ${word}`);
    assert.equal(r[0].pratipadika, expectedStem, `stem for ${word}`);
    assert.equal(r[0].vibhakti, expectedVibhakti, `vibhakti for ${word}`);
  };
  check('agniBiH', 'agni', Vibhakti.Trtiya);
  check('guravaH', 'guru', Vibhakti.Prathama);
  check('sItayA', 'sItA', Vibhakti.Trtiya);
  check('nadyaH', 'nadI', Vibhakti.Prathama);
  check('vArIRi', 'vAri', Vibhakti.Prathama);
  check('manasi', 'manas', Vibhakti.Saptami);
  check('DenUnAm', 'Denu', Vibhakti.Sasti);
  check('rAjYA', 'rAjan', Vibhakti.Trtiya);
  check('pitfzu', 'pitf', Vibhakti.Saptami);
  // ṇatva surfaces (guru + unā → guruṇā) must reverse too.
  check('guruRA', 'guru', Vibhakti.Trtiya);
  check('taruRA', 'taru', Vibhakti.Trtiya);
});

test('reverse declension: strong ending must not be shadowed by weak a-m H', () => {
  const r = analyzeSubanta('agniH');
  // a-m would reconstruct agni with a weak H; i-m/i-f have the strong iH.
  assert.ok(r.some((x) => x.stemClass === 'i-m' && x.linga === Linga.Pumsaka
    && x.pratipadika === 'agni' && x.ending === 'iH'));
});

test('reverse declension: WrampaH and WrampeNa → base Wramp', () => {
  const nom = analyzeSubanta('WrampaH');
  assert.equal(nom.length, 1);
  assert.equal(nom[0].base, 'Wramp');
  assert.equal(nom[0].pratipadika, 'Wrampa');
  assert.equal(nom[0].vibhakti, Vibhakti.Prathama);
  assert.equal(nom[0].vacana, Vacana.Eka);
  assert.equal(nom[0].linga, Linga.Pumsaka);

  const inst = analyzeSubanta('WrampeNa');
  assert.ok(inst.length > 0);
  assert.equal(inst[0].base, 'Wramp');
  assert.equal(inst[0].pratipadika, 'Wrampa');
  assert.equal(inst[0].vibhakti, Vibhakti.Trtiya);
  assert.equal(inst[0].vacana, Vacana.Eka);
});

test('masculine a-stem nominative: rAma → rAmaH', () => {
  assert.equal(
    deriveSubantas({
      pratipadika: 'rAma',
      linga: Linga.Pumsaka,
      vibhakti: Vibhakti.Prathama,
      vacana: Vacana.Eka,
    })[0].text(),
    'rAmaH',
  );
});

test('full MIT Dhātupāṭha is loaded', () => {
  assert.ok(DHATUPATHA.length > 2000, `expected 2000+ roots, got ${DHATUPATHA.length}`);
  assert.equal(findDhatu('BU')?.code, '01.0001');
  assert.equal(findDhatu('BU')?.gana, 1);
  assert.ok(searchDhatus('BU').length >= 5);
  assert.ok(SUTRAS.length > 3900);
});

test('nāmādhatu (denominative) derivations', () => {
  const form = (pratipadika: string, pratyaya: NamadhatuPratyaya) =>
    deriveNamadhatus({ pratipadika, pratyaya })[0].text();
  assert.equal(form('putra', NamadhatuPratyaya.Kyac), 'putrIyati');
  assert.equal(form('putra', NamadhatuPratyaya.Kamyac), 'putrakAmyati'); // putrakāmyati
  assert.equal(form('putra', NamadhatuPratyaya.KyacAcara), 'putrIyati'); // 3.1.10 upamānād ācāre
  assert.equal(form('vidyA', NamadhatuPratyaya.Kyac), 'vidyAyati');    // ā-stem takes -ya
  assert.equal(form('putra', NamadhatuPratyaya.KyaN), 'putrAyate');
  assert.equal(form('Syena', NamadhatuPratyaya.KyaN), 'SyenAyate');
  assert.equal(form('putra', NamadhatuPratyaya.Nic), 'putrayati');
  assert.equal(form('vidyA', NamadhatuPratyaya.Nic), 'vidyAyati'); // vidyāyati (ā+a→ā)
  assert.equal(form('vidyA', NamadhatuPratyaya.KyaN), 'vidyAyate'); // vidyāyate (ā+ā→ā)
  assert.equal(form('kazwa', NamadhatuPratyaya.KyaNKa), 'kazwAyate'); // kaṣṭāyate
  assert.equal(form('lohita', NamadhatuPratyaya.KyaS), 'lohitAyate');
  // 3.1.15 / 3.1.16 / 3.1.19
  assert.equal(form('roma', NamadhatuPratyaya.Varticara), 'romAyate');
  assert.equal(form('bAzpa', NamadhatuPratyaya.Udvamana), 'bAzpAyate');
  assert.equal(form('namas', NamadhatuPratyaya.KyacNama), 'namasyati');
  assert.equal(form('citra', NamadhatuPratyaya.KyacNama), 'citrayati'); // citra + ya → citraya (final a kept)
  assert.equal(form('pucCa', NamadhatuPratyaya.NiN), 'pucCayate'); // 3.1.20
});

test('upasargas (prefixes, 1.4.58–1.4.60)', () => {
  assert.equal(UPASARGAS.length, 19);
  assert.ok(isUpasarga('pra'));
  assert.ok(isUpasarga('aBi'));
  assert.ok(!isUpasarga('bhavatu'));
  assert.equal(applyUpasargaSandhi('pra', 'nam'), 'Ram'); // 8.4.14 ṇatva
  assert.equal(applyUpasargaSandhi('sam', 'BU'), 'BU');
  assert.equal(applyUpasargaSandhi('aBi', 'su'), 'zu'); // 8.3.65 ṣatva on the root
  assert.deepEqual(applyAyatiSandhi('parA', 'ay'), { upasarga: 'palA', root: 'ay' }); // 8.2.19
  assert.equal(
    deriveTinantas({ ...baseArgs, dhatu: 'ay', upasarga: 'parA', pada: Pada.Atmane })[0].text(),
    'palAyate', // palāyate
  );
  assert.ok(deriveTinantas({ ...baseArgs, dhatu: 'su', upasarga: 'aBi' })[0].text().startsWith('aBiz'));

  assert.equal(
    deriveTinantas({ ...baseArgs, dhatu: 'BU', upasarga: 'pra' })[0].text(),
    'praBavati', // prabhavati
  );
  assert.equal(
    deriveTinantas({ ...baseArgs, dhatu: 'nam', upasarga: 'pra' })[0].text(),
    'praRamati', // praṇamati
  );
  // 6.1.77 iko yaṇ aci: u + a → va (anu + ay → anvayati)
  assert.equal(
    deriveTinantas({ ...baseArgs, dhatu: 'ay', upasarga: 'anu' })[0].text(),
    'anvayati', // anvayati
  );
  // 8.3.66 sadir aprateḥ: ni/vi + sad → niṣīdati / viṣīdati
  assert.equal(
    deriveTinantas({ ...baseArgs, dhatu: 'sad', upasarga: 'ni' })[0].text(),
    'nizIdati', // niṣīdati
  );
  assert.equal(
    deriveTinantas({ ...baseArgs, dhatu: 'sad', upasarga: 'prati' })[0].text(),
    'pratisIdati', // no ṣatva after prati
  );
  // 6.1.101 akaḥ savarṇe dīrghaḥ: pra + ay → plāyati (8.2.19 pra→pla)
  assert.equal(
    deriveTinantas({ ...baseArgs, dhatu: 'ay', upasarga: 'pra' })[0].text(),
    'plAyati', // plāyati
  );
});

test('bulk smoke test: all Dhātupāṭha roots × lakāras × padas', () => {
  const lakaras = [Lakara.Lat, Lakara.Lit, Lakara.Lut, Lakara.Lrt, Lakara.Lot, Lakara.Lan, Lakara.Lng, Lakara.Lin];
  let checked = 0;
  for (const d of DHATUPATHA) {
    for (const lakara of lakaras) {
      for (const pada of [Pada.Parasmai, Pada.Atmane]) {
        const r = deriveTinantas({
          dhatu: d, lakara, prayoga: Prayoga.Kartari,
          purusha: Purusha.Prathama, vacana: Vacana.Eka, pada,
        });
        assert.ok(r.length === 1 && r[0].text().length > 0, `${d.code} ${lakara} ${pada}`);
        checked++;
      }
    }
  }
  assert.ok(checked > 30000);
});

test('yaṅ unavailable for non-monomorphic roots returns no forms (3.1.22)', () => {
  assert.equal(deriveTinantas({ ...baseArgs, dhatu: 'gADf', sanadi: Sanadi.Yan }).length, 0);
  assert.equal(deriveTinantas({ ...baseArgs, dhatu: 'eDa', sanadi: Sanadi.Yan }).length, 0);
  // valid roots still work
  assert.ok(deriveTinantas({ ...baseArgs, dhatu: 'pac', sanadi: Sanadi.Yan }).length === 1);
});

test('paradigm generator (full conjugation table)', () => {
  const para = deriveParadigm({ dhatu: 'BU' });
  assert.equal(para.cells.length, 8 * 2 * 3 * 3); // 8 lakāras × 2 padas × 9 forms
  const latPara = para.cells.find(
    (c) => c.lakara === Lakara.Lat && c.pada === Pada.Parasmai &&
      c.purusha === Purusha.Prathama && c.vacana === Vacana.Eka,
  );
  assert.equal(latPara?.text, 'Bavati');
  const rendered = formatParadigm(para);
  assert.ok(rendered.includes('## lat · parasmai'));
  assert.ok(rendered.includes('Bavati'));
});

test('strī-pratyayas: ṭāp (4.1.4) and ṅīp (4.1.5)', () => {
  assert.equal(deriveStri({ stem: 'deva' })?.text(), 'devI');   // devī (ṇīṣ, not *devā)
  assert.equal(deriveStri({ stem: 'aja' })?.text(), 'ajA');     // ajā
  assert.equal(deriveStri({ stem: 'kartf' })?.text(), 'kartrI'); // kartrī
  assert.equal(deriveStri({ stem: 'daNDin' })?.text(), 'daNDinI'); // daṇḍinī
  assert.equal(deriveStri({ stem: 'Bavat' })?.text(), 'BavatI');   // bhavatī (4.1.6)
  assert.equal(deriveStri({ stem: 'pacat' })?.text(), 'pacanti');  // pacantī (4.1.6)
  assert.equal(deriveStri({ stem: 'dIvan' })?.text(), 'dIvarI');   // dhīvarī (4.1.7)
  assert.equal(deriveStri({ stem: 'pAman' })?.text(), 'pAmA');     // pāmā (4.1.13 ḍāp)
  assert.equal(deriveStri({ stem: 'sImAn' })?.text(), 'sImA');     // sīmā (4.1.13)
  assert.equal(deriveStri({ stem: 'kurucara' })?.text(), 'kurucarI'); // kurucarī (4.1.15)
  assert.equal(deriveStri({ stem: 'itvara' })?.text(), 'itvarI');   // itvarī (4.1.15)
  assert.equal(deriveStri({ stem: 'kumAra' })?.text(), 'kumArI');   // kumārī (4.1.20)
  assert.equal(deriveStri({ stem: 'kiSora' })?.text(), 'kiSorI');   // kiśorī (4.1.20)
  assert.equal(deriveStri({ stem: 'brAhmaRa' })?.text(), 'brAhmaRI'); // brāhmaṇī (4.1.41)
  assert.equal(deriveStri({ stem: 'bahu' })?.text(), 'bahvI');      // bahvī (4.1.45)
  assert.equal(deriveStri({ stem: 'antarvat' })?.text(), 'antarvatnI'); // antarvatnī (4.1.32)
  assert.equal(deriveStri({ stem: 'pativat' })?.text(), 'pativatnI');   // pativatnī (4.1.32)
  assert.equal(deriveStri({ stem: 'pati' })?.text(), 'patnI');         // patnī (4.1.33)
  assert.equal(deriveStri({ stem: 'pUtakratu' })?.text(), 'pUtakratAyI'); // 4.1.36
  assert.equal(deriveStri({ stem: 'manu' })?.text(), 'manAyI');        // manāyī (4.1.38)
  assert.equal(deriveStri({ stem: 'harita' })?.text(), 'hariRI');      // hariṇī (4.1.39)
  assert.equal(deriveStri({ stem: 'Syeza' })?.text(), 'SyenI');        // śyenī (4.1.40)
  assert.equal(deriveStri({ stem: 'kuND' })?.text(), 'kuNDI');         // kuṇḍī (4.1.42)
  assert.equal(deriveStri({ stem: 'sthala' })?.text(), 'sthalI');      // sthalī (4.1.42)
  assert.equal(deriveStri({ stem: 'nIla' })?.text(), 'nIlI');          // nīlī (4.1.42)
  assert.equal(deriveStri({ stem: 'SoRa' })?.text(), 'SoRI');          // śoṇī (4.1.43)
  assert.equal(deriveStri({ stem: 'paTu' })?.text(), 'paTvI');          // paṭvī (4.1.44)
  assert.equal(deriveStri({ stem: 'mRdu' })?.text(), 'mRdvI');         // mṛdvī (4.1.44)
  assert.equal(deriveStri({ stem: 'cRaD' })?.text(), 'cRaDI');         // caṇḍī (4.1.45)
  assert.equal(deriveStri({ stem: 'kamala' })?.text(), 'kamalI');      // kamalī (4.1.45)
  assert.equal(deriveStri({ stem: 'indra' })?.text(), 'indrARi');      // indrāṇī (4.1.49)
  assert.equal(deriveStri({ stem: 'rudra' })?.text(), 'rudrARi');      // rudrāṇī (4.1.49)
  assert.equal(deriveStri({ stem: 'sakhin' })?.text(), 'sakhI');       // sakhī
  assert.equal(deriveStri({ stem: 'sakhA' })?.text(), 'sakhI');        // sakhī
  assert.equal(deriveStri({ stem: 'vahu' })?.text(), 'vahvI');         // vahvī
  assert.equal(deriveStri({ stem: 'aSiSu' })?.text(), 'aSivI');        // aśiśvī (4.1.62)
  assert.equal(deriveStri({ stem: 'yuvan' })?.text(), 'yuvatI');       // yuvatī (4.1.77)
  assert.equal(deriveStri({ stem: 'BavAn' })?.text(), 'BavatI');       // bhavatī (4.1.87)
  assert.equal(deriveStri({ stem: 'rAjan' })?.text(), 'rAjYI');        // rājñī
  assert.equal(deriveStri({ stem: 'bhagavAt' })?.text(), 'BagavatI');  // bhagavatī
  assert.equal(deriveStri({ stem: 'taruNa' })?.text(), 'taruNI');        // taruṇī
});

test('8.4.1 ṇatva (n → ṇ after r/ṣ/ṛ in a pada)', () => {
  assert.equal(applyNatva('kRzna'), 'kRzRa');  // kṛṣṇa (n → ṇ after ṣ)
  assert.equal(applyNatva('puzna'), 'puzRa');  // puṣṇa
  assert.equal(applyNatva('mAtfna'), 'mAtfRa'); // mātṛṇā
  assert.equal(applyNatva('agni'), 'agni');     // no r/ṣ before n
  assert.equal(applyNatva('arKeRa'), 'arKeRa'); // 8.4.2: guttural intervenes, n→ṇ applied
  assert.equal(applyNatva('darpRa'), 'darpRa'); // 8.4.2: labial intervenes
  assert.equal(applyNatva('prayaAni'), 'prayaARi'); // 8.4.16: y intervenes (semivowel)
  // 8.3.23 mo'nusvāraḥ: m → M before a consonant
  assert.equal(applyAnusvara('samgamati'), 'saMgamati');
  assert.equal(
    deriveTinantas({ ...baseArgs, dhatu: 'gam', upasarga: 'sam' })[0].text(),
    'saMgacchati', // saṃgacchati (7.3.77 gam → gacch)
  );
  // 8.4.16 in a real derivation: pra+vap lot 1s → prava-pā-ṇi
  assert.equal(
    deriveTinantas({ ...baseArgs, dhatu: 'vap', upasarga: 'pra', lakara: Lakara.Lot,
      purusha: Purusha.Uttama, vacana: Vacana.Eka })[0].text(),
    'pravapARi',
  );
});

test('Vyakarana facade', () => {
  const v = new Vyakarana();
  assert.equal(v.deriveTinantas({ ...baseArgs, dhatu: 'BU' })[0].text(), 'Bavati');
});

test('7.3.77: √gam present stem gacch- (gacchati/agacchat/gacchet)', () => {
  const f = (lakara: Lakara, pada: Pada, purusha: Purusha, vacana: Vacana) =>
    deriveTinantas({ ...baseArgs, dhatu: 'gam', lakara, pada, purusha, vacana })[0].text();
  assert.equal(f(Lakara.Lat, Pada.Parasmai, Purusha.Prathama, Vacana.Eka), 'gacchati');
  assert.equal(f(Lakara.Lat, Pada.Parasmai, Purusha.Prathama, Vacana.Bahu), 'gacchanti');
  assert.equal(f(Lakara.Lat, Pada.Atmane, Purusha.Prathama, Vacana.Eka), 'gacchate');
  assert.equal(f(Lakara.Lan, Pada.Parasmai, Purusha.Prathama, Vacana.Eka), 'agacchat');
  assert.equal(f(Lakara.Lot, Pada.Parasmai, Purusha.Prathama, Vacana.Eka), 'gacchatu');
  assert.equal(f(Lakara.Lin, Pada.Parasmai, Purusha.Prathama, Vacana.Eka), 'gacchet');
  // non-present systems keep the bare gam- stem
  assert.equal(f(Lakara.LatN, Pada.Parasmai, Purusha.Prathama, Vacana.Eka), 'agamat');
  assert.equal(f(Lakara.Lrt, Pada.Parasmai, Purusha.Prathama, Vacana.Eka), 'gamizyati');
  // the governing sūtra is emitted in the trace
  assert.ok(deriveTinantas({ ...baseArgs, dhatu: 'gam' })[0].history.some((h) => h.rule.includes('7.3.77')));
});

test('√vac present/aorist forms (vakti, vacanti, avocat)', () => {
  const f = (d: string, lakara: Lakara, pu: Purusha, v: Vacana) =>
    deriveTinantas({ ...baseArgs, dhatu: d, lakara, purusha: pu, vacana: v })[0].text();
  for (const root of ['vac', 'vach']) {
    assert.equal(f(root, Lakara.Lat, Purusha.Prathama, Vacana.Eka), 'vakti');    // vakti
    assert.equal(f(root, Lakara.Lat, Purusha.Madhyama, Vacana.Eka), 'vakzi');   // vakṣi
    assert.equal(f(root, Lakara.Lat, Purusha.Prathama, Vacana.Bahu), 'vacanti'); // vacanti
    assert.equal(f(root, Lakara.LatN, Purusha.Prathama, Vacana.Eka), 'avocat'); // avocat
  }
  assert.ok(deriveTinantas({ ...baseArgs, dhatu: 'vac' })[0].history
    .some((h) => h.rule.includes('8.2.30')));
});

test('√vac kṛt forms: uktvā/ukta but vaktum/vaktavya', () => {
  assert.equal(deriveKrdantas({ dhatu: 'vac', krt: Krt.KtvA })[0].text(), 'uktvA');
  assert.equal(deriveKrdantas({ dhatu: 'vac', krt: Krt.Tac })[0].text(), 'ukta');
  assert.equal(deriveKrdantas({ dhatu: 'vac', krt: Krt.Tum })[0].text(), 'vaktum');
  assert.equal(deriveKrdantas({ dhatu: 'vac', krt: Krt.Tavya })[0].text(), 'vaktavya');
});

test('√han weak stem ghn- in the 3rd-person plural', () => {
  const f = (lakara: Lakara) => deriveTinantas({
    ...baseArgs, dhatu: 'han', lakara, purusha: Purusha.Prathama, vacana: Vacana.Bahu,
  })[0].text();
  assert.equal(f(Lakara.Lat), 'ghnanti');  // ghnanti (not *hananti)
  assert.equal(f(Lakara.Lan), 'aghnan');   // aghnan
  assert.equal(f(Lakara.Lot), 'ghnantu');  // ghnantu
  assert.equal(deriveTinantas({ ...baseArgs, dhatu: 'han',
    purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text(), 'hanti'); // strong stem retained
});

test('√i (2P) weak-stem paradigms: itaH/ithaH/ivaH, Et, iyAt', () => {
  const f = (lakara: Lakara, pada: Pada, pu: Purusha, v: Vacana) =>
    deriveTinantas({ ...baseArgs, dhatu: 'i', lakara, pada, purusha: pu, vacana: v })[0].text();
  // weak stem in the dual/plural, guṇa e- in the strong singular
  assert.equal(f(Lakara.Lat, Pada.Parasmai, Purusha.Prathama, Vacana.Dvi), 'itaH');   // itah
  assert.equal(f(Lakara.Lat, Pada.Parasmai, Purusha.Madhyama, Vacana.Bahu), 'itha');  // itha
  assert.equal(f(Lakara.Lat, Pada.Parasmai, Purusha.Uttama, Vacana.Dvi), 'ivaH');    // ivah
  assert.equal(f(Lakara.Lat, Pada.Parasmai, Purusha.Prathama, Vacana.Bahu), 'yAnti'); // yanti
  assert.equal(f(Lakara.Lan, Pada.Parasmai, Purusha.Prathama, Vacana.Eka), 'Et');     // ait
  assert.equal(f(Lakara.Lin, Pada.Parasmai, Purusha.Prathama, Vacana.Eka), 'iyAt');   // iyat
  assert.equal(f(Lakara.Lot, Pada.Parasmai, Purusha.Madhyama, Vacana.Eka), 'ehi');    // ehi (come)
  assert.equal(f(Lakara.Lat, Pada.Atmane, Purusha.Prathama, Vacana.Eka), 'ite');     // ite
});

test('√ad (2P) athematic present: atti/adanti (not *adati)', () => {
  const f = (lakara: Lakara, pu: Purusha, v: Vacana) =>
    deriveTinantas({ ...baseArgs, dhatu: 'ad', lakara, purusha: pu, vacana: v })[0].text();
  assert.equal(f(Lakara.Lat, Purusha.Prathama, Vacana.Eka), 'atti');    // atti
  assert.equal(f(Lakara.Lat, Purusha.Prathama, Vacana.Bahu), 'adanti'); // adanti
  assert.equal(f(Lakara.Lat, Purusha.Madhyama, Vacana.Eka), 'atsi');    // atsi
  assert.equal(f(Lakara.Lat, Purusha.Uttama, Vacana.Eka), 'admi');      // admi
  assert.equal(f(Lakara.Lan, Purusha.Prathama, Vacana.Eka), 'Adat');    // ādat
  assert.equal(f(Lakara.Lin, Purusha.Prathama, Vacana.Eka), 'adyAt');   // adyāt
  assert.equal(f(Lakara.Lot, Purusha.Prathama, Vacana.Eka), 'attu');    // attu
});

test('√dviṣ (2P) athematic present: dveṣṭi/adveṭ/dviṣyāt', () => {
  const f = (lakara: Lakara, pada: Pada, pu: Purusha, v: Vacana) =>
    deriveTinantas({ ...baseArgs, dhatu: 'dviS', lakara, pada, purusha: pu, vacana: v })[0].text();
  assert.equal(f(Lakara.Lat, Pada.Parasmai, Purusha.Prathama, Vacana.Eka), 'dvezTi');  // dveṣṭi
  assert.equal(f(Lakara.Lat, Pada.Parasmai, Purusha.Prathama, Vacana.Bahu), 'dviSanti'); // dviṣanti
  assert.equal(f(Lakara.Lat, Pada.Parasmai, Purusha.Madhyama, Vacana.Eka), 'dvezXi'); // dvekṣi
  assert.equal(f(Lakara.Lat, Pada.Atmane, Purusha.Prathama, Vacana.Eka), 'dviSTe');  // dviṣṭe
  assert.equal(f(Lakara.Lan, Pada.Parasmai, Purusha.Prathama, Vacana.Eka), 'advET');   // adveṭ
  assert.equal(f(Lakara.Lin, Pada.Parasmai, Purusha.Prathama, Vacana.Eka), 'dviSyAt'); // dviṣyāt
  assert.equal(f(Lakara.Lot, Pada.Parasmai, Purusha.Madhyama, Vacana.Eka), 'dviDDi');  // dviḍḍhi
});

test('√ad kṛt forms: attvā/attum/anna (8.4.55)', () => {
  assert.equal(deriveKrdantas({ dhatu: 'ad', krt: Krt.KtvA })[0].text(), 'attvA');
  assert.equal(deriveKrdantas({ dhatu: 'ad', krt: Krt.Tum })[0].text(), 'attum');
  assert.equal(deriveKrdantas({ dhatu: 'ad', krt: Krt.Tavya })[0].text(), 'attavyam');
  assert.equal(deriveKrdantas({ dhatu: 'ad', krt: Krt.Tac })[0].text(), 'anna');
  assert.equal(deriveKrdantas({ dhatu: 'ad', krt: Krt.Ktavatu })[0].text(), 'annavAn');
});

test('√grah (9P) gṛhṇā- present: gfhRAti/gfhRanti (not *grahati)', () => {
  const f = (lakara: Lakara, pada: Pada, pu: Purusha, v: Vacana) =>
    deriveTinantas({ ...baseArgs, dhatu: 'grah', lakara, pada, purusha: pu, vacana: v })[0].text();
  assert.equal(f(Lakara.Lat, Pada.Parasmai, Purusha.Prathama, Vacana.Eka), 'gfhRAti');  // gṛhṇāti
  assert.equal(f(Lakara.Lat, Pada.Parasmai, Purusha.Prathama, Vacana.Bahu), 'gfhRanti'); // gṛhṇanti
  assert.equal(f(Lakara.Lat, Pada.Atmane, Purusha.Prathama, Vacana.Eka), 'gfhRIte'); // gṛhṇīte
  assert.equal(f(Lakara.Lan, Pada.Parasmai, Purusha.Prathama, Vacana.Eka), 'agfhRAt');  // agṛhṇāt
  assert.equal(f(Lakara.Lin, Pada.Parasmai, Purusha.Prathama, Vacana.Eka), 'gfhRIyAt'); // gṛhṇīyāt
  assert.equal(f(Lakara.Lrt, Pada.Parasmai, Purusha.Prathama, Vacana.Eka), 'grAhIzyati'); // grāhīṣyati
});

test('√grah/√jñā verbal nouns and jñā present (jānāti)', () => {
  const f = (d: string, k: Krt) => deriveKrdantas({ dhatu: d, krt: k })[0].text();
  assert.equal(f('grah', Krt.KtvA), 'gfhitvA');    // gṛhītvā
  assert.equal(f('grah', Krt.Tac), 'gfhita');      // gṛhīta
  assert.equal(f('grah', Krt.Tum), 'gfhItum');     // gṛhītum
  assert.equal(f('jFnA', Krt.KtvA), 'jFAtvA');     // jñātvā
  assert.equal(f('jFnA', Krt.Tac), 'jFAta');       // jñāta
  assert.equal(deriveTinantas({ ...baseArgs, dhatu: 'jFnA',
    purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text(), 'jAnAti'); // jānāti
});

test('√vid (2P “know”) athematic: vetti/vidanti (not *vidati)', () => {
  const f = (lakara: Lakara, pu: Purusha, v: Vacana) =>
    deriveTinantas({ ...baseArgs, dhatu: 'vid', lakara, purusha: pu, vacana: v })[0].text();
  assert.equal(f(Lakara.Lat, Purusha.Prathama, Vacana.Eka), 'vetti');    // vetti
  assert.equal(f(Lakara.Lat, Purusha.Prathama, Vacana.Bahu), 'vidanti'); // vidanti
  assert.equal(f(Lakara.Lat, Purusha.Madhyama, Vacana.Eka), 'vetsi');    // vetsi
  assert.equal(f(Lakara.Lat, Purusha.Uttama, Vacana.Eka), 'vedmi');      // vedmi
  assert.equal(f(Lakara.Lan, Purusha.Prathama, Vacana.Eka), 'avet');     // avet
  assert.equal(f(Lakara.Lin, Purusha.Prathama, Vacana.Eka), 'vidyAt');   // vidyāt
  assert.equal(f(Lakara.Lit, Purusha.Prathama, Vacana.Eka), 'veda');     // veda
});

test('√iṣ (2P) athematic: eṣṭi/iṣanti (not *iṣati)', () => {
  const f = (lakara: Lakara, pada: Pada, pu: Purusha, v: Vacana) =>
    deriveTinantas({ ...baseArgs, dhatu: 'iS', lakara, pada, purusha: pu, vacana: v })[0].text();
  assert.equal(f(Lakara.Lat, Pada.Parasmai, Purusha.Prathama, Vacana.Eka), 'ezTi');   // eṣṭi
  assert.equal(f(Lakara.Lat, Pada.Parasmai, Purusha.Prathama, Vacana.Bahu), 'iSanti'); // iṣanti
  assert.equal(f(Lakara.Lat, Pada.Parasmai, Purusha.Madhyama, Vacana.Eka), 'ekzi');  // ekṣi
  assert.equal(f(Lakara.Lat, Pada.Atmane, Purusha.Prathama, Vacana.Eka), 'izTe');    // iṣṭe
  assert.equal(f(Lakara.Lan, Pada.Parasmai, Purusha.Prathama, Vacana.Eka), 'ET');    // aiṭ
  assert.equal(f(Lakara.Lin, Pada.Parasmai, Purusha.Prathama, Vacana.Eka), 'iSyAt'); // iṣyāt
  assert.equal(f(Lakara.Lrt, Pada.Parasmai, Purusha.Prathama, Vacana.Eka), 'eziSyati'); // eṣiṣyati
});

test('√mṛj (2P) athematic: mārṣṭi/mṛjanti (not *mṛjati)', () => {
  const f = (lakara: Lakara, pu: Purusha, v: Vacana) =>
    deriveTinantas({ ...baseArgs, dhatu: 'mfz', lakara, purusha: pu, vacana: v })[0].text();
  assert.equal(f(Lakara.Lat, Purusha.Prathama, Vacana.Eka), 'mArzTi');   // mārṣṭi
  assert.equal(f(Lakara.Lat, Purusha.Prathama, Vacana.Bahu), 'mfjanti'); // mṛjanti
  assert.equal(f(Lakara.Lat, Purusha.Madhyama, Vacana.Eka), 'mArkzi');  // mārkṣi
  assert.equal(f(Lakara.Lat, Purusha.Uttama, Vacana.Eka), 'mArjmi');    // mārjmi
  assert.equal(f(Lakara.Lan, Purusha.Prathama, Vacana.Eka), 'amArT');   // amārṭ
  assert.equal(f(Lakara.Lin, Purusha.Prathama, Vacana.Eka), 'mfjyAt');  // mṛjyāt
  assert.equal(f(Lakara.Lrt, Purusha.Prathama, Vacana.Eka), 'mArjizyati'); // mārjiṣyati
});

test('√pā/√sthā present stems pib-/tiṣṭh- and iṭ-less futures', () => {
  const f = (d: string, lakara: Lakara) =>
    deriveTinantas({ ...baseArgs, dhatu: d, lakara,
      purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text();
  assert.equal(f('pA', Lakara.Lat), 'pibati');    // pibati (not *pāti)
  assert.equal(f('pA', Lakara.Lan), 'apibat');    // apibat
  assert.equal(f('pA', Lakara.Lin), 'pibet');     // pibet
  assert.equal(f('pA', Lakara.Lrt), 'pAsyati');   // pāsyati (no iṭ)
  assert.equal(f('sTA', Lakara.Lat), 'tiSThati'); // tiṣṭhati (not *sthāti)
  assert.equal(f('sTA', Lakara.Lan), 'atiSThat'); // atiṣṭhat
  assert.equal(f('sTA', Lakara.Lrt), 'sTAsyati'); // sthāsyati (no iṭ)
});

test('√ṛ (1P) ṛcch- present, ariṣya future, āra perfect, ārat aorist', () => {
  const f = (lakara: Lakara) =>
    deriveTinantas({ ...baseArgs, dhatu: 'fR', lakara,
      purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text();
  assert.equal(f(Lakara.Lat), 'fcCati');  // ṛcchati (not *ṛati)
  assert.equal(f(Lakara.Lan), 'AfcCat');  // ārcchat
  assert.equal(f(Lakara.Lot), 'fcCatu');  // ṛcchatu
  assert.equal(f(Lakara.Lin), 'fcCet');   // ṛcchet
  assert.equal(f(Lakara.Lrt), 'arizyati'); // ariṣyati
  assert.equal(f(Lakara.Lit), 'ara');     // āra
  assert.equal(f(Lakara.LatN), 'Arat');  // ārat
});

test('present-participle stems from present stems; vidvān', () => {
  const satr = (d: string) => deriveKrdantas({ dhatu: d, krt: Krt.Satr })[0].text();
  assert.equal(satr('gam'), 'gacchat');  // gacchat (not *gamat)
  assert.equal(satr('pA'), 'pibat');     // pibat (not *pāt)
  assert.equal(satr('sTA'), 'tiSThat');  // tiṣṭhat (not *sthāt)
  assert.equal(satr('grah'), 'gfhRat');  // gṛhṇat
  assert.equal(satr('jFnA'), 'jAnat');   // jānat
  assert.equal(deriveKrdantas({ dhatu: 'vid', krt: Krt.Ktavatu })[0].text(), 'vidvAn'); // vidvān
});

test('causative (ṇic) stems for corrected roots', () => {
  const nic = (d: string) => deriveTinantas({ ...baseArgs, dhatu: d,
    sanadi: Sanadi.Nic, purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text();
  assert.equal(nic('ad'), 'Adayati');    // ādayati
  assert.equal(nic('dviS'), 'dvezayati'); // dveṣayati
  assert.equal(nic('vac'), 'vAcayati');   // vācayati
  assert.equal(nic('grah'), 'grAhayati'); // grāhayati
  assert.equal(nic('jFnA'), 'jFApayati'); // jñāpayati
  assert.equal(nic('pA'), 'pAyayati');    // pāyayati
  assert.equal(nic('sTA'), 'sTApayati');  // sthāpayati
  assert.equal(nic('fR'), 'arpayati');    // arpayati
});

test('desiderative (san) stems for corrected roots', () => {
  const san = (d: string) => deriveTinantas({ ...baseArgs, dhatu: d,
    sanadi: Sanadi.San, purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text();
  assert.equal(san('dviS'), 'dvivizati');  // dviviṣati
  assert.equal(san('vac'), 'vivakzati');   // vivakṣati
  assert.equal(san('grah'), 'jigfkzati');  // jighṛkṣati
  assert.equal(san('jFnA'), 'jijFAsati');  // jijñāsati
  assert.equal(san('sTA'), 'tiSThAsati');  // tiṣṭhāsati
  assert.equal(san('fR'), 'aririzati');    // aririṣati
});

test('√jñā/√dviṣ aorist, future, perfect from conjugation source', () => {
  const f = (d: string, lk: Lakara) =>
    deriveTinantas({ ...baseArgs, dhatu: d, lakara: lk,
      purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text();
  assert.equal(f('jFnA', Lakara.LatN), 'ajFAsIt');  // ajñāsīt
  assert.equal(f('jFnA', Lakara.Lrt), 'jFAsyati');  // jñāsyati
  assert.equal(f('jFnA', Lakara.Lit), 'jajFau');    // jajñau
  assert.equal(f('dviS', Lakara.LatN), 'advikzat'); // adviKṣat
  assert.equal(f('dviS', Lakara.Lit), 'didveza');   // didveṣa
});

test('√grah aorist/perfect: ajigrahat/jagrāha', () => {
  const f = (lk: Lakara) => deriveTinantas({ ...baseArgs, dhatu: 'grah', lakara: lk,
    purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text();
  assert.equal(f(Lakara.LatN), 'ajigrahat'); // ajigrahat
  assert.equal(f(Lakara.Lit), 'jagrAha');    // jagrāha
});

test('√iṣ/√mṛj aorist and mṛj desiderative (Wiktionary)', () => {
  const f = (d: string, lk: Lakara) => deriveTinantas({ ...baseArgs, dhatu: d, lakara: lk,
    purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text();
  assert.equal(f('iS', Lakara.LatN), 'EzIt');       // aiṣīt
  assert.equal(f('mfz', Lakara.LatN), 'amArkzIt');  // amārkṣīt
  assert.equal(deriveTinantas({ ...baseArgs, dhatu: 'mfz', sanadi: Sanadi.San,
    purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text(), 'mimArjizati'); // mimārjiṣati
});

test('high-frequency aorists: yaj/han/dhā/hu', () => {
  const f = (d: string) => deriveTinantas({ ...baseArgs, dhatu: d, lakara: Lakara.LatN,
    purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text();
  assert.equal(f('yaj'), 'ayAkzIt'); // ayākṣīt
  assert.equal(f('han'), 'ahAnIt');  // ahānīt
  assert.equal(f('DA'), 'aDAt');     // adhāt
  assert.equal(f('hu'), 'ahOzIt');   // ahauṣīt
});

test('special past participles/gerunds: pīta, hitvā, sthita, labdha', () => {
  const f = (d: string, k: Krt) => deriveKrdantas({ dhatu: d, krt: k })[0].text();
  assert.equal(f('pA', Krt.Tac), 'pIta');    // pīta
  assert.equal(f('pA', Krt.KtvA), 'pItvA');  // pītvā
  assert.equal(f('DA', Krt.KtvA), 'hitvA');  // hitvā
  assert.equal(f('sTA', Krt.Tac), 'sTita');  // sthita
  assert.equal(f('lab', Krt.Tac), 'labDa');  // labdha
  assert.equal(f('lab', Krt.KtvA), 'labDvA'); // labdhvā
});

test('caste-name feminines: brāhmaṇī but kṣatriyā/vaiśyā/śūdrā', () => {
  assert.equal(deriveStri({ stem: 'brAhmaRa' })?.text(), 'brAhmaRI'); // brāhmaṇī
  assert.equal(deriveStri({ stem: 'kzatriya' })?.text(), 'kzatriyA'); // kṣatriyā
  assert.equal(deriveStri({ stem: 'vaiSya' })?.text(), 'vaiSyA');     // vaiśyā
  assert.equal(deriveStri({ stem: 'sUdra' })?.text(), 'sUdrA');       // śūdrā
});

test('√ad agent noun attṛ', () => {
  assert.equal(deriveKrdantas({ dhatu: 'ad', krt: Krt.TRn })[0].text(), 'attf'); // attṛ
});

test('athematic optatives: bhindyāt/rundhyāt/duhyāt/śṛṇuyāt', () => {
  const lin = (d: string) => deriveTinantas({ ...baseArgs, dhatu: d, lakara: Lakara.Lin,
    purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text();
  assert.equal(lin('bhid'), 'bhinDyAt');  // bhindyāt
  assert.equal(lin('rudh'), 'runDyAt');   // rundhyāt
  assert.equal(lin('duh'), 'duhyAt');     // duhyāt
  assert.equal(lin('zru'), 'zRuNuyAt');   // śṛṇuyāt
});

test('athematic imperative 3s: bhinattu/śṛṇotu/vaktu/rundhatu', () => {
  const lot = (d: string) => deriveTinantas({ ...baseArgs, dhatu: d, lakara: Lakara.Lot,
    purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text();
  assert.equal(lot('bhid'), 'bhinattu');  // bhinattu
  assert.equal(lot('zru'), 'zRNotu');     // śṛṇotu
  assert.equal(lot('vac'), 'vaktu');      // vaktu
  assert.equal(lot('rudh'), 'rundhatu');  // rundhatu
});

test('√śru imperfect/future without iṭ: aśṛṇot/śroṣyati', () => {
  const f = (lk: Lakara) => deriveTinantas({ ...baseArgs, dhatu: 'zru', lakara: lk,
    purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text();
  assert.equal(f(Lakara.Lan), 'azRNot');   // aśṛṇot
  assert.equal(f(Lakara.Lrt), 'zrOzyati'); // śroṣyati (no iṭ)
});

test('iṭ-less futures neṣyati/jeṣyati', () => {
  const lrt = (d: string) => deriveTinantas({ ...baseArgs, dhatu: d, lakara: Lakara.Lrt,
    purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text();
  assert.equal(lrt('nI'), 'nezyati'); // neṣyati
  assert.equal(lrt('ji'), 'jezyati'); // jeṣyati
});

test('√muc future mokṣyati', () => {
  assert.equal(deriveTinantas({ ...baseArgs, dhatu: 'muc', lakara: Lakara.Lrt,
    purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text(), 'mokzyati'); // mokṣyati
});

test('√rudh future rotsyati', () => {
  assert.equal(deriveTinantas({ ...baseArgs, dhatu: 'rudh', lakara: Lakara.Lrt,
    purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text(), 'rotsyati'); // rotsyati
});

test('iṭ-less futures for ñit-marked roots: ceṣyati/soṣyati/śeṣyati', () => {
  const lrt = (d: string) => deriveTinantas({ ...baseArgs, dhatu: d, lakara: Lakara.Lrt,
    purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text();
  assert.equal(lrt('ciY'), 'cezyati'); // ceṣyati
  assert.equal(lrt('zuY'), 'sozyati'); // soṣyati
  assert.equal(lrt('SiY'), 'Sezyati'); // śeṣyati
});

test('8.4.2 interveners: prabhunā (not *prabhuṇā), guruṇā, taruṇā', () => {
  const inst = (w: string) => deriveSubantas({ pratipadika: w, linga: Linga.Pumsaka,
    vibhakti: Vibhakti.Trtiya, vacana: Vacana.Eka })[0].text();
  assert.equal(inst('guru'), 'guruRA');   // guruṇā (r directly before u)
  assert.equal(inst('prabhu'), 'prabhunA'); // prabhunā (b blocks ṇatva)
  assert.equal(inst('taru'), 'taruRA');   // taruṇā (r before u)
  assert.equal(inst('madhu'), 'madhunA'); // madhunā (no r)
});

test('lyuṭ action nouns ayana/jayana/jñāna', () => {
  const lyuT = (d: string) => deriveKrdantas({ dhatu: d, krt: Krt.LyuT })[0].text();
  assert.equal(lyuT('i'), 'ayana');   // ayana
  assert.equal(lyuT('ji'), 'jayana'); // jayana
  assert.equal(lyuT('jFnA'), 'jFAna'); // jñāna
});

test('u-stem genitive plural: gurūṇām but prabhūnām/madhūnām', () => {
  const gen = (w: string) => deriveSubantas({ pratipadika: w, linga: Linga.Pumsaka,
    vibhakti: Vibhakti.Sasti, vacana: Vacana.Bahu })[0].text();
  assert.equal(gen('guru'), 'gurURAm');   // gurūṇām (r trigger)
  assert.equal(gen('prabhu'), 'prabhUnAm'); // prabhūnām (no trigger)
  assert.equal(gen('madhu'), 'madhUnAm'); // madhūnām
});

test('ṛ-stem accusative plural pitṝn/kartṝn', () => {
  const acc = (w: string) => deriveSubantas({ pratipadika: w, linga: Linga.Pumsaka,
    vibhakti: Vibhakti.Dvitiya, vacana: Vacana.Bahu })[0].text();
  assert.equal(acc('pitf'), 'pitFn');  // pitṝn
  assert.equal(acc('kartf'), 'kartFn'); // kartṝn
});

test('an-n instrumental ṇatva: karmaṇā but nāmnā', () => {
  const inst = (w: string) => deriveSubantas({ pratipadika: w, linga: Linga.Napumsaka,
    vibhakti: Vibhakti.Trtiya, vacana: Vacana.Eka })[0].text();
  assert.equal(inst('karman'), 'karmRA'); // karmaṇā (r + m intervenes)
  assert.equal(inst('nAman'), 'nAmnA');   // nāmnā (no r trigger)
});

test('√śru verbal nouns: śrotum/śrotavya/śrotṛ (no extra iṭ)', () => {
  const f = (k: Krt) => deriveKrdantas({ dhatu: 'zru', krt: k })[0].text();
  assert.equal(f(Krt.Tum), 'zrOtum');     // śrotum
  assert.equal(f(Krt.Tavya), 'zrOtavya'); // śrotavya
  assert.equal(f(Krt.Tfc), 'zrOtf');      // śrotṛ
});

test('√labh verbal nouns: labdhum/labdhavya/labdhi/lābha', () => {
  const f = (k: Krt) => deriveKrdantas({ dhatu: 'lab', krt: k })[0].text();
  assert.equal(f(Krt.Tum), 'labDum');       // labdhum
  assert.equal(f(Krt.Tavya), 'labDavyam'); // labdhavyam
  assert.equal(f(Krt.Tfc), 'labDf');       // labdhṛ
  assert.equal(f(Krt.Ktin), 'labDi');      // labdhi
  assert.equal(f(Krt.ghaH), 'lABa');       // lābha
});

test('√labh ktavatu labdhavān', () => {
  assert.equal(deriveKrdantas({ dhatu: 'lab', krt: Krt.Ktavatu })[0].text(), 'labDavAn'); // labdhavān
});

test('anīyar gerundives jñānīya/ayanīya/jayanīya', () => {
  const ani = (d: string) => deriveKrdantas({ dhatu: d, krt: Krt.Ani })[0].text();
  assert.equal(ani('jFnA'), 'jFAnIya'); // jñānīya
  assert.equal(ani('i'), 'ayanIya');    // ayanīya
  assert.equal(ani('ji'), 'jayanIya');  // jayanīya
});

test('ghaH action nouns dāna/dhāna/jñāna/śravaṇa', () => {
  const ghaH = (d: string) => deriveKrdantas({ dhatu: d, krt: Krt.ghaH })[0].text();
  assert.equal(ghaH('dA'), 'dAna');    // dāna
  assert.equal(ghaH('DA'), 'dAna');    // dhāna
  assert.equal(ghaH('jFnA'), 'jFAna'); // jñāna
  assert.equal(ghaH('zru'), 'zravaRa'); // śravaṇa
});

test('passives jñāyate/śrūyate', () => {
  const pass = (d: string) => deriveTinantas({ ...baseArgs, dhatu: d,
    prayoga: Prayoga.Karmani, purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text();
  assert.equal(pass('jFnA'), 'jFAyate'); // jñāyate
  assert.equal(pass('zru'), 'zrUyate');  // śrūyate
});

test('passive gṛhyate', () => {
  assert.equal(deriveTinantas({ ...baseArgs, dhatu: 'grah', prayoga: Prayoga.Karmani,
    purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text(), 'gfhyate'); // gṛhyate
});

test('bhāve (impersonal) gṛhyate/jñāyate/śrūyate', () => {
  const bh = (d: string) => deriveTinantas({ ...baseArgs, dhatu: d,
    prayoga: Prayoga.Bhave, purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text();
  assert.equal(bh('grah'), 'gfhyate'); // gṛhyate
  assert.equal(bh('jFnA'), 'jFAyate'); // jñāyate
  assert.equal(bh('zru'), 'zrUyate');  // śrūyate
});

test('ṇini agent nouns jñāyin/jayin', () => {
  const nini = (d: string) => deriveKrdantas({ dhatu: d, krt: Krt.Nini })[0].text();
  assert.equal(nini('jFnA'), 'jFAyin'); // jñāyin
  assert.equal(nini('ji'), 'jayin');    // jayin
});

test('√jñā tṛn agent noun jñātṛ', () => {
  assert.equal(deriveKrdantas({ dhatu: 'jFnA', krt: Krt.TRn })[0].text(), 'jFAtf'); // jñātṛ
});

test('śatṛ from present stems: jayat/śṛṇvat/ṛcchat', () => {
  const satr = (d: string) => deriveKrdantas({ dhatu: d, krt: Krt.Satr })[0].text();
  assert.equal(satr('ji'), 'jayat');   // jayat
  assert.equal(satr('zru'), 'zRNavat'); // śṛṇvat
  assert.equal(satr('fR'), 'fcCat');   // ṛcchat
});

test('śānan participles nayamāna/jayamāna', () => {
  const s = (d: string) => deriveKrdantas({ dhatu: d, krt: Krt.Sanan })[0].text();
  assert.equal(s('nI'), 'nayamAna'); // nayamāna
  assert.equal(s('ji'), 'jayamAna'); // jayamāna
});

test('kyap kriyā', () => {
  assert.equal(deriveKrdantas({ dhatu: 'kf', krt: Krt.Kyap })[0].text(), 'kriyA'); // kriyā
});

test('śānan gṛhyamāṇa/jñāyamāna/śrūyamāna/iyamāna', () => {
  const s = (d: string) => deriveKrdantas({ dhatu: d, krt: Krt.Sanan })[0].text();
  assert.equal(s('grah'), 'gfhyamARa'); // gṛhyamāṇa
  assert.equal(s('jFnA'), 'jFAyamAna'); // jñāyamāna
  assert.equal(s('zru'), 'zrUyamARa');  // śrūyamāṇa
  assert.equal(s('i'), 'iyamAna');      // iyamāna
});

test('ṣṭran kartra/gantra/jñātra/śrotra', () => {
  const f = (d: string) => deriveKrdantas({ dhatu: d, krt: Krt.STran })[0].text();
  assert.equal(f('kf'), 'kartra');   // kartra
  assert.equal(f('gam'), 'gantra');  // gantra
  assert.equal(f('jFnA'), 'jFAtra'); // jñātra
  assert.equal(f('zru'), 'zrOtra');  // śrotra
});

test('ñit-marker roots kṛt forms (Y not part of stem)', () => {
  const f = (d: string, k: Krt) => deriveKrdantas({ dhatu: d, krt: k })[0].text();
  assert.equal(f('ciY', Krt.KtvA), 'citvA'); // citvā
  assert.equal(f('zuY', Krt.KtvA), 'sutvA'); // sutvā
  assert.equal(f('SiY', Krt.Tac), 'Sita');   // śita
  assert.equal(f('yaj', Krt.naN), 'yajYa');  // yajña (explicit override kept)
});

test('class-5 śatṛ cinvat/sunvat/śinvat/stṛṇvat', () => {
  const f = (d: string) => deriveKrdantas({ dhatu: d, krt: Krt.Satr })[0].text();
  assert.equal(f('ciY'), 'cinvat');   // cinvat
  assert.equal(f('zuY'), 'sunvat');   // sunvat
  assert.equal(f('SiY'), 'Sinvat');   // śinvat
  assert.equal(f('stfY'), 'stfRvat'); // stṛṇvat
});

test('lyuṭ cayana', () => {
  assert.equal(deriveKrdantas({ dhatu: 'ciY', krt: Krt.LyuT })[0].text(), 'cayana'); // cayana
});

test('class-5 śānan cinvamāna/sunvamāna/śinvamāna/stṛṇvamāna', () => {
  const f = (d: string) => deriveKrdantas({ dhatu: d, krt: Krt.Sanan })[0].text();
  assert.equal(f('ciY'), 'cinvamAna');   // cinvamāna
  assert.equal(f('zuY'), 'sunvamAna');   // sunvamāna
  assert.equal(f('SiY'), 'SinvamAna');   // śinvamāna
  assert.equal(f('stfY'), 'stfRvamAna'); // stṛṇvamāna
});

test('upasargas apply to aorists', () => {
  const f = (u: string, d: string) => deriveTinantas({ ...baseArgs, dhatu: d,
    lakara: Lakara.LatN, purusha: Purusha.Prathama, vacana: Vacana.Eka, upasarga: u })[0].text();
  assert.equal(f('pra', 'gam'), 'prAgamat');  // prāgamat
  assert.equal(f('sam', 'gam'), 'samagamat'); // saṃgamat
  assert.equal(f('vi', 'gam'), 'vyagamat');   // vigamat
  assert.equal(f('pra', 'BU'), 'prABUt');     // prābhūt
});

test('paradigm honours upasarga', () => {
  const p = deriveParadigm({ dhatu: 'gam', upasarga: 'pra',
    lakaras: [Lakara.Lat], padas: [Pada.Parasmai] });
  assert.equal(p.cells[0].text, 'pragacchati'); // pragacchati
});

test('ktin jñāti/śroti', () => {
  assert.equal(deriveKrdantas({ dhatu: 'jFnA', krt: Krt.Ktin })[0].text(), 'jFAti'); // jñāti
  assert.equal(deriveKrdantas({ dhatu: 'zru', krt: Krt.Ktin })[0].text(), 'zrOti');  // śroti
});

test('ṣa Feminine action nouns jñānā/śrūā/cayā/pīā/dānā/ayā/jayā', () => {
  const f = (d: string) => deriveKrdantas({ dhatu: d, krt: Krt.Sa })[0].text();
  assert.equal(f('jFnA'), 'jFAnA'); // jñānā
  assert.equal(f('zru'), 'zrUA');   // śrūā
  assert.equal(f('ciY'), 'cayA');   // cayā
  assert.equal(f('pA'), 'pIA');     // pīā
  assert.equal(f('dA'), 'dAnA');    // dānā
  assert.equal(f('i'), 'ayA');      // ayā
  assert.equal(f('ji'), 'jayA');    // jayā
});

test('yat jñānya/śroya/cayya', () => {
  const f = (d: string) => deriveKrdantas({ dhatu: d, krt: Krt.Yat })[0].text();
  assert.equal(f('jFnA'), 'jFAnya'); // jñānya
  assert.equal(f('zru'), 'zrOya');   // śroya
  assert.equal(f('ciY'), 'cayya');   // cayya
});

test('ṇvanip śrotra-vat/jñāna-vat/cayana-vat', () => {
  const f = (d: string) => deriveKrdantas({ dhatu: d, krt: Krt.Nvanip })[0].text();
  assert.equal(f('zru'), 'zrOvaR'); // śrotravān
  assert.equal(f('jFnA'), 'jFAvan'); // jñānavān
  assert.equal(f('ciY'), 'cayvan');  // cayanavān
});

test('class-5 ñit roots: no Y marker in finite forms', () => {
  const f = (d: string, lk: Lakara) => deriveTinantas({ ...baseArgs, dhatu: d, lakara: lk,
    purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text();
  assert.equal(f('ciY', Lakara.Lin), 'cinuyAt');  // cinuyāt
  assert.equal(f('ciY', Lakara.Lot), 'cinotu');   // cinotu
  assert.equal(f('ciY', Lakara.Lit), 'cikAya');   // cikāya
  assert.equal(f('zuY', Lakara.Lan), 'asunot');   // asunot
  assert.equal(f('SiY', Lakara.Lin), 'SinuyAt');  // śinuyāt
  assert.equal(f('stfY', Lakara.Lot), 'stfRnotu'); // stṛṇotu
});

test('ñit marker never leaks into finite surfaces', () => {
  const f = (d: string, lk: Lakara) => deriveTinantas({ ...baseArgs, dhatu: d, lakara: lk,
    purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text();
  assert.equal(f('ciY', Lakara.LatN), 'acAyIt'); // ācāyīt
  assert.equal(f('zuY', Lakara.LatN), 'asOzIt'); // asauṣīt
  assert.ok(!f('SiY', Lakara.LatN).includes('Y')); // no indicatory Y
  assert.ok(!f('stfY', Lakara.LatN).includes('Y'));
});

test('ñit secondary conjugations cāyayati/sāvayati/cikīṣati', () => {
  const f = (d: string, sd: Sanadi) => deriveTinantas({ ...baseArgs, dhatu: d,
    sanadi: sd, purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text();
  assert.equal(f('ciY', Sanadi.Nic), 'cayayati'); // cāyayati
  assert.equal(f('zuY', Sanadi.Nic), 'sAvayati'); // sāvayati
  assert.equal(f('ciY', Sanadi.San), 'cicizati'); // cikīṣati
  assert.equal(f('zuY', Sanadi.San), 'sisuzati'); // susūṣati
});

test('source-backed causatives dhāpayati/mocayati/eṣayati/mārjayati/lambhayati', () => {
  const nic = (d: string) => deriveTinantas({ ...baseArgs, dhatu: d,
    sanadi: Sanadi.Nic, purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text();
  assert.equal(nic('DA'), 'DApayati');  // dhāpayati
  assert.equal(nic('muc'), 'mocayati'); // mocayati
  assert.equal(nic('iS'), 'ezayati');   // eṣayati
  assert.equal(nic('mfz'), 'mArjayati'); // mārjayati
  assert.equal(nic('lab'), 'lamBayati'); // lambhayati
});

test('source-backed desideratives mumukṣati/lipsati/rurutsati', () => {
  const san = (d: string) => deriveTinantas({ ...baseArgs, dhatu: d,
    sanadi: Sanadi.San, purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text();
  assert.equal(san('muc'), 'mumukzati'); // mumukṣati
  assert.equal(san('lab'), 'lipsati');   // lipsati
  assert.equal(san('rudh'), 'rurutsati');// rurutsati
});

test('ktavatu hitavān/sthitavān/pītavān', () => {
  const f = (d: string) => deriveKrdantas({ dhatu: d, krt: Krt.Ktavatu })[0].text();
  assert.equal(f('DA'), 'hitavAn');  // hitavān
  assert.equal(f('sTA'), 'sThitavAn'); // sthitavān
  assert.equal(f('pA'), 'pItavAn');  // pītavān
});

test('śānan dāyamāna/sthātamāna/pāyamāna', () => {
  const f = (d: string) => deriveKrdantas({ dhatu: d, krt: Krt.Sanan })[0].text();
  assert.equal(f('dA'), 'dAyamAna');  // dāyamāna
  assert.equal(f('sTA'), 'sTAtamAna'); // sthātamāna
  assert.equal(f('pA'), 'pAyamAna');  // pāyamāna
});

test('śatṛ ghnat/aDat', () => {
  assert.equal(deriveKrdantas({ dhatu: 'han', krt: Krt.Satr })[0].text(), 'ghnat'); // ghnat
  assert.equal(deriveKrdantas({ dhatu: 'adh', krt: Krt.Satr })[0].text(), 'aDat');  // adhat
});

test('śānan hanamāna/daśdamāna', () => {
  assert.equal(deriveKrdantas({ dhatu: 'han', krt: Krt.Sanan })[0].text(), 'hanamAna'); // hanamāna
  assert.equal(deriveKrdantas({ dhatu: 'DA', krt: Krt.Sanan })[0].text(), 'daDamAna');  // dadhamāna
});

test('ṇini dāpin/ādin/vācin/eṣṭṛ/mārjin', () => {
  const f = (d: string) => deriveKrdantas({ dhatu: d, krt: Krt.Nini })[0].text();
  assert.equal(f('DA'), 'dApin');   // dāpin
  assert.equal(f('ad'), 'Adin');    // ādin
  assert.equal(f('vac'), 'vAcin');  // vācin
  assert.equal(f('iS'), 'eziR');    // eṣṭṛ
  assert.equal(f('mfz'), 'mArjin'); // mārjin
});

test('tṛn dadhṛ/gṛhītṛ/śrotṛ/eṣṭṛ/pūjā', () => {
  const f = (d: string) => deriveKrdantas({ dhatu: d, krt: Krt.TRn })[0].text();
  assert.equal(f('DA'), 'daDtf');   // dadhṛ
  assert.equal(f('grah'), 'gfhItf'); // gṛhītṛ
  assert.equal(f('zru'), 'zrOtf');   // śrotṛ
  assert.equal(f('iS'), 'ezwf');     // eṣṭṛ
});

test('tṛc dadhṛ/eṣṭṛ/mārjṭṛ/hantṛ', () => {
  const f = (d: string) => deriveKrdantas({ dhatu: d, krt: Krt.Tfc })[0].text();
  assert.equal(f('DA'), 'daDtf');   // dadhṛ
  assert.equal(f('iS'), 'ezwf');    // eṣṭṛ
  assert.equal(f('mfz'), 'mArgtf'); // mārjṭṛ
  assert.equal(f('han'), 'hantf');  // hantṛ
});

test('infinitives dhātum/sthātum', () => {
  assert.equal(deriveKrdantas({ dhatu: 'DA', krt: Krt.Tum })[0].text(), 'DAtum'); // dhātum
  assert.equal(deriveKrdantas({ dhatu: 'sTA', krt: Krt.Tum })[0].text(), 'sTAtum'); // sthātum
});

test('gerundives dhātavya/sthātavya/pātavya', () => {
  const f = (d: string) => deriveKrdantas({ dhatu: d, krt: Krt.Tavya })[0].text();
  assert.equal(f('DA'), 'DAtavya');  // dhātavya
  assert.equal(f('sTA'), 'sTAtavya'); // sthātavya
  assert.equal(f('pA'), 'pAtavya');  // pātavya
});

test('ktvā vitvā/bitvā/rudhvā', () => {
  const f = (d: string) => deriveKrdantas({ dhatu: d, krt: Krt.KtvA })[0].text();
  assert.equal(f('vid'), 'vitvA');  // vitvā
  assert.equal(f('bhid'), 'bitvA'); // bitvā
  assert.equal(f('rudh'), 'rudvA'); // rudhvā
});

test('lyuṭ dhāna/sthāna/pāna/eṣaṇa/mārjana', () => {
  const f = (d: string) => deriveKrdantas({ dhatu: d, krt: Krt.LyuT })[0].text();
  assert.equal(f('DA'), 'DAna');   // dhāna
  assert.equal(f('sTA'), 'sTAna'); // sthāna
  assert.equal(f('pA'), 'pAna');   // pāna
  assert.equal(f('iS'), 'ezaRa');  // eṣaṇa
  assert.equal(f('mfz'), 'mArjana'); // mārjana
});

test('ghaH bheda/śravaṇa', () => {
  assert.equal(deriveKrdantas({ dhatu: 'bhid', krt: Krt.ghaH })[0].text(), 'Bheda'); // bheda
  assert.equal(deriveKrdantas({ dhatu: 'zru', krt: Krt.ghaH })[0].text(), 'zravaRa'); // śravaṇa
});

test('ṣa dhānā/sthānā/vidā/eṣā/mārjā/lābhā', () => {
  const f = (d: string) => deriveKrdantas({ dhatu: d, krt: Krt.Sa })[0].text();
  assert.equal(f('DA'), 'DAnA');  // dhānā
  assert.equal(f('sTA'), 'sTAnA'); // sthānā
  assert.equal(f('vid'), 'vidA');  // vidā
  assert.equal(f('iS'), 'ezA');    // eṣā
  assert.equal(f('mfz'), 'mArjA'); // mārjā
  assert.equal(f('lab'), 'lABA');  // lābhā
});

test('passives dīyate/sthīyate/pīyate', () => {
  const f = (d: string) => deriveTinantas({ ...baseArgs, dhatu: d,
    prayoga: Prayoga.Karmani, purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text();
  assert.equal(f('DA'), 'dIyate');   // dīyate
  assert.equal(f('pA'), 'pIyate');   // pīyate
  assert.equal(f('sTA'), 'sTIyate');   // sthīyate (not *sthātyate)
});

test('passive non-present lakāras use the ordinary lakāra stem', () => {
  const f = (d: string, lk: Lakara) => deriveTinantas({ ...baseArgs, dhatu: d,
    prayoga: Prayoga.Karmani, lakara: lk,
    purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text();
  assert.equal(f('pac', Lakara.Lrt), 'pakzyate');  // paksyate (not *pacte)
  assert.equal(f('BU', Lakara.Lrt), 'Bavizyate');  // bhavisyate (not *Bavte)
  assert.equal(f('kf', Lakara.Lrt), 'karizyate');  // karisyate
  assert.equal(f('pac', Lakara.Lit), 'papace');    // papāce
  assert.equal(f('pac', Lakara.Lng), 'apakzyata'); // apaksyata
  // Present-system yak is unaffected.
  assert.equal(f('pac', Lakara.Lat), 'pacyate');
  assert.equal(f('pac', Lakara.Lan), 'apacyata');
});

test('perfect middle (karmani) of ā-final roots uses the weak stem', () => {
  const f = (d: string, p: Purusha = Purusha.Prathama, v: Vacana = Vacana.Eka) =>
    deriveTinantas({ ...baseArgs, dhatu: d, prayoga: Prayoga.Karmani,
      lakara: Lakara.Lit, purusha: p, vacana: v })[0].text();
  assert.equal(f('DA'), 'dadhe');   // dadhé (not *dadhaue)
  assert.equal(f('pA'), 'pape');    // papé (not *papaue)
  assert.equal(f('sTA'), 'tasthe'); // tasthé
  assert.equal(f('dA'), 'dade');    // dade
  assert.equal(f('jFnA'), 'jajFe'); // jajñé
  assert.equal(f('dA', Purusha.Madhyama), 'dadize'); // dadiṣé
  assert.equal(f('jFnA', Purusha.Prathama, Vacana.Bahu), 'jajFire'); // jajñiré
  // Parasmai strong au forms remain intact.
  const par = (d: string) => deriveTinantas({ ...baseArgs, dhatu: d,
    lakara: Lakara.Lit, purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text();
  assert.equal(par('DA'), 'daDO');  // dadháu
  assert.equal(par('pA'), 'papO');  // papáu
});

test('bhāve (impersonal) honours lakāra but stays 3s', () => {
  const f = (lk: Lakara) => deriveTinantas({ ...baseArgs, dhatu: 'pac',
    prayoga: Prayoga.Bhave, lakara: lk,
    purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text();
  assert.equal(f(Lakara.Lat), 'pacyate');
  assert.equal(f(Lakara.Lan), 'apacyata');
  assert.equal(f(Lakara.Lot), 'pacyatAm');
  assert.equal(f(Lakara.Lin), 'pacyeta');
  assert.equal(f(Lakara.Lrt), 'pakzyate');
  // Impersonal: purusha/vacana are forced to 3s eka.
  assert.equal(deriveTinantas({ ...baseArgs, dhatu: 'pac', prayoga: Prayoga.Bhave,
    purusha: Purusha.Madhyama, vacana: Vacana.Bahu })[0].text(), 'pacyate');
});

test('passive aorists (karmani/bhāve) use ātmane and special 3s forms', () => {
  const f = (d: string, pr: Prayoga) => deriveTinantas({ ...baseArgs, dhatu: d,
    lakara: Lakara.LatN, prayoga: pr,
    purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text();
  assert.equal(f('vac', Prayoga.Karmani), 'avAci');  // avāci
  assert.equal(f('ni', Prayoga.Karmani), 'anAyi');   // anāyi
  assert.equal(f('dA', Prayoga.Karmani), 'adAyi');   // adāyi
  assert.equal(f('dA', Prayoga.Bhave), 'adAyi');
  // Active aorist is unaffected.
  assert.equal(f('dA', Prayoga.Kartari), 'adAt');    // adāt
  assert.equal(f('vac', Prayoga.Kartari), 'avocat');
});

test('√muc root aorist full paradigm (active + middle)', () => {
  const f = (pada: Pada, p: Purusha, v: Vacana) =>
    deriveTinantas({ ...baseArgs, dhatu: 'muc', lakara: Lakara.LatN, pada,
      purusha: p, vacana: v })[0].text();
  assert.equal(f(Pada.Parasmai, Purusha.Prathama, Vacana.Eka), 'amok');    // ámok
  assert.equal(f(Pada.Parasmai, Purusha.Prathama, Vacana.Bahu), 'amucan'); // ámucan
  assert.equal(f(Pada.Parasmai, Purusha.Uttama, Vacana.Eka), 'amocam');    // ámocam
  assert.equal(f(Pada.Atmane, Purusha.Prathama, Vacana.Eka), 'amukta');    // ámukta
  assert.equal(f(Pada.Atmane, Purusha.Prathama, Vacana.Bahu), 'amucata');  // ámucata
  assert.equal(f(Pada.Atmane, Purusha.Uttama, Vacana.Eka), 'amuci');       // ámuci
});

test('upasarga + perfect: reduplicate the root, not the prefix', () => {
  const f = (upa: string, d: string) => deriveTinantas({ ...baseArgs, dhatu: d,
    lakara: Lakara.Lit, upasarga: upa,
    purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text();
  assert.equal(f('pra', 'gam'), 'prajagAma'); // prajagāma, not *papragama
  assert.equal(f('sam', 'gam'), 'saMjagAma'); // saṃjagāma
  assert.equal(f('vi', 'gam'), 'vijagAma');   // vijagāma
  assert.equal(f('pra', 'BU'), 'prabaBUva');  // prababhūva
  assert.equal(f('pra', 'kf'), 'pracakAra');  // pracakāra
  assert.equal(f('pra', 'ad'), 'prAd');       // prāda (6.1.84 a+ā→ā)
  // luṭ/lṛt use the bare-root stem tables too.
  const fut = (upa: string, d: string, lk: Lakara) => deriveTinantas({ ...baseArgs,
    dhatu: d, lakara: lk, upasarga: upa,
    purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text();
  assert.equal(fut('sam', 'pac', Lakara.Lrt), 'saMpakzyati'); // saṃpakṣyati
  assert.equal(fut('sam', 'pac', Lakara.Lut), 'saMpaktA');    // saṃpaktā
  assert.equal(fut('pra', 'kf', Lakara.Lrt), 'prakarizyati');   // prakariṣyati
});

test('upasarga + saṇādi: build the stem from the bare root', () => {
  const f = (upa: string, d: string, sd: Sanadi) => deriveTinantas({ ...baseArgs,
    dhatu: d, upasarga: upa, sanadi: sd,
    purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text();
  assert.equal(f('pra', 'BU', Sanadi.Nic), 'praBAvayati');   // prabhāvayati
  assert.equal(f('sam', 'kf', Sanadi.Nic), 'saMkArayati');   // saṃkārayati
  assert.equal(f('pra', 'pac', Sanadi.San), 'prapipakzati'); // prapipakṣati
  assert.equal(f('vi', 'gam', Sanadi.San), 'vijigamizati');  // vijigamiṣati
  assert.equal(f('pra', 'BU', Sanadi.Yan), 'praBoBUyate');   // prabobhūyate
  assert.equal(f('pra', 'BU', Sanadi.YangLuk), 'praBoBavIti'); // prabobhavīti
});

test('ud is a valid upasarga (1.4.58 prādayaḥ)', () => {
  const f = (d: string) => deriveTinantas({ ...baseArgs, dhatu: d,
    upasarga: 'ud', purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text();
  assert.equal(f('i'), 'udeti');   // udeti (not bare eti)
  assert.equal(f('gam'), 'udgacchati');
  assert.equal(f('kf'), 'udkaroti');
});

test('optative middle 3p keeps dental n in -ran (bhaveran)', () => {
  const f = (d: string) => deriveTinantas({ ...baseArgs, dhatu: d,
    lakara: Lakara.Lin, pada: Pada.Atmane,
    purusha: Purusha.Prathama, vacana: Vacana.Bahu })[0].text();
  assert.equal(f('BU'), 'Baveran');  // bháveran, not *bhaveraṇ
  assert.equal(f('pac'), 'paceran'); // paceran
  assert.equal(f('gam'), 'gacheran');
  // Genuine ṇatva after r in the same pada is unaffected (guru → guruṇā).
  assert.equal(deriveSubantas({ pratipadika: 'guru', linga: Linga.Pumsaka,
    vibhakti: 3, vacana: Vacana.Eka })[0].text(), 'guruRA');
});

test('imperative 2s of √dhā vs √dā (dhehi / dehi)', () => {
  const f = (d: string) => deriveTinantas({ ...baseArgs, dhatu: d,
    lakara: Lakara.Lot, purusha: Purusha.Madhyama, vacana: Vacana.Eka })[0].text();
  assert.equal(f('DA'), 'Dehi'); // dhehi (धेहि)
  assert.equal(f('dA'), 'dehi'); // dehi (देहि)
});

test('class-5 imperative paradigms (śṛṇu/cinu/sunu)', () => {
  const f = (d: string, p: Purusha, v: Vacana) => deriveTinantas({ ...baseArgs,
    dhatu: d, lakara: Lakara.Lot, purusha: p, vacana: v })[0].text();
  assert.equal(f('zru', Purusha.Madhyama, Vacana.Eka), 'zRuNu');     // śṛṇu
  assert.equal(f('zru', Purusha.Prathama, Vacana.Bahu), 'zRuNvantu'); // śṛṇvantu
  assert.equal(f('zru', Purusha.Uttama, Vacana.Eka), 'zRuNavARi');   // śṛṇavāni
  assert.equal(f('ciY', Purusha.Madhyama, Vacana.Eka), 'cinu');       // cinu
  assert.equal(f('ciY', Purusha.Prathama, Vacana.Bahu), 'cinvantu');  // cinvantu
  assert.equal(f('zuY', Purusha.Madhyama, Vacana.Eka), 'sunu');       // sunu
  assert.equal(f('SiY', Purusha.Prathama, Vacana.Bahu), 'SInvantu');  // śinvantu
  assert.equal(f('stfY', Purusha.Madhyama, Vacana.Eka), 'stfRnu');    // stṛṇu
});

test('class-5 optative paradigms (cinuyāt, sunuyāt, stṛṇuyāt)', () => {
  const f = (d: string, p: Purusha, v: Vacana) => deriveTinantas({ ...baseArgs,
    dhatu: d, lakara: Lakara.Lin, purusha: p, vacana: v })[0].text();
  assert.equal(f('ciY', Purusha.Prathama, Vacana.Dvi), 'cinuyAtAm');
  assert.equal(f('ciY', Purusha.Prathama, Vacana.Bahu), 'cinuyuH');
  assert.equal(f('zuY', Purusha.Prathama, Vacana.Bahu), 'sunuyuH');
  assert.equal(f('SiY', Purusha.Prathama, Vacana.Dvi), 'SinuyAtAm');
  assert.equal(f('stfY', Purusha.Prathama, Vacana.Bahu), 'stfRnuyuH');
});

test('class-5 imperfect weak-stem forms', () => {
  const f = (d: string, p: Purusha, v: Vacana) => deriveTinantas({ ...baseArgs,
    dhatu: d, lakara: Lakara.Lan, purusha: p, vacana: v })[0].text();
  assert.equal(f('zru', Purusha.Prathama, Vacana.Dvi), 'azRuNutAm');
  assert.equal(f('zru', Purusha.Prathama, Vacana.Bahu), 'azRuNvan');
  assert.equal(f('ciY', Purusha.Prathama, Vacana.Bahu), 'acinvan');
  assert.equal(f('zuY', Purusha.Prathama, Vacana.Dvi), 'asunutAm');
  assert.equal(f('SiY', Purusha.Prathama, Vacana.Bahu), 'aSinvan');
  assert.equal(f('stfY', Purusha.Prathama, Vacana.Bahu), 'astfRnvan');
});

test('class-5 middle present 3d (cinvāte)', () => {
  assert.equal(deriveTinantas({ ...baseArgs, dhatu: 'ciY', pada: Pada.Atmane,
    purusha: Purusha.Prathama, vacana: Vacana.Dvi })[0].text(), 'cinvAte'); // cinvā́te
  assert.equal(deriveTinantas({ ...baseArgs, dhatu: 'ciY', pada: Pada.Atmane,
    purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text(), 'cinute'); // cinuté
});

test('class-5 middle present paradigms (cinvāte / śṛṇvāte)', () => {
  const f = (d: string, p: Purusha, v: Vacana) => deriveTinantas({ ...baseArgs,
    dhatu: d, pada: Pada.Atmane, purusha: p, vacana: v })[0].text();
  assert.equal(f('ciY', Purusha.Madhyama, Vacana.Eka), 'cinuze');  // cinuṣé
  assert.equal(f('ciY', Purusha.Uttama, Vacana.Eka), 'cinve');     // cinvé
  assert.equal(f('ciY', Purusha.Uttama, Vacana.Bahu), 'cinmahe');  // cinmáhe
  assert.equal(f('zru', Purusha.Prathama, Vacana.Dvi), 'zRuNvAte'); // śṛṇvā́te
  assert.equal(f('zru', Purusha.Uttama, Vacana.Eka), 'zRuNve');    // śṛṇvé
  assert.equal(f('zuY', Purusha.Prathama, Vacana.Bahu), 'sunvate'); // sunváte
  assert.equal(f('SiY', Purusha.Madhyama, Vacana.Eka), 'Sinuze');  // śinuṣé
  assert.equal(f('stfY', Purusha.Prathama, Vacana.Dvi), 'stfRnvAte'); // stṛṇvā́te
});

test('√hu (juhoti) full present-system paradigm', () => {
  const f = (lk: Lakara, pada: Pada, p: Purusha, v: Vacana) => deriveTinantas({
    ...baseArgs, dhatu: 'hu', lakara: lk, pada, purusha: p, vacana: v })[0].text();
  assert.equal(f(Lakara.Lat, Pada.Parasmai, Purusha.Madhyama, Vacana.Dvi), 'juhuthaH'); // juhutháḥ
  assert.equal(f(Lakara.Lat, Pada.Parasmai, Purusha.Uttama, Vacana.Bahu), 'juhumaH');  // juhumáḥ
  assert.equal(f(Lakara.Lan, Pada.Parasmai, Purusha.Prathama, Vacana.Bahu), 'ajuhavuH'); // ájuhavuḥ
  assert.equal(f(Lakara.Lot, Pada.Parasmai, Purusha.Madhyama, Vacana.Eka), 'juhudhi'); // juhudhí
  assert.equal(f(Lakara.Lin, Pada.Parasmai, Purusha.Prathama, Vacana.Eka), 'juhuyAt'); // juhuyā́t
  assert.equal(f(Lakara.Lat, Pada.Atmane, Purusha.Prathama, Vacana.Dvi), 'juhvAte');   // júhvāte
  assert.equal(f(Lakara.Lan, Pada.Atmane, Purusha.Uttama, Vacana.Eka), 'ajuhvi');      // ájuhvi
});

test('√as (asti) weak forms from Wiktionary', () => {
  const f = (lk: Lakara, p: Purusha, v: Vacana) => deriveTinantas({ ...baseArgs,
    dhatu: 'as', lakara: lk, purusha: p, vacana: v })[0].text();
  assert.equal(f(Lakara.Lat, Purusha.Prathama, Vacana.Dvi), 'staH');   // stáḥ
  assert.equal(f(Lakara.Lat, Purusha.Madhyama, Vacana.Dvi), 'sthaH');  // stháḥ
  assert.equal(f(Lakara.Lat, Purusha.Uttama, Vacana.Bahu), 'smaH');    // smáḥ
  assert.equal(f(Lakara.Lot, Purusha.Prathama, Vacana.Dvi), 'astAm');  // astā́m
  assert.equal(f(Lakara.Lot, Purusha.Madhyama, Vacana.Bahu), 'asta');  // astá
  assert.equal(f(Lakara.Lan, Purusha.Madhyama, Vacana.Eka), 'AsIH');   // āsī́ḥ
  assert.equal(f(Lakara.Lan, Purusha.Uttama, Vacana.Eka), 'Asam');     // ā́sam
});

test('√dā / √dhā optative 1d/1p (dadyāva, dadhyāma)', () => {
  const f = (d: string, v: Vacana) => deriveTinantas({ ...baseArgs, dhatu: d,
    lakara: Lakara.Lin, purusha: Purusha.Uttama, vacana: v })[0].text();
  assert.equal(f('dA', Vacana.Dvi), 'dadyAva');
  assert.equal(f('dA', Vacana.Bahu), 'dadyAma');
  assert.equal(f('DA', Vacana.Dvi), 'dadhyAva');
  assert.equal(f('DA', Vacana.Bahu), 'dadhyAma');
});

test('√grah imperative 2s gṛhāṇá (not gṛhāṅa)', () => {
  assert.equal(deriveTinantas({ ...baseArgs, dhatu: 'grah', lakara: Lakara.Lot,
    purusha: Purusha.Madhyama, vacana: Vacana.Eka })[0].text(), 'gfhARa');
});

test('√tanu (tanoti) present-system paradigm from Wiktionary', () => {
  const f = (lk: Lakara, pada: Pada, p: Purusha, v: Vacana) => deriveTinantas({
    ...baseArgs, dhatu: 'tanu', lakara: lk, pada, purusha: p, vacana: v })[0].text();
  assert.equal(f(Lakara.Lat, Pada.Parasmai, Purusha.Madhyama, Vacana.Eka), 'tanOzi'); // tanóṣi
  assert.equal(f(Lakara.Lat, Pada.Parasmai, Purusha.Uttama, Vacana.Bahu), 'tanmaH'); // tanmáḥ
  assert.equal(f(Lakara.Lan, Pada.Parasmai, Purusha.Prathama, Vacana.Bahu), 'atanvan');
  assert.equal(f(Lakara.Lot, Pada.Parasmai, Purusha.Prathama, Vacana.Eka), 'tanotu');
  assert.equal(f(Lakara.Lin, Pada.Parasmai, Purusha.Prathama, Vacana.Eka), 'tanuyAt');
  assert.equal(f(Lakara.Lat, Pada.Atmane, Purusha.Prathama, Vacana.Dvi), 'tanvAte');
  assert.equal(f(Lakara.Lat, Pada.Atmane, Purusha.Uttama, Vacana.Eka), 'tanve');
});

test('dhātupāṭha indicatory markers x/Y never leak into surfaces', () => {
  const f = (d: string) => deriveTinantas({ ...baseArgs, dhatu: d,
    purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text();
  assert.equal(f('mucx'), 'mucati'); // was *mucalati (x→l)
  assert.equal(f('patx'), 'patati');
  assert.equal(f('Apx'), 'Apnoti');  // āpnoti (explicit class-5 form)
  assert.equal(f('Sakx'), 'Saknoti'); // śaknoti
  assert.equal(f('ciY'), 'cinoti');   // Y stripped, explicit form kept
  // kṛt stems too: Apx → āpta, not *āpxta.
  assert.equal(deriveKrdantas({ dhatu: 'Apx', krt: Krt.Tac })[0].text(), 'Apta');
  assert.equal(deriveKrdantas({ dhatu: 'mucx', krt: Krt.Tac })[0].text(), 'mukta');
});

test('indicatory markers stripped in saṇādi stems too', () => {
  const f = (d: string, sd: Sanadi) => deriveTinantas({ ...baseArgs,
    dhatu: d, sanadi: sd, purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text();
  assert.equal(f('mucx', Sanadi.Nic), 'mocayati');  // mocayati, not *mucxayati
  assert.equal(f('mucx', Sanadi.San), 'mumukzati'); // mumukṣati
});

test('√hu present participle is júhvat', () => {
  assert.equal(deriveKrdantas({ dhatu: 'hu', krt: Krt.Satr })[0].text(), 'juhvat');
});

test('ṇin agent noun of √grah is grāhin (hard dental n)', () => {
  assert.equal(deriveKrdantas({ dhatu: 'grah', krt: Krt.Nini })[0].text(), 'grAhin');
  // Genuine ṇatva after r/h with intervening vowels still applies.
  assert.equal(deriveKrdantas({ dhatu: 'grah', krt: Krt.SanaC })[0].text(), 'grahamARa');
});

test('√ji ṇvul agent noun is jayaka (not *jeaka)', () => {
  assert.equal(deriveKrdantas({ dhatu: 'ji', krt: Krt.Nvul })[0].text(), 'jayaka');
});

test('i-final roots take ay before ṇvul -aka', () => {
  const f = (d: string) => deriveKrdantas({ dhatu: d, krt: Krt.Nvul })[0].text();
  assert.equal(f('ci'), 'cayaka');
  assert.equal(f('i'), 'ayaka');
  assert.equal(f('kzi'), 'kzayaka');
  assert.equal(f('ji'), 'jayaka');
});

test('class-4 roots drop indicatory final I/u (nṛtyati, trasyati)', () => {
  const f = (d: string) => deriveTinantas({ ...baseArgs, dhatu: d,
    purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text();
  assert.equal(f('nftI'), 'nftyati');   // nṛtyati, not *nftayyati
  assert.equal(f('trasI'), 'trasyati'); // trasyati, not *trasayyati
  assert.equal(f('divu'), 'divyati');
});

test('class-4 indicatory ī stripped in all lakāras and kṛtas', () => {
  const f = (lk: Lakara) => deriveTinantas({ ...baseArgs, dhatu: 'nftI',
    lakara: lk, purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text();
  assert.ok(!f(Lakara.Lat).includes('I'));
  assert.ok(!f(Lakara.Lit).includes('I'));
  assert.ok(!f(Lakara.Lrt).includes('I'));
  assert.ok(!f(Lakara.LatN).includes('I'));
  assert.equal(deriveKrdantas({ dhatu: 'nftI', krt: Krt.Nvanip })[0].text(), 'nftvan');
});

test('Curādi (class-10) roots take ṇic -ayati with guṇa', () => {
  const f = (d: string) => deriveTinantas({ ...baseArgs, dhatu: d,
    purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text();
  assert.equal(f('pUja'), 'pUjayati');  // pūjayati
  assert.equal(f('cura'), 'corayati');  // corayati (u → o)
  assert.equal(f('midi'), 'medayati');  // medayati (i → e)
  assert.equal(f('kudri'), 'kodrayati');
});

test('√diś causative is deśayati', () => {
  assert.equal(deriveTinantas({ ...baseArgs, dhatu: 'diS', sanadi: Sanadi.Nic,
    purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text(), 'deSayati');
});

test('causative guṇa/vṛddhi before ṇic (bodháyati etc.)', () => {
  const f = (d: string) => deriveTinantas({ ...baseArgs, dhatu: d, sanadi: Sanadi.Nic,
    purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text();
  assert.equal(f('budh'), 'bodhayati'); // bodháyati (Wiktionary)
  assert.equal(f('duh'), 'dohayati');
  assert.equal(f('ruh'), 'rohayati');
  assert.equal(f('sah'), 'sAhayati');   // sāhayati
  assert.equal(f('vah'), 'vAhayati');   // vāhayati
  assert.equal(f('ruC'), 'roCayati');   // rocayati
});

test('causatives of √vṛt and √gras', () => {
  const f = (d: string) => deriveTinantas({ ...baseArgs, dhatu: d, sanadi: Sanadi.Nic,
    purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text();
  assert.equal(f('vft'), 'vartayati');
  assert.equal(f('gras'), 'grAsayati');
});

test('explicit nic on Curādi midí does not double -ay', () => {
  assert.equal(deriveTinantas({ ...baseArgs, dhatu: 'midi', sanadi: Sanadi.Nic,
    purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text(), 'medayati');
});

test('√yuj śānac is yuñjāna', () => {
  assert.equal(deriveKrdantas({ dhatu: 'yuj', krt: Krt.cAnaS })[0].text(), 'yuNYAna');
});

test('√bhū ap/yuc stems are bhava/bhavana', () => {
  assert.equal(deriveKrdantas({ dhatu: 'BU', krt: Krt.ap })[0].text(), 'BAva');
  assert.equal(deriveKrdantas({ dhatu: 'BU', krt: Krt.yuc })[0].text(), 'BAvana');
});

test('√ji śānac is jayamāna', () => {
  assert.equal(deriveKrdantas({ dhatu: 'ji', krt: Krt.SanaC })[0].text(), 'jayamAna');
});

test('upasarga is retained in karmani passive stems', () => {
  const f = (upa: string, d: string) => deriveTinantas({ ...baseArgs, dhatu: d,
    upasarga: upa, prayoga: Prayoga.Karmani,
    purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text();
  assert.equal(f('pra', 'gam'), 'pragamyate');
  assert.equal(f('sam', 'pac'), 'saMpacyate');
  assert.equal(f('vi', 'kf'), 'vikriyate');
  assert.equal(f('anu', 'dA'), 'anudIyate');
});

test('upasarga retained in passive aorist 3s', () => {
  assert.equal(deriveTinantas({ ...baseArgs, dhatu: 'dA', upasarga: 'anu',
    prayoga: Prayoga.Karmani, lakara: Lakara.LatN,
    purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text(), 'anvadAyi');
  assert.equal(deriveTinantas({ ...baseArgs, dhatu: 'vac', upasarga: 'pra',
    prayoga: Prayoga.Karmani, lakara: Lakara.LatN,
    purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text(), 'prAvAci');
});


test('luṭ of long-vowel roots drops iṭ (sthātā, pātā, jñātā)', () => {
  const f = (d: string) => deriveTinantas({ ...baseArgs, dhatu: d,
    lakara: Lakara.Lut, purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text();
  assert.equal(f('sTA'), 'sTAtA');
  assert.equal(f('pA'), 'pAtA');
  assert.equal(f('jFnA'), 'jFAtA');
  assert.equal(f('nI'), 'netA');
  assert.equal(f('ji'), 'jetA');
  assert.equal(f('zru'), 'zrotA');
});

test('√muc luṭ is moktā', () => {
  assert.equal(deriveTinantas({ ...baseArgs, dhatu: 'muc', lakara: Lakara.Lut,
    purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text(), 'moktA');
});

test('luṭ stems grahītā / labdhā', () => {
  const f = (d: string) => deriveTinantas({ ...baseArgs, dhatu: d,
    lakara: Lakara.Lut, purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text();
  assert.equal(f('grah'), 'grahItA');
  assert.equal(f('lab'), 'labDA');
  assert.equal(f('vid'), 'veditA');
  assert.equal(deriveTinantas({ ...baseArgs, dhatu: 'vid', lakara: Lakara.Lut,
    pada: Pada.Atmane, purusha: Purusha.Prathama, vacana: Vacana.Eka })[0].text(), 'veditA');
});

test('√bhid class-7 present paradigm (bhinátti)', () => {
  const f = (p: Purusha, v: Vacana) => deriveTinantas({ ...baseArgs, dhatu: 'bhid',
    purusha: p, vacana: v })[0].text();
  assert.equal(f(Purusha.Madhyama, Vacana.Eka), 'bhinatsi');
  assert.equal(f(Purusha.Prathama, Vacana.Dvi), 'bhinttaH');
  assert.equal(f(Purusha.Uttama, Vacana.Eka), 'bhinadmi');
  assert.equal(f(Purusha.Uttama, Vacana.Bahu), 'bhindmaH');
});
