# CODE_REVIEW: 2025-01-27
"""
Assert No Empty Terms
===============================================================================

Smoke test - Various delimiter formats:
    >>> import pandas as pd
    >>> import tempfile
    >>> from pathlib import Path
    >>> from techminer2.scopus._internals.assert_no_empty_terms import assert_no_empty_terms

    >>> with tempfile.TemporaryDirectory() as temp_dir:
    ...     root = str(Path(temp_dir))
    ...     data_dir = Path(root) / "data" / "processed"
    ...     data_dir.mkdir(parents=True)
    ...
    ...     # Case 1: File not found
    ...     try:
    ...         assert_no_empty_terms("keywords", root)
    ...     except AssertionError as e:
    ...         print("main.csv.zip" in str(e))
    ...     True
    ...
    ...     # Case 2: Valid data with standard delimiter "; "
    ...     df_ok = pd.DataFrame({"keywords": ["A; B", "C"]})
    ...     df_ok.to_csv(data_dir / "main.csv.zip", index=False, compression="zip")
    ...     assert_no_empty_terms("keywords", root)
    ...
    ...     # Case 3: Valid data with compact delimiter ";"
    ...     df_ok2 = pd.DataFrame({"keywords": ["A;B;C", "D"]})
    ...     df_ok2.to_csv(data_dir / "main.csv.zip", index=False, compression="zip")
    ...     assert_no_empty_terms("keywords", root)
    ...
    ...     # Case 4: Column not found
    ...     try:
    ...         assert_no_empty_terms("missing", root)
    ...     except AssertionError as e:
    ...         print("Column" in str(e))
    ...     True
    ...
    ...     # Case 5: Empty term with space "A; ;B"
    ...     df_bad1 = pd.DataFrame({"keywords": ["A; ;B"]})
    ...     df_bad1.to_csv(data_dir / "main.csv.zip", index=False, compression="zip")
    ...     try:
    ...         assert_no_empty_terms("keywords", root)
    ...     except AssertionError as e:
    ...         print("Empty term" in str(e))
    ...     True
    ...
    ...     # Case 6: Empty term without space "A;;B"
    ...     df_bad2 = pd.DataFrame({"keywords": ["A;;B"]})
    ...     df_bad2.to_csv(data_dir / "main.csv.zip", index=False, compression="zip")
    ...     try:
    ...         assert_no_empty_terms("keywords", root)
    ...     except AssertionError as e:
    ...         print("Empty term" in str(e))
    ...     True
    ...
    ...     # Case 7: Mixed delimiters "A; B;C"
    ...     df_mixed = pd.DataFrame({"keywords": ["A; B;C"]})
    ...     df_mixed.to_csv(data_dir / "main.csv.zip", index=False, compression="zip")
    ...     assert_no_empty_terms("keywords", root)  # Should pass


"""
from pathlib import Path

import pandas as pd


def assert_no_empty_terms(
    source: str,
    root_directory: str = "./",
) -> None:

    database_file = Path(root_directory) / "data" / "processed" / "main.csv.zip"

    if not database_file.exists():
        raise AssertionError(f"{database_file.name} not found")

    try:
        dataframe = pd.read_csv(
            database_file,
            encoding="utf-8",
            compression="zip",
            low_memory=False,
            usecols=[source],
        )
    except ValueError as err:
        raise AssertionError(f'Column "{source}" not found in main.csv.zip') from err

    series = (
        dataframe[source]
        .dropna()
        .astype(str)
        .str.replace(r"\s*;\s*", ";", regex=True)
        .str.split(";")
        .explode()
        .str.strip()
    )

    if (series == "").any():
        raise AssertionError(f'Empty term found in column "{source}"')
