# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

#
# Creates a co-occurrence networkx graph from a co-occurrence matrix.
#
import networkx as nx

from .co_occurrence.co_occurrence_matrix import co_occurrence_matrix
from .co_occurrence.normalize_co_occurrence_matrix import normalize_co_occurrence_matrix
from .nx_apply_cdlib_algorithm import nx_apply_cdlib_algorithm
from .nx_compute_edge_width_from_edge_weight import nx_compute_edge_width_from_edge_weight
from .nx_compute_node_size_from_item_occ import nx_compute_node_size_from_item_occ
from .nx_compute_spring_layout import nx_compute_spring_layout
from .nx_compute_textfont_opacity_from_item_occ import nx_compute_textfont_opacity_from_item_occ
from .nx_compute_textfont_size_from_item_occ import nx_compute_textfont_size_from_item_occ
from .nx_compute_textposition_from_graph import nx_compute_textposition_from_graph
from .nx_set_edge_color_from_palette import nx_set_edge_color_from_palette
from .nx_set_edge_color_to_constant import nx_set_edge_color_to_constant
from .nx_set_node_color_from_group_attr import nx_set_node_color_from_group_attr


def nx_create_co_occurrence_graph(
    #
    # FUNCTION PARAMS:
    rows_and_columns,
    #
    # COLUMN PARAMS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_items=None,
    #
    # NETWORK CLUSTERING:
    association_index="association",
    algorithm_or_dict="louvain",
    #
    # LAYOUT:
    nx_k=None,
    nx_iterations=30,
    nx_random_state=0,
    #
    # NODES:
    node_size_min=30,
    node_size_max=70,
    textfont_size_min=10,
    textfont_size_max=20,
    textfont_opacity_min=0.35,
    textfont_opacity_max=1.00,
    #
    # EDGES:
    edge_color="#7793a5",
    edge_width_min=0.8,
    edge_width_max=3.0,
    #
    # AXES:
    # xaxes_range=None,
    # yaxes_range=None,
    # show_axes=False,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    cooc_matrix = co_occurrence_matrix(
        #
        # FUNCTION PARAMS:
        columns=rows_and_columns,
        #
        # COLUMN PARAMS:
        col_top_n=top_n,
        col_occ_range=occ_range,
        col_gc_range=gc_range,
        col_custom_items=custom_items,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    if association_index is not None:
        cooc_matrix = normalize_co_occurrence_matrix(cooc_matrix, association_index)

    #
    # Create the networkx graph
    nx_graph = nx.Graph()
    nx_graph = __add_nodes_from(nx_graph, cooc_matrix)
    nx_graph = __add_weighted_edges_from(nx_graph, cooc_matrix)

    #
    # Cluster the networkx graph
    if isinstance(algorithm_or_dict, str):
        nx_graph = nx_apply_cdlib_algorithm(nx_graph, algorithm_or_dict)
    if isinstance(algorithm_or_dict, dict):
        nx_graph = __assign_group_from_dict(nx_graph, algorithm_or_dict)

    #
    # Sets the layout
    nx_graph = nx_compute_spring_layout(nx_graph, nx_k, nx_iterations, nx_random_state)

    #
    # Sets the node attributes
    nx_graph = nx_set_node_color_from_group_attr(nx_graph)

    nx_graph = nx_compute_node_size_from_item_occ(nx_graph, node_size_min, node_size_max)

    nx_graph = nx_compute_textfont_size_from_item_occ(
        nx_graph, textfont_size_min, textfont_size_max
    )

    nx_graph = nx_compute_textfont_opacity_from_item_occ(
        nx_graph, textfont_opacity_min, textfont_opacity_max
    )

    #
    # Sets the edge attributes
    nx_graph = nx_compute_edge_width_from_edge_weight(nx_graph, edge_width_min, edge_width_max)

    nx_graph = nx_compute_textposition_from_graph(nx_graph)

    nx_graph = nx_set_edge_color_to_constant(nx_graph, edge_color)
    nx_graph = nx_set_edge_color_from_palette(nx_graph)

    return nx_graph


def __add_nodes_from(
    nx_graph,
    cooc_matrix,
):
    matrix = cooc_matrix.df_.copy()
    nodes = matrix.columns.tolist()
    nx_graph.add_nodes_from(nodes, group=0)

    for node in nx_graph.nodes():
        # nx_graph.nodes[node]["text"] = node

        #
        # Remove metrics from the name
        nx_graph.nodes[node]["text"] = " ".join(node.split(" ")[:-1])

    return nx_graph


def __add_weighted_edges_from(
    nx_graph,
    cooc_matrix,
):
    matrix = cooc_matrix.df_.copy()

    for i_row, row in enumerate(cooc_matrix.df_.index.tolist()):
        for i_col, col in enumerate(cooc_matrix.df_.columns.tolist()):
            #
            # Unicamente toma valores por encima de la diagonal principal
            if i_col <= i_row:
                continue

            weight = matrix.loc[row, col]
            if weight > 0:
                nx_graph.add_weighted_edges_from(
                    ebunch_to_add=[(row, col, weight)],
                    dash="solid",
                )

    return nx_graph


def __assign_group_from_dict(nx_graph, group_dict):
    #
    # The group is assigned using and external algorithm. It is designed
    # to provide analysis capabilities to the system when other types of
    # analysis are conducted, for example, factor analysis.
    for node, group in group_dict.items():
        nx_graph.nodes[node]["group"] = group
    return nx_graph
