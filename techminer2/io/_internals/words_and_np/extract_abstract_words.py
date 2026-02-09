from techminer2 import CorpusField
from techminer2.io._internals.operations import extract_uppercase


def extract_abstract_words(root_directory: str) -> int:

    return extract_uppercase(
        source=CorpusField.ABS_TOK_WITH_UPPER_WORD,
        target=CorpusField.ABS_WORD_TOK,
        root_directory=root_directory,
    )
