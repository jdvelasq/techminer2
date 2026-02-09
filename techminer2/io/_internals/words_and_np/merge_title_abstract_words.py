from techminer2 import CorpusField
from techminer2.io._internals.operations import copy_column, merge_columns


def merge_title_abstract_words(root_directory: str) -> int:

    result = merge_columns(
        sources=[
            CorpusField.ABS_WORD_TOK,
            CorpusField.DOCTITLE_WORD_TOK,
        ],
        target=CorpusField.WORD_TOK,
        root_directory=root_directory,
    )

    copy_column(
        source=CorpusField.WORD_TOK,
        target=CorpusField.WORD_NORM,
        root_directory=root_directory,
    )

    return result
