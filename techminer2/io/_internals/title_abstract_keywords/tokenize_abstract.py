from techminer2.io._internals.operations import tokenize_column


def tokenize_abstract(root_directory: str) -> int:

    return tokenize_column(
        source="abstract_raw",
        target="abstract_tokenized",
        root_directory=root_directory,
    )
