"""This module contains functions for network analysis that are common to
several modules.


"""

from collections import defaultdict

import networkx as nx
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from cdlib import algorithms

from .list_cells_in_matrix import (
    AutoCorrCellsList,
    CoocCellsList,
    list_cells_in_matrix,
)
from .read_records import read_records

CLUSTER_COLORS = (
    px.colors.qualitative.Dark24
    + px.colors.qualitative.Light24
    + px.colors.qualitative.Pastel1
    + px.colors.qualitative.Pastel2
    + px.colors.qualitative.Set1
    + px.colors.qualitative.Set2
    + px.colors.qualitative.Set3
)


# =============================================================================
def nx_create_graph_from_matrix(
    matrix,
    node_size_min=30,
    node_size_max=70,
    textfont_size_min=10,
    textfont_size_max=20,
):
    """Creates a networkx graph from a matrix list."""

    graph = nx.Graph()

    graph = nx_add_nodes__to_graph_from_matrix(graph, matrix)
    graph = nx_create_node_occ_property_from_node_name(graph)
    graph = nx_compute_node_property_from_occ(
        graph, "node_size", node_size_min, node_size_max
    )
    graph = nx_compute_node_property_from_occ(
        graph, "textfont_size", textfont_size_min, textfont_size_max
    )

    graph = nx_add_edges_to_graph_from_matrix(graph, matrix)

    return graph


def nx_add_nodes__to_graph_from_matrix(graph, matrix):
    """Creates nodes from 'row' and 'column' columns in a matrix list."""

    # Adds the items in 'row' column as nodes
    nodes = matrix.df_.index.to_list()
    nodes = [
        (node, {"group": 0, "color": "#8da4b4", "textfont_color": "black"})
        for node in nodes
    ]
    graph.add_nodes_from(nodes)

    if matrix.rows_ != matrix.columns_:
        # Adds the items in 'column' column as nodes
        nodes = matrix.df_.columns.to_list()
        nodes = [
            (node, {"group": 1, "color": "#556f81", "textfont_color": "black"})
            for node in nodes
        ]
        graph.add_nodes_from(nodes)

    return graph


def nx_add_edges_to_graph_from_matrix(graph, matrix):
    """Creates edges from 'row' and 'column' columns in a matrix list."""

    matrix_list = list_cells_in_matrix(matrix)
    return nx_add_edges_to_graph_from_matrix_list(graph, matrix_list)


def nx_add_edges_to_graph_from_matrix_list(graph, matrix_list):
    """Creates edges from 'row' and 'column' columns in a matrix list."""

    table = matrix_list.df_.copy()

    if isinstance(matrix_list, AutoCorrCellsList):
        table = table[table["row"] < table["column"]]
        table = table.loc[table.CORR > 0, :]

    elif isinstance(matrix_list, CoocCellsList):
        table = table[table["row"] < table["column"]]
        table = table.loc[table.OCC > 0, :]

    else:
        table = table[table[matrix_list.metric_] > 0]

    for _, row in table.iterrows():
        graph.add_edges_from(
            [(row[0], row[1])],
            value=row[2],
            width=2,
            dash="solid",
            color="#8da4b4",
        )

    return graph


# =============================================================================
#
#
# Functions for manipulating networkx graphs
#
#


def nx_create_graph_from_matrix_list(
    matrix_list,
    node_size_min=30,
    node_size_max=70,
    textfont_size_min=10,
    textfont_size_max=20,
):
    """Creates a networkx graph from a matrix list."""

    graph = nx.Graph()

    graph = nx_add_nodes__to_graph_from_matrix_list(graph, matrix_list)
    graph = nx_create_node_occ_property_from_node_name(graph)
    graph = nx_compute_node_property_from_occ(
        graph, "node_size", node_size_min, node_size_max
    )
    graph = nx_compute_node_property_from_occ(
        graph, "textfont_size", textfont_size_min, textfont_size_max
    )

    graph = nx_add_edges_to_graph_from_matrix_list(graph, matrix_list)

    return graph


