"""

Smoke test:
    >>> from tm2p._intern.data_access import get_references_data_path
    >>> get_references_data_path("my_root_directory")
    PosixPath('my_root_directory/data/processed/references.csv.zip')


"""

from pathlib import Path


def get_references_data_path(root_directory: str) -> Path:

    return Path(root_directory) / "ingest" / "processed" / "references.csv.zip"
