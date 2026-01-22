from techminer2.io._internals.operators.copy_column import copy_column


def create_abstract_column(root_directory: str) -> int:

    return internal__copy(
        source="tokenized_abstract", target="abstract", root_directory=root_directory
    )
