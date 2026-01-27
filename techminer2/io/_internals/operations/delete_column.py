# CODE_REVIEW: 2025-01-27
"""
Delete Column
===============================================================================

Smoke test:
    >>> import pandas as pd
    >>> import tempfile
    >>> from pathlib import Path
    >>> from techminer2.scopus._internals.delete_column import delete_column

    >>> with tempfile.TemporaryDirectory() as temp_dir:
    ...     root = str(Path(temp_dir))
    ...     data_dir = Path(root) / "data" / "processed"
    ...     data_dir.mkdir(parents=True)
    ...     file_path = data_dir / "main.csv.zip"
    ...
    ...     # Setup: DataFrame with two columns
    ...     df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
    ...     df.to_csv(file_path, index=False, compression="zip")
    ...
    ...     # Case 1: Valid Deletion
    ...     rows = delete_column("B", root)
    ...     df_new = pd.read_csv(file_path, compression="zip")
    ...     print(f"Rows processed: {rows}")
    ...     print(df_new.columns.tolist())
    ...
    ...     # Case 2: Missing Column (Fail Loudly)
    ...     try:
    ...         delete_column("Z", root)
    ...     except KeyError as e:
    ...         print("Caught expected error")
    Rows processed: 2
    ['A']
    Caught expected error

"""
from pathlib import Path

import pandas as pd


def delete_column(column: str, root_directory: str) -> int:

    database_file = Path(root_directory) / "data" / "processed" / "main.csv.zip"

    if not database_file.exists():
        raise AssertionError(f"{database_file.name} not found")

    dataframe = pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
        low_memory=False,
    )

    if column not in dataframe.columns:
        raise KeyError(f"Column '{column}' not found in {database_file.name}")

    dataframe = dataframe.drop(columns=column)

    temp_file = database_file.with_suffix(".tmp")
    dataframe.to_csv(
        temp_file,
        sep=",",
        encoding="utf-8",
        index=False,
        compression="zip",
    )
    temp_file.replace(database_file)

    return len(dataframe)
