from tm2p._intern import ParamsMixin
from tm2p._intern.nx import compute_node_metrics
from tm2p.portfolio.intellectual_structure.coupling_network._intern.doc.create_nx_graph import (
    doc_create_nx_graph,
)


class DocNetworkMetrics(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        nx_graph = doc_create_nx_graph(params=self.params)
        return compute_node_metrics(nx_graph=nx_graph)
