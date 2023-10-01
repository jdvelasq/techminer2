# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Words Viewer
===============================================================================


>>> from techminer2.analyze.co_occurrence import words_viewer
>>> words_viewer(
...     #
...     # FUNCTION PARAMS:
...     columns='author_keywords',
...     rows='authors',
...     #
...     # COLUMN PARAMS:
...     col_top_n=10,
...     col_occ_range=(None, None),
...     col_gc_range=(None, None),
...     col_custom_items=None,
...     #
...     # ROW PARAMS:
...     row_top_n=10,    
...     row_occ_range=(None, None),
...     row_gc_range=(None, None),
...     row_custom_items=None,
...     #
...     # LAYOUT:
...     nx_k=None,
...     nx_iterations=30,
...     nx_random_state=0,
...     #
...     # NODES:
...     node_colors=("#7793a5", "#465c6b"),
...     node_size_min=30,
...     node_size_max=70,
...     textfont_size_min=10,
...     textfont_size_max=20,
...     textfont_opacity_min=0.35,
...     textfont_opacity_max=1.00,
...     #
...     # EDGES
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
... ).write_html("sphinx/_static/analyze/co_occurrence/words_viewer_0.html")

.. raw:: html

    <iframe src="../../../../_static/analyze/co_occurrence/words_viewer_0.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> words_viewer(
...     #
...     # FUNCTION PARAMS:
...     columns='author_keywords',
...     rows=None,
...     #
...     # COLUMN PARAMS:
...     col_top_n=10,
...     col_occ_range=(None, None),
...     col_gc_range=(None, None),
...     col_custom_items=None,
...     #
...     # ROW PARAMS:
...     row_top_n=None,    
...     row_occ_range=(None, None),
...     row_gc_range=(None, None),
...     row_custom_items=None,
...     #
...     # LAYOUT:
...     nx_k=None,
...     nx_iterations=30,
...     nx_random_state=0,
...     #
...     # NODES:
...     node_colors=("#7793a5", "#465c6b"),
...     node_size_min=30,
...     node_size_max=70,
...     textfont_size_min=10,
...     textfont_size_max=20,
...     textfont_opacity_min=0.35,
...     textfont_opacity_max=1.00,
...     #
...     # EDGES
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
... ).write_html("sphinx/_static/analyze/co_occurrence/words_viewer_1.html")

.. raw:: html

    <iframe src="../../../../_static/analyze/co_occurrence/words_viewer_1.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
