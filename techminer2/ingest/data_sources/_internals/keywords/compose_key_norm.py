from techminer2 import CorpusField
from techminer2.ingest.data_sources._internals.operations import merge_columns


def compose_key_norm(root_directory: str) -> int:

    return merge_columns(
        sources=(
            CorpusField.AUTHKW_NORM,
            CorpusField.IDXKW_NORM,
        ),
        target=CorpusField.KW_NORM,
        root_directory=root_directory,
    )
