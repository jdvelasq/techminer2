from techminer2 import CorpusField
from techminer2.ingest.data_sources._internals.operations import transform_column


def repair_citcount_global(root_directory: str) -> int:

    return transform_column(
        source=CorpusField.CIT_COUNT_GLOBAL,
        target=CorpusField.CIT_COUNT_GLOBAL,
        function=lambda w: w.fillna(0).astype(int),
        root_directory=root_directory,
    )
