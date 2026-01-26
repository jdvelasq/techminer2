from techminer2.io._internals.operations import uppercase_descriptors


def uppercase_abstract(root_directory: str) -> int:

    return uppercase_descriptors(
        source="abstract_tokenized",
        target="abstract",
        root_directory=root_directory,
    )
