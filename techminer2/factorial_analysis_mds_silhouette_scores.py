"""
Factorial analysis using MDS and agglomerative clustering / Silhouette scores
===============================================================================


>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/factorial_analysis_mds_silhouette_scores.png"
>>> factorial_analysis_mds_silhouette_scores(
...     'author_keywords', 
...     min_occ=2, 
...     max_n_clusters=8,
...     directory=directory,
... ).savefig(file_name)

.. image:: images/factorial_analysis_mds_silhouette_scores.png
    :width: 700px
    :align: center

"""

from sklearn.cluster import AgglomerativeClustering
from sklearn.manifold import MDS

from .co_occurrence_matrix import co_occurrence_matrix
from .factorial_analysis_manifold import Factorial_analysis_manifold


def factorial_analysis_mds_silhouette_scores(
    column,
    min_occ=2,
    max_occ=None,
    max_n_clusters=8,
    figsize=(8, 8),
    random_state=0,
    directory="./",
):
    coc_matrix = co_occurrence_matrix(
        column=column,
        min_occ=min_occ,
        max_occ=max_occ,
        normalization=None,
        directory=directory,
    )

    manifold_method = MDS(n_components=2, random_state=random_state)
    clustering_method = AgglomerativeClustering()

    estimator = Factorial_analysis_manifold(
        matrix=coc_matrix,
        manifold_method=manifold_method,
        clustering_method=clustering_method,
    )

    return estimator.silhouette_scores_plot(
        max_n_clusters=max_n_clusters, figsize=figsize
    )
