#!/usr/bin/env node
/**
 * pypanini CLI. All forms are SLP1.
 *
 * Examples:
 *   pypanini tinanta --dhatu BU
 *   pypanini tinanta --dhatu BU --purusha prathama --vacana eka --trace
 *   pypanini tinanta --dhatu pac --prayoga karmani
 *   pypanini tinanta --dhatu BU --sanadi nic
 *   pypanini krdanta --dhatu kf --krt tac
 *   pypanini subanta --pratipadika bala --linga napumsaka --vibhakti 3 --vacana bahu
 */

import { Prakriya } from './core/prakriya';
import {
  Gana,
  Krt,
  Lakara,
  Linga,
  Pada,
  Prayoga,
  Purusha,
  Sanadi,
  TinantaArgs,
  Vibhakti,
  Vacana,
} from './core/types';
import { resolveDhatu, DHATUPATHA, searchDhatus } from './data/dhatupatha';
import { SUTRAS } from './data/sutras';
import { deriveTinantas } from './tinanta';
import { deriveKrdantas } from './krdanta';
import { deriveSubantas } from './subanta';
import { analyzeSubanta, describeAnalysis } from './analyze';
import { buildSanadiStem } from './sanadi';
import { deriveNamadhatus, NamadhatuPratyaya, NAMADHATU_INFO } from './namadhatu';
import { deriveParadigm, formatParadigm } from './paradigm';

type Flags = Record<string, string | boolean>;

function parseFlags(argv: string[]): Flags {
  const flags: Flags = {};
  for (let i = 0; i < argv.length; i++) {
    const arg = argv[i];
    if (arg.startsWith('--')) {
      const key = arg.slice(2);
      const next = argv[i + 1];
      if (next !== undefined && !next.startsWith('--')) {
        flags[key] = next;
        i++;
      } else {
        flags[key] = true;
      }
    }
  }
  return flags;
}

function str(flags: Flags, key: string, fallback = ''): string {
  const v = flags[key];
  return typeof v === 'string' ? v : fallback;
}

function showTrace(label: string, p: Prakriya): void {
  console.log(`${label}  =>  ${p.text()}`);
  for (const step of p.history) {
    console.log(`  ${step.rule.padEnd(48)} | ${step.result}`);
  }
  console.log();
}

function printHelp(): void {
  console.log(`pypanini — pure TypeScript Pāṇinian word generator (SLP1 I/O)

Usage:
  pypanini <command> [options]

Commands:
  tinanta    Derive finite verb forms
  krdanta    Derive kṛdanta forms
  namadhatu  Derive denominative verbs (3.1.8–3.1.21)
  subanta    Derive subanta forms
  paradigm   Full conjugation table (all lakāras × both padas) for a dhātu
  analyze    Analyse a declined word → base + case/number/gender
  dhatus     List/search the full Dhātupāṭha (--search <prefix> --limit <n>)
  sutras     Look up sūtra text by code (--code 3.1.20) or search (--search <text>)

Common options:
  --trace            Print the prakriyā (sūtra-by-sūtra derivation)
  --dhatu <SLP1>     Verb root, e.g. BU, pac, kf
  --lakara <name>    lat (default), lit, lut, lrt, lot, lan, lng, lin, latN (aorist)
  --prayoga <name>   kartari (default), karmani
  --pada <name>      parasmai, atmane (default: from dhātu)
  --purusha <name>   prathama, madhyama, uttama
  --vacana <name>    eka, dvi, bahu
  --sanadi <name>    none, san, nic, yan, yang, yangLuk
  --upasarga <s>     pra, sam, pari, anu, vi, aBi, ... (1.4.58)
  --krt <name>       tac, tfc, satr, ani, tum, tavya, lyuT, ktvA, nvul, ktavatu, sanaC, yat, ktin, Nini, Sanan, STran, TRn, Kyap, Sa
  --pratyaya <name>  kyac, kAmyac, kyaN, Nic, Buvyac, kyaS, kyaNKa, kyaNKara, kyaNSukha,
                     varticara, udvamana, kyacNama, NiN
  --pratipadika <s>  Nominal stem, e.g. bala (a), agni (i), guru (u), sItA (ā), nadI (ī)
  --linga <name>     pumsaka, stri, napumsaka
  --vibhakti <1..8>  Case ending number

Analysis (reverse declension):
  pypanini analyze --word WrampaH
  pypanini subanta --word WrampeNa --analyze     (--declension also works)

  Supported stem classes: a-/i-/u- (m/n), ā-/ī-/u- (f), -as (n), -an/-at/-ṛ (m).
`);
}

