from pathlib import Path

import pandas as pd  # type: ignore


def rename_column(source: str, target: str, root_directory: str) -> int:

    database_file = Path(root_directory) / "data" / "processed" / "main.csv.zip"

    dataframe = pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
    )

    if source not in dataframe.columns:
        return 0

    dataframe = dataframe.rename(columns={source: target})

    dataframe.to_csv(
        database_file,
        sep=",",
        encoding="utf-8",
        index=False,
        compression="zip",
    )

    return len(dataframe)
