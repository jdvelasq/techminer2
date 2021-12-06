"""
Co-occurrence SVD map
===============================================================================

Plots the SVD of the co-occurrence matrix normalized with the **cosine** measure.

The plot is based on the SVD technique used in T-LAB's comparative analysis.

**Algorithm**

1. Apply SVD to the co-occurrence matrix with `n_components=20`.

2. Plot the decomposed matrix.


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/co_occurrence_svd_map.png"
>>> matrix = co_occurrence_matrix('author_keywords', min_occ=15, directory=directory)
>>> co_occurrence_svd_map(matrix).savefig(file_name)


.. image:: images/co_occurrence_svd_map.png
    :width: 700px
    :align: center




"""
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import AutoMinorLocator
from sklearn.decomposition import TruncatedSVD
from sklearn.manifold import MDS


def co_occurrence_svd_map(
    matrix,
    max_terms=150,
    dim_x=0,
    dim_y=1,
    figsize=(7, 7),
    n_iter=5,
    random_state=0,
):

    max_dimensions = min(20, len(matrix.columns) - 1)

    decomposed_matrix = TruncatedSVD(
        n_components=max_dimensions, n_iter=n_iter, random_state=random_state
    ).fit_transform(matrix)

    if decomposed_matrix.shape[0] > max_terms:
        decomposed_matrix = decomposed_matrix.head(max_terms)
    if isinstance(matrix.index, pd.MultiIndex):
        labels = matrix.index.get_level_values(0)
    else:
        labels = matrix.index

    decomposed_matrix = pd.DataFrame(
        decomposed_matrix,
        columns=[f"dim{dim}" for dim in range(max_dimensions)],
        index=labels,
    )

    fig = plt.Figure(figsize=figsize)
    ax = fig.subplots()
    ax.tick_params(axis="x", labelsize=7)
    ax.tick_params(axis="y", labelsize=7)

    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.tick_params(which="mayor", color="k", length=5)
    ax.tick_params(which="minor", color="k", length=2)

    x_min = decomposed_matrix[f"dim{dim_x}"].min()
    x_max = decomposed_matrix[f"dim{dim_x}"].max()
    y_min = decomposed_matrix[f"dim{dim_y}"].min()
    y_max = decomposed_matrix[f"dim{dim_y}"].max()

    ax.axis([x_min, x_max, y_min, y_max])
    ax.axhline(0, color="gray", linestyle="--")
    ax.axvline(0, color="gray", linestyle="--")

    for label, values in decomposed_matrix.iterrows():

        ax.text(
            x=values[f"dim{dim_x}"],
            y=values[f"dim{dim_y}"],
            s=label,
            fontsize=8,
            horizontalalignment="center",
            verticalalignment="center",
            alpha=0.9,
            weight="bold",
        )

    ax.set_xlabel(f"Dimension {dim_x}", fontsize=8)
    ax.set_ylabel(f"Dimension {dim_y}", fontsize=8)

    for side in ["top", "right", "bottom", "left"]:
        ax.spines[side].set_visible(False)

    fig.set_tight_layout(True)

    return fig
