"""
Smoke test:
    >>> from tm2p.enum import ThFile
    >>> from tm2p.refine._intern.data_access import get_thesaurus_path
    >>> get_thesaurus_path(
    ...     root_directory="my_root_directory", file=ThFile.CONCEPT
    ... )
    PosixPath('my_root_directory/refine/thesaurus/concept.the.txt')

"""

from pathlib import Path

from tm2p.enum import ThFile


def get_thesaurus_path(root_directory: str, file: ThFile) -> Path:

    return Path(root_directory) / "refine" / "thesaurus" / file.value
