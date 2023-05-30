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

from .. import record_utils


def summary_view(
    root_dir="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """
    Returns an coverage report of the dataset.

    Args:
        root_dir (str, optional): Root directory. Defaults to "./".
        database (str, optional): Database to be used. Defaults to "documents".
        start_year (int, optional): Start year. Defaults to None.
        end_year (int, optional): End year. Defaults to None.
        filters (dict, optional): Filters to be applied to the database.
            Defaults to {}.

    Returns:
        pd.DataFrame: Coverage report.

    """

    documents = record_utils.read_records(
        root_dir=root_dir,
        database=database,
        start_year=start_year,
        end_year=end_year,
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
