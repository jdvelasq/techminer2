"""
Dotted Gantt Chart
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/dotted_gantt_chart.png"
>>> dotted_gantt_chart(
...     column='author_keywords',
...     top_n=20, 
...     directory=directory,
... ).savefig(file_name)

.. image:: images/dotted_gantt_chart.png
    :width: 700px
    :align: center

>>> dotted_gantt_chart(
...     column='author_keywords',
...     top_n=20, 
...     directory=directory,
...     plot=False,
... ).head()
pub_year                2016  2017  2018  2019  2020  2021
author_keywords                                           
fintech                    4     6    16    16    38    59
financial technologies     1     0     6     4     5    12
financial inclusion        0     2     0     2     3    10
blockchain                 0     2     3     4     2     6
innovation                 2     1     3     3     3     1


"""


from ._dotted_gantt_chart import _dotted_gantt_chart
from .annual_occurrence_matrix import annual_occurrence_matrix
from .topic_view import topic_view


def dotted_gantt_chart(
    column,
    metric="num_documents",
    top_n=None,
    min_occ=1,
    max_occ=None,
    sort_values=None,
    sort_index=None,
    directory="./",
    #
    figsize=(6, 6),
    plot=True,
):
    indicators = topic_view(
        column=column,
        metric=metric,
        top_n=top_n,
        min_occ=min_occ,
        max_occ=max_occ,
        sort_values=sort_values,
        sort_index=sort_index,
        directory=directory,
    )

    topics = indicators.index

    production = annual_occurrence_matrix(
        column,
        min_occ=1,
        directory=directory,
    )

    production = production.loc[topics]

    if plot is False:
        return production

    return _dotted_gantt_chart(production, figsize=figsize)
