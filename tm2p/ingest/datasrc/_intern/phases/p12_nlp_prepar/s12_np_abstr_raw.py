from tm2p.enum import Field
from tm2p.ingest.datasrc._intern.oper import extract_uppercase


def s12_np_abstr_raw(root_directory: str) -> int:

    return extract_uppercase(
        source=Field.ABSTR_UPPER,
        target=Field.NP_ABSTR_RAW,
        root_directory=root_directory,
    )
