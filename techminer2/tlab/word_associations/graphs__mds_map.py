"""
MDS Map
===============================================================================

Plots the SVD of the co-occurrence matrix normalized with the **salton** measure.

The plot is based on the SVD technique used in T-LAB's comparative analysis.

**Algorithm**

1. Computes the  co-occurrence matrix normalized with the **salton** association index.

2. Apply SVD to the co-occurrence matrix with `n_components=2`.

3. Plot the decomposed matrix.



>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/tlab__word_associations__graphs__mds_map.html"

>>> from techminer2 import tlab
>>> mds_map = tlab.word_associations.graphs__mds_map(
...     criterion='author_keywords',
...     topic_min_occ=5,    
...     directory=directory,
...     delta=0.3,
... )

>>> mds_map.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/tlab__word_associations__graphs__mds_map.html" height="800px" width="100%" frameBorder="0"></iframe>


>>> mds_map.table_.head()
                                   dim0      dim1
row                                              
regtech 28:329                31.434517 -2.152565
fintech 12:249                16.709623  5.191047
compliance 07:030              8.672894 -4.116138
regulatory technology 07:037   3.119939 -0.566268
regulation 05:164              6.324591  2.907691

"""

from dataclasses import dataclass

import pandas as pd
from sklearn.decomposition import TruncatedSVD

from ... import vantagepoint
from ..._lib.map_chart import map_chart


@dataclass(init=False)
class _Results:
    plot_: None
    table_: None


def graphs__mds_map(
    criterion,
    topics_length=50,
    topic_min_occ=None,
    topic_min_citations=None,
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

    result = _Results()
    result.table_ = decomposed_matrix
    result.plot_ = map_chart(
        dataframe=decomposed_matrix,
        dim_x=0,
        dim_y=1,
        delta=delta,
    )

    return result
