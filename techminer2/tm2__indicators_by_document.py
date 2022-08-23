"""
Document Indicators
===============================================================================


>>> directory = "data/regtech/"

>>> from techminer2.tm2__indicators_by_document import tm2__indicators_by_document
>>> tm2__indicators_by_document(
...     directory=directory,
... ).head()
                                                    global_citations  ...                                 doi
article                                                               ...                                    
Abi-Lahoud E, 2018, CEUR WORKSHOP PROC, V2044                      0  ...                                 NaN
Anagnostopoulos I, 2018, J ECON BUS, V100, P7                    110  ...      10.1016/J.JECONBUS.2018.07.003
Arner DW, 2017, HANDB OF BLOCKCHAIN, DIGIT FINA...                 7  ...  10.1016/B978-0-12-810441-5.00016-6
Arner DW, 2017, NORTHWEST J INTL LAW BUS, V37, ...               118  ...                                 NaN
Arner DW, 2019, EUR BUS ORG LAW REV, V20, P55                     18  ...          10.1007/S40804-019-00135-1
<BLANKLINE>
[5 rows x 5 columns]


>>> from pprint import pprint
>>> pprint(tm2__indicators_by_document(directory=directory).columns.to_list())
['global_citations',
 'local_citations',
 'global_citations_per_year',
 'local_citations_per_year',
 'doi']

"""

from ._read_records import read_records


def tm2__indicators_by_document(
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Document indicators"""

    records = read_records(
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
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
    records = records.set_index("article")
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
