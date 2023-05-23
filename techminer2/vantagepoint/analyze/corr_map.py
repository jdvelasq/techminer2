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

from ... import network_utils
from .list_cells_in_matrix import list_cells_in_matrix


@dataclass(init=False)
class _Chart:
    plot_: None
    table_: None
    prompt_: None


def corr_map(
    matrix,
    nx_k=0.5,
    nx_iterations=10,
    delta=1.0,
    node_min_size=30,
    node_max_size=70,
    textfont_size_min=10,
    textfont_size_max=20,
    seed=0,
):
    """Correlation map."""

    matrix_list = list_cells_in_matrix(matrix)

    graph = nx.Graph()
    graph = network_utils.create_graph_nodes(graph, matrix_list)
    graph = network_utils.create_occ_node_property(graph)
    graph = network_utils.compute_prop_sizes(
        graph, "node_size", node_min_size, node_max_size
    )
    graph = network_utils.compute_prop_sizes(
        graph, "textfont_size", textfont_size_min, textfont_size_max
    )
    graph = network_utils.create_graph_edges(graph, matrix_list)

    graph = network_utils.set_edge_properties_for_corr_maps(graph)

    graph = network_utils.compute_spring_layout(
        graph, nx_k, nx_iterations, seed
    )

    node_trace = network_utils.create_node_trace(graph)
    text_trace = network_utils.create_text_trace(graph)
    edge_traces = network_utils.create_edge_traces(graph)

    fig = network_utils.create_network_graph(
        edge_traces, node_trace, text_trace, delta
    )

    chart = _Chart()
    chart.plot_ = fig
    chart.table_ = matrix_list.matrix_list_
    chart.prompt_ = matrix_list.prompt_

    return chart

    # nodes = network_utils.create_nodes_from_matrix(obj)
    # nodes = network_utils.create_occ_from_index(nodes)

    # matrix_list = network_utils.melt_matrix_obj(obj)

    # node_occ = _extract_node_occ(matrix_list)
    # node_sizes = network_utils.compute_node_sizes(
    #     node_occ, node_min_size, node_max_size
    # )
    # textfont_sizes = network_utils.compute_textfont_sizes(
    #     node_occ, textfont_size_min, textfont_size_max
    # )
    # node_names = _extract_node_name(matrix_list)
    # matrix_list = _remove_node_names_from_matrix(matrix_list)

    # graph = nx.Graph()
    # graph = _create_nodes(graph, node_names, node_sizes, textfont_sizes)
    # graph = _create_edges(graph, matrix_list)
    # graph = network_utils.compute_graph_layout(
    #     graph, nx_k, nx_iterations, seed
    # )

    # edge_traces = _create_edge_traces(graph)
    #
    # text_trace = _create_text_trace(graph)

    # fig = _create_network_graph(edge_traces, node_trace, text_trace, delta)

    # chart = _Chart()
    # chart.plot_ = fig
    # chart.table_ = obj.matrix_
    # chart.prompt_ = obj.prompt_

    # return chart


# def _create_node_trace(graph):
#     """Create node trace for network graph."""

#     node_x, node_y = network_utils.extract_node_coordinates(graph)
#     node_sizes = network_utils.extract_node_sizes(graph)
#     node_trace = go.Scatter(
#         x=node_x,
#         y=node_y,
#         mode="markers",
#         hoverinfo="text",
#         marker=dict(
#             color="#8da4b4",
#             size=node_sizes,
#             line={"width": 1.5, "color": "white"},
#             opacity=1,
#         ),
#     )

#     return node_trace


# def _create_graph_edges(graph, matrix_list):
#     matrix_list = matrix_list.copy()
#     matrix_list = matrix_list[matrix_list["row"] < matrix_list["column"]]

#     matrix_list["edge_type"] = 0
#     matrix_list.loc[
#         (matrix_list.CORR > 0.25) & (matrix_list.CORR <= 0.5), "edge_type"
#     ] = 1
#     matrix_list.loc[
#         (matrix_list.CORR > 0.50) & (matrix_list.CORR <= 0.75), "edge_type"
#     ] = 2
#     matrix_list.loc[(matrix_list.CORR > 0.75), "edge_type"] = 3

