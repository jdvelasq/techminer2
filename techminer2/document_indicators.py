"""
Document Indicators
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> document_indicators(directory=directory).head()
                                                    global_citations  ...                          doi
document_id                                                           ...                             
Abdullah EME et al, 2018, INT J ENG TECHNOL                        8  ...  10.14419/IJET.V7I2.29.13140
Abu Daqar MAM et al, 2020, BANKS BANK SYST                         2  ...   10.21511/BBS.15(3).2020.03
Acar O et al, 2019, PROCEDIA COMPUT SCI                           10  ...  10.1016/J.PROCS.2019.09.138
Ahern D et al, 2021, EUR BUS ORG LAW REV                           0  ...   10.1007/S40804-021-00217-Z
Al Nawayseh MK et al, 2020, J OPEN INNOV: TECHN...                10  ...        10.3390/JOITMC6040153
<BLANKLINE>
[5 rows x 5 columns]


>>> from pprint import pprint
>>> pprint(document_indicators(directory=directory).columns.to_list())
['global_citations',
 'local_citations',
 'global_citations_per_year',
 'local_citations_per_year',
 'doi']

"""

from ._read_records import read_all_records, read_filtered_records


def document_indicators(directory="./", file_name="documents.csv"):

    if file_name == "documents.csv":
        records = read_filtered_records(directory=directory)
    elif file_name == "references.csv":
        records = read_all_records(directory=directory, file_name=file_name)
    else:
        raise ValueError("file_name must be 'documents.csv' or 'references.csv'")

    max_pub_year = records.pub_year.dropna().max()

    # -----------------------------------------------------------------------------------
    records = records.assign(
        global_citations_per_year=records.global_citations
        / (max_pub_year - records.pub_year + 1)
    )
    records = records.assign(
        global_citations_per_year=records.global_citations_per_year.round(3)
    )

    # -----------------------------------------------------------------------------------
    records = records.assign(
        local_citations_per_year=records.local_citations
        / (max_pub_year - records.pub_year + 1)
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
