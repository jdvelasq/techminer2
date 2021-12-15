"""
Co-occurrence network analysis
===============================================================================

This module is eqivalent to Bibliometrix' Conceptual Structure/Co-occurrence Network.
The following capabilities are available:

1. Clustering the co-occurrence matrix using sklearn algorithms.

2. Plots the network of co-occurrence relationships, using the clusters found.

3. Build a pandas.DataFrame with the cluster members.

4. Compute and visualize the centrality-density map.

5. Apply a manifold technique to visualize the elements of the cluster. Here
   the manifold is restricted to 2D space (`n_components=2`).


>>> from techminer2 import *
>>> from sklearn.manifold import MDS
>>> directory = "/workspaces/techminer-api/data/"
>>> mds = MDS(random_state=12345)
>>> coc_matrix = co_occurrence_matrix(directory, column='author_keywords', min_occ=12)
>>> analyzer = co_occurrence_network_analysis(
...     coc_matrix, 
...     clustering_method='louvain', 
...     manifold_method=mds,
... )

# >>> analyzer.communities().head(5)


>>> file_name = "/workspaces/techminer-api/sphinx/images/co_occurrence_network_analysis_network_map.png"
>>> analyzer.network().savefig(file_name)

.. image:: images/co_occurrence_network_analysis_network_map.png
    :width: 700px
    :align: center

>>> file_name = "/workspaces/techminer-api/sphinx/images/co_occurrence_network_analysis_manifold_map.png"
>>> analyzer.manifold_map().savefig(file_name)

.. image:: images/co_occurrence_network_analysis_manifold_map.png
    :width: 700px
    :align: center

>>> # analyzer.centrality_density_table()


>>> file_name = "/workspaces/techminer-api/sphinx/images/co_occurrence_network_analysis_cen_den_map.png"
>>> analyzer.centrality_density_map().savefig(file_name)

.. image:: images/co_occurrence_network_analysis_cen_den_map.png
    :width: 700px
    :align: center



"""
from techminer2.utils.co_occurrence_analysis import Co_occurrence_analysis

from .networkx import network_clustering

cluster_colors = [
    "tab:blue",
    "tab:orange",
    "tab:green",
    "tab:red",
    "tab:purple",
    "tab:brown",
    "tab:pink",
    "tab:gray",
    "tab:olive",
    "tab:cyan",
    "cornflowerblue",
    "lightsalmon",
    "limegreen",
    "tomato",
    "mediumvioletred",
    "darkgoldenrod",
    "lightcoral",
    "silver",
    "darkkhaki",
    "skyblue",
] * 5


class Co_occurrence_network_analysis(Co_occurrence_analysis):
    def __init__(
        self,
        co_occurrence_matrix,
        clustering_method,
        manifold_method,
        random_state=12345,
    ):
        super().__init__(
            co_occurrence_matrix=co_occurrence_matrix,
            clustering_method=clustering_method,
            manifold_method=manifold_method,
            random_state=random_state,
        )

        # ----< algorithm >----------------------------------------------------
        self._sort_co_occurrence_matrix()
        self._make_nodes()
        self._make_edges()
        #
        self._clustering()
        #
        self.make_manifold_data()
        self._compute_centrality_density()

    def _clustering(self):

        self.nodes_, self.edges_ = network_clustering(
            self.nodes_,
            self.edges_,
            self.clustering_method,
            random_state=self.random_state,
        )

        self.labels_ = self.nodes_["group"].copy()


def co_occurrence_network_analysis(
    co_occurrence_matrix,
    clustering_method,
    manifold_method,
):

    return Co_occurrence_network_analysis(
        co_occurrence_matrix=co_occurrence_matrix,
        clustering_method=clustering_method,
        manifold_method=manifold_method,
    )
