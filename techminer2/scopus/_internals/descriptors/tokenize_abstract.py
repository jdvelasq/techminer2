from techminer2.scopus._internals.operators.tokenize_column import tokenize_column


def tokenize_abstract(root_directory: str) -> int:

    return tokenize_column(
        source="raw_abstract",
        target="tokenized_abstract",
        root_directory=root_directory,
    )
