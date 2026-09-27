import sys
from pypanini.tinanta import TinantaDerivationEngine
TE = TinantaDerivationEngine()
c = TE.derive('cakz', 'lw', 'madhyama', 'eka', 'kartari', None, '02.0007')
print(c)
