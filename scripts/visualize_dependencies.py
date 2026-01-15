"""
Create visual dependency graph of subpackages.

Requires: graphviz (install: pip install graphviz)
"""

import os
import re
from collections import defaultdict
from pathlib import Path


def analyze_dependencies(root_dir):
    """Same as analyze_dependencies.py but returns data."""
    # Delegate to the existing `analyze_dependencies.py` script implementation
    # which exposes `analyze_subpackage_dependencies(root_dir)` returning
    # (dependencies, subpackages).
    import importlib

    # Try importing the module as a top-level module (when running from
    # the `scripts/` directory) or as `scripts.analyze_dependencies`.
    mod = None
    try:
        mod = importlib.import_module("analyze_dependencies")
    except Exception:
        try:
            mod = importlib.import_module("scripts.analyze_dependencies")
        except Exception as e:
            raise RuntimeError(
                "Could not import analyze_dependencies module from scripts/"
            ) from e

    return mod.analyze_subpackage_dependencies(root_dir)


def create_dependency_graph(dependencies, subpackages, output_file="dependencies.dot"):
    """Create Graphviz DOT file for dependency visualization."""

    with open(output_file, "w") as f:
        f.write("digraph techminer2_dependencies {\n")
        f.write("    rankdir=LR;\n")
        f.write("    node [shape=box, style=rounded];\n")
        f.write("\n")

        # Color nodes by dependency count
        for pkg in subpackages:
            dep_count = len(dependencies.get(pkg, set()))

            if dep_count == 0:
                color = "lightgreen"  # Independent
            elif dep_count <= 2:
                color = "lightyellow"  # Few dependencies
            else:
                color = "lightcoral"  # Many dependencies

            f.write(f'    "{pkg}" [fillcolor="{color}", style="filled"];\n')

        f.write("\n")

        # Add edges
        for pkg, deps in dependencies.items():
            for dep in deps:
                f.write(f'    "{pkg}" -> "{dep}";\n')

        f.write("}\n")

    print(f"Dependency graph saved to: {output_file}")
    print(f"Generate image with: dot -Tpng {output_file} -o dependencies.png")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python visualize_dependencies.py /path/to/techminer2/repo")
        sys.exit(1)

    root_dir = sys.argv[1]
    dependencies, subpackages = analyze_dependencies(root_dir)
    create_dependency_graph(dependencies, subpackages)
