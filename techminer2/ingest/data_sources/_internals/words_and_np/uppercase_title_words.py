from techminer2 import CorpusField
from techminer2.ingest.data_sources._internals.operations import uppercase_words


def uppercase_title_words(root_directory: str) -> int:

    return uppercase_words(
        source=CorpusField.TITLE_TOK,
        target=CorpusField.TITLE_TOK_WORD_UPPER,
        root_directory=root_directory,
    )
