# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals

import pathlib

import pandas as pd  # type: ignore


def internal__collect(
    source,
    dest,
    #
    # DATABASE PARAMS:
    root_dir,
):
    """:meta private:"""

    database_file = pathlib.Path(root_dir) / "data/processed/database.csv.zip"

    dataframe = pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
        low_memory=False,
    )

    if source not in dataframe.columns:
        return

    text_column = dataframe[source]
    text_column = text_column.str.split()
    text_column = text_column.map(
        lambda y: [word for word in y if word.isupper()], na_action="ignore"
    )
    text_column = text_column.map(
        lambda y: pd.NA if len(y) == 0 else y, na_action="ignore"
    )
    text_column = text_column.str.join("; ")

    dataframe[dest] = text_column

    dataframe.to_csv(
        database_file,
        sep=",",
        encoding="utf-8",
        index=False,
        compression="zip",
    )
