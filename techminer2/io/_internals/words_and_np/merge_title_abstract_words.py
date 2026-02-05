from techminer2 import CorpusField
from techminer2.io._internals.operations import copy_column, merge_columns


def merge_title_abstract_words(root_directory: str) -> int:

    result = merge_columns(
        sources=[
            CorpusField.WORD_ABS_RAW,
            CorpusField.WORD_TITLE_RAW,
        ],
        target=CorpusField.ALL_WORD_RAW,
        root_directory=root_directory,
    )

    copy_column(
        source=CorpusField.ALL_WORD_RAW,
        target=CorpusField.ALL_WORD_NORM,
        root_directory=root_directory,
    )

    return result
