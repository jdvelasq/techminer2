"""
SVD of the TF Matrix
===============================================================================

Plots the SVD of the TF-IDF matrix (0/1 values).

The plot is based on the SVD technique used in T-LAB's comparative analysis.

**Algorithm**

1. Transpose the TF matrix

2. Apply SVD to the transposed matrix. T-LAB uses `n_components=20`. 

3. Plot the decomposed matrix as a map.



>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/tlab__singular_value_decomposition__svd__tf_matrix.html"

>>> from techminer2 import tlab
>>> svd = tlab.singular_value_decomposition.svd__tf_matrix(
...     criterion='author_keywords',
...     topic_min_occ=3,
...     directory=directory,
... )

>>> svd.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/tlab__singular_value_decomposition__svd__tf_matrix.html" height="800px" width="100%" frameBorder="0"></iframe>



>>> svd.table_.head()
                                  dim0      dim1  ...     dim11     dim12
author_keywords                                   ...                    
regtech 28:329                5.110503 -0.826361  ...  0.024196 -0.002287
fintech 12:249                2.750827  0.355165  ...  0.106912  0.007621
regulatory technology 07:037  0.568663  2.201471  ...  0.025344 -0.114681
compliance 07:030             1.406428  0.046633  ... -0.026871 -0.002102
regulation 05:164             1.076132  0.856966  ... -0.030314 -0.326806
<BLANKLINE>
[5 rows x 13 columns]

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


def svd__tf_matrix(
    criterion,
    topics_length=None,
    topic_min_occ=None,
    topic_min_citations=None,
    custom_topics=None,
    dim_x=0,
    dim_y=1,
    svd__n_iter=5,
    svd__random_state=0,
    delta=1,
    scheme=None,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):

    matrix = vantagepoint.analyze.tfidf.tf_matrix(
        criterion=criterion,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_min_citations=topic_min_citations,
        custom_topics=custom_topics,
        scheme=scheme,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    ).transpose()

    max_dimensions = min(20, len(matrix.columns) - 1, len(matrix.index))

    decomposed_matrix = TruncatedSVD(
        n_components=max_dimensions,
        n_iter=svd__n_iter,
        random_state=svd__random_state,
    ).fit_transform(matrix)

    labels = matrix.index

    decomposed_matrix = pd.DataFrame(
        decomposed_matrix,
        columns=[f"dim{dim}" for dim in range(max_dimensions)],
        index=labels,
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
