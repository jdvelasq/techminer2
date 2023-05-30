"""This module contains functions for network analysis that are common to
several modules.


"""
import networkx as nx
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from cdlib import algorithms


def apply_community_detection_method(graph, method):
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


COLORS = (
    px.colors.qualitative.Dark24
    + px.colors.qualitative.Light24
    + px.colors.qualitative.Pastel1
    + px.colors.qualitative.Pastel2
    + px.colors.qualitative.Set1
    + px.colors.qualitative.Set2
    + px.colors.qualitative.Set3
)


def set_color_nodes_by_group(graph):
    """Modifies the color of the nodes according to the group."""

    groups = []
    for node in graph.nodes():
        groups.append(graph.nodes[node]["group"])
    n_groups = len(set(groups))

    if n_groups in [1, 2]:
        return graph

    for node in graph.nodes():
        group = graph.nodes[node]["group"]
        graph.nodes[node]["color"] = COLORS[group]

    return graph


def create_graph(
    matrix_list,
    node_size_min=30,
    node_size_max=70,
    textfont_size_min=10,
    textfont_size_max=20,
):
    """Creates a networkx graph from a matrix list."""

    graph = nx.Graph()

    graph = create_graph_nodes(graph, matrix_list)
    graph = create_occ_node_property(graph)
    graph = compute_prop_sizes(
        graph, "node_size", node_size_min, node_size_max
    )
    graph = compute_prop_sizes(
        graph, "textfont_size", textfont_size_min, textfont_size_max
    )

    graph = create_graph_edges(graph, matrix_list)

    return graph


def create_graph_edges(graph, matrix_list):
    """Creates edges from 'row' and 'column' columns in a matrix list."""

    table = matrix_list.cells_list_.copy()
    if (
        matrix_list.criterion_ == matrix_list.other_criterion_
        and matrix_list.is_matrix_subset_ is False
    ):
        table = table[table["row"] < table["column"]]
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


def compute_circular_layout(graph):
    """Computes a circular layout with the last node as center"""

    pos = nx.circular_layout(graph)
    last_node = list(graph.nodes())[-1]
    for node in graph.nodes():
        if node == last_node:
            graph.nodes[node]["pos"] = [0, 0]
        else:
            graph.nodes[node]["pos"] = pos[node]

    return graph


def compute_newtork_statistics(graph):
    """Compute network statistics."""

    nodes = list(graph.nodes())
    degree = [graph.nodes[node]["degree"] for node in nodes]
    betweenness = nx.betweenness_centrality(graph)
    closeness = nx.closeness_centrality(graph)
    pagerank = nx.pagerank(graph)

    indicators = pd.DataFrame(
        {
            "Degree": degree,
            "Betweenness": betweenness,
            "Closeness": closeness,
            "PageRank": pagerank,
        },
        index=nodes,
    )

    return indicators


def compute_node_degree(graph):
    """Computes the degree of each node in a networkx graph."""

    for node, adjacencies in graph.adjacency():
        graph.nodes[node]["degree"] = len(adjacencies)

    return graph


def compute_spring_layout(graph, k, iterations, seed):
    """Computes the layout of a networkx graph."""
    pos = nx.spring_layout(graph, k=k, iterations=iterations, seed=seed)
    for node in graph.nodes():
        graph.nodes[node]["pos"] = pos[node]
    return graph


def compute_graph_textfont_color(graph):
    """Computes the textfont color for each node in a networkx graph."""

    occ = [graph.nodes[node]["OCC"] for node in graph.nodes()]
    occ_scaled = scale_occ(occ, max_size=1.0, min_size=0.35)
    colors = px.colors.sequential.Greys
    textfont_color = np.array(colors)[
        np.round(occ_scaled * (len(colors) - 1)).astype(int)
    ]

    for index, node in enumerate(graph.nodes()):
        graph.nodes[node]["textfont_color"] = textfont_color[index]

    return graph


def occ_to_textfont_color(occ):
    """Computes the textfont color from an OCC list."""
    occ_scaled = scale_occ(occ, max_size=1.0, min_size=0.35)
    colors = px.colors.sequential.Greys
    textfont_color = np.array(colors)[
        np.round(occ_scaled * (len(colors) - 1)).astype(int)
    ]
    return textfont_color


def compute_prop_sizes(graph, prop, min_size, max_size):
    """Compute key size for a networkx graph from OCC property of the node."""

    if min_size == max_size:
        return graph

    occ = [graph.nodes[node]["OCC"] for node in graph.nodes()]

    occ_scaled = scale_occ(occ, max_size, min_size)

    for index, node in enumerate(graph.nodes()):
        graph.nodes[node][prop] = occ_scaled[index]

    return graph


def scale_occ(occ, max_size, min_size):
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


def compute_textposition_from_lists(node_x, node_y):
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


def compute_textposition_from_nx_graph(graph):
    """Computes the text position for a node in a networkx graph."""

    node_x, node_y = extract_node_coordinates(graph)

    return compute_textposition_from_lists(node_x, node_y)


def create_edge_traces(graph):
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


