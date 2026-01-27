# CODE_REVIEW: 2025-01-27
"""
Coalesce Column
===============================================================================

Smoke test:
    >>> import pandas as pd
    >>> import tempfile
    >>> from pathlib import Path
    >>> from techminer2.io._internals.operations.coalesce_column import coalesce_column

    >>> with tempfile.TemporaryDirectory() as temp_dir:
    ...     root = str(Path(temp_dir))
    ...     data_dir = Path(root) / "data" / "processed"
    ...     data_dir.mkdir(parents=True)
    ...     file_path = data_dir / "main.csv.zip"
    ...
    ...     # Setup: Create dummy data
    ...     df = pd.DataFrame({"A": [1, 2, None], "B": [None, 2, 3]})
    ...     df.to_csv(file_path, index=False, compression="zip")
    ...
    ...     # Coalesce B with A (fill NA in B from A)
    ...     n = coalesce_column("A", "B", root)
    ...     df_new = pd.read_csv(file_path, compression="zip")
    ...     print(f"Coalesced: {n}")
    ...     print(df_new.columns.tolist())
    ...     print(df_new["B"].tolist())
    Coalesced: 3
    ['A', 'B']
    [1.0, 2.0, 3.0]

"""
from pathlib import Path

import pandas as pd


def coalesce_column(source: str, target: str, root_directory: str) -> int:

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

    if target in dataframe.columns:
        dataframe[target] = dataframe[target].fillna(dataframe[source])
    else:
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
