from tm2p.enum import Field
from tm2p.ingest.data_source._intern.oper.transform_col import transform_column


def s02_org_first(root_directory: str) -> int:

    return transform_column(
        source=Field.ORG,
        target=Field.ORG_FIRST,
        function=_extract,
        root_directory=root_directory,
    )


def _extract(series):
    return series.str.split("; ").str[0]
