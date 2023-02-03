"""
SVD of the Co-occurrence Matrix
===============================================================================

Plots the SVD of the co-occurrence matrix normalized with the **salton** measure.

The plot is based on the SVD technique used in T-LAB's comparative analysis.

**Algorithm**

1. Computes the co-occurrence matrix normalized with the **salton** association index.

2. Apply SVD to the co-occurrence matrix with `n_components=20`.

3. Plot the decomposed matrix.



>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/tlab__singular_value_decomposition__svd__co_occ_matrix.html"

>>> from techminer2 import tlab
>>> svd = tlab.singular_value_decomposition.svd__co_occ_matrix(
...     criterion='words',
...     topic_min_occ=4,    
...     topics_length=30,
...     directory=directory,
...     delta=0.4,
... )

>>> svd.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/tlab__singular_value_decomposition__svd__co_occ_matrix.html" height="800px" width="100%" frameBorder="0"></iframe>


>>> svd.table_.head()
                                    dim0      dim1  ...     dim18     dim19
row                                                 ...                    
regtech 28:329                 40.984750 -5.825990  ...  0.155973  0.094078
regulatory technology 20:274   29.043701  7.856001  ... -0.043433  0.051670
financial institutions 16:198  20.398775 -3.811445  ... -0.208498  0.258354
regulatory compliance 15:232   24.902161 -2.185884  ... -0.185359 -0.058335
financial regulation 12:395    16.169054  7.859049  ...  0.382016 -0.036938
<BLANKLINE>
[5 rows x 20 columns]


"""

from dataclasses import dataclass

import pandas as pd
from sklearn.decomposition import TruncatedSVD

from ... import vantagepoint
from ..._map_chart import map_chart


@dataclass(init=False)
class _Results:
    plot_: None
    table_: None


def svd__co_occ_matrix(
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

    matrix = vantagepoint.analyze.matrix.co_occ_matrix(
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

    result = _Results()
    result.table_ = decomposed_matrix
    result.plot_ = map_chart(
        dataframe=decomposed_matrix,
        dim_x=dim_x,
        dim_y=dim_y,
        delta=delta,
    )

    return result
