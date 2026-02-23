from pathlib import Path

from techminer2 import CorpusField
from techminer2.ingest.data_sources._internals.operations.coalesce_column import (
    coalesce_column,
)

from ..operations.data_file import DataFile


def normalize_srctitle_abbr_raw(root_directory: str) -> int:

    ref_file = Path(root_directory) / "ingest" / "processed" / "references.csv.zip"

    if ref_file.exists():
        coalesce_column(
            source=CorpusField.SRC_TITLE_ABBR_RAW,
            target=CorpusField.SRC_TITLE_ABBR_NORM,
            root_directory=root_directory,
            file=DataFile.REFERENCES,
        )

    return coalesce_column(
        source=CorpusField.SRC_TITLE_ABBR_RAW,
        target=CorpusField.SRC_TITLE_ABBR_NORM,
        root_directory=root_directory,
        file=DataFile.MAIN,
    )
