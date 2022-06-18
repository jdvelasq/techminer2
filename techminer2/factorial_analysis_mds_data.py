"""
Factorial analysis using MDS and agglomerative clustering / Data
===============================================================================


>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/images/factorial_analysis_mds_map.png"
>>> factorial_analysis_mds_data(
...     'author_keywords', 
...     min_occ=2, 
...     n_clusters=4, 
...     directory=directory,
... ).head()
                                      Dim-1      Dim-2  Cluster
author_keywords        #d  #c                                  
fintech                139 1285  119.556140  75.277252        3
financial technologies 28  225    23.641797  18.772177        1
financial inclusion    17  339     2.328290  21.330215        1
blockchain             17  149    20.605851  -4.306540        0
bank                   12  185    10.463677 -13.440231        0


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
