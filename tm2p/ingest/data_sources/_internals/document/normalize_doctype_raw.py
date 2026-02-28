from tm2p import CorpusField
from tm2p.ingest.data_sources._internals.operations import transform_column


def normalize_doctype_raw(root_directory: str) -> int:

    return transform_column(
        source=CorpusField.PUBTYPE_RAW,
        target=CorpusField.PUBTYPE_NORM,
        function=lambda x: x.str.capitalize(),
        root_directory=root_directory,
    )
