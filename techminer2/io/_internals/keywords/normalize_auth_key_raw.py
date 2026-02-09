from techminer2 import CorpusField

from ..operations import copy_column


def normalize_auth_key_raw(root_directory: str) -> int:

    return copy_column(
        source=CorpusField.AUTH_KEY_TOK,
        target=CorpusField.AUTH_KEY_NORM,
        root_directory=root_directory,
    )
