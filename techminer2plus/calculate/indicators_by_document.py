# flake8: noqa
"""
Indicators by Document 
===============================================================================


>>> root_dir = "data/regtech/"

>>> import techminer2plus
>>> techminer2plus.calculate.indicators_by_document(
...     root_dir=root_dir,
... ).head()
                                                    year  ...                                 doi
article                                                   ...                                    
Anagnostopoulos I, 2018, J ECON BUS, V100, P7       2018  ...      10.1016/J.JECONBUS.2018.07.003
Arner DW, 2017, HANDBBLOCKCHAIN, DIGIT FINANC, ...  2017  ...  10.1016/B978-0-12-810441-5.00016-6
Arner DW, 2017, NORTHWEST J INTL LAW BUS, V37, ...  2017  ...                                 NaN
Battanta L, 2020, PROC EUR CONF INNOV ENTREPREN...  2020  ...                 10.34190/EIE.20.143
Baxter LG, 2016, DUKE LAW J, V66, P567              2016  ...                                 NaN
<BLANKLINE>
[5 rows x 6 columns]


>>> from pprint import pprint
>>> pprint(techminer2plus.calculate.indicators_by_document(
...     root_dir=root_dir).columns.to_list())
['year',
 'global_citations',
 'local_citations',
 'global_citations_per_year',
 'local_citations_per_year',
 'doi']

# pylint: disable=line-too-long
"""

from ..records import read_records


def indicators_by_document(
    root_dir="./",
    database="main",
    # Database filters:
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Document indicators"""

    records = read_records(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    max_year = records.year.dropna().max()

    records = records.assign(
        global_citations_per_year=records.global_citations
        / (max_year - records.year + 1)
    )
    records = records.assign(
        global_citations_per_year=records.global_citations_per_year.round(3)
    )

    records = records.assign(
        local_citations_per_year=records.local_citations
        / (max_year - records.year + 1)
    )
    records = records.assign(
        local_citations_per_year=records.local_citations_per_year.round(3)
    )

    records["global_citations"] = records.global_citations.map(
        int, na_action="ignore"
    )

    records = records.set_index("article")
    records = records.sort_index(axis="index", ascending=True)

    records = records[
        [
            "year",
            "global_citations",
            "local_citations",
            "global_citations_per_year",
            "local_citations_per_year",
            "doi",
        ]
    ]

    return records
