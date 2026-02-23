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


from techminer2 import CorpusField

from ._file_dispatch import get_file_operations
from .data_file import DataFile


def coalesce_column(
    source: CorpusField,
    target: CorpusField,
    root_directory: str,
    file: DataFile = DataFile.MAIN,
) -> int:

    assert isinstance(source, CorpusField)
    assert isinstance(target, CorpusField)
    assert isinstance(root_directory, str)
    assert isinstance(file, DataFile)

    load_data, save_data, get_path = get_file_operations(file)

    dataframe = load_data(root_directory=root_directory, usecols=None)

    if source.value not in dataframe.columns:
        raise KeyError(
            f"Source column '{source.value}' not found in {get_path(root_directory).name}"
        )

    if target.value in dataframe.columns:
        dataframe[target.value] = dataframe[target.value].fillna(
            dataframe[source.value]
        )
    else:
        dataframe[target.value] = dataframe[source.value]

    save_data(df=dataframe, root_directory=root_directory)

    return int(dataframe[target.value].notna().sum())
