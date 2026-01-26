from .helpers.normalize_keywords_helper import normalize_keywords_helper


def normalize_index_keywords(root_directory: str) -> int:

    return normalize_keywords_helper(
        source="index_keywords_raw",
        target="index_keywords_norm",
        root_directory=root_directory,
    )
