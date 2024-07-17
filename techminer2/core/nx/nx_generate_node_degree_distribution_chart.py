# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Network Deegre Plot
===============================================================================

# * Preparation

# >>> import techminer2 as tm2
# >>> root_dir = "data/regtech/"

# * Object oriented interface

# >>> degree_plot = (
# ...     tm2p.records(root_dir=root_dir)
# ...     .co_occurrence_matrix(
# ...         columns='author_keywords',
# ...         col_top_n=20,
# ...     )
# ...     .network_create(
# ...         algorithm_or_estimator="louvain"
# ...     )
# ...     .network_degree_plot()
# ... )
# >>> degree_plot
# NetworkDegreePlot()


# * Functional interface

# >>> cooc_matrix = tm2p.co_occurrence_matrix(
# ...    columns='author_keywords',
# ...    col_top_n=20,
# ...    root_dir=root_dir,
# ... )
# >>> network = tm2p.network_create(
# ...     cooc_matrix,
# ...     algorithm_or_estimator='louvain',
# ... )
# >>> degree_plot = network_degree_plot(network)
# >>> degree_plot
# NetworkDegreePlot()


# * Results

# >>> degree_plot.fig_.write_html("sphinx/_static/network_degree_plot.html")

# .. raw:: html

#     <iframe src="../../_static/network_degree_plot.html"   height="600px" width="100%" frameBorder="0"></iframe>

# >>> degree_plot.df_.head()
#    Node                          Name  Degree
# 0     0                REGTECH 28:329      19
# 1     1                FINTECH 12:249      13
# 2     2             COMPLIANCE 07:030      10
# 3     3             REGULATION 05:164      10
# 4     4  REGULATORY_TECHNOLOGY 07:037       9

# >>> print(degree_plot.prompt_)
# Your task is to generate an analysis about the degree of the nodes in a \\
# networkx graph of a co-ocurrence matrix. Analyze the table below, delimited \\
# by triple backticks, identifying any notable patterns, trends, or outliers \\
# in the data, and discuss their implications in the network.
# <BLANKLINE>
# Table:
# ```
# |    |   Node | Name                           |   Degree |
# |---:|-------:|:-------------------------------|---------:|
# |  0 |      0 | REGTECH 28:329                 |       19 |
# |  1 |      1 | FINTECH 12:249                 |       13 |
# |  2 |      2 | COMPLIANCE 07:030              |       10 |
# |  3 |      3 | REGULATION 05:164              |       10 |
# |  4 |      4 | REGULATORY_TECHNOLOGY 07:037   |        9 |
# |  5 |      5 | ARTIFICIAL_INTELLIGENCE 04:023 |        9 |
# |  6 |      6 | RISK_MANAGEMENT 03:014         |        8 |
# |  7 |      7 | BLOCKCHAIN 03:005              |        6 |
# |  8 |      8 | SUPTECH 03:004                 |        6 |
# |  9 |      9 | ANTI_MONEY_LAUNDERING 05:034   |        5 |
# | 10 |     10 | FINANCIAL_REGULATION 04:035    |        5 |
# | 11 |     11 | INNOVATION 03:012              |        5 |
# | 12 |     12 | FINANCIAL_SERVICES 04:168      |        4 |
# | 13 |     13 | SEMANTIC_TECHNOLOGIES 02:041   |        4 |
# | 14 |     14 | CHARITYTECH 02:017             |        4 |
# | 15 |     15 | ENGLISH_LAW 02:017             |        4 |
# | 16 |     16 | DATA_PROTECTION 02:027         |        3 |
# | 17 |     17 | ACCOUNTABILITY 02:014          |        3 |
# | 18 |     18 | DATA_PROTECTION_OFFICER 02:014 |        3 |
# | 19 |     19 | SMART_CONTRACTS 02:022         |        2 |
# ```
# <BLANKLINE>


"""
from dataclasses import dataclass

import pandas as pd
import plotly.express as px

from ...helpers.format_prompt_for_dataframes import format_prompt_for_dataframes
from .nx_assign_degree_to_nodes import nx_assign_degree_to_nodes


def nx_generate_node_degree_distribution_chart(
    #
    # NX GRAPH:
    nx_graph,
    #
    # CHART PARAMS:
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

        return format_prompt_for_dataframes(main_text, table.to_markdown())

    #
    #
    # MAIN CODE:
    #
    #

    nx_graph = nx_assign_degree_to_nodes(nx_graph)
    degrees = collect_degrees(nx_graph)
    dataframe = to_dataframe(degrees)
    dataframe = dataframe[["Node", "Name", "Degree"]]
    fig = plot(dataframe, textfont_size, yshift)
    prompt = generate_chatgpt_prompt(dataframe)

    @dataclass
    class Results:
        fig_ = fig
        df_ = dataframe
        prompt_ = prompt

    return Results()
