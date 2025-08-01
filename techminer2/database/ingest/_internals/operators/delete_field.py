# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

import pathlib

import pandas as pd  # type: ignore

from ....._dtypes import DTYPES


def internal__delete_field(
    field,
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

    dataframe = dataframe.drop(field, axis=1)

    dataframe.to_csv(
        database_file,
        sep=",",
        encoding="utf-8",
        index=False,
        compression="zip",
    )
