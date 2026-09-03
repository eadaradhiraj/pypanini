# Generative Validation Stats

Engine: wholly generative (tinanta/krdanta derive from pada/sew/gana, no hardcoded dicts, expanded 10 antas)
Cross-check: skt-morph-data JSON (read-only)
Date: 2026-09-03T11:18:37.021611Z
Run: python -W ignore::ResourceWarning -m unittest tests.test_dhatu -v (10 antas ×10 lakaras ×9 + 5 krdanta antas)

```
test_01_0001_BU (tests.test_dhatu.TestDhatuGenerative.test_01_0001_BU) ... ok
test_01_0002_eD (tests.test_dhatu.TestDhatuGenerative.test_01_0002_eD) ... ok
test_01_0003_sparD (tests.test_dhatu.TestDhatuGenerative.test_01_0003_sparD) ... ok
test_cli (tests.test_dhatu.TestDhatuGenerative.test_cli) ... ok

----------------------------------------------------------------------
Ran 4 tests in 16.842s

OK

```

## Per-dhatu (tests/test_dhatu.py -W ignore)

### 01.0001
```
===========================================================================
VALIDATION  /home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0001.json  |  dhatu=BU (BU sattAyAm)
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
VALIDATION  /home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0002.json  |  dhatu=eD (eDa~ vfdDO)
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
VALIDATION  /home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0003.json  |  dhatu=sparD (sparDa~ saNGarze)
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
VALIDATION  /home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0004.json  |  dhatu=gAD (gADf~ pratizWAlipsayorgranTe ca)
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
VALIDATION  /home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0005.json  |  dhatu=bAD (bADf~ loqane, rowane)
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
VALIDATION  /home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0006.json  |  dhatu=nAD (nADf~ yAcYopatApESvaryASIzzu)
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
VALIDATION  /home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0007.json  |  dhatu=nAT (nATf~ yAcYopatApESvaryASIzzu)
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
VALIDATION  /home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0008.json  |  dhatu=daD (daDa~ DAraRe)
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
VALIDATION  /home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0009.json  |  dhatu=skudi (skudi~ ApravaRe)
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
    ⚠ luN       8/ 9  e.g. ('prathama eka', 'askundayizwa')
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
    ⚠ lw        0/ 9  e.g. ('prathama eka', 'cAskundaH')

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ⚠ lw        0/ 9  e.g. ('prathama eka', 'cAskundaH')

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ⚠ yang_krut    (yananta   )  0/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  835/883  (94.6%)  ⚠ missing
===========================================================================
```

