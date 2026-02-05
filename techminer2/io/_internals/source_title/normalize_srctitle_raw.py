from pathlib import Path

from techminer2 import CorpusField
from techminer2.io._internals.operations import transform_column

from ..operations.data_file import DataFile


def _normalize(text):
    #
    #              DYNA (Colombia)
    # Sustainability (Switzerland)
    #              npj Clean Water
    # Automotive Engineer (London)
    #
    text = text.str.replace("-", "_", regex=False)
    text = text.str.replace("<.*?>", "", regex=True)
    return text


def normalize_srctitle_raw(root_directory: str) -> int:

    ref_file = Path(root_directory) / "data" / "processed" / "references.csv.zip"

    if ref_file.exists():

        transform_column(
            source=CorpusField.SRC_TITLE_RAW,
            target=CorpusField.SRC_TITLE_NORM,
            function=_normalize,
            root_directory=root_directory,
            file=DataFile.REFERENCES,
        )

    return transform_column(
        source=CorpusField.SRC_TITLE_RAW,
        target=CorpusField.SRC_TITLE_NORM,
        function=_normalize,
        root_directory=root_directory,
        file=DataFile.MAIN,
    )
