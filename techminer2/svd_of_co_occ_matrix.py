"""
SVD of Co-occurrence Matrix
===============================================================================

Plots the SVD of the co-occurrence matrix normalized with the **salton** measure.

The plot is based on the SVD technique used in T-LAB's comparative analysis.

**Algorithm**

1. Computes the  co-occurrence matrix normalized with the **salton** association index.

2. Apply SVD to the co-occurrence matrix with `n_components=20`.

3. Plot the decomposed matrix.


>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/svd_of_co_occ_matrix.html"

>>> svd = svd_of_co_occ_matrix(
...     column='author_keywords',
...     min_occ=5,    
...     directory=directory,
... )

>>> svd.plot_.write_html(file_name)

.. raw:: html

    <iframe src="_static/svd_of_co_occ_matrix.html" height="800px" width="100%" frameBorder="0"></iframe>


>>> svd.table_.head()
                                     dim0       dim1  ...      dim9     dim10
row                                                   ...                    
regtech 70:462                  85.583912   8.166457  ...  0.206008  0.208199
fintech 42:406                  60.949638 -11.167665  ... -0.233467 -0.998573
blockchain 18:109               24.948933  -6.642690  ... -0.017336  0.676491
artificial intelligence 13:065  13.776312  -1.005190  ... -0.022696  0.566117
compliance 12:020               10.424578  11.346089  ... -0.330724 -0.264842
<BLANKLINE>
[5 rows x 11 columns]

"""

import pandas as pd
from sklearn.decomposition import TruncatedSVD

from .co_occ_matrix import co_occ_matrix
from .map_chart import map_chart


class _Result:
    def __init__(self):
        self.table_ = None
        self.plot_ = None


def svd_of_co_occ_matrix(
    column,
    top_n=50,
    min_occ=None,
    max_occ=None,
    dim_x=0,
    dim_y=1,
    directory="./",
    svd__n_iter=5,
    random_state=0,
    delta=0.5,
):
    """Co-occurrence SVD Map."""

    matrix = co_occ_matrix(
        column=column,
        top_n=top_n,
        min_occ=min_occ,
        max_occ=max_occ,
        directory=directory,
        database="documents",
    )

    max_dimensions = min(20, len(matrix.columns) - 1)

    decomposed_matrix = TruncatedSVD(
        n_components=max_dimensions,
        n_iter=svd__n_iter,
        random_state=random_state,
    ).fit_transform(matrix)

    decomposed_matrix = pd.DataFrame(
        decomposed_matrix,
        columns=[f"dim{dim}" for dim in range(max_dimensions)],
        index=matrix.index,
    )

    result = _Result()
    result.table_ = decomposed_matrix
    result.plot_ = map_chart(
        dataframe=decomposed_matrix,
        dim_x=dim_x,
        dim_y=dim_y,
        delta=delta,
    )

    return result