### 01.0010
```
===========================================================================
VALIDATION  /home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0010.json  |  dhatu=Svidi (Svidi~ SvEtye)
===========================================================================
✓ tokens: 975  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ✓ lw        9/ 9
    ⚠ liw       0/ 9  e.g. ('prathama eka', 'saSvinde')
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
    ⚠ liw       0/ 9  e.g. ('prathama eka', 'saSvinde')
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ✓ luN       9/ 9
    ✓ lfN       9/ 9

  [san] sanadi=sannanta prayoga=kartari
    ⚠ lw        0/ 9  e.g. ('prathama eka', 'Suskundizate')
    ⚠ liw       0/ 9  e.g. ('prathama eka', 'SuskundizAYcakre')
    ⚠ luw       0/ 9  e.g. ('prathama eka', 'SuskundizitA')
    ⚠ lfw       0/ 9  e.g. ('prathama eka', 'Suskundizizyate')
    ⚠ low       0/ 9  e.g. ('prathama eka', 'SuskundizatAm')
    ⚠ laN       0/ 9  e.g. ('prathama eka', 'aSuskundizata')
    ⚠ viDiliN   0/ 9  e.g. ('prathama eka', 'Suskundizeta')
    ⚠ ASIrliN   0/ 9  e.g. ('prathama eka', 'SuskundizizIzwa')
    ⚠ luN       0/ 9  e.g. ('prathama eka', 'aSuskundizizwa')
    ⚠ lfN       0/ 9  e.g. ('prathama eka', 'aSuskundizizyata')

  [san_yak] sanadi=sannanta prayoga=karmani
    ⚠ lw        0/ 9  e.g. ('prathama eka', 'Suskundizyate')
    ⚠ liw       0/ 9  e.g. ('prathama eka', 'SuskundizAYcakre')
    ⚠ luw       0/ 9  e.g. ('prathama eka', 'SuskundizitA')
    ⚠ lfw       0/ 9  e.g. ('prathama eka', 'Suskundizizyate')
    ⚠ low       0/ 9  e.g. ('prathama eka', 'SuskundizyatAm')
    ⚠ laN       0/ 9  e.g. ('prathama eka', 'aSuskundizyata')
    ⚠ viDiliN   0/ 9  e.g. ('prathama eka', 'Suskundizyeta')
    ⚠ ASIrliN   0/ 9  e.g. ('prathama eka', 'SuskundizizIzwa')
    ⚠ luN       0/ 9  e.g. ('prathama eka', 'aSuskundizi')
    ⚠ lfN       0/ 9  e.g. ('prathama eka', 'aSuskundizizyata')

  [nich] sanadi=nijanta prayoga=kartari
    ✓ lw        9/ 9
    ✓ liw       9/ 9
    ✓ luw       9/ 9
    ✓ lfw       9/ 9
    ✓ low       9/ 9
    ✓ laN       9/ 9
    ✓ viDiliN   9/ 9
    ✓ ASIrliN   9/ 9
    ⚠ luN       8/ 9  e.g. ('prathama eka', 'aSvindayizwa')
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
    ⚠ lw        0/ 9  e.g. ('prathama eka', 'SoSvindyate')
    ⚠ liw       0/ 9  e.g. ('prathama eka', 'SoSvindAYcakre')
    ⚠ luw       0/ 9  e.g. ('prathama eka', 'SoSvinditA')
    ⚠ lfw       0/ 9  e.g. ('prathama eka', 'SoSvindizyate')
    ⚠ low       0/ 9  e.g. ('prathama eka', 'SoSvindyatAm')
    ⚠ laN       0/ 9  e.g. ('prathama eka', 'aSoSvindyata')
    ⚠ viDiliN   0/ 9  e.g. ('prathama eka', 'SoSvindyeta')
    ⚠ ASIrliN   0/ 9  e.g. ('prathama eka', 'SoSvindizIzwa')
    ⚠ luN       0/ 9  e.g. ('prathama eka', 'aSoSvindizwa')
    ⚠ lfN       0/ 9  e.g. ('prathama eka', 'aSoSvindizyata')

  [yang_yak] sanadi=yananta prayoga=karmani
    ⚠ lw        0/ 9  e.g. ('prathama eka', 'SoSvindyate')
    ⚠ liw       0/ 9  e.g. ('prathama eka', 'SoSvindAYcakre')
    ⚠ luw       0/ 9  e.g. ('prathama eka', 'SoSvinditA')
    ⚠ lfw       0/ 9  e.g. ('prathama eka', 'SoSvindizyate')
    ⚠ low       0/ 9  e.g. ('prathama eka', 'SoSvindyatAm')
    ⚠ laN       0/ 9  e.g. ('prathama eka', 'aSoSvindyata')
    ⚠ viDiliN   0/ 9  e.g. ('prathama eka', 'SoSvindyeta')
    ⚠ ASIrliN   0/ 9  e.g. ('prathama eka', 'SoSvindizIzwa')
    ⚠ luN       0/ 9  e.g. ('prathama eka', 'aSoSvindizwa')
    ⚠ lfN       0/ 9  e.g. ('prathama eka', 'aSoSvindizyata')

  [yangluk] sanadi=yanluganta prayoga=kartari
    ⚠ lw        0/ 9  e.g. ('prathama eka', 'sASvindi')

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ⚠ lw        0/ 9  e.g. ('prathama eka', 'sASvindi')

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ⚠ san_krut     (sannanta  )  0/29
  ✓ nich_krut    (nijanta   ) 29/29
  ⚠ yang_krut    (yananta   )  0/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  428/883  (48.5%)  ⚠ missing
===========================================================================
```
