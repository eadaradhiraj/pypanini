from pypanini.krdanta import KrdantaEngine
KE = KrdantaEngine()

# Monkey patch _get_meta to force aniT
orig_meta = KE._get_meta
def fake_meta(dhatu, dhatu_id):
    if dhatu == "cakz":
        return {'clean': 'cakz', 'pada': 'Atmanepadi', 'sew_raw': 'aniw', 'sew': False}
    return orig_meta(dhatu, dhatu_id)
KE._get_meta = fake_meta

for p in ['tavya', 'tumun', 'tfc', 'kta', 'ktvA']:
    print(p, KE.derive_krdanta('cakz', p, sanadi=None, dhatu_id='fake'))
