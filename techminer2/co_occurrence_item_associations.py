"""
Co-occurrence Matrix / Item Associations
===============================================================================


>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/co_occurrence_item_associations.png"
>>> co_occurrence_item_associations(
...     'fintech', 
...     'author_keywords', 
...     directory=directory,
... ).savefig(file_name)

.. image:: images/co_occurrence_item_associations.png
    :width: 700px
    :align: center


>>> co_occurrence_item_associations(
...     'fintech', 
...     'author_keywords', 
...     directory=directory,
...     plot=False,
... ).head()
author_keywords
financial inclusion       15
financial technologies    14
blockchain                13
regulation                10
innovation                10
Name: fintech, dtype: int64

"""

import numpy as np

from .cleveland_dot_chart import cleveland_dot_chart
from .co_occurrence_matrix import co_occurrence_matrix


def co_occurrence_item_associations(
    item,
    column,
    top_n=10,
    min_occ=1,
    directory="./",
    plot=True,
    color="k",
    figsize=(8, 6),
):

    coc_matrix = co_occurrence_matrix(
        column,
        min_occ=1,
        normalization=None,
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
    series = series.sort_values(ascending=False)

    # -----------------------------------------------------------------------------------

    if plot is False:
        return series

    series = series.head(top_n)

    return cleveland_dot_chart(
        series,
        figsize=figsize,
        color=color,
        title="'" + item + "' associations",
        xlabel="Occurrences",
        ylabel="Words",
    )
