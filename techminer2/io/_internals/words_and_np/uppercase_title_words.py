from techminer2 import Field
from techminer2.io._internals.operations import uppercase_words


def uppercase_title_words(root_directory: str) -> int:

    return uppercase_words(
        source=Field.TITLE_TOK,
        target=Field.TITLE_UPPER_WORD,
        root_directory=root_directory,
    )
