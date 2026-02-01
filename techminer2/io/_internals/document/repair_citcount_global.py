from techminer2 import Field
from techminer2.io._internals.operations import transform_column


def repair_citcount_global(root_directory: str) -> int:

    return transform_column(
        source=Field.CITCOUNT_GLOBAL,
        target=Field.CITCOUNT_GLOBAL,
        function=lambda w: w.fillna(0).astype(int),
        root_directory=root_directory,
    )
