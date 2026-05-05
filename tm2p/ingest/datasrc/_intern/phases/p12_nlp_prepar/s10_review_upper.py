from tm2p.enum import Field
from tm2p.ingest.datasrc._intern.oper import review_upperc


def s10_review_upper(root_directory: str) -> int:

    return review_upperc(
        source=Field.ABSTR_UPPER,
        target=Field.ABSTR_UPPER,
        root_directory=root_directory,
    )
