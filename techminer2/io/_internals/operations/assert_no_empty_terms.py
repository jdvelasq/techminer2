# CODE_REVIEW: 2025-01-27
from pathlib import Path

import pandas as pd


def assert_no_empty_terms(
    source: str,
    root_directory: str = "./",
) -> None:

    database_file = Path(root_directory) / "data" / "processed" / "main.csv.zip"

    if not database_file.exists():
        raise AssertionError(f"{database_file.name} not found")

    try:
        dataframe = pd.read_csv(
            database_file,
            encoding="utf-8",
            compression="zip",
            low_memory=False,
            usecols=[source],
        )
    except ValueError as err:
        raise AssertionError(f'Column "{source}" not found in main.csv.zip') from err

    series = (
        dataframe[source]
        .dropna()
        .astype(str)
        .str.replace(r"\s*;\s*", ";", regex=True)
        .str.split(";")
        .explode()
        .str.strip()
    )

    if (series == "").any():
        raise AssertionError(f'Empty term found in column "{source}"')
