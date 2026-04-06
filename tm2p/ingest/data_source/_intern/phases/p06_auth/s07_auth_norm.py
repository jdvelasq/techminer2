from tm2p._intern.enum import Field
from tm2p.ingest.data_source._intern.oper.copy_col import copy_column


def s07_auth_norm(root_directory: str) -> int:

    return copy_column(
        source=Field.AUTH_RAW,
        target=Field.AUTH_NORM,
        root_directory=root_directory,
    )
