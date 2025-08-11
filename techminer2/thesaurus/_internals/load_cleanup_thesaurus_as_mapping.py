"""Default cleanup thesaurus."""
import glob
from importlib.resources import files

from techminer2.thesaurus._internals.load_reversed_thesaurus_as_mapping import (
    internal__load_reversed_thesaurus_as_mapping,
)


def internal__load_cleanup_thesaurus_as_mapping():

    file_paths = files("techminer2.package_data.thesaurus.cleanup").joinpath("*.txt")
    file_paths = str(file_paths)
    file_paths = glob.glob(file_paths)
    mapping = {}
    for file_path in file_paths:
        mapping.update(internal__load_reversed_thesaurus_as_mapping(file_path))
    return mapping
