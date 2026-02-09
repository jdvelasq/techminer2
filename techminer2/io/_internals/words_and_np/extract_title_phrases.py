from techminer2 import CorpusField
from techminer2.io._internals.operations import copy_column, extract_uppercase


def extract_title_phrases(root_directory: str) -> int:

    result = extract_uppercase(
        source=CorpusField.DOCTITLE_TOK_WITH_UPPER_NP,
        target=CorpusField.DOCTITLE_NP_TOK,
        root_directory=root_directory,
    )

    copy_column(
        source=CorpusField.DOCTITLE_NP_TOK,
        target=CorpusField.DOCTITLE_NP_NORM,
        root_directory=root_directory,
    )

    return result
