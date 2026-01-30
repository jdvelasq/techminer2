from techminer2 import Field
from techminer2.io._internals.operations import merge_columns


def compose_keywords_norm(root_directory: str) -> int:

    return merge_columns(
        sources=[
            Field.AUTHKEY_NORM,
            Field.IDXKEY_NORM,
        ],
        target=Field.KEY_NORM,
        root_directory=root_directory,
    )
