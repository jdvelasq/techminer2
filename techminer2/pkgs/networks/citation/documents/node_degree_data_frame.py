# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Node Degree Dataframe
===============================================================================

>>> from techminer2.pkgs.networks.citation.documents  import NodeDegreeDataFrame
>>> (
...     NodeDegreeDataFrame()
...     #
...     # UNIT OF ANALYSIS:
...     .having_terms_in_top(30)
...     .having_citation_threshold(0)
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     .where_records_match(None)
...     #
...     .build()
... ).head()
   Node                                               Name  Degree
0     0                   Hu Z., 2019, SYMMETRY, V11 1:176       7
1     1       Gomber P., 2017, J BUS ECON, V87, P537 1:489       4
2     2  Gomber P., 2018, J MANAGE INF SYST, V35, P220 ...       4
3     3       Alt R., 2018, ELECTRON MARK, V28, P235 1:150       4
4     4  Gozman D., 2018, J MANAGE INF SYST, V35, P145 ...       2



"""
from ....._internals.mixins import ParamsMixin
from ....._internals.nx import (
    internal__assign_degree_to_nodes,
    internal__collect_node_degrees,
    internal__create_node_degrees_data_frame,
)
from .._internals.from_documents.create_nx_graph import internal__create_nx_graph


class NodeDegreeDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):

        nx_graph = internal__create_nx_graph(self.params)
        nx_graph = internal__assign_degree_to_nodes(nx_graph)
        node_degrees = internal__collect_node_degrees(nx_graph)
        data_frame = internal__create_node_degrees_data_frame(node_degrees)

        return data_frame
