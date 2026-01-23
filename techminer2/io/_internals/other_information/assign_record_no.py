from pathlib import Path

import pandas as pd  # type: ignore


def assign_record_no(root_directory):

    database_file = Path(root_directory) / "data" / "processed" / "main.csv.zip"

    dataframe = pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
        low_memory=False,
    )

    num_zeros = len(str(len(dataframe)))
    dataframe["record_no"] = [
        f"{i:0{num_zeros}d}" for i in range(1, len(dataframe) + 1)
    ]

    dataframe.to_csv(
        database_file,
        sep=",",
        encoding="utf-8",
        index=False,
        compression="zip",
    )
