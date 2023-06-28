# flake8: noqa
"""
Network Deegre Plot
===============================================================================


>>> root_dir = "data/regtech/"

>>> import techminer2plus
>>> file_name = "sphinx/_static/network_degree_plot.html"
>>> cooc_matrix = techminer2plus.co_occurrence_matrix(
...    columns='author_keywords',
...    col_top_n=20,
...    root_dir=root_dir,
... )
>>> graph = techminer2plus.network_clustering(
...    cooc_matrix,
...    algorithm_or_estimator='louvain',
... )
>>> chart = techminer2plus.network_degree_plot(graph)
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/network_degree_plot.html"
    height="600px" width="100%" frameBorder="0"></iframe>




>>> print(chart.prompt_)
Your task is to generate an analysis about the degree of the nodes in a \\
networkx graph of a co-ocurrence matrix. Analyze the table below, delimited \\
by triple backticks, identifying any notable patterns, trends, or outliers \\
in the data, and discuss their implications in the network.
<BLANKLINE>
Table:
```
|    |   Node | Name                           |   Degree |
|---:|-------:|:-------------------------------|---------:|
|  0 |      0 | REGTECH 28:329                 |       19 |
|  1 |      1 | FINTECH 12:249                 |       13 |
|  2 |      2 | COMPLIANCE 07:030              |       10 |
|  3 |      3 | REGULATION 05:164              |       10 |
|  4 |      4 | REGULATORY_TECHNOLOGY 07:037   |        9 |
|  5 |      5 | ARTIFICIAL_INTELLIGENCE 04:023 |        9 |
|  6 |      6 | RISK_MANAGEMENT 03:014         |        8 |
|  7 |      7 | BLOCKCHAIN 03:005              |        6 |
|  8 |      8 | SUPTECH 03:004                 |        6 |
|  9 |      9 | ANTI_MONEY_LAUNDERING 05:034   |        5 |
| 10 |     10 | FINANCIAL_REGULATION 04:035    |        5 |
| 11 |     11 | INNOVATION 03:012              |        5 |
| 12 |     12 | FINANCIAL_SERVICES 04:168      |        4 |
| 13 |     13 | SEMANTIC_TECHNOLOGIES 02:041   |        4 |
| 14 |     14 | CHARITYTECH 02:017             |        4 |
| 15 |     15 | ENGLISH_LAW 02:017             |        4 |
| 16 |     16 | DATA_PROTECTION 02:027         |        3 |
| 17 |     17 | ACCOUNTABILITY 02:014          |        3 |
| 18 |     18 | DATA_PROTECTION_OFFICER 02:014 |        3 |
| 19 |     19 | SMART_CONTRACTS 02:022         |        2 |
```
<BLANKLINE>



# pylint: disable=line-too-long
"""

import pandas as pd
import plotly.express as px

from .chatbot_prompts import format_chatbot_prompt_for_df
from .classes import NetworkDegreePlot
from .network_lib import nx_compute_node_degree


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

        main_text = (
            "Your task is to generate an analysis about the degree of the nodes in a networkx "
            "graph of a co-ocurrence matrix. Analyze the table below, delimited by triple "
            "backticks, identifying any notable patterns, trends, or outliers in the data, and "
            "discuss their implications in the network."
        )

        return format_chatbot_prompt_for_df(main_text, table.to_markdown())

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
