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

>>> from techminer2.tools import query
>>> query(  
...     expr="SELECT source_title FROM database LIMIT 5;",
...     database_params = {
...         "root_dir": "example/",
...         "database": "main",
...         "year_filter": (None, None),
...         "cited_by_filter": (None, None),
...     }
... )
                                      source_title
0                      Review of Financial Studies
1  International Journal of Information Management
2                             Financial Innovation
3                           China Economic Journal
4                Journal of Economics and Business



"""
import duckdb

from .._read_records import read_records


def query(
    expr,
    database_params,
):
    """:meta private:"""

    database = read_records(**database_params)
    return duckdb.query(expr).df()
