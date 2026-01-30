from techminer2 import Field
from techminer2.io._internals.operations import transform_column


def normalize_document_type(root_directory: str) -> int:

    return transform_column(
        source=Field.DOCTYPE_RAW,
        target=Field.DOCTYPE_NORM,
        function=lambda x: x.str.capitalize(),
        root_directory=root_directory,
    )
