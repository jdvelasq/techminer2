from pathlib import Path

from tm2p import CorpusField
from tm2p.ingest.data_sourc._intern.operations.coalesce_column import coalesce_column
from tm2p.ingest.data_sourc._intern.operations.ltwa_column import ltwa_column
from tm2p.ingest.data_sourc._intern.operations.transform_column import transform_column

from ..operations.data_file import DataFile


def _transform(x):
    x = x.str.replace(".", "", regex=False)
    x = x.str.replace(",", "", regex=False)
    x = x.str.upper()
    return x


def normalize_srctitle_abbr_raw(root_directory: str) -> int:

    ref_file = Path(root_directory) / "ingest" / "processed" / "references.csv.zip"

    if ref_file.exists():
        coalesce_column(
            source=CorpusField.SRC_NORM,
            target=CorpusField.SRC_ISO4_NORM,
            root_directory=root_directory,
            file=DataFile.REFERENCES,
        )

        transform_column(
            source=CorpusField.SRC_ISO4_NORM,
            target=CorpusField.SRC_ISO4_NORM,
            function=_transform,
            root_directory=root_directory,
            file=DataFile.REFERENCES,
        )

    coalesce_column(
        source=CorpusField.SRC_NORM,
        target=CorpusField.SRC_ISO4_NORM,
        root_directory=root_directory,
        file=DataFile.MAIN,
    )

    transform_column(
        source=CorpusField.SRC_ISO4_NORM,
        target=CorpusField.SRC_ISO4_NORM,
        function=_transform,
        root_directory=root_directory,
        file=DataFile.MAIN,
    )

    return ltwa_column(
        source=CorpusField.SRC_ISO4_NORM,
        target=CorpusField.SRC_ISO4_NORM,
        root_directory=root_directory,
        file=DataFile.MAIN,
    )
