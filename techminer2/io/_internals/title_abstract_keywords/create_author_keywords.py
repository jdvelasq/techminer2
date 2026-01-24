from techminer2.io._internals.operations import copy_column


def create_author_keywords(root_directory: str) -> int:

    return copy_column(
        source="raw_author_keywords",
        target="author_keywords",
        root_directory=root_directory,
    )
