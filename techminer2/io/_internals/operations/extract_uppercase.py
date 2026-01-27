# CODE_REVIEW: 2026-01-23
from pathlib import Path

import pandas as pd  # type: ignore


def _extract_uppercase_words(text):
    if pd.isna(text):
        return pd.NA
    words = [word for word in str(text).split() if word.isupper()]
    return "; ".join(words) if words else pd.NA


def extract_uppercase(source: str, target: str, root_directory: str) -> int:

    database_file = Path(root_directory) / "data" / "processed" / "main.csv.zip"

    if not database_file.exists():
        raise AssertionError(f"{database_file.name} not found")

    dataframe = pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
        low_memory=False,
    )

    if source not in dataframe.columns:
        return 0

    dataframe[target] = dataframe[source].apply(_extract_uppercase_words)

    non_null_count = int(dataframe[target].notna().sum())

    temp_file = database_file.with_suffix(".tmp")
    dataframe.to_csv(
        temp_file,
        sep=",",
        encoding="utf-8",
        index=False,
        compression="zip",
    )
    temp_file.replace(database_file)

    return non_null_count
