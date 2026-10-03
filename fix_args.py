with open("pypanini/tinanta.py", "r") as f:
    content = f.read()

# We need to remove `upasarga` from its current position and put it after `json_path`
import re

old_sig = """        prayoga: str = "kartari",
        upasarga: Optional[str] = None,
        sanadi: Optional[str] = None,
        dhatu_id: Optional[str] = None,
        json_path: Optional[str] = None,"""

new_sig = """        prayoga: str = "kartari",
        sanadi: Optional[str] = None,
        dhatu_id: Optional[str] = None,
        json_path: Optional[str] = None,
        upasarga: Optional[str] = None,"""

content = content.replace(old_sig, new_sig)

# also fix the wrapper call
old_call = "cands, log = self._derive_inner(dhatu, lakara, purusha, vacana, prayoga, upasarga, sanadi, dhatu_id, json_path, _force_pada, _cakz_bypass, _sad_c10_recurse)"
new_call = "cands, log = self._derive_inner(dhatu, lakara, purusha, vacana, prayoga, sanadi, dhatu_id, json_path, upasarga, _force_pada, _cakz_bypass, _sad_c10_recurse)"
content = content.replace(old_call, new_call)

# also fix the derive_all signature and call
old_sig_all = """        prayoga: str = "kartari",
        upasarga: Optional[str] = None,
        sanadi: Optional[str] = None,"""

new_sig_all = """        prayoga: str = "kartari",
        sanadi: Optional[str] = None,
        upasarga: Optional[str] = None,"""

content = content.replace(old_sig_all, new_sig_all)

old_call_all = "forms, _ = self.derive(dhatu, lakara, p, v, prayoga, upasarga, sanadi)"
new_call_all = "forms, _ = self.derive(dhatu, lakara, p, v, prayoga, sanadi, upasarga=upasarga)"
content = content.replace(old_call_all, new_call_all)

with open("pypanini/tinanta.py", "w") as f:
    f.write(content)
print("Fixed args")
