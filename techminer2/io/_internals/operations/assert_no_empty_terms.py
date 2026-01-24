from pathlib import Path

import pandas as pd


def assert_no_empty_terms(
    source,
    root_directory="./",
):
    """:meta private:"""

    database_file = Path(root_directory) / "data" / "processed" / "main.csv.zip"

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
