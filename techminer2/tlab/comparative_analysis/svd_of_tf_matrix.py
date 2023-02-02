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
>>> file_name = "sphinx/_static/tlab__svd_of_tf_matrix.html"

>>> from techminer2 import tlab__comparative_analysis__svd_of_tf_matrix
>>> svd = tlab__comparative_analysis__svd_of_tf_matrix(
...     criterion='author_keywords',
...     topic_min_occ=6,
...     directory=directory,
... )

>>> svd.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/tlab__svd_of_tf_matrix.html" height="800px" width="100%" frameBorder="0"></iframe>



>>> svd.table_.head()
                                    dim0      dim1  ...      dim8      dim9
author_keywords                                     ...                    
regtech 69:461                  8.027279 -0.675318  ...  0.054604 -0.178393
fintech 42:406                  5.832399  0.584421  ... -0.058765  0.034144
blockchain 18:109               2.456070 -1.152906  ... -0.066790 -0.094229
artificial intelligence 13:065  1.444791  1.461649  ...  0.116242 -0.692996
regulatory technology 12:047    0.602569  2.623255  ... -1.191997 -0.215982
<BLANKLINE>
[5 rows x 10 columns]

"""
import pandas as pd
from sklearn.decomposition import TruncatedSVD

from ..._lib.map_chart import map_chart
from ...vantagepoint.analyze.tfidf.tf_matrix import tf_matrix


class _Result:
    def __init__(self):
        self.table_ = None
        self.plot_ = None


def tlab__comparative_analysis__svd_of_tf_matrix(
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

    matrix = tf_matrix(
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

    result = _Result()
    result.table_ = decomposed_matrix
    result.plot_ = map_chart(
        dataframe=decomposed_matrix,
        dim_x=dim_x,
        dim_y=dim_y,
        delta=delta,
    )

    return result
