from techminer2 import Field
from techminer2.io._internals.operations import extract_uppercase


def extract_abstract_noun_phrases_raw(root_directory: str) -> int:

    return extract_uppercase(
        source=Field.ABS_TOK,
        target=Field.NP_ABS_RAW,
        root_directory=root_directory,
    )
