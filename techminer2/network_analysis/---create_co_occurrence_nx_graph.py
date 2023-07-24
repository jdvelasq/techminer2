# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements


import networkx as nx

from ..co_occurrence_analysis.co_occurrence_matrix import co_occurrence_matrix

# from .matrix_normalization import matrix_normalization
# from .nx_utils import (
#     nx_apply_community_detection_method,
#     nx_compute_spring_layout,
#     nx_compute_textposition,
#     nx_scale_edge_width,
#     nx_scale_node_size_prop_to_occ_property,
#     nx_scale_textfont_opacity_prop_to_occ_property,
#     nx_scale_textfont_size_prop_to_occ_property,
#     nx_set_node_color_by_group,
# )


def create_co_occurrence_nx_graph(
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
    # NETWORK PARAMS:
    algorithm_or_estimator="louvain",
    normalization_index=None,
    color="#7793a5",
    nx_k=None,
    nx_iterations=10,
    nx_random_state=0,
    node_size_min=30,
    node_size_max=70,
    textfont_size_min=10,
    textfont_size_max=20,
    edge_width_min=0.8,
    edge_width_max=3.0,
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

    if normalization_index is not None:
        cooc_matrix = matrix_normalization(cooc_matrix, normalization_index)

    #
    # Creates an empty network
    nx_graph = nx.Graph()

    #
    # Add nodes
    nodes = cooc_matrix.df_.columns.tolist()
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
            group=0,
            color=color,
            node_size=node_size_min,
            textfont_color=color,
            textfont_size=textfont_size_min,
        )

    #
    # Add edges
    for i_row in range(cooc_matrix.df_.shape[0]):
        for i_col in range(i_row + 1, cooc_matrix.df_.shape[1]):
            if cooc_matrix.df_.iloc[i_row, i_col] > 0:
                #
                source_node = cooc_matrix.df_.index[i_row]
                target_node = cooc_matrix.df_.columns[i_col]
                weight = cooc_matrix.df_.iloc[i_row, i_col]

                nx_graph.add_weighted_edges_from(
                    ebunch_to_add=[(source_node, target_node, weight)],
                    width=weight,
                    dash="solid",
                    color="#7793a5",
                )

    #
    # Scales the node size
    nx_graph = nx_scale_node_size_prop_to_occ_property(nx_graph, node_size_min, node_size_max)

    #
    # Scales the font size
    nx_graph = nx_scale_textfont_size_prop_to_occ_property(
        nx_graph, textfont_size_min, textfont_size_max
    )

    #
    # Scales the font color
    nx_graph = nx_scale_textfont_opacity_prop_to_occ_property(
        nx_graph, textfont_opacity_min=0.35, textfont_opacity_max=1.00
    )

    #
    # Scales edge width
    nx_graph = nx_scale_edge_width(nx_graph, edge_width_min, edge_width_max)

    #
    # Layout and text position
    nx_graph = nx_compute_spring_layout(
        graph=nx_graph, k=nx_k, iterations=nx_iterations, seed=nx_random_state
    )
    nx_graph = nx_compute_textposition(nx_graph)

    #
    # Network clustering
    if isinstance(algorithm_or_estimator, str):
        nx_graph = nx_apply_community_detection_method(nx_graph, algorithm_or_estimator)
        nx_graph = nx_set_node_color_by_group(nx_graph)

    return nx_graph
