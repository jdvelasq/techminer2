from techminer2 import CorpusField
from techminer2.ingest.data_sources._internals.operations import tokenize_column


def tokenize_raw_abstract(root_directory: str) -> int:

    return tokenize_column(
        source=CorpusField.ABS_RAW,
        target=CorpusField.ABS_TOK,
        root_directory=root_directory,
    )
