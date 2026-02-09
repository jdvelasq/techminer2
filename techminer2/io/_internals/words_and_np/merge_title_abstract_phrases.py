from techminer2 import CorpusField
from techminer2.io._internals.operations import copy_column, merge_columns


def merge_title_abstract_phrases(root_directory: str) -> int:

    result = merge_columns(
        sources=[
            CorpusField.ABS_NP_TOK,
            CorpusField.DOCTITLE_NP_TOK,
        ],
        target=CorpusField.NP_TOK,
        root_directory=root_directory,
    )

    copy_column(
        source=CorpusField.NP_TOK,
        target=CorpusField.NP_NORM,
        root_directory=root_directory,
    )

    return result
