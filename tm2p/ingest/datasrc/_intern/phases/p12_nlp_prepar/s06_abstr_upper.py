from tm2p.enum import Field
from tm2p.ingest.datasrc._intern.oper import uppercase_keyterms


def s06_abstr_upper(root_directory: str) -> int:

    return uppercase_keyterms(
        source=Field.ABSTR_TOK,
        target=Field.ABSTR_UPPER,
        root_directory=root_directory,
    )
