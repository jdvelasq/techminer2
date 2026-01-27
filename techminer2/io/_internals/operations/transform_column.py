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
