from techminer2 import Field
from techminer2.io._internals.operations import uppercase_descriptors


def uppercase_abstract(root_directory: str) -> int:

    return uppercase_descriptors(
        source=Field.ABS_TOK,
        target=Field.ABS_UPPER,
        root_directory=root_directory,
    )
