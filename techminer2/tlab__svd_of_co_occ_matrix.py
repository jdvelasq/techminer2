"""
SVD of the Co-occurrence Matrix
===============================================================================

Plots the SVD of the co-occurrence matrix normalized with the **salton** measure.

The plot is based on the SVD technique used in T-LAB's comparative analysis.

**Algorithm**

1. Computes the  co-occurrence matrix normalized with the **salton** association index.

2. Apply SVD to the co-occurrence matrix with `n_components=20`.

3. Plot the decomposed matrix.



>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/tlab__svd_of_co_occ_matrix.html"

>>> from techminer2 import tlab__svd_of_co_occ_matrix
>>> svd = tlab__svd_of_co_occ_matrix(
...     criterion='author_keywords',
...     topic_min_occ=5,    
...     directory=directory,
... )

>>> svd.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/tlab__svd_of_co_occ_matrix.html" height="800px" width="100%" frameBorder="0"></iframe>


>>> svd.table_.head()
                                     dim0      dim1  ...      dim9     dim10
row                                                  ...                    
regtech 69:461                  84.928900 -2.721688  ...  0.099540 -0.399477
fintech 42:406                  61.832611  2.278441  ... -0.384420  0.069563
blockchain 18:109               25.915631 -4.905159  ...  0.121866 -0.188590
artificial intelligence 13:065  15.160618  6.382477  ...  0.865626 -0.858157
compliance 12:020               13.045184 -5.500958  ... -0.142193  0.747093
<BLANKLINE>
[5 rows x 11 columns]

"""

import pandas as pd
from sklearn.decomposition import TruncatedSVD

from .map_chart import map_chart
from .vantagepoint__co_occ_matrix import vantagepoint__co_occ_matrix


class _Result:
    def __init__(self):
        self.table_ = None
        self.plot_ = None


def tlab__svd_of_co_occ_matrix(
    criterion,
    topics_length=50,
    topic_min_occ=None,
    topic_min_citations=None,
    dim_x=0,
    dim_y=1,
    svd__n_iter=5,
    random_state=0,
    delta=0.5,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Co-occurrence SVD Map."""

    matrix = vantagepoint__co_occ_matrix(
        criterion=criterion,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_min_citations=topic_min_citations,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
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
