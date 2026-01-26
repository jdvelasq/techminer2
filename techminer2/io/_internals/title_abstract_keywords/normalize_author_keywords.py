from .helpers import normalize_keywords_helper


def normalize_author_keywords(root_directory: str) -> int:

    return normalize_keywords_helper(
        source="author_keywords_raw",
        target="author_keywords_norm",
        root_directory=root_directory,
    )
