from techminer2.io._internals.operations import tokenize_column


def tokenize_document_title(root_directory: str) -> int:

    return tokenize_column(
        source="document_title_raw",
        target="document_title_tokenized",
        root_directory=root_directory,
    )