def create_graph_nodes(graph, matrix_list):
    """Creates nodes from 'row' and 'column' columns in a matrix list."""

    # adds items in 'row' column as nodes
    nodes = matrix_list.cells_list_["row"].drop_duplicates().to_list()
    nodes = [(node, {"group": 0, "color": "#8da4b4"}) for node in nodes]
    graph.add_nodes_from(nodes)

    # adds items in 'column' column as nodes
    candidates = matrix_list.cells_list_["column"].drop_duplicates().to_list()
    nodes = []
    for candidate in candidates:
        if candidate not in graph.nodes:
            nodes.append(candidate)
    if len(nodes) > 1:
        nodes = [(node, {"group": 1, "color": "#556f81"}) for node in nodes]
        graph.add_nodes_from(nodes)

    return graph


def create_network_graph(
    edge_traces,
    node_trace,
    text_trace,
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
            dict(
                text="",
                showarrow=False,
                xref="paper",
                yref="paper",
                x=0.005,
                y=-0.002,
                align="left",
                font={"size": 10},
            )
        ],
    )

    fig = go.Figure(
        data=edge_traces + [node_trace] + [text_trace],
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
        # xaxis_range=[-1 - delta, 1 + delta],
        paper_bgcolor="white",
        plot_bgcolor="white",
    )

    return fig


def create_node_trace(graph):
    """Creates a node trace for a networkx graph."""

    node_x, node_y = extract_node_coordinates(graph)
    node_colors = extract_node_colors(graph)
    node_sizes = extract_node_sizes(graph)
    node_trace = go.Scatter(
        x=node_x,
        y=node_y,
        mode="markers",
        hoverinfo="text",
        marker={
            "color": node_colors,
            "size": node_sizes,
            "line": {"width": 1.5, "color": "white"},
            "opacity": 1.0,
        },
    )

    return node_trace


def create_occ_node_property(graph):
    """Adds OCC value as a property of the node in a graph."""

    for node in graph.nodes():
        occ = node.split(" ")[-1]
        occ = occ.split(":")[0]
        occ = int(occ)
        graph.nodes[node]["OCC"] = occ

    return graph


def create_text_trace(graph):
    """Create text trace for network graph."""

    node_x, node_y = extract_node_coordinates(graph)
    node_names = extract_node_names(graph)
    textfont_sizes = extract_textfont_sizes(graph)
    textposition = compute_textposition_from_nx_graph(graph)
    node_colors = extract_node_colors(graph)

    node_sizes = extract_node_sizes(graph)
    node_sizes = [size - 12 for size in node_sizes]

    text_trace = go.Scatter(
        x=node_x,
        y=node_y,
        mode="markers+text",
        text=node_names,
        hoverinfo="text",
        marker={
            "color": node_colors,
            "size": node_sizes,
            "line": {"width": 0, "color": "red"},
            "opacity": 1,
        },
        textposition=textposition,
        textfont={"size": textfont_sizes},
    )

    return text_trace


def extract_textfont_sizes(graph):
    """Extracts textfont sizes from a networkx graph."""

    textfont_sizes = []
    for node in graph.nodes():
        textfont_sizes.append(graph.nodes[node]["textfont_size"])

    return textfont_sizes


def extract_node_colors(graph):
    """Extracts node colors from a networkx graph."""

    node_colors = []
    for node in graph.nodes():
        node_colors.append(graph.nodes[node]["color"])

    return node_colors


def extract_node_coordinates(graph):
    """Extracts node coordinates from a networkx graph."""

    node_x = []
    node_y = []
    for node in graph.nodes():
        pos_x, pos_y = graph.nodes[node]["pos"]
        node_x.append(pos_x)
        node_y.append(pos_y)

    return node_x, node_y


def extract_node_names(graph):
    """Extracts node names from a networkx graph."""

    node_names = []
    for node in graph.nodes():
        node_names.append(node)

    return node_names


def extract_node_sizes(graph):
    """Extracts node sizes from a networkx graph."""

    node_sizes = []
    for node in graph.nodes():
        if "node_size" not in graph.nodes[node]:
            raise ValueError(
                f"Node {node} does not have a node_size property."
            )
        node_sizes.append(graph.nodes[node]["node_size"])

    return node_sizes


def set_edge_properties_for_corr_maps(graph):
    """Sets edge properties for correlation maps."""

    for edge in graph.edges():
        if graph.edges[edge]["value"] < 0.25:
            graph.edges[edge]["width"] = 2
            graph.edges[edge]["dash"] = "dot"
            graph.edges[edge]["color"] = "#8da4b4"

        elif graph.edges[edge]["value"] < 0.5:
            graph.edges[edge]["width"] = 2
            graph.edges[edge]["dash"] = "solid"
            graph.edges[edge]["color"] = "#8da4b4"

        elif graph.edges[edge]["value"] < 0.75:
            graph.edges[edge]["width"] = 4
            graph.edges[edge]["dash"] = "solid"
            graph.edges[edge]["color"] = "#8da4b4"

        else:
            graph.edges[edge]["width"] = 6
            graph.edges[edge]["dash"] = "solid"
            graph.edges[edge]["color"] = "#8da4b4"

    return graph


def set_edge_properties_for_co_occ_networks(graph):
    """Sets edge properties for co-occurrence networks."""

    for edge in graph.edges():
        graph.edges[edge]["width"] = 1
        graph.edges[edge]["color"] = "lightgrey"

    return graph


def set_node_colors(graph, node_names, new_color):
    """Sets node colors in a networkx graph."""

    for node in graph.nodes():
        if node in node_names:
            graph.nodes[node]["color"] = new_color

    return graph
