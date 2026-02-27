from techminer2 import CorpusField
from techminer2.ingest.data_sources._internals.operations import tokenize_column


def tokenize_raw_abstract(root_directory: str) -> int:

    return tokenize_column(
        source=CorpusField.ABSTR_RAW,
        target=CorpusField.ABSTR_TOK,
        root_directory=root_directory,
    )
