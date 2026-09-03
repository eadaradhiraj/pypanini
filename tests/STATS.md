# Generative Validation Stats

Engine: wholly generative (tinanta/krdanta derive from pada/sew/gana, no hardcoded dicts)
Cross-check: skt-morph-data JSON (read-only)
Date: 2026-09-03T09:18:15Z
Run: python -m unittest tests.test_dhatu -v | python tests/test_dhatu.py <id>

```
test_01_0001_BU (tests.test_dhatu.TestDhatuGenerative.test_01_0001_BU) ... ok
test_01_0002_eD (tests.test_dhatu.TestDhatuGenerative.test_01_0002_eD) ... ok
test_01_0003_sparD (tests.test_dhatu.TestDhatuGenerative.test_01_0003_sparD) ... ok
test_cli (tests.test_dhatu.TestDhatuGenerative.test_cli) ... ok

----------------------------------------------------------------------
Ran 4 tests in 17.569s

OK
```

## Per-dhatu (tests/test_dhatu.py)

### 01.0001
```
===========================================================================
VALIDATION  /home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0001.json  |  dhatu=BU (BU sattAyAm)
===========================================================================
✓ tokens: 82577  engine: generative (no hardcoded dict)

-- tinanta (10 lakaras, 9 purusha/vacana) --
  ✓ lw        9/ 9
  ✓ liw       9/ 9
  ✓ luw       9/ 9
  ✓ lfw       9/ 9
  ✓ low       9/ 9
  ✓ laN       9/ 9
  ✓ viDiliN   9/ 9
  ✓ ASIrliN   9/ 9
  ✓ luN       9/ 9
  ✓ lfN       9/ 9

-- krdanta (tri-linga + avyaya) --
---------------------------------------------------------------------------
GRAND  122/122  (100.0%)  ✓ ALL MATCHED
===========================================================================
```

### 01.0002
```
===========================================================================
VALIDATION  /home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0002.json  |  dhatu=eD (eDa~ vfdDO)
===========================================================================
✓ tokens: 1436  engine: generative (no hardcoded dict)

-- tinanta (10 lakaras, 9 purusha/vacana) --
  ✓ lw        9/ 9
  ✓ liw       9/ 9
  ✓ luw       9/ 9
  ✓ lfw       9/ 9
  ✓ low       9/ 9
  ✓ laN       9/ 9
  ✓ viDiliN   9/ 9
  ✓ ASIrliN   9/ 9
  ✓ luN       9/ 9
  ✓ lfN       9/ 9

-- krdanta (tri-linga + avyaya) --
---------------------------------------------------------------------------
GRAND  119/119  (100.0%)  ✓ ALL MATCHED
===========================================================================
```

### 01.0003
```
===========================================================================
VALIDATION  /home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0003.json  |  dhatu=sparD (sparDa~ saNGarze)
===========================================================================
✓ tokens: 3754  engine: generative (no hardcoded dict)

-- tinanta (10 lakaras, 9 purusha/vacana) --
  ✓ lw        9/ 9
  ✓ liw       9/ 9
  ✓ luw       9/ 9
  ✓ lfw       9/ 9
  ✓ low       9/ 9
  ✓ laN       9/ 9
  ✓ viDiliN   9/ 9
  ✓ ASIrliN   9/ 9
  ✓ luN       9/ 9
  ✓ lfN       9/ 9

-- krdanta (tri-linga + avyaya) --
---------------------------------------------------------------------------
GRAND  119/119  (100.0%)  ✓ ALL MATCHED
===========================================================================
```

### 01.0004
```
===========================================================================
VALIDATION  /home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0004.json  |  dhatu=gAD (gADf~ pratizWAlipsayorgranTe ca)
===========================================================================
✓ tokens: 1915  engine: generative (no hardcoded dict)

-- tinanta (10 lakaras, 9 purusha/vacana) --
  ✓ lw        9/ 9
  ✓ liw       9/ 9
  ✓ luw       9/ 9
  ✓ lfw       9/ 9
  ✓ low       9/ 9
  ✓ laN       9/ 9
  ✓ viDiliN   9/ 9
  ✓ ASIrliN   9/ 9
  ✓ luN       9/ 9
  ✓ lfN       9/ 9

-- krdanta (tri-linga + avyaya) --
---------------------------------------------------------------------------
GRAND  119/119  (100.0%)  ✓ ALL MATCHED
===========================================================================
```

### 01.0005
```
===========================================================================
VALIDATION  /home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0005.json  |  dhatu=bAD (bADf~ loqane, rowane)
===========================================================================
✓ tokens: 26470  engine: generative (no hardcoded dict)

-- tinanta (10 lakaras, 9 purusha/vacana) --
  ✓ lw        9/ 9
  ✓ liw       9/ 9
  ✓ luw       9/ 9
  ✓ lfw       9/ 9
  ✓ low       9/ 9
  ✓ laN       9/ 9
  ✓ viDiliN   9/ 9
  ✓ ASIrliN   9/ 9
  ✓ luN       9/ 9
  ✓ lfN       9/ 9

-- krdanta (tri-linga + avyaya) --
---------------------------------------------------------------------------
GRAND  119/119  (100.0%)  ✓ ALL MATCHED
===========================================================================
```

### 01.0006
```
===========================================================================
VALIDATION  /home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0006.json  |  dhatu=nAD (nADf~ yAcYopatApESvaryASIzzu)
===========================================================================
✓ tokens: 1911  engine: generative (no hardcoded dict)

-- tinanta (10 lakaras, 9 purusha/vacana) --
  ✓ lw        9/ 9
  ✓ liw       9/ 9
  ✓ luw       9/ 9
  ✓ lfw       9/ 9
  ✓ low       9/ 9
  ✓ laN       9/ 9
  ✓ viDiliN   9/ 9
  ✓ ASIrliN   9/ 9
  ✓ luN       9/ 9
  ✓ lfN       9/ 9

-- krdanta (tri-linga + avyaya) --
---------------------------------------------------------------------------
GRAND  119/119  (100.0%)  ✓ ALL MATCHED
===========================================================================
```

### 01.0007
```
===========================================================================
VALIDATION  /home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0007.json  |  dhatu=nAT (nATf~ yAcYopatApESvaryASIzzu)
===========================================================================
✓ tokens: 4415  engine: generative (no hardcoded dict)

-- tinanta (10 lakaras, 9 purusha/vacana) --
  ✓ lw        9/ 9
  ✓ liw       9/ 9
  ✓ luw       9/ 9
  ✓ lfw       9/ 9
  ✓ low       9/ 9
  ✓ laN       9/ 9
  ✓ viDiliN   9/ 9
  ✓ ASIrliN   9/ 9
  ✓ luN       9/ 9
  ✓ lfN       9/ 9

-- krdanta (tri-linga + avyaya) --
---------------------------------------------------------------------------
GRAND  119/119  (100.0%)  ✓ ALL MATCHED
===========================================================================
```

