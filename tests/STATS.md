# Generative Validation Stats

Engine: wholly generative (tinanta/krdanta derive from pada/sew/gana, no hardcoded dicts, expanded 10 antas)
Cross-check: skt-morph-data JSON (read-only)
Date: 2026-09-03T12:25:39.976409Z
Run: python -W ignore::ResourceWarning -m unittest tests.test_dhatu -v (10 antas ×10 lakaras ×9 + 5 krdanta antas)

```
test_01_0001_BU (tests.test_dhatu.TestDhatuGenerative.test_01_0001_BU) ... ok
test_01_0002_eD (tests.test_dhatu.TestDhatuGenerative.test_01_0002_eD) ... ok
test_01_0003_sparD (tests.test_dhatu.TestDhatuGenerative.test_01_0003_sparD) ... ok
test_cli (tests.test_dhatu.TestDhatuGenerative.test_cli) ... ok

----------------------------------------------------------------------
Ran 4 tests in 15.903s

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
VALIDATION  /home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0010.json  |  dhatu=Svidi (Svidi~ SvEtye)
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
    ⚠ luN       3/ 9  e.g. ('madhyama eka', 'aSvindayizwa')
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
    ⚠ lw        0/ 9  e.g. ('prathama eka', 'SiSvindti')

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ⚠ lw        0/ 9  e.g. ('prathama eka', 'SiSvindti')

-- krdanta (all antas) --
  ✓ krut         (mUla      ) 29/29
  ✓ san_krut     (sannanta  ) 29/29
  ✓ nich_krut    (nijanta   ) 29/29
  ⚠ yang_krut    (yananta   )  0/29
  ✓ yangluk_krut (yanluganta) 29/29
---------------------------------------------------------------------------
GRAND  830/883  (94.0%)  ⚠ missing
===========================================================================
```

