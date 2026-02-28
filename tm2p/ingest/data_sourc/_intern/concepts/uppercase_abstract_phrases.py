from tm2p import CorpusField
from tm2p.ingest.data_sourc._intern.operations import uppercase_keyterms


def uppercase_abstract_phrases(root_directory: str) -> int:

    return uppercase_keyterms(
        source=CorpusField.ABSTR_TOK,
        target=CorpusField.ABSTR_UPPER,
        root_directory=root_directory,
    )
