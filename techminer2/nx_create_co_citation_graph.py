# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

import networkx as nx

from ._read_records import read_records
from .nx_apply_cdlib_algorithm import nx_apply_cdlib_algorithm
from .nx_compute_edge_width_from_edge_weight import nx_compute_edge_width_from_edge_weight
from .nx_compute_node_degree import nx_compute_node_degree
from .nx_compute_node_size_from_node_degree import nx_compute_node_size_from_node_degree
from .nx_compute_spring_layout import nx_compute_spring_layout
from .nx_compute_textfont_opacity_from_node_degree import (
    nx_compute_textfont_opacity_from_node_degree,
)
from .nx_compute_textfont_size_from_node_degree import nx_compute_textfont_size_from_node_degree
from .nx_compute_textposition_from_graph import nx_compute_textposition_from_graph
from .nx_set_edge_color_to_constant import nx_set_edge_color_to_constant
from .nx_set_node_color_from_group_attr import nx_set_node_color_from_group_attr


def nx_create_co_citation_graph(
    #
    # FUNCTION PARAMS:
    unit_of_analysis,
    #
    # COLUMN PARAMS:
    top_n=None,
    citations_min=None,
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
    #
    # Create the networkx graph
    nx_graph = nx.Graph()

    nx_graph = __add_weighted_edges_from(
        nx_graph=nx_graph,
        unit_of_analysis=unit_of_analysis,
        #
        # COLUMN PARAMS:
        top_n=top_n,
        citations_min=citations_min,
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
    nx_graph = nx_compute_spring_layout(nx_graph, nx_k, nx_iterations, nx_random_state)

    #
    # Sets the node attributes
    nx_graph = nx_compute_node_degree(nx_graph)

    nx_graph = nx_set_node_color_from_group_attr(nx_graph)

    nx_graph = nx_compute_node_size_from_node_degree(nx_graph, node_size_min, node_size_max)
    nx_graph = nx_compute_textfont_size_from_node_degree(
        nx_graph, textfont_size_min, textfont_size_max
    )
    nx_graph = nx_compute_textfont_opacity_from_node_degree(
        nx_graph, textfont_opacity_min, textfont_opacity_max
    )

    #
    # Sets the edge attributes
    nx_graph = nx_compute_edge_width_from_edge_weight(nx_graph, edge_width_min, edge_width_max)
    nx_graph = nx_compute_textposition_from_graph(nx_graph)
    nx_graph = nx_set_edge_color_to_constant(nx_graph, edge_color)

    return nx_graph


def __add_weighted_edges_from(
    nx_graph,
    unit_of_analysis,
    #
    # COLUMN PARAMS:
    top_n=None,
    citations_min=None,
    custom_items=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    records = read_records(
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
        matrix_list["column"] = (
            matrix_list["column"].str.split(", ").map(lambda x: x[:3]).str.join(", ")
        )

    else:
        raise ValueError("Bad unit_of_analysis")

    matrix_list = matrix_list.loc[matrix_list.apply(lambda x: x.row != x.column, axis=1), :]

    matrix_list["OCC"] = 1
    matrix_list = matrix_list.groupby(["row", "column"], as_index=False).aggregate("sum")

    matrix_list = matrix_list.sort_values(["OCC", "row", "column"], ascending=[False, True, True])

    #
    # Filter the data
    valid_items = __compute_valid_items(
        unit_of_analysis=unit_of_analysis,
        records=records,
        top_n=top_n,
        citations_min=citations_min,
        custom_items=custom_items,
    )

    matrix_list = matrix_list.loc[matrix_list.row.isin(valid_items), :]
    matrix_list = matrix_list.loc[matrix_list.column.isin(valid_items), :]

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
    citations_min,
    custom_items,
):
    if custom_items is not None:
        return custom_items

    global_references = records["global_references"].dropna().copy()

    global_references = global_references.str.split(";")
    global_references = global_references.explode()
    global_references = global_references.str.strip()

    if unit_of_analysis == "cited_authors":
        global_references = global_references.str.split(", ").map(lambda x: x[0])

    elif unit_of_analysis == "cited_sources":
        global_references = global_references.str.split(", ").map(lambda x: x[2])

    elif unit_of_analysis == "cited_references":
        global_references = global_references.str.split(", ").map(lambda x: x[:3]).str.join(", ")

    else:
        raise ValueError("Bad unit_of_analysis")

    valid_items = global_references.value_counts().to_frame()
    valid_items.columns = ["citations"]
    valid_items = valid_items.reset_index()
    valid_items.sort_values(["citations", "index"], ascending=[False, True], inplace=True)

    if top_n is not None:
        valid_items = valid_items.head(top_n)

    if citations_min is not None:
        valid_items = valid_items.loc[valid_items.citations >= citations_min]

    return valid_items["index"].tolist()
