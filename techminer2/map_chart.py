"""
Map Chart
===============================================================================

>>> import pandas as pd
>>> from sklearn.decomposition import TruncatedSVD
>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/map_chart.png"
>>> co_occ_matrix = co_occurrence_matrix(
...     column='author_keywords',
...     min_occ=5,
...     normalization="salton",
...     directory=directory,
... )
>>> decomposed_matrix = TruncatedSVD(
...     n_components=2,
...     random_state=0,
... ).fit_transform(co_occ_matrix)
>>> decomposed_matrix = pd.DataFrame(
...     decomposed_matrix,
...     columns=['dim0', 'dim1'],
...     index=co_occ_matrix.index,
... )
>>> map_chart(
...     decomposed_matrix, 
...     figsize=(7, 7),
... ).savefig(file_name)


.. image:: images/map_chart.png
    :width: 700px
    :align: center
"""
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import AutoMinorLocator


def _get_quadrant(x, y, x_axis_at, y_axis_at):
    if x >= y_axis_at and y >= x_axis_at:
        return 0
    if x < y_axis_at and y >= x_axis_at:
        return 1
    if x < y_axis_at and y < x_axis_at:
        return 2
    return 3


def map_chart(
    data,
    dim_x=0,
    dim_y=1,
    max_items=100,
    color="k",
    figsize=(7, 7),
):
    data = data.copy()

    fig = plt.Figure(figsize=figsize)
    ax = fig.subplots()

    if isinstance(data.index, pd.MultiIndex):
        data.index = data.index.get_level_values(0)

    x_axis_at = data[f"dim{dim_y}"].mean()
    y_axis_at = data[f"dim{dim_x}"].mean()

    quadrants = {
        index: _get_quadrant(x_, y_, x_axis_at, y_axis_at)
        for index, x_, y_ in zip(data.index, data[f"dim{dim_x}"], data[f"dim{dim_y}"])
    }

    ax.plot(
        data[f"dim{dim_x}"],
        data[f"dim{dim_y}"],
        "o",
        markersize=2,
        color=color,
        alpha=0.5,
    )

    for index, row in data.head(max_items).iterrows():

        quadrant = quadrants[index]

        ha = {
            0: "left",
            1: "right",
            2: "right",
            3: "left",
        }[quadrant]

        va = {
            0: "bottom",
            1: "bottom",
            2: "top",
            3: "top",
        }[quadrant]

        ax.text(
            x=row[dim_x],
            y=row[dim_y],
            s=index,
            color=color,
            fontsize=8,
            horizontalalignment=ha,
            verticalalignment=va,
            alpha=0.9,
            # weight="bold",
        )

    ax.yaxis.set_ticks_position("both")
    ax.xaxis.set_ticks_position("both")

    ax.tick_params(axis="x", labelsize=7)
    ax.tick_params(axis="y", labelsize=7)

    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())

    ax.tick_params(which="mayor", color="k", length=5)
    ax.tick_params(which="minor", color="k", length=2)

    ax.axhline(x_axis_at, color="gray", linestyle="--")
    ax.axvline(y_axis_at, color="gray", linestyle="--")

    for x in ["top", "right", "bottom", "left"]:
        ax.spines[x].set_visible(False)

    fig.set_tight_layout(True)

    return fig
