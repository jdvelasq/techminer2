from techminer2 import Field
from techminer2.io._internals.operations import count_column_items


def calculate_num_authors(root_directory):

    return count_column_items(
        source=Field.AUTH,
        target=Field.NUMAUTH,
        root_directory=root_directory,
    )


#
