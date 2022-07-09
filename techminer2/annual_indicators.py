"""
Annual Indicators
===============================================================================

>>> from techminer2 import *
>>> directory = "data/regtech/"

>>> annual_indicators(directory) # doctest: +NORMALIZE_WHITESPACE
   year  cum_OCC  ...  cum_local_citations  mean_local_citations_per_year
0  2016        2  ...                    5                           -0.0
1  2017        7  ...                   12                           -0.0
2  2018       23  ...                   44                           -0.0
3  2019       37  ...                   57                           -0.0
4  2020       62  ...                   73                           -0.0
5  2021       84  ...                   76                           -0.0
6  2022       94  ...                   76                           -0.0
<BLANKLINE>
[7 rows x 12 columns]


>>> annual_indicators(directory, database="references").tail() # doctest: +NORMALIZE_WHITESPACE
    year  cum_OCC  ...  cum_local_citations  mean_local_citations_per_year
43  2018      885  ...                  823                           -0.0
44  2019     1025  ...                  950                           -0.0
45  2020     1171  ...                 1073                           -0.0
46  2021     1211  ...                 1103                           -0.0
47  2022     1214  ...                 1104                           -0.0
<BLANKLINE>
[5 rows x 12 columns]

>>> annual_indicators(directory, database="cited_by").tail() # doctest: +NORMALIZE_WHITESPACE
   year  cum_OCC  ...  cum_global_citations  mean_global_citations_per_year
1  2018       14  ...                   385                           -0.02
2  2019       66  ...                  1677                           -0.01
3  2020      171  ...                  2516                           -0.00
4  2021      355  ...                  3113                           -0.00
5  2022      474  ...                  3198                           -0.00
<BLANKLINE>
[5 rows x 8 columns]

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
 'mean_local_citations_per_year',
 'year']

"""
from ._read_records import read_records


def annual_indicators(
    directory="./",
    database="documents",
):
    """Computes annual indicators,"""

    records = read_records(directory=directory, database=database, use_filter=False)
    records = records.assign(OCC=1)

    columns = ["OCC", "year"]

    if "local_citations" in records.columns:
        columns.append("local_citations")
    if "global_citations" in records.columns:
        columns.append("global_citations")
    records = records[columns]

    records = records.groupby("year", as_index=False).sum()
    records = records.sort_values(by=["year"], ascending=True)
    records = records.reset_index(drop=True)
    records = records.assign(cum_OCC=records.OCC.cumsum())
    records.insert(1, "cum_OCC", records.pop("cum_OCC"))

    current_year = records.index.max()
    records = records.assign(citable_years=current_year - records.year + 1)

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

    return records