def nx_add_nodes__to_graph_from_matrix_list(graph, matrix_list):
    """Creates nodes from 'row' and 'column' columns in a matrix list."""

    # adds items in 'row' column as nodes
    nodes = matrix_list.df_["row"].drop_duplicates().to_list()
    nodes = [
        (node, {"group": 0, "color": "#8da4b4", "textfont_color": "black"})
        for node in nodes
    ]
    graph.add_nodes_from(nodes)

    # adds items in 'column' column as nodes
    candidates = matrix_list.df_["column"].drop_duplicates().to_list()
    nodes = []
    for candidate in candidates:
        if candidate not in graph.nodes:
            nodes.append(candidate)
    if len(nodes) > 0:
        nodes = [
            (node, {"group": 1, "color": "#556f81", "textfont_color": "black"})
            for node in nodes
        ]
        graph.add_nodes_from(nodes)

    return graph


def nx_create_node_occ_property_from_node_name(graph):
    """Adds OCC value as a property of the node in a graph."""

    for node in graph.nodes():
        occ = node.split(" ")[-1]
        occ = occ.split(":")[0]
        occ = int(occ)
        graph.nodes[node]["OCC"] = occ

    return graph


def nx_apply_community_detection_method(graph, method):
    """Network community detection."""

    algorithm = {
        "label_propagation": algorithms.label_propagation,
        "leiden": algorithms.leiden,
        "louvain": algorithms.louvain,
        "walktrap": algorithms.walktrap,
    }[method]

    # applies the community detection method
    if method == "label_propagation":
        communities = algorithm(graph).communities
    elif method == "leiden":
        communities = algorithm(graph).communities
    elif method == "louvain":
        communities = algorithm(graph, randomize=False).communities
    elif method == "walktrap":
        communities = algorithm(graph).communities

    # assigns the community to each node
    for i_community, community in enumerate(communities):
        for node in community:
            graph.nodes[node]["group"] = i_community

    return graph


def nx_compute_circular_layout(graph):
    """Computes a circular layout with the last node as center"""

    pos = nx.circular_layout(graph)
    last_node = list(graph.nodes())[-1]
    for node in graph.nodes():
        if node == last_node:
            graph.nodes[node]["pos"] = [0, 0]
        else:
            graph.nodes[node]["pos"] = pos[node]

    return graph


def nx_compute_spectral_layout(graph, scale):
    """Computes the layout of a networkx graph."""
    pos = nx.spectral_layout(graph, scale=scale)
    for node in graph.nodes():
        graph.nodes[node]["pos"] = pos[node]
    return graph


def nx_compute_spring_layout(graph, k, iterations, seed):
    """Computes the layout of a networkx graph."""
    pos = nx.spring_layout(graph, k=k, iterations=iterations, seed=seed)
    for node in graph.nodes():
        graph.nodes[node]["pos"] = pos[node]
    return graph


def nx_compute_node_degree(graph):
    """Computes the degree of each node in a networkx graph."""

    for node, adjacencies in graph.adjacency():
        graph.nodes[node]["degree"] = len(adjacencies)

    return graph


# pylint: disable=invalid-name
def nx_compute_node_statistics(graph):
    """Compute network statistics."""

    nodes = list(graph.nodes())
    degree = [graph.nodes[node]["degree"] for node in nodes]
    occ = [graph.nodes[node]["OCC"] for node in nodes]
    occ_gc = [node.split(" ")[-1] for node in nodes]
    gc = [int(text.split(":")[-1]) for text in occ_gc]
    betweenness = nx.betweenness_centrality(graph)
    closeness = nx.closeness_centrality(graph)
    pagerank = nx.pagerank(graph)

    # Callon centrality  - density
    callon_matrix = nx_graph_to_co_occ_matrix(graph).astype(float)
    callon_centrality = callon_matrix.values.diagonal()
    callon_density = callon_matrix.sum() - callon_centrality

    # strategic_diagram["callon_centrality"] *= 10
    # strategic_diagram["callon_density"] *= 100

    indicators = pd.DataFrame(
        {
            "Degree": degree,
            "Betweenness": betweenness,
            "Closeness": closeness,
            "PageRank": pagerank,
            "Centrality": callon_centrality,
            "Density": callon_density,
            "_occ_": occ,
            "_gc_": gc,
            "_name_": nodes,
        },
        index=nodes,
    )

    indicators = indicators.sort_values(
        by=["Degree", "_occ_", "_gc_", "_name_"],
        ascending=[False, False, False, True],
    )

    indicators = indicators.drop(columns=["_occ_", "_gc_", "_name_"])

    return indicators


