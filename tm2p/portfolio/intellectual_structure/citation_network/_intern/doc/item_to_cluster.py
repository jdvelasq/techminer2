from tm2p._intern import ParamsMixin
from tm2p._intern.helpers.assign_cluter_numbers_by_cluster_size import (
    assign_cluster_numbers_by_cluster_size,
)
from tm2p._intern.plots.nx import detect_communities, nodes_to_clusters

from .create_nx_graph import doc_create_nx_graph


class DocItemToCluster(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        use_counters = self.params.counters

        if isinstance(self.params.clustering, (str, dict)):
            i2c = self._get_i2c_from_network_based_clustering()

        else:
            raise ValueError(
                f"Clustering estimator {self.params.clustering} is not supported."
            )

        c2i = assign_cluster_numbers_by_cluster_size(
            items=list(i2c.keys()),
            clusters=list(i2c.values()),
        )

        i2c = {item: cluster for cluster, items in c2i.items() for item in items}

        if use_counters is False:

            i2c = {
                " ".join(item.split(" ")[:-1]): cluster for item, cluster in i2c.items()
            }

        return i2c

    def _get_i2c_from_network_based_clustering(self) -> dict[str, int]:

        nx_graph = doc_create_nx_graph(self.params)
        nx_graph = detect_communities(self.params, nx_graph)
        i2c = nodes_to_clusters(nx_graph)

        return i2c
