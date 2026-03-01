from tm2p import CorpusField

from ..oper import copy_column


def normalize_idx_key_raw(root_directory: str) -> int:

    return copy_column(
        source=CorpusField.IDXKW_TOK,
        target=CorpusField.IDXKW_NORM,
        root_directory=root_directory,
    )
