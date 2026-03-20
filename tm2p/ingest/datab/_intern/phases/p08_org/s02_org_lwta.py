from tm2p import Field
from tm2p.ingest.datab._intern.oper.ltwa_col import ltwa_column
from tm2p.ingest.datab._intern.phases.get_datab_marker import get_datab_marker


def s02_org_lwta(root_directory: str) -> int:

    marker = get_datab_marker(root_directory)
    function = {
        "OpenAlex": None,
        "PubMed": _scopus,
        "Scopus": _scopus,
        "WoS": _scopus,
    }[marker]

    if function:
        return function(root_directory)
    return 0


def _scopus(root_directory: str) -> int:

    return ltwa_column(
        source=Field.ORG,
        target=Field.ORG,
        root_directory=root_directory,
    )
