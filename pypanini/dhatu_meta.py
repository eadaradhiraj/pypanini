"""
pypanini.dhatu_meta
~~~~~~~~~~~~~~~~~~~
Single shared scan of skt-morph-data JSON metadata.

Both derivation engines need the same per-file fields (info table + id) to
build their dhatu caches; scanning the ~2,300 JSON files twice cost ~10s per
fresh process. This module parses each file ONCE (per-gana sorted, 01 last so
validated BvAdi entries win clean/op collisions, exactly like the engines did)
and hands the pre-parsed rows to both engines, whose entry-building logic is
unchanged and verbatim.

Pure read-only cross-check data (never used for generation itself).
"""
from __future__ import annotations

import glob
import json
from pathlib import Path

# (json path, info table, id) in scan order; None until first scan.
_SCAN: list | None = None


def scan_dhatu_jsons() -> list:
    """Return [(jf, info, id_val)] rows, scanning files at most once."""
    global _SCAN
    if _SCAN is not None:
        return _SCAN
    rows: list = []
    try:
        _bases = [Path("skt-morph-data") / _g
                  for _g in ("02", "03", "04", "05", "06", "07", "08", "09", "10", "01")]
        _jfs = [jf for _b in _bases if _b.exists()
                for jf in sorted(glob.glob(str(_b / "*.json")))]
        for jf in _jfs:
            try:
                with open(jf, encoding="utf-8") as _fh:
                    _d = json.load(_fh)
                _info = {x["name"]: x["value"] for x in _d.get("info", [])}
                if not _info.get("OpadeSikasvarUpam", ""):
                    continue
                rows.append((jf, _info, _d.get("id", "") or Path(jf).stem))
            except Exception:
                continue
    except Exception:
        pass
    _SCAN = rows
    return _SCAN
