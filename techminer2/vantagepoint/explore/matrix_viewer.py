# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
.. _matrix_viewer:

Matrix Viewer
===============================================================================



>>> from techminer2 import vantagepoint
>>> root_dir = "data/regtech/"
>>> vantagepoint.explore.matrix_viewer(
...     root_dir=root_dir,
...     columns='author_keywords',
...     rows='authors',
...     col_top_n=10,
...     row_top_n=10,    
... ).write_html("sphinx/_static/matrix_viewer_0.html")

.. raw:: html

    <iframe src="../../../../_static/matrix_viewer_0.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> vantagepoint.explore.matrix_viewer(
...     root_dir=root_dir,
...     columns='author_keywords',
...     col_top_n=10,
... ).write_html("sphinx/_static/matrix_viewer_1.html")

.. raw:: html

    <iframe src="../../../../_static/matrix_viewer_1.html" height="600px" width="100%" frameBorder="0"></iframe>

    
"""
import networkx as nx

from ...vosviewer.nx_utils import (
    nx_compute_spring_layout,
    nx_compute_textposition,
    nx_scale_links,
)
from ...vosviewer.px_utils import px_create_network_chart
from ..discover.matrix.co_occurrence_matrix import co_occurrence_matrix


def matrix_viewer(
    #
    # FUNCTION PARAMS:
    columns,
    rows=None,
    #
    # FIG PARAMS:
    n_labels=None,
    nx_k=None,
    nx_iterations=30,
    nx_random_state=0,
    node_size=30,
    textfont_size=10,
    link_width_min=0.8,
    link_width_max=4.0,
    xaxes_range=None,
    yaxes_range=None,
    show_axes=False,
    #
    # COLUMN PARAMS:
    col_top_n=None,
    col_occ_range=(None, None),
    col_gc_range=(None, None),
    col_custom_items=None,
    #
    # ROW PARAMS:
    row_top_n=None,
    row_occ_range=(None, None),
    row_gc_range=(None, None),
    row_custom_items=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """Makes network map from a co-ocurrence matrix."""

    cooc_matrix = co_occurrence_matrix(
        #
        # FUNCTION PARAMS:
        columns=columns,
        rows=rows,
        #
        # COLUMN PARAMS:
        col_top_n=col_top_n,
        col_occ_range=col_occ_range,
        col_gc_range=col_gc_range,
        col_custom_items=col_custom_items,
        #
        # ROW PARAMS:
        row_top_n=row_top_n,
        row_occ_range=row_occ_range,
        row_gc_range=row_gc_range,
        row_custom_items=row_custom_items,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    nx_graph = nx.Graph()

    nx_graph = __add_nodes_from_axis(
        nx_graph=nx_graph,
        axis=1,
        cooc_matrix=cooc_matrix,
        group=0,
        color="#7793a5",
        node_size=node_size,
        textfont_color="black",
        textfont_size=textfont_size,
    )

    if rows is not None:
        # The matrix is not symmetric
        nx_graph = __add_nodes_from_axis(
            nx_graph=nx_graph,
            axis=0,
            cooc_matrix=cooc_matrix,
            group=1,
            color="#465c6b",
            node_size=node_size,
            textfont_color="black",
            textfont_size=textfont_size,
        )

    if rows is None:
        nx_graph = ___add_links_for_symmetric_matrices(
            nx_graph,
            cooc_matrix,
        )
    else:
        nx_graph = ___add_links_for_non_symmetric_matrices(
            nx_graph,
            cooc_matrix,
        )

    nx_graph = nx_compute_spring_layout(
        graph=nx_graph, k=nx_k, iterations=nx_iterations, seed=nx_random_state
    )

    nx_graph = nx_compute_textposition(nx_graph)

    nx_graph = nx_scale_links(nx_graph, link_width_min, link_width_max)

    fig = px_create_network_chart(
        nx_graph=nx_graph,
        xaxes_range=xaxes_range,
        yaxes_range=yaxes_range,
        show_axes=show_axes,
        n_labels=n_labels,
    )

    return fig


def __add_nodes_from_axis(
    nx_graph,
    axis,
    cooc_matrix,
    group,
    color,
    node_size,
    textfont_color,
    textfont_size,
):
    #
    # Adds nodes from axis to nx_graph
    #
    if axis in (0, "index"):
        nodes = cooc_matrix.df_.index.tolist()
    elif axis in (1, "columns"):
        nodes = cooc_matrix.df_.columns.tolist()
    else:
        raise ValueError("axis must be 0, 1")

    for node in nodes:
        nx_graph.add_nodes_from(
            [node],
            #
            # NODE ATTR:
            text=" ".join(node.split(" ")[:-1]),
            OCC=int(node.split(" ")[-1].split(":")[0]),
            global_citations=int(node.split(" ")[-1].split(":")[0]),
            #
            # OTHER ATTR:
            group=group,
            color=color,
            node_size=node_size,
            textfont_color=textfont_color,
            textfont_size=textfont_size,
        )

    return nx_graph


def ___add_links_for_symmetric_matrices(nx_graph, cooc_matrix):
    #
    for i_row in range(cooc_matrix.df_.shape[0]):
        for i_col in range(i_row + 1, cooc_matrix.df_.shape[1]):
            if cooc_matrix.df_.iloc[i_row, i_col] > 0:
                #
                source_node = cooc_matrix.df_.index[i_row]
                target_node = cooc_matrix.df_.columns[i_col]
                weight = cooc_matrix.df_.iloc[i_row, i_col]

                nx_graph.add_weighted_edges_from(
                    ebunch_to_add=[(source_node, target_node, weight)],
                    # weight=weight,
                    dash="solid",
                    color="#7793a5",
                )

    return nx_graph


def ___add_links_for_non_symmetric_matrices(nx_graph, cooc_matrix):
    #
    # Adds links from ...
    for i_row in range(cooc_matrix.df_.shape[0]):
        for i_col in range(cooc_matrix.df_.shape[1]):
            if cooc_matrix.df_.iloc[i_row, i_col] > 0:
                #
                source_node = cooc_matrix.df_.index[i_row]
                target_node = cooc_matrix.df_.columns[i_col]
                weight = cooc_matrix.df_.iloc[i_row, i_col]

                nx_graph.add_weighted_edges_from(
                    ebunch_to_add=[(source_node, target_node, weight)],
                    # weight=weight,
                    dash="solid",
                    color="#b8c6d0",
                )

    return nx_graph
