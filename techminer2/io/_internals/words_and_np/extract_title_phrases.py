from techminer2 import CorpusField
from techminer2.io._internals.operations import copy_column, extract_uppercase


def extract_title_phrases(root_directory: str) -> int:

    result = extract_uppercase(
        source=CorpusField.TITLE_UPPER_NP,
        target=CorpusField.NP_TITLE_RAW,
        root_directory=root_directory,
    )

    copy_column(
        source=CorpusField.NP_TITLE_RAW,
        target=CorpusField.NP_TITLE_NORM,
        root_directory=root_directory,
    )

    return result
