"""
Network deegre plot
===============================================================================


>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> file_name = "sphinx/_static/vantagepoint__network_degree_plot.html"
>>> co_occ_matrix = vantagepoint.analyze.co_occ_matrix(
...    criterion='author_keywords',
...    topic_min_occ=2,
...    directory=directory,
... )
>>> chart = vantagepoint.analyze.network_degree_plot(co_occ_matrix)
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/vantagepoint__network_degree_plot.html"
    height="600px" width="100%" frameBorder="0"></iframe>

>>> chart.table_.head()
                           Name  Degree  Node
0                regtech 28:329      24     0
1                fintech 12:249      15     1
2             compliance 07:030      13     2
3             regulation 05:164      13     3
4  regulatory technology 07:037      11     4

>>> print(chart.prompt_)
Analyze the table below, which provides the degree of nodes in a networkx \
graph of a co-ocurrence matrix. Identify any notable patterns, trends, or \
outliers in the data, and discuss their implications in the network.
<BLANKLINE>
|    | Name                               |   Degree |   Node |
|---:|:-----------------------------------|---------:|-------:|
|  0 | regtech 28:329                     |       24 |      0 |
|  1 | fintech 12:249                     |       15 |      1 |
|  2 | compliance 07:030                  |       13 |      2 |
|  3 | regulation 05:164                  |       13 |      3 |
|  4 | regulatory technology 07:037       |       11 |      4 |
|  5 | reporting 02:001                   |       10 |      5 |
|  6 | artificial intelligence 04:023     |        9 |      6 |
|  7 | risk management 03:014             |        9 |      7 |
|  8 | financial regulation 04:035        |        8 |      8 |
|  9 | financial services 04:168          |        7 |      9 |
| 10 | blockchain 03:005                  |        7 |     10 |
| 11 | suptech 03:004                     |        7 |     11 |
| 12 | finance 02:001                     |        7 |     12 |
| 13 | innovation 03:012                  |        6 |     13 |
| 14 | anti-money laundering 03:021       |        5 |     14 |
| 15 | sandbox 02:012                     |        5 |     15 |
| 16 | accountability 02:014              |        4 |     16 |
| 17 | charitytech 02:017                 |        4 |     17 |
| 18 | data protection officer 02:014     |        4 |     18 |
| 19 | english law 02:017                 |        4 |     19 |
| 20 | gdpr 02:014                        |        4 |     20 |
| 21 | semantic technologies 02:041       |        4 |     21 |
| 22 | data protection 02:027             |        3 |     22 |
| 23 | smart contracts 02:022             |        2 |     23 |
| 24 | technology 02:010                  |        2 |     24 |
| 25 | anti money laundering (aml) 02:013 |        1 |     25 |
<BLANKLINE>
<BLANKLINE>




"""
from dataclasses import dataclass

import networkx as nx
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

from ... import network_utils
from .list_cells_in_matrix import list_cells_in_matrix


@dataclass(init=False)
class _NetworkDegreePlot:
    graph_: nx.Graph
    plot_: go.Figure
    table_: pd.DataFrame
    prompt_: str


def network_degree_plot(
    matrix,
    textfont_size=8,
    yshift=3,
):
    """Compute and plots the degree of a co-occurrence matrix."""

    def collect_degrees(graph):
        """Collects the degrees of a graph as a sorted list."""

        degrees = []
        for node in graph.nodes():
            degrees.append((node, graph.nodes[node]["degree"]))
        degrees = sorted(degrees, key=lambda x: x[1], reverse=True)

        return degrees

    def to_dataframe(degrees):
        """Converts a list of degrees to a dataframe."""

        data = pd.DataFrame(degrees, columns=["Name", "Degree"])
        data["Node"] = data.index

        return data

    def plot(data, textfont_size, yshift):
        """Plots the degree of a co-occurrence matrix."""

        fig = px.line(
            data,
            x="Node",
            y="Degree",
            hover_data="Name",
            markers=True,
        )
        fig.update_traces(
            marker=dict(size=5, line={"color": "black", "width": 1}),
            marker_color="black",
            line=dict(color="black", width=1),
        )
        fig.update_layout(
            paper_bgcolor="white",
            plot_bgcolor="white",
        )
        fig.update_yaxes(
            linecolor="gray",
            linewidth=2,
            gridcolor="lightgray",
            griddash="dot",
            title="Degree",
        )
        fig.update_xaxes(
            linecolor="gray",
            linewidth=2,
            gridcolor="lightgray",
            griddash="dot",
            title="Node",
        )

        for _, row in data.iterrows():
            fig.add_annotation(
                x=row["Node"],
                y=row["Degree"],
                text=row["Name"],
                showarrow=False,
                textangle=-90,
                yanchor="bottom",
                font={"size": textfont_size},
                yshift=yshift,
            )

        return fig

    def generate_chatgpt_prompt(table):
        """Generates a chatgpt prompt."""

        prompt = (
            "Analyze the table below, which provides the degree of nodes in a "
            "networkx graph of a co-ocurrence matrix. Identify any notable "
            "patterns, trends, or outliers in the data, and discuss their "
            "implications in the network."
            f"\n\n{table.to_markdown()}\n\n"
        )

        return prompt

    #
    #
    # Main:
    #
    #

    matrix_list = list_cells_in_matrix(matrix)
    graph = network_utils.create_graph(matrix_list)
    graph = network_utils.compute_node_degree(graph)
    degrees = collect_degrees(graph)
    dataframe = to_dataframe(degrees)
    fig = plot(dataframe, textfont_size, yshift)

    obj = _NetworkDegreePlot()
    obj.plot_ = fig
    obj.graph_ = graph
    obj.table_ = dataframe
    obj.prompt_ = generate_chatgpt_prompt(dataframe)

    return obj
