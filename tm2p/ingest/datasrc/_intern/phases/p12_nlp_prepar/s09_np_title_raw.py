from tm2p.enum import Field
from tm2p.ingest.datasrc._intern.oper import extract_uppercase


def s09_np_title_raw(root_directory: str) -> int:

    return extract_uppercase(
        source=Field.TITLE_UPPER,
        target=Field.NP_TITLE_RAW,
        root_directory=root_directory,
    )
