from tm2p.enum import Field
from tm2p.ingest.datab._intern.oper.copy_col import copy_column
from tm2p.ingest.datab._intern.oper.transform_col import transform_column


def s03_auth_raw_scopus(root_directory: str) -> int:

    transform_column(
        source=Field.AUTH_RAW,
        target=Field.AUTH_RAW,
        function=_normalize,
        root_directory=root_directory,
    )

    return copy_column(
        source=Field.AUTH_RAW,
        target=Field.AUTH_NORM,
        root_directory=root_directory,
    )


def _normalize(series):
    series = series.copy()
    series = series.str.replace(".", "", regex=False)
    series = series.str.replace(",", "", regex=False)
    return series
