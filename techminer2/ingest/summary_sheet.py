# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _ingest.summary_sheet:

Summary Sheet
===============================================================================


>>> from techminer2.ingest import summary_sheet
>>> summary_sheet(
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... ).head()
                 column  number of terms coverage (%)
0              abstract               52         1.0%
1  abstract_nlp_phrases               47         0.9%
2          affiliations               52         1.0%
3                art_no                8        0.15%
4               article               52         1.0%

"""
import pandas as pd

from .._read_records import read_records


def summary_sheet(
    #
    # DATABASE PARAMS:
    root_dir: str = "./",
    database: str = "main",
    year_filter: tuple = (None, None),
    cited_by_filter: tuple = (None, None),
    **filters,
):
    """Returns an coverage report of the dataset.

    :meta private:
    """

    records = read_records(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    columns = sorted(records.columns)
    n_documents = len(records)

    report = pd.DataFrame({"column": columns})

    report["number of terms"] = [n_documents - records[col].isnull().sum() for col in columns]

    report["coverage (%)"] = [
        f"{ (n_documents - records[col].isnull().sum()) / n_documents:5.2}%" for col in columns
    ]

    return report
