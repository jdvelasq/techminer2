"""
Network Plot
===============================================================================

>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> matrix_list = co_occ_matrix_list(
...    column='author_keywords',
...    min_occ=3,
...    directory=directory,
... )

>>> from techminer2.co_occ_network import co_occ_network
>>> graph = co_occ_network(matrix_list)
>>> from techminer2.network_community_detection import network_community_detection
>>> graph = network_community_detection(graph, method='louvain')

>>> from techminer2.network_plot import network_plot
>>> file_name = "sphinx/_static/network_plot.html"
>>> network_plot(graph).write_html(file_name)

.. raw:: html

    <iframe src="_static/network_plot.html" height="600px" width="100%" frameBorder="0"></iframe>


"""
import networkx as nx
import numpy as np
import plotly.graph_objects as go


def network_plot(
    graph,
    nx_k=0.5,
    nx_iteratons=10,
    delta=1.0,
):
    """Network plot"""

    graph = _make_layout(graph, nx_k, nx_iteratons)
    edge_trace, node_trace = _create_traces(graph)
    node_trace = _color_node_points(graph, node_trace)
    fig = _create_network_graph(edge_trace, node_trace, delta)
    return fig


def _color_node_points(G, node_trace):
    node_adjacencies = []
    node_hove_text = []
    for _, adjacencies in enumerate(G.adjacency()):
        node_adjacencies.append(len(adjacencies[1]))
        text = "<b>" + adjacencies[0] + "</b>"
        if adjacencies[1]:
            max_len = list(adjacencies[1].keys())
            max_len = max([len(x) for x in max_len])
            fmt = "<br> {:>" + str(max_len) + "} {}"
            for key, value in adjacencies[1].items():
                text += fmt.format(key, value["weight"])
        node_hove_text.append(text)

    # node_trace.marker.color = node_adjacencies
    node_trace.hovertext = node_hove_text
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
        if graph.nodes[node]["group"] == 0:
            colors.append("#F1948A")
        else:
            colors.append("#5DADE2")

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
            size=13,
            line_width=2,
        ),
        textposition=textposition,
    )

    return edge_trace, node_trace


def _make_layout(graph, k=0.2, iteratons=50):
    pos = nx.spring_layout(graph, k=k, iterations=iteratons)
    for node in graph.nodes():
        graph.nodes[node]["pos"] = pos[node]
    return graph


# from operator import itemgetter

# import matplotlib.pyplot as plt
#
# import numpy as np

# group_colors = [
#     "tab:blue",
#     "tab:orange",
#     "tab:green",
#     "tab:red",
#     "tab:purple",
#     "tab:brown",
#     "tab:pink",
#     "tab:gray",
#     "tab:olive",
#     "tab:cyan",
#     "cornflowerblue",
#     "lightsalmon",
#     "limegreen",
#     "tomato",
#     "mediumvioletred",
#     "darkgoldenrod",
#     "lightcoral",
#     "silver",
#     "darkkhaki",
#     "skyblue",
# ] * 5


# def network_plot(
#     network,
#     figsize=(7, 7),
#     k=0.20,
#     iterations=50,
#     max_labels=50,
# ):

#     fig = plt.figure(figsize=figsize)
#     ax = fig.subplots()

#     options = {
#         "width": 1,
#         "with_labels": False,
#         "font_size": 7,
#         "font_weight": "regular",
#         "alpha": 0.7,
#     }

#     # --------------------------------------------------------------------------------
#     G = network["G"]
#     nodes = network["nodes"]
#     edges = network["edges"]

#     # --------------------------------------------------------------------------------
#     pos = nx.spring_layout(G, k=k, iterations=iterations)

#     colors = [node[1]["group"] for node in nodes]
#     colors = [group_colors[color] for color in colors]

#     sizes = [node[1]["size"] for node in G.nodes.data()]
#     sizes = [size / max(sizes) for size in sizes]
#     max_size = max(sizes)
#     min_size = min(sizes)
#     if max_size == min_size:
#         sizes = [500 for size in sizes]
#     else:
#         sizes = [
#             (size - min_size) / (max_size - min_size) * 1400 + 100 for size in sizes
#         ]

#     edge_colors = ["silver"] * len(edges)

#     # draws the network
#     nx.draw(
#         G,
#         node_color=colors,
#         node_size=sizes,
#         edge_color=edge_colors,
#         pos=pos,
#         **options,
#     )

#     # edge color of nodes
#     ax.collections[0].set_edgecolor("k")

#     # plot centers as black dots
#     x_points = [value[0] for value in pos.values()]
#     y_points = [value[1] for value in pos.values()]

#     size = [
#         (node[0], node[1]["size"], pos[node[0]][0], pos[node[0]][1])
#         for node in G.nodes.data()
#     ]
#     size = sorted(size, key=itemgetter(1), reverse=True)
#     x_points_marked = [value[2] for value in size[:max_labels]]
#     y_points_marked = [value[3] for value in size[:max_labels]]

#     ax.scatter(
#         x_points_marked,
#         y_points_marked,
#         marker="o",
#         s=20,
#         c="k",
#         alpha=1.0,
#         zorder=10,
#     )

#     #  Center of the plot
#     x_mean = sum(x_points) / len(x_points)
#     y_mean = sum(y_points) / len(y_points)

#     xlim = ax.get_xlim()
#     ylim = ax.get_ylim()

#     factor = 0.05
#     rx = factor * (xlim[1] - xlim[0])
#     ry = factor * (ylim[1] - ylim[0])
#     radious = np.sqrt(rx**2 + ry**2)

#     for label in size[:max_labels]:

#         label = label[0]

#         x_point, y_point = pos[label]

#         x_c = x_point - x_mean
#         y_c = y_point - y_mean
#         angle = np.arctan(np.abs(y_c / x_c))
#         x_label = x_point + np.copysign(radious * np.cos(angle), x_c)
#         y_label = y_point + np.copysign(radious * np.sin(angle), y_c)

#         ha = "left" if x_point > x_mean else "right"
#         va = "center"

#         ax.text(
#             x_label,
#             y_label,
#             s=label,
#             fontsize=7,
#             bbox=dict(
#                 facecolor="w",
#                 alpha=1.0,
#                 edgecolor="gray",
#                 boxstyle="round,pad=0.5",
#             ),
#             horizontalalignment=ha,
#             verticalalignment=va,
#             alpha=0.9,
#             zorder=13,
#         )

#         ax.plot(
#             [x_point, x_label],
#             [y_point, y_label],
#             lw=1,
#             ls="-",
#             c="k",
#             zorder=13,
#         )

#     fig.set_tight_layout(True)

#     return fig
