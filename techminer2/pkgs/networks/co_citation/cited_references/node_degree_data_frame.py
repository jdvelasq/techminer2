# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Node Degree Frame
===============================================================================

>>> from techminer2.pkgs.networks.co_citation.cited_references import NodeDegreeDataFrame
>>> (
...     NodeDegreeDataFrame()
...     #
...     # UNIT OF ANALYSIS:
...     .having_terms_in_top(30)
...     .having_citation_threshold(0)
...     .having_terms_in(None)
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     .where_records_match(None)
...     #
...     .build()
... ).head()
   Node                                          Name  Degree
0     0                  Lin M., 2013, MANAGE SCI 1:7      16
1     1             Burtch G., 2013, INF SYST RES 1:4      15
2     2      Polasik M., 2015, INT J ELECT COMMER 1:3      15
3     3  Dahlberg T., 2008, ELECT COMMER RES APPL 1:3      14
4     4          Duarte J., 2012, REV FINANC STUD 1:6      12




"""
from ....._internals.mixins import ParamsMixin
from .._internals.node_degree_data_frame import (
    NodeDegreeDataFrame as InternalNodeDegreeDataFrame,
)


class NodeDegreeDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):
        return (
            InternalNodeDegreeDataFrame()
            .update(**self.params.__dict__)
            .unit_of_analysis("cited_references")
            .build()
        )
