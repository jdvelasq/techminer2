from tm2p.enum import Field
from tm2p.ingest.datasrc._intern.oper.transform_col import transform_column


def s04_ctry(root_directory: str) -> int:

    return transform_column(
        source=Field.CTRY,
        target=Field.CTRY,
        function=_extract,
        root_directory=root_directory,
    )


def _extract(series):
    series = series.str.split("; ")
    series = series.map(
        lambda x: [y for y in x if y != "[UNKNOWN]"], na_action="ignore"
    )
    series = series.map(set, na_action="ignore")
    series = series.map(sorted, na_action="ignore")
    series = series.str.join("; ")
    return series
