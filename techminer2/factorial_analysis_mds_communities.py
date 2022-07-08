"""
Factorial analysis using MDS and agglomerative clustering / Communities
===============================================================================


>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> file_name = "sphinx/images/factorial_analysis_mds_map.png"
>>> factorial_analysis_mds_communities(
...     'author_keywords', 
...     min_occ=2, 
...     n_clusters=4, 
...     directory=directory,
... ).head()
                         CL_00  ...             CL_03
rn                              ...                  
0          blockchain 017:0149  ...  fintech 139:1285
1          innovation 013:0249  ...                  
2                bank 012:0185  ...                  
3   financial service 011:0300  ...                  
4        crowdfunding 008:0116  ...                  
<BLANKLINE>
[5 rows x 4 columns]

"""

from sklearn.cluster import AgglomerativeClustering
from sklearn.manifold import MDS

from .co_occurrence_matrix import co_occurrence_matrix
from .factorial_analysis_manifold import Factorial_analysis_manifold


def factorial_analysis_mds_communities(
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

    return estimator.cluster_members()
