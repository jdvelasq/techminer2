from techminer2 import Field
from techminer2.io._internals.operations import merge_columns


def compose_all_key_norm(root_directory: str) -> int:

    return merge_columns(
        sources=[
            Field.AUTH_KEY_NORM,
            Field.IDX_KEY_NORM,
        ],
        target=Field.ALL_KEY_NORM,
        root_directory=root_directory,
    )
