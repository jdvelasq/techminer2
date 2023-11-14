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
from dataclasses import dataclass
from typing import Dict

import duckdb
import pandas as pd

from .records import Records


@dataclass
class Query:
    def __init__(
        self,
        #
        # QUERY:
        expr: str,
        #
        # DATABASE PARAMS:
        root_dir: str = "./",
        database: str = "main",
        year_filter: tuple = (None, None),
        cited_by_filter: tuple = (None, None),
        **filters,
    ):
        #
        # QUERY:
        self._expr = expr

        #
        # DATABASE PARAMS:
        self._root_dir = root_dir
        self._database = database
        self._year_filter = year_filter
        self._cited_by_filter = cited_by_filter
        self._filters = filters

        #
        # RESULTS:
        self.df_: pd.DataFrame = pd.DataFrame()

    def __post_init__(self):
        """:meta private:"""

        # The variable 'database' is required by duckdb.query(expr).df()
        database = Records(
            #
            # DATABASE PARAMS:
            root_dir=self._root_dir,
            database=self._database,
            year_filter=self._year_filter,
            cited_by_filter=self._cited_by_filter,
            **self._filters,
        ).df_

        self.df_ = duckdb.query(self._expr).df()


# class _Query(ReadRecordsMixin):
#     """:meta private:"""

#     def __init__(
#         self,
#         #
#         # DATABASE PARAMS
#         root_dir="./",
#         database="main",
#         year_filter=(None, None),
#         cited_by_filter=(None, None),
#         **filters,
#     ):
#         super().__init__(
#             root_dir=root_dir,
#             database=database,
#             year_filter=year_filter,
#             cited_by_filter=cited_by_filter,
#             **filters,
#         )

#     def execute(self, expr):
#         """:meta private:"""

#         # The variable 'database' is required by duckdb.query(expr).df()
#         database = self.read_records()
#         return duckdb.query(expr).df()


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
