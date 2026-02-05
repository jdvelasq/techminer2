from techminer2 import CorpusField
from techminer2.io._internals.operations import copy_column, extract_uppercase


def extract_abstract_phrases(root_directory: str) -> int:

    result = extract_uppercase(
        source=CorpusField.ABS_UPPER_NP,
        target=CorpusField.NP_ABS_RAW,
        root_directory=root_directory,
    )

    copy_column(
        source=CorpusField.NP_ABS_RAW,
        target=CorpusField.NP_ABS_NORM,
        root_directory=root_directory,
    )

    return result
