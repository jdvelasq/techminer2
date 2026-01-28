from pathlib import Path
from typing import Callable

import pandas as pd
from pandas import Series


def transform_column(
    source: str,
    target: str,
    function: Callable[[Series], Series],
    root_directory: str,
    file: str = "main.csv.zip",
) -> int:

    database_file = Path(root_directory) / "data" / "processed" / file

    if not database_file.exists():
        raise AssertionError(f"{database_file.name} not found")

    dataframe = pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
        low_memory=False,
    )

    if source not in dataframe.columns:
        return 0

    dataframe[target] = function(dataframe[source])

    non_null_count = int(dataframe[target].notna().sum())

    temp_file = database_file.with_suffix(".tmp")
    dataframe.to_csv(
        temp_file,
        sep=",",
        encoding="utf-8",
        index=False,
        compression="zip",
    )
    temp_file.replace(database_file)

    return non_null_count
