from techminer2 import Field

from ..operations import merge_columns


def compose_keywords_raw(root_directory: str) -> int:

    return merge_columns(
        sources=[
            Field.AUTHKEY_RAW,
            Field.IDXKEY_RAW,
        ],
        target=Field.ALLKEY_RAW,
        root_directory=root_directory,
    )
