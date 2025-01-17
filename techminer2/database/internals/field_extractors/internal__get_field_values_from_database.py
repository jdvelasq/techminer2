# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

import pathlib

import pandas as pd  # type: ignore


def internal__get_field_values_from_database(root_dir, field):
    """Returns a DataFrame with the content of the field in all databases."""

    database_file = pathlib.Path(root_dir) / "databases/database.csv.zip"

    dataframe = pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
    )

    df = dataframe[[field]].dropna()

    df[field] = df[field].str.split("; ")
    df = df.explode(field)
    df[field] = df[field].str.strip()
    df = df.drop_duplicates()
    df = df.reset_index(drop=True)
    df = df.rename(columns={field: "term"})

    return df
