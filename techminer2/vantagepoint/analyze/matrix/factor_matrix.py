"""
Factor Matrix (TODO)
===============================================================================

Factor matrix obtained by appliying PCA to the co-occurrence matrix. 
matrix.

>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> vantagepoint.analyze.matrix.factor_matrix(
...     vantagepoint.analyze.matrix.co_occurrence_matrix(
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
