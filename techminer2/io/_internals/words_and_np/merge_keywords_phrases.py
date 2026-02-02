from techminer2 import Field
from techminer2.io._internals.operations import merge_columns


def merge_keywords_phrases(root_directory: str) -> int:

    return merge_columns(
        sources=[
            Field.ALLKEY_RAW,
            Field.ALLNP_RAW,
        ],
        target=Field.ALLKEY_NP_RAW,
        root_directory=root_directory,
    )
