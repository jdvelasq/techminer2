# flake8: noqa
# pylint: disable=line-too-long
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=missing-docstring
"""
.. _global_indicators_by_year_table:

Global Indicators by Year Table
===============================================================================



>>> root_dir = "data/regtech/"

>>> import techminer2 as tm2
>>> tm2.global_indicators_by_year_table(root_dir) 
      OCC  cum_OCC  ...  cum_local_citations  mean_local_citations_per_year
year                ...                                                    
2016    1        1  ...                  0.0                           0.00
2017    4        5  ...                  3.0                           0.11
2018    3        8  ...                 33.0                           1.67
2019    6       14  ...                 52.0                           0.63
2020   14       28  ...                 81.0                           0.52
2021   10       38  ...                 90.0                           0.30
2022   12       50  ...                 93.0                           0.12
2023    2       52  ...                 93.0                           0.00
<BLANKLINE>
[8 rows x 11 columns]


>>> tm2.global_indicators_by_year_table(
...     root_dir=root_dir, database="references"
... ).tail()
      OCC  cum_OCC  ...  cum_local_citations  mean_local_citations_per_year
year                ...                                                    
2018   89      594  ...                729.0                           0.30
2019   91      685  ...                837.0                           0.30
2020  114      799  ...                982.0                           0.42
2021   80      879  ...               1067.0                           0.53
2022   30      909  ...               1099.0                           1.07
<BLANKLINE>
[5 rows x 11 columns]


>>> tm2.global_indicators_by_year_table(
...     root_dir=root_dir, database="cited_by"
... ).tail() 
      OCC  cum_OCC  ...  cum_global_citations  mean_global_citations_per_year
year                ...                                                      
2019   33       44  ...                  1764                            8.15
2020   76      120  ...                  2879                            3.67
2021  107      227  ...                  3511                            1.97
2022  150      377  ...                  3871                            1.20
2023   10      387  ...                  3871                            0.00
<BLANKLINE>
[5 rows x 7 columns]



>>> from pprint import pprint
>>> pprint(
...     sorted(
...         tm2p.global_indicators_by_year_table(
...             root_dir=root_dir,
...         ).columns.to_list()
...     )
... )
['OCC',
 'citable_years',
 'cum_OCC',
 'cum_global_citations',
 'cum_local_citations',
 'global_citations',
 'local_citations',
 'mean_global_citations',
 'mean_global_citations_per_year',
 'mean_local_citations',
 'mean_local_citations_per_year']



"""
from ..._read_records import read_records


def global_metrics_by_year_table(
    #
    # DATABASE PARAMS
    root_dir: str = "./",
    database: str = "main",
    year_filter: tuple = (None, None),
    cited_by_filter: tuple = (None, None),
    **filters,
):
    """Computes global database indicators per year."""

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
        records = records.assign(
            mean_global_citations=records.global_citations / records.OCC
        )
        records = records.assign(
            cum_global_citations=records.global_citations.cumsum()
        )
        records = records.assign(
            mean_global_citations_per_year=records.mean_global_citations
            / records.citable_years
        )
        records.mean_global_citations_per_year = (
            records.mean_global_citations_per_year.round(2)
        )

    if "local_citations" in records.columns:
        records = records.assign(
            mean_local_citations=records.local_citations / records.OCC
        )
        records = records.assign(
            cum_local_citations=records.local_citations.cumsum()
        )
        records = records.assign(
            mean_local_citations_per_year=records.mean_local_citations
            / records.citable_years
        )
        records.mean_local_citations_per_year = (
            records.mean_local_citations_per_year.round(2)
        )

    return records
