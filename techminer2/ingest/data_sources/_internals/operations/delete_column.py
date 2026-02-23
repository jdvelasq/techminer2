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

from techminer2 import CorpusField

from ._file_dispatch import get_file_operations
from .data_file import DataFile


def delete_column(
    column: CorpusField,
    root_directory: str,
    file: DataFile = DataFile.MAIN,
) -> int:

    load_data, save_data, get_path = get_file_operations(file)

    dataframe = load_data(root_directory=root_directory, usecols=None)

    if column.value not in dataframe.columns:
        raise KeyError(
            f"Column '{column.value}' not found in {get_path(root_directory).name}"
        )
    dataframe = dataframe.drop(columns=column.value)
    save_data(df=dataframe, root_directory=root_directory)

    return len(dataframe)
