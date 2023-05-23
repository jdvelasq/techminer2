"""This module contains functions for network analysis that are common to
several modules.


"""
import networkx as nx
import numpy as np
import plotly.graph_objects as go

# from . import vantagepoint


def create_graph_edges(graph, matrix_list):
    """Creates edges from 'row' and 'column' columns in a matrix list."""

    table = matrix_list.matrix_list_.copy()
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


def compute_spring_layout(graph, k, iterations, seed):
    """Computes the layout of a networkx graph."""
    pos = nx.spring_layout(graph, k=k, iterations=iterations, seed=seed)
    for node in graph.nodes():
        graph.nodes[node]["pos"] = pos[node]
    return graph


def compute_prop_sizes(graph, prop, min_size, max_size):
    """Compute key size for a networkx graph from OCC property of the node."""

    # assign the OCC as value for the key property
    for node in graph.nodes():
        graph.nodes[node][prop] = graph.nodes[node]["OCC"]

    # computes the min value of the key property
    min_value = min([graph.nodes[node][prop] for node in graph.nodes()])

    # adjust the key property for min_size as current value minus min value
    for node in graph.nodes():
        graph.nodes[node][prop] = (
            graph.nodes[node][prop] - min_value + min_size
        )

    # computes the max value of the key property
    max_value = max([graph.nodes[node][prop] for node in graph.nodes()])

    # adjust the key property for max_size
    if max_value > max_size:
        for node in graph.nodes():
            graph.nodes[node][prop] = min_size + (
                graph.nodes[node][prop] - min_size
            ) / (max_value - min_size) * (max_size - min_size)

    return graph


def compute_textposition(graph):
    """Computes the text position for a node in a networkx graph."""

    node_x, node_y = extract_node_coordinates(graph)

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

    for col in ["row", "column"]:
        if col == "row":
            color = "#8da4b4"
            group = 0
        else:
            color = "#556f81"
            group = 1

        nodes = matrix_list.matrix_list_[col].drop_duplicates().to_list()
        nodes = [(node, {"color": color, "group": group}) for node in nodes]
        graph.add_nodes_from(nodes)

        if (
            matrix_list.criterion_for_rows_
            == matrix_list.criterion_for_columns_
            or matrix_list.metric_ == "CORR"
        ):
            break

    return graph


def create_network_graph(edge_traces, node_trace, text_trace, delta=1.0):
    """Creates a network graph from edge traces, node trace and text trace using plotly express."""

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
        xaxis={"showgrid": False, "zeroline": False, "showticklabels": False},
        yaxis={"showgrid": False, "zeroline": False, "showticklabels": False},
    )

    fig = go.Figure(
        data=edge_traces + [node_trace] + [text_trace],
        layout=layout,
    )

    fig.update_layout(
        hoverlabel={
            "bgcolor": "white",
            "font_family": "monospace",
        },
        xaxis_range=[-1 - delta, 1 + delta],
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
            "opacity": 1,
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
    textposition = compute_textposition(graph)
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


# def compute_textfont_sizes(node_occ, textfont_size_min, textfont_size_max):
#     """Computes the textfont sizes for a networkx graph."""
#     textfont_sizes = np.array(node_occ)
#     textfont_sizes = textfont_sizes - textfont_sizes.min() + textfont_size_min
#     if textfont_sizes.max() > textfont_size_max:
#         textfont_sizes = textfont_size_min + (
#             textfont_sizes - textfont_size_min
#         ) / (textfont_sizes.max() - textfont_size_min) * (
#             textfont_size_max - textfont_size_min
#         )
#     return textfont_sizes


# def create_nodes_from_matrix(obj):
#     """Creates a nodes table from a matrix."""

#     matrix_list = vantagepoint.analyze.list_cells_in_matrix(obj)
#     nodes = matrix_list["row"].drop_duplicates().to_list()
#     if obj.criterion_for_columns_ != obj.criterion_for_rows_:
#         nodes += matrix_list["column"].drop_duplicates().to_list()
#     nodes = sorted(list(set(nodes)))
#     nodes_table = pd.DataFrame(index=nodes)
#     return nodes_table


# def create_occ_from_index(nodes_table):
#     """Creates an occ column in a dataframe from index values."""

#     nodes_table = nodes_table.copy()
#     nodes_table["OCC"] = nodes_table.index.copy()
#     nodes_table["OCC"] = nodes_table["OCC"].str.split(" ")[-1]
#     nodes_table["OCC"] = nodes_table["OCC"].str.split(":")[0]
#     nodes_table["OCC"] = nodes_table["OCC"].astype(int)
#     return nodes_table


# def melt_matrix_obj(matrix_obj):
#     """Melt a matrix obj."""
#     matrix = matrix_obj.matrix_.melt(
#         value_name=matrix_obj.metric_,
#         var_name="column",
#         ignore_index=False,
#     )
#     matrix = matrix.reset_index()
#     matrix = matrix.rename(columns={"index": "row"})
#     matrix = matrix[matrix[matrix_obj.metric_] > 0.0]
#     return matrix
