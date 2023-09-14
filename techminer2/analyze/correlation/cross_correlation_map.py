# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
.. _correlation_analysis.cross_correlation_map:

Cross-correlation Map
===============================================================================

Creates an Cross-correlation Map.

>>> # grey colors: https://www.w3schools.com/colors/colors_shades.asp
>>> from techminer2.correlation import cross_correlation_map
>>> cross_correlation_map(
...     #
...     # FUNCTION PARAMS:
...     rows_and_columns='authors', 
...     cross_with='countries',
...     method="pearson",
...     #
...     # LAYOUT:
...     nx_k=None,
...     nx_iterations=30,
...     nx_random_state=0,
...     #
...     # NODES:
...     node_color="#7793a5",
...     node_size_min=30,
...     node_size_max=70,
...     textfont_size_min=10,
...     textfont_size_max=20,
...     textfont_opacity_min=0.35,
...     textfont_opacity_max=1.00,
...     #
...     # EDGES:
...     edge_colors=("#7793a5", "#7793a5", "#7793a5", "#7793a5"),
...     #
...     # AXES:
...     xaxes_range=None,
...     yaxes_range=None,
...     show_axes=False,
...     #
...     # ITEM PARAMS:
...     top_n=10,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_items=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... ).write_html("sphinx/_static/correlation/cross_correlation_map.html")

.. raw:: html

    <iframe src="../../../../_static/correlation/cross_correlation_map.html"
    height="600px" width="100%" frameBorder="0"></iframe>

"""
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

from .correlation_map import correlation_map
from .cross_correlation_matrix import cross_correlation_matrix


def cross_correlation_map(
    #
    # FUNCTION PARAMS:
    rows_and_columns,
    cross_with,
    method="pearson",
    #
    # LAYOUT:
    nx_k=None,
    nx_iterations=30,
    nx_random_state=0,
    #
    # NODES:
    node_color="#7793a5",
    node_size_min=30,
    node_size_max=70,
    textfont_size_min=10,
    textfont_size_max=20,
    textfont_opacity_min=0.35,
    textfont_opacity_max=1.00,
    #
    # EDGES:
    edge_colors=("#7793a5", "#7793a5", "#7793a5", "#7793a5"),
    #
    # AXES:
    xaxes_range=None,
    yaxes_range=None,
    show_axes=False,
    #
    # ITEM PARAMS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_items=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """Correlation map.

    :meta private:
    """

    corr_matrix = cross_correlation_matrix(
        #
        # FUNCTION PARAMS:
        rows_and_columns=rows_and_columns,
        cross_with=cross_with,
        method=method,
        #
        # ITEM PARAMS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    ).df_

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
        node_size_min=node_size_min,
        node_size_max=node_size_max,
        textfont_size_min=textfont_size_min,
        textfont_size_max=textfont_size_max,
        textfont_opacity_min=textfont_opacity_min,
        textfont_opacity_max=textfont_opacity_max,
        #
        # EDGES:
        edge_colors=edge_colors,
        #
        # AXES:
        xaxes_range=xaxes_range,
        yaxes_range=yaxes_range,
        show_axes=show_axes,
    )
