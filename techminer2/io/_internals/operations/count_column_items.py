# CODE_REVIEW: 2025-01-27
"""
Count Column Items
===============================================================================

Smoke test:
    >>> import pandas as pd
    >>> import tempfile
    >>> from pathlib import Path
    >>> from techminer2.scopus._internals.count_column_items import count_column_items

    >>> with tempfile.TemporaryDirectory() as temp_dir:
    ...     root = str(Path(temp_dir))
    ...     data_dir = Path(root) / "data" / "processed"
    ...     data_dir.mkdir(parents=True)
    ...     file_path = data_dir / "main.csv.zip"
    ...
    ...     # Setup: Data using strict "; " separator
    ...     df = pd.DataFrame({
    ...         "authors": ["A; B", "C", None, "D; E; F"]
    ...     })
    ...     df.to_csv(file_path, index=False, compression="zip")
    ...
    ...     # Case 1: Valid Count
    ...     n = count_column_items("authors", "num_authors", root)
    ...     df_new = pd.read_csv(file_path, compression="zip")
    ...     print(f"Rows processed: {n}")
    ...     print(df_new["num_authors"].tolist())
    ...
    ...     # Case 2: Missing Source (Fail Loudly)
    ...     try:
    ...         count_column_items("missing", "x", root)
    ...     except KeyError as e:
    ...         print("Caught expected error")
    Rows processed: 4
    [2, 1, 0, 3]
    Caught expected error

"""
from pathlib import Path

import pandas as pd


def count_column_items(source: str, target: str, root_directory: str) -> int:

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
        raise KeyError(f"Source column '{source}' not found in {database_file.name}")

    dataframe[target] = (
        dataframe[source].str.split("; ").str.len().fillna(0).astype(int)
    )

    non_null_count = int(len(dataframe))

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
