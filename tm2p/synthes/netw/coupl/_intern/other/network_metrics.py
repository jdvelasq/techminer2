from tm2p._intern import ParamsMixin
from tm2p._intern.nx import compute_network_metrics
from tm2p.synthes.netw.coupl._intern.other.create_nx_graph import other_create_nx_graph


class OtherNetworkMetrics(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        nx_graph = other_create_nx_graph(params=self.params)
        return compute_network_metrics(nx_graph=nx_graph)
