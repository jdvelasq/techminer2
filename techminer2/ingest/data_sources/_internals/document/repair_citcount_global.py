from techminer2 import CorpusField
from techminer2.ingest.data_sources._internals.operations import transform_column


def repair_citcount_global(root_directory: str) -> int:

    return transform_column(
        source=CorpusField.GCS,
        target=CorpusField.GCS,
        function=lambda w: w.fillna(0).astype(int),
        root_directory=root_directory,
    )
