from tm2p import Field
from tm2p.ingest.datab._intern.oper.transform_col import transform_column


def s04_org_first(root_directory: str) -> int:

    return transform_column(
        source=Field.ORG,
        target=Field.ORG_FIRST,
        function=_extract,
        root_directory=root_directory,
    )


def _extract(series):
    return series.str.split("; ").str[0]
