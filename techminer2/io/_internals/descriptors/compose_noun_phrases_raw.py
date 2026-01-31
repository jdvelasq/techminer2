from techminer2 import Field
from techminer2.io._internals.operations import merge_columns


def compose_noun_phrases_raw(root_directory: str) -> int:

    return merge_columns(
        sources=[
            Field.NP_ABS_RAW,
            Field.NP,
        ],
        target=Field.NP,
        root_directory=root_directory,
    )
