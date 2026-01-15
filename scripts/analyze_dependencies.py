"""
Analyze import dependencies between subpackages.

Shows which subpackages import from which other subpackages.
"""

import os
import re
from collections import defaultdict
from pathlib import Path


def get_subpackages(root_dir):
    """Get all subpackages in techminer2."""
    subpackages = []
    root_path = Path(root_dir) / "techminer2"

    for item in root_path.iterdir():
        if item.is_dir() and (item / "__init__.py").exists():
            subpackages.append(item.name)

    return sorted(subpackages)


def analyze_imports_in_file(file_path, root_dir):
    """Extract imports from a Python file."""
    imports = []

    # compile line-level patterns (capture top-level subpackage name)
    pattern_from = re.compile(r"from\s+techminer2\.([A-Za-z0-9_]+)")
    pattern_import = re.compile(r"import\s+techminer2\.([A-Za-z0-9_]+)")

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                # ignore doctest lines that start with '>>>' (possibly preceded by whitespace)
                if line.lstrip().startswith(">>>"):
                    continue

                m1 = pattern_from.search(line)
                if m1:
                    imports.append(m1.group(1))

                m2 = pattern_import.search(line)
                if m2:
                    imports.append(m2.group(1))

                # detect bare imports like 'import subpackage'
                m3 = re.match(r"^\s*import\s+([A-Za-z0-9_]+)", line)
                if m3:
                    name = m3.group(1)
                    if name != "techminer2":
                        imports.append(name)

                # detect relative imports that may reference other top-level subpackages
                # e.g. 'from ..otherpkg import ...' -> capture 'otherpkg'
                m4 = re.search(r"from\s+\.{2,}([A-Za-z0-9_]+)", line)
                if m4:
                    imports.append(m4.group(1))
    except Exception:
        pass

    return imports


def analyze_subpackage_dependencies(root_dir):
    """Analyze dependencies between subpackages."""
    subpackages = get_subpackages(root_dir)

    # Map: subpackage -> set of subpackages it imports from
    dependencies = defaultdict(set)

    root_path = Path(root_dir) / "techminer2"

    for subpackage in subpackages:
        subpackage_path = root_path / subpackage

        # Find all Python files in this subpackage
        for py_file in subpackage_path.rglob("*.py"):
            imports = analyze_imports_in_file(py_file, root_dir)

            for imported in imports:
                if imported in subpackages and imported != subpackage:
                    dependencies[subpackage].add(imported)

    return dependencies, subpackages


def print_dependency_report(dependencies, subpackages):
    """Print dependency analysis report."""
    print("=" * 80)
    print("SUBPACKAGE DEPENDENCY ANALYSIS")
    print("=" * 80)
    print()

    # Count dependencies
    total_deps = sum(len(deps) for deps in dependencies.values())
    independent = [pkg for pkg in subpackages if len(dependencies.get(pkg, set())) == 0]

    print(f"Total subpackages: {len(subpackages)}")
    print(f"Independent subpackages: {len(independent)}")
    print(f"Total cross-dependencies: {total_deps}")
    print()

    # Show independent subpackages
    if independent:
        print("INDEPENDENT SUBPACKAGES (✅ Good!):")
        for pkg in sorted(independent):
            print(f"  ✅ {pkg}")
        print()

    # Show dependencies
    print("SUBPACKAGE DEPENDENCIES:")
    print()

    for subpackage in sorted(subpackages):
        deps = dependencies.get(subpackage, set())

        if deps:
            print(f"📦 {subpackage} depends on:")
            for dep in sorted(deps):
                print(f"    └─> {dep}")
            print()

    # Dependency matrix
    print("=" * 80)
    print("DEPENDENCY MATRIX")
    print("=" * 80)
    print()
    print("Legend: ✅ = Independent, ⚠️ = Has dependencies")
    print()

    for subpackage in sorted(subpackages):
        deps = dependencies.get(subpackage, set())
        status = "✅" if len(deps) == 0 else f"⚠️ ({len(deps)} deps)"
        print(f"{status:15} {subpackage}")


