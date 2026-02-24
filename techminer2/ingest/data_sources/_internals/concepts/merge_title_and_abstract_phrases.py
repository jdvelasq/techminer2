from techminer2 import CorpusField
from techminer2.ingest.data_sources._internals.operations import merge_columns


def merge_title_and_abstract_phrases(root_directory: str) -> int:

    return merge_columns(
        sources=(
            CorpusField.NP_ABS_RAW,
            CorpusField.NP_TITLE_RAW,
        ),
        target=CorpusField.NP_RAW,
        root_directory=root_directory,
    )
