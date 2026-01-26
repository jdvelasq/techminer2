from techminer2.io._internals.operations import merge_columns


def compose_keywords_norm(root_directory: str) -> int:

    return merge_columns(
        sources=[
            "author_keywords_norm",
            "index_keywords_norm",
        ],
        target="keywords_norm",
        root_directory=root_directory,
    )
