"""Network Plot"""

import networkx as nx
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


def get_network_graph_plot(
    graph,
    nx_k=0.5,
    nx_iterations=10,
    delta=1.0,
):
    """Network plot"""

    graph = _make_layout(graph, nx_k, nx_iterations)
    edge_trace, node_trace = _create_traces(graph)
    node_trace = _color_node_points(graph, node_trace)
    fig = _create_network_graph(edge_trace, node_trace, delta)
    return fig


def _color_node_points(G, node_trace):
    node_adjacencies = []
    node_hover_text = []
    for _, adjacencies in enumerate(G.adjacency()):
        node_adjacencies.append(len(adjacencies[1]))
        text = "<b>" + adjacencies[0] + "</b>"
        if adjacencies[1]:
            max_len = list(adjacencies[1].keys())
            max_len = max([len(x) for x in max_len])
            fmt = "<br>  {:>" + str(max_len) + "}"
            for index, key in enumerate(adjacencies[1].keys()):
                if index > 30:
                    text += fmt.format("[...]")
                    break
                text += fmt.format(key)
        node_hover_text.append(text)

    # node_trace.marker.color = node_adjacencies
    node_trace.hovertext = node_hover_text
    return node_trace


def _create_network_graph(edge_trace, node_trace, delta=1.0):
    fig = go.Figure(
        data=[edge_trace, node_trace],
        layout=go.Layout(
            title="",
            titlefont=dict(size=16),
            showlegend=False,
            hovermode="closest",
            margin=dict(b=0, l=0, r=0, t=0),
            annotations=[
                dict(
                    text="",
                    showarrow=False,
                    xref="paper",
                    yref="paper",
                    x=0.005,
                    y=-0.002,
                    align="left",
                    font=dict(size=10),
                )
            ],
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        ),
    )
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="white",
            font_family="monospace",
        )
    )
    fig.update_xaxes(range=[-1 - delta, 1 + delta])
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
    )
    return fig


def _create_traces(graph):
    edge_x = []
    edge_y = []
    for edge in graph.edges():
        x0, y0 = graph.nodes[edge[0]]["pos"]
        x1, y1 = graph.nodes[edge[1]]["pos"]
        edge_x.append(x0)
        edge_x.append(x1)
        edge_x.append(None)
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)

    edge_trace = go.Scatter(
        x=edge_x,
        y=edge_y,
        line=dict(width=0.7, color="#888"),
        hoverinfo="none",
        mode="lines",
    )

    node_x = []
    node_y = []
    text = []
    colors = []
    for node in graph.nodes():
        x, y = graph.nodes[node]["pos"]
        node_x.append(x)
        node_y.append(y)
        text.append(node)
        group = graph.nodes[node]["group"]
        if graph.nodes[node]["group"] < 24:
            colors.append(px.colors.qualitative.Dark24[group])
        else:
            group = group - 24
            colors.append(px.colors.qualitative.Light24[group])

    node_size = []
    text_size = []
    for node, adjacencies in enumerate(graph.adjacency()):
        node_size.append(1 + len(adjacencies[1]))

    max_size = max(node_size)
    min_size = min(node_size)

    textfont_size_max = max_size if max_size < 20 else 20
    textfont_size_min = min_size if min_size > 7 else 7

    if max_size == min_size:
        node_size = [13] * len(node_size)
        text_size = [10] * len(node_size)
    else:
        text_size = [
            textfont_size_min
            + (textfont_size_max - textfont_size_min)
            * (x - min_size)
            / (max_size - min_size)
            for x in node_size
        ]
        node_size = [8 + 25 * (x - min_size) / (max_size - min_size) for x in node_size]

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

    node_trace = go.Scatter(
        x=node_x,
        y=node_y,
        mode="markers+text",
        hoverinfo="text",
        text=text,
        marker=dict(
            color=colors,
            size=node_size,
            line=dict(width=1, color="DarkSlateGrey"),
        ),
        textposition=textposition,
        textfont=dict(size=text_size),
    )

    return edge_trace, node_trace


def _make_layout(graph, k=0.2, iterations=50):
    pos = nx.spring_layout(graph, k=k, iterations=iterations)
    for node in graph.nodes():
        graph.nodes[node]["pos"] = pos[node]
    return graph
