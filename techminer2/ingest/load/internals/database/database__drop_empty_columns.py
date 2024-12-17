"""Drop empty columns in databases."""

import glob
import os

import pandas as pd  # type: ignore

from ..._message import message


def database__drop_empty_columns(root_dir):
    """Drop NA columns in database/ directory"""

    message("Dropping NA columns in database files")

    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8", compression="zip")
        original_cols = data.columns.copy()
        data = data.dropna(axis=1, how="all")
        if len(data.columns) != len(original_cols):
            removed_cols = set(original_cols) - set(data.columns)
            print(f"     ---> Removed columns: {removed_cols}")
        data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")
