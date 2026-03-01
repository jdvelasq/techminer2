# CODE_REVIEW: 2025-01-27
"""
Count Column Items
===============================================================================

Smoke test:
    >>> import pandas as pd
    >>> import tempfile
    >>> from pathlib import Path
    >>> from tm2p.scopus._intern.count_column_items import count_column_items

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

from tm2p import CorpusField

from ._file_dispatch import get_file_operations
from .data_file import DataFile


def count_column_items(
    source: CorpusField,
    target: CorpusField,
    root_directory: str,
    file: DataFile = DataFile.MAIN,
) -> int:

    assert isinstance(source, CorpusField)
    assert isinstance(target, CorpusField)

    load_data, save_data, get_path = get_file_operations(file)

    dataframe = load_data(root_directory=root_directory, usecols=None)

    if source.value not in dataframe.columns:
        raise KeyError(
            f"Source column '{source.value}' not found in {get_path(root_directory).name}"
        )

    dataframe[target.value] = (
        dataframe[source.value].str.split("; ").str.len().fillna(0).astype(int)
    )

    save_data(df=dataframe, root_directory=root_directory)

    return int(len(dataframe))
