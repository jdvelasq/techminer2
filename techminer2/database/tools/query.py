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
    >>> df = (
    ...     Query()
    ...     #
    ...     .with_query_expression("SELECT source_title FROM database LIMIT 5;")
    ...     #
    ...     .where_root_directory("examples/fintech/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     #
    ...     .run()
    ... )
    >>> df
                                            source_title
    0  International Journal of Applied Engineering R...
    1                          Telecommunications Policy
    2                             China Economic Journal
    3  Contemporary Studies in Economic and Financial...
    4                              New Political Economy

    >>> df = (
    ...     Query()
    ...     #
    ...     .with_query_expression("SELECT raw_descriptors, raw_nouns_and_phrases, raw_keywords FROM database;")
    ...     #
    ...     .where_root_directory("examples/fintech/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     #
    ...     .run()
    ... )
    >>> for i, row in df.iterrows():
    ...     if row["raw_keywords"] is None:
    ...         set_a = set()
    ...     else:
    ...         set_a = set(row["raw_keywords"].split("; "))
    ...     set_b = set(row["raw_nouns_and_phrases"].split("; "))
    ...     set_c = set(row["raw_descriptors"].split("; "))
    ...     assert (set_a | set_b) == set_c, f"Row {i} mismatch: {set_a} + {set_b} != {set_c}"




"""
import duckdb

from techminer2._internals.mixins import ParamsMixin
from techminer2.database._internals.io import (
    internal__load_filtered_records_from_database,
)


class Query(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        database = internal__load_filtered_records_from_database(params=self.params)
        return duckdb.query(self.params.query_expression).df()
