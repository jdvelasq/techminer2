"""
Correlation Map (GPT)
===============================================================================

Creates auto-correlation and cross-correlation maps.

>>> directory = "data/regtech/"

>>> file_name = "sphinx/_static/vantagepoint__corr_map_1.html"

>>> from techminer2 import vantagepoint
>>> obj = vantagepoint.analyze.auto_corr_matrix(
...     criterion='authors',
...     topics_length=10,
...     directory=directory,
... )
>>> print(obj.matrix_.to_markdown())
|                  |   Arner DW 3:185 |   Buckley RP 3:185 |   Butler T/1 2:041 |   Hamdan A 2:018 |   Lin W 2:017 |   Singh C 2:017 |   Brennan R 2:014 |   Crane M 2:014 |   Sarea A 2:012 |   Grassi L 2:002 |
|:-----------------|-----------------:|-------------------:|-------------------:|-----------------:|--------------:|----------------:|------------------:|----------------:|----------------:|-----------------:|
| Arner DW 3:185   |                1 |                  1 |                  0 |         0        |             0 |               0 |                 0 |               0 |        0        |                0 |
| Buckley RP 3:185 |                1 |                  1 |                  0 |         0        |             0 |               0 |                 0 |               0 |        0        |                0 |
| Butler T/1 2:041 |                0 |                  0 |                  1 |         0        |             0 |               0 |                 0 |               0 |        0        |                0 |
| Hamdan A 2:018   |                0 |                  0 |                  0 |         1        |             0 |               0 |                 0 |               0 |        0.416667 |                0 |
| Lin W 2:017      |                0 |                  0 |                  0 |         0        |             1 |               1 |                 0 |               0 |        0        |                0 |
| Singh C 2:017    |                0 |                  0 |                  0 |         0        |             1 |               1 |                 0 |               0 |        0        |                0 |
| Brennan R 2:014  |                0 |                  0 |                  0 |         0        |             0 |               0 |                 1 |               1 |        0        |                0 |
| Crane M 2:014    |                0 |                  0 |                  0 |         0        |             0 |               0 |                 1 |               1 |        0        |                0 |
| Sarea A 2:012    |                0 |                  0 |                  0 |         0.416667 |             0 |               0 |                 0 |               0 |        1        |                0 |
| Grassi L 2:002   |                0 |                  0 |                  0 |         0        |             0 |               0 |                 0 |               0 |        0        |                1 |

>>> print(vantagepoint.analyze.tf_matrix(
...     criterion='authors', 
...     topics_length=10,
...     directory=directory,
... ).to_markdown())
| article                                                                                                             |   Arner DW 3:185 |   Buckley RP 3:185 |   Butler T/1 2:041 |   Hamdan A 2:018 |   Lin W 2:017 |   Singh C 2:017 |   Brennan R 2:014 |   Crane M 2:014 |   Sarea A 2:012 |   Grassi L 2:002 |
|:--------------------------------------------------------------------------------------------------------------------|-----------------:|-------------------:|-------------------:|-----------------:|--------------:|----------------:|------------------:|----------------:|----------------:|-----------------:|
| Arner DW, 2017, HANDB OF BLOCKCHAIN, DIGIT FINANC, AND INCL, VOL 1: CRYPTOCURR, FINTECH, INSURTECH, AND REGUL, P359 |                1 |                  1 |                  0 |                0 |             0 |               0 |                 0 |               0 |               0 |                0 |
| Arner DW, 2017, NORTHWEST J INTL LAW BUS, V37, P373                                                                 |                1 |                  1 |                  0 |                0 |             0 |               0 |                 0 |               0 |               0 |                0 |
| Battanta L, 2020, PROC EUR CONF INNOV ENTREPREN, ECIE, V2020-September, P112                                        |                0 |                  0 |                  0 |                0 |             0 |               0 |                 0 |               0 |               0 |                1 |
| Buckley RP, 2020, J BANK REGUL, V21, P26                                                                            |                1 |                  1 |                  0 |                0 |             0 |               0 |                 0 |               0 |               0 |                0 |
| Butler T/1, 2018, J RISK MANG FINANCIAL INST, V11, P19                                                              |                0 |                  0 |                  1 |                0 |             0 |               0 |                 0 |               0 |               0 |                0 |
| Butler T/1, 2019, PALGRAVE STUD DIGIT BUS ENABLING TECHNOL, P85                                                     |                0 |                  0 |                  1 |                0 |             0 |               0 |                 0 |               0 |               0 |                0 |
| Grassi L, 2022, J IND BUS ECON, V49, P441                                                                           |                0 |                  0 |                  0 |                0 |             0 |               0 |                 0 |               0 |               0 |                1 |
| Rabbani MR, 2022, LECT NOTES NETWORKS SYST, V423 LNNS, P381                                                         |                0 |                  0 |                  0 |                0 |             0 |               0 |                 0 |               0 |               1 |                0 |
| Ryan P, 2020, ICEIS - PROC INT CONF ENTERP INF SYST, V2, P787                                                       |                0 |                  0 |                  0 |                0 |             0 |               0 |                 1 |               1 |               0 |                0 |
| Ryan P, 2021, LECT NOTES BUS INF PROCESS, V417, P905                                                                |                0 |                  0 |                  0 |                0 |             0 |               0 |                 1 |               1 |               0 |                0 |
| Singh C, 2020, J MONEY LAUND CONTROL, V24, P464                                                                     |                0 |                  0 |                  0 |                0 |             1 |               1 |                 0 |               0 |               0 |                0 |
| Singh C, 2022, J FINANC CRIME, V29, P45                                                                             |                0 |                  0 |                  0 |                0 |             1 |               1 |                 0 |               0 |               0 |                0 |
| Turki M, 2020, HELIYON, V6                                                                                          |                0 |                  0 |                  0 |                1 |             0 |               0 |                 0 |               0 |               1 |                0 |
| Turki M, 2021, ADV INTELL SYS COMPUT, V1141, P349                                                                   |                0 |                  0 |                  0 |                1 |             0 |               0 |                 0 |               0 |               0 |                0 |


>>> chart = vantagepoint.analyze.corr_map(obj)
>>> chart.plot_.write_html(file_name)


.. raw:: html

    <iframe src="../../_static/vantagepoint__corr_map_1.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> file_name = "sphinx/_static/vantagepoint__corr_map_2.html"

>>> from techminer2 import vantagepoint
>>> obj = vantagepoint.analyze.cross_corr_matrix(
...     criterion_for_columns = 'authors', 
...     criterion_for_rows='countries',
...     topics_length=10,
...     directory=directory,
... )
>>> print(obj.matrix_.to_markdown())
|                   |   Arner DW 3:185 |   Buckley RP 3:185 |   Barberis JN 2:161 |   Brennan R 2:014 |   Butler T/1 2:041 |   Crane M 2:014 |   Hamdan A 2:018 |   Lin W 2:017 |   Singh C 2:017 |   Turki M 2:018 |
|:------------------|-----------------:|-------------------:|--------------------:|------------------:|-------------------:|----------------:|-----------------:|--------------:|----------------:|----------------:|
| Arner DW 3:185    |         1        |           1        |            0.922664 |          0        |           0        |        0        |                0 |     -0.365858 |       -0.365858 |               0 |
| Buckley RP 3:185  |         1        |           1        |            0.922664 |          0        |           0        |        0        |                0 |     -0.365858 |       -0.365858 |               0 |
| Barberis JN 2:161 |         0.922664 |           0.922664 |            1        |          0        |           0        |        0        |                0 |     -0.183387 |       -0.183387 |               0 |
| Brennan R 2:014   |         0        |           0        |            0        |          1        |           0.882498 |        1        |                0 |      0        |        0        |               0 |
| Butler T/1 2:041  |         0        |           0        |            0        |          0.882498 |           1        |        0.882498 |                0 |      0.225806 |        0.225806 |               0 |
| Crane M 2:014     |         0        |           0        |            0        |          1        |           0.882498 |        1        |                0 |      0        |        0        |               0 |
| Hamdan A 2:018    |         0        |           0        |            0        |          0        |           0        |        0        |                1 |      0        |        0        |               1 |
| Lin W 2:017       |        -0.365858 |          -0.365858 |           -0.183387 |          0        |           0.225806 |        0        |                0 |      1        |        1        |               0 |
| Singh C 2:017     |        -0.365858 |          -0.365858 |           -0.183387 |          0        |           0.225806 |        0        |                0 |      1        |        1        |               0 |
| Turki M 2:018     |         0        |           0        |            0        |          0        |           0        |        0        |                1 |      0        |        0        |               1 |

>>> chart = vantagepoint.analyze.corr_map(obj)
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/vantagepoint__corr_map_2.html" height="600px" width="100%" frameBorder="0"></iframe>



"""
from dataclasses import dataclass

