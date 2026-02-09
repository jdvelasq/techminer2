from techminer2 import CorpusField
from techminer2.io._internals.operations import copy_column, merge_columns


def merge_keywords_phrases(root_directory: str) -> int:

    result = merge_columns(
        sources=[
            CorpusField.KEY_TOK,
            CorpusField.NP_TOK,
        ],
        target=CorpusField.KEY_AND_NP_TOK,
        root_directory=root_directory,
    )

    copy_column(
        source=CorpusField.KEY_AND_NP_TOK,
        target=CorpusField.KEY_AND_NP_NORM,
        root_directory=root_directory,
    )

    return result
