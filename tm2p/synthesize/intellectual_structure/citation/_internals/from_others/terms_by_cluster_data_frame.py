from tm2p._internals import ParamsMixin
from tm2p._internals.nx import (
    internal__cluster_nx_graph,
    internal__extract_communities_to_frame,
)
from tm2p.synthesize.intellectual_structure.citation._internals.from_others.create_nx_graph import (
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
