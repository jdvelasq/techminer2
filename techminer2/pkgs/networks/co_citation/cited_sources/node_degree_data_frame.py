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

>>> from techminer2.pkgs.networks.co_citation.cited_sources import NodeDegreeDataFrame
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
   Node                            Name  Degree
0     0      ELECT COMMER RES APPL 1:32      27
1     1  MIS QUART MANAGE INF SYST 1:47      26
2     2               INF SYST RES 1:18      25
3     3                 MANAGE SCI 1:30      25
4     4                 COMMUN ACM 1:12      25




"""
from .....internals.mixins import InputFunctionsMixin
from ..internals.node_degree_data_frame import (
    NodeDegreeDataFrame as InternalNodeDegreeDataFrame,
)


class NodeDegreeDataFrame(
    InputFunctionsMixin,
):
    """:meta private:"""

    def build(self):
        return (
            InternalNodeDegreeDataFrame()
            .update_params(**self.params.__dict__)
            .unit_of_analysis("cited_sources")
            .build()
        )
