from techminer2 import CorpusField
from techminer2.ingest.sources._internals.operations import extract_uppercase


def extract_title_phrases(root_directory: str) -> int:

    return extract_uppercase(
        source=CorpusField.DOC_TITLE_TOK_WITH_UPPER_NP,
        target=CorpusField.DOC_TITLE_NP_TOK,
        root_directory=root_directory,
    )
