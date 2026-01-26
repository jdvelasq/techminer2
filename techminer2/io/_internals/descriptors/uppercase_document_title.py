from techminer2.io._internals.operations import uppercase_descriptors


def uppercase_document_title(root_directory: str) -> int:

    return uppercase_descriptors(
        source="document_title_tokenized",
        target="document_title",
        root_directory=root_directory,
    )
