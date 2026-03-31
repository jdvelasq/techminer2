from tm2p._intern import ParamsMixin
from tm2p._intern.nx import compute_network_metrics
from tm2p.synthes.netw.coupl._intern.doc.create_nx_graph import doc_create_nx_graph


class DocNetworkMetrics(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        nx_graph = doc_create_nx_graph(params=self.params)
        return compute_network_metrics(nx_graph=nx_graph)
