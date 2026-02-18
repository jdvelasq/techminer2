from importlib.resources import files

import pandas as pd  # type: ignore


def load_csv(filename: str) -> pd.DataFrame:

    datapath = files("techminer2._internals.package_data.csv.data").joinpath(filename)

    return pd.read_csv(str(datapath), encoding="utf-8")
