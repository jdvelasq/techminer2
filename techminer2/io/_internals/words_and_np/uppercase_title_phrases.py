from techminer2 import Field
from techminer2.io._internals.operations import uppercase_keyterms


def uppercase_title_phrases(root_directory: str) -> int:

    return uppercase_keyterms(
        source=Field.TITLE_TOK,
        target=Field.TITLE_UPPER_NP,
        root_directory=root_directory,
    )
