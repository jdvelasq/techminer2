from tm2p.enum import Field
from tm2p.ingest.datasrc._intern.oper.transform_col import transform_column


def s03_org_set(root_directory: str) -> int:

    return transform_column(
        source=Field.ORG,
        target=Field.ORG,
        function=_extract,
        root_directory=root_directory,
    )


def _extract(series):
    series = series.str.split("; ")
    series = series.map(set, na_action="ignore")
    series = series.map(sorted, na_action="ignore")
    series = series.str.join("; ")
    return series
