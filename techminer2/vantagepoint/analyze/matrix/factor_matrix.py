"""
Factor Matrix (TODO)
===============================================================================

Factor matrix obtained by appliying PCA to the co-occurrence matrix. 
matrix.

>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> vantagepoint.analyze.matrix.factor_matrix(
...     vantagepoint.analyze.matrix.co_occ_matrix(
...         criterion='authors', 
...         topic_min_occ=2,
...         directory=directory, 
...     )
... )
component                 Factor 0  Factor 1  ...  Factor 4      Factor 5
explained_variance        3.551365  2.201479  ...  0.474565      0.285714
explained_variance_ratio  0.386418  0.239539  ...  0.051637      0.031088
row                                           ...                        
Arner DW 3:185            3.920561  0.600934  ... -0.148250 -3.523138e-17
Buckley RP 3:185          3.920561  0.600934  ... -0.148250 -3.523138e-17
Arman AA 2:000           -0.472960 -0.489055  ...  1.643183  1.414214e+00
Barberis JN 2:161         2.752839  0.324807  ...  0.074600  2.027977e-17
Brennan R 2:014          -1.576144  2.532547  ... -0.147991 -6.807181e-17
Butler T/1 2:041         -0.472960 -0.489055  ...  1.643183 -1.414214e+00
Crane M 2:014            -1.576144  2.532547  ... -0.147991 -6.807181e-17
Grassi L 2:002           -0.641277 -0.885031  ... -0.464342  3.076766e-17
Hamdan A 2:018           -0.817727 -1.641907  ... -0.363928  2.806076e-16
Lanfranchi D 2:002       -0.641277 -0.885031  ... -0.464342  3.076766e-17
Lin W 2:017              -0.641277 -0.885031  ... -0.464342  1.001566e-16
Ryan P 2:014             -1.576144  2.532547  ... -0.147991 -6.807181e-17
Sarea A 2:012            -0.719045 -1.322270  ... -0.035271 -5.733399e-16
Singh C 2:017            -0.641277 -0.885031  ... -0.464342  1.001566e-16
Turki M 2:018            -0.817727 -1.641907  ... -0.363928  2.806076e-16
<BLANKLINE>
[15 rows x 6 columns]



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
