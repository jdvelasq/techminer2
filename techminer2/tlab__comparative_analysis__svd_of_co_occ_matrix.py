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

>>> from techminer2 import tlab__comparative_analysis__svd_of_co_occ_matrix
>>> svd = tlab__comparative_analysis__svd_of_co_occ_matrix(
...     criterion='words',
...     topic_min_occ=4,    
...     topics_length=30,
...     directory=directory,
...     delta=0.4,
... )

>>> svd.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/tlab__svd_of_co_occ_matrix.html" height="800px" width="100%" frameBorder="0"></iframe>


>>> svd.table_.head()
                                     dim0       dim1  ...     dim18     dim19
row                                                   ...                    
regtech 69:461                  96.128479  -5.992499  ... -0.256446  0.634847
fintech 42:406                  70.447064  -6.502379  ... -0.253378 -1.142547
regulatory technology 27:241    34.855736  17.837853  ... -0.170260 -0.245663
financial technology 24:289     37.628786   9.002861  ...  0.429911  0.681598
artificial intelligence 19:071  25.652384  -5.882582  ... -1.169009 -0.405793
<BLANKLINE>
[5 rows x 20 columns]


"""

import pandas as pd
from sklearn.decomposition import TruncatedSVD

from .map_chart import map_chart
from .vantagepoint.analyze.matrix.co_occ_matrix import co_occ_matrix


class _Result:
    def __init__(self):
        self.table_ = None
        self.plot_ = None


def tlab__comparative_analysis__svd_of_co_occ_matrix(
    criterion,
    topics_length=50,
    topic_min_occ=None,
    topic_min_citations=None,
    dim_x=0,
    dim_y=1,
    svd__n_iter=5,
    random_state=0,
    delta=0.2,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Co-occurrence SVD Map."""

    matrix = co_occ_matrix(
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
