from techminer2 import Field
from techminer2.io._internals.operations import extract_uppercase


def extract_abstract_words(root_directory: str) -> int:

    return extract_uppercase(
        source=Field.ABS_UPPER_WORD,
        target=Field.WORD_ABS_RAW,
        root_directory=root_directory,
    )
