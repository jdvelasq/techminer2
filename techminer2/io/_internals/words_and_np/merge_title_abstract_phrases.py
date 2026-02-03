from techminer2 import Field
from techminer2.io._internals.operations import merge_columns


def merge_title_abstract_phrases(root_directory: str) -> int:

    return merge_columns(
        sources=[
            Field.NP_ABS_RAW,
            Field.NP_TITLE_RAW,
        ],
        target=Field.ALLNP_RAW,
        root_directory=root_directory,
    )
