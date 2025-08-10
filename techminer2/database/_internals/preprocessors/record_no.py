"""Create art_no column in databses."""

import pathlib
import sys

import pandas as pd  # type: ignore


def internal__preprocess_record_no(root_dir):
    """Create art_no column in databases."""
    #
    sys.stderr.write("INFO  Assign 'record_no' identifier to each record\n")
    sys.stderr.flush()

    database_file = pathlib.Path(root_dir) / "data/processed/database.csv.zip"

    dataframe = pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
        low_memory=False,
    )

    dataframe["record_no"] = range(1, len(dataframe) + 1)

    dataframe.to_csv(
        database_file,
        sep=",",
        encoding="utf-8",
        index=False,
        compression="zip",
    )


#
