"""
Pie chart
===============================================================================



>>> from techminer import *
>>> directory = "/workspaces/techminer-api/tests/data/"
>>> pie_chart(series=annual_indicators(directory)['num_documents'], darkness=annual_indicators(directory)['global_citations'])

.. image:: images/pie_chart.png
    :width: 500px
    :align: center


"""


import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

TEXTLEN = 40


def pie_chart(
    series,
    darkness=None,
    cmap="Greys",
    figsize=(6, 6),
    fontsize=9,
    wedgeprops={
        "width": 0.6,
        "edgecolor": "k",
        "linewidth": 0.5,
        "linestyle": "-",
        "antialiased": True,
    },
):
    """Plot a pie chart."""
    darkness = series if darkness is None else darkness

    cmap = plt.cm.get_cmap(cmap)
    colors = [
        cmap(0.1 + 0.90 * (d - min(darkness)) / (max(darkness) - min(darkness)))
        for d in darkness
    ]

    matplotlib.rc("font", size=fontsize)
    fig = plt.Figure(figsize=figsize)
    ax = fig.subplots()

    ax.pie(
        x=series,
        labels=series.index,
        colors=colors,
        wedgeprops=wedgeprops,
    )

    fig.set_tight_layout(True)

    return fig
