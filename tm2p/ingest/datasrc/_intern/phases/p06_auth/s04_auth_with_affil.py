from tm2p.enum import Field
from tm2p.ingest.datasrc._intern.oper.copy_col import copy_column
from tm2p.ingest.datasrc._intern.phases.get_datab_marker import get_datab_marker


def s04_auth_with_affil(root_directory: str) -> int:

    marker = get_datab_marker(root_directory)
    function = {
        "OpenAlex": None,
        "PubMed": None,
        "Scopus": None,
        "WoS": _wos,
    }[marker]

    if function:
        return function(root_directory)

    return 0


def _wos(root_directory: str) -> int:
    return copy_column(
        source=Field.AFFIL,
        target=Field.AUTH_WITH_AFFIL,
        root_directory=root_directory,
    )
