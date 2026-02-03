from techminer2 import Field
from techminer2.io._internals.operations import extract_uppercase


def extract_title_phrases(root_directory: str) -> int:

    return extract_uppercase(
        source=Field.TITLE_UPPER_NP,
        target=Field.NP_TITLE_RAW,
        root_directory=root_directory,
    )
