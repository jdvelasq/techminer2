from techminer2 import CorpusField
from techminer2.ingest.data_sources._internals.operations import merge_columns


def merge_title_and_abstract_words(root_directory: str) -> int:

    return merge_columns(
        sources=(
            CorpusField.ABS_WORD_TOK,
            CorpusField.TITLE_WORD_TOK,
        ),
        target=CorpusField.WORD_TOK,
        root_directory=root_directory,
    )
