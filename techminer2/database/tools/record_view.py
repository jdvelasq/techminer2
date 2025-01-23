# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Retrieve records
=======================================================================================

>>> from techminer2.database.tools import document_view


>>> (
...     RecordRetriever()
...     .with_data_in("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     .sort_records_by("date_oldest") # date_newest, date_oldest, global_cited_by_highest, 
...                                     # global_cited_by_lowest, local_cited_by_highest, 
...                                     # local_cited_by_lowest, first_author_a_to_z, 
...                                     # first_author_z_to_a, source_title_a_to_z, 
...                                     # source_title_z_to_a
...     .build()
... )


>>> documents = document_view(
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
...     sort_by="date_oldest", # date_newest, date_oldest, global_cited_by_highest, 
...                            # global_cited_by_lowest, local_cited_by_highest, 
...                            # local_cited_by_lowest, first_author_a_to_z, 
...                            # first_author_z_to_a, source_title_a_to_z, 
...                            # source_title_z_to_a
... )
>>> len(documents)
50
>>> print(documents[0])
Record-No: 37
AR Mackenzie A., 2015, LONDON BUS SCH REV, V26, P50
TI THE FINTECH REVOLUTION
AU Mackenzie A.
TC 76
SO London Business School Review
PY 2015
AB how innovators are using TECHNOLOGY to take on the world of FINANCE . 2015
   LONDON_BUSINESS_SCHOOL
** FINTECH_REVOLUTION; LONDON_BUSINESS_SCHOOL
<BLANKLINE>


"""

from ...internals.utils.utils_records_for_reporting import _utils_records_for_reporting
from ..load.load__database import load__filtered_database


def select_documents(
    #
    # DATABASE PARAMS
    root_dir: str = "./",
    database: str = "main",
    year_filter: tuple = (None, None),
    cited_by_filter: tuple = (None, None),
    sort_by: str = "date_newest",
    **filters,
):
    """:meta private:"""

    filtered_records = load__filtered_database(
        root_dir=root_dir,
        database=database,
        record_years_range=year_filter,
        record_citations_range=cited_by_filter,
        records_order_by=sort_by,
        **filters,
    )

    formated_records = _utils_records_for_reporting(
        records=filtered_records,
    )

    return formated_records
