"""Create art_no column in databses."""

import pathlib

import pandas as pd  # type: ignore

from ..message import message


def preprocessing__record_no(root_dir):
    """Create art_no column in databases."""
    #
    message("Assign record_no identifier to each record")

    database_file = pathlib.Path(root_dir) / "databases/database.csv.zip"

    dataframe = pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
    )

    dataframe["record_no"] = range(1, len(dataframe) + 1)

    dataframe.to_csv(
        database_file,
        sep=",",
        encoding="utf-8",
        index=False,
        compression="zip",
    )