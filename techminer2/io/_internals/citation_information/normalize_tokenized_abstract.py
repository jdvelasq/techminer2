from techminer2.io._internals.operations.tokenize_column import tokenize_column


def normalize_tokenized_abstract(root_directory: str) -> int:

    return tokenize_column(
        source="raw_abstract",
        target="tokenized_abstract",
        root_directory=root_directory,
    )