#     matrix_list["width"] = 2
#     matrix_list.loc[matrix_list.edge_type == 1, "width"] = 2
#     matrix_list.loc[matrix_list.edge_type == 2, "width"] = 4
#     matrix_list.loc[matrix_list.edge_type == 3, "width"] = 6

#     matrix_list["dash"] = "dot"
#     matrix_list.loc[matrix_list.edge_type == 1, "dash"] = "solid"
#     matrix_list.loc[matrix_list.edge_type == 2, "dash"] = "solid"
#     matrix_list.loc[matrix_list.edge_type == 3, "dash"] = "solid"

#     for _, row in matrix_list.iterrows():
#         graph.add_edges_from(
#             [(row.row, row.column)],
#             width=row.width,
#             edge_type=row.edge_type,
#             dash=row.dash,
#         )

#     return graph


# def _create_nodes(graph, node_names, node_sizes, textfont_sizes):
#     nodes = [
#         (node, {"size": occ, "textfont_size": textsize})
#         for node, occ, textsize in zip(node_names, node_sizes, textfont_sizes)
#     ]
#     graph.add_nodes_from(nodes)
#     return graph


# def _create_text_trace(graph):
#     """Create text trace for network graph."""

#     node_x, node_y = network_utils.extract_node_coordinates(graph)
#     node_names = network_utils.extract_node_names(graph)
#     textfont_sizes = network_utils.extract_textfont_sizes(graph)
#     textposition = network_utils.compute_textposition(node_x, node_y)

#     node_sizes = network_utils.extract_node_sizes(graph)
#     node_sizes = [size - 12 for size in node_sizes]

#     text_trace = go.Scatter(
#         x=node_x,
#         y=node_y,
#         mode="markers+text",
#         text=node_names,
#         hoverinfo="text",
#         marker={
#             "color": "#8da4b4",
#             "size": node_sizes,
#             "line": {"width": 0, "color": "#8da4b4"},
#             "opacity": 1,
#         },
#         textposition=textposition,
#         textfont={"size": textfont_sizes},
#     )

#     return text_trace


# def _create_edge_traces(graph):
#     #
#     def _create_edge_trace(graph, edge_type):
#         edge_trace = go.Scatter(
#             x=[],
#             y=[],
#             line={"color": "#8da4b4"},
#             hoverinfo="none",
#             mode="lines",
#         )

#         found = False
#         for edge in graph.edges():
#             pos_x0, pos_y0 = graph.nodes[edge[0]]["pos"]
#             pos_x1, pos_y1 = graph.nodes[edge[1]]["pos"]

#             width = graph.edges[edge]["width"]
#             dash = graph.edges[edge]["dash"]
#             type_ = graph.edges[edge]["edge_type"]

#             if type_ == edge_type:
#                 found = True
#                 edge_trace["line"]["width"] = width
#                 edge_trace["line"]["dash"] = dash
#                 edge_trace["x"] += (pos_x0, pos_x1, None)
#                 edge_trace["y"] += (pos_y0, pos_y1, None)

#         if found:
#             return edge_trace
#         else:
#             return None

#     result = []
#     for edge_type in [0, 1, 2, 3]:
#         edge_trace = _create_edge_trace(graph, edge_type)
#         if edge_trace:
#             result.append(edge_trace)
#     return result


# def _remove_node_names_from_matrix(matrix_list):
#     matrix_list = matrix_list.copy()
#     matrix_list["row"] = matrix_list["row"].apply(
#         lambda x: " ".join(x.split(" ")[:-1])
#     )
#     matrix_list["column"] = matrix_list["column"].apply(
#         lambda x: " ".join(x.split(" ")[:-1])
#     )
#     return matrix_list


# def _extract_node_name(matrix_list):
#     nodes = matrix_list["row"].drop_duplicates().to_list()
#     nodes = [" ".join(node.split(" ")[:-1]) for node in nodes]
#     return nodes


# def _extract_node_occ(matrix_list):
#     nodes = matrix_list["row"].drop_duplicates().to_list()
#     occ = [node.split(" ")[-1] for node in nodes]
#     occ = [node.split(":")[0] for node in occ]
#     occ = [int(node) for node in occ]
#     return occ
