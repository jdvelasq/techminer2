import pandas as pd  # type: ignore

from tm2p._internals import Params
from tm2p._internals.data_access import load_filtered_main_data


def extract_values(params: Params) -> pd.DataFrame:
    field = params.source_field.value
    df = load_filtered_main_data(params)[[field]].dropna().copy()
    df[field] = df[field].str.split("; ")
    return (
        df.explode(field)
        .assign(**{field: lambda d: d[field].str.strip()})
        .drop_duplicates()
        .reset_index(drop=True)
        .rename(columns={field: "term"})
    )