import networkx as nx
import numpy as np
import plotly.graph_objects as go


@dataclass(init=False)
class _Chart:
    plot_: None
    table_: None
    prompt_: None


def corr_map(
    obj,
    nx_k=0.5,
    nx_iterations=20,
    delta=1.0,
    node_min_size=30,
    node_max_size=70,
    textfont_size_min=10,
    textfont_size_max=25,
    seed=0,
):
    matrix_list = _melt_matrix(obj.matrix_)

    node_occ = _extract_node_occ(matrix_list)
    node_sizes = _compute_node_sizes(node_occ, node_min_size, node_max_size)
    textfont_sizes = _compute_textfont_sizes(
        node_occ, textfont_size_min, textfont_size_max
    )
    node_names = _extract_node_name(matrix_list)
    matrix_list = _remove_node_names_from_matrix(matrix_list)

    graph = nx.Graph()
    graph = _create_nodes(graph, node_names, node_sizes, textfont_sizes)
    graph = _create_edges(graph, matrix_list)
    graph = _compute_graph_layout(graph, nx_k, nx_iterations, seed)

    edge_traces = _create_edge_traces(graph)
    node_trace = _create_node_trace(graph)
    text_trace = _create_text_trace(graph)

    fig = _create_network_graph(edge_traces, node_trace, text_trace, delta)

    chart = _Chart()
    chart.plot_ = fig
    chart.table_ = obj.matrix_
    chart.prompt_ = obj.prompt_

    return chart


