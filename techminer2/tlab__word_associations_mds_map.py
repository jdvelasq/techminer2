"""
Word Associations MDS Map
===============================================================================

Plots the SVD of the co-occurrence matrix normalized with the **salton** measure.

The plot is based on the SVD technique used in T-LAB's comparative analysis.

**Algorithm**

1. Computes the  co-occurrence matrix normalized with the **salton** association index.

2. Apply SVD to the co-occurrence matrix with `n_components=2`.

3. Plot the decomposed matrix.



>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/tlab__word_associations_mds_map.html"

>>> from techminer2 import tlab__word_associations_mds_map
>>> mds_map = tlab__word_associations_mds_map(
...     column='author_keywords',
...     min_occ=5,    
...     directory=directory,
... )

>>> mds_map.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/tlab__word_associations_mds_map.html" height="800px" width="100%" frameBorder="0"></iframe>


>>> mds_map.table_.head()
                                     dim0       dim1
row                                                 
regtech 70:462                  85.583912   8.166457
fintech 42:406                  60.949638 -11.167665
blockchain 18:109               24.948933  -6.642690
artificial intelligence 13:065  13.776312  -1.005190
compliance 12:020               10.424578  11.346089

"""

import pandas as pd
from sklearn.decomposition import TruncatedSVD

from .map_chart import map_chart
from .vantagepoint__co_occ_matrix import vantagepoint__co_occ_matrix


class _Result:
    def __init__(self):
        self.table_ = None
        self.plot_ = None


def tlab__word_associations_mds_map(
    column,
    top_n=50,
    min_occ=None,
    max_occ=None,
    directory="./",
    svd__n_iter=5,
    random_state=0,
    delta=0.5,
):
    """Co-occurrence SVD Map."""

    matrix = vantagepoint__co_occ_matrix(
        column=column,
        top_n=top_n,
        min_occ=min_occ,
        max_occ=max_occ,
        directory=directory,
        database="documents",
    )

    max_dimensions = 2

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
        dim_x=0,
        dim_y=1,
        delta=delta,
    )

    return result
