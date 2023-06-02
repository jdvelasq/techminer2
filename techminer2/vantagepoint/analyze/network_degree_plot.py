"""
Network Deegre Plot
===============================================================================


>>> root_dir = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> file_name = "sphinx/_static/vantagepoint__network_degree_plot.html"
>>> co_occ_matrix = vantagepoint.analyze.co_occ_matrix(
...    columns='author_keywords',
...    col_occ_range=(3, None),
...    root_dir=root_dir,
... )
>>> normalized_co_occ_matrix = vantagepoint.analyze.association_index(
...     co_occ_matrix, "association"
... )
>>> graph = vantagepoint.analyze.cluster_criterion(
...    normalized_co_occ_matrix,
...    community_clustering='louvain',
... )
>>> chart = vantagepoint.analyze.network_degree_plot(graph)
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/vantagepoint__network_degree_plot.html"
    height="600px" width="100%" frameBorder="0"></iframe>




>>> print(chart.prompt_)
Analyze the table below, which provides the degree of nodes in a networkx graph of a co-ocurrence matrix. Identify any notable patterns, trends, or outliers in the data, and discuss their implications in the network.
<BLANKLINE>
|    | Name                           |   Degree |   Node |
|---:|:-------------------------------|---------:|-------:|
|  0 | regtech 28:329                 |       12 |      0 |
|  1 | fintech 12:249                 |       11 |      1 |
|  2 | regulatory technology 07:037   |        9 |      2 |
|  3 | regulation 05:164              |        9 |      3 |
|  4 | compliance 07:030              |        8 |      4 |
|  5 | artificial intelligence 04:023 |        7 |      5 |
|  6 | risk management 03:014         |        7 |      6 |
|  7 | suptech 03:004                 |        6 |      7 |
|  8 | blockchain 03:005              |        5 |      8 |
|  9 | innovation 03:012              |        5 |      9 |
| 10 | financial regulation 04:035    |        4 |     10 |
| 11 | financial services 04:168      |        4 |     11 |
| 12 | anti-money laundering 03:021   |        3 |     12 |
<BLANKLINE>
<BLANKLINE>



"""

import pandas as pd
import plotly.express as px

from ...classes import NetworkDegreePlot
from ...network_utils import compute_node_degree


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

    graph = compute_node_degree(graph)
    degrees = collect_degrees(graph)
    dataframe = to_dataframe(degrees)
    fig = plot(dataframe, textfont_size, yshift)

    obj = NetworkDegreePlot()
    obj.plot_ = fig
    obj.graph_ = graph
    obj.table_ = dataframe
    obj.prompt_ = generate_chatgpt_prompt(dataframe)

    return obj
