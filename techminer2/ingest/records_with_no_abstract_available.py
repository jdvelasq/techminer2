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




"""
from .._read_records import read_records


def records_with_no_abstract_available(
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """
    :meta private:
    """

    records = read_records(
        root_dir=root_dir,
        database="main",
        year_filter=(None, None),
        cited_by_filter=(None, None),
    )

    records = records[
        records.abstract.isna() | (records.abstract == "[no abstract available]")
    ]

    for _, record in records.iterrows():
        print(record.title)
        print(record.article)
        print(record.abstract)
        print()
