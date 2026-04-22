import networkx as nx  # type: ignore
import numpy as np
from sklearn.cluster import (  # type: ignore
    DBSCAN,
    AffinityPropagation,
    AgglomerativeClustering,
    SpectralClustering,
)

from tm2p._intern import Params
from tm2p._intern.helpers.assign_cluter_numbers_by_cluster_size import (
    assign_cluster_numbers_by_cluster_size,
)
from tm2p._intern.plots.nx import (
    detect_communities,
    nodes_to_clusters,
    remove_selfloop_edges,
)

from ..direct_matrix import DirectMatrix


def get_i2c(
    params: Params,
) -> dict[str, int]:

    use_counters = params.use_counters

    if isinstance(params.clustering, (str, dict)):
        i2c = _get_i2c_from_network_based_clustering(params)
    elif isinstance(
        params.clustering,
        (
            AgglomerativeClustering,
            DBSCAN,
            SpectralClustering,
            AffinityPropagation,
        ),
    ):
        _check_valid_association_index(params.association_index)
        i2c = _get_i2c_from_matrix_based_clustering(params)
    else:
        raise ValueError(f"Clustering estimator {params.clustering} is not supported.")

    c2i = assign_cluster_numbers_by_cluster_size(
        items=list(i2c.keys()),
        clusters=list(i2c.values()),
    )

    i2c = {item: cluster for cluster, items in c2i.items() for item in items}

    if use_counters is False:

        i2c = {" ".join(item.split(" ")[:-1]): cluster for item, cluster in i2c.items()}

    return i2c


def _get_i2c_from_network_based_clustering(params: Params) -> dict[str, int]:

    matrix = DirectMatrix().update(**params.__dict__).using_counters(True).run()

    nx_graph = nx.from_pandas_adjacency(matrix)
    nx_graph = remove_selfloop_edges(nx_graph)
    nx_graph = detect_communities(params, nx_graph)
    i2c = nodes_to_clusters(nx_graph)

    return i2c


def _get_i2c_from_matrix_based_clustering(params: Params) -> dict[str, int]:

    matrix = DirectMatrix().update(**params.__dict__).using_counters(True).run()
    dissimilarity_matrix = 1.0 - matrix
    np.fill_diagonal(dissimilarity_matrix.values, 0.0)

    estimator_name = params.clustering.__class__.__name__
    if estimator_name in [
        "AgglomerativeClustering",
        "DBSCAN",
    ]:
        params.clustering.fit(dissimilarity_matrix)  # type: ignore

    elif estimator_name in [
        "SpectralClustering",
        "AffinityPropagation",
    ]:

        params.clustering.fit(matrix)  # type: ignore

    else:

        raise ValueError(
            f"Clustering estimator {estimator_name} is not supported. Valid options are: "
            "AgglomerativeClustering, DBSCAN, SpectralClustering, AffinityPropagation"
        )

    clusters = params.clustering.labels_  # type: ignore

    i2c = dict(zip(matrix.index.tolist(), clusters.tolist()))

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
