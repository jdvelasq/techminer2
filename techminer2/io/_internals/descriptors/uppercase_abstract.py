from techminer2 import Field
from techminer2.io._internals.operations import uppercase_keyterms


def uppercase_abstract(root_directory: str) -> int:

    return uppercase_keyterms(
        source=Field.ABS_TOK,
        target=Field.ABS_UPPER,
        root_directory=root_directory,
    )
