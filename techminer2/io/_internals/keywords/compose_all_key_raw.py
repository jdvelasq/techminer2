from techminer2 import CorpusField

from ..operations import merge_columns


def compose_all_key_raw(root_directory: str) -> int:

    return merge_columns(
        sources=[
            CorpusField.AUTH_KEY_RAW,
            CorpusField.IDX_KEY_RAW,
        ],
        target=CorpusField.ALL_KEY_RAW,
        root_directory=root_directory,
    )
