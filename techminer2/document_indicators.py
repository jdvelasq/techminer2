"""
Document Indicators
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> document_indicators(directory=directory).head()



>>> from pprint import pprint
>>> pprint(document_indicators(directory=directory).columns.to_list())
['global_citations',
 'local_citations',
 'global_citations_per_year',
 'local_citations_per_year',
 'doi']

"""

from ._read_records import read_records


def document_indicators(directory="./", database="documents", use_filter=True):

    records = read_records(
        directory=directory, database=database, use_filter=use_filter
    )

    max_year = records.year.dropna().max()

    # -----------------------------------------------------------------------------------
    records = records.assign(
        global_citations_per_year=records.global_citations
        / (max_year - records.year + 1)
    )
    records = records.assign(
        global_citations_per_year=records.global_citations_per_year.round(3)
    )

    # -----------------------------------------------------------------------------------
    records = records.assign(
        local_citations_per_year=records.local_citations / (max_year - records.year + 1)
    )
    records = records.assign(
        local_citations_per_year=records.local_citations_per_year.round(3)
    )

    # -----------------------------------------------------------------------------------
    records["global_citations"] = records.global_citations.map(int, na_action="ignore")

    # -----------------------------------------------------------------------------------
    records = records.set_index("document_id")
    records = records.sort_index(axis="index", ascending=True)

    # -----------------------------------------------------------------------------------
    records = records[
        [
            "global_citations",
            "local_citations",
            "global_citations_per_year",
            "local_citations_per_year",
            "doi",
        ]
    ]

    return records
