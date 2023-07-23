# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
.. _co_occurrence_analysis.matrix_viewer:

Matrix Viewer
===============================================================================


>>> from techminer2.co_occurrence_analysis import matrix_viewer
>>> matrix_viewer(
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
...     node_size=30,
...     textfont_size=10,
...     #
...     # EDGES
...     edge_color="#b8c6d0",
...     edge_width_min=0.8,
...     edge_width_max=4.0,
...     #
...     # AXES:
...     xaxes_range=None,
...     yaxes_range=None,
...     show_axes=False,
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... ).write_html("sphinx/_static/co_occurrence_analysis/matrix_viewer_0.html")

.. raw:: html

    <iframe src="../../../../_static/co_occurrence_analysis/matrix_viewer_0.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> matrix_viewer(
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
...     node_size=30,
...     textfont_size=10,
...     #
...     # EDGES
...     edge_color="#b8c6d0",
...     edge_width_min=0.8,
...     edge_width_max=4.0,
...     #
...     # AXES:
...     xaxes_range=None,
...     yaxes_range=None,
...     show_axes=False,
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... ).write_html("sphinx/_static/co_occurrence_analysis/matrix_viewer_1.html")

.. raw:: html

    <iframe src="../../../../_static/co_occurrence_analysis/matrix_viewer_1.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
"""
import networkx as nx

from ...nx_compute_edge_width_from_edge_weight import nx_compute_edge_width_from_edge_weight
from ...nx_compute_spring_layout import nx_compute_spring_layout
from ...nx_compute_textposition_from_graph import nx_compute_textposition_from_graph
from ...nx_set_edge_color_to_constant import nx_set_edge_color_to_constant
from ...nx_set_node_size_to_constant import nx_set_node_size_to_constant
from ...nx_set_textfont_opacity_to_constant import nx_set_textfont_opacity_to_constant
from ...nx_set_textfont_size_to_constant import nx_set_textfont_size_to_constant
from ...nx_visualize_graph import nx_visualize_graph
from ..co_occurrence_matrix import co_occurrence_matrix


def matrix_viewer(
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
    node_size=30,
    textfont_size=10,
    #
    # EDGES
    edge_color="#b8c6d0",
    edge_width_min=0.8,
    edge_width_max=4.0,
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
    # Create the networkx graph
    nx_graph = nx.Graph()
    nx_graph = __add_nodes_from(nx_graph, cooc_matrix)
    nx_graph = __add_weighted_edges_from(nx_graph, cooc_matrix)

    #
    # Sets the layout
    nx_graph = nx_compute_spring_layout(nx_graph, nx_k, nx_iterations, nx_random_state)

    #
    # Sets the node attributes
    nx_graph = nx_set_node_size_to_constant(nx_graph, node_size)
    nx_graph = nx_set_textfont_size_to_constant(nx_graph, textfont_size)
    nx_graph = nx_set_textfont_opacity_to_constant(nx_graph, 1.0)

    #
    # Sets the edge attributes
    nx_graph = nx_compute_edge_width_from_edge_weight(nx_graph, edge_width_min, edge_width_max)
    nx_graph = nx_compute_textposition_from_graph(nx_graph)

    nx_graph = nx_set_edge_color_to_constant(nx_graph, edge_color)

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


#######
def __add_nodes_from(
    nx_graph,
    cooc_matrix,
):
    #
    # Adds rows nodes
    matrix = cooc_matrix.df_.copy()
    nodes = matrix.index.tolist()
    nx_graph.add_nodes_from(nodes, group=0, node_color="#7793a5")

    #
    # Adds columns nodes
    if matrix.index.tolist() != matrix.columns.tolist():
        nodes = matrix.columns.tolist()
        nx_graph.add_nodes_from(nodes, group=1, node_color="#465c6b")

    for node in nx_graph.nodes():
        nx_graph.nodes[node]["text"] = node

    return nx_graph


def __add_weighted_edges_from(nx_graph, cooc_matrix):
    #
    # Adds links from ...
    #
    matrix = cooc_matrix.df_.copy()

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
                        dash="solid",
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
                    dash="solid",
                )

    return nx_graph


#######
# def __add_nodes_from_axis(
#     nx_graph,
#     axis,
#     cooc_matrix,
#     group,
#     color,
#     node_size,
#     textfont_color,
#     textfont_size,
# ):
#     #
#     # Adds nodes from axis to nx_graph
#     #
#     if axis in (0, "index"):
#         nodes = cooc_matrix.df_.index.tolist()
#     elif axis in (1, "columns"):
#         nodes = cooc_matrix.df_.columns.tolist()
#     else:
#         raise ValueError("axis must be 0, 1")

#     for node in nodes:
#         nx_graph.add_nodes_from(
#             [node],
#             #
#             # NODE ATTR:
#             text=" ".join(node.split(" ")[:-1]),
#             OCC=int(node.split(" ")[-1].split(":")[0]),
#             global_citations=int(node.split(" ")[-1].split(":")[0]),
#             #
#             # OTHER ATTR:
#             group=group,
#             color=color,
#             node_size=node_size,
#             textfont_color=textfont_color,
#             textfont_size=textfont_size,
#         )

#     return nx_graph


# def ___add_links_for_symmetric_matrices(nx_graph, cooc_matrix, edge_color):
#     #
#     for i_row in range(cooc_matrix.df_.shape[0]):
#         for i_col in range(i_row + 1, cooc_matrix.df_.shape[1]):
#             if cooc_matrix.df_.iloc[i_row, i_col] > 0:
#                 #
#                 source_node = cooc_matrix.df_.index[i_row]
#                 target_node = cooc_matrix.df_.columns[i_col]
#                 weight = cooc_matrix.df_.iloc[i_row, i_col]

#                 nx_graph.add_weighted_edges_from(
#                     ebunch_to_add=[(source_node, target_node, weight)],
#                     # weight=weight,
#                     dash="solid",
#                     color=edge_color,
#                 )

#     return nx_graph


# def ___add_links_for_non_symmetric_matrices(nx_graph, cooc_matrix, edge_color):
#     #
#     # Adds links from ...
#     for i_row in range(cooc_matrix.df_.shape[0]):
#         for i_col in range(cooc_matrix.df_.shape[1]):
#             if cooc_matrix.df_.iloc[i_row, i_col] > 0:
#                 #
#                 source_node = cooc_matrix.df_.index[i_row]
#                 target_node = cooc_matrix.df_.columns[i_col]
#                 weight = cooc_matrix.df_.iloc[i_row, i_col]

#                 nx_graph.add_weighted_edges_from(
#                     ebunch_to_add=[(source_node, target_node, weight)],
#                     # weight=weight,
#                     dash="solid",
#                     color=edge_color,
#                 )

#     return nx_graph
