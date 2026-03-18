from tm2p import Field
from tm2p.ingest.datab._intern.oper import count_column_items


def s05_n_auth(root_directory: str) -> int:

    return count_column_items(
        source=Field.AUTH_RAW,
        target=Field.N_AUTH,
        root_directory=root_directory,
    )
