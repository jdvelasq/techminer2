from techminer2 import CorpusField
from techminer2.io._internals.operations import uppercase_keyterms


def uppercase_abstract_phrases(root_directory: str) -> int:

    return uppercase_keyterms(
        source=CorpusField.ABS_TOK,
        target=CorpusField.ABS_TOK_WITH_UPPER_NP,
        root_directory=root_directory,
    )
