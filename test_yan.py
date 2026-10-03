from pypanini import TinantaDerivationEngine
te = TinantaDerivationEngine()
te._get_meta = lambda d, i: {'clean': 'ji', 'pada': 'Atmanepadi', 'padam': 'parasmEpadI', 'sew': False, 'sew_raw': 'aniw', 'gana': 'BvAdiH', 'is_idit': False, 'op': 'ji', 'is_mit': False, 'antara': ''}
# Need to capture _yan_stem
print(te.derive('ji', sanadi='yananta', _force_pada='Atmanepadi', dhatu_id='01.1096'))
