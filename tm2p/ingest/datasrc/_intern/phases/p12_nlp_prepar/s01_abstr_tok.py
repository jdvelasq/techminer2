from tm2p.enum import Field
from tm2p.ingest.datasrc._intern.oper import tokenize_column


def s01_abstr_tok(root_directory: str) -> int:

    return tokenize_column(
        source=Field.ABSTR_RAW,
        target=Field.ABSTR_TOK,
        root_directory=root_directory,
    )
