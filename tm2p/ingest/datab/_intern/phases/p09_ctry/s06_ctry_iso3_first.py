import pandas as pd  # type: ignore

from tm2p import Field
from tm2p._intern.packag_data import load_builtin_mapping
from tm2p.ingest.oper.transform_column import transform_column


def s06_ctry_iso3_first(root_directory: str) -> int:

    country_to_iso3 = load_builtin_mapping("country_to_alpha3.json")

    def _transform(series):
        series = series.map(
            lambda x: country_to_iso3.get(x, pd.NA),
            na_action="ignore",
        )
        return series

    return transform_column(
        source=Field.CTRY_FIRST,
        target=Field.CTRY_ISO3_FIRST,
        function=_transform,
        root_directory=root_directory,
    )
