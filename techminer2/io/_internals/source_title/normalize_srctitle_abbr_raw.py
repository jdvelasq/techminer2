from techminer2 import Field
from techminer2.io._internals.operations.coalesce_column import coalesce_column


def normalize_srctitle_abbr_raw(root_directory: str) -> int:

    return coalesce_column(
        source=Field.SRCTITLE_ABBR_RAW,
        target=Field.SRCTITLE_ABBR_NORM,
        root_directory=root_directory,
    )
