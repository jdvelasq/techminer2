from tm2p import CorpusField
from tm2p.ingest.data_sourc._intern.oper import uppercase_keyterms


def uppercase_title_phrases(root_directory: str) -> int:

    return uppercase_keyterms(
        source=CorpusField.TITLE_TOK,
        target=CorpusField.TITLE_UPPER,
        root_directory=root_directory,
    )
