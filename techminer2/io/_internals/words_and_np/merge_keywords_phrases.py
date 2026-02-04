from techminer2 import Field
from techminer2.io._internals.operations import copy_column, merge_columns


def merge_keywords_phrases(root_directory: str) -> int:

    result = merge_columns(
        sources=[
            Field.ALL_KEY_RAW,
            Field.ALL_NP_RAW,
        ],
        target=Field.ALL_KEY_NP_RAW,
        root_directory=root_directory,
    )

    copy_column(
        source=Field.ALL_KEY_NP_RAW,
        target=Field.ALL_KEY_NP_NORM,
        root_directory=root_directory,
    )

    return result
