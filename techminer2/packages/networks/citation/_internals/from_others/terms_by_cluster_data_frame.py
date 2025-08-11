# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Builds a terms by cluster frame from other fields.



"""
from techminer2._internals.mixins import ParamsMixin
from techminer2._internals.nx import (
    internal__cluster_nx_graph,
    internal__extract_communities_to_frame,
)
from techminer2.packages.networks.citation._internals.from_others.create_nx_graph import (
    internal__create_nx_graph,
)


class TermsByClusterDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        nx_graph = internal__create_nx_graph(self.params)
        nx_graph = internal__cluster_nx_graph(self.params, nx_graph)
        return internal__extract_communities_to_frame(self.params, nx_graph)

        nx_graph = internal__create_nx_graph(self.params)
        nx_graph = internal__cluster_nx_graph(self.params, nx_graph)
        return internal__extract_communities_to_frame(self.params, nx_graph)
