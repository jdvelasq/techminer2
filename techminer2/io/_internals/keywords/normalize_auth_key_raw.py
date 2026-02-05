from techminer2 import CorpusField

from .helpers import normalize_keywords_helper


def normalize_auth_key_raw(root_directory: str) -> int:

    return normalize_keywords_helper(
        source=CorpusField.AUTH_KEY_RAW,
        target=CorpusField.AUTH_KEY_NORM,
        root_directory=root_directory,
    )
