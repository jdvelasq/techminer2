from tm2p._intern import ParamsMixin
from tm2p._intern.nx import compute_node_metrics
from tm2p.portf.intellect_struct.coupl_netw._intern.others_borrar._create_nx_graph import (
    other_create_nx_graph,
)


class xOtherNetworkMetrics(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        nx_graph = other_create_nx_graph(params=self.params)
        return compute_node_metrics(nx_graph=nx_graph)
