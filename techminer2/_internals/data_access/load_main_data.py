"""
Smoke test:
    >>> from techminer2._internals.data_access import load_main_data
    >>> df = load_main_data(root_directory="examples/small/")

    >>> df = load_main_data(
    ...     root_directory="examples/small/",
    ...     usecols=["record_id", "raw_document_title"],
    ... )



"""

from typing import Optional

import pandas as pd

from .get_main_data_path import get_main_data_path


def load_main_data(
    root_directory: str,
    usecols: Optional[list[str]] = None,
) -> pd.DataFrame:

    path = get_main_data_path(root_directory)

    if not path.exists():
        raise AssertionError(f"{path.name} not found")

    try:
        return pd.read_csv(
            path,
            usecols=usecols,
            compression="zip",
            encoding="utf-8",
            low_memory=False,
        )
    except ValueError as err:
        raise AssertionError(f'Columns "{usecols}" not found in {path.name}') from err
