from techminer2 import Field
from techminer2.io._internals.operations import merge_columns


def merge_title_abstract_words(root_directory: str) -> int:

    return merge_columns(
        sources=[
            Field.WORD_ABS_RAW,
            Field.WORD_TITLE_RAW,
        ],
        target=Field.ALLWORD_RAW,
        root_directory=root_directory,
    )
