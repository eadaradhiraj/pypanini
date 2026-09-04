# Generative Validation Stats

Engine: wholly generative (tinanta/krdanta derive from pada/sew/gana, no hardcoded dicts, expanded 10 antas)
Cross-check: skt-morph-data JSON (read-only)
Date: 2026-09-04T10:10:29Z
Run: python -W ignore::ResourceWarning -m unittest tests.test_dhatu -v (10 antas ×10 lakaras ×9 + 5 krdanta antas)

```
test_01_0001_BU (tests.test_dhatu.TestDhatuGenerative.test_01_0001_BU) ... ok
test_01_0002_eD (tests.test_dhatu.TestDhatuGenerative.test_01_0002_eD) ... ok
test_01_0003_sparD (tests.test_dhatu.TestDhatuGenerative.test_01_0003_sparD) ... ok
test_cli (tests.test_dhatu.TestDhatuGenerative.test_cli) ... ok

----------------------------------------------------------------------
Ran 4 tests in 17.703s

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
