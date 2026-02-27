from techminer2 import CorpusField
from techminer2.ingest.data_sources._internals.operations import (
    copy_column,
    merge_columns,
)


def merge_keywords_and_phrases(root_directory: str) -> int:

    result = merge_columns(
        sources=(
            CorpusField.KW_TOK,
            CorpusField.NP_RAW,
        ),
        target=CorpusField.CONCEPT_RAW,
        root_directory=root_directory,
    )

    copy_column(
        source=CorpusField.CONCEPT_RAW,
        target=CorpusField.CONCEPT_NORM,
        root_directory=root_directory,
    )

    return result
