from tm2p._intern import ParamsMixin, remove_counters
from tm2p._intern.nx import cluster_nx_graph, extract_communities
from tm2p.portfolio.intellect_struct.coupl_netw._intern.doc_borrar._create_nx_graph import (
    doc_create_nx_graph,
)


class xDocItemsByCluster(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        use_counters = self.params.use_counters
        self.params.use_counters = True
        nx_graph = doc_create_nx_graph(self.params)
        nx_graph = cluster_nx_graph(params=self.params, nx_graph=nx_graph)
        communities = extract_communities(nx_graph)
        if use_counters is False:
            self.params.use_counters = False
            for col in communities.columns:
                communities[col] = communities[col].apply(remove_counters)
        return communities
