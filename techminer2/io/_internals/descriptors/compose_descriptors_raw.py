from techminer2 import Field
from techminer2.io._internals.operations import merge_columns


def compose_descriptors_raw(root_directory: str) -> int:

    return merge_columns(
        sources=[
            Field.ALLKEY_RAW,
            Field.NP,
        ],
        target=Field.KEYTERMS_RAW,
        root_directory=root_directory,
    )
