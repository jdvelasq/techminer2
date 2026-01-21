from pathlib import Path

import pandas as pd  # type: ignore


def merge_columns(sources: list[str], target: str, root_directory: str) -> int:

    database_file = Path(root_directory) / "data" / "processed" / "main.csv.zip"

    dataframe = pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
    )

    existing_sources = [col for col in sources if col in dataframe.columns]

    if not existing_sources:
        return 0

    all_items = None
    for source in existing_sources:
        items = dataframe[source].astype(str).str.split("; ")
        all_items = items if all_items is None else all_items + items

    all_items = all_items.map(lambda x: [item for item in x if item and item != "nan"])
    all_items = all_items.map(lambda x: sorted(set(x)) if x else [])

    dataframe[target] = all_items.map(lambda x: "; ".join(x) if x else pd.NA)

    dataframe.to_csv(
        database_file,
        sep=",",
        encoding="utf-8",
        index=False,
        compression="zip",
    )

    return len(dataframe[target].dropna())
