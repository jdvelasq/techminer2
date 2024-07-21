# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Co-occurrence Matrix Network
===============================================================================


>>> from techminer2.co_occurrence_matrix import co_occurrence_matrix_network
>>> co_occurrence_matrix_network(
...     #
...     # FUNCTION PARAMS:
...     columns='author_keywords',
...     rows='authors',
...     retain_counters=True,
...     #
...     # COLUMN PARAMS:
...     col_top_n=10,
...     col_occ_range=(None, None),
...     col_gc_range=(None, None),
...     col_custom_terms=None,
...     #
...     # ROW PARAMS:
...     row_top_n=10,    
...     row_occ_range=(None, None),
...     row_gc_range=(None, None),
...     row_custom_terms=None,
...     #
...     # LAYOUT:
...     nx_k=None,
...     nx_iterations=30,
...     nx_random_state=0,
...     #
...     # NODES AND EDGES:
...     node_size_range=(30, 70),
...     textfont_size_range=(10, 20),
...     textfont_opacity_range=(0.35, 1.00),
...     edge_color="#b8c6d0",
...     edge_width_range=(0.8, 4.0),
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
... ).write_html("sphinx/_static/co_occurrence_matrix/co_occurrence_matrix_network_0.html")

.. raw:: html

    <iframe src="../_static/co_occurrence_matrix/co_occurrence_matrix_network_0.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> co_occurrence_matrix_network(
...     #
...     # FUNCTION PARAMS:
...     columns='author_keywords',
...     rows=None,
...     retain_counters=True,
...     #
...     # COLUMN PARAMS:
...     col_top_n=10,
...     col_occ_range=(None, None),
...     col_gc_range=(None, None),
...     col_custom_terms=None,
...     #
...     # ROW PARAMS:
...     row_top_n=None,    
...     row_occ_range=(None, None),
...     row_gc_range=(None, None),
...     row_custom_terms=None,
...     #
...     # LAYOUT:
...     nx_k=None,
...     nx_iterations=30,
...     nx_random_state=0,
...     #
...     # NODES AND EDGES:
...     node_size_range=(30, 70),
...     textfont_size_range=(10, 20),
...     textfont_opacity_range=(0.35, 1.00),
...     edge_color="#b8c6d0",
...     edge_width_range=(0.8, 4.0),
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
... ).write_html("sphinx/_static/co_occurrence_matrix/co_occurrence_matrix_network_1.html")

.. raw:: html

    <iframe src="../../../../_static/co_occurrence_matrix/co_occurrence_matrix_network_1.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
"""
import networkx as nx

from .._core.nx.nx_assign_opacity_to_text_based_on_frequency import nx_assign_opacity_to_text_based_on_frequency
from .._core.nx.nx_assign_sizes_to_nodes_based_on_occurrences import nx_assign_sizes_to_nodes_based_on_occurrences
from .._core.nx.nx_assign_text_positions_to_nodes_by_quadrants import nx_assign_text_positions_to_nodes_by_quadrants
from .._core.nx.nx_assign_textfont_sizes_to_nodes_based_on_occurrences import nx_assign_textfont_sizes_to_nodes_based_on_occurrences
from .._core.nx.nx_assign_uniform_color_to_edges import nx_assign_uniform_color_to_edges
from .._core.nx.nx_assign_widths_to_edges_based_on_weight import nx_assign_widths_to_edges_based_on_weight
from .._core.nx.nx_compute_spring_layout_positions import nx_compute_spring_layout_positions
from .._core.nx.nx_network_plot import nx_network_plot
from .co_occurrence_matrix import co_occurrence_matrix


def co_occurrence_matrix_network(
    #
    # FUNCTION PARAMS:
    columns,
    rows=None,
    retain_counters=True,
    #
    # COLUMN PARAMS:
    col_top_n=None,
    col_occ_range=(None, None),
    col_gc_range=(None, None),
    col_custom_terms=None,
    #
    # ROW PARAMS:
    row_top_n=None,
    row_occ_range=(None, None),
    row_gc_range=(None, None),
    row_custom_terms=None,
    #
    # LAYOUT:
    nx_k=None,
    nx_iterations=30,
    nx_random_state=0,
    #
    # NODES:
    node_size_range=(30, 70),
    textfont_size_range=(10, 20),
    textfont_opacity_range=(0.35, 1.00),
    #
    # EDGES:
    edge_color="#b8c6d0",
    edge_width_range=(0.8, 4.0),
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

    cooc_matrix = co_occurrence_matrix(
        #
        # FUNCTION PARAMS:
        columns=columns,
        rows=rows,
        retain_counters=retain_counters,
        #
        # COLUMN PARAMS:
        col_top_n=col_top_n,
        col_occ_range=col_occ_range,
        col_gc_range=col_gc_range,
        col_custom_terms=col_custom_terms,
        #
        # ROW PARAMS:
        row_top_n=row_top_n,
        row_occ_range=row_occ_range,
        row_gc_range=row_gc_range,
        row_custom_terms=row_custom_terms,
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
    nx_graph = _add_nodes_from_co_occurrence_matrix(nx_graph, cooc_matrix)
    nx_graph = _add_weighted_edges_from_co_occurrence_matrix(nx_graph, cooc_matrix)

    #
    # Sets the layout
    nx_graph = nx_compute_spring_layout_positions(nx_graph, nx_k, nx_iterations, nx_random_state)

    #
    # Sets the node attributes
    nx_graph = nx_assign_sizes_to_nodes_based_on_occurrences(nx_graph, node_size_range)
    nx_graph = nx_assign_textfont_sizes_to_nodes_based_on_occurrences(nx_graph, textfont_size_range)

    nx_graph = nx_assign_opacity_to_text_based_on_frequency(nx_graph, textfont_opacity_range)
    #
    # Sets the edge attributes
    nx_graph = nx_assign_widths_to_edges_based_on_weight(nx_graph, edge_width_range)
    nx_graph = nx_assign_text_positions_to_nodes_by_quadrants(nx_graph)

    nx_graph = nx_assign_uniform_color_to_edges(nx_graph, edge_color)

    return nx_network_plot(
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
def _add_nodes_from_co_occurrence_matrix(
    nx_graph,
    cooc_matrix,
):
    #
    # Adds rows nodes
    matrix = cooc_matrix.copy()
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


def _add_weighted_edges_from_co_occurrence_matrix(nx_graph, cooc_matrix):
    #
    # Adds links from ...
    #
    matrix = cooc_matrix.copy()

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
