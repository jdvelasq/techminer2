from techminer2 import CorpusField
from techminer2.ingest.data_sources._internals.operations import merge_columns


def merge_title_and_abstract_phrases(root_directory: str) -> int:

    return merge_columns(
        sources=(
            CorpusField.ABS_NP_TOK,
            CorpusField.TITLE_NP_TOK,
        ),
        target=CorpusField.NP_TOK,
        root_directory=root_directory,
    )