def _create_network_graph(edge_traces, node_trace, text_trace, delta=1.0):
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


def _create_text_trace(graph):
    def extract_node_coordinates(graph):
        node_x = []
        node_y = []
        for node in graph.nodes():
            x, y = graph.nodes[node]["pos"]
            node_x.append(x)
            node_y.append(y)
        return node_x, node_y

    def extract_node_sizes(graph):
        node_sizes = []
        for node in graph.nodes():
            node_sizes.append(graph.nodes[node]["size"])
        return node_sizes

    def extract_node_names(graph):
        node_names = []
        for node in graph.nodes():
            node_names.append(node)
        return node_names

    def extract_textfont_sizes(graph):
        textfont_sizes = []
        for node in graph.nodes():
            textfont_sizes.append(graph.nodes[node]["textfont_size"])
        return textfont_sizes

    def compute_textposition(node_x, node_y):
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

    node_x, node_y = extract_node_coordinates(graph)
    node_names = extract_node_names(graph)
    textfont_sizes = extract_textfont_sizes(graph)
    textposition = compute_textposition(node_x, node_y)

    node_sizes = extract_node_sizes(graph)
    node_sizes = [size - 12 for size in node_sizes]

    text_trace = go.Scatter(
        x=node_x,
        y=node_y,
        mode="markers+text",
        text=node_names,
        hoverinfo="text",
        marker={
            "color": "#8da4b4",
            "size": node_sizes,
            "line": {"width": 0, "color": "#8da4b4"},
            "opacity": 1,
        },
        textposition=textposition,
        textfont={"size": textfont_sizes},
    )

    return text_trace


def _create_node_trace(graph):
    #
    def extract_node_coordinates(graph):
        node_x = []
        node_y = []
        for node in graph.nodes():
            x, y = graph.nodes[node]["pos"]
            node_x.append(x)
            node_y.append(y)
        return node_x, node_y

    def extract_node_names(graph):
        node_names = []
        for node in graph.nodes():
            node_names.append(node)
        return node_names

    def extract_node_sizes(graph):
        node_sizes = []
        for node in graph.nodes():
            node_sizes.append(graph.nodes[node]["size"])
        return node_sizes

    def extract_textfont_sizes(graph):
        textfont_sizes = []
        for node in graph.nodes():
            textfont_sizes.append(graph.nodes[node]["textfont_size"])
        return textfont_sizes

    def compute_textposition(node_x, node_y):
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

    node_x, node_y = extract_node_coordinates(graph)
    # node_names = extract_node_names(graph)
    node_sizes = extract_node_sizes(graph)
    # textfont_sizes = extract_textfont_sizes(graph)
    # textposition = compute_textposition(node_x, node_y)

    node_trace = go.Scatter(
        x=node_x,
        y=node_y,
        # mode="markers+text",
        mode="markers",
        hoverinfo="text",
        # text=node_names,
        marker=dict(
            color="#8da4b4",
            size=node_sizes,
            line={"width": 1.5, "color": "white"},
            opacity=1,
        ),
        # textposition=textposition,
        # textfont={"size": textfont_sizes},
    )

    return node_trace