function parseEnum<T extends string>(value: string, allowed: readonly T[], fallback: T): T {
  return (allowed as readonly string[]).includes(value) ? (value as T) : fallback;
}

function main(): void {
  const [command, ...rest] = process.argv.slice(2);
  const flags = parseFlags(rest);
  const trace = flags.trace === true;

  if (!command || command === 'help' || command === '--help' || command === '-h') {
    printHelp();
    return;
  }

  function runAnalyze(word: string): void {
    const results = analyzeSubanta(word);
    if (results.length === 0) {
      console.log(`${word}: no declension analysis found`);
      return;
    }
    console.log(`${word}:`);
    for (const a of results) console.log(`  ${describeAnalysis(a)}`);
  }

  if (command === 'analyze' || command === 'parse') {
    const word = str(flags, 'word', rest.find((a) => !a.startsWith('--')) ?? '');
    if (!word) {
      console.error('analyze requires --word <SLP1> (or a positional word)');
      process.exitCode = 1;
      return;
    }
    runAnalyze(word);
    return;
  }

  if (command === 'dhatus') {
    const query = str(flags, 'search');
    const list = query ? searchDhatus(query, parseInt(str(flags, 'limit', '100'), 10)) : DHATUPATHA;
    console.log(`${list.length} dhātus${query ? ` matching "${query}"` : ''}`);
    for (const d of list) {
      console.log(`${(d.code ?? '').padEnd(9)} ${d.text.padEnd(12)} g${d.gana}  ${d.artha ?? ''}`);
    }
    return;
  }

  if (command === 'sutras') {
    const code = str(flags, 'code');
    const query = str(flags, 'search');
    if (code) {
      const s = SUTRAS.find(([c]) => c === code);
      if (!s) {
        console.error(`sūtra ${code} not found`);
        process.exitCode = 1;
      } else {
        console.log(`${s[0]}\t${s[1]}`);
      }
    } else if (query) {
      const limit = parseInt(str(flags, 'limit', '30'), 10);
      const hits = SUTRAS.filter(([, t]) => t.includes(query)).slice(0, limit);
      console.log(`${hits.length} sūtras matching "${query}"`);
      for (const [c, t] of hits) console.log(`${c.padEnd(8)} ${t}`);
    } else {
      console.error('sutras requires --code <n.n.n> or --search <text>');
      process.exitCode = 1;
    }
    return;
  }

  if (command === 'tinanta') {
    const dhatuText = str(flags, 'dhatu', 'BU');
    const dhatu = resolveDhatu(dhatuText, Gana.Bhvadi);
    const lakara = parseEnum(str(flags, 'lakara', 'lat'), Object.values(Lakara) as Lakara[], Lakara.Lat);
    const prayoga = parseEnum(str(flags, 'prayoga', 'kartari'), Object.values(Prayoga) as Prayoga[], Prayoga.Kartari);
    const pada = parseEnum(str(flags, 'pada', ''), Object.values(Pada) as Pada[], dhatu.pada);
    const purushaFlag = str(flags, 'purusha');
    const vacanaFlag = str(flags, 'vacana');
    const sanadi = parseEnum(str(flags, 'sanadi', 'none'), Object.values(Sanadi) as Sanadi[], Sanadi.None);

    const purushas = purushaFlag
      ? [parseEnum(purushaFlag, Object.values(Purusha) as Purusha[], Purusha.Prathama)]
      : [Purusha.Prathama, Purusha.Madhyama, Purusha.Uttama];
    const vacanas = vacanaFlag
      ? [parseEnum(vacanaFlag, Object.values(Vacana) as Vacana[], Vacana.Eka)]
      : [Vacana.Eka, Vacana.Dvi, Vacana.Bahu];

    for (const purusha of purushas) {
      for (const vacana of vacanas) {
        const args: TinantaArgs = {
          dhatu, lakara, prayoga, pada, purusha, vacana, sanadi,
          upasarga: str(flags, 'upasarga') || undefined,
        };
        const p = deriveTinantas(args)[0];
        const effectivePada = buildSanadiStem(dhatu.text, sanadi).pada ?? pada;
        const label = `${dhatu.text} ${lakara} ${prayoga} ${effectivePada} ${purusha} ${vacana}`;
        if (trace) showTrace(label, p);
        else console.log(p.text());
      }
    }
    return;
  }

  if (command === 'krdanta') {
    const dhatu = resolveDhatu(str(flags, 'dhatu', 'BU'), Gana.Bhvadi);
    const krt = parseEnum(str(flags, 'krt', 'tac'), Object.values(Krt) as Krt[], Krt.Tac);
    const prayogaFlag = str(flags, 'prayoga');
    const prayoga = prayogaFlag
      ? parseEnum(prayogaFlag, Object.values(Prayoga) as Prayoga[], Prayoga.Kartari)
      : undefined;
    const sanadi = parseEnum(str(flags, 'sanadi', 'none'), Object.values(Sanadi) as Sanadi[], Sanadi.None);
    const p = deriveKrdantas({ dhatu, krt, prayoga, sanadi })[0];
    if (trace) showTrace(`krdanta ${dhatu.text} ${krt}`, p);
    else console.log(p.text());
    return;
  }

  if (command === 'paradigm') {
    const dhatu = str(flags, 'dhatu', 'BU');
    const sanadi = parseEnum(str(flags, 'sanadi', 'none'), Object.values(Sanadi) as Sanadi[], Sanadi.None);
    const prayoga = parseEnum(str(flags, 'prayoga', 'kartari'), Object.values(Prayoga) as Prayoga[], Prayoga.Kartari);
    const p = deriveParadigm({ dhatu, sanadi, prayoga });
    console.log(formatParadigm(p));
    return;
  }

  if (command === 'namadhatu') {
    const pratipadika = str(flags, 'pratipadika', str(flags, 'word', 'putra'));
    const pratyaya = parseEnum(
      str(flags, 'pratyaya', 'kyac'),
      Object.values(NamadhatuPratyaya) as NamadhatuPratyaya[],
      NamadhatuPratyaya.Kyac,
    );
    const p = deriveNamadhatus({ pratipadika, pratyaya })[0];
    if (trace) showTrace(`namadhatu ${pratipadika} ${pratyaya} (${NAMADHATU_INFO[pratyaya].sutra})`, p);
    else console.log(p.text());
    return;
  }

  if (command === 'subanta') {
    if (flags.analyze === true || flags.declension === true) {
      const word = str(flags, 'word', rest.find((a) => !a.startsWith('--')) ?? '');
      if (!word) {
        console.error('analysis requires --word <SLP1>');
        process.exitCode = 1;
        return;
      }
      runAnalyze(word);
      return;
    }
    const pratipadika = str(flags, 'pratipadika', 'bala');
    const linga = parseEnum(str(flags, 'linga', 'napumsaka'), Object.values(Linga) as Linga[], Linga.Napumsaka);
    const vibhaktiNum = parseInt(str(flags, 'vibhakti', '1'), 10);
    const vibhakti = (vibhaktiNum >= 1 && vibhaktiNum <= 8 ? vibhaktiNum : 1) as Vibhakti;
    const vacana = parseEnum(str(flags, 'vacana', 'eka'), Object.values(Vacana) as Vacana[], Vacana.Eka);
    const p = deriveSubantas({ pratipadika, linga, vibhakti, vacana })[0];
    if (trace) showTrace(`subanta ${pratipadika} ${vibhakti} ${vacana}`, p);
    else console.log(p.text());
    return;
  }

  console.error(`Unknown command: ${command}`);
  printHelp();
  process.exitCode = 1;
}

main();
