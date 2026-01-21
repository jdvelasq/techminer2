from techminer2.io._internals.operators.count_items import count_items


def calculate_num_authors(root_directory):

    return count_items(
        source="authors",
        target="num_authors",
        root_directory=root_directory,
    )


#
