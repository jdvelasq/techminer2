"""
Factor Analysis --- matrix
===============================================================================

Factor matrix obtained by appliying PCA to the similarity (co-occurrence) 
matrix.

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/tests/data/"
>>> factor_matrix(co_occurrence_matrix(directory, column='authors', min_occ=6))
component                 Factor 0  Factor 1      Factor 2  Factor 3  \
explained_variance       21.725331 15.188322      4.900000  4.517707    
explained_variance_ratio  0.355411  0.248470      0.080161  0.073907   
authors          #nd #tc                                               
Rabbani MR       10  69  -7.457430  6.816402  4.764260e-16  0.154755   
Arner DW         9   135  8.644183  4.495553  1.743793e-16  0.111311   
Wojcik D         7   49  -0.475153 -2.993645 -4.949747e+00  3.967407   
Buckley RP       7   132  7.448032  3.628330  2.298904e-16  0.051120   
Reyes-Mercado P  7   0   -0.475153 -2.993645  4.949747e+00  3.967407   
Wonglimpiyarat J 6   52  -0.441073 -2.657812 -1.221041e-14 -1.652716   
Gozman DP        6   26  -0.441073 -2.657812 -1.304308e-14 -1.652716   
Serrano W        6   15  -0.441073 -2.657812 -2.486696e-14 -1.652716   
Khan S           6   49  -5.479113  4.336065 -2.317433e-17  0.011582   
Schwienbacher A  6   50  -0.441073 -2.657812 -2.200040e-16 -1.652716   
Ozili PK         6   151 -0.441073 -2.657812  1.271205e-14 -1.652716   
---
component                    Factor  4     Factor  5  
explained_variance            3.600000      3.600000   
explained_variance_ratio      0.058894      0.058894  
authors          #nd #tc                              
Rabbani MR       10  69  -2.394465e-17 -3.556690e-17  
Arner DW         9   135 -4.125227e-16  3.252556e-16  
Wojcik D         7   49   2.252013e-15  6.264949e-15  
Buckley RP       7   132 -4.125227e-16  2.697444e-16  
Reyes-Mercado P  7   0   -2.466435e-15 -6.558127e-15  
Wonglimpiyarat J 6   52   1.753989e+00  4.356088e+00  
Gozman DP        6   26  -2.917738e-01 -1.316149e+00  
Serrano W        6   15  -2.794042e+00 -2.500854e+00  
Khan S           6   49  -2.394465e-17 -3.556690e-17  
Schwienbacher A  6   50   4.140452e+00 -2.378176e+00  
Ozili PK         6   151 -2.808625e+00  1.839091e+00 


"""

import pandas as pd
from sklearn.decomposition import PCA


def factor_matrix(
    similarity_matrix,
    pca=None,
):
    if pca is None:
        pca = PCA(n_components=6)
    pca.fit(similarity_matrix)
    transformed_matrix = pca.transform(similarity_matrix)
    columns = [
        (f"Factor {i_component}", ev, evratio)
        for i_component, (ev, evratio) in enumerate(
            zip(pca.explained_variance_, pca.explained_variance_ratio_)
        )
    ]
    columns = pd.MultiIndex.from_tuples(
        columns, names=["component", "explained_variance", "explained_variance_ratio"]
    )
    matrix = pd.DataFrame(
        transformed_matrix,
        index=similarity_matrix.index,
        columns=columns,
    )
    return matrix
