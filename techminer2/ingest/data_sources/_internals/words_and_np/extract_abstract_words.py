from techminer2 import CorpusField
from techminer2.ingest.data_sources._internals.operations import extract_uppercase


def extract_abstract_words(root_directory: str) -> int:

    return extract_uppercase(
        source=CorpusField.ABS_TOK_WORD_UPPER,
        target=CorpusField.ABS_WORD_TOK,
        root_directory=root_directory,
    )
