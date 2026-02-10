from importlib.resources import files

from techminer2.refine.thesaurus_old._internals.load_reversed_thesaurus_as_mapping import (
    internal__load_reversed_thesaurus_as_mapping,
)


def internal__load_cleanup_thesaurus_as_mapping() -> dict[str, str]:
    """Load all cleanup thesaurus files and merge into single mapping."""
    cleanup_dir = files("techminer2.package_data.thesaurus.cleanup")
    txt_files = [str(f) for f in cleanup_dir.iterdir() if f.name.endswith(".txt")]
    mapping: dict[str, str] = {}
    for file_path in txt_files:
        mapping.update(internal__load_reversed_thesaurus_as_mapping(file_path))
    return mapping
