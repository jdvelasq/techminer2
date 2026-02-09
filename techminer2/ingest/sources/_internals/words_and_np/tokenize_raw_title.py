from techminer2 import CorpusField
from techminer2.ingest.sources._internals.operations import tokenize_column


def tokenize_raw_title(root_directory: str) -> int:

    return tokenize_column(
        source=CorpusField.DOC_TITLE_RAW,
        target=CorpusField.DOC_TITLE_TOK,
        root_directory=root_directory,
    )
