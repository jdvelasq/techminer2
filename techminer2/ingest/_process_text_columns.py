"""Process text columns in all database files."""

import glob
import os

import pandas as pd  #  type: ignore

from ._message import message


def process_text_columns(root_dir, process_func, msg):
    """Process text columns in all database files.

    Args:
        root_dir (str): root directory.
        process_func (function): function to be applied to each column.

    :meta private:
    """
    message(f"Processing text columns ({msg})")

    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8", compression="zip")
        cols = data.select_dtypes(include=["object"]).columns
        for col in cols:
            data[col] = process_func(data[col])
        data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")
