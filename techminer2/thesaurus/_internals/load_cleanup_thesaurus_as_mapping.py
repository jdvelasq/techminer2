"""Default cleanup thesaurus."""

import glob

import pkg_resources  # type: ignore

from .load_reversed_thesaurus_as_mapping import (
    internal__load_reversed_thesaurus_as_mapping,
)


def internal__load_cleanup_thesaurus_as_mapping():
    file_paths = pkg_resources.resource_filename(
        "techminer2", "package_data/thesaurus/cleanup/*.txt"
    )
    file_paths = glob.glob(file_paths)
    mapping = {}
    for file_path in file_paths:
        mapping.update(internal__load_reversed_thesaurus_as_mapping(file_path))
    return mapping
