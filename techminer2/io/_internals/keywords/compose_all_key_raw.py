from techminer2 import Field

from ..operations import merge_columns


def compose_all_key_raw(root_directory: str) -> int:

    return merge_columns(
        sources=[
            Field.AUTH_KEY_RAW,
            Field.IDX_KEY_RAW,
        ],
        target=Field.ALL_KEY_RAW,
        root_directory=root_directory,
    )
