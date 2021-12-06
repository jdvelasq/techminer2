"""
Factorial analysis of author keywords using MDS
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
>>> file_name = "/workspaces/techminer-api/sphinx/images/author_keywords_factorial_mds_map.png"
>>> author_keywords_factorial_mds_map(min_occ=2, n_clusters=4, directory=directory).savefig(file_name)

.. image:: images/author_keywords_factorial_mds_map.png
    :width: 650px
    :align: center

>>> author_keywords_factorial_mds_map(min_occ=2, n_clusters=4, directory=directory, plot=False).head()
                                      Dim-1      Dim-2  Cluster
author_keywords        #d  #c                                  
fintech                139 1285 -140.731033 -10.443134        3
financial technologies 28  225   -30.071916   0.960073        1
financial inclusion    17  339    -9.693089 -19.124404        1
blockchain             17  149   -15.865792 -13.315312        1
innovation             13  249   -12.162853   9.074538        0

"""

import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from sklearn.manifold import MDS

from .co_occurrence_matrix import co_occurrence_matrix
from .factorial_analysis_manifold import Factorial_analysis_manifold


def author_keywords_factorial_mds_map(
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
        column="author_keywords",
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
