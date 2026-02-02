from techminer2 import Field
from techminer2.io._internals.operations import uppercase_words


def uppercase_abstract_words(root_directory: str) -> int:

    return uppercase_words(
        source=Field.ABS_TOK,
        target=Field.ABS_UPPER_WORD,
        root_directory=root_directory,
    )
