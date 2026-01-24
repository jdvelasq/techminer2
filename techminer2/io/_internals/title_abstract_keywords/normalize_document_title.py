from techminer2.io._internals.operations import uppercase_descriptors


def normalize_document_title(root_directory: str) -> int:

    return uppercase_descriptors(
        source="tokenized_document_title",
        target="document_title",
        root_directory=root_directory,
    )
