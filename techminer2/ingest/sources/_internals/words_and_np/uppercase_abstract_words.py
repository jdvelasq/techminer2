from techminer2 import CorpusField
from techminer2.ingest.sources._internals.operations import uppercase_words


def uppercase_abstract_words(root_directory: str) -> int:

    return uppercase_words(
        source=CorpusField.ABS_TOK,
        target=CorpusField.ABS_TOK_WORD_UPPER,
        root_directory=root_directory,
    )
