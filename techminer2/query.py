# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Query
===============================================================================

>>> from techminer2 import query
>>> query(  
...     expr="SELECT source_title FROM database LIMIT 5;",
...     #
...     # DATABASE PARAMS:
...     root_dir="example",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
                                     source_title
0                           Technology in Society
1  Research in International Business and Finance
2                                        Computer
3                            Financial Innovation
4                    Journal of Corporate Finance

"""
import duckdb

from ._common._read_records import read_records


def query(
    expr,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    database = read_records(
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    return duckdb.query(expr).df()
