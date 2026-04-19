import pandas as pd  # type: ignore

from tm2p.enum import Field
from tm2p.ingest.datasrc._intern.oper.transform_col import transform_column


def s03_ctry_first(root_directory: str) -> int:

    return transform_column(
        source=Field.CTRY,
        target=Field.CTRY_FIRST,
        function=_extract,
        root_directory=root_directory,
    )


def _extract(series):
    series = series.str.split("; ").str[0]
    series = series.map(lambda x: pd.NA if x == "[UNKNOWN]" else x, na_action="ignore")
    return series
