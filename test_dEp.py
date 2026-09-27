from pypanini.krdanta import KrdantaEngine
KE = KrdantaEngine()
for s in [None, 'sannanta', 'nijanta', 'yananta', 'yanluganta']:
    print(s, KE.derive_krdanta('dE', 'kta', s, 'saM', '01.1073'))
