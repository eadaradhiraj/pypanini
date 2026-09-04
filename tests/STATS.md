# Generative Validation Stats

Engine: wholly generative (tinanta/krdanta derive from pada/sew/gana, no hardcoded dicts, expanded 10 antas)
Cross-check: skt-morph-data JSON (read-only)
Date: 2026-09-04T19:09:31Z
Run: python -W ignore::ResourceWarning -m unittest tests.test_dhatu -v (10 antas ×10 lakaras ×9 + 5 krdanta antas)

```
test_01_0001_BU (tests.test_dhatu.TestDhatuGenerative.test_01_0001_BU) ... ok
test_01_0002_eD (tests.test_dhatu.TestDhatuGenerative.test_01_0002_eD) ... ok
test_01_0003_sparD (tests.test_dhatu.TestDhatuGenerative.test_01_0003_sparD) ... ok
test_cli (tests.test_dhatu.TestDhatuGenerative.test_cli) ... ok

----------------------------------------------------------------------
Ran 4 tests in 18.385s

OK

```

## Per-dhatu (tests/test_dhatu.py -W ignore)

### 01.0001
```
===========================================================================
VALIDATION  skt-morph-data/01/01.0001.json  |  dhatu=BU (BU sattAyAm)
===========================================================================
✓ tokens: 41540  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```

### 01.0002
```
===========================================================================
VALIDATION  skt-morph-data/01/01.0002.json  |  dhatu=eD (eDa~ vfdDO)
===========================================================================
✓ tokens: 720  engine: generative (no hardcoded dict)

-- tinanta (6 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
---------------------------------------------------------------------------
GRAND  627/627  (100.0%)  ✓ ALL MATCHED
===========================================================================
```

### 01.0003
```
===========================================================================
VALIDATION  skt-morph-data/01/01.0003.json  |  dhatu=sparD (sparDa~ saNGarze)
===========================================================================
✓ tokens: 1879  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```

### 01.0004
```
===========================================================================
VALIDATION  skt-morph-data/01/01.0004.json  |  dhatu=gAD (gADf~ pratizWAlipsayorgranTe ca)
===========================================================================
✓ tokens: 959  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```

### 01.0005
```
===========================================================================
VALIDATION  skt-morph-data/01/01.0005.json  |  dhatu=bAD (bADf~ loqane, rowane)
===========================================================================
✓ tokens: 13239  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```

### 01.0006
```
===========================================================================
VALIDATION  skt-morph-data/01/01.0006.json  |  dhatu=nAD (nADf~ yAcYopatApESvaryASIzzu)
===========================================================================
✓ tokens: 957  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```

### 01.0007
```
===========================================================================
VALIDATION  skt-morph-data/01/01.0007.json  |  dhatu=nAT (nATf~ yAcYopatApESvaryASIzzu)
===========================================================================
✓ tokens: 2209  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```

### 01.0008
```
===========================================================================
VALIDATION  skt-morph-data/01/01.0008.json  |  dhatu=daD (daDa~ DAraRe)
===========================================================================
✓ tokens: 1146  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```

### 01.0009
```
===========================================================================
VALIDATION  skt-morph-data/01/01.0009.json  |  dhatu=skudi (skudi~ ApravaRe)
===========================================================================
✓ tokens: 975  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```

### 01.0010
```
===========================================================================
VALIDATION  skt-morph-data/01/01.0010.json  |  dhatu=Svidi (Svidi~ SvEtye)
===========================================================================
✓ tokens: 975  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```

