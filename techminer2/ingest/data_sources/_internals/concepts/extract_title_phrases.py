from techminer2 import CorpusField
from techminer2.ingest.data_sources._internals.operations import extract_uppercase


def extract_title_phrases(root_directory: str) -> int:

    return extract_uppercase(
        source=CorpusField.TITLE_UPPER,
        target=CorpusField.NP_TITLE_RAW,
        root_directory=root_directory,
    )
