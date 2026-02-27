from techminer2 import CorpusField

from ..operations import copy_column


def normalize_idx_key_raw(root_directory: str) -> int:

    return copy_column(
        source=CorpusField.IDXKW_TOK,
        target=CorpusField.IDXKW_NORM,
        root_directory=root_directory,
    )
