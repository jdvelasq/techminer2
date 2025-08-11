# flake8: noqa
"""Drop empty columns in databases."""
import pathlib
import sys

import pandas as pd  # type: ignore


def internal__drop_empty_columns(root_dir):
    """Drop NA columns in database/ directory"""

    sys.stderr.write("INFO  Dropping NA columns in database file\n")
    sys.stderr.flush()

    dataframe = pd.read_csv(
        pathlib.Path(root_dir) / "data/processed/database.csv.zip",
        encoding="utf-8",
        compression="zip",
        low_memory=False,
    )

    original_cols = dataframe.columns.copy()
    dataframe = dataframe.dropna(axis=1, how="all")

    dataframe.to_csv(
        pathlib.Path(root_dir) / "data/processed/database.csv.zip",
        sep=",",
        encoding="utf-8",
        index=False,
        compression="zip",
    )

    if len(dataframe.columns) != len(original_cols):
        removed_cols = set(original_cols) - set(dataframe.columns)

        for i_col, col in enumerate(removed_cols):
            if i_col == 0:
                sys.stderr.write("Dropped columns:\n")
            sys.stderr.write(f"  - {col}\n")

    sys.stderr.flush()