def find_circular_dependencies(dependencies):
    """Find circular dependencies between subpackages.

    This version will report file-level import locations for each circular
    pair if `locations` mapping is provided.
    """
    print()
    print("=" * 80)
    print("CIRCULAR DEPENDENCY CHECK")
    print("=" * 80)
    print()

    circular = []

    for pkg_a, deps_a in dependencies.items():
        for pkg_b in deps_a:
            if pkg_a in dependencies.get(pkg_b, set()):
                # normalize ordering so each pair appears once (A,B) with A < B
                if (pkg_b, pkg_a) not in circular:
                    circular.append((pkg_a, pkg_b))

    if circular:
        print("⚠️ CIRCULAR DEPENDENCIES FOUND:")
        for pkg_a, pkg_b in circular:
            print(f"    {pkg_a} ↔ {pkg_b}")
            # print file-level locations if available in kwargs
            # locations is expected to be passed via closure or externally
            # (we'll attempt to read a global if set)
            locs = globals().get("_IMPORT_LOCATIONS")
            if locs:
                a_to_b = locs.get(pkg_a, {}).get(pkg_b, [])
                b_to_a = locs.get(pkg_b, {}).get(pkg_a, [])

                if a_to_b:
                    print(f"      Files in {pkg_a} importing {pkg_b}:")
                    for fp, ln, line in a_to_b:
                        print(f"        {fp}:{ln}: {line}")
                if b_to_a:
                    print(f"      Files in {pkg_b} importing {pkg_a}:")
                    for fp, ln, line in b_to_a:
                        print(f"        {fp}:{ln}: {line}")
                print()
    else:
        print("✅ No circular dependencies found!")


def build_import_locations(root_dir, subpackages):
    """Build a mapping of import locations between subpackages.

    Returns a dict: locations[pkg_from][pkg_to] = list of (file_path, lineno, line)
    """
    root_path = Path(root_dir) / "techminer2"
    locations = {pkg: defaultdict(list) for pkg in subpackages}

    # Patterns to match imports; capture the top-level subpackage name
    pattern_from = re.compile(r"from\s+techminer2\.([A-Za-z0-9_]+)")
    pattern_import = re.compile(r"import\s+techminer2\.([A-Za-z0-9_]+)")
    pattern_rel = re.compile(r"from\s+\.{2,}([A-Za-z0-9_]+)")
    pattern_bare = re.compile(r"^\s*import\s+([A-Za-z0-9_]+)")

    for pkg in subpackages:
        pkg_path = root_path / pkg
        if not pkg_path.exists():
            continue
        for py_file in pkg_path.rglob("*.py"):
            try:
                with open(py_file, "r", encoding="utf-8") as fh:
                    for i, line in enumerate(fh, 1):
                        # skip doctest lines
                        if line.lstrip().startswith(">>>"):
                            continue

                        # relative imports that climb up to another package
                        m_rel = pattern_rel.search(line)
                        if m_rel:
                            imported = m_rel.group(1)
                            if imported in subpackages and imported != pkg:
                                locations[pkg][imported].append(
                                    (
                                        os.path.relpath(str(py_file), root_dir),
                                        i,
                                        line.strip(),
                                    )
                                )

                        m1 = pattern_from.search(line)
                        if m1:
                            imported = m1.group(1)
                            if imported in subpackages and imported != pkg:
                                locations[pkg][imported].append(
                                    (
                                        os.path.relpath(str(py_file), root_dir),
                                        i,
                                        line.strip(),
                                    )
                                )
                        m2 = pattern_import.search(line)
                        if m2:
                            imported = m2.group(1)
                            if imported in subpackages and imported != pkg:
                                locations[pkg][imported].append(
                                    (
                                        os.path.relpath(str(py_file), root_dir),
                                        i,
                                        line.strip(),
                                    )
                                )

                        # bare imports like 'import subpackage'
                        m_bare = pattern_bare.search(line)
                        if m_bare:
                            imported = m_bare.group(1)
                            if imported in subpackages and imported != pkg:
                                locations[pkg][imported].append(
                                    (
                                        os.path.relpath(str(py_file), root_dir),
                                        i,
                                        line.strip(),
                                    )
                                )
            except Exception:
                # ignore unreadable files
                pass

    return locations


def main():
    import sys

    if len(sys.argv) < 2:
        print("Usage: python analyze_dependencies.py /path/to/techminer2/repo")
        sys.exit(1)

    root_dir = sys.argv[1]

    if not os.path.exists(os.path.join(root_dir, "techminer2")):
        print(f"Error: {root_dir} does not contain techminer2 package")
        sys.exit(1)

    dependencies, subpackages = analyze_subpackage_dependencies(root_dir)

    # Build file-level import locations to help pinpoint cycles
    locations = build_import_locations(root_dir, subpackages)
    # expose to find_circular_dependencies via a well-known global
    globals()["_IMPORT_LOCATIONS"] = locations

    print_dependency_report(dependencies, subpackages)
    find_circular_dependencies(dependencies)

    print()
    print("=" * 80)
    print("RECOMMENDATIONS")
    print("=" * 80)
    print()

    dependent_count = len([pkg for pkg in subpackages if dependencies.get(pkg)])

    if dependent_count == 0:
        print("✅ All subpackages are independent - excellent architecture!")
    else:
        print(f"⚠️ {dependent_count} subpackages have dependencies")
        print()
        print("To improve independence:")
        print("  1. Review each dependency (is it necessary?)")
        print("  2. Move shared code to _internals/")
        print("  3. Consider duplicating small utilities")
        print("  4. Use dependency injection for services")


if __name__ == "__main__":
    main()
