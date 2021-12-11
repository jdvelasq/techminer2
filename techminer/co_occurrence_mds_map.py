"""
Co-occurrence MDS map
===============================================================================

Plots the co-word association MDS map.

The plot is based on the MDS map for word associations in T-LAB. 

**Algorithm**

1. Compute co-occurrence matrix.
2. Apply SVD to the co-occurrence matrix with `n_components=2`.
3. Apply MDS with `n_components=2` to the SVD matrix.
4. Plot the MDS matrix.

Note: any association index can be used.

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/co_occurrence_mds_map.png"
>>> co_occurrence_mds_map(
...     column='author_keywords',
...     min_occ=5,    
...     directory=directory,
... ).savefig(file_name)

.. image:: images/co_occurrence_mds_map.png
    :width: 700px
    :align: center




"""
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import AutoMinorLocator, MultipleLocator
from sklearn.decomposition import TruncatedSVD
from sklearn.manifold import MDS

from .co_occurrence_matrix import co_occurrence_matrix
from .map_chart import map_chart


def co_occurrence_mds_map(
    column,
    min_occ=1,
    max_occ=None,
    normalization=None,
    scheme=None,
    directory="./",
    figsize=(7, 7),
    svd__n_iter=5,
    mds__n_init=4,
    mds__max_iter=300,
    random_state=0,
):
    matrix = co_occurrence_matrix(
        column=column,
        min_occ=min_occ,
        max_occ=max_occ,
        normalization=normalization,
        scheme=scheme,
        directory=directory,
    )

    decomposed_matrix = TruncatedSVD(
        n_components=20, n_iter=svd__n_iter, random_state=random_state
    ).fit_transform(matrix)
    mds_matrix = MDS(
        n_components=2,
        n_init=mds__n_init,
        max_iter=mds__max_iter,
        random_state=random_state,
    ).fit_transform(decomposed_matrix)
    if mds_matrix.shape[0] > 150:
        mds_matrix = mds_matrix[:150, :]
    if isinstance(matrix.index, pd.MultiIndex):
        labels = matrix.index.get_level_values(0)
    else:
        labels = matrix.index

    mds = pd.DataFrame(mds_matrix, columns=["dim0", "dim1"], index=labels)

    return map_chart(
        data=mds,
        dim_x=0,
        dim_y=1,
        max_items=1000,
        figsize=figsize,
        color="k",
    )

    # fig = plt.Figure(figsize=figsize)
    # ax = fig.subplots()

    # ax.yaxis.set_ticks_position("both")
    # ax.xaxis.set_ticks_position("both")

    # ax.tick_params(axis="x", labelsize=7)
    # ax.tick_params(axis="y", labelsize=7)

    # ax.xaxis.set_minor_locator(AutoMinorLocator())
    # ax.yaxis.set_minor_locator(AutoMinorLocator())

    # ax.tick_params(which="mayor", color="k", length=5)
    # ax.tick_params(which="minor", color="k", length=2)

    # ax.axis([mds.dim0.min(), mds.dim0.max(), mds.dim1.min(), mds.dim1.max()])
    # ax.axhline(0, color="gray", linestyle="--")
    # ax.axvline(0, color="gray", linestyle="--")

    # for label, values in mds.iterrows():

    #     ax.text(
    #         x=values[0],
    #         y=values[1],
    #         s=label,
    #         fontsize=8,
    #         horizontalalignment="center",
    #         verticalalignment="center",
    #         alpha=0.9,
    #         weight="bold",
    #         # zorder=13,
    #     )

    # for x in ["top", "right", "bottom", "left"]:
    #     ax.spines[x].set_visible(False)

    # fig.set_tight_layout(True)

    # return fig
