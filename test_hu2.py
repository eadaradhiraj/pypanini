import json
from pypanini import KrdantaEngine
ke = KrdantaEngine()

# derive krdantas for hu with pra
res = ke.derive_all_krdantas("hu", sanadi="nijanta", upasarga="pra", dhatu_id="03.0001")
print("Engine generated nijanta:")
for k, v in res.items():
    if isinstance(v, dict):
        print(f"  {k}: {v.get('avyaya', v)}")
    else:
        print(f"  {k}: {v}")

