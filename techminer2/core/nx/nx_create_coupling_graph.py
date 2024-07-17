# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

import networkx as nx
import numpy as np

from ...helpers.append_occurrences_and_citations_to_axis import append_occurrences_and_citations_to_axis
from ...metrics.performance_metrics import performance_metrics
from ..read_filtered_database import read_filtered_database
from .nx_apply_cdlib_algorithm import nx_apply_cdlib_algorithm
from .nx_assign_colors_to_nodes_by_group_attribute import nx_assign_colors_to_nodes_by_group_attribute
from .nx_assign_opacity_to_text_based_on_frequency import nx_assign_opacity_to_text_based_on_frequency
from .nx_assign_sizes_to_nodes_based_on_occurrences import nx_assign_sizes_to_nodes_based_on_occurrences
from .nx_assign_text_positions_to_nodes_by_quadrants import nx_assign_text_positions_to_nodes_by_quadrants
from .nx_assign_textfont_sizes_to_nodes_based_on_occurrences import nx_assign_textfont_sizes_to_nodes_based_on_occurrences
from .nx_assign_uniform_color_to_edges import nx_assign_uniform_color_to_edges
from .nx_assign_widths_to_edges_based_on_weight import nx_assign_widths_to_edges_based_on_weight
from .nx_compute_spring_layout_positions import nx_compute_spring_layout_positions


def nx_create_coupling_graph(
    #
    # FUNCTION PARAMS:
    unit_of_analysis,
    #
    # COLUMN PARAMS:
    top_n=None,
    citations_threshold=0,
    occurrence_threshold=2,
    custom_items=None,
    #
    # NETWORK CLUSTERING:
    algorithm_or_dict="louvain",
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
    edge_color="#7793a5",
    edge_width_range=(0.8, 3.0),
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    #
    # Create the networkx graph
    nx_graph = nx.Graph()

    nx_graph = __add_weighted_edges_from(
        nx_graph=nx_graph,
        unit_of_analysis=unit_of_analysis,
        #
        # COLUMN PARAMS:
        top_n=top_n,
        citations_threshold=citations_threshold,
        occurrence_threshold=occurrence_threshold,
        custom_items=custom_items,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    for node in nx_graph.nodes():
        nx_graph.nodes[node]["text"] = node
    #
    # Cluster the networkx graph
    if isinstance(algorithm_or_dict, str):
        nx_graph = nx_apply_cdlib_algorithm(nx_graph, algorithm_or_dict)
    if isinstance(algorithm_or_dict, dict):
        nx_graph = __assign_group_from_dict(nx_graph, algorithm_or_dict)

    #
    # Sets the layout
    nx_graph = nx_compute_spring_layout_positions(nx_graph, nx_k, nx_iterations, nx_random_state)

    #
    # Sets the node attributes
    nx_graph = nx_assign_colors_to_nodes_by_group_attribute(nx_graph)

    # nx_graph = nx_compute_node_degree(nx_graph)
    # nx_graph = nx_compute_node_size_from_node_degree(nx_graph, node_size_range)
    # nx_graph = nx_compute_textfont_size_from_node_degree(nx_graph, textfont_size_range)
    # nx_graph = nx_compute_textfont_opacity_from_node_degree(
    #     nx_graph, textfont_opacity_range
    # )
    nx_graph = nx_assign_sizes_to_nodes_based_on_occurrences(nx_graph, node_size_range)
    nx_graph = nx_assign_textfont_sizes_to_nodes_based_on_occurrences(nx_graph, textfont_size_range)
    nx_graph = nx_assign_opacity_to_text_based_on_frequency(nx_graph, textfont_opacity_range)

    #
    # Sets the edge attributes
    nx_graph = nx_assign_widths_to_edges_based_on_weight(nx_graph, edge_width_range)
    nx_graph = nx_assign_text_positions_to_nodes_by_quadrants(nx_graph)
    nx_graph = nx_assign_uniform_color_to_edges(nx_graph, edge_color)

    return nx_graph


def __add_weighted_edges_from(
    nx_graph,
    unit_of_analysis,
    #
    # COLUMN PARAMS:
    top_n=None,
    citations_threshold=0,
    occurrence_threshold=2,
    custom_items=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    records = read_filtered_database(
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    #
    data_frame = records[[unit_of_analysis, "global_references"]]
    data_frame = data_frame.dropna()
    data_frame[unit_of_analysis] = data_frame[unit_of_analysis].str.split("; ").map(lambda x: [y.strip() for y in x])
    data_frame["global_references"] = data_frame["global_references"].str.split(";").map(lambda x: [y.strip() for y in x])

    data_frame = data_frame.explode(unit_of_analysis)
    data_frame = data_frame.explode("global_references")

    data_frame = data_frame.groupby(["global_references"], as_index=True).agg({unit_of_analysis: list})

    data_frame.columns = ["row"]
    data_frame["column"] = data_frame.row.copy()

    data_frame = data_frame.explode("row")
    data_frame = data_frame.explode("column")
    data_frame = data_frame.loc[data_frame.row != data_frame.column, :]
    data_frame = data_frame.groupby(["row", "column"], as_index=False).size()

    #
    # Filter the data

    metrics = performance_metrics(
        #
        # ITEMS PARAMS:
        field=unit_of_analysis,
        metric="OCC",
        #
        # ITEM FILTERS:
        top_n=top_n,
        occ_range=(occurrence_threshold, None),
        gc_range=(citations_threshold, None),
        custom_items=custom_items,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    ).df_

    data_frame = data_frame.loc[data_frame.row.isin(metrics.index), :]
    data_frame = data_frame.loc[data_frame.column.isin(metrics.index), :]

    #
    # Adds the counters to the data frame:
    data_frame.index = data_frame.row.values
    data_frame = append_occurrences_and_citations_to_axis(
        dataframe=data_frame,
        axis=0,
        field=unit_of_analysis,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
    data_frame["row"] = data_frame.index.values

    #
    # Adds the counters to the data frame:
    data_frame.index = data_frame.column.values
    data_frame = append_occurrences_and_citations_to_axis(
        dataframe=data_frame,
        axis=0,
        field=unit_of_analysis,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
    data_frame["column"] = data_frame.index.values

    #
    #
    data_frame.index = np.arange(len(data_frame))

    #
    # Adds the data to the network:
    for _, row in data_frame.iterrows():
        nx_graph.add_weighted_edges_from(
            ebunch_to_add=[(row.row, row.column, row["size"])],
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
