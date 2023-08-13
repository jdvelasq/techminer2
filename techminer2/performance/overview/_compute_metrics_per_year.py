# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""

>>> from techminer2.performance.overview._compute_metrics_per_year import compute_metrics_per_year
>>> metrics = compute_metrics_per_year(
...     #
...     # DATABASE PARAMS
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),    
... )    
>>> print(metrics.to_markdown())
|   year |   OCC |   cum_OCC |   local_citations |   global_citations |   citable_years |   mean_global_citations |   cum_global_citations |   mean_global_citations_per_year |   mean_local_citations |   cum_local_citations |   mean_local_citations_per_year |
|-------:|------:|----------:|------------------:|-------------------:|----------------:|------------------------:|-----------------------:|---------------------------------:|-----------------------:|----------------------:|--------------------------------:|
|   2016 |     1 |         1 |                 8 |                 30 |               8 |                30       |                     30 |                             3.75 |                8       |                     8 |                            1    |
|   2017 |     4 |         5 |                19 |                162 |               7 |                40.5     |                    192 |                             5.79 |                4.75    |                    27 |                            0.68 |
|   2018 |     3 |         8 |                30 |                182 |               6 |                60.6667  |                    374 |                            10.11 |               10       |                    57 |                            1.67 |
|   2019 |     6 |        14 |                20 |                 47 |               5 |                 7.83333 |                    421 |                             1.57 |                3.33333 |                    77 |                            0.67 |
|   2020 |    14 |        28 |                23 |                 93 |               4 |                 6.64286 |                    514 |                             1.66 |                1.64286 |                   100 |                            0.41 |
|   2021 |    10 |        38 |                 9 |                 27 |               3 |                 2.7     |                    541 |                             0.9  |                0.9     |                   109 |                            0.3  |
|   2022 |    12 |        50 |                 3 |                 22 |               2 |                 1.83333 |                    563 |                             0.92 |                0.25    |                   112 |                            0.12 |
|   2023 |     2 |        52 |                 0 |                  0 |               1 |                 0       |                    563 |                             0    |                0       |                   112 |                            0    |




>>> print(metrics.T.to_markdown())
|                                |   2016 |   2017 |     2018 |      2019 |      2020 |   2021 |      2022 |   2023 |
|:-------------------------------|-------:|-------:|---------:|----------:|----------:|-------:|----------:|-------:|
| OCC                            |   1    |   4    |   3      |   6       |  14       |   10   |  12       |      2 |
| cum_OCC                        |   1    |   5    |   8      |  14       |  28       |   38   |  50       |     52 |
| local_citations                |   8    |  19    |  30      |  20       |  23       |    9   |   3       |      0 |
| global_citations               |  30    | 162    | 182      |  47       |  93       |   27   |  22       |      0 |
| citable_years                  |   8    |   7    |   6      |   5       |   4       |    3   |   2       |      1 |
| mean_global_citations          |  30    |  40.5  |  60.6667 |   7.83333 |   6.64286 |    2.7 |   1.83333 |      0 |
| cum_global_citations           |  30    | 192    | 374      | 421       | 514       |  541   | 563       |    563 |
| mean_global_citations_per_year |   3.75 |   5.79 |  10.11   |   1.57    |   1.66    |    0.9 |   0.92    |      0 |
| mean_local_citations           |   8    |   4.75 |  10      |   3.33333 |   1.64286 |    0.9 |   0.25    |      0 |
| cum_local_citations            |   8    |  27    |  57      |  77       | 100       |  109   | 112       |    112 |
| mean_local_citations_per_year  |   1    |   0.68 |   1.67   |   0.67    |   0.41    |    0.3 |   0.12    |      0 |


"""
from ..._read_records import read_records


def compute_metrics_per_year(
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

    records = read_records(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
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
        records = records.assign(
            mean_global_citations_per_year=records.mean_global_citations / records.citable_years
        )
        records.mean_global_citations_per_year = records.mean_global_citations_per_year.round(2)

    if "local_citations" in records.columns:
        records = records.assign(mean_local_citations=records.local_citations / records.OCC)
        records = records.assign(cum_local_citations=records.local_citations.cumsum())
        records = records.assign(
            mean_local_citations_per_year=records.mean_local_citations / records.citable_years
        )
        records.mean_local_citations_per_year = records.mean_local_citations_per_year.round(2)

    return records
