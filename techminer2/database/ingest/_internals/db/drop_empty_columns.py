# flake8: noqa
"""Drop empty columns in databases."""

import pathlib
import sys

import pandas as pd  # type: ignore

from ....._internals.log_message import internal__log_message


def internal__drop_empty_columns(root_dir):
    """Drop NA columns in database/ directory"""

    sys.stderr.write("\nINFO  Dropping NA columns in database file.")
    sys.stderr.flush()

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
        for i_col, col in enumerate(removed_cols):
            if i_col == 0:
                sys.stderr.write(f"\n        Columns: {col}")
            else:
                sys.stderr.write(f"\n                 {col}")

    sys.stderr.flush()
