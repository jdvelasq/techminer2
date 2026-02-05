from techminer2 import CorpusField
from techminer2.io._internals.operations import extract_uppercase


def extract_title_words(root_directory: str) -> int:

    return extract_uppercase(
        source=CorpusField.TITLE_UPPER_WORD,
        target=CorpusField.WORD_TITLE_RAW,
        root_directory=root_directory,
    )
