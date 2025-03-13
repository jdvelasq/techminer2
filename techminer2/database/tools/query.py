# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=unused-variable
# pylint: disable=too-few-public-methods
"""
Query
===============================================================================

Example:
    >>> from techminer2.database.tools import Query
    >>> (
    ...     Query()
    ...     #
    ...     .with_query_expression("SELECT source_title FROM database LIMIT 5;")
    ...     #
    ...     .where_root_directory_is("example/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     #
    ...     .run()
    ... )
                                            source_title
    0  International Journal of Applied Engineering R...
    1                          Telecommunications Policy
    2                             China Economic Journal
    3  Contemporary Studies in Economic and Financial...
    4                              New Political Economy




"""
import duckdb

from ..._internals.mixins import ParamsMixin
from .._internals.io import internal__load_filtered_records_from_database


class Query(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        database = internal__load_filtered_records_from_database(params=self.params)
        return duckdb.query(self.params.query_expression).df()
