"""

Smoke test:
    >>> from tm2p._intern.data_access import get_thesaurus_path
    >>> get_thesaurus_path(
    ...     root_directory="my_root_directory", file="file.the.txt"
    ... )
    PosixPath('my_root_directory/data/thesaurus/file.the.txt')


"""

from pathlib import Path


def get_thesaurus_path(root_directory: str, file: str) -> Path:

    return Path(root_directory) / "refine" / "thesaurus" / file