### 01.0011
```
===========================================================================
VALIDATION  skt-morph-data/01/01.0011.json  |  dhatu=vadi (vadi~ aBivAdanastutyoH)
===========================================================================
✓ tokens: 3764  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0012
```
===========================================================================
VALIDATION  skt-morph-data/01/01.0012.json  |  dhatu=Badi (Badi~ kalyARe suKe ca)
===========================================================================
✓ tokens: 976  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0013
```
===========================================================================
VALIDATION  skt-morph-data/01/01.0013.json  |  dhatu=madi (madi~ stutimodamadasvapnakAntigatizu)
===========================================================================
✓ tokens: 3711  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0014
```
===========================================================================
VALIDATION  skt-morph-data/01/01.0014.json  |  dhatu=spadi (spadi~ kiYciccalane)
===========================================================================
✓ tokens: 2814  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0015
```
===========================================================================
VALIDATION  /home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0015.json  |  dhatu=klidi (klidi~ paridevane)
===========================================================================
✓ tokens: 976  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0016
```
===========================================================================
VALIDATION  /home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0016.json  |  dhatu=mud (muda~ harze)
===========================================================================
✓ tokens: 7698  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0017
```
===========================================================================
VALIDATION  /home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0017.json  |  dhatu=dad (dada~ dAne)
===========================================================================
✓ tokens: 1152  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0018
```
===========================================================================
VALIDATION  /home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0018.json  |  dhatu=zvad (zvada~ AsvAdane)
===========================================================================
✓ tokens: 1140  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0019
```
===========================================================================
VALIDATION  /home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0019.json  |  dhatu=svard (svarda~ AsvAdane)
===========================================================================
✓ tokens: 978  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0020
```
===========================================================================
VALIDATION  /home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0020.json  |  dhatu=urd (urda~ mAne krIqAyAM AsvAdane ca)
===========================================================================
✓ tokens: 721  engine: generative (no hardcoded dict)

