from techminer2 import CorpusField
from techminer2.io._internals.operations import tokenize_column


def tokenize_raw_title(root_directory: str) -> int:

    return tokenize_column(
        source=CorpusField.DOCTITLE_RAW,
        target=CorpusField.DOCTITLE_TOK,
        root_directory=root_directory,
    )