def nx_compute_node_textfont_color_from_occ(graph):
    """Computes the textfont color for each node in a networkx graph."""

    occ = [graph.nodes[node]["OCC"] for node in graph.nodes()]
    occ_scaled = nx_scale_node_occ(occ, max_size=1.0, min_size=0.40)
    colors = px.colors.sequential.Greys
    textfont_color = np.array(colors)[
        np.round(occ_scaled * (len(colors) - 1)).astype(int)
    ]

    for index, node in enumerate(graph.nodes()):
        graph.nodes[node]["textfont_color"] = textfont_color[index]

    return graph


def nx_compute_node_property_from_occ(graph, prop, min_size, max_size):
    """Compute key size for a networkx graph from OCC property of the node."""

    if min_size == max_size:
        for index, node in enumerate(graph.nodes()):
            graph.nodes[node][prop] = min_size
        return graph

    occ = [graph.nodes[node]["OCC"] for node in graph.nodes()]

    occ_scaled = nx_scale_node_occ(occ, max_size, min_size)

    for index, node in enumerate(graph.nodes()):
        graph.nodes[node][prop] = occ_scaled[index]

    return graph


def nx_compute_textposition_from_graph(graph):
    """Computes the text position for a node in a networkx graph."""

    node_x, node_y = nx_extract_node_coordinates(graph)

    return nx_compute_node_textposition_from_node_coordinates(node_x, node_y)


def nx_compute_node_textposition_from_node_coordinates(node_x, node_y):
    """Computes the text positon for a node from its x and y coordinates."""

    x_mean = np.mean(node_x)
    y_mean = np.mean(node_y)

    textposition = []

    for x_pos, y_pos in zip(node_x, node_y):
        if x_pos >= x_mean and y_pos >= y_mean:
            textposition.append("top right")
        if x_pos <= x_mean and y_pos >= y_mean:
            textposition.append("top left")
        if x_pos <= x_mean and y_pos <= y_mean:
            textposition.append("bottom left")
        if x_pos >= x_mean and y_pos <= y_mean:
            textposition.append("bottom right")

    return textposition


def nx_extract_communities(graph, conserve_counters):
    """Gets communities from a networkx graph as a dictionary."""

    communities = {}

    for node, data in graph.nodes(data=True):
        text = f"CL_{data['group'] :02d}"
        if text not in communities:
            communities[text] = []
        if conserve_counters is False:
            node = " ".join(node.split(" ")[:-1])
        communities[text].append(node)

    return communities


def nx_extract_node_textfont_colors(graph):
    """Extracts textfont colors from a networkx graph."""

    textfont_colors = []
    for node in graph.nodes():
        textfont_colors.append(graph.nodes[node]["textfont_color"])

    return textfont_colors


def nx_extract_node_textfont_sizes(graph):
    """Extracts textfont sizes from a networkx graph."""

    textfont_sizes = []
    for node in graph.nodes():
        textfont_sizes.append(graph.nodes[node]["textfont_size"])

    return textfont_sizes


def nx_extract_node_colors(graph):
    """Extracts node colors from a networkx graph."""

    node_colors = []
    for node in graph.nodes():
        node_colors.append(graph.nodes[node]["color"])

    return node_colors


def nx_extract_node_coordinates(graph):
    """Extracts node coordinates from a networkx graph."""

    node_x = []
    node_y = []
    for node in graph.nodes():
        pos_x, pos_y = graph.nodes[node]["pos"]
        node_x.append(pos_x)
        node_y.append(pos_y)

    return node_x, node_y


def nx_extract_node_names(graph):
    """Extracts node names from a networkx graph."""

    node_names = []
    for node in graph.nodes():
        node_names.append(node)

    return node_names


def nx_extract_node_sizes(graph):
    """Extracts node sizes from a networkx graph."""

    node_sizes = []
    for node in graph.nodes():
        if "node_size" not in graph.nodes[node]:
            raise ValueError(
                f"Node {node} does not have a node_size property."
            )
        node_sizes.append(graph.nodes[node]["node_size"])

    return node_sizes


