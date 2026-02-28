from tm2p import CorpusField

from ..operations import copy_column


def normalize_auth_key_raw(root_directory: str) -> int:

    return copy_column(
        source=CorpusField.AUTHKW_TOK,
        target=CorpusField.AUTHKW_NORM,
        root_directory=root_directory,
    )
