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

>>> from techminer2.database.tools import Query
>>> (
...     Query()
...     .with_query_expression("SELECT source_title FROM database LIMIT 5;")
...     .where_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     .build()
... )
                                        source_title
0  International Journal of Applied Engineering R...
1                          Telecommunications Policy
2                             China Economic Journal
3  Contemporary Studies in Economic and Financial...
4                              New Political Economy




"""
import duckdb

from ...internals.mixins import InputFunctionsMixin
from ..load import DatabaseLoader


class Query(
    InputFunctionsMixin,
):
    """:meta private:"""

    def build(self):
        database = DatabaseLoader().update_params(**self.params.__dict__).build()
        return duckdb.query(self.params.query_expr).df()
