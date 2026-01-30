from techminer2 import Field
from techminer2.io._internals.operations.coalesce_column import coalesce_column


def normalize_source_title_abbr(root_directory: str) -> int:

    return coalesce_column(
        source=Field.SRCTITLE_ABBR,
        target=Field.SRCTITLE_NORM,
        root_directory=root_directory,
    )
