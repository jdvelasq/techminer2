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

>>> from techminer2.pkgs.networks.coupling.documents  import NodeDegreeDataFrame
>>> (
...     NodeDegreeDataFrame()
...     #
...     # UNIT OF ANALYSIS:
...     .having_terms_in_top(20)
...     .having_citation_threshold(0)
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_range_is(None, None)
...     .where_record_citations_range_is(None, None)
...     .where_records_match(None)
...     #
...     .run()
... ).head()
   Node                                        Name  Degree
0     0  Anagnostopoulos I., 2018, J ECON BUS 1:202       5
1     1                 Hu Z., 2019, SYMMETRY 1:176       5
2     2           Alt R., 2018, ELECTRON MARK 1:150       5
3     3    Gomber P., 2018, J MANAGE INF SYST 1:576       3
4     4     Schueffel P., 2016, J INNOV MANAG 1:226       3


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

    def run(self):

        nx_graph = internal__create_nx_graph(self.params)
        nx_graph = internal__assign_degree_to_nodes(nx_graph)
        node_degrees = internal__collect_node_degrees(nx_graph)
        data_frame = internal__create_node_degrees_data_frame(node_degrees)

        return data_frame
