# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Record Display
===============================================================================

>>> from techminer2.documents import record_display
>>> documents = record_display(
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
...     sort_by="date_oldest",
... )
>>> len(documents)
50
>>> print(documents[0])
Record-No: 37
AR Mackenzie A., 2015, LONDON BUS SCH REV, V26, P50
AU Mackenzie A.
TC 76
SO London Business School Review
PY 2015
AB how innovators are using TECHNOLOGY to take on the world of FINANCE.  2015
   LONDON_BUSINESS_SCHOOL
** FINTECH_REVOLUTION; LONDON_BUSINESS_SCHOOL
<BLANKLINE>


"""

from .._core.read_filtered_database import read_filtered_database
from ..helpers.helper_records_for_reporting import helper_records_for_reporting


def record_display(
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

    filtered_records = read_filtered_database(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        sort_by=sort_by,
        **filters,
    )

    formated_records = helper_records_for_reporting(
        records=filtered_records,
    )

    return formated_records
