"""
Annual Indicators (!)
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> annual_indicators(directory)
          num_documents  ...  mean_local_citations_per_year
pub_year                 ...                               
2016                  5  ...                           0.97
2017                 10  ...                           0.96
2018                 34  ...                           0.93
2019                 38  ...                           0.97
2020                 62  ...                           0.50
2021                 99  ...                           0.20
<BLANKLINE>
[6 rows x 11 columns]

>>> from pprint import pprint
>>> pprint(annual_indicators(directory).columns.to_list())
['num_documents',
 'local_citations',
 'global_citations',
 'mean_global_citations',
 'mean_local_citations',
 'cum_num_documents',
 'cum_global_citations',
 'cum_local_citations',
 'citable_years',
 'mean_global_citations_per_year',
 'mean_local_citations_per_year']

"""

from ._read_records import read_filtered_records


def annual_indicators(directory="./"):

    records = read_filtered_records(directory)
    records = records.assign(num_documents=1)
    records = records[
        [
            "pub_year",
            "num_documents",
            "local_citations",
            "global_citations",
        ]
    ].copy()
    records = records.groupby("pub_year", as_index=True).sum()
    records = records.sort_index(ascending=True, axis="index")
    records = records.assign(
        mean_global_citations=records.global_citations / records.num_documents
    )
    records = records.assign(
        mean_local_citations=records.local_citations / records.num_documents
    )
    records = records.assign(cum_num_documents=records.num_documents.cumsum())
    records = records.assign(cum_global_citations=records.global_citations.cumsum())
    records = records.assign(cum_local_citations=records.local_citations.cumsum())
    current_year = records.index.max()
    records = records.assign(citable_years=current_year - records.index + 1)
    records = records.assign(
        mean_global_citations_per_year=records.mean_global_citations
        / records.citable_years
    )
    records.mean_global_citations_per_year = (
        records.mean_global_citations_per_year.round(2)
    )
    records = records.assign(
        mean_local_citations_per_year=records.mean_local_citations
        / records.citable_years
    )
    records.mean_local_citations_per_year = records.mean_local_citations_per_year.round(
        2
    )

    return records
