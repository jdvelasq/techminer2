# flake8: noqa
# pylint: disable=import-outside-toplevel
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Smoke test:
    >>> from techminer2.database._internals.io import internal__write_records_to_database
    >>> internal__write_records_to_database(params, records) # doctest: +SKIP


"""
import pandas as pd

from .get_references_data_path import get_references_data_path


def save_references_data(df: pd.DataFrame, root_directory: str) -> None:

    references_data_path = get_references_data_path(root_directory)

    temp_file = references_data_path.with_suffix(".tmp")
    df.to_csv(
        temp_file,
        sep=",",
        encoding="utf-8",
        index=False,
        compression="zip",
    )
    temp_file.replace(references_data_path)