-- tinanta (6 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
---------------------------------------------------------------------------
GRAND  627/627  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0021
```
===========================================================================
VALIDATION  /home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0021.json  |  dhatu=kurd (kurda~ krIqAyAm eva)
===========================================================================
✓ tokens: 1891  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0022
```
===========================================================================
VALIDATION  /home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0022.json  |  dhatu=Kurd (Kurda~ krIqAyAm eva)
===========================================================================
✓ tokens: 977  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0023
```
===========================================================================
VALIDATION  /home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0023.json  |  dhatu=gurd (gurda~ krIqAyAm eva)
===========================================================================
✓ tokens: 977  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0024
```
===========================================================================
VALIDATION  /home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0024.json  |  dhatu=gud (guda~ krIqAyAm eva)
===========================================================================
✓ tokens: 1358  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0025
```
===========================================================================
VALIDATION  /home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0025.json  |  dhatu=zUd (zUda~ kzaraRe)
===========================================================================
✓ tokens: 1858  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0026
```
===========================================================================
VALIDATION  /home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0026.json  |  dhatu=hrAd (hrAda~ avyakte Sabde)
===========================================================================
✓ tokens: 962  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0027
```
===========================================================================
VALIDATION  /home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0027.json  |  dhatu=hlAdI (hlAdI~ avyakte Sabde suKe ca)
===========================================================================
✓ tokens: 2293  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0028
```
===========================================================================
VALIDATION  /home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0028.json  |  dhatu=svAd (svAda~ AsvAdane)
===========================================================================
✓ tokens: 961  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0029
```
===========================================================================
VALIDATION  /home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0029.json  |  dhatu=pard (parda~ kutsite Sabde)
===========================================================================
✓ tokens: 978  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0030
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0030.json  |  dhatu=yatI (yatI~ prayatne)
===========================================================================
✓ tokens: 14105  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0031
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0031.json  |  dhatu=yut (yutf~ BAsane)
===========================================================================
✓ tokens: 1357  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0032
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0032.json  |  dhatu=jut (jutf~ BAsane)
===========================================================================
✓ tokens: 1358  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0033
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0033.json  |  dhatu=viT (viTf~ yAcane)
===========================================================================
✓ tokens: 1358  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0034
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0034.json  |  dhatu=veT (veTf~ yAcane)
===========================================================================
✓ tokens: 960  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0035
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0035.json  |  dhatu=SraTi (SraTi~ SETilye)
===========================================================================
✓ tokens: 974  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0036
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0036.json  |  dhatu=graTi (graTi~ kOwilye)
===========================================================================
✓ tokens: 1884  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0037
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0037.json  |  dhatu=katT (katTa~ SlAGAyAm)
===========================================================================
✓ tokens: 1897  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0039
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0039.json  |  dhatu=citI (citI~ saMjYAne)
===========================================================================
✓ tokens: 3013  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0040
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0040.json  |  dhatu=cyutir (cyuti~r Asecane)
===========================================================================
✓ tokens: 1557  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0041
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0041.json  |  dhatu=Scutir (Scuti~r Asecane)
===========================================================================
✓ tokens: 1555  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0042
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0042.json  |  dhatu=Scyutir (Scyuti~r kzaraRe)
===========================================================================
✓ tokens: 1557  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0043
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0043.json  |  dhatu=jyut (jyutf~ BAsane)
===========================================================================
✓ tokens: 1543  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0044
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0044.json  |  dhatu=maTi (maTi~ hiMsAsaNkleSanayoH)
===========================================================================
✓ tokens: 1088  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0045
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0045.json  |  dhatu=kuTi (kuTi~ hiMsAsaNkleSanayoH)
===========================================================================
✓ tokens: 1088  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0046
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0046.json  |  dhatu=puTi (puTi~ hiMsAsaNkleSanayoH)
===========================================================================
✓ tokens: 1088  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0047
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0047.json  |  dhatu=luTi (luTi~ hiMsAsaNkleSanayoH)
===========================================================================
✓ tokens: 1087  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0051
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0051.json  |  dhatu=KAd (KAdf~ BakzaRe)
===========================================================================
✓ tokens: 2877  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0054
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0054.json  |  dhatu=gad (gada~ vyaktAyAM vAci)
===========================================================================
✓ tokens: 8469  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0058
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0058.json  |  dhatu=nard (narda~ Sabde)
===========================================================================
✓ tokens: 3082  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0059
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0059.json  |  dhatu=gard (garda~ Sabde)
===========================================================================
✓ tokens: 1091  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0060
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0060.json  |  dhatu=tard (tarda~ hiMsAyAm)
===========================================================================
✓ tokens: 1091  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0061
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0061.json  |  dhatu=kard (karda~ kutsite Sabde)
===========================================================================
✓ tokens: 1092  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0062
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0062.json  |  dhatu=Kard (Karda~ dandaSUke (sarpadaMSe))
===========================================================================
✓ tokens: 1092  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0066
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0066.json  |  dhatu=bidi (bidi~ avayave)
===========================================================================
✓ tokens: 1090  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0067
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0067.json  |  dhatu=Bidi (Bidi~ avayave)
===========================================================================
✓ tokens: 1088  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0071
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0071.json  |  dhatu=cadi (cadi~ AhlAde dIptO ca)
===========================================================================
✓ tokens: 1091  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0072
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0072.json  |  dhatu=tradi (tradi~ cezwAyAm)
===========================================================================
✓ tokens: 1089  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0073
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0073.json  |  dhatu=kadi (kadi~ AhvAne rodane ca)
===========================================================================
✓ tokens: 1091  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0074
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0074.json  |  dhatu=kradi (kradi~ AhvAne rodane ca)
===========================================================================
✓ tokens: 6167  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0075
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0075.json  |  dhatu=kladi (kladi~ AhvAne rodane ca)
===========================================================================
✓ tokens: 1091  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0076
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0076.json  |  dhatu=klidi (klidi~ paridevane)
===========================================================================
✓ tokens: 1091  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0096
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0096.json  |  dhatu=kuk (kuka~ AdAne)
===========================================================================
✓ tokens: 1356  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0106
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0106.json  |  dhatu=vask (vaska~ gatO)
===========================================================================
✓ tokens: 959  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0107
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0107.json  |  dhatu=mask (maska~ gatO)
===========================================================================
✓ tokens: 959  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0108
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0108.json  |  dhatu=wik (wikf~ gatO)
===========================================================================
✓ tokens: 1356  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0110
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0110.json  |  dhatu=tik (tikf~ gatO)
===========================================================================
✓ tokens: 1356  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0114
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0114.json  |  dhatu=zvakk (zvakka~ gatO)
===========================================================================
✓ tokens: 956  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0119
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0119.json  |  dhatu=lAG (lAGf~ sAmarTye)
===========================================================================
✓ tokens: 1851  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0122
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0122.json  |  dhatu=SlAG (SlAGf~ katTane)
===========================================================================
✓ tokens: 963  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0123
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0123.json  |  dhatu=Pakk (Pakka~ nIcErgatO)
===========================================================================
✓ tokens: 1074  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0127
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0127.json  |  dhatu=Suk (Suka~ gatO)
===========================================================================
✓ tokens: 1542  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0131
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0131.json  |  dhatu=lAK (lAKf~ SozaRAlamarTayoH)
===========================================================================
✓ tokens: 1073  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0134
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0134.json  |  dhatu=SAK (SAKf~ vyAptO)
===========================================================================
✓ tokens: 1073  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0135
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0135.json  |  dhatu=SlAK (SlAKf~ vyAptO)
===========================================================================
✓ tokens: 1073  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0152
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0152.json  |  dhatu=valg (valga~ gatO)
===========================================================================
✓ tokens: 3071  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0180
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0180.json  |  dhatu=GagG (GagGa~ hasane)
===========================================================================
✓ tokens: 1067  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0186
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0186.json  |  dhatu=varc (varca~ dIptO)
===========================================================================
✓ tokens: 967  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0204
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0204.json  |  dhatu=Brej (Brejf~ dIptO)
===========================================================================
✓ tokens: 966  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0205
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0205.json  |  dhatu=BrAj (BrAjf~ dIptO)
===========================================================================
✓ tokens: 975  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0206
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0206.json  |  dhatu=kAq (kAqf~ anAdare)
===========================================================================
✓ tokens: 968  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0208
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0208.json  |  dhatu=peb (pebf sevane)
===========================================================================
✓ tokens: 956  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0209
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0209.json  |  dhatu=pleb (plebf~ sevane)
===========================================================================
✓ tokens: 955  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0210
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0210.json  |  dhatu=Suc (Suca~ Soke)
===========================================================================
✓ tokens: 5910  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0211
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0211.json  |  dhatu=kuc (kuca~ Sabde tAre)
===========================================================================
✓ tokens: 1545  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0230
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0230.json  |  dhatu=guj (guja~ avyakte Sabde)
===========================================================================
✓ tokens: 1542  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0257
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0257.json  |  dhatu=zarj (zarja~ arjane)
===========================================================================
✓ tokens: 1111  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0258
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0258.json  |  dhatu=garj (garja~ Sabde)
===========================================================================
✓ tokens: 6880  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0259
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0259.json  |  dhatu=tarj (tarja~ Bartsane)
===========================================================================
✓ tokens: 3886  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0260
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0260.json  |  dhatu=karj (karja~ vyaTane)
===========================================================================
✓ tokens: 1074  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0261
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0261.json  |  dhatu=Karj (Karja~ vyaTane pUjane mArjane ca)
===========================================================================
✓ tokens: 1074  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0273
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0273.json  |  dhatu=lAj (lAja~ Barjane Bartsane ca)
===========================================================================
✓ tokens: 1082  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0277
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0277.json  |  dhatu=tuj (tuja~ hiMsAyAm)
===========================================================================
✓ tokens: 1556  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0283
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0283.json  |  dhatu=muj (muja~ Sabde)
===========================================================================
✓ tokens: 1556  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0288
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0288.json  |  dhatu=vezw (vezwa~ vezwane)
===========================================================================
✓ tokens: 10199  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0289
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0289.json  |  dhatu=cezw (cezwa~ cezwAyAm)
===========================================================================
✓ tokens: 3581  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0292
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0292.json  |  dhatu=Gaww (Gawwa~ calane)
===========================================================================
✓ tokens: 6246  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0318
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0318.json  |  dhatu=heq (heqf~ anAdare)
===========================================================================
✓ tokens: 959  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0320
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0320.json  |  dhatu=bAq (bAqf~ AplAvye)
===========================================================================
✓ tokens: 960  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0321
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0321.json  |  dhatu=vAq (vAqf~ AplAvye)
===========================================================================
✓ tokens: 956  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0322
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0322.json  |  dhatu=drAq (drAqf~ viSaraRe)
===========================================================================
✓ tokens: 960  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0323
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0323.json  |  dhatu=DrAq (DrAqf~ viSaraRe)
===========================================================================
✓ tokens: 959  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0324
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0324.json  |  dhatu=SAq (SAqf~ SlAGAyAm)
===========================================================================
✓ tokens: 960  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0327
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0327.json  |  dhatu=meq (meqf~ unmAde)
===========================================================================
✓ tokens: 1070  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0328
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0328.json  |  dhatu=mreq (mreqf~ unmAde)
===========================================================================
✓ tokens: 2078  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0329
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0329.json  |  dhatu=mlew (mlewf~ unmAde)
===========================================================================
✓ tokens: 1074  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0338
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0338.json  |  dhatu=kiw (kiwa~ trAse)
===========================================================================
✓ tokens: 1546  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0339
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0339.json  |  dhatu=Kiw (Kiwa~ trAse)
===========================================================================
✓ tokens: 1546  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0340
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0340.json  |  dhatu=Siw (Siwa~ anAdare)
===========================================================================
✓ tokens: 1545  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0348
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0348.json  |  dhatu=piw (piwa~ SabdasaNGAtayoH)
===========================================================================
✓ tokens: 1545  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0351
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0351.json  |  dhatu=luw (luwa~ viloqane)
===========================================================================
✓ tokens: 1546  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0352
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0352.json  |  dhatu=luq (luqa~ viloqane)
===========================================================================
✓ tokens: 7357  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0353
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0353.json  |  dhatu=ciw (ciwa~ paraprEzye)
===========================================================================
✓ tokens: 1546  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0354
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0354.json  |  dhatu=viw (viwa~ Sabde)
===========================================================================
✓ tokens: 1546  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0355
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0355.json  |  dhatu=biw (biwa~ AkroSe)
===========================================================================
✓ tokens: 1546  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0356
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0356.json  |  dhatu=hiw (hiwa~ AkroSe)
===========================================================================
✓ tokens: 1544  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0358
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0358.json  |  dhatu=kiw (kiwa~ gatO)
===========================================================================
✓ tokens: 1545  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0364
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0364.json  |  dhatu=muq (muqa~ mardane)
===========================================================================
✓ tokens: 1546  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0365
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0365.json  |  dhatu=pruq (pruqa~ mardane vimardane)
===========================================================================
✓ tokens: 1545  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0366
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0366.json  |  dhatu=muw (muwa~ mardane)
===========================================================================
✓ tokens: 1542  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0367
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0367.json  |  dhatu=puq (puqa~ mardane)
===========================================================================
✓ tokens: 1542  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0389
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0389.json  |  dhatu=ruW (ruWa~ upaGAte)
===========================================================================
✓ tokens: 1546  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0390
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0390.json  |  dhatu=luW (luWa~ upaGAte)
===========================================================================
✓ tokens: 1546  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0393
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0393.json  |  dhatu=piW (piWa~ hiMsAsaNkleSanayoH)
===========================================================================
✓ tokens: 1545  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0395
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0395.json  |  dhatu=SuW (SuWa~ pratiGAte gatipratiGAte ca)
===========================================================================
✓ tokens: 1546  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0404
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0404.json  |  dhatu=kaqq (kaqqa~ kArkaSye)
===========================================================================
✓ tokens: 1091  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0406
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0406.json  |  dhatu=tuq (tuqf~ toqane)
===========================================================================
✓ tokens: 1546  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0408
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0408.json  |  dhatu=huq (huqf~ gatO)
===========================================================================
✓ tokens: 1546  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0421
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0421.json  |  dhatu=tep (tepf~ kzaraRe kampane ca)
===========================================================================
✓ tokens: 959  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0424
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0424.json  |  dhatu=glep (glepf~ dEnye)
===========================================================================
✓ tokens: 958  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0426
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0426.json  |  dhatu=kep (kepf~ kampane gatO ca)
===========================================================================
✓ tokens: 959  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0427
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0427.json  |  dhatu=gep (gepf~ kampane gatO ca)
===========================================================================
✓ tokens: 958  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0428
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0428.json  |  dhatu=glep (glepf~ kampane gatO ca)
===========================================================================
✓ tokens: 959  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0429
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0429.json  |  dhatu=mep (mepf~ gatO)
===========================================================================
✓ tokens: 958  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0431
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0431.json  |  dhatu=lep (lepf~ gatO)
===========================================================================
✓ tokens: 958  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0432
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0432.json  |  dhatu=hep (hepf~ gatO)
===========================================================================
✓ tokens: 955  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0433
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0433.json  |  dhatu=Dep (Depf~ gatO)
===========================================================================
✓ tokens: 955  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0455
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0455.json  |  dhatu=SalB (SalBa~ katTane)
===========================================================================
✓ tokens: 955  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0456
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0456.json  |  dhatu=valB (valBa~ Bojane)
===========================================================================
✓ tokens: 955  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0457
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0457.json  |  dhatu=galB (galBa~ DArzwye)
===========================================================================
✓ tokens: 955  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0464
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0464.json  |  dhatu=jalp (jalpa~ vyaktAyAM vAci)
===========================================================================
✓ tokens: 5914  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0469
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0469.json  |  dhatu=cup (cupa~ mandAyAM gatO)
===========================================================================
✓ tokens: 1546  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0470
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0470.json  |  dhatu=tup (tupa~ hiMsAyAm)
===========================================================================
✓ tokens: 1546  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0474
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0474.json  |  dhatu=tuP (tuPa~ hiMsAyAm)
===========================================================================
✓ tokens: 1545  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0500
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0500.json  |  dhatu=SuB (SuBa~ BAzaRe BAsane hiMsAyAM ca)
===========================================================================
✓ tokens: 1543  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0505
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0505.json  |  dhatu=GuR (GuRa~ BramaRe)
===========================================================================
✓ tokens: 1358  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0506
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0506.json  |  dhatu=GurR (GurRa~ BramaRe)
===========================================================================
✓ tokens: 2746  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0509
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0509.json  |  dhatu=BAm (BAma~ kroDe)
===========================================================================
✓ tokens: 959  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0527
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0527.json  |  dhatu=pER (pERf~ gatipreraRaSlezaRezu)
===========================================================================
✓ tokens: 1073  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0528
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0528.json  |  dhatu=prER (prERf~ gatipreraRaSlezaRezu)
===========================================================================
✓ tokens: 1071  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0711
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0711.json  |  dhatu=BAs (BAsf~ dIptO)
===========================================================================
✓ tokens: 2819  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0713
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0713.json  |  dhatu=rAs (rAsf~ Sabde)
===========================================================================
✓ tokens: 960  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0734
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0734.json  |  dhatu=kAS (kASf~ dIptO)
===========================================================================
✓ tokens: 13324  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0807
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0807.json  |  dhatu=tus (tusa~ Sabde)
===========================================================================
✓ tokens: 1546  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0813
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0813.json  |  dhatu=jarj (jarja~ pariBAzaRahiMsAtarjanezu)
===========================================================================
✓ tokens: 1081  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0814
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0814.json  |  dhatu=carc (carca~ pariBAzaRahiMsAtarjanezu)
===========================================================================
✓ tokens: 1082  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0815
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0815.json  |  dhatu=JarJ (JarJa~ pariBAzaRahiMsAtarjanezu)
===========================================================================
✓ tokens: 1070  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0816
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0816.json  |  dhatu=pis (pisf~ gatO)
===========================================================================
✓ tokens: 1549  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0817
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0817.json  |  dhatu=pes (pesf~ gatO)
===========================================================================
✓ tokens: 1075  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0818
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0818.json  |  dhatu=vis (visf~ gatO)
===========================================================================
✓ tokens: 1543  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0819
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0819.json  |  dhatu=ves (vesf~ gatO)
===========================================================================
✓ tokens: 1071  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0820
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0820.json  |  dhatu=piS (piSf~ gatO)
===========================================================================
✓ tokens: 1542  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0821
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0821.json  |  dhatu=peS (peSf~ gatO)
===========================================================================
✓ tokens: 1070  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0824
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0824.json  |  dhatu=miS (miSa~ Sabde rozakfte gatO ca)
===========================================================================
✓ tokens: 1546  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0847
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0847.json  |  dhatu=ruc (ruca~ dIptAvaBiprItO ca)
===========================================================================
✓ tokens: 13064  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0848
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0848.json  |  dhatu=Guw (Guwa~ parivartane)
===========================================================================
✓ tokens: 1370  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0849
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0849.json  |  dhatu=ruw (ruwa~ pratiGAte)
===========================================================================
✓ tokens: 1368  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0850
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0850.json  |  dhatu=luw (luwa~ pratiGAte)
===========================================================================
✓ tokens: 1369  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0851
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0851.json  |  dhatu=luW (luWa~ pratiGAte)
===========================================================================
✓ tokens: 1369  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0853
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0853.json  |  dhatu=SuB (SuBa~ dIptO)
===========================================================================
✓ tokens: 2764  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0856
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0856.json  |  dhatu=tuB (tuBa~ hiMsAyAm)
===========================================================================
✓ tokens: 1367  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0878
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0878.json  |  dhatu=kadi (kadi~ vEklavye)
===========================================================================
✓ tokens: 979  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0879
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0879.json  |  dhatu=kradi (kradi~ vEklavye)
===========================================================================
✓ tokens: 979  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0880
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0880.json  |  dhatu=kladi (kladi~ vEklavye)
===========================================================================
✓ tokens: 979  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  883/883  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0947
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0947.json  |  dhatu=mleq (mleqf~ unmAde)
===========================================================================
✓ tokens: 1071  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0948
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0948.json  |  dhatu=mew (mewf~ unmAde)
===========================================================================
✓ tokens: 1070  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0949
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0949.json  |  dhatu=biq (biqa~ AkroSe)
===========================================================================
✓ tokens: 2996  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0956
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0956.json  |  dhatu=rAj (rAjf~ dIptO)
===========================================================================
✓ tokens: 10071  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0993
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0993.json  |  dhatu=kuc (kuca~ samparcanakOwilyapratizwamBavileKanezu)
===========================================================================
✓ tokens: 6980  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.0994
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.0994.json  |  dhatu=buD (buDa~ avagamane)
===========================================================================
✓ tokens: 14329  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.1002
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.1002.json  |  dhatu=rew (rewf~ pariBAzaRe)
===========================================================================
✓ tokens: 1137  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.1007
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.1007.json  |  dhatu=med (medf~ meDAhiMsanayoH saNgame ca)
===========================================================================
✓ tokens: 1139  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.1008
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.1008.json  |  dhatu=miT (miTf~ meDAhiMsanayoH)
===========================================================================
✓ tokens: 1640  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.1009
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.1009.json  |  dhatu=meT (meTf~ meDAhiMsanayoH)
===========================================================================
✓ tokens: 1136  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.1010
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.1010.json  |  dhatu=miD (miDf~ meDAhiMsanayoH)
===========================================================================
✓ tokens: 1637  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.1011
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.1011.json  |  dhatu=meD (meDf~ meDAhiMsanayoH saNgame ca)
===========================================================================
✓ tokens: 2201  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.1016
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.1016.json  |  dhatu=buDir (buDi~r boDane)
===========================================================================
✓ tokens: 12221  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.1018
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.1018.json  |  dhatu=veR (veRf~ gatijYAnacintAniSAmanavAditragrahaRezu)
===========================================================================
✓ tokens: 1136  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.1019
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.1019.json  |  dhatu=ven (venf~ gatijYAnacintAniSAmanavAditragrahaRezu)
===========================================================================
✓ tokens: 1134  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.1025
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.1025.json  |  dhatu=dAS (dASf~ dAne)
===========================================================================
✓ tokens: 4285  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
### 01.1041
```
===========================================================================
VALIDATION  D:\Data\skt-morph-data\data\01\01.1041.json  |  dhatu=dAs (dAsf~ dAne)
===========================================================================
✓ tokens: 1139  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yak] sanadi=None prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san_yak] sanadi=sannanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [nich_yak] sanadi=nijanta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang] sanadi=yananta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yang_yak] sanadi=yananta prayoga=karmani
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [yangluk] sanadi=yanluganta prayoga=kartari
    ✓ lw        9/ 9

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ✓ lw        9/ 9

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 32/32
  ✓ san_krut     (sannanta  ) 32/32
  ✓ nich_krut    (nijanta   ) 32/32
  ✓ yang_krut    (yananta   ) 29/29
  ✓ yangluk_krut (yanluganta) 32/32
---------------------------------------------------------------------------
GRAND  895/895  (100.0%)  ✓ ALL MATCHED
===========================================================================
```