### 01.0011
```
===========================================================================
VALIDATION  /home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0011.json  |  dhatu=vadi (vadi~ aBivAdanastutyoH)
===========================================================================
✓ tokens: 3764  engine: generative (no hardcoded dict)

-- tinanta (10 antas × 10 lakaras × 9) --
   antas: ting, yak, san, san_yak, nich, nich_yak, yang, yang_yak, yangluk, yangluk_yak

  [ting] sanadi=None prayoga=kartari
    ⚠ lw        0/ 9  e.g. ('prathama eka', 'vadayate')
    ⚠ liw       0/ 9  e.g. ('prathama eka', 'vavadie')
    ⚠ luw       0/ 9  e.g. ('prathama eka', 'vadayitA')
    ⚠ lfw       0/ 9  e.g. ('prathama eka', 'vadayizyate')
    ⚠ low       0/ 9  e.g. ('prathama eka', 'vadayatAm')
    ⚠ laN       0/ 9  e.g. ('prathama eka', 'avadayata')
    ⚠ viDiliN   0/ 9  e.g. ('prathama eka', 'vadayeta')
    ⚠ ASIrliN   0/ 9  e.g. ('prathama eka', 'vadiizIzwa')
    ⚠ luN       0/ 9  e.g. ('prathama eka', 'avadiizwa')
    ⚠ lfN       0/ 9  e.g. ('prathama eka', 'avadayizyata')

  [yak] sanadi=None prayoga=karmani
    ⚠ lw        0/ 9  e.g. ('prathama eka', 'vadiyate')
    ⚠ liw       0/ 9  e.g. ('prathama eka', 'vavadie')
    ⚠ luw       0/ 9  e.g. ('prathama eka', 'vadayitA')
    ⚠ lfw       0/ 9  e.g. ('prathama eka', 'vadayizyate')
    ⚠ low       0/ 9  e.g. ('prathama eka', 'vadiyatAm')
    ⚠ laN       0/ 9  e.g. ('prathama eka', 'avadiyata')
    ⚠ viDiliN   0/ 9  e.g. ('prathama eka', 'vadiyeta')
    ⚠ ASIrliN   0/ 9  e.g. ('prathama eka', 'vadayizIzwa')
    ⚠ luN       0/ 9  e.g. ('prathama eka', 'avadayi')
    ⚠ lfN       0/ 9  e.g. ('prathama eka', 'avadayizyata')

  [san] sanadi=sannanta prayoga=kartari
    ⚠ lw        0/ 9  e.g. ('prathama eka', 'vivadizate')
    ⚠ liw       0/ 9  e.g. ('prathama eka', 'vivadizAYcakre')
    ⚠ luw       0/ 9  e.g. ('prathama eka', 'vivadizitA')
    ⚠ lfw       0/ 9  e.g. ('prathama eka', 'vivadizizyate')
    ⚠ low       0/ 9  e.g. ('prathama eka', 'vivadizatAm')
    ⚠ laN       0/ 9  e.g. ('prathama eka', 'avivadizata')
    ⚠ viDiliN   0/ 9  e.g. ('prathama eka', 'vivadizeta')
    ⚠ ASIrliN   0/ 9  e.g. ('prathama eka', 'vivadizizIzwa')
    ⚠ luN       0/ 9  e.g. ('prathama eka', 'avivadizizwa')
    ⚠ lfN       0/ 9  e.g. ('prathama eka', 'avivadizizyata')

  [san_yak] sanadi=sannanta prayoga=karmani
    ⚠ lw        0/ 9  e.g. ('prathama eka', 'vivadizyate')
    ⚠ liw       0/ 9  e.g. ('prathama eka', 'vivadizAYcakre')
    ⚠ luw       0/ 9  e.g. ('prathama eka', 'vivadizitA')
    ⚠ lfw       0/ 9  e.g. ('prathama eka', 'vivadizizyate')
    ⚠ low       0/ 9  e.g. ('prathama eka', 'vivadizyatAm')
    ⚠ laN       0/ 9  e.g. ('prathama eka', 'avivadizyata')
    ⚠ viDiliN   0/ 9  e.g. ('prathama eka', 'vivadizyeta')
    ⚠ ASIrliN   0/ 9  e.g. ('prathama eka', 'vivadizizIzwa')
    ⚠ luN       0/ 9  e.g. ('prathama eka', 'avivadizi')
    ⚠ lfN       0/ 9  e.g. ('prathama eka', 'avivadizizyata')

  [nich] sanadi=nijanta prayoga=kartari
    ⚠ lw        0/ 9  e.g. ('prathama eka', 'vadAyayati')
    ⚠ liw       0/ 9  e.g. ('prathama eka', 'vadAyayAYcakAra')
    ⚠ luw       0/ 9  e.g. ('prathama eka', 'vadAyayitA')
    ⚠ lfw       0/ 9  e.g. ('prathama eka', 'vadAyayizyati')
    ⚠ low       0/ 9  e.g. ('prathama eka', 'vadAyayatu')
    ⚠ laN       0/ 9  e.g. ('prathama eka', 'avadAyayat')
    ⚠ viDiliN   0/ 9  e.g. ('prathama eka', 'vadAyayet')
    ⚠ ASIrliN   0/ 9  e.g. ('prathama eka', 'vadAyayyAt')
    ⚠ luN       0/ 9  e.g. ('prathama eka', 'avadAyayizwa')
    ⚠ lfN       0/ 9  e.g. ('prathama eka', 'avadAyayizyat')

  [nich_yak] sanadi=nijanta prayoga=karmani
    ⚠ lw        0/ 9  e.g. ('prathama eka', 'vadAyyate')
    ⚠ liw       0/ 9  e.g. ('prathama eka', 'vadAyayAYcakre')
    ⚠ luw       0/ 9  e.g. ('prathama eka', 'vadAyitA')
    ⚠ lfw       0/ 9  e.g. ('prathama eka', 'vadAyayizyate')
    ⚠ low       0/ 9  e.g. ('prathama eka', 'vadAyyatAm')
    ⚠ laN       0/ 9  e.g. ('prathama eka', 'avadAyyata')
    ⚠ viDiliN   0/ 9  e.g. ('prathama eka', 'vadAyyeta')
    ⚠ ASIrliN   0/ 9  e.g. ('prathama eka', 'vadAyayizIzwa')
    ⚠ luN       0/ 9  e.g. ('prathama eka', 'avadAyi')
    ⚠ lfN       0/ 9  e.g. ('prathama eka', 'avadAyayizyata')

  [yang] sanadi=yananta prayoga=kartari
    ⚠ lw        0/ 9  e.g. ('prathama eka', 'vAvadiyate')
    ⚠ liw       0/ 9  e.g. ('prathama eka', 'vAvadiAYcakre')
    ⚠ luw       0/ 9  e.g. ('prathama eka', 'vAvadiitA')
    ⚠ lfw       0/ 9  e.g. ('prathama eka', 'vAvadiizyate')
    ⚠ low       0/ 9  e.g. ('prathama eka', 'vAvadiyatAm')
    ⚠ laN       0/ 9  e.g. ('prathama eka', 'avAvadiyata')
    ⚠ viDiliN   0/ 9  e.g. ('prathama eka', 'vAvadiyeta')
    ⚠ ASIrliN   0/ 9  e.g. ('prathama eka', 'vAvadizIzwa')
    ⚠ luN       0/ 9  e.g. ('prathama eka', 'avAvadiizwa')
    ⚠ lfN       0/ 9  e.g. ('prathama eka', 'avAvadiizyata')

  [yang_yak] sanadi=yananta prayoga=karmani
    ⚠ lw        0/ 9  e.g. ('prathama eka', 'vAvadiyate')
    ⚠ liw       0/ 9  e.g. ('prathama eka', 'vAvadiAYcakre')
    ⚠ luw       0/ 9  e.g. ('prathama eka', 'vAvadiitA')
    ⚠ lfw       0/ 9  e.g. ('prathama eka', 'vAvadiizyate')
    ⚠ low       0/ 9  e.g. ('prathama eka', 'vAvadiyatAm')
    ⚠ laN       0/ 9  e.g. ('prathama eka', 'avAvadiyata')
    ⚠ viDiliN   0/ 9  e.g. ('prathama eka', 'vAvadiyeta')
    ⚠ ASIrliN   0/ 9  e.g. ('prathama eka', 'vAvadizIzwa')
    ⚠ luN       0/ 9  e.g. ('prathama eka', 'avAvadiizwa')
    ⚠ lfN       0/ 9  e.g. ('prathama eka', 'avAvadiizyata')

  [yangluk] sanadi=yanluganta prayoga=kartari
    ⚠ lw        0/ 9  e.g. ('prathama eka', 'vAvadiati')

  [yangluk_yak] sanadi=yanluganta prayoga=karmani
    ⚠ lw        0/ 9  e.g. ('prathama eka', 'vAvadiati')

-- krdanta (all antas) --
  ⚠ krut         (mUla      )  0/29
  ⚠ san_krut     (sannanta  )  0/29
  ⚠ nich_krut    (nijanta   )  0/29
  ⚠ yang_krut    (yananta   )  0/29
  ⚠ yangluk_krut (yanluganta)  0/29
---------------------------------------------------------------------------
GRAND  0/883  (0.0%)  ⚠ missing
===========================================================================
```
