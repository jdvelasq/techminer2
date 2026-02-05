from techminer2 import CorpusField
from techminer2.io._internals.operations import copy_column, merge_columns


def merge_keywords_phrases(root_directory: str) -> int:

    result = merge_columns(
        sources=[
            CorpusField.ALL_KEY_RAW,
            CorpusField.ALL_NP_RAW,
        ],
        target=CorpusField.ALL_KEY_NP_RAW,
        root_directory=root_directory,
    )

    copy_column(
        source=CorpusField.ALL_KEY_NP_RAW,
        target=CorpusField.ALL_KEY_NP_NORM,
        root_directory=root_directory,
    )

    return result
