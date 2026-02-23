"""Terms by Cluster Frame."""

from techminer2._internals import ParamsMixin
from techminer2._internals.nx import (
    internal__cluster_nx_graph,
    internal__extract_communities_to_frame,
)
from techminer2.analyze._networks.co_citation._internals.create_nx_graph import (
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