def nx_extract_node_occ(graph):
    """Extracts node sizes from a networkx graph."""

    occ = []
    for node in graph.nodes():
        if "OCC" not in graph.nodes[node]:
            raise ValueError(
                f"Node {node} does not have a node_size property."
            )
        occ.append(graph.nodes[node]["OCC"])

    return occ


def nx_node_occ_to_node_textfont_color(occ):
    """Computes the textfont color from an OCC list."""
    occ_scaled = nx_scale_node_occ(occ, max_size=1.0, min_size=0.35)
    colors = px.colors.sequential.Greys
    textfont_color = np.array(colors)[
        np.round(occ_scaled * (len(colors) - 1)).astype(int)
    ]
    return textfont_color


def nx_scale_node_occ(occ, max_size, min_size):
    """Scales the OCC values to a range of sizes."""

    occ = np.array(occ)
    min_occ = occ.min()
    occ = occ - min_occ + min_size
    max_value = occ.max()
    if max_value > max_size:
        occ = min_size + (occ - min_size) / (max_value - min_size) * (
            max_size - min_size
        )
    return occ


def nx_set_node_color_by_group(graph):
    """Modifies the color of the nodes according to the group."""

    groups = []
    for node in graph.nodes():
        groups.append(graph.nodes[node]["group"])
    n_groups = len(set(groups))

    if n_groups in [1, 2]:
        return graph

    for node in graph.nodes():
        group = graph.nodes[node]["group"]
        graph.nodes[node]["color"] = CLUSTER_COLORS[group]

    return graph


def nx_graph_to_co_occ_matrix(graph):
    """Reconstructs the co-occurrence matrix from a graph."""

    matrix = nx.to_pandas_adjacency(graph)
    matrix = matrix.astype(int)
    matrix.loc[:, :] = 0

    for node in graph.nodes():
        matrix.loc[node, node] = graph.nodes[node]["OCC"]

    for edge in graph.edges():
        matrix.loc[edge[0], edge[1]] = graph.edges[edge]["value"]
        matrix.loc[edge[1], edge[0]] = graph.edges[edge]["value"]

    return matrix


def nx_set_node_colors(graph, node_names, new_color):
    """Sets node colors in a networkx graph."""

    for node in graph.nodes():
        if node in node_names:
            graph.nodes[node]["color"] = new_color

    return graph


def nx_set_edge_properties_for_corr_maps(graph, color):
    """Sets edge properties for correlation maps."""

    for edge in graph.edges():
        if graph.edges[edge]["value"] < 0.25:
            graph.edges[edge]["width"] = 2
            graph.edges[edge]["dash"] = "dot"
            graph.edges[edge]["color"] = color

        elif graph.edges[edge]["value"] < 0.5:
            graph.edges[edge]["width"] = 2
            graph.edges[edge]["dash"] = "solid"
            graph.edges[edge]["color"] = color

        elif graph.edges[edge]["value"] < 0.75:
            graph.edges[edge]["width"] = 4
            graph.edges[edge]["dash"] = "solid"
            graph.edges[edge]["color"] = color

        else:
            graph.edges[edge]["width"] = 6
            graph.edges[edge]["dash"] = "solid"
            graph.edges[edge]["color"] = color

    return graph


def nx_set_edge_properties_for_co_occ_networks(graph):
    """Sets edge properties for co-occurrence networks."""

    for edge in graph.edges():
        graph.edges[edge]["width"] = 1
        graph.edges[edge]["color"] = "lightgray"

    graph = nx_compute_node_textfont_color_from_occ(graph)

    return graph


###############################################################################


def px_create_edge_traces(graph):
    """Creates edge traces for a networkx graph."""

    edge_traces = []

    for edge in graph.edges():
        pos_x0, pos_y0 = graph.nodes[edge[0]]["pos"]
        pos_x1, pos_y1 = graph.nodes[edge[1]]["pos"]
        color = graph.edges[edge]["color"]
        dash = graph.edges[edge]["dash"]
        width = graph.edges[edge]["width"]

        edge_trace = go.Scatter(
            x=(pos_x0, pos_x1),
            y=(pos_y0, pos_y1),
            line={"color": color, "dash": dash, "width": width},
            hoverinfo="none",
            mode="lines",
        )

        edge_traces.append(edge_trace)

    return edge_traces


