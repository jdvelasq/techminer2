# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Network Degree Frame
===============================================================================

>>> from techminer2.pkgs.networks.coupling.countries  import NodeDegreeDataFrame
>>> (
...     NodeDegreeDataFrame()
...     #
...     # UNIT OF ANALYSIS:
...     .having_terms_in_top(20)
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
   Node                    Name  Degree
0     0   United States 16:3189      16
1     1         Germany 07:1814      15
2     2       Australia 05:0783      13
3     3           China 08:1085      13
4     4  United Kingdom 03:0636      12




"""
from .....internals.mixins import ParamsMixin
from ..internals.from_others.node_degree_data_frame import InternalNodeDegreeDataFrame


class NodeDegreeDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):
        return (
            InternalNodeDegreeDataFrame()
            .update_params(**self.params.__dict__)
            .unit_of_analysis("countries")
            .build()
        )
