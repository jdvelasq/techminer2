"""
Annual Indicators
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> annual_indicators(directory) # doctest: +NORMALIZE_WHITESPACE
      num_documents  ...  mean_local_citations_per_year
year                 ...                               
2016              2  ...                           0.36
2017              5  ...                           0.23
2018             16  ...                           0.40
2019             14  ...                           0.23
2020             25  ...                           0.21
2021             22  ...                           0.07
2022             10  ...                           0.00
<BLANKLINE>
[7 rows x 8 columns]


"""
from ._read_records import read_records


def annual_indicators(directory="./", database="documents"):
    """Computes annual indicators,"""
    records = read_records(directory=directory, database=database, use_filter=False)
    records = records.assign(num_documents=1)
    #
    columns = ["num_documents"]
    if "year" in records.columns:
        columns.append("year")
    if "local_citations" in records.columns:
        columns.append("local_citations")
    if "global_citations" in records.columns:
        columns.append("global_citations")
    records = records[columns]

    #
    records = records.groupby("year", as_index=True).sum()
    records = records.sort_index(ascending=True, axis="index")
    records = records.assign(cum_num_documents=records.num_documents.cumsum())
    current_year = records.index.max()
    records = records.assign(citable_years=current_year - records.index + 1)

    if "global_citataions" in records.columns:
        records = records.assign(
            mean_global_citations=records.global_citations / records.num_documents
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
            mean_local_citations=records.local_citations / records.num_documents
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
