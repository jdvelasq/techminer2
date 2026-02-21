"""Remove lines starting with '# pylint:' across .py files.

Run: python3 scripts/remove_pylint_lines.py
"""

import os
import re

ROOT = os.path.dirname(os.path.dirname(__file__))
EXCLUDE_DIRS = {".venv", "venv", "__pycache__", ".git"}

pattern = re.compile(r"(?m)^[ \t]*#\s*pylint:.*(?:\r?\n)?")
modified = []
for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]
    for fname in filenames:
        if not fname.endswith(".py"):
            continue
        fpath = os.path.join(dirpath, fname)
        try:
            with open(fpath, "r", encoding="utf8") as fh:
                content = fh.read()
        except Exception:
            continue
        new_content = pattern.sub("", content)
        if new_content != content:
            try:
                with open(fpath, "w", encoding="utf8") as fh:
                    fh.write(new_content)
                modified.append(fpath)
            except Exception:
                pass

print(f"Processed .py files under: {ROOT}")
print(f"Modified files: {len(modified)}")
for p in modified:
    print(p)
