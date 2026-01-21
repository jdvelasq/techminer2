from pathlib import Path
from typing import Callable

import pandas as pd  # type: ignore


def transform_column(
    source: str,
    target: str,
    function: Callable,
    root_directory: str,
) -> int:

    database_file = Path(root_directory) / "data" / "processed" / "main.csv.zip"

    dataframe = pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
    )

    if source not in dataframe.columns:
        return 0

    dataframe[target] = function(dataframe[source])

    dataframe.to_csv(
        database_file,
        sep=",",
        encoding="utf-8",
        index=False,
        compression="zip",
    )

    return len(dataframe[target].dropna())
