# flake8: noqa
# pylint: disable=line-too-long
"""
Network Clustering
===============================================================================

Clusters a co-occurrence network using community detection algorithm or sklearn algoritmos.

* Community detection algorithms:

    * ``louvain```

    * ``label_propagation``

    * ``walktrap``

* Sklearn algorithms:
    
    They are specified through the ``algorithm_or_estimator`` parameter.


* Preparation

>>> import techminer2 as tm2
>>> from sklearn.cluster import KMeans
>>> root_dir = "data/regtech/"


* Object oriented interface

>>> (
...     tm2p.records(root_dir=root_dir)
...     .co_occurrence_matrix(
...         columns='author_keywords',
...         col_top_n=20,
...     )
...     .network_create(
...         normalization_index='association',
...         algorithm_or_estimator=KMeans(
...             n_clusters=4, 
...             random_state=1,
...         )
...     )
... )
CoocNetwork(cooc-matrix='CoocMatrix(columns='author_keywords',
    rows='author_keywords', dims=(20,  20))', algorithm-or-
    estimator=KMeans(n_clusters=4, random_state=1))

>>> (
...     tm2p.records(root_dir=root_dir)
...     .co_occurrence_matrix(
...         columns='author_keywords',
...         col_top_n=20,
...     )
...     .network_create(
...         normalization_index='association',
...         algorithm_or_estimator='louvain',
...     )
... )
CoocNetwork(cooc-matrix='CoocMatrix(columns='author_keywords',
    rows='author_keywords', dims=(20,  20))', algorithm-or-
    estimator='louvain')

* Functional interface

>>> cooc_matrix = tm2p.co_occurrence_matrix(
...    columns='author_keywords',
...    col_top_n=20,
...    root_dir=root_dir,
... )

>>> network_create(
...     cooc_matrix,
...     normalization_index='association',
...     algorithm_or_estimator='louvain',
... )
CoocNetwork(cooc-matrix='CoocMatrix(columns='author_keywords',
    rows='author_keywords', dims=(20,  20))', algorithm-or-
    estimator='louvain')

>>> network_create(
...     cooc_matrix,
...     normalization_index='association',
...     algorithm_or_estimator=KMeans(
...         n_clusters=4, 
...         random_state=1,
...     ),
... )
CoocNetwork(cooc-matrix='CoocMatrix(columns='author_keywords',
    rows='author_keywords', dims=(20,  20))', algorithm-or-
    estimator=KMeans(n_clusters=4, random_state=1))


"""
import textwrap
from dataclasses import dataclass
from dataclasses import field as datafield

import networkx as nx
import numpy as np
import pandas as pd

# from .._network_lib import (  # nx_apply_community_detection_method,; nx_set_node_color_by_group,
#     nx_create_graph_from_matrix,
#     nx_set_edge_properties_for_co_occ_networks,
# )
# from .create_degree_plot import create_degree_plot

# # from ..vantagepoint.analyze.discover.matrix.matrix_normalization import (
# #     matrix_normalization,
# # )
# from .get_network_communities import get_network_communities
# from .network_metrics import network_metrics
# from .network_report import network_report
# from .network_viewer import network_viewer


