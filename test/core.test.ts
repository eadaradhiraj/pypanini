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
    '1.3.1|BU',
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
  assert.equal(aorist('kf', Purusha.Prathama, Vacana.Bahu), 'akArzan'); // akārṣuḥ
  assert.equal(aorist('kf', Purusha.Uttama, Vacana.Eka), 'akArzm');    // akārṣam
  // passive aorist 3s
  assert.equal(aorist('vac', Purusha.Prathama, Vacana.Eka), 'avAci');
  assert.equal(aorist('dA', Purusha.Prathama, Vacana.Eka), 'adAyi');
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
  assert.equal(desiderative('vid'), 'vivizati');   // vividiṣati
  assert.equal(desiderative('yaj'), 'yiyakzati');  // yiyakṣati
  assert.equal(desiderative('han'), 'jighAmsati'); // jighāṃsati
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
  assert.equal(deriveKrdantas({ dhatu: 'yaj', krt: Krt.Tac })[0].text(), 'yazwa');  // yaṣṭa
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
  assert.equal(deriveKrdantas({ dhatu: 'pac', krt: Krt.Nvul })[0].text(), 'pAcaka'); // pācaka
  assert.equal(deriveKrdantas({ dhatu: 'yaj', krt: Krt.Nvul })[0].text(), 'yAjaka'); // yājaka
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
  assert.equal(deriveKrdantas({ dhatu: 'pac', krt: Krt.ghaH })[0].text(), 'pAca');  // pāka (medial vṛddhi)
  assert.equal(deriveKrdantas({ dhatu: 'tyj', krt: Krt.ghaH })[0].text(), 'tyAja'); // tyāga
  assert.equal(deriveKrdantas({ dhatu: 'BU', krt: Krt.ghaH })[0].text(), 'BAva');  // bhāva
  assert.equal(deriveKrdantas({ dhatu: 'car', krt: Krt.ghaH })[0].text(), 'cAra');  // cāra
  assert.equal(deriveKrdantas({ dhatu: 'ji', krt: Krt.ghaH })[0].text(), 'jaya');   // jaya
  assert.equal(deriveKrdantas({ dhatu: 'vid', krt: Krt.ghaH })[0].text(), 'veda');  // veda
  assert.equal(deriveKrdantas({ dhatu: 'nam', krt: Krt.ghaH })[0].text(), 'nAma');  // nāma
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
  assert.equal(deriveKrdantas({ dhatu: 'ji', krt: Krt.kSnu })[0].text(), 'jizNu');
  assert.equal(deriveKrdantas({ dhatu: 'sTA', krt: Krt.kSnu })[0].text(), 'sTAsnu');
  assert.equal(deriveKrdantas({ dhatu: 'BU', krt: Krt.kSnu })[0].text(), 'BUzNu');
});

test('kṛdanta: iṣṇuc (-iṣṇu, 3.2.136/138)', () => {
  assert.equal(deriveKrdantas({ dhatu: 'BU', krt: Krt.izNuc })[0].text(), 'BavizNu'); // bhaviṣṇu
  assert.equal(deriveKrdantas({ dhatu: 'ruc', krt: Krt.izNuc })[0].text(), 'rocizNu'); // rociṣṇu
  assert.equal(deriveKrdantas({ dhatu: 'saha', krt: Krt.izNuc })[0].text(), 'sahizNu'); // sahiṣṇu
  assert.equal(deriveKrdantas({ dhatu: 'car', krt: Krt.izNuc })[0].text(), 'carizNu'); // cariṣṇu
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
  assert.equal(deriveKrdantas({ dhatu: 'kf', krt: Krt.khyun })[0].text(), 'karaNa');
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

  // bhavat (m), -at stem
  assert.equal(form('Bavat', Vibhakti.Dvitiya, Vacana.Eka), 'Bavantam');
  assert.equal(form('Bavat', Vibhakti.Trtiya, Vacana.Bahu), 'BavadBiH');
  assert.equal(form('Bavat', Vibhakti.Saptami, Vacana.Bahu), 'Bavatsu');

  // pitṛ (m), -ṛ stem
  assert.equal(form('pitf', Vibhakti.Prathama, Vacana.Eka), 'pitA');
  assert.equal(form('pitf', Vibhakti.Sasti, Vacana.Bahu), 'pitrIRAm');
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
  assert.equal(form('putra', NamadhatuPratyaya.KyaN), 'putrAyate');
  assert.equal(form('Syena', NamadhatuPratyaya.KyaN), 'SyenAyate');
  assert.equal(form('putra', NamadhatuPratyaya.Nic), 'putrayati');
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
  assert.equal(deriveStri({ stem: 'deva' })?.text(), 'devA');   // devā
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
    'saMgamati', // saṃgamati
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
