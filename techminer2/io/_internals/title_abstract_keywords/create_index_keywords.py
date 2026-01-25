from techminer2.io._internals.operations import copy_column


def create_index_keywords(root_directory: str) -> int:

    return copy_column(
        source="cleaned_index_keywords",
        target="index_keywords",
        root_directory=root_directory,
    )
