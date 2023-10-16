# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=unused-variable
"""
Query
===============================================================================

>>> from techminer2 import Query
>>> Query(  
...     #
...     # DATABASE PARAMS:
...     root_dir="example",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... ).execute("SELECT source_title FROM database LIMIT 5;")
                                      source_title
0                      Review of Financial Studies
1  International Journal of Information Management
2                             Financial Innovation
3                           China Economic Journal
4                Journal of Economics and Business



"""
import duckdb

from ._read_records import ReadRecordsMixin


class Query(ReadRecordsMixin):
    """Query class."""

    def __init__(
        self,
        #
        # DATABASE PARAMS
        root_dir="./",
        database="main",
        year_filter=(None, None),
        cited_by_filter=(None, None),
        **filters,
    ):
        super().__init__(
            root_dir=root_dir,
            database=database,
            year_filter=year_filter,
            cited_by_filter=cited_by_filter,
            **filters,
        )

    def execute(self, expr):
        """Query."""

        # The variable 'database' is required by duckdb.query(expr).df()
        database = self.read_records()
        return duckdb.query(expr).df()


# def query(
#     expr,
#     #
#     # DATABASE PARAMS:
#     root_dir="./",
#     database="main",
#     year_filter=(None, None),
#     cited_by_filter=(None, None),
#     **filters,
# ):
#     """:meta private:"""

#     database = read_records(
#         #
#         # DATABASE PARAMS:
#         root_dir=root_dir,
#         database=database,
#         year_filter=year_filter,
#         cited_by_filter=cited_by_filter,
#         **filters,
#     )

#     return duckdb.query(expr).df()
