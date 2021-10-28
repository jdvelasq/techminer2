"""
Coverage
========

    Calculate the coverage of the records.
"""


import pandas as pd
from techminer.data.records import load_records


def coverage(directory_or_records):
    """
    Calculate the coverage of the records.

    Parameters
    ----------
    directory_or_records : str or pandas.DataFrame
        Path to the directory containing the records or a list of records.

    Returns
    -------
    pandas.DataFrame
        DataFrame with the coverage of the records.
    """
    if isinstance(directory_or_records, str):
        records = load_records(directory_or_records)
    else:
        records = directory_or_records.copy()

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
