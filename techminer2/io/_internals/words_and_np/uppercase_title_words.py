from techminer2 import CorpusField
from techminer2.io._internals.operations import uppercase_words


def uppercase_title_words(root_directory: str) -> int:

    return uppercase_words(
        source=CorpusField.DOCTITLE_TOK,
        target=CorpusField.DOCTITLE_TOK_WITH_UPPER_WORD,
        root_directory=root_directory,
    )
