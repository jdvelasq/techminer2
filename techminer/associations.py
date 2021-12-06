"""
Associations (co-occurrence analysis)
===============================================================================


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> series, fig =  associations(
...     "Wojcik D", 
...     "authors", 
...     top_n=15, 
...     association=None, 
...     directory=directory,
... )
>>> series
authors
Hoepner AGF    1.0
Knight E       1.0
Clark GL       1.0
Cojoianu TF    1.0
Sohns F        1.0
Pazitka V      1.0
Name: Wojcik D, dtype: float64

>>> file_name = "/workspaces/techminer-api/sphinx/images/associations.png"
>>> fig.savefig(file_name)


.. image:: images/associations.png
    :width: 650px
    :align: center

"""

import matplotlib.pyplot as plt
import numpy as np

import networkx as nx

from .co_occurrence_matrix import co_occurrence_matrix


def associations(
    item,
    column,
    top_n=30,
    association=None,
    directory="./",
    figsize=(6, 6),
    networkx_k=0.2,
    networkx_iterations=30,
):

    coc_matrix = co_occurrence_matrix(
        column, min_occ=1, normalization=association, directory=directory
    )
    coc_matrix.columns = coc_matrix.columns.get_level_values(0)
    coc_matrix.index = coc_matrix.index.get_level_values(0)
    series = coc_matrix[item]
    series = series.map(lambda x: np.nan if x == 0 else x)
    series = series.dropna()
    series = series.head(top_n)
    series = series[series.index != item]

    # -----------------------------------------------------------------------------------

    G = nx.Graph()
    G.add_weighted_edges_from(
        [(item, index, item_) for item_, index in zip(series, series.index)]
    )

    # -----------------------------------------------------------------------------------

    fig = plt.figure(figsize=figsize)
    ax = fig.subplots()

    options = {
        "width": 1,
        "with_labels": True,
        "font_size": 7,
        "font_weight": "regular",
        "alpha": 0.7,
    }

    pos = nx.spring_layout(G, k=networkx_k, iterations=networkx_iterations)

    nx.draw(
        G,
        pos=pos,
        node_size=20,
        **options,
    )
    ax.collections[0].set_edgecolor("k")

    fig.set_tight_layout(True)

    # -----------------------------------------------------------------------------------

    return series, fig
