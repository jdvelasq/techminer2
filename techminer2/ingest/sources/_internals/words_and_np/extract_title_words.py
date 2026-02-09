from techminer2 import CorpusField
from techminer2.ingest.sources._internals.operations import extract_uppercase


def extract_title_words(root_directory: str) -> int:

    return extract_uppercase(
        source=CorpusField.DOC_TITLE_TOK_WITH_UPPER_WORD,
        target=CorpusField.DOC_TITLE_WORD_TOK,
        root_directory=root_directory,
    )
