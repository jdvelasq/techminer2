from techminer2 import Field
from techminer2.io._internals.operations import count_column_items


def calculate_numref_global(root_directory: str) -> int:

    return count_column_items(
        source=Field.REF_RAW,
        target=Field.NUMREF_GLOBAL,
        root_directory=root_directory,
    )


#
