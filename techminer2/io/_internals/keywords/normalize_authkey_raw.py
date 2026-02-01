from techminer2 import Field

from .helpers import normalize_keywords_helper


def normalize_authkey_raw(root_directory: str) -> int:

    return normalize_keywords_helper(
        source=Field.AUTHKEY_RAW,
        target=Field.AUTHKEY_NORM,
        root_directory=root_directory,
    )
