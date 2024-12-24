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

>>> from techminer2.prepare.database import Query
>>> (
...     Query()
...     .set_database_params(
...         root_dir="example/",
...         database="main",
...         year_filter=(None, None),
...         cited_by_filter=(None, None),
...     ).build(expr="SELECT source_title FROM database LIMIT 5;")
... )
                                        source_title
0  International Journal of Applied Engineering R...
1                          Telecommunications Policy
2                             China Economic Journal
3  Contemporary Studies in Economic and Financial...
4                              New Political Economy




"""
import duckdb

from ...internals.params.database_params import DatabaseParams, DatabaseParamsMixin
from ...internals.read_filtered_database import read_filtered_database


class Query(
    DatabaseParamsMixin,
):
    """:meta private:"""

    def __init__(self):
        self.database_params = DatabaseParams()

    def build(self, expr):
        database = read_filtered_database(**self.database_params.__dict__)
        return duckdb.query(expr).df()
