"""
Topic Associations Table
===============================================================================


>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/images/topic_associations.png"
>>> topic_associations_table(
...     'fintech', 
...     'author_keywords', 
...     directory=directory,
... ).savefig(file_name)

.. image:: images/topic_associations.png
    :width: 700px
    :align: center

"""
import pandas as pd

from .co_occurrence_matrix import co_occurrence_matrix


def topic_associations_table(
    item,
    column,
    top_n=10,
    min_occ=1,
    normalization=None,
    directory="./",
):

    coc_matrix = co_occurrence_matrix(
        column,
        min_occ=min_occ,
        normalization=normalization,
        directory=directory,
    )

    coc_matrix.columns = coc_matrix.columns.get_level_values(0)
    coc_matrix.index = coc_matrix.index.get_level_values(0)

    series = coc_matrix[item]
    series = series.map(lambda x: pd.NA if x == 0 else x)
    series = series.dropna()
    series = series[series.index != item]
    series = series.astype(int)
    series = series.to_frame()
    series = series.reset_index()
    series = series.sort_values(by=[item, column], ascending=[False, True])
    series = series.set_index(column)
    series = series[item]

    if top_n is not None:
        series = series.head(top_n)

    return _cleveland_chart(
        series,
        figsize=figsize,
        color=color,
        title="'" + item + "' associations",
        xlabel=xlabel,
        ylabel="Words",
    )
