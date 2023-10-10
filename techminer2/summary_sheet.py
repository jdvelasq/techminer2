# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Summary Sheet
===============================================================================


>>> from techminer2 import summary_sheet
>>> summary_sheet(
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... ).head()
              column  number of terms coverage (%)
0  abbr_source_title               50         1.0%
1           abstract               48        0.96%
2       affiliations               49        0.98%
3             art_no               50         1.0%
4            article               50         1.0%

"""
import pandas as pd

from ._common._read_records import read_records


def summary_sheet(
    #
    # DATABASE PARAMS:
    root_dir: str = "./",
    database: str = "main",
    year_filter: tuple = (None, None),
    cited_by_filter: tuple = (None, None),
    **filters,
):
    """:meta private:"""

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

    report["number of terms"] = [
        n_documents - records[col].isnull().sum() for col in columns
    ]

    report["coverage (%)"] = [
        f"{ (n_documents - records[col].isnull().sum()) / n_documents:5.2}%"
        for col in columns
    ]

    return report
