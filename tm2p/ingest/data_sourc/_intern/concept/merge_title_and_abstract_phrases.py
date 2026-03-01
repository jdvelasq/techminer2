from tm2p import CorpusField
from tm2p.ingest.data_sourc._intern.oper import merge_columns


def merge_title_and_abstract_phrases(root_directory: str) -> int:

    return merge_columns(
        sources=(
            CorpusField.NP_ABSTR_RAW,
            CorpusField.NP_TITLE_RAW,
        ),
        target=CorpusField.NP_RAW,
        root_directory=root_directory,
    )
