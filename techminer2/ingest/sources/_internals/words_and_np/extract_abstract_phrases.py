from techminer2 import CorpusField
from techminer2.ingest.sources._internals.operations import extract_uppercase


def extract_abstract_phrases(root_directory: str) -> int:

    return extract_uppercase(
        source=CorpusField.ABS_TOK_NP_UPPER,
        target=CorpusField.ABS_NP_TOK,
        root_directory=root_directory,
    )
