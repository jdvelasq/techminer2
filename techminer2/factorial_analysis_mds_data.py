"""
Factorial analysis using MDS and agglomerative clustering / Data
===============================================================================


>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/factorial_analysis_mds_map.png"
>>> factorial_analysis_mds_data(
...     'author_keywords', 
...     min_occ=2, 
...     n_clusters=4, 
...     directory=directory,
... ).head()
                                     Dim-1       Dim-2  Cluster
author_keywords        #d  #c                                  
fintech                139 1285  18.720838  139.915120        3
financial technologies 28  225   22.666187   20.337616        1
financial inclusion    17  339  -14.225525   15.898773        2
block-chain            17  149   -6.146172   19.745569        2
innovating             13  249   14.588923    5.253269        1


"""

from sklearn.cluster import AgglomerativeClustering
from sklearn.manifold import MDS

from .co_occurrence_matrix import co_occurrence_matrix
from .factorial_analysis_manifold import Factorial_analysis_manifold


def factorial_analysis_mds_data(
    column,
    min_occ=2,
    max_occ=None,
    n_clusters=2,
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
    clustering_method = AgglomerativeClustering(n_clusters=n_clusters)

    estimator = Factorial_analysis_manifold(
        matrix=coc_matrix,
        manifold_method=manifold_method,
        clustering_method=clustering_method,
    )

    return estimator.data()
