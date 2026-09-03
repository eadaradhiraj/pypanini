# Generative Validation Stats

Engine: wholly generative (tinanta/krdanta derive from pada/sew/gana, no hardcoded dicts, expanded 10 antas)
Cross-check: skt-morph-data JSON (read-only)
Date: 2026-09-03T10:04:57.232964Z
Run: python -m unittest tests.test_dhatu -v | python tests/test_dhatu.py <id> (10 antas ×10 lakaras ×9 + 5 krdanta antas)

```
test_01_0001_BU (tests.test_dhatu.TestDhatuGenerative.test_01_0001_BU) ... /home/edhiraj/Documents/projs/pypanini/tests/test_dhatu.py:122: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0001.json' mode='r' encoding='utf-8'>
  d = json.load(open(json_path, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/tests/test_dhatu.py:140: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0001.json' mode='r' encoding='utf-8'>
  data = json.load(open(json_path, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1157.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0983.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0164.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0178.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0067.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0352.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0519.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0937.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0173.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0766.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0970.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0023.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0375.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0693.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0608.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0621.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1050.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1048.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0880.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0074.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0772.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0560.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0213.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0025.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0121.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1090.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0163.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0954.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1000.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0534.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1106.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0947.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0141.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0760.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0832.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1124.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0638.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0331.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0100.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0416.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0419.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1125.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0911.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0980.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0229.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0432.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0580.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0882.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0409.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0588.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1040.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0590.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0189.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1142.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0597.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1023.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0539.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0047.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0031.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0601.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0591.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0573.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1044.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0697.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0487.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0120.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0247.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0266.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0662.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0261.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0977.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0718.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0879.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0912.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0668.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1043.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0678.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1146.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1115.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1094.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0306.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0677.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0969.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0180.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1070.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1024.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0945.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1028.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0208.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0277.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0918.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0467.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0752.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1131.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0237.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0934.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0052.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0493.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0365.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0631.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0812.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0872.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0577.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0029.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0479.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0916.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1010.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0454.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0223.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0664.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0913.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0209.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0433.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1035.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0281.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1036.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0893.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0118.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0652.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0527.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0939.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0390.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0836.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0982.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0395.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0431.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0558.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0547.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0981.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0725.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0599.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0712.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0957.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0092.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0790.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0041.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0548.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0319.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0622.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0294.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0242.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0061.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0474.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0393.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0077.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0380.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0920.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0275.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0187.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0576.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0611.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0535.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0708.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0529.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0072.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0050.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0139.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0552.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0168.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1109.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1056.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0150.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0116.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0475.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0820.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0578.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0507.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1156.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0567.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0800.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0080.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0786.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0899.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0524.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0990.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0108.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0754.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1062.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0174.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0384.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1049.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0706.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0284.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1069.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0892.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0048.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0056.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0736.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0105.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0293.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0406.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1163.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0075.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0093.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0767.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0614.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1073.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0719.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0197.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0615.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1126.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0235.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0374.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0198.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1161.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0169.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0637.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0722.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0280.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0054.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0340.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1071.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0665.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0015.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0636.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0376.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0741.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0771.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0062.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0564.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0040.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0366.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0715.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0046.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0851.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0822.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0256.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0789.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1108.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0546.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1022.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0386.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0764.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0202.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0296.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1099.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0328.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1004.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0702.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0933.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0410.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0162.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1017.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0778.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0485.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0224.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0037.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0297.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1153.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0051.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0495.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0756.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0885.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0604.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0968.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1032.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0667.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0813.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1002.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0466.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1160.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0642.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0960.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0598.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0926.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0183.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0795.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0972.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1047.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0302.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0488.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0660.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0504.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0336.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0361.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1147.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0321.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0309.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0695.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0371.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0292.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0188.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0043.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1134.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0470.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0233.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0624.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0583.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0265.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0585.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0629.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0541.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0481.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0701.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0927.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0661.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0228.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0952.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0343.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0835.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0850.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0572.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0153.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0377.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0523.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0710.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0666.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0420.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0458.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0006.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0740.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1026.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0563.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0857.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0214.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0844.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0354.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0456.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0699.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0489.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0890.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0476.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0787.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0860.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0626.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0584.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0001.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1077.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0691.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0382.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0283.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0081.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0240.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0418.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0412.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1128.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1009.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0755.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0735.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0704.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0156.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0200.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0350.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0182.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0904.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0304.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0333.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0595.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0326.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0252.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0427.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0902.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0154.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0930.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0593.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0002.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0801.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0950.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0423.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0368.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0024.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0803.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0935.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1075.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0347.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0014.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0743.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0149.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0997.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0094.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0828.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0190.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0282.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0647.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0222.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0887.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0692.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0032.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0796.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0271.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0900.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0307.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0146.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0440.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0396.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0444.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0045.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0511.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1123.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1079.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0963.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1027.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0428.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0540.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0176.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0227.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0434.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0516.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0815.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0498.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0931.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0605.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0745.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0853.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0707.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0381.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1110.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0320.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0909.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0946.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0323.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0317.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0854.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1121.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0829.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0087.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0119.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0689.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0411.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1038.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0367.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0013.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0142.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0746.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0568.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0254.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0102.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0225.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0010.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0408.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0429.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0291.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0948.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0449.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0414.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0273.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0955.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0542.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0088.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1080.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0687.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1074.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0830.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0877.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0370.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0463.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1118.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0944.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0486.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0157.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0623.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0793.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0995.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0218.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0238.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0269.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0036.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0627.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0632.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0084.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0083.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0655.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0179.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1072.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0469.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0967.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0602.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0949.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0688.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1015.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0648.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0226.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1165.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1112.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0091.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0849.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0502.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0788.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0993.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0603.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0518.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0203.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1143.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0966.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1057.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0749.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0290.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0066.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0628.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1012.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0351.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1066.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0592.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0268.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0589.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0985.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0133.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1061.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0131.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0478.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1166.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0827.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1114.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0030.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0645.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0250.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0729.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0490.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0276.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0391.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0468.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0472.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0571.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1005.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0491.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0503.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0207.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0975.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0792.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1164.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0403.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0751.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0312.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0895.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0607.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0784.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0543.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0095.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0685.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1135.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0674.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0867.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0057.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0450.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0345.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0819.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0551.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0831.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1141.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0744.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0606.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0274.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0106.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0124.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0305.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0039.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0388.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0341.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0962.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0768.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1078.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0172.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1058.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0194.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0286.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1086.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1033.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0989.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0159.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0260.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1054.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0435.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0723.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1144.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0448.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0181.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0327.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0004.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0042.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0724.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1059.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1020.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0730.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0734.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1152.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0917.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0750.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0774.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1096.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1151.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0244.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0251.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0212.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0619.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1113.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0728.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0362.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0387.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0727.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0455.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0065.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1041.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0337.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1001.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0910.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0196.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0457.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0126.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0230.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0158.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0346.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0334.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0011.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1130.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0925.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0526.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0231.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0438.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1116.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0206.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0961.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0239.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0270.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0038.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0279.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0675.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0318.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0617.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0349.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0356.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0369.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0422.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0499.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0825.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0634.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0700.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0517.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0919.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0672.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0530.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0389.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0663.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0858.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1021.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0905.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0711.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0817.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0964.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0561.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0550.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0798.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1011.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0753.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0865.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0976.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0484.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0545.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0683.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0110.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0289.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0570.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0034.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0022.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0441.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0400.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0791.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0808.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0616.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0942.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0299.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0958.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0640.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0682.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1039.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0612.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0713.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0086.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1082.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0509.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0758.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0696.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0253.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1076.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0596.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0781.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0761.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0884.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0012.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1037.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0673.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0630.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0234.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0586.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0288.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0757.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0127.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1100.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0059.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0103.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0184.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0886.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0856.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0515.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0805.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0348.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0078.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1119.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0522.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0653.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0763.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1148.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0834.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1029.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1046.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0259.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1111.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0679.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0147.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0797.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0405.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0210.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0017.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0453.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0262.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0759.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0671.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0780.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1145.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0355.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0633.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0313.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0773.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0533.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1019.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0731.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0839.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0398.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0807.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0104.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0128.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1150.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0714.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0027.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0870.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0553.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0018.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0738.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0649.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0690.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0953.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0314.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0538.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0742.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0837.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0565.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0285.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0138.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0020.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0421.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0814.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0249.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1088.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0737.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0221.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0514.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0342.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0033.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0862.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0473.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0315.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0641.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0609.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1092.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1127.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1042.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0482.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1087.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0397.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0358.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0135.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0847.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0694.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0875.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0442.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0703.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0941.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0868.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0562.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0644.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0579.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1030.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0322.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0171.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0959.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0079.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0559.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0838.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0991.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0063.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0876.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0144.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0554.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0413.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0923.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0122.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0492.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0035.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0204.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0721.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1105.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0494.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0316.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0060.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1084.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1018.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0287.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0401.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1063.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0855.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0582.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0956.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0965.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0804.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0373.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1031.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0298.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0357.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0922.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0639.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1158.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0646.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0824.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0264.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0869.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0846.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0123.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0600.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0007.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0987.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0676.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0903.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0301.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0658.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0246.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0874.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0889.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0785.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0733.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1136.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0241.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0651.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0248.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0353.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0464.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0151.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0513.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0028.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0166.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0439.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0055.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1139.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0915.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0446.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0109.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0243.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0861.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0537.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0544.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0005.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0404.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0267.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0232.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0765.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1097.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0901.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1085.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0096.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1117.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0823.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0992.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0451.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0999.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0155.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0986.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1067.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0684.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0680.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0716.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1007.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0098.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1140.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0826.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0191.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0657.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0019.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0929.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0938.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0777.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0840.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0217.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0021.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0512.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1095.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0426.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0841.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0152.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0897.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0053.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0089.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0085.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0443.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0130.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1103.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0117.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0775.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0460.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1008.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0177.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1083.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0263.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0338.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0134.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1006.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0896.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0816.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0167.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0650.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0216.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0101.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0090.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0215.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0008.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0531.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0610.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0383.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1060.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0549.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0852.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0536.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0459.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0720.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0794.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0643.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0698.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0811.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0848.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0508.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0520.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0385.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0594.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0201.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0016.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0311.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0480.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0883.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0859.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0821.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0936.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0099.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0709.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1162.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0372.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0402.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0125.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0994.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0049.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0888.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0064.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0295.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0378.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0748.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0308.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0465.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0447.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0199.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0521.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0510.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1068.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1133.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0424.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0747.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0618.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0471.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1138.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0073.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0160.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0996.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0129.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0186.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0998.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0770.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0026.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0143.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0940.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0245.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0220.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0878.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0659.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1051.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0310.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0732.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0779.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0430.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0330.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0300.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0114.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0332.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0501.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0082.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0477.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0654.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1065.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0339.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0928.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1098.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0717.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0921.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0278.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0906.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1081.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0833.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0255.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0739.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0974.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0211.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0069.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1120.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0810.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0115.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0399.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0112.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0192.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1093.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0979.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0009.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0335.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0863.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0806.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0705.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0555.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0445.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0782.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0140.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0193.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0581.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0161.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0866.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0148.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0344.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0907.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0898.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0566.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0843.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0669.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0136.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0359.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0620.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0392.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1053.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0908.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0003.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0809.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1104.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0924.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0324.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1101.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0097.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0569.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0379.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0557.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1034.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0497.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0071.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0394.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0864.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1132.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1064.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0145.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0132.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0625.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0107.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1055.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0973.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0165.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0670.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0656.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0257.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0175.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0984.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0871.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0219.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1159.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0195.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1014.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0802.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0988.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0525.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0783.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0137.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0170.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0799.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0842.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1154.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0681.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0415.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0462.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0943.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0556.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0425.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1045.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1003.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0272.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1052.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1016.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0452.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0505.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1025.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0483.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0574.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0111.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0070.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0363.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0360.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0845.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1137.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1102.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0461.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0932.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0437.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0496.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0894.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0891.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1122.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0325.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1155.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0635.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0185.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1107.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0407.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0500.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0575.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1089.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0436.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0776.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0532.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0613.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1129.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0258.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0881.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0971.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0914.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1091.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0236.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0726.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0528.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0058.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0818.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0873.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0205.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0329.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1013.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0068.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0417.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0303.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0769.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1149.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0762.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0951.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0506.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0076.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0113.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0587.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0686.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0044.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0978.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/tinanta.py:55: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0364.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1157.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0983.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0164.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0178.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0067.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0352.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0519.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0937.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0173.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0766.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0970.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0023.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0375.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0693.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0608.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0621.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1050.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1048.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0880.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0074.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0772.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0560.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0213.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0025.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0121.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1090.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0163.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0954.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1000.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0534.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1106.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0947.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0141.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0760.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0832.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1124.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0638.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0331.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0100.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0416.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0419.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1125.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0911.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0980.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0229.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0432.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0580.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0882.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0409.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0588.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1040.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0590.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0189.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1142.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0597.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1023.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0539.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0047.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0031.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0601.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0591.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0573.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1044.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0697.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0487.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0120.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0247.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0266.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0662.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0261.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0977.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0718.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0879.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0912.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0668.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1043.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0678.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1146.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1115.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1094.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0306.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0677.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0969.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0180.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1070.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1024.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0945.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1028.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0208.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0277.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0918.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0467.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0752.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1131.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0237.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0934.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0052.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0493.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0365.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0631.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0812.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0872.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0577.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0029.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0479.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0916.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1010.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0454.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0223.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0664.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0913.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0209.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0433.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1035.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0281.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1036.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0893.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0118.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0652.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0527.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0939.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0390.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0836.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0982.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0395.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0431.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0558.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0547.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0981.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0725.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0599.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0712.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0957.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0092.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0790.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0041.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0548.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0319.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0622.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0294.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0242.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0061.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0474.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0393.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0077.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0380.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0920.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0275.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0187.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0576.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0611.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0535.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0708.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0529.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0072.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0050.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0139.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0552.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0168.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1109.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1056.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0150.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0116.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0475.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0820.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0578.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0507.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1156.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0567.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0800.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0080.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0786.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0899.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0524.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0990.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0108.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0754.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1062.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0174.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0384.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1049.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0706.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0284.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1069.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0892.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0048.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0056.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0736.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0105.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0293.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0406.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1163.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0075.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0093.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0767.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0614.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1073.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0719.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0197.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0615.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1126.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0235.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0374.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0198.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1161.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0169.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0637.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0722.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0280.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0054.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0340.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1071.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0665.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0015.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0636.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0376.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0741.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0771.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0062.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0564.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0040.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0366.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0715.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0046.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0851.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0822.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0256.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0789.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1108.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0546.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1022.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0386.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0764.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0202.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0296.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1099.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0328.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1004.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0702.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0933.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0410.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0162.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1017.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0778.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0485.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0224.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0037.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0297.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1153.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0051.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0495.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0756.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0885.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0604.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0968.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1032.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0667.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0813.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1002.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0466.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1160.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0642.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0960.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0598.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0926.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0183.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0795.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0972.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1047.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0302.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0488.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0660.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0504.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0336.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0361.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1147.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0321.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0309.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0695.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0371.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0292.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0188.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0043.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1134.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0470.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0233.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0624.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0583.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0265.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0585.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0629.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0541.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0481.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0701.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0927.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0661.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0228.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0952.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0343.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0835.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0850.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0572.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0153.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0377.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0523.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0710.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0666.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0420.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0458.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0006.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0740.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1026.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0563.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0857.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0214.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0844.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0354.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0456.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0699.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0489.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0890.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0476.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0787.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0860.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0626.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0584.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0001.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1077.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0691.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0382.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0283.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0081.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0240.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0418.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0412.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1128.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1009.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0755.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0735.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0704.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0156.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0200.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0350.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0182.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0904.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0304.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0333.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0595.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0326.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0252.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0427.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0902.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0154.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0930.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0593.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0002.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0801.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0950.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0423.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0368.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0024.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0803.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0935.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1075.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0347.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0014.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0743.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0149.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0997.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0094.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0828.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0190.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0282.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0647.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0222.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0887.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0692.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0032.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0796.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0271.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0900.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0307.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0146.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0440.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0396.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0444.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0045.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0511.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1123.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1079.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0963.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1027.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0428.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0540.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0176.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0227.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0434.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0516.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0815.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0498.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0931.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0605.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0745.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0853.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0707.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0381.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1110.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0320.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0909.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0946.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0323.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0317.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0854.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1121.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0829.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0087.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0119.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0689.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0411.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1038.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0367.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0013.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0142.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0746.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0568.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0254.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0102.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0225.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0010.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0408.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0429.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0291.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0948.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0449.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0414.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0273.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0955.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0542.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0088.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1080.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0687.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1074.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0830.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0877.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0370.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0463.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1118.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0944.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0486.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0157.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0623.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0793.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0995.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0218.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0238.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0269.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0036.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0627.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0632.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0084.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0083.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0655.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0179.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1072.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0469.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0967.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0602.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0949.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0688.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1015.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0648.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0226.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1165.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1112.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0091.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0849.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0502.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0788.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0993.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0603.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0518.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0203.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1143.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0966.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1057.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0749.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0290.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0066.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0628.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1012.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0351.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1066.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0592.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0268.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0589.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0985.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0133.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1061.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0131.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0478.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1166.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0827.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1114.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0030.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0645.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0250.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0729.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0490.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0276.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0391.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0468.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0472.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0571.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1005.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0491.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0503.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0207.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0975.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0792.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1164.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0403.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0751.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0312.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0895.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0607.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0784.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0543.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0095.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0685.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1135.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0674.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0867.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0057.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0450.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0345.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0819.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0551.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0831.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1141.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0744.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0606.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0274.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0106.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0124.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0305.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0039.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0388.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0341.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0962.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0768.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1078.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0172.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1058.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0194.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0286.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1086.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1033.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0989.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0159.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0260.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1054.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0435.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0723.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1144.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0448.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0181.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0327.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0004.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0042.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0724.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1059.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1020.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0730.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0734.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1152.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0917.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0750.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0774.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1096.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1151.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0244.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0251.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0212.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0619.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1113.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0728.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0362.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0387.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0727.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0455.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0065.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1041.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0337.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1001.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0910.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0196.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0457.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0126.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0230.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0158.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0346.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0334.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0011.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1130.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0925.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0526.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0231.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0438.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1116.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0206.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0961.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0239.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0270.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0038.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0279.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0675.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0318.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0617.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0349.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0356.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0369.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0422.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0499.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0825.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0634.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0700.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0517.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0919.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0672.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0530.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0389.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0663.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0858.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1021.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0905.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0711.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0817.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0964.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0561.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0550.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0798.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1011.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0753.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0865.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0976.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0484.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0545.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0683.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0110.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0289.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0570.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0034.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0022.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0441.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0400.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0791.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0808.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0616.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0942.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0299.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0958.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0640.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0682.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1039.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0612.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0713.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0086.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1082.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0509.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0758.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0696.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0253.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1076.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0596.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0781.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0761.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0884.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0012.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1037.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0673.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0630.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0234.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0586.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0288.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0757.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0127.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1100.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0059.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0103.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0184.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0886.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0856.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0515.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0805.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0348.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0078.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1119.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0522.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0653.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0763.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1148.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0834.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1029.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1046.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0259.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1111.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0679.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0147.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0797.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0405.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0210.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0017.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0453.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0262.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0759.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0671.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0780.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1145.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0355.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0633.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0313.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0773.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0533.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1019.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0731.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0839.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0398.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0807.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0104.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0128.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1150.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0714.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0027.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0870.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0553.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0018.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0738.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0649.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0690.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0953.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0314.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0538.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0742.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0837.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0565.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0285.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0138.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0020.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0421.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0814.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0249.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1088.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0737.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0221.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0514.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0342.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0033.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0862.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0473.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0315.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0641.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0609.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1092.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1127.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1042.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0482.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1087.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0397.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0358.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0135.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0847.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0694.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0875.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0442.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0703.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0941.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0868.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0562.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0644.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0579.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1030.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0322.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0171.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0959.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0079.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0559.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0838.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0991.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0063.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0876.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0144.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0554.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0413.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0923.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0122.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0492.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0035.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0204.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0721.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1105.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0494.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0316.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0060.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1084.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1018.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0287.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0401.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1063.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0855.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0582.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0956.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0965.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0804.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0373.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1031.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0298.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0357.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0922.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0639.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1158.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0646.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0824.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0264.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0869.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0846.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0123.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0600.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0007.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0987.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0676.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0903.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0301.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0658.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0246.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0874.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0889.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0785.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0733.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1136.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0241.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0651.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0248.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0353.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0464.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0151.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0513.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0028.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0166.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0439.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0055.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1139.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0915.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0446.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0109.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0243.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0861.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0537.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0544.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0005.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0404.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0267.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0232.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0765.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1097.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0901.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1085.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0096.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1117.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0823.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0992.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0451.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0999.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0155.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0986.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1067.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0684.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0680.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0716.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1007.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0098.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1140.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0826.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0191.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0657.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0019.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0929.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0938.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0777.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0840.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0217.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0021.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0512.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1095.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0426.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0841.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0152.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0897.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0053.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0089.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0085.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0443.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0130.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1103.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0117.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0775.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0460.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1008.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0177.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1083.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0263.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0338.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0134.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1006.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0896.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0816.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0167.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0650.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0216.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0101.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0090.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0215.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0008.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0531.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0610.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0383.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1060.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0549.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0852.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0536.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0459.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0720.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0794.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0643.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0698.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0811.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0848.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0508.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0520.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0385.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0594.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0201.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0016.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0311.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0480.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0883.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0859.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0821.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0936.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0099.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0709.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1162.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0372.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0402.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0125.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0994.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0049.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0888.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0064.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0295.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0378.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0748.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0308.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0465.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0447.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0199.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0521.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0510.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1068.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1133.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0424.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0747.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0618.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0471.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1138.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0073.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0160.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0996.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0129.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0186.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0998.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0770.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0026.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0143.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0940.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0245.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0220.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0878.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0659.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1051.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0310.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0732.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0779.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0430.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0330.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0300.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0114.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0332.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0501.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0082.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0477.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0654.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1065.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0339.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0928.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1098.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0717.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0921.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0278.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0906.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1081.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0833.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0255.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0739.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0974.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0211.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0069.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1120.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0810.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0115.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0399.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0112.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0192.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1093.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0979.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0009.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0335.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0863.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0806.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0705.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0555.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0445.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0782.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0140.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0193.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0581.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0161.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0866.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0148.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0344.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0907.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0898.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0566.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0843.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0669.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0136.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0359.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0620.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0392.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1053.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0908.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0003.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0809.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1104.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0924.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0324.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1101.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0097.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0569.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0379.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0557.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1034.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0497.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0071.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0394.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0864.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1132.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1064.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0145.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0132.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0625.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0107.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1055.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0973.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0165.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0670.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0656.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0257.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0175.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0984.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0871.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0219.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1159.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0195.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1014.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0802.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0988.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0525.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0783.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0137.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0170.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0799.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0842.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1154.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0681.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0415.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0462.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0943.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0556.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0425.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1045.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1003.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0272.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1052.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1016.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0452.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0505.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1025.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0483.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0574.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0111.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0070.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0363.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0360.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0845.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1137.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1102.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0461.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0932.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0437.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0496.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0894.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0891.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1122.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0325.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1155.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0635.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0185.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1107.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0407.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0500.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0575.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1089.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0436.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0776.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0532.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0613.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1129.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0258.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0881.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0971.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0914.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1091.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0236.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0726.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0528.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0058.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0818.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0873.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0205.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0329.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1013.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0068.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0417.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0303.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0769.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1149.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0762.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0951.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0506.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0076.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0113.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0587.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0686.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0044.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0978.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/pypanini/krdanta.py:45: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0364.json' mode='r' encoding='utf-8'>
  d = json.load(open(jf, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
ok
test_01_0002_eD (tests.test_dhatu.TestDhatuGenerative.test_01_0002_eD) ... /home/edhiraj/Documents/projs/pypanini/tests/test_dhatu.py:122: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0002.json' mode='r' encoding='utf-8'>
  d = json.load(open(json_path, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/tests/test_dhatu.py:140: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0002.json' mode='r' encoding='utf-8'>
  data = json.load(open(json_path, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
ok
test_01_0003_sparD (tests.test_dhatu.TestDhatuGenerative.test_01_0003_sparD) ... /home/edhiraj/Documents/projs/pypanini/tests/test_dhatu.py:122: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0003.json' mode='r' encoding='utf-8'>
  d = json.load(open(json_path, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
/home/edhiraj/Documents/projs/pypanini/tests/test_dhatu.py:140: ResourceWarning: unclosed file <_io.TextIOWrapper name='/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0003.json' mode='r' encoding='utf-8'>
  data = json.load(open(json_path, encoding="utf-8"))
ResourceWarning: Enable tracemalloc to get the object allocation traceback
ok
test_cli (tests.test_dhatu.TestDhatuGenerative.test_cli) ... ok

----------------------------------------------------------------------
Ran 4 tests in 17.309s

OK

```

## Per-dhatu (tests/test_dhatu.py)

### 01.0001
```
===========================================================================
VALIDATION  /home/edhiraj/Documents/projs/skt-morph-data/data/01/01.0001.json  |  dhatu=BU (BU sattAyAm)
===========================================================================
✓ tokens: 82577  engine: generative (no hardcoded dict)

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
✓ tokens: 1436  engine: generative (no hardcoded dict)

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
✓ tokens: 3754  engine: generative (no hardcoded dict)

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
✓ tokens: 1915  engine: generative (no hardcoded dict)

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
✓ tokens: 26470  engine: generative (no hardcoded dict)

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
✓ tokens: 1911  engine: generative (no hardcoded dict)

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
✓ tokens: 4415  engine: generative (no hardcoded dict)

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
