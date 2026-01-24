from techminer2.io._internals.operations import copy_column


def create_descriptors(root_directory: str) -> int:

    return copy_column(
        source="raw_descriptors",
        target="descriptors",
        root_directory=root_directory,
    )
