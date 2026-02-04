from techminer2 import Field
from techminer2.io._internals.operations import copy_column, merge_columns


def merge_title_abstract_phrases(root_directory: str) -> int:

    result = merge_columns(
        sources=[
            Field.NP_ABS_RAW,
            Field.NP_TITLE_RAW,
        ],
        target=Field.ALL_NP_RAW,
        root_directory=root_directory,
    )

    copy_column(
        source=Field.ALL_NP_RAW, target=Field.ALL_NP_NORM, root_directory=root_directory
    )

    return result
