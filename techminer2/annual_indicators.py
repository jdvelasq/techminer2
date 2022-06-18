"""
Annual Indicators
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> annual_indicators(directory)
          num_documents  ...  cum_local_citations
pub_year                 ...                     
2016                  5  ...                   29
2017                 10  ...                   77
2018                 34  ...                  204
2019                 38  ...                  315
2020                 62  ...                  377
2021                 99  ...                  397
<BLANKLINE>
[6 rows x 8 columns]

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

    return records
