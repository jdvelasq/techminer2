# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=import-outside-toplevel
"""
Find records
===============================================================================

Extracts documents from the databaase containing the text string specified by
the parameter ``search_for`` in the column specified by the parameter
``field``. This functions allows the use of regular expressions for
searching. The report is saved to the file ``reports/find_records.txt``.


## >>> from techminer2.search import find_records
## >>> root_dir = "data/regtech/"
## >>> find_records(
## ...     #
## ...     # SEARCH PARAMS:
## ...     field='author_keywords',
## ...     search_for='REGTECH',
## ...     case=False,
## ...     flags=0,
## ...     regex=True,
## ...     report_filename="find_records.txt",
## ...     #
## ...     # DATABASE PARAMS:
## ...     root_dir="example/", 
## ...     database="main",
## ...     year_filter=None,
## ...     cited_by_filter=None,
## ... )
--INFO-- The file 'example/reports/find_records.txt' was created.

## >>> find_records(
## ...     #
## ...     # SEARCH PARAMS:
## ...     field='abstract',
## ...     search_for='five-year',
## ...     case=False,
## ...     flags=0,
## ...     regex=True,
## ...     report_filename="find_records.txt",
## ...     #
## ...     # DATABASE PARAMS:
## ...     root_dir="example/", 
## ...     database="main",
## ...     year_filter=None,
## ...     cited_by_filter=None,
## ... )
--INFO-- The file 'example/reports/find_records.txt' was created.

>>> find_records(
...     #
...     # SEARCH PARAMS:
...     field='abstract',
...     search_for='anti',
...     case=False,
...     flags=0,
...     regex=True,
...     report_filename="find_records.txt",
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=None,
...     cited_by_filter=None,
... )
--INFO-- The file 'example/reports/find_records.txt' was created.

"""
from ..internals.read_filtered_database import read_filtered_database
from ..internals.utils.utils_format_report_for_records import (
    _utils_format_report_for_records,
)


def find_records(
    #
    # SEARCH PARAMS:
    field,
    search_for,
    case=False,
    flags=0,
    regex=True,
    report_filename="find_records.txt",
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """:meta private:"""

    def filter_records(criterion, search_for, case, flags, regex, records):
        """Filter records by the specified criteria."""

        records = records.copy()
        contains = records[criterion].str.contains(
            search_for, case=case, flags=flags, regex=regex
        )
        contains = contains.dropna()
        contains = contains[contains]
        records = records.loc[contains.index, :]

        return records

    records = read_filtered_database(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        sort_by=None,
        **filters,
    )

    records = filter_records(field, search_for, case, flags, regex, records)

    _utils_format_report_for_records(
        root_dir=root_dir,
        target_dir="",
        records=records,
        report_filename=report_filename,
    )
