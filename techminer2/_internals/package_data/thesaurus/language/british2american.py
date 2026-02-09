from pathlib import Path
from typing import Dict

__all__ = ["BRITISH_TO_AMERICAN"]

TXT_NAME = "british2american.the.txt"


def _load_mapping() -> Dict[str, str]:
    p = Path(__file__).parent / TXT_NAME
    mapping: Dict[str, str] = {}
    if not p.exists():
        return mapping

    with p.open(encoding="utf-8") as fh:
        lines = [ln.rstrip("\n") for ln in fh]

    i = 0
    n = len(lines)
    while i < n:
        # skip empty lines
        if not lines[i].strip():
            i += 1
            continue
        key = lines[i].strip()
        i += 1
        # find next non-empty line for value
        while i < n and not lines[i].strip():
            i += 1
        if i < n:
            value = lines[i].strip()
            i += 1
        else:
            value = ""
        if key:
            mapping[key] = value
    return mapping


BRITISH_TO_AMERICAN: Dict[str, str] = _load_mapping()