# pylint: disable=too-many-instance-attributes
@dataclass
class CoocNetwork:
    """Co-cccurrence Network.

    :meta private:
    """

    #
    # RESULTS:
    nx_graph: nx.Graph
    cooc_matrix: pd.DataFrame
    algorithm_or_estimator: str
    #
    # DATABASE PARAMS:
    root_dir: str = "./"
    database: str = "main"
    year_filter: tuple = (None, None)
    cited_by_filter: tuple = (None, None)
    filters: dict = datafield(default_factory=dict)

    def __repr__(self):
        cooc_matrix_repr = (
            repr(self.cooc_matrix)
            .replace("\n", " ")
            .replace("    ", "   ")
            .replace("   ", "  ")
            .replace("  ", " ")
        )

        text = "CoocNetwork("
        text += f"cooc-matrix='{cooc_matrix_repr}'"
        text += f", algorithm-or-estimator={self.algorithm_or_estimator}"
        text += ")"
        text = textwrap.fill(text, width=75, subsequent_indent="    ")

        return text

    def network_communities(self):
        """Returns the communities of the network.

        :meta private:
        """

        return network_communities(self)

    # pylint: disable=too-many-arguments
    def network_degree_plot(
        self,
        textfont_size=10,
        marker_size=7,
        line_color="black",
        line_width=1.5,
        yshift=4,
    ):
        """Returns the degree plot of the network.

        :meta private:
        """

        return create_degree_plot(
            nx_graph=self,
            textfont_size=textfont_size,
            marker_size=marker_size,
            line_color=line_color,
            line_width=line_width,
            yshift=yshift,
        )

    def network_metrics(
        self,
    ):
        """Returns the degree plot of the network.

        :meta private:
        """

        return network_metrics(
            network=self,
        )

    def network_viewer(
        self,
    ):
        """Returns the degree plot of the network.

        :meta private:
        """

        return network_viewer(
            network=self,
        )

    def network_report(
        self,
        report_dir,
        #
        # CONCORDANCES
        top_n=100,
    ):
        """Returns the degree plot of the network.

        :meta private:
        """

        return network_report(
            network=self,
            report_dir=report_dir,
            #
            # CONCORDANCES
            top_n=top_n,
            #
            # DATABASE PARAMS:
            root_dir=self.root_dir,
            database=self.database,
            year_filter=self.year_filter,
            cited_by_filter=self.cited_by_filter,
            **self.filters,
        )


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def network_create(
    cooc_matrix=None,
    algorithm_or_estimator=None,
    normalization_index=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """Cluster a co-occurrence matrix"""

    cooc_matrix = matrix_normalization(cooc_matrix, normalization_index)

    if isinstance(algorithm_or_estimator, str):
        return cluster_network_with_community_deteccion(
            cooc_matrix,
            algorithm_or_estimator,
            root_dir=root_dir,
            database=database,
            year_filter=year_filter,
            cited_by_filter=cited_by_filter,
            **filters,
        )

    return cluster_network_with_sklearn_estimators(
        cooc_matrix,
        algorithm_or_estimator,
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def cluster_network_with_community_deteccion(
    cooc_matrix,
    algorithm,
    #
    # DATABASE PARAMS:
    root_dir,
    database,
    year_filter,
    cited_by_filter,
    **filters,
):
    """Cluster a co-occurrence matrix

    :meta private:
    """

    graph = nx_create_graph_from_matrix(cooc_matrix)
    graph = nx_apply_community_detection_method(graph, algorithm)
    graph = nx_set_node_color_by_group(graph)
    graph = nx_set_edge_properties_for_co_occ_networks(graph)

    return CoocNetwork(
        nx_graph=graph,
        cooc_matrix=cooc_matrix,
        algorithm_or_estimator=repr(algorithm),
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def cluster_network_with_sklearn_estimators(
    cooc_matrix,
    estimator,
    #
    # DATABASE PARAMS:
    root_dir,
    database,
    year_filter,
    cited_by_filter,
    **filters,
):
    """Cluster the matrix by sklearn cluster methods.

    :meta private:
    """

    # compute the dissimilarity matrix
    values = cooc_matrix.df_.values
    np.fill_diagonal(values, 0)
    dissimilarity_matrix = values / np.abs(values).sum(axis=1, keepdims=True)

    # perform clustering using the specified estimator
    clustering = estimator.fit(dissimilarity_matrix)
    labels = clustering.labels_.tolist()

    # create communities
    n_clusters = len(set(labels))
    communities = {i_cluster: [] for i_cluster in range(n_clusters)}
    for i_label, label in enumerate(labels):
        communities[label].append(i_label)

    lengths = [(key, len(communities[key])) for key in communities.keys()]
    lengths = sorted(lengths, key=lambda x: x[1], reverse=True)

    new_labels = {}
    for new_label, (old_label, _) in enumerate(lengths):
        new_labels[old_label] = new_label

    labels = [new_labels[label] for label in labels]

    # create a graph
    # smatrix_list = list_cells_in_matrix(cooc_matrix)
    graph = nx_create_graph_from_matrix(cooc_matrix)

    columns = cooc_matrix.df_.columns.tolist()
    names2cluster = dict(zip(columns, labels))

    for node in graph.nodes():
        graph.nodes[node]["group"] = names2cluster[node]

    graph = nx_set_node_color_by_group(graph)

    return CoocNetwork(
        nx_graph=graph,
        cooc_matrix=cooc_matrix,
        algorithm_or_estimator=repr(estimator),
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
