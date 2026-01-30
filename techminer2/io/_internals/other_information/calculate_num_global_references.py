from techminer2 import Field
from techminer2.io._internals.operations import count_column_items


def calculate_num_global_references(root_directory: str) -> int:

    return count_column_items(
        source=Field.REF_GLOBAL_RAW,
        target=Field.NUMREF,
        root_directory=root_directory,
    )


#
