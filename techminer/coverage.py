"""
Coverage Report
===============================================================================
"""

import pandas as pd

from techminer.utils.io import load_records_from_directory


def _coverage_from_records(records):

    columns = sorted(records.columns)
    n_records = len(records)
    coverage_ = pd.DataFrame(
        {
            "column": columns,
            "number of items": [
                n_records - records[col].isnull().sum() for col in columns
            ],
            "coverage (%)": [
                "{:5.2%}".format((n_records - records[col].isnull().sum()) / n_records)
                for col in columns
            ],
        }
    )

    return coverage_


def _coverage_from_directory(directory):
    return _coverage_from_records(load_records_from_directory(directory))


def coverage(dirpath_or_records):
    """
    Returns an coverage report of the dataset.

    Parameters
    ----------
    dirpath_or_records: str or list
        path to the directory or the records object.

    Returns
    -------
    pandas.DataFrame
        Coverage statistcs
    """
    if isinstance(dirpath_or_records, str):
        return _coverage_from_directory(dirpath_or_records)
    elif isinstance(dirpath_or_records, pd.DataFrame):
        return _coverage_from_records(dirpath_or_records)
    else:
        raise TypeError("dirpath_or_records must be a string or a pandas.DataFrame")
