# flake8: noqa
"""Drop empty columns in databases."""

import pathlib

import pandas as pd  # type: ignore

from .....internals.log_info_message import log_info_message


def internal__drop_empty_columns(root_dir):
    """Drop NA columns in database/ directory"""

    log_info_message("Dropping NA columns in database file")

    dataframe = pd.read_csv(
        pathlib.Path(root_dir) / "databases/database.csv.zip",
        encoding="utf-8",
        compression="zip",
    )

    original_cols = dataframe.columns.copy()
    dataframe = dataframe.dropna(axis=1, how="all")

    dataframe.to_csv(
        pathlib.Path(root_dir) / "databases/database.csv.zip",
        sep=",",
        encoding="utf-8",
        index=False,
        compression="zip",
    )

    if len(dataframe.columns) != len(original_cols):
        removed_cols = set(original_cols) - set(dataframe.columns)
        print(f"     ---> Removed columns: {removed_cols}")
