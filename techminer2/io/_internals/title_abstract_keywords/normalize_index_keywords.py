from techminer2 import Field

from .helpers.normalize_keywords_helper import normalize_keywords_helper


def normalize_index_keywords(root_directory: str) -> int:

    return normalize_keywords_helper(
        source=Field.IDXKEY_RAW.value,
        target=Field.IDXKEY_NORM.value,
        root_directory=root_directory,
    )
