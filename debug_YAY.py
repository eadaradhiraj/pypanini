import sys
from unittest.mock import patch
from pypanini import TinantaDerivationEngine

te = TinantaDerivationEngine()
old_get_meta = te._get_meta
def new_get_meta(dhatu, dhatu_id):
    print("GET META", dhatu, dhatu_id)
    return old_get_meta(dhatu, dhatu_id)
te._get_meta = new_get_meta
print(te.derive("ji", lakara="lw", purusha="prathama", vacana="eka", prayoga="kartari", sanadi="yananta", _force_pada="parasmEpadi", dhatu_id="01.1096"))
