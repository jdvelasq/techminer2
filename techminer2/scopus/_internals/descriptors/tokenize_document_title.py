from techminer2.scopus._internals.operators.tokenize_column import tokenize_column


def tokenize_document_title(root_directory: str) -> int:

    return tokenize_column(
        source="raw_document_title",
        target="tokenized_document_title",
        root_directory=root_directory,
    )