def _create_edge_traces(graph):
    #
    def _create_edge_trace(graph, edge_type):
        edge_trace = go.Scatter(
            x=[],
            y=[],
            line={"color": "#8da4b4"},
            hoverinfo="none",
            mode="lines",
        )

        found = False
        for edge in graph.edges():
            x0, y0 = graph.nodes[edge[0]]["pos"]
            x1, y1 = graph.nodes[edge[1]]["pos"]

            width = graph.edges[edge]["width"]
            dash = graph.edges[edge]["dash"]
            type_ = graph.edges[edge]["edge_type"]

            if type_ == edge_type:
                found = True

                edge_trace["line"]["width"] = width
                edge_trace["line"]["dash"] = dash

                edge_trace["x"] += (x0, x1, None)
                edge_trace["y"] += (y0, y1, None)

        if found:
            return edge_trace
        else:
            return None

    result = []
    for edge_type in [0, 1, 2, 3]:
        edge_trace = _create_edge_trace(graph, edge_type)
        if edge_trace:
            result.append(edge_trace)
    return result


def _compute_graph_layout(graph, k, iterations, seed):
    pos = nx.spring_layout(graph, k=k, iterations=iterations, seed=seed)
    for node in graph.nodes():
        graph.nodes[node]["pos"] = pos[node]
    return graph


def _create_edges(graph, matrix_list):
    matrix_list = matrix_list.copy()
    matrix_list = matrix_list[matrix_list["row"] < matrix_list["column"]]

    matrix_list["edge_type"] = 0
    matrix_list.loc[
        (matrix_list.CORR > 0.25) & (matrix_list.CORR <= 0.5), "edge_type"
    ] = 1
    matrix_list.loc[
        (matrix_list.CORR > 0.50) & (matrix_list.CORR <= 0.75), "edge_type"
    ] = 2
    matrix_list.loc[(matrix_list.CORR > 0.75), "edge_type"] = 3

    matrix_list["width"] = 2
    matrix_list.loc[matrix_list.edge_type == 1, "width"] = 2
    matrix_list.loc[matrix_list.edge_type == 2, "width"] = 4
    matrix_list.loc[matrix_list.edge_type == 3, "width"] = 6

    matrix_list["dash"] = "dot"
    matrix_list.loc[matrix_list.edge_type == 1, "dash"] = "solid"
    matrix_list.loc[matrix_list.edge_type == 2, "dash"] = "solid"
    matrix_list.loc[matrix_list.edge_type == 3, "dash"] = "solid"

    for _, row in matrix_list.iterrows():
        graph.add_edges_from(
            [(row.row, row.column)],
            width=row.width,
            edge_type=row.edge_type,
            dash=row.dash,
        )

    return graph


def _remove_node_names_from_matrix(matrix_list):
    matrix_list = matrix_list.copy()
    matrix_list["row"] = matrix_list["row"].apply(lambda x: " ".join(x.split(" ")[:-1]))
    matrix_list["column"] = matrix_list["column"].apply(
        lambda x: " ".join(x.split(" ")[:-1])
    )
    return matrix_list


def _create_nodes(graph, node_names, node_sizes, textfont_sizes):
    nodes = [
        (node, {"size": occ, "textfont_size": textsize})
        for node, occ, textsize in zip(node_names, node_sizes, textfont_sizes)
    ]
    graph.add_nodes_from(nodes)
    return graph


def _compute_textfont_sizes(node_occ, textfont_size_min, textfont_size_max):
    textfont_sizes = np.array(node_occ)
    textfont_sizes = textfont_sizes - textfont_sizes.min() + textfont_size_min
    if textfont_sizes.max() > textfont_size_max:
        textfont_sizes = textfont_size_min + (textfont_sizes - textfont_size_min) / (
            textfont_sizes.max() - textfont_size_min
        ) * (textfont_size_max - textfont_size_min)
    return textfont_sizes


def _compute_node_sizes(node_occ, node_min_size, node_max_size):
    node_sizes = np.array(node_occ)
    node_sizes = node_sizes - node_sizes.min() + node_min_size
    if node_sizes.max() > node_max_size:
        node_sizes = node_min_size + (node_sizes - node_min_size) / (
            node_sizes.max() - node_min_size
        ) * (node_max_size - node_min_size)
    return node_sizes


def _extract_node_name(matrix_list):
    nodes = matrix_list["row"].drop_duplicates().to_list()
    nodes = [" ".join(node.split(" ")[:-1]) for node in nodes]
    return nodes


def _extract_node_occ(matrix_list):
    nodes = matrix_list["row"].drop_duplicates().to_list()
    occ = [node.split(" ")[-1] for node in nodes]
    occ = [node.split(":")[0] for node in occ]
    occ = [int(node) for node in occ]
    return occ


def _melt_matrix(matrix):
    matrix = matrix.melt(value_name="CORR", var_name="column", ignore_index=False)
    matrix = matrix.reset_index()
    matrix = matrix.rename(columns={"index": "row"})
    matrix = matrix[matrix.CORR > 0.0]
    return matrix
