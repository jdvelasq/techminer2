from tm2p.enum import Field
from tm2p.ingest.datasrc._intern.oper import uppercase_keyterms


def s11_title_upper(root_directory: str) -> int:

    return uppercase_keyterms(
        source=Field.TITLE_TOK,
        target=Field.TITLE_UPPER,
        root_directory=root_directory,
    )
