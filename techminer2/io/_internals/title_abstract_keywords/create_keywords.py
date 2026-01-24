from techminer2.io._internals.operations import merge_columns


def create_keywords(root_directory: str) -> int:

    return merge_columns(
        sources=[
            "author_keywords",
            "index_keywords",
        ],
        target="keywords",
        root_directory=root_directory,
    )
