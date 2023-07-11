# flake8: noqa
# pylint: disable=line-too-long
"""
.. _factor_decomposition_2d_map:

Factor Decomposition 2D Map 
===============================================================================

Plots the MDS (with 2 components) of the normalized co-occurrence matrix.


* Preparation

>>> import techminer2plus as tm2p
>>> root_dir = "data/regtech/"

* Object oriented interface

>>> fig = (
...     tm2p.records(root_dir=root_dir)
...     .co_occurrence_matrix(
...         columns='author_keywords',
...         col_top_n=20,
...     )
...     .factor_decomposition_svd()
...     .factor_decomposition_2d_map()
... )

    
* Functional interface

>>> cooc_matrix = tm2p.co_occurrence_matrix(
...     root_dir="data/regtech/",
...     columns='author_keywords',
...     col_top_n=20,
... )
>>> factor_matrix = tm2p.factor_decomposition_svd(
...     cooc_matrix,
... )
>>> fig = factor_matrix.factor_decomposition_2d_map()

* Results:

>>> fig.write_html("sphinx/_static/factor_decomposition_2d_map.html")

.. raw:: html

    <iframe src="../../_static/factor_decomposition_2d_map.html" height="600px" width="100%" frameBorder="0"></iframe>


"""
from .manifold_2d_map import manifold_2d_map


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def factor_decomposition_2d_map(
    factor_matrix,
    #
    # Plot params:
    dim_x=0,
    dim_y=1,
    node_color="#556f81",
    node_size_min=12,
    node_size_max=50,
    textfont_size_min=8,
    textfont_size_max=20,
    xaxes_range=None,
    yaxes_range=None,
):
    """MDS 2D map."""

    frame = factor_matrix.df_.iloc[:, [dim_x, dim_y]]
    node_occ = factor_matrix.df_.index.to_list()
    node_occ = [item.split(" ")[-1] for item in node_occ]
    node_occ = [item.split(":")[0] for item in node_occ]
    node_occ = [int(item) for item in node_occ]

    fig = manifold_2d_map(
        node_x=frame[frame.columns[dim_x]],
        node_y=frame[frame.columns[dim_y]],
        node_text=frame.index.to_list(),
        node_occ=node_occ,
        node_color=node_color,
        node_size_min=node_size_min,
        node_size_max=node_size_max,
        textfont_size_min=textfont_size_min,
        textfont_size_max=textfont_size_max,
        xaxes_range=xaxes_range,
        yaxes_range=yaxes_range,
    )

    return fig
