# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
import pathlib

import pandas as pd  # type: ignore


def internal__count(
    source,
    dest,
    #
    # DATABASE PARAMS:
    root_dir,
):
    database_file = pathlib.Path(root_dir) / "data/processed/database.csv.zip"

    dataframe = pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
        low_memory=False,
    )

    if source not in dataframe.columns:
        return

    dataframe[dest] = dataframe[source].str.split("; ")
    dataframe[dest] = dataframe[dest].map(len, na_action="ignore")
    dataframe[dest] = dataframe[dest].fillna(0).astype(int)

    dataframe.to_csv(
        database_file,
        sep=",",
        encoding="utf-8",
        index=False,
        compression="zip",
    )
