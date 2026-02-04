from techminer2 import Field
from techminer2.io._internals.operations import copy_column, extract_uppercase


def extract_title_phrases(root_directory: str) -> int:

    result = extract_uppercase(
        source=Field.TITLE_UPPER_NP,
        target=Field.NP_TITLE_RAW,
        root_directory=root_directory,
    )

    copy_column(
        source=Field.NP_TITLE_RAW,
        target=Field.NP_TITLE_NORM,
        root_directory=root_directory,
    )

    return result
