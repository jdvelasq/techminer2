from tm2p import CorpusField
from tm2p.ingest.data_sources._internals.operations import uppercase_keyterms


def uppercase_title_phrases(root_directory: str) -> int:

    return uppercase_keyterms(
        source=CorpusField.TITLE_TOK,
        target=CorpusField.TITLE_UPPER,
        root_directory=root_directory,
    )
