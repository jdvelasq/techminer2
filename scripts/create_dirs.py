#!/usr/bin/env python3
"""
Create a sequence of directories under a parent path.

Change the globals below to adjust the parent directory or folder names.
"""
import sys
from pathlib import Path

# Global variables (edit these as needed)
# Default parent directory (change this value as you like)
PARENT_DIR = Path("parent-dir")
# Sequence of folder names to create under the parent
FOLDERS = [
    "auth",
    "auth_first",
    "authkw",
    "concept",
    "ctry",
    "ctry_first",
    "idxkw",
    "kw",
    "org",
    "org_first",
    "src",
]


def create_directories(parent: Path, folders):
    parent = Path(parent)
    parent.mkdir(parents=True, exist_ok=True)
    created = []
    for name in folders:
        p = parent / name
        p.mkdir(parents=True, exist_ok=True)
        created.append(p)
    return created


def main(argv=None):
    argv = argv or sys.argv[1:]
    parent = PARENT_DIR
    if argv:
        parent = Path(argv[0])
    created = create_directories(parent, FOLDERS)
    for p in created:
        print(f"Created: {p.resolve()}")


if __name__ == "__main__":
    main()
