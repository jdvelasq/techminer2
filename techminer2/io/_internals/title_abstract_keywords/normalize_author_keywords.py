from techminer2 import Field

from .helpers import normalize_keywords_helper


def normalize_author_keywords(root_directory: str) -> int:

    return normalize_keywords_helper(
        source=Field.AUTHKEY_RAW.value,
        target=Field.AUTHKEY_NORM.value,
        root_directory=root_directory,
    )
