# CODE_REVIEW: 2025-01-27
"""
Copy Column
===============================================================================

Smoke test:
    >>> import pandas as pd
    >>> import tempfile
    >>> from pathlib import Path
    >>> from techminer2.scopus._internals.copy_column import copy_column

    >>> with tempfile.TemporaryDirectory() as temp_dir:
    ...     root = str(Path(temp_dir))
    ...     data_dir = Path(root) / "data" / "processed"
    ...     data_dir.mkdir(parents=True)
    ...     file_path = data_dir / "main.csv.zip"
    ...
    ...     # Setup: Create dummy data
    ...     df = pd.DataFrame({"A": [1, 2, None]})
    ...     df.to_csv(file_path, index=False, compression="zip")
    ...
    ...     # Case 1: Valid Copy
    ...     n = copy_column("A", "B", root)
    ...     df_new = pd.read_csv(file_path, compression="zip")
    ...     print(f"Copied: {n}")
    ...     print(df_new.columns.tolist())
    ...     print(df_new["B"].tolist())
    ...
    ...     # Case 2: Missing Source (Fail Loudly)
    ...     try:
    ...         copy_column("Z", "X", root)
    ...     except KeyError as e:
    ...         print("Caught expected error")
    Copied: 2
    ['A', 'B']
    [1.0, 2.0, nan]
    Caught expected error

"""
from pathlib import Path

import pandas as pd


def copy_column(source: str, target: str, root_directory: str) -> int:

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

    dataframe[target] = dataframe[source]

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
