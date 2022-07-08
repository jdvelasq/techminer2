"""
Annual Indicators
===============================================================================

>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> annual_indicators(directory) # doctest: +NORMALIZE_WHITESPACE
      OCC  cum_OCC  ...  cum_local_citations  mean_local_citations_per_year
year                ...                                                    
2016    2        2  ...                    5                           0.36
2017    5        7  ...                   12                           0.23
2018   16       23  ...                   44                           0.40
2019   14       37  ...                   57                           0.23
2020   25       62  ...                   73                           0.21
2021   22       84  ...                   76                           0.07
2022   10       94  ...                   76                           0.00
<BLANKLINE>
[7 rows x 11 columns]


>>> annual_indicators(directory, database="references").tail() # doctest: +NORMALIZE_WHITESPACE
      OCC  cum_OCC  ...  cum_local_citations  mean_local_citations_per_year
year                ...                                                    
2018  189      885  ...                  823                           0.22
2019  140     1025  ...                  950                           0.23
2020  146     1171  ...                 1073                           0.28
2021   40     1211  ...                 1103                           0.38
2022    3     1214  ...                 1104                           0.33
<BLANKLINE>
[5 rows x 11 columns]

>>> annual_indicators(directory, database="cited_by").tail() # doctest: +NORMALIZE_WHITESPACE
      OCC  cum_OCC  ...  cum_global_citations  mean_global_citations_per_year
year                ...                                                      
2018   11       14  ...                   385                            6.56
2019   52       66  ...                  1677                            6.21
2020  105      171  ...                  2516                            2.66
2021  184      355  ...                  3113                            1.62
2022  119      474  ...                  3198                            0.71
<BLANKLINE>
[5 rows x 7 columns]

>>> from pprint import pprint
>>> pprint(sorted(annual_indicators(directory=directory).columns.to_list()))
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
from ._read_records import read_records


def annual_indicators(directory="./", database="documents", as_index=True):
    """Computes annual indicators,"""

    records = read_records(directory=directory, database=database, use_filter=False)
    records = records.assign(OCC=1)

    columns = ["OCC", "year"]

    if "local_citations" in records.columns:
        columns.append("local_citations")
    if "global_citations" in records.columns:
        columns.append("global_citations")
    records = records[columns]

    records = records.groupby("year", as_index=True).sum()
    records = records.sort_index(ascending=True, axis="index")
    records = records.assign(cum_OCC=records.OCC.cumsum())
    records.insert(1, "cum_OCC", records.pop("cum_OCC"))

    current_year = records.index.max()
    records = records.assign(citable_years=current_year - records.index + 1)

    if "global_citations" in records.columns:
        records = records.assign(
            mean_global_citations=records.global_citations / records.OCC
        )
        records = records.assign(cum_global_citations=records.global_citations.cumsum())
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
        records = records.assign(cum_local_citations=records.local_citations.cumsum())
        records = records.assign(
            mean_local_citations_per_year=records.mean_local_citations
            / records.citable_years
        )
        records.mean_local_citations_per_year = (
            records.mean_local_citations_per_year.round(2)
        )

    if as_index is False:
        records = records.reset_index()

    return records
