# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
import pathlib

import pandas as pd


def internal__check_empty_terms(
    source,
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """:meta private:"""

    database_file = pathlib.Path(root_dir) / "databases/database.csv.zip"

    dataframe = pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
        low_memory=False,
    )

    if source in dataframe.columns and not dataframe[source].dropna().empty:
        check_empty_terms(dataframe[source])

    dataframe.to_csv(
        database_file,
        sep=",",
        encoding="utf-8",
        index=False,
        compression="zip",
    )


def check_empty_terms(series):
    series = series.copy()
    series = series.dropna()
    series = series.str.split("; ")
    series = series.explode()
    series = series.str.strip()

    def check_not_empty(x):
        assert x != "", f'Empty term found in column "{series.name}"'

    series.map(check_not_empty)
