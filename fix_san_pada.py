import re
with open('pypanini/tinanta.py', 'r') as f:
    content = f.read()

old_block = """                    base_no_a = base_fut[:-1] if base_fut.endswith("a") else base_fut
                    atman_form = self._conjugate_at_stem_atmane(base_no_a, "lw" if lakara=="lfw" else "laN", purusha, vacana)
                    paras_form = self._conjugate_at_stem_parasmai(base_no_a, "lw" if lakara=="lfw" else "laN", purusha, vacana)
                    direct = [fut + "te", fut + "ti"]
                    cands_all += atman_form + paras_form + direct"""

injection = """                    base_no_a = base_fut[:-1] if base_fut.endswith("a") else base_fut
                    if pada in ("Atmanepadi", "ubhayapadi"):
                        cands_all += self._conjugate_at_stem_atmane(base_no_a, "lw" if lakara=="lfw" else "laN", purusha, vacana)
                    if pada in ("parasmEpadi", "ubhayapadi"):
                        cands_all += self._conjugate_at_stem_parasmai(base_no_a, "lw" if lakara=="lfw" else "laN", purusha, vacana)
                    # direct = [fut + "te", fut + "ti"]  # removed blind direct addition"""

if old_block in content:
    content = content.replace(old_block, injection)
    with open('pypanini/tinanta.py', 'w') as f:
        f.write(content)
    print("Patched lfw/lfN successfully")
else:
    print("Could not find block lfw")
