# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""

>>> from techminer2.metrics._compute_trend_metrics import compute_trend_metrics
>>> metrics = compute_trend_metrics(
...     #
...     # DATABASE PARAMS
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),    
... )    
>>> print(metrics.to_markdown())
|   year |   OCC |   cum_OCC |   local_citations |   global_citations |   citable_years |   mean_global_citations |   cum_global_citations |   mean_global_citations_per_year |   mean_local_citations |   cum_local_citations |   mean_local_citations_per_year |
|-------:|------:|----------:|------------------:|-------------------:|----------------:|------------------------:|-----------------------:|---------------------------------:|-----------------------:|----------------------:|--------------------------------:|
|   2015 |     1 |         1 |                 4 |                 76 |               5 |                  76     |                     76 |                            15.2  |              4         |                     4 |                            0.8  |
|   2016 |     7 |         8 |                 4 |                870 |               4 |                 124.286 |                    946 |                            31.07 |              0.571429  |                     8 |                            0.14 |
|   2017 |    10 |        18 |                11 |               1815 |               3 |                 181.5   |                   2761 |                            60.5  |              1.1       |                    19 |                            0.37 |
|   2018 |    17 |        35 |                14 |               3366 |               2 |                 198     |                   6127 |                            99    |              0.823529  |                    33 |                            0.41 |
|   2019 |    15 |        50 |                 1 |               2008 |               1 |                 133.867 |                   8135 |                           133.87 |              0.0666667 |                    34 |                            0.07 |





"""
from .._core.read_filtered_database import read_filtered_database


def compute_trend_metrics(
    #
    # DATABASE PARAMS
    root_dir: str = "./",
    database: str = "main",
    year_filter: tuple = (None, None),
    cited_by_filter: tuple = (None, None),
    **filters,
):
    """Computes global database indicators per year.

    :meta private:
    """

    records = read_filtered_database(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        sort_by=None,
        **filters,
    )

    records = records.assign(OCC=1)

    columns = ["OCC", "year"]

    if "local_citations" in records.columns:
        columns.append("local_citations")
    if "global_citations" in records.columns:
        columns.append("global_citations")
    records = records[columns]

    records["year"] = records["year"].astype(int)
    records = records.groupby("year", as_index=True).sum()
    records = records.sort_index(ascending=True, axis=0)
    records = records.assign(cum_OCC=records.OCC.cumsum())
    records.insert(1, "cum_OCC", records.pop("cum_OCC"))

    current_year = records.index.max()
    records = records.assign(citable_years=current_year - records.index + 1)

    if "global_citations" in records.columns:
        records = records.assign(mean_global_citations=records.global_citations / records.OCC)
        records = records.assign(cum_global_citations=records.global_citations.cumsum())
        records = records.assign(mean_global_citations_per_year=records.mean_global_citations / records.citable_years)
        records.mean_global_citations_per_year = records.mean_global_citations_per_year.round(2)

    if "local_citations" in records.columns:
        records = records.assign(mean_local_citations=records.local_citations / records.OCC)
        records = records.assign(cum_local_citations=records.local_citations.cumsum())
        records = records.assign(mean_local_citations_per_year=records.mean_local_citations / records.citable_years)
        records.mean_local_citations_per_year = records.mean_local_citations_per_year.round(2)

    return records
