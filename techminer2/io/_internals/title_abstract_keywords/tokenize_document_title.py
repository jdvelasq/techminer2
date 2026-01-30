from techminer2 import Field
from techminer2.io._internals.operations import tokenize_column


def tokenize_document_title(root_directory: str) -> int:

    return tokenize_column(
        source=Field.TITLE_RAW,
        target=Field.TITLE_TOK,
        root_directory=root_directory,
    )
