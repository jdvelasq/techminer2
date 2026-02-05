from techminer2 import CorpusField
from techminer2.io._internals.operations import merge_columns


def compose_all_key_norm(root_directory: str) -> int:

    return merge_columns(
        sources=[
            CorpusField.AUTH_KEY_NORM,
            CorpusField.IDX_KEY_NORM,
        ],
        target=CorpusField.ALL_KEY_NORM,
        root_directory=root_directory,
    )
