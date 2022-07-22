"""
Cluster Map
===============================================================================

# >>> from techminer2 import *
# >>> directory = "data/regtech/"
# >>> file_name = "sphinx/_static/cluster_map_occurrence.html"

# >>> occ_mtx = occ_flood_matrix(
# ...    column='author_keywords',
# ...    by='authors',
# ...    min_occ=3,
# ...    directory=directory,
# ... )
# >>> occ_mtx
#                    author_keywords            authors  OCC
# 0                   regtech 70:462     Arner DW 7:220    6
# 1                   fintech 42:406     Arner DW 7:220    5
# 2                   regtech 70:462   Buckley RP 6:217    5
# 3      financial regulation 08:091     Arner DW 7:220    4
# 4                   fintech 42:406   Buckley RP 6:217    4
# 5                   fintech 42:406  Zetzsche DA 4:092    4
# 6                   regtech 70:462  Zetzsche DA 4:092    4
# 7                   account 04:022    Brennan R 3:008    3
# 8                   account 04:022       Ryan P 3:008    3
# 9   data protection officer 03:008    Brennan R 3:008    3
# 10  data protection officer 03:008       Ryan P 3:008    3
# 11     financial regulation 08:091   Buckley RP 6:217    3
# 12                  regtech 70:462  Barberis JN 4:146    3
# 13                  regtech 70:462    Brennan R 3:008    3
# 14                  regtech 70:462       Ryan P 3:008    3

# >>> cluster_map(
# ...     occ_mtx
# ... ).write_html(file_name)

# .. raw:: html

#     <iframe src="_static/cluster_map_occurrence.html" height="600px" width="100%" frameBorder="0"></iframe>

"""

import networkx as nx
import plotly.graph_objects as go


def cluster_map(
    flood_matrix,
):
    """Makes cluster map from a ocurrence flooding matrix."""

    G = nx.Graph()
    G = _create_nodes(G, flood_matrix)
    G = _create_edges(G, flood_matrix)
    G = _make_layout(G)
    edge_trace, node_trace = _create_traces(G)
    node_trace = _color_node_points(G, node_trace)
    fig = _create_network_graph(edge_trace, node_trace)
    return fig


def _make_layout(G, k=0.2, iteratons=50):
    pos = nx.spring_layout(G, k=k, iterations=iteratons)
    for node in G.nodes():
        G.nodes[node]["pos"] = pos[node]
    return G


def _create_network_graph(edge_trace, node_trace):
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
    # fig.update_traces(textposition="top center")
    fig.update_xaxes(range=[-1.5, 1.5])
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
    )
    return fig


def _color_node_points(G, node_trace):
    node_adjacencies = []
    node_hove_text = []
    for node, adjacencies in enumerate(G.adjacency()):
        node_adjacencies.append(len(adjacencies[1]))
        text = "<b>" + adjacencies[0] + "</b>"
        max_len = list(adjacencies[1].keys())
        max_len = max([len(x) for x in max_len])
        fmt = "<br> {:>" + str(max_len) + "} {}"
        for key, value in adjacencies[1].items():
            text += fmt.format(key, value["weight"])
        node_hove_text.append(text)

    # node_trace.marker.color = node_adjacencies
    node_trace.hovertext = node_hove_text
    return node_trace


def _create_traces(G):

    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = G.nodes[edge[0]]["pos"]
        x1, y1 = G.nodes[edge[1]]["pos"]
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
    for node in G.nodes():
        x, y = G.nodes[node]["pos"]
        node_x.append(x)
        node_y.append(y)
        text.append(node)
        if G.nodes[node]["group"] == 0:
            colors.append("#F1948A")
        else:
            colors.append("#5DADE2")

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
        textposition="bottom left",
    )

    return edge_trace, node_trace


def _create_edges(G, flood_matrix):

    edges = []

    for _, row in flood_matrix.iterrows():
        edges.append((row[0], row[1], row[2]))

    G.add_weighted_edges_from(edges)
    return G


def _create_nodes(G, flood_matrix):

    nodes = []

    col0 = flood_matrix[flood_matrix.columns[0]]
    value_counts0 = col0.value_counts()
    nodes += [
        (item, dict(size=value_counts0[item], group=0)) for item in value_counts0.index
    ]

    col1 = flood_matrix[flood_matrix.columns[1]]
    value_counts1 = col1.value_counts()
    nodes += [
        (item, dict(size=value_counts1[item], group=1)) for item in value_counts1.index
    ]

    G.add_nodes_from(nodes)
    return G
