from ..operations import merge_columns


def compose_keywords_raw(root_directory: str) -> int:

    return merge_columns(
        sources=[
            "author_keywords_raw",
            "index_keywords_raw",
        ],
        target="keywords_raw",
        root_directory=root_directory,
    )
