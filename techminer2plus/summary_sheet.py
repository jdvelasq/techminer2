# flake8: noqa
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
"""Summary sheet."""
import pandas as pd


def summary_sheet(records):
    """Returns an coverage report of the dataset."""

    columns = sorted(records.columns)
    n_documents = len(records)

    report = pd.DataFrame({"column": columns})

    report["number of terms"] = [
        n_documents - records[col].isnull().sum() for col in columns
    ]

    report["coverage (%)"] = [
        f"{ (n_documents - records[col].isnull().sum()) / n_documents:5.2}%"
        for col in columns
    ]

    return report
