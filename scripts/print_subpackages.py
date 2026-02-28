#!/usr/bin/env python3
"""Create a file with the directory-only structure of a package.

By default it prefers a `techminer` directory, falls back to `techminer2`.
It excludes any directory named `_helpers` or `_internals`.
"""
import argparse
import os


def gather_dirs(root, excluded=None):
    if excluded is None:
        excluded = {"_helpers", "_internals"}

    root = os.path.normpath(root)
    out = []
    out.append(root + "/")

    for dirpath, dirs, files in os.walk(root, topdown=True):
        # prune excluded directories so walk doesn't descend into them
        dirs[:] = [d for d in dirs if d not in excluded]
        rel = os.path.relpath(dirpath, root)
        if rel == ".":
            continue
        path = os.path.join(root, rel).replace("\\", "/") + "/"
        out.append(path)

    out = sorted(out)
    return out


def build_tree_lines(paths, root):
    # paths: list of full paths ending with '/'
    root = root.rstrip("/\\") + "/"
    tree = {}

    def insert(parts):
        node = tree
        for p in parts:
            node = node.setdefault(p, {})

    for p in paths:
        if p == root:
            continue
        rel = p[len(root) :].strip("/")
        if not rel:
            continue
        parts = rel.split("/")
        insert(parts)

    lines = [root]

    def render(node, prefix=""):
        keys = sorted(node.keys())
        for i, k in enumerate(keys):
            last = i == (len(keys) - 1)
            connector = "└── " if last else "├── "
            lines.append(prefix + connector + k + "/")
            if node[k]:
                extension = "    " if last else "│   "
                render(node[k], prefix + extension)

    render(tree, "")
    return lines


def main():
    p = argparse.ArgumentParser(description="List package directories to a file")
    p.add_argument(
        "--root",
        "-r",
        help="Root package directory (default: detect techminer/ or techminer2/)",
    )
    p.add_argument(
        "--output", "-o", default="subpackages_structure.txt", help="Output file"
    )
    p.add_argument(
        "--style",
        "-s",
        choices=("flat", "tree"),
        default="flat",
        help="Output style: flat or tree",
    )
    args = p.parse_args()

    root = args.root
    if not root:
        if os.path.isdir("techminer"):
            root = "techminer"
        elif os.path.isdir("techminer2"):
            root = "techminer2"
        else:
            print("No 'techminer' or 'techminer2' directory found. Provide --root.")
            return 2

    if not os.path.isdir(root):
        print(f"Root path does not exist: {root}")
        return 3

    lines = gather_dirs(root)

    if args.style == "tree":
        lines = build_tree_lines(lines, root)

    with open(args.output, "w", encoding="utf-8") as fh:
        for line in lines:
            fh.write(line + "\n")

    print(f"Wrote {len(lines)} directories to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
