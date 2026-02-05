from techminer2 import CorpusField

from .helpers.normalize_keywords_helper import normalize_keywords_helper


def normalize_idx_key_raw(root_directory: str) -> int:

    return normalize_keywords_helper(
        source=CorpusField.IDX_KEY_RAW,
        target=CorpusField.IDX_KEY_NORM,
        root_directory=root_directory,
    )
