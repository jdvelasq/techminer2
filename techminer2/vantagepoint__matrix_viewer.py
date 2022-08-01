"""
Matrix Viwer
===============================================================================



**Matrix view for a occurrence matrix.**


>>> directory = "data/regtech/"

>>> file_name = "sphinx/_static/vantagepoint__matrix_viewer-0.html"

>>> from techminer2 import vantagepoint__occ_matrix_list
>>> matrix = vantagepoint__occ_matrix_list(
...    criterion_for_columns='author_keywords',
...    criterion_for_rows='authors',
...    topic_min_occ=3,
...    directory=directory,
... )
>>> matrix
                  row                          column  OCC
0      Arner DW 7:220                  regtech 69:461    6
1      Arner DW 7:220                  fintech 42:406    5
2      Arner DW 7:220               blockchain 18:109    1
3      Arner DW 7:220    regulatory technology 12:047    1
4      Arner DW 7:220     financial technology 09:032    1
5      Arner DW 7:220     financial regulation 08:091    4
6      Arner DW 7:220       financial services 05:135    1
7      Arner DW 7:220      financial inclusion 05:068    2
8      Arner DW 7:220    anti-money laundering 04:030    1
9      Arner DW 7:220     financial innovation 04:007    1
10     Arner DW 7:220                  finance 03:019    1
11   Buckley RP 6:217                  regtech 69:461    5
12   Buckley RP 6:217                  fintech 42:406    4
13   Buckley RP 6:217               blockchain 18:109    1
14   Buckley RP 6:217     financial regulation 08:091    3
15   Buckley RP 6:217       financial services 05:135    1
16   Buckley RP 6:217      financial inclusion 05:068    2
17   Buckley RP 6:217    anti-money laundering 04:030    1
18   Buckley RP 6:217                  finance 03:019    1
19  Barberis JN 4:146                  regtech 69:461    3
20  Barberis JN 4:146                  fintech 42:406    2
21  Barberis JN 4:146    regulatory technology 12:047    1
22  Barberis JN 4:146     financial technology 09:032    1
23  Barberis JN 4:146     financial regulation 08:091    2
24  Barberis JN 4:146       financial services 05:135    1
25  Barberis JN 4:146      financial inclusion 05:068    1
26  Barberis JN 4:146    anti-money laundering 04:030    1
27  Barberis JN 4:146     financial innovation 04:007    1
28  Barberis JN 4:146                  finance 03:019    1
29  Zetzsche DA 4:092                  regtech 69:461    4
30  Zetzsche DA 4:092                  fintech 42:406    4
31  Zetzsche DA 4:092               blockchain 18:109    1
32  Zetzsche DA 4:092     financial regulation 08:091    2
33  Zetzsche DA 4:092      financial inclusion 05:068    2
34  Zetzsche DA 4:092    anti-money laundering 04:030    1
35  Zetzsche DA 4:092                  finance 03:019    1
36    Brennan R 3:008                  regtech 69:461    3
37    Brennan R 3:008               compliance 12:020    2
38    Brennan R 3:008           accountability 04:022    3
39    Brennan R 3:008                     gdpr 03:012    2
40    Brennan R 3:008  data protection officer 03:008    3
41    Brennan R 3:008             semantic web 03:002    1
42       Ryan P 3:008                  regtech 69:461    3
43       Ryan P 3:008               compliance 12:020    2
44       Ryan P 3:008           accountability 04:022    3
45       Ryan P 3:008                     gdpr 03:012    2
46       Ryan P 3:008  data protection officer 03:008    3
47       Ryan P 3:008             semantic web 03:002    1

>>> vantagepoint__matrix_viewer(
...     matrix,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../_static/vantagepoint__matrix_viewer-0.html" height="600px" width="100%" frameBorder="0"></iframe>


**Matrix view for a co-occurrence matrix.**

>>> file_name = "sphinx/_static/vantagepoint__matrix_viewer-1.html"

>>> from techminer2 import vantagepoint__co_occ_matrix_list
>>> matrix = vantagepoint__co_occ_matrix_list(
...    criterion='author_keywords',
...    topic_min_occ=8,
...    directory=directory,
... )
>>> matrix
                               row                          column  OCC
0                   regtech 69:461                  regtech 69:461   69
1                   regtech 69:461                  fintech 42:406   42
2                   regtech 69:461               blockchain 18:109   17
3                   regtech 69:461  artificial intelligence 13:065   10
4                   regtech 69:461    regulatory technology 12:047    4
5                   regtech 69:461               compliance 12:020   12
6                   regtech 69:461     financial technology 09:032    5
7                   regtech 69:461     financial regulation 08:091    8
8                   fintech 42:406                  regtech 69:461   42
9                   fintech 42:406                  fintech 42:406   42
10                  fintech 42:406               blockchain 18:109   14
11                  fintech 42:406  artificial intelligence 13:065    8
12                  fintech 42:406    regulatory technology 12:047    3
13                  fintech 42:406               compliance 12:020    3
14                  fintech 42:406     financial technology 09:032    4
15                  fintech 42:406     financial regulation 08:091    5
16               blockchain 18:109                  regtech 69:461   17
17               blockchain 18:109                  fintech 42:406   14
18               blockchain 18:109               blockchain 18:109   18
19               blockchain 18:109  artificial intelligence 13:065    2
20               blockchain 18:109               compliance 12:020    3
21               blockchain 18:109     financial technology 09:032    1
22               blockchain 18:109     financial regulation 08:091    1
23  artificial intelligence 13:065                  regtech 69:461   10
24  artificial intelligence 13:065                  fintech 42:406    8
25  artificial intelligence 13:065               blockchain 18:109    2
26  artificial intelligence 13:065  artificial intelligence 13:065   13
27  artificial intelligence 13:065    regulatory technology 12:047    2
28  artificial intelligence 13:065               compliance 12:020    1
29  artificial intelligence 13:065     financial technology 09:032    2
30  artificial intelligence 13:065     financial regulation 08:091    2
31    regulatory technology 12:047                  regtech 69:461    4
32    regulatory technology 12:047                  fintech 42:406    3
33    regulatory technology 12:047  artificial intelligence 13:065    2
34    regulatory technology 12:047    regulatory technology 12:047   12
35    regulatory technology 12:047     financial technology 09:032    6
36    regulatory technology 12:047     financial regulation 08:091    2
37               compliance 12:020                  regtech 69:461   12
38               compliance 12:020                  fintech 42:406    3
39               compliance 12:020               blockchain 18:109    3
40               compliance 12:020  artificial intelligence 13:065    1
41               compliance 12:020               compliance 12:020   12
42     financial technology 09:032                  regtech 69:461    5
43     financial technology 09:032                  fintech 42:406    4
44     financial technology 09:032               blockchain 18:109    1
45     financial technology 09:032  artificial intelligence 13:065    2
46     financial technology 09:032    regulatory technology 12:047    6
47     financial technology 09:032     financial technology 09:032    9
48     financial technology 09:032     financial regulation 08:091    2
49     financial regulation 08:091                  regtech 69:461    8
50     financial regulation 08:091                  fintech 42:406    5
51     financial regulation 08:091               blockchain 18:109    1
52     financial regulation 08:091  artificial intelligence 13:065    2
53     financial regulation 08:091    regulatory technology 12:047    2
54     financial regulation 08:091     financial technology 09:032    2
55     financial regulation 08:091     financial regulation 08:091    8

>>> vantagepoint__matrix_viewer(
...     matrix,
...     nx_k=0.5,
...     nx_iteratons=5,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../_static/vantagepoint__matrix_viewer-1.html" height="600px" width="100%" frameBorder="0"></iframe>



"""
import networkx as nx
import numpy as np
import plotly.graph_objects as go


