# flake8: noqa
"""
(NEW) Network Deegre Plot
===============================================================================


>>> root_dir = "data/regtech/"

>>> import techminer2plus
>>> file_name = "sphinx/_static/techminer2plus__network_degree_plot.html"
>>> co_occ_matrix = techminer2plus.system.analyze.co_occ_matrix(
...    columns='author_keywords',
...    col_occ_range=(3, None),
...    root_dir=root_dir,
... )
>>> normalized_co_occ_matrix = techminer2plus.system.analyze.association_index(
...     co_occ_matrix, "association"
... )
>>> graph = techminer2plus.system.analyze.cluster_column(
...    normalized_co_occ_matrix,
...    community_clustering='louvain',
... )
>>> chart = techminer2plus.system.analyze.network_degree_plot(graph)
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/techminer2plus__network_degree_plot.html"
    height="600px" width="100%" frameBorder="0"></iframe>




>>> print(chart.prompt_)
Analyze the table below, which provides the degree of nodes in a networkx graph of a co-ocurrence matrix. Identify any notable patterns, trends, or outliers in the data, and discuss their implications in the network.
<BLANKLINE>
|    |   Node | Name                                   |   Degree |
|---:|-------:|:---------------------------------------|---------:|
|  0 |      0 | REGTECH 28:329                         |       12 |
|  1 |      1 | FINTECH 12:249                         |       11 |
|  2 |      2 | REGULATION 05:164                      |        9 |
|  3 |      3 | COMPLIANCE 07:030                      |        8 |
|  4 |      4 | ARTIFICIAL_INTELLIGENCE 04:023         |        7 |
|  5 |      5 | RISK_MANAGEMENT 03:014                 |        7 |
|  6 |      6 | REGULATORY_TECHNOLOGY 03:007           |        7 |
|  7 |      7 | SUPTECH 03:004                         |        6 |
|  8 |      8 | INNOVATION 03:012                      |        5 |
|  9 |      9 | BLOCKCHAIN 03:005                      |        5 |
| 10 |     10 | FINANCIAL_SERVICES 04:168              |        4 |
| 11 |     11 | FINANCIAL_REGULATION 04:035            |        4 |
| 12 |     12 | ANTI_MONEY_LAUNDERING 04:023           |        3 |
| 13 |     13 | REGULATORY_TECHNOLOGY (REGTECH) 04:030 |        2 |
<BLANKLINE>
<BLANKLINE>



# pylint: disable=line-too-long
"""

import pandas as pd
import plotly.express as px

from ...classes import NetworkDegreePlot
from ...network import nx_compute_node_degree


# pylint: disable=too-many-arguments
def network_degree_plot(
    graph,
    textfont_size=10,
    marker_size=7,
    line_color="black",
    line_width=1.5,
    yshift=4,
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
            marker={
                "size": marker_size,
                "line": {"color": line_color, "width": 0},
            },
            marker_color=line_color,
            line={"color": line_color, "width": line_width},
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
            "Your task is to generate an analysis about the degree of the nodes in a networkx \\\n"
            "graph of a co-ocurrence matrix. Analyze the table below, delimited by triple  \\\n"
            "backticks, identifying any notable patterns, trends, or outliers in the data, and  \\\n"
            "discuss their implications in the network. \n\n"
            f"Table:\n```\n{table.to_markdown()}\n```\n"
        )

        return prompt

    #
    #
    # Main:
    #
    #

    graph = nx_compute_node_degree(graph)
    degrees = collect_degrees(graph)
    dataframe = to_dataframe(degrees)
    dataframe = dataframe[["Node", "Name", "Degree"]]
    fig = plot(dataframe, textfont_size, yshift)

    obj = NetworkDegreePlot()
    obj.plot_ = fig
    obj.graph_ = graph
    obj.table_ = dataframe
    obj.prompt_ = generate_chatgpt_prompt(dataframe)

    return obj