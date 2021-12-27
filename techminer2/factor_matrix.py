"""
Factor Matrix
===============================================================================

Factor matrix obtained by appliying PCA to the co-occurrence matrix. 
matrix.

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> factor_matrix(
...     co_occurrence_matrix(
...         column='authors', 
...         min_occ=6,
...         directory=directory, 
...     )
... )
 


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
