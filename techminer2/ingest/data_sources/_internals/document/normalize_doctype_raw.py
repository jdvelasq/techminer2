from techminer2 import CorpusField
from techminer2.ingest.data_sources._internals.operations import transform_column


def normalize_doctype_raw(root_directory: str) -> int:

    return transform_column(
        source=CorpusField.DOC_TYPE_RAW,
        target=CorpusField.DOC_TYPE_NORM,
        function=lambda x: x.str.capitalize(),
        root_directory=root_directory,
    )
