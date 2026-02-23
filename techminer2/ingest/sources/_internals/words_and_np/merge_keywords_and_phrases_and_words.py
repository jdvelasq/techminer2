from techminer2 import CorpusField
from techminer2.ingest.sources._internals.operations import copy_column, merge_columns


def merge_keywords_and_phrases_and_words(root_directory: str) -> int:

    result = merge_columns(
        sources=(
            CorpusField.HYB_KEY_TOK,
            CorpusField.NP_TOK,
            CorpusField.WORD_TOK,
        ),
        target=CorpusField.TERM_TOK,
        root_directory=root_directory,
    )

    copy_column(
        source=CorpusField.TERM_TOK,
        target=CorpusField.TERM_NORM,
        root_directory=root_directory,
    )

    return result
