# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

import pathlib

import pandas as pd  # type: ignore


def internal__merge_fields(
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

    new_field = None

    for field in source:
        if field in dataframe.columns:
            if new_field is None:
                new_field = dataframe[field].astype(str).str.split("; ")
            else:
                new_field = new_field + dataframe[field].astype(str).str.split("; ")

    #
    # Remove duplicates and sort
    new_field = new_field.map(lambda x: [z for z in x if z != "nan"])
    new_field = new_field.map(lambda x: sorted(set(x)), na_action="ignore")
    new_field = new_field.map("; ".join, na_action="ignore")
    new_field = new_field.map(lambda x: x if x != "" else pd.NA)

    #
    # Create the new field
    dataframe[dest] = new_field

    dataframe.to_csv(
        database_file,
        sep=",",
        encoding="utf-8",
        index=False,
        compression="zip",
    )
