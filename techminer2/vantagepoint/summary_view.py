# flake8: noqa
"""
Summary View
===============================================================================

This function returns a dataframe with the coverage (percentage of no nulls)
and the number of different terms (topics) of each column in the dataset.

>>> root_dir = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> vantagepoint.summary_view(root_dir).head()
           column  number of terms coverage (%)
0        abstract               48        0.92%
1  abstract_words               47         0.9%
2    affiliations               52         1.0%
3          art_no                8        0.15%
4         article               52         1.0%

"""
import pandas as pd

from ..record_utils import read_records


def summary_view(
    root_dir="./",
    database="documents",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """
    Returns an coverage report of the dataset.

    Args:
        root_dir (str, optional): Root directory. Defaults to "./".
        database (str, optional): Database to be used. Defaults to "documents".
        year_filter (tuple, optional): Year database filter. Defaults to None.
        cited_by_filter (tuple, optional): Cited by database filter. Defaults to None.
        **filters (dict, optional): Filters to be applied to the database. Defaults to {}.

    Returns:
        pd.DataFrame: Coverage report.

    """

    documents = read_records(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    columns = sorted(documents.columns)
    n_documents = len(documents)

    report = pd.DataFrame({"column": columns})

    report["number of terms"] = [
        n_documents - documents[col].isnull().sum() for col in columns
    ]

    report["coverage (%)"] = [
        f"{ (n_documents - documents[col].isnull().sum()) / n_documents:5.2}%"
        for col in columns
    ]

    return report
