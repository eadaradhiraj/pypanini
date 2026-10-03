import json
from pypanini import TinantaDerivationEngine
te = TinantaDerivationEngine()

# derive kartari for vi+ji
res, _ = te.derive("ji", lakara="lw", purusha="prathama", vacana="eka", prayoga="kartari", upasarga="vi", dhatu_id="01.1096")
print("Engine generated vi+ji (kartari):", res)

with open("skt-morph-data/01/01.1096.json", "r") as f:
    data = json.load(f)
    print("Expected vi+ji in JSON:", data["upasarga_forms"]["vi"]["conjugations"]["ting"]["kartari"]["lw"]["prathama"]["eka"])
