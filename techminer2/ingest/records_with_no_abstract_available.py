# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Records with No Abstract Available
===============================================================================




>>> from techminer2.ingest import records_with_no_abstract_available
>>> records_with_no_abstract_available(
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
... )
FINTECH
Puschmann T., 2017, BUSIN INFO SYS ENG, V59, P69
nan
<BLANKLINE>
FINTECH and the TRANSFORMATION of the FINANCIAL_INDUSTRY
Alt R., 2018, ELECTRON MARK, V28, P235
nan
<BLANKLINE>



"""
from ..core.read_filtered_database import read_filtered_database


def records_with_no_abstract_available(
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """
    :meta private:
    """

    records = read_filtered_database(
        root_dir=root_dir,
        database="main",
        year_filter=(None, None),
        cited_by_filter=(None, None),
    )

    records = records[
        records.abstract.isna() | (records.abstract == "[no abstract available]")
    ]

    for _, record in records.iterrows():
        print(record.document_title)
        print(record.article)
        print(record.abstract)
        print()
