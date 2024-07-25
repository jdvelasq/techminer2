"""Create art_no column in databses."""

import pathlib

import pandas as pd  #  type: ignore

from ._message import message


def create_art_no_column(root_dir):
    """Create art_no column in databases."""
    #
    message("Assign REC-No identifier to each record")

    processed_dir = pathlib.Path(root_dir) / "databases"
    files = list(processed_dir.glob("_*.zip"))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8", compression="zip")
        data["art_no"] = range(1, len(data) + 1)
        data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")
