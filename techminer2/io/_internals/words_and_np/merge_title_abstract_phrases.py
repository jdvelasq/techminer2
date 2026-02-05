from techminer2 import CorpusField
from techminer2.io._internals.operations import copy_column, merge_columns


def merge_title_abstract_phrases(root_directory: str) -> int:

    result = merge_columns(
        sources=[
            CorpusField.NP_ABS_RAW,
            CorpusField.NP_TITLE_RAW,
        ],
        target=CorpusField.ALL_NP_RAW,
        root_directory=root_directory,
    )

    copy_column(
        source=CorpusField.ALL_NP_RAW,
        target=CorpusField.ALL_NP_NORM,
        root_directory=root_directory,
    )

    return result
