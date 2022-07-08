"""
Topics Comparison Chart
===============================================================================


>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> file_name = "sphinx/images/topics_comparison_chart.png"
>>> topics_comparison_chart(
...     'fintech', 
...     'block-chain',
...     'author_keywords', 
...     directory=directory,
...     top_n=20,
... ).savefig(file_name)

.. image:: images/topics_comparison_chart.png
    :width: 700px
    :align: center


>>> topics_comparison_chart(
...     'fintech', 
...     'block-chain',
...     'author_keywords', 
...     directory=directory,
...     top_n=20,
...     plot=False,
... ).head()
author_keywords         fintech  block-chain
author_keywords                             
financial technologies       14            2
financial inclusion          15            0
cryptocurrencies              7            6
regulating                   10            1
innovating                   10            0

"""

import numpy as np

from .co_occurrence_matrix import co_occurrence_matrix
from .stacked_bar_chart import stacked_bar_chart


def topics_comparison_chart(
    topic_a,
    topic_b,
    column,
    top_n=10,
    min_occ=1,
    directory="./",
    plot=True,
    figsize=(8, 6),
):

    coc_matrix = co_occurrence_matrix(
        column,
        min_occ=min_occ,
        normalization=None,
        directory=directory,
    )

    coc_matrix.columns = coc_matrix.columns.get_level_values(0)
    coc_matrix.index = coc_matrix.index.get_level_values(0)

    # -----------------------------------------------------------------------------------
    # return "block-chain" in coc_matrix.columns.tolist()
    matrix = coc_matrix[[topic_a, topic_b]].copy()
    matrix = matrix.loc[matrix.sum(axis=1) > 0]
    matrix = matrix[matrix.index != topic_a]
    matrix = matrix[matrix.index != topic_b]
    matrix = matrix.astype(int)

    matrix = matrix.assign(suma=matrix.sum(axis=1))
    matrix = matrix.sort_values(by="suma", ascending=False)
    matrix.drop("suma", axis=1, inplace=True)

    # -----------------------------------------------------------------------------------

    if plot is False:
        return matrix

    matrix = matrix.head(top_n)
    xlabel = "Occurrences"

    return stacked_bar_chart(
        matrix,
        figsize=figsize,
        xlabel=xlabel,
    )
