"""
Co-occurrence Matrix / Cluster MDS Map
===============================================================================

# >>> from techminer2 import *
# >>> directory = "data/regtech/"
# >>> file_name = "sphinx/images/co_occurrence_matrix_cluster_mds_map.png"
# >>> co_occurrence_matrix_cluster_mds_map(
# ...     'author_keywords',
# ...     min_occ=2, 
# ...     directory=directory,
# ... ).savefig(file_name)

# .. image:: images/co_occurrence_matrix_cluster_mds_map.png
#     :width: 700px
#     :align: center


"""
from sklearn.manifold import MDS

# from .co_occurrence_matrix import co_occurrence_matrix
# from .network import network
# from ._network_map import network_map


def co_occurrence_matrix_cluster_mds_map(
    column,
    min_occ=2,
    max_occ=None,
    normalization=None,
    clustering_method="louvain",
    directory="./",
    color_scheme="clusters",
    figsize=(7, 7),
):

    coc_matrix = co_occurrence_matrix(
        column=column,
        min_occ=min_occ,
        max_occ=max_occ,
        normalization=normalization,
        directory=directory,
    )

    manifold_method = MDS(n_components=2)

    network_ = network(
        matrix=coc_matrix,
        clustering_method=clustering_method,
        manifold_method=manifold_method,
    )

    return network_map(
        network_,
        color_scheme=color_scheme,
        figsize=figsize,
    )
