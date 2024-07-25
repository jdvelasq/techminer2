# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Auto-correlation Map
===============================================================================

Creates an Auto-correlation Map.

>>> # grey colors: https://www.w3schools.com/colors/colors_shades.asp
>>> from techminer2.correlation_matrix import auto_correlation_map
>>> auto_correlation_map(
...     #
...     # FUNCTION PARAMS:
...     rows_and_columns='authors',
...     method="pearson",
...     #
...     # ITEM PARAMS:
...     top_n=None,
...     occ_range=(2, None),
...     gc_range=(None, None),
...     custom_terms=None,
...     #
...     # LAYOUT:
...     nx_k=None,
...     nx_iterations=30,
...     nx_random_state=0,
...     #
...     # NODES:
...     node_color="#7793a5",
...     node_size_range=(30, 70),
...     textfont_size_range=(10, 20),
...     textfont_opacity_range=(0.35, 1.00),
...     #
...     # EDGES:
...     edge_top_n=None,
...     edge_similarity_min=None,
...     edge_widths=(2, 2, 4, 6),
...     edge_colors=("#7793a5", "#7793a5", "#7793a5", "#7793a5"),
...     #
...     # AXES:
...     xaxes_range=None,
...     yaxes_range=None,
...     show_axes=False,
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... ).write_html("sphinx/_static/correlation_matrix/auto_correlation_map.html")

.. raw:: html

    <iframe src="../_static/correlation_matrix/auto_correlation_map.html"
    height="600px" width="100%" frameBorder="0"></iframe>

"""
import pandas as pd  # type: ignore
from sklearn.metrics.pairwise import cosine_similarity  # type: ignore

from ._correlation_map import correlation_map
from .auto_correlation_matrix import auto_correlation_matrix


def auto_correlation_map(
    #
    # FUNCTION PARAMS:
    rows_and_columns,
    method="pearson",
    #
    # ITEM PARAMS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_terms=None,
    #
    # LAYOUT:
    nx_k=None,
    nx_iterations=30,
    nx_random_state=0,
    #
    # NODES:
    node_color="#7793a5",
    node_size_range=(30, 70),
    textfont_size_range=(10, 20),
    textfont_opacity_range=(0.35, 1.00),
    #
    # EDGES:
    edge_top_n=None,
    edge_similarity_min=None,
    edge_widths=(2, 2, 4, 6),
    edge_colors=("#7793a5", "#7793a5", "#7793a5", "#7793a5"),
    #
    # AXES:
    xaxes_range=None,
    yaxes_range=None,
    show_axes=False,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """:meta private:"""

    corr_matrix = auto_correlation_matrix(
        #
        # FUNCTION PARAMS:
        rows_and_columns=rows_and_columns,
        method=method,
        #
        # ITEM PARAMS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_terms=custom_terms,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    similarity = pd.DataFrame(
        cosine_similarity(corr_matrix),
        index=corr_matrix.index,
        columns=corr_matrix.columns,
    )

    return correlation_map(
        similarity=similarity,
        #
        # LAYOUT:
        nx_k=nx_k,
        nx_iterations=nx_iterations,
        nx_random_state=nx_random_state,
        #
        # NODES:
        node_color=node_color,
        node_size_range=node_size_range,
        textfont_size_range=textfont_size_range,
        textfont_opacity_range=textfont_opacity_range,
        #
        # EDGES:
        edge_top_n=edge_top_n,
        edge_similarity_min=edge_similarity_min,
        edge_widths=edge_widths,
        edge_colors=edge_colors,
        #
        # AXES:
        xaxes_range=xaxes_range,
        yaxes_range=yaxes_range,
        show_axes=show_axes,
    )
