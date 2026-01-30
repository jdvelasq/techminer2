from techminer2 import Field
from techminer2.io._internals.operations import tokenize_column


def tokenize_abstract(root_directory: str) -> int:

    return tokenize_column(
        source=Field.ABS_RAW,
        target=Field.ABS_TOK,
        root_directory=root_directory,
    )
