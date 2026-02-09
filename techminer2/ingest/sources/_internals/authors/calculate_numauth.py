from techminer2 import CorpusField
from techminer2.ingest.sources._internals.operations import count_column_items


def calculate_numauth(root_directory):

    return count_column_items(
        source=CorpusField.AUTH_NORM,
        target=CorpusField.NUM_AUTH,
        root_directory=root_directory,
    )
