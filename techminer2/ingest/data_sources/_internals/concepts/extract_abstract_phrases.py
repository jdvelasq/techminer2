from techminer2 import CorpusField
from techminer2.ingest.data_sources._internals.operations import extract_uppercase


def extract_abstract_phrases(root_directory: str) -> int:

    return extract_uppercase(
        source=CorpusField.ABS_UPPER,
        target=CorpusField.NP_ABS_RAW,
        root_directory=root_directory,
    )