"""
import networkx as nx
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

from ...nx_compute_edge_width_from_edge_weight import nx_compute_edge_width_from_edge_weight
from ...nx_compute_node_size_from_item_occ import nx_compute_node_size_from_item_occ
from ...nx_compute_spring_layout import nx_compute_spring_layout
from ...nx_compute_textfont_opacity_from_item_occ import nx_compute_textfont_opacity_from_item_occ
from ...nx_compute_textfont_size_from_item_occ import nx_compute_textfont_size_from_item_occ
from ...nx_compute_textposition_from_graph import nx_compute_textposition_from_graph
from ...nx_set_edge_color_to_constant import nx_set_edge_color_to_constant
from ...nx_visualize_graph import nx_visualize_graph
from .co_occurrence_matrix import co_occurrence_matrix


def words_viewer(
    #
    # FUNCTION PARAMS:
    columns,
    rows=None,
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
    # LAYOUT:
    nx_k=None,
    nx_iterations=30,
    nx_random_state=0,
    #
    # NODES:
    node_colors=("#7793a5", "#465c6b"),
    node_size_min=30,
    node_size_max=70,
    textfont_size_min=10,
    textfont_size_max=20,
    textfont_opacity_min=0.35,
    textfont_opacity_max=1.00,
    #
    # EDGES
    edge_colors=("#7793a5", "#7793a5", "#7793a5", "#7793a5"),
    # edge_width_min=0.8,
    # edge_width_max=4.0,
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
    """Makes network map from a co-ocurrence matrix.

    :meta private:
    """

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

    #
    #
    similarity = pd.DataFrame(
        cosine_similarity(cooc_matrix.df_),
        index=cooc_matrix.df_.index,
        columns=cooc_matrix.df_.columns,
    )

    #
    # Create the networkx graph
    nx_graph = nx.Graph()
    nx_graph = __add_nodes_from(nx_graph, similarity, node_colors)
    nx_graph = __add_weighted_edges_from(nx_graph, similarity)

    #
    # Sets the layout
    nx_graph = nx_compute_spring_layout(nx_graph, nx_k, nx_iterations, nx_random_state)

    #
    # Sets the node attributes
    nx_graph = nx_compute_node_size_from_item_occ(nx_graph, node_size_min, node_size_max)
    nx_graph = nx_compute_textfont_size_from_item_occ(
        nx_graph, textfont_size_min, textfont_size_max
    )

    nx_graph = nx_compute_textfont_opacity_from_item_occ(
        nx_graph, textfont_opacity_min, textfont_opacity_max
    )
    #
    # Sets the edge attributes
    nx_graph = __set_edge_properties(nx_graph, edge_colors)
    nx_graph = nx_compute_textposition_from_graph(nx_graph)

    return nx_visualize_graph(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
        #
        # NETWORK PARAMS:
        xaxes_range=xaxes_range,
        yaxes_range=yaxes_range,
        show_axes=show_axes,
    )


def __add_nodes_from(
    nx_graph,
    similarity_matrix,
    node_colors,
):
    #
    # Adds rows nodes
    matrix = similarity_matrix.copy()
    nodes = matrix.index.tolist()
    nx_graph.add_nodes_from(nodes, group=0, node_color=node_colors[0])

    #
    # Adds columns nodes
    if matrix.index.tolist() != matrix.columns.tolist():
        nodes = matrix.columns.tolist()
        nx_graph.add_nodes_from(nodes, group=1, node_color=node_colors[1])

    for node in nx_graph.nodes():
        nx_graph.nodes[node]["text"] = node

    return nx_graph


def __add_weighted_edges_from(nx_graph, similarity_matrix):
    #
    # Adds links from ...
    #
    matrix = similarity_matrix.copy()

    if matrix.index.tolist() == matrix.columns.tolist():
        #
        # This is a symmetric matrix:
        #
        for i_row, row in enumerate(matrix.index.tolist()):
            for i_col, col in enumerate(matrix.columns.tolist()):
                #
                if matrix.iloc[i_row, i_col] > 0:
                    #
                    # Unicamente toma valores por encima de la diagonal principal
                    if i_col <= i_row:
                        continue

                    weight = matrix.loc[row, col]
                    nx_graph.add_weighted_edges_from(
                        ebunch_to_add=[(row, col, weight)],
                    )

        return nx_graph

    #
    # This is a non-symmetric matrix:
    #
    for i_row, row in enumerate(matrix.index.tolist()):
        for i_col, col in enumerate(matrix.columns.tolist()):
            #
            if matrix.loc[row, col] > 0:
                #
                weight = matrix.loc[row, col]
                nx_graph.add_weighted_edges_from(
                    ebunch_to_add=[(row, col, weight)],
                )

    return nx_graph


def __set_edge_properties(nx_graph, edge_colors):
    for edge in nx_graph.edges():
        weight = nx_graph.edges[edge]["weight"]

        if weight < 0.25:
            width, dash = 2, "dot"
            edge_color = edge_colors[0]

        elif weight < 0.5:
            width, dash = 2, "dash"
            edge_color = edge_colors[1]

        elif weight < 0.75:
            width, dash = 4, "solid"
            edge_color = edge_colors[2]

        else:
            width, dash = 6, "solid"
            edge_color = edge_colors[3]

        nx_graph.edges[edge]["width"] = width
        nx_graph.edges[edge]["dash"] = dash
        nx_graph.edges[edge]["color"] = edge_color

    return nx_graph
