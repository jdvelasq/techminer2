from techminer2.io._internals.operations import count_column_items


def calculate_num_authors(root_directory):

    return count_column_items(
        source="authors",
        target="num_authors",
        root_directory=root_directory,
    )


#
