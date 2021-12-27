"""
Co-occurrence Matrix / Topic Associations
===============================================================================


>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/co_occurrence_matrix_topic_associations.png"
>>> co_occurrence_matrix_topic_associations(
...     'fintech', 
...     'author_keywords', 
...     directory=directory,
... ).savefig(file_name)

.. image:: images/co_occurrence_matrix_topic_associations.png
    :width: 700px
    :align: center


>>> co_occurrence_matrix_topic_associations(
...     'fintech', 
...     'author_keywords', 
...     directory=directory,
...     plot=False,
... ).head()
author_keywords
financial inclusion       15
financial technologies    14
block-chain               13
innovating                10
regulating                10
Name: fintech, dtype: int64

"""

import numpy as np

from .visualization_api.cleveland_dot_chart import cleveland_dot_chart
from .co_occurrence_matrix import co_occurrence_matrix


def co_occurrence_matrix_topic_associations(
    item,
    column,
    top_n=10,
    min_occ=1,
    normalization=None,
    directory="./",
    plot=True,
    color="k",
    figsize=(8, 6),
):

    coc_matrix = co_occurrence_matrix(
        column,
        min_occ=min_occ,
        normalization=normalization,
        directory=directory,
    )

    coc_matrix.columns = coc_matrix.columns.get_level_values(0)
    coc_matrix.index = coc_matrix.index.get_level_values(0)

    # -----------------------------------------------------------------------------------
    series = coc_matrix[item]
    series = series.map(lambda x: np.nan if x == 0 else x)
    series = series.dropna()
    series = series[series.index != item]
    series = series.astype(int)
    series = series.to_frame()
    series = series.reset_index()
    series = series.sort_values(by=[item, column], ascending=[False, True])
    series = series.set_index(column)
    series = series[item]
    # -----------------------------------------------------------------------------------

    if plot is False:
        return series

    series = series.head(top_n)

    if normalization is None:
        xlabel = "Occurrences"
    else:
        xlabel = normalization.capitalize()

    return cleveland_dot_chart(
        series,
        figsize=figsize,
        color=color,
        title="'" + item + "' associations",
        xlabel=xlabel,
        ylabel="Words",
    )
