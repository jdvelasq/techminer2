from tm2p import CorpusField
from tm2p.ingest.data_sourc._internals.operations import count_column_items


def calculate_numauth(root_directory):

    return count_column_items(
        source=CorpusField.AUTH_NORM,
        target=CorpusField.N_AUTH,
        root_directory=root_directory,
    )
