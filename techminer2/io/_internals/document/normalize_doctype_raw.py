from techminer2 import Field
from techminer2.io._internals.operations import transform_column


def normalize_doctype_raw(root_directory: str) -> int:

    return transform_column(
        source=Field.DOC_TYPE_RAW,
        target=Field.DOC_TYPE_NORM,
        function=lambda x: x.str.capitalize(),
        root_directory=root_directory,
    )
