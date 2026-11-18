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
    '8.4.68|Bav + a + ti',
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
  // passive aorist 3s
  assert.equal(aorist('vac', Purusha.Prathama, Vacana.Eka), 'avAci');
  assert.equal(aorist('dA', Purusha.Prathama, Vacana.Eka), 'adAyi');
  // precative active (bhū → bhūyāt)
  assert.equal(derivePrecative({ root: 'BU', pada: Pada.Parasmai, purusha: Purusha.Prathama, vacana: Vacana.Eka })?.text(), 'BUyAt');
});

test('karmani passive: pac → pacyate', () => {
  const p = deriveTinantas({
    ...baseArgs,
    dhatu: 'pac',
    prayoga: Prayoga.Karmani,
    pada: Pada.Atmane,
  })[0];
  assert.equal(p.text(), 'pacyate');
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
  assert.equal(deriveKrdantas({ dhatu: 'kf', krt: Krt.Nini })[0].text(), 'kArin'); // kārin
  assert.equal(deriveKrdantas({ dhatu: 'dA', krt: Krt.Nini })[0].text(), 'dAyin'); // dāyin
});

test('kṛdanta: śānan (-māna, 3.2.128)', () => {
  assert.equal(deriveKrdantas({ dhatu: 'pU', krt: Krt.Sanan })[0].text(), 'pavamAna'); // pavamāna
  assert.equal(deriveKrdantas({ dhatu: 'yaj', krt: Krt.Sanan })[0].text(), 'yajamAna'); // yajamāna
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
  assert.equal(deriveKrdantas({ dhatu: 'ni', krt: Krt.TRn })[0].text(), 'neSTf'); // neṣṭṛ
  assert.equal(deriveKrdantas({ dhatu: 'tviz', krt: Krt.TRn })[0].text(), 'tvaSTf'); // tvaṣṭṛ
});

test('kṛdanta: kyap (-yā feminine, 3.3.99)', () => {
  assert.equal(deriveKrdantas({ dhatu: 'vid', krt: Krt.Kyap })[0].text(), 'vidyA'); // vidyā
  assert.equal(deriveKrdantas({ dhatu: 'man', krt: Krt.Kyap })[0].text(), 'manyA'); // manyā
  assert.equal(deriveKrdantas({ dhatu: 'i', krt: Krt.Kyap })[0].text(), 'ityA');   // ityā
  assert.equal(deriveKrdantas({ dhatu: 'zi', krt: Krt.Kyap })[0].text(), 'zayyA'); // śayyā
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
  assert.equal(p.text(), 'balaiH');
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
  assert.equal(form('sItA', Linga.Stri, Vibhakti.Sasti, Vacana.Bahu), 'sItAnAm');

  // nadī (f), ī-stem
  assert.equal(form('nadI', Linga.Stri, Vibhakti.Prathama, Vacana.Bahu), 'nadyaH');
});

test('subanta: feminine u-stem and -as neuter consonant stem', () => {
  const form = (pratipadika: string, linga: Linga, vibhakti: Vibhakti, vacana: Vacana) =>
    deriveSubantas({ pratipadika, linga, vibhakti, vacana })[0].text();

  // dhenu (f), u-stem
  assert.equal(form('Denu', Linga.Stri, Vibhakti.Prathama, Vacana.Eka), 'DenuH');
  assert.equal(form('Denu', Linga.Stri, Vibhakti.Trtiya, Vacana.Eka), 'DenvA');
  assert.equal(form('Denu', Linga.Stri, Vibhakti.Sasti, Vacana.Bahu), 'DenUnAm');

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
  assert.equal(form('putra', NamadhatuPratyaya.Kamyac), 'putrkAmyati');
  assert.equal(form('putra', NamadhatuPratyaya.KyaN), 'putrAyate');
  assert.equal(form('Syena', NamadhatuPratyaya.KyaN), 'SyenAyate');
  assert.equal(form('putra', NamadhatuPratyaya.Nic), 'putrayati');
  assert.equal(form('kazwa', NamadhatuPratyaya.KyaNKa), 'kazwAyate'); // kaṣṭāyate
  assert.equal(form('lohita', NamadhatuPratyaya.KyaS), 'lohitAyate');
  // 3.1.15 / 3.1.16 / 3.1.19
  assert.equal(form('roma', NamadhatuPratyaya.Varticara), 'romAyate');
  assert.equal(form('bAzpa', NamadhatuPratyaya.Udvamana), 'bAzpAyate');
  assert.equal(form('namas', NamadhatuPratyaya.KyacNama), 'namasyati');
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

test('Vyakarana facade', () => {
  const v = new Vyakarana();
  assert.equal(v.deriveTinantas({ ...baseArgs, dhatu: 'BU' })[0].text(), 'Bavati');
});
