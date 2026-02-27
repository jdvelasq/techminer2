from pathlib import Path

from techminer2 import CorpusField
from techminer2.ingest.data_sources._internals.operations import transform_column

from ..operations.data_file import DataFile


def _normalize(text):
    text = text.str.replace("<.*?>", "", regex=True)
    return text


def normalize_srctitle_raw(root_directory: str) -> int:

    ref_file = Path(root_directory) / "ingest" / "processed" / "references.csv.zip"

    if ref_file.exists():

        transform_column(
            source=CorpusField.SRC_RAW,
            target=CorpusField.SRC_NORM,
            function=_normalize,
            root_directory=root_directory,
            file=DataFile.REFERENCES,
        )

    return transform_column(
        source=CorpusField.SRC_RAW,
        target=CorpusField.SRC_NORM,
        function=_normalize,
        root_directory=root_directory,
        file=DataFile.MAIN,
    )
