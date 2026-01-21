from pathlib import Path

import pandas as pd  # type: ignore


def collect_uppercase_words(source: str, target: str, root_directory: str) -> int:

    database_file = Path(root_directory) / "data" / "processed" / "main.csv.zip"

    dataframe = pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
    )

    if source not in dataframe.columns:
        return 0

    def _extract_uppercase_words(text):
        if pd.isna(text):
            return pd.NA
        words = [word for word in str(text).split() if word.isupper()]
        return "; ".join(words) if words else pd.NA

    dataframe[target] = dataframe[source].apply(_extract_uppercase_words)

    dataframe.to_csv(
        database_file,
        sep=",",
        encoding="utf-8",
        compression="zip",
    )

    return len(dataframe[target].dropna())
