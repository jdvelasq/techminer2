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
0  Fintech and the Remaking of Financial Institut...
1  Northwestern Journal of International Law and ...
2                  European Research Studies Journal
3  KSII Transactions on Internet and Information ...
4          Review of International Political Economy



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
