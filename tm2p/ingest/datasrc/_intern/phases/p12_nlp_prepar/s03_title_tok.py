from tm2p.enum import Field
from tm2p.ingest.datasrc._intern.oper import tokenize_column


def s03_title_tok(root_directory: str) -> int:

    return tokenize_column(
        source=Field.TITLE_RAW,
        target=Field.TITLE_TOK,
        root_directory=root_directory,
    )
