from techminer2 import CorpusField
from techminer2.ingest.data_sources._internals.operations import (
    copy_column,
    merge_columns,
)


def merge_keywords_and_words(root_directory: str) -> int:

    result = merge_columns(
        sources=(
            CorpusField.HYB_KEY_TOK,
            CorpusField.WORD_TOK,
        ),
        target=CorpusField.KEY_AND_WORD_TOK,
        root_directory=root_directory,
    )

    copy_column(
        source=CorpusField.KEY_AND_WORD_TOK,
        target=CorpusField.KEY_AND_WORD_NORM,
        root_directory=root_directory,
    )

    return result
