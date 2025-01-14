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
...     .set_analysis_params(
...         expr="SELECT source_title FROM database LIMIT 5;",
...     #
...     ).set_database_params(
...         root_dir="example/",
...         database="main",
...         year_filter=(None, None),
...         cited_by_filter=(None, None),
...     ).build()
... )
                                        source_title
0  International Journal of Applied Engineering R...
1                          Telecommunications Policy
2                             China Economic Journal
3  Contemporary Studies in Economic and Financial...
4                              New Political Economy




"""
from dataclasses import dataclass
from typing import Optional

import duckdb

from ...internals.params.database_params import DatabaseParams, DatabaseParamsMixin
from ..load.load__filtered_database import load__filtered_database


@dataclass
class AnalysisParams:
    """:meta private:"""

    expr: Optional[str] = None


class AnalysisParamsMixin:
    """:meta private:"""

    def set_analysis_params(self, **kwars):
        for key, value in kwars.items():
            if hasattr(self.analysis_params, key):
                setattr(self.analysis_params, key, value)
            else:
                raise ValueError(f"Invalid parameter for AnalysisParams: {key}")
        return self


class Query(
    AnalysisParamsMixin,
    DatabaseParamsMixin,
):
    """:meta private:"""

    def __init__(self):
        self.analysis_params = AnalysisParams()
        self.database_params = DatabaseParams()

    def build(self):
        database = load__filtered_database(**self.database_params.__dict__)
        return duckdb.query(self.analysis_params.expr).df()
