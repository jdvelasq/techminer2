from techminer2 import CorpusField
from techminer2.ingest.sources._internals.operations import copy_column, merge_columns


def merge_keywords_phrases_words(root_directory: str) -> int:

    result = merge_columns(
        sources=(
            CorpusField.KEY_TOK,
            CorpusField.NP_TOK,
            CorpusField.WORD_TOK,
        ),
        target=CorpusField.DESCRIPTOR_TOK,
        root_directory=root_directory,
    )

    copy_column(
        source=CorpusField.DESCRIPTOR_TOK,
        target=CorpusField.DESCRIPTOR_NORM,
        root_directory=root_directory,
    )

    return result
