from tm2p import CorpusField
from tm2p.ingest.data_sources._internals.operations import count_column_items


def calculate_numref_global(root_directory: str) -> int:

    return count_column_items(
        source=CorpusField.REF_RAW,
        target=CorpusField.N_REF_GBL,
        root_directory=root_directory,
    )


#
