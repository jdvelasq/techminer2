# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

import pathlib

import pandas as pd  # type: ignore


def internal__fillna(
    fill_field,
    with_field,
    #
    # DATABASE PARAMS:
    root_dir,
):
    database_file = pathlib.Path(root_dir) / "databases/database.csv.zip"

    dataframe = pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
    )

    if fill_field in dataframe.columns:

        dataframe[fill_field] = dataframe[fill_field].mask(
            dataframe[fill_field].isna(),
            dataframe[with_field],
        )

        dataframe.to_csv(
            database_file,
            sep=",",
            encoding="utf-8",
            index=False,
            compression="zip",
        )
