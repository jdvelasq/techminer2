# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

import networkx as nx
import numpy as np

from ..read_filtered_database import read_filtered_database
from .assign_colors_to_nodes_by_group_attribute import assign_colors_to_nodes_by_group_attribute
from .assign_opacity_to_text_based_on_citations import assign_opacity_to_text_based_on_citations
from .assign_sizes_to_nodes_based_on_citations import assign_sizes_to_nodes_based_on_citations
from .assign_text_positions_to_nodes_by_quadrants import assign_text_positions_to_nodes_by_quadrants
from .assign_textfont_sizes_to_nodes_based_on_citations import assign_textfont_sizes_to_nodes_based_on_citations
from .assign_uniform_color_to_edges import assign_uniform_color_to_edges
from .assign_widths_to_edges_based_on_weight import assign_widths_to_edges_based_on_weight
from .compute_spring_layout_positions import compute_spring_layout_positions
from .nx_apply_cdlib_algorithm import nx_apply_cdlib_algorithm


def create_co_citation_graph(
    #
    # FUNCTION PARAMS:
    unit_of_analysis,
    #
    # COLUMN PARAMS:
    top_n=None,
    citations_threshold=None,
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
        custom_items=custom_items,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    if unit_of_analysis == "cited_references":
        for node in nx_graph.nodes():
            nx_graph.nodes[node]["text"] = ", ".join(node.split(", ")[:2])

    else:
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
    nx_graph = compute_spring_layout_positions(nx_graph, nx_k, nx_iterations, nx_random_state)

    #
    # Sets the node attributes
    # nx_graph = nx_compute_node_degree(nx_graph)

    nx_graph = assign_colors_to_nodes_by_group_attribute(nx_graph)

    nx_graph = assign_sizes_to_nodes_based_on_citations(
        nx_graph,
        node_size_range,
    )
    nx_graph = assign_textfont_sizes_to_nodes_based_on_citations(
        nx_graph,
        textfont_size_range,
    )
    nx_graph = assign_opacity_to_text_based_on_citations(
        nx_graph,
        textfont_opacity_range,
    )

    #
    # Sets the edge attributes
    nx_graph = assign_widths_to_edges_based_on_weight(
        nx_graph,
        edge_width_range,
    )
    nx_graph = assign_text_positions_to_nodes_by_quadrants(nx_graph)
    nx_graph = assign_uniform_color_to_edges(nx_graph, edge_color)

    return nx_graph


def __add_weighted_edges_from(
    nx_graph,
    unit_of_analysis,
    #
    # COLUMN PARAMS:
    top_n=None,
    citations_threshold=None,
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

    matrix_list = records[["global_references"]].dropna().copy()
    matrix_list = matrix_list.rename(columns={"global_references": "column"})
    matrix_list = matrix_list.assign(row=records[["global_references"]])

    for name in ["column", "row"]:
        matrix_list[name] = matrix_list[name].str.split(";")
        matrix_list = matrix_list.explode(name)
        matrix_list[name] = matrix_list[name].str.strip()

    if unit_of_analysis == "cited_authors":
        matrix_list["row"] = matrix_list["row"].str.split(", ").map(lambda x: x[0])
        matrix_list["column"] = matrix_list["column"].str.split(", ").map(lambda x: x[0])
    elif unit_of_analysis == "cited_sources":
        matrix_list["row"] = matrix_list["row"].str.split(", ").map(lambda x: x[2])
        matrix_list["column"] = matrix_list["column"].str.split(", ").map(lambda x: x[2])
    elif unit_of_analysis == "cited_references":
        matrix_list["row"] = matrix_list["row"].str.split(", ").map(lambda x: x[:3]).str.join(", ")
        matrix_list["column"] = matrix_list["column"].str.split(", ").map(lambda x: x[:3]).str.join(", ")
    else:
        raise ValueError("Bad unit_of_analysis")

    matrix_list = matrix_list.loc[matrix_list.apply(lambda x: x.row != x.column, axis=1), :]

    matrix_list["OCC"] = 1
    matrix_list = matrix_list.groupby(["row", "column"], as_index=False).aggregate("sum")

    matrix_list = matrix_list.sort_values(["OCC", "row", "column"], ascending=[False, True, True])

    #
    # Computes valild items
    valid_items = __compute_valid_items(
        unit_of_analysis=unit_of_analysis,
        records=records,
        top_n=top_n,
        citations_threshold=citations_threshold,
        custom_items=custom_items,
    )

    #
    # Filter data
    matrix_list = matrix_list.loc[matrix_list.row.isin(valid_items["index"].to_list()), :]
    matrix_list = matrix_list.loc[matrix_list.column.isin(valid_items["index"].to_list()), :]

    #
    # Adds citations
    max_citations = valid_items.citations.max()
    n_zeros = int(np.log10(max_citations - 1)) + 1
    fmt = " 1:{:0" + str(n_zeros) + "d}"

    #
    # Rename the items adding the citations
    rename_dict = {
        key: value
        for key, value in zip(
            valid_items["index"].to_list(),
            (valid_items["index"] + valid_items["citations"].map(fmt.format)).to_list(),
        )
    }
    matrix_list["row"] = matrix_list["row"].map(rename_dict)
    matrix_list["column"] = matrix_list["column"].map(rename_dict)

    #
    # Adds the data to the network:
    for _, x in matrix_list.iterrows():
        nx_graph.add_weighted_edges_from(
            ebunch_to_add=[(x.row, x.column, x.size)],
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


def __compute_valid_items(
    unit_of_analysis,
    records,
    top_n,
    citations_threshold,
    custom_items,
):
    if custom_items is not None:
        return custom_items

    #
    # Creates a list with global references
    global_references = records["global_references"].dropna().copy()
    global_references = global_references.str.split(";")
    global_references = global_references.explode()
    global_references = global_references.str.strip()

    #
    # Transforms each reference into the element of interest
    if unit_of_analysis == "cited_authors":
        global_references = global_references.str.split(", ").map(lambda x: x[0])
    elif unit_of_analysis == "cited_sources":
        global_references = global_references.str.split(", ").map(lambda x: x[2])
    elif unit_of_analysis == "cited_references":
        global_references = global_references.str.split(", ").map(lambda x: x[:3]).str.join(", ")
    else:
        raise ValueError("Bad unit_of_analysis")

    #
    # Counts the number of appareances of each element of interest
    valid_items = global_references.value_counts().to_frame()
    valid_items.columns = ["citations"]
    valid_items = valid_items.reset_index()
    valid_items = valid_items.sort_values(["citations", "index"], ascending=[False, True])

    #
    # Applies the filters
    if top_n is not None:
        valid_items = valid_items.head(top_n)
    if citations_threshold is not None:
        valid_items = valid_items.loc[valid_items.citations >= citations_threshold]

    #
    # Returns the selected elements as a list
    return valid_items
