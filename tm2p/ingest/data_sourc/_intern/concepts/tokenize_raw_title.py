from tm2p import CorpusField
from tm2p.ingest.data_sourc._intern.operations import tokenize_column


def tokenize_raw_title(root_directory: str) -> int:

    return tokenize_column(
        source=CorpusField.TITLE_RAW,
        target=CorpusField.TITLE_TOK,
        root_directory=root_directory,
    )