def px_create_node_trace(graph):
    """Creates a node trace for a networkx graph."""

    node_x, node_y = nx_extract_node_coordinates(graph)
    node_colors = nx_extract_node_colors(graph)
    node_sizes = nx_extract_node_sizes(graph)
    node_names = nx_extract_node_names(graph)
    node_trace = go.Scatter(
        x=node_x,
        y=node_y,
        mode="markers",
        text=node_names,
        hoverinfo="text",
        marker={
            "color": node_colors,
            "size": node_sizes,
            "line": {"width": 1.5, "color": "white"},
            "opacity": 1.0,
        },
    )

    return node_trace


def px_create_network_fig(
    edge_traces,
    node_trace,
    xaxes_range,
    yaxes_range,
    show_axes,
):
    """Creates a network graph from tracesusing plotly express."""

    layout = go.Layout(
        title="",
        titlefont=dict(size=16),
        showlegend=False,
        hovermode="closest",
        margin={"b": 0, "l": 0, "r": 0, "t": 0},
        annotations=[
            {
                "text": "",
                "showarrow": False,
                "xref": "paper",
                "yref": "paper",
                "x": 0.005,
                "y": -0.002,
                "align": "left",
                "font": {"size": 10},
            }
        ],
    )

    fig = go.Figure(
        data=edge_traces + [node_trace],
        layout=layout,
    )

    if show_axes is False:
        fig.update_layout(
            xaxis={
                "showgrid": False,
                "zeroline": False,
                "showticklabels": False,
            },
            yaxis={
                "showgrid": False,
                "zeroline": False,
                "showticklabels": False,
            },
        )

    if xaxes_range is not None:
        fig.update_xaxes(range=xaxes_range)

    if yaxes_range is not None:
        fig.update_yaxes(range=yaxes_range)

    fig.update_layout(
        hoverlabel={
            "bgcolor": "white",
            "font_family": "monospace",
        },
        paper_bgcolor="white",
        plot_bgcolor="white",
    )

    return fig


# pylint: disable=too-many-locals
def px_add_names_to_fig_nodes(fig, graph, n_labels, is_article):
    """Adds node names to a network figure."""

    node_x, node_y = nx_extract_node_coordinates(graph)
    node_names = nx_extract_node_names(graph)
    textfont_sizes = nx_extract_node_textfont_sizes(graph)
    textposition = nx_compute_textposition_from_graph(graph)
    node_occs = nx_extract_node_occ(graph)

    node_citations = [int(name.split(":")[1]) for name in node_names]

    frame = pd.DataFrame(
        {
            "name": node_names,
            "occ": node_occs,
            "citation": node_citations,
        }
    )
    frame = frame.sort_values(["occ", "citation", "name"], ascending=False)
    selected_names = frame["name"].tolist()[:n_labels]

    if n_labels is None:
        n_labels = len(node_names)

    #
    node_x.reverse()
    node_y.reverse()
    node_names.reverse()
    textfont_sizes.reverse()
    textposition.reverse()
    node_occs.reverse()
    #

    # i_label = 0
    for pos_x, pos_y, name, textfont_size, textpos, node_occ in zip(
        node_x, node_y, node_names, textfont_sizes, textposition, node_occs
    ):
        # if node_occ >= occ_min:
        #     if i_label >= n_labels:
        #         break
        #     i_label += 1
        # else:
        #     continue

        if name not in selected_names:
            continue

        if textpos == "top right":
            xanchor = "left"
            yanchor = "bottom"
            xshift = 4
            yshift = 4
        elif textpos == "top left":
            xanchor = "right"
            yanchor = "bottom"
            xshift = -4
            yshift = 4
        elif textpos == "bottom right":
            xanchor = "left"
            yanchor = "top"
            xshift = 4
            yshift = -4
        elif textpos == "bottom left":
            xanchor = "right"
            yanchor = "top"
            xshift = -4
            yshift = -4
        else:
            xanchor = "center"
            yanchor = "center"

        if is_article is True:
            name = ", ".join(name.split(", ")[:2])

        fig.add_annotation(
            x=pos_x,
            y=pos_y,
            text=name,
            showarrow=False,
            # textangle=-90,
            # yanchor="bottom",
            font={"size": textfont_size},
            # yshift=yshift,
            bordercolor="grey",
            bgcolor="white",
            xanchor=xanchor,
            yanchor=yanchor,
            xshift=xshift,
            yshift=yshift,
        )

    return fig


