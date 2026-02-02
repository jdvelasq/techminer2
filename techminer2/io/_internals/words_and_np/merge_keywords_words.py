from techminer2 import Field
from techminer2.io._internals.operations import merge_columns


def merge_keywords_words(root_directory: str) -> int:

    return merge_columns(
        sources=[
            Field.ALLKEY_RAW,
            Field.ALLWORD_RAW,
        ],
        target=Field.ALLKEY_WORD_RAW,
        root_directory=root_directory,
    )
