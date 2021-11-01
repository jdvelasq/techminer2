"""
Summary Report
===============================================================================
"""
import pandas as pd

from techminer.utils.io import load_records


def _summary_from_records(records):
    """
    Returns an overview of the dataset.

    Parameters
    ----------
    records: pandas.DataFrame
        records object.

    Returns
    -------
    pandas.DataFrame
        Summary statistcs
    """

    return summary


def _summary_from_directory(directory):
    return _summary_from_records(load_records(directory))


def summary(directory_or_records):
    """
    Returns an overview of the dataset.

    Parameters
    ----------
    directory_or_records: str or list
        path to the directory or the records object.

    Returns
    -------
    pandas.DataFrame
        Summary statistcs
    """
    if isinstance(directory_or_records, str):
        return _summary_from_directory(directory_or_records)
    elif isinstance(directory_or_records, pd.DataFrame):
        return _summary_from_records(directory_or_records)
    else:
        raise TypeError("directory_or_records must be a string or a pandas.DataFrame")
