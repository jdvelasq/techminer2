import pandas as pd  # type: ignore

from tm2p.enum import Field
from tm2p.ingest.datasrc._intern.oper import transform_column


def s06_auth_first(root_directory: str) -> int:

    def _extract(series: pd.Series) -> pd.Series:
        return series.str.split(";").str[0].str.strip()

    return transform_column(
        source=Field.AUTH_RAW,
        target=Field.AUTH_FIRST,
        function=_extract,
        root_directory=root_directory,
    )
