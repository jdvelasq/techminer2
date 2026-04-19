from tm2p.enum import Field
from tm2p.ingest.datasrc._intern.oper.copy_col import copy_column


def s07_auth_norm(root_directory: str) -> int:

    return copy_column(
        source=Field.AUTH_RAW,
        target=Field.AUTH_NORM,
        root_directory=root_directory,
    )
