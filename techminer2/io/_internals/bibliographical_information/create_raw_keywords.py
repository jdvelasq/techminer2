from techminer2.io.operators.merge import merge_columns


def create_raw_keywords(root_directory: str) -> int:

    return merge_columns(
        sources=[
            "raw_author_keywords",
            "raw_index_keywords",
        ],
        target="raw_keywords",
        root_directory=root_directory,
    )