def vantagepoint__matrix_viewer(
    matrix_list,
    nx_k=0.5,
    nx_iteratons=10,
    delta=1.0,
):
    """Makes cluster map from a ocurrence flooding matrix."""

    column = matrix_list["column"].drop_duplicates().sort_values()
    row = matrix_list["row"].drop_duplicates().sort_values()
    if row.equals(column):
        return _matrix_viewer_for_co_occ_matrix(matrix_list, nx_k, nx_iteratons, delta)
    return _matrix_viewer_for_occ_matrix(matrix_list, nx_k, nx_iteratons, delta)


def _matrix_viewer_for_co_occ_matrix(matrix_list, nx_k, nx_iteratons, delta):
    graph = nx.Graph()
    graph = _create_nodes(graph, matrix_list, 0)
    graph = _create_edges(graph, matrix_list)
    graph = _make_layout(graph, nx_k, nx_iteratons)
    edge_trace, node_trace = _create_traces(graph)
    node_trace = _color_node_points(graph, node_trace)
    fig = _create_network_graph(edge_trace, node_trace, delta)
    return fig


def _matrix_viewer_for_occ_matrix(matrix_list, nx_k, nx_iteratons, delta):
    graph = nx.Graph()
    graph = _create_nodes(graph, matrix_list, 0)
    graph = _create_nodes(graph, matrix_list, 1)
    graph = _create_edges(graph, matrix_list)
    graph = _make_layout(graph, nx_k, nx_iteratons)
    edge_trace, node_trace = _create_traces(graph)
    node_trace = _color_node_points(graph, node_trace)
    fig = _create_network_graph(edge_trace, node_trace, delta)
    return fig


def _make_layout(G, k=0.2, iteratons=50):
    pos = nx.spring_layout(G, k=k, iterations=iteratons)
    for node in G.nodes():
        G.nodes[node]["pos"] = pos[node]
    return G


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


def _color_node_points(G, node_trace):
    node_adjacencies = []
    node_hove_text = []
    for _, adjacencies in enumerate(G.adjacency()):
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


def _create_edges(G, flood_matrix):
    edges = []
    for _, row in flood_matrix.iterrows():
        edges.append((row[0], row[1], row[2]))
    G.add_weighted_edges_from(edges)
    return G


def _create_nodes(G, flood_matrix, col_index):

    nodes = []

    col = flood_matrix[flood_matrix.columns[col_index]]
    value_counts = col.value_counts()
    nodes += [
        (item, dict(size=value_counts[item], group=col_index))
        for item in value_counts.index
    ]

    G.add_nodes_from(nodes)
    return G
