from techminer2 import Field
from techminer2.io._internals.operations import merge_columns


def compose_noun_phrases_raw(root_directory: str) -> int:

    return merge_columns(
        sources=[
            Field.NOUNPH_ABS_RAW,
            Field.NOUNPH_TITLE_RAW,
        ],
        target=Field.NOUNPH_RAW,
        root_directory=root_directory,
    )
