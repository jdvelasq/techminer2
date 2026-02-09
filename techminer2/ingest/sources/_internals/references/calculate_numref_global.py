from techminer2 import CorpusField
from techminer2.ingest.sources._internals.operations import count_column_items


def calculate_numref_global(root_directory: str) -> int:

    return count_column_items(
        source=CorpusField.REF_RAW,
        target=CorpusField.NUM_REF_GLOBAL,
        root_directory=root_directory,
    )


#
