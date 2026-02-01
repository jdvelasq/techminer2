from techminer2 import Field
from techminer2.io._internals.operations import count_column_items


def calculate_numauth(root_directory):

    return count_column_items(
        source=Field.AUTH_NORM,
        target=Field.NUMAUTH,
        root_directory=root_directory,
    )
