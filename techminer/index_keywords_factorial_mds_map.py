"""
Factorial analysis of index keywords using MDS
===============================================================================


Factorial analysis based on the clustering applyed to the dimensionality reduction 
of the co-occurrence matrix.

Based on the bibliometrix/R/conceptualStructure.R code.


**Algorithm**

1. Compute the co-occurrence matrix
2. Apply the dimensionality reduction (sklearn mainfold learning algorithms).
3. Apply the clustering algorithm (sklearn clustering algorithms).
4. Visualize the results.

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/index_keywords_factorial_mds_map.png"
>>> index_keywords_factorial_mds_map(min_occ=2, n_clusters=4, directory=directory).savefig(file_name)

.. image:: images/index_keywords_factorial_mds_map.png
    :width: 650px
    :align: center

>>> index_keywords_factorial_mds_map(min_occ=2, n_clusters=4, directory=directory, plot=False).head()
                                    Dim-1      Dim-2  Cluster
index_keywords          #d #c                                
fintech                 48 269  16.143702  50.125956        3
financial service       19 347  22.105529   6.559340        1
finance                 18 489   7.862350  19.429127        1
sustainable development 12 93   12.796153   4.013132        1
investment              10 187   6.800274  10.064215        1

"""

from sklearn.cluster import AgglomerativeClustering
from sklearn.manifold import MDS

from .co_occurrence_matrix import co_occurrence_matrix
from .factorial_analysis_manifold import Factorial_analysis_manifold


def index_keywords_factorial_mds_map(
    min_occ=2,
    max_occ=None,
    n_clusters=2,
    top_n=5,
    figsize=(8, 8),
    plot=True,
    random_state=0,
    directory="./",
):
    coc_matrix = co_occurrence_matrix(
        column="index_keywords",
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

    if plot is False:
        return estimator.data()

    return estimator.map(top_n=top_n, figsize=figsize)
