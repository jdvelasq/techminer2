from techminer2 import Field
from techminer2.io._internals.operations import extract_uppercase


def extract_document_title_noun_phrases_raw(root_directory: str) -> int:

    return extract_uppercase(
        source=Field.TITLE_TOK,
        target=Field.NP,
        root_directory=root_directory,
    )
