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

>>> from techminer2.pkgs.networks.citation.sources import NodeDegreeDataFrame
>>> (
...     NodeDegreeDataFrame()
...     #
...     # UNIT OF ANALYSIS:
...     .having_terms_in_top(30)
...     .having_citation_threshold(0)
...     .having_occurrence_threshold(2)
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
   Node                                             Name  Degree
0     0                                   Symmetry 1:176       7
1     1  Journal of Management Information Systems 2:696       5
2     2               Sustainability (Switzerland) 2:150       5
3     3                         Electronic Markets 2:287       4
4     4          Journal of Economics and Business 3:422       4


"""

from .....internals.mixins import ParamsMixin
from ..internals.from_others.node_degree_data_frame import (
    NodeDegreeDataFrame as OtherNodeDegreeDataFrame,
)


class NodeDegreeDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):
        return (
            OtherNodeDegreeDataFrame()
            .update_params(**self.params.__dict__)
            .unit_of_analysis("source_title")
            .build()
        )
