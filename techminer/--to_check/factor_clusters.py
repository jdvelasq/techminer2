"""
Factor Analysis --- clusters
===============================================================================

Factor matrix obtained by appliying PCA to the similarity (co-occurrence) 
matrix.

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/tests/data/"
>>> factor_clusters(co_occurrence_matrix(directory, column='authors', min_occ=6))
(authors           #nd  #tc
 Rabbani MR        10   69     2
 Arner DW          9    135    0
 Wojcik D          7    49     1
 Buckley RP        7    132    0
 Reyes-Mercado P   7    0      1
 Wonglimpiyarat J  6    52     1
 Gozman DP         6    26     1
 Serrano W         6    15     1
 Khan S            6    49     2
 Schwienbacher A   6    50     1
 Ozili PK          6    151    1
 Name: cluster, dtype: int32,
 component                 Factor 0  Factor 1      Factor 2  Factor 3  \
 explained_variance       21.725331 15.188322      4.900000  4.517707    
 explained_variance_ratio  0.355411  0.248470      0.080161  0.073907   
 CLUST_0                   8.046108  4.061942  2.021349e-16  0.081215   
 CLUST_1                  -0.450810 -2.753764 -3.238633e-17 -0.046967   
 CLUST_2                  -6.468272  5.576234  2.266258e-16  0.083168   
 -
 component                     Factor 4      Factor 5  
 explained_variance            3.600000      3.600000   
 explained_variance_ratio      0.058894      0.058894  
 CLUST_0                  -4.125227e-16  2.975000e-16  
 CLUST_1                   2.306957e-16 -2.595327e-16  
 CLUST_2                  -2.394465e-17 -3.556690e-17  )


"""

from ._rows_clustering import rows_clustering


def factor_clusters(
    factors_matrix,
    cluster_estimator=None,
):
    return rows_clustering(
        factors_matrix,
        cluster_estimator=cluster_estimator,
    )
