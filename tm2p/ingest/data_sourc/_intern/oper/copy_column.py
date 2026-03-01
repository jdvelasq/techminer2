# CODE_REVIEW: 2025-01-27
"""
Copy Column
===============================================================================

Smoke test:
    >>> import pandas as pd
    >>> import tempfile
    >>> from pathlib import Path
    >>> from tm2p.scopus._intern.copy_column import copy_column

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
    ...     n = copy_column(Fields.A, Fields.B, root)
    ...     df_new = pd.read_csv(file_path, compression="zip")
    ...     print(f"Copied: {n}")
    ...     print(df_new.columns.tolist())
    ...     print(df_new["B"].tolist())
    ...
    ...     # Case 2: Missing Source (Fail Loudly)
    ...     try:
    ...         copy_column(Fields.Z, Fields.X, root)
    ...     except KeyError as e:
    ...         print("Caught expected error")
    Copied: 2
    ['A', 'B']
    [1.0, 2.0, nan]
    Caught expected error

"""

from tm2p import CorpusField

from ._file_dispatch import get_file_operations
from .data_file import DataFile


def copy_column(
    source: CorpusField,
    target: CorpusField,
    root_directory: str,
    file: DataFile = DataFile.MAIN,
) -> int:

    load_data, save_data, get_path = get_file_operations(file)

    dataframe = load_data(root_directory=root_directory, usecols=None)

    if source.value not in dataframe.columns:
        raise KeyError(
            f"Source column '{source.value}' not found in {get_path(root_directory).name}"
        )

    dataframe[target.value] = dataframe[source.value]

    save_data(df=dataframe, root_directory=root_directory)

    return int(dataframe[target.value].notna().sum())
