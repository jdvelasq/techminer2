from techminer2 import Field
from techminer2.io._internals.operations import copy_column, merge_columns


def merge_title_abstract_words(root_directory: str) -> int:

    result = merge_columns(
        sources=[
            Field.WORD_ABS_RAW,
            Field.WORD_TITLE_RAW,
        ],
        target=Field.ALL_WORD_RAW,
        root_directory=root_directory,
    )

    copy_column(
        source=Field.ALL_WORD_RAW,
        target=Field.ALL_WORD_NORM,
        root_directory=root_directory,
    )

    return result