###############################################################################


# pylint: disable=too-many-arguments
def extract_records_per_cluster(
    communities,
    field,
    # Database params:
    root_dir,
    database,
    year_filter,
    cited_by_filter,
    **filters,
):
    """Return a dictionary of records per cluster."""

    def convert_cluster_to_items_dict(communities):
        """Converts the cluster to items dict."""

        items2cluster = {}
        for cluster, items in communities.items():
            for item in items:
                items2cluster[item] = cluster

        return items2cluster

    def explode_field(records, field):
        """Explodes records."""

        records = records.copy()
        records = records[field]
        records = records.dropna()
        records = records.str.split("; ").explode().map(lambda w: w.strip())

        return records

    def select_valid_records(records, clusters):
        """Selects valid records."""

        community_terms = []
        for cluster in clusters.values():
            community_terms.extend(cluster)

        records = records.copy()
        records = records[records.isin(community_terms)]

        return records

    def create_raw_cluster_field(records, field, clusters):
        """Adds a cluster field with non unique elements."""

        records = records.to_frame()
        records["clusters"] = records[field].map(clusters)
        # records["article"] = records.index.to_list()
        records = records.groupby("article").agg({"clusters": list})
        records["clusters"] = (
            records["clusters"].apply(lambda x: sorted(x)).str.join("; ")
        )

        return records

    def compute_cluster(list_of_clusters):
        """Computes the cluster most frequent in a list."""

        counter = defaultdict(int)
        for cluster in list_of_clusters:
            counter[cluster] += 1
        return max(counter, key=counter.get)

    #
    # Main code:
    #

    records_main = read_records(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
    records_main.index = pd.Index(records_main.article)

    items2cluster = convert_cluster_to_items_dict(communities)
    exploded_records = explode_field(records_main, field)
    selected_records = select_valid_records(exploded_records, communities)
    selected_records = create_raw_cluster_field(
        selected_records, field, items2cluster
    )

    records_main = read_records(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
    records_main.index = pd.Index(records_main.article)

    records_main["_RAW_CLUSTERS_"] = pd.NA
    records_main.loc[records_main.index, "_RAW_CLUSTERS_"] = selected_records[
        "clusters"
    ]
    records_main["_CLUSTERS_"] = records_main["_RAW_CLUSTERS_"]
    records_main = records_main.dropna(subset=["_CLUSTERS_"])
    records_main["_CLUSTERS_"] = (
        records_main["_CLUSTERS_"]
        .str.split("; ")
        .map(lambda x: [z.strip() for z in x])
        .map(set)
        .str.join("; ")
    )

    records_main["_ASSIGNED_CLUSTER_"] = (
        records_main["_RAW_CLUSTERS_"]
        .str.split("; ")
        .map(lambda x: [z.strip() for z in x])
        .map(compute_cluster)
    )

    clusters = (
        records_main["_ASSIGNED_CLUSTER_"].dropna().drop_duplicates().to_list()
    )

    records_per_cluster = dict()

    for cluster in clusters:
        clustered_records = records_main[
            records_main._ASSIGNED_CLUSTER_ == cluster
        ].copy()
        clustered_records = clustered_records.sort_values(
            ["global_citations", "local_citations"],
            ascending=[False, False],
        )

        records_per_cluster[cluster] = clustered_records.copy()

    return records_per_cluster


# def generate_clusters_database(
#     communities,
#     field,
#     # Database params:
#     root_dir,
#     database,
#     year_filter,
#     cited_by_filter,
#     **filters,
# ):
#     """Generates the file root_dir/databases/_CLUSTERS_.csv"""

#     def convert_cluster_to_items_dict(communities):
#         """Converts the cluster to items dict."""

#         items2cluster = {}
#         for cluster, items in communities.items():
#             for item in items:
#                 items2cluster[item] = cluster

#         return items2cluster

#     def explode_field(records, field):
#         """Explodes records."""

#         records = records.copy()
#         records = records[field]
#         records = records.dropna()
#         records = records.str.split("; ").explode().map(lambda w: w.strip())

#         return records

#     def select_valid_records(records, clusters):
#         """Selects valid records."""

#         community_terms = []
#         for cluster in clusters.values():
#             community_terms.extend(cluster)

#         records = records.copy()
#         records = records[records.isin(community_terms)]

#         return records

#     def create_raw_cluster_field(records, field, clusters):
#         """Adds a cluster field with non unique elements."""

#         records = records.to_frame()
#         records["clusters"] = records[field].map(clusters)
#         # records["article"] = records.index.to_list()
#         records = records.groupby("article").agg({"clusters": list})
#         records["clusters"] = (
#             records["clusters"].apply(lambda x: sorted(x)).str.join("; ")
#         )

#         return records

#     #
#     # Main code:
#     #

#     records = read_records(
#         root_dir=root_dir,
#         database=database,
#         year_filter=year_filter,
#         cited_by_filter=cited_by_filter,
#         **filters,
#     )
#     records.index = records.article

#     items2cluster = convert_cluster_to_items_dict(communities)
#     exploded_records = explode_field(records, field)
#     selected_records = select_valid_records(exploded_records, communities)
#     selected_records = create_raw_cluster_field(
#         selected_records, field, items2cluster
#     )

#     records = read_records(
#         root_dir=root_dir,
#         database=database,
#         year_filter=year_filter,
#         cited_by_filter=cited_by_filter,
#         **filters,
#     )
#     records.index = records.article

#     records["_RAW_CLUSTERS_"] = pd.NA
#     records.loc[records.index, "_RAW_CLUSTERS_"] = selected_records["clusters"]
#     records["_CLUSTERS_"] = records["_RAW_CLUSTERS_"]
#     records = records.dropna(subset=["_CLUSTERS_"])
#     records["_CLUSTERS_"] = (
#         records["_CLUSTERS_"]
#         .str.split("; ")
#         .map(lambda x: [z.strip() for z in x])
#         .map(set)
#         .str.join("; ")
#     )

#     database_path = pathlib.Path(root_dir) / "databases" / "_CLUSTERS_.csv"

#     records.to_csv(database_path, index=False, encoding="utf-8")


# def --generate_databases_per_cluster(root_dir):
#     """Generates the files root_dir/databases/_CLUSTER_XX_.csv"""

#     def compute_cluster(list_of_clusters):
#         """Computes the cluster most frequent in a list."""

#         counter = defaultdict(int)
#         for cluster in list_of_clusters:
#             counter[cluster] += 1
#         return max(counter, key=counter.get)

#     #
#     # Main code:
#     #

#     records = read_records(
#         root_dir=root_dir,
#         database="_CLUSTERS_",
#     )

#     records["_ASSIGNED_CLUSTER_"] = (
#         records["_RAW_CLUSTERS_"]
#         .str.split("; ")
#         .map(lambda x: [z.strip() for z in x])
#         .map(compute_cluster)
#     )

#     clusters = (
#         records["_ASSIGNED_CLUSTER_"].dropna().drop_duplicates().to_list()
#     )

#     # Remove existent _CLUSTER_XX_.csv files:
#     database_dir = pathlib.Path(root_dir) / "databases"
#     files = list(database_dir.glob("_CLUSTER_*_.csv"))
#     for file in files:
#         os.remove(file)

#     for cluster in clusters:
#         clustered_records = records[records._ASSIGNED_CLUSTER_ == cluster]
#         clustered_records = clustered_records.sort_values(
#             ["global_citations", "local_citations"],
#             ascending=[False, False],
#         )

#         file_name = f"_CLUSTER_{cluster[-2:]}_.csv"
#         file_path = os.path.join(root_dir, "databases", file_name)
#         clustered_records.to_csv(file_path, index=False, encoding="utf-8")
