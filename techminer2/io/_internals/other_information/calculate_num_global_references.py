from techminer2.io._internals.operators.count_items import count_items


def calculate_num_global_references(root_directory: str) -> int:

    return count_items(
        source="global_references",
        target="num_global_references",
        root_directory=root_directory,
    )


#
