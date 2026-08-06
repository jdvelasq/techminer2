from abc import ABC, abstractmethod

import networkx as nx  # type: ignore
import numpy as np
from sklearn.cluster import (  # type: ignore
    DBSCAN,
    AffinityPropagation,
    AgglomerativeClustering,
    SpectralClustering,
)

from tm2p._intern import ParamsMixin
from tm2p._intern.helpers.assign_clust_num_by_clust_size import (
    assign_cluster_numbers_by_cluster_size,
)
from tm2p._intern.plots.nx import (
    detect_communities,
    nodes_to_clusters,
    remove_selfloop_edges,
)


class BaseUnitToCluster(
    ABC,
    ParamsMixin,
):
    """:meta private:"""

    @abstractmethod
    def get_similarity_matrix(self):
        pass

    def _get_i2c(self):

        matrix = (
            self.get_similarity_matrix()
            .update(**self.params.__dict__)  # type: ignore
            .using_counters(True)
            .run()
        )

        if isinstance(self.params.clustering, (str, dict)):

            nx_graph = nx.from_pandas_adjacency(matrix)
            nx_graph = remove_selfloop_edges(nx_graph)
            nx_graph = detect_communities(self.params, nx_graph)
            i2c = nodes_to_clusters(nx_graph)

            return i2c

        if not isinstance(
            self.params.clustering,
            (
                AgglomerativeClustering,
                DBSCAN,
                SpectralClustering,
                AffinityPropagation,
            ),
        ):
            raise ValueError(
                f"Clustering estimator {self.params.clustering} is not supported."
            )

        _check_valid_association_index(self.params.association_index)

        estimator_name = self.params.clustering.__class__.__name__

        if estimator_name in [
            "AgglomerativeClustering",
            "DBSCAN",
        ]:
            dissimilarity_matrix = 1.0 - matrix
            np.fill_diagonal(dissimilarity_matrix.values, 0.0)
            self.params.clustering.fit(dissimilarity_matrix)  # type: ignore

        elif estimator_name in [
            "SpectralClustering",
            "AffinityPropagation",
        ]:

            self.params.clustering.fit(matrix)  # type: ignore

        else:

            raise ValueError(
                f"Clustering estimator {estimator_name} is not supported. Valid options are: "
                "AgglomerativeClustering, DBSCAN, SpectralClustering, AffinityPropagation"
            )

        clusters = self.params.clustering.labels_  # type: ignore

        i2c = dict(zip(matrix.index.tolist(), clusters.tolist()))

        return i2c

    def run(self):

        i2c = self._get_i2c()
        c2i = assign_cluster_numbers_by_cluster_size(
            items=list(i2c.keys()),
            clusters=list(i2c.values()),
        )
        i2c = {item: cluster for cluster, items in c2i.items() for item in items}

        if self.params.use_counters is False:
            i2c = {
                " ".join(item.split(" ")[:-1]): cluster for item, cluster in i2c.items()
            }

        return i2c


def _check_valid_association_index(association_index: str):

    valid_indices = [
        "JACCARD",
        "DICE",
        "SALTON",
        "EQUIVALENCE",
        "INCLUSION",
    ]

    if association_index not in valid_indices:
        raise ValueError(
            f"This association index is not supported for clustering. Valid options are: {', '.join(valid_indices)}"
        )
