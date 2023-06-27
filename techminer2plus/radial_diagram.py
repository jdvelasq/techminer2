# flake8: noqa
"""
Radial Diagram
===============================================================================

A radial diagram is a visualization technique that displays the associations
between a term and other terms in a co-occurrence matrix. The radial diagram
is a network graph in which the nodes are the terms and the edges are the
co-occurrence between the terms. The radial diagram is a useful tool for
identifying the most relevant terms associated with a given term.



>>> import techminer2plus
>>> cooc_matrix = techminer2plus.analyze.matrix.co_occurrence_matrix(
...     root_dir="data/regtech/",
...     columns='author_keywords',
...     col_top_n=20,
... )

>>> file_name = "sphinx/_static/analyze/associations/radial_diagram.html"
>>> chart = techminer2plus.analyze.associations.radial_diagram(
...     item="REGTECH",
...     cooc_matrix=cooc_matrix,
...     nx_k=None,
...     nx_iterations=20,
... )

>>> chart.item_name_
'REGTECH 28:329'

>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../_static/analyze/associations/radial_diagram.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> chart.series_
author_keywords
FINTECH 12:249                    12
REGULATORY_TECHNOLOGY 07:037       2
COMPLIANCE 07:030                  7
REGULATION 05:164                  4
ANTI_MONEY_LAUNDERING 05:034       1
FINANCIAL_SERVICES 04:168          3
FINANCIAL_REGULATION 04:035        2
ARTIFICIAL_INTELLIGENCE 04:023     2
RISK_MANAGEMENT 03:014             2
INNOVATION 03:012                  1
BLOCKCHAIN 03:005                  2
SUPTECH 03:004                     3
SEMANTIC_TECHNOLOGIES 02:041       2
DATA_PROTECTION 02:027             2
SMART_CONTRACTS 02:022             2
CHARITYTECH 02:017                 2
ENGLISH_LAW 02:017                 2
ACCOUNTABILITY 02:014              2
DATA_PROTECTION_OFFICER 02:014     2
Name: REGTECH 28:329, dtype: int64

>>> print(chart.prompt_)
Your task is to generate a short analysis of a table for a research paper. \\
Summarize the table below, delimited by triple backticks, in one unique \\
paragraph with at most 30 words. The table contains the values of co- \\
occurrence (OCC) of the 'REGTECH' with the 'author_keywords' field in a \\
bibliographic dataset. Identify any notable patterns, trends, or outliers \\
in the data, and discuss their implications for the research field. Be sure \\
to provide a concise summary of your findings.
<BLANKLINE>
Table:
```
| author_keywords                |   REGTECH 28:329 |
|:-------------------------------|-----------------:|
| FINTECH 12:249                 |               12 |
| REGULATORY_TECHNOLOGY 07:037   |                2 |
| COMPLIANCE 07:030              |                7 |
| REGULATION 05:164              |                4 |
| ANTI_MONEY_LAUNDERING 05:034   |                1 |
| FINANCIAL_SERVICES 04:168      |                3 |
| FINANCIAL_REGULATION 04:035    |                2 |
| ARTIFICIAL_INTELLIGENCE 04:023 |                2 |
| RISK_MANAGEMENT 03:014         |                2 |
| INNOVATION 03:012              |                1 |
| BLOCKCHAIN 03:005              |                2 |
| SUPTECH 03:004                 |                3 |
| SEMANTIC_TECHNOLOGIES 02:041   |                2 |
| DATA_PROTECTION 02:027         |                2 |
| SMART_CONTRACTS 02:022         |                2 |
| CHARITYTECH 02:017             |                2 |
| ENGLISH_LAW 02:017             |                2 |
| ACCOUNTABILITY 02:014          |                2 |
| DATA_PROTECTION_OFFICER 02:014 |                2 |
```
<BLANKLINE>



# pylint: disable=line-too-long
"""
import networkx as nx

# from ...classes import RadialDiagram
# from ...network_lib import (
#     nx_compute_node_property_from_occ,
#     nx_compute_spring_layout,
#     nx_create_node_occ_property_from_node_name,
#     px_add_names_to_fig_nodes,
#     px_create_edge_traces,
#     px_create_network_fig,
#     px_create_node_trace,
# )
# from .item_associations import item_associations


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def radial_diagram(
    item,
    cooc_matrix,
    #
    # Figure params:
    n_labels=None,
    nx_k=None,
    nx_iterations=30,
    nx_random_state=0,
    node_size_min=30,
    node_size_max=70,
    textfont_size_min=10,
    textfont_size_max=20,
    xaxes_range=None,
    yaxes_range=None,
    show_axes=False,
):
    """Plots a radial diagram."""

    def create_graph(
        name,
        series,
        node_size_min,
        node_size_max,
        textfont_size_min,
        textfont_size_max,
    ):
        """Creates a networkx graph."""
        graph = nx.Graph()

        # Adds the central item
        nodes = [
            (name, {"group": 0, "color": "#556f81", "textfont_color": "black"})
        ]

        # Adds the items in the column as nodes
        nodes += [
            (
                index,
                {"group": 1, "color": "#8da4b4", "textfont_color": "black"},
            )
            for index in series.index.to_list()
        ]
        graph.add_nodes_from(nodes)

        # Sets node properties
        graph = nx_create_node_occ_property_from_node_name(graph)
        graph = nx_compute_node_property_from_occ(
            graph, "node_size", node_size_min, node_size_max
        )
        graph = nx_compute_node_property_from_occ(
            graph, "textfont_size", textfont_size_min, textfont_size_max
        )

        for index, value in series.items():
            graph.add_edges_from(
                [(name, index)],
                value=value,
                width=2,
                dash="solid",
                color="#8da4b4",
            )

        return graph

    #
    # Main code:
    #
    name, series, _, prompt = item_associations(
        item=item, cooc_matrix=cooc_matrix
    )

    graph = create_graph(
        name=name,
        series=series,
        node_size_min=node_size_min,
        node_size_max=node_size_max,
        textfont_size_min=textfont_size_min,
        textfont_size_max=textfont_size_max,
    )

    graph = nx_compute_spring_layout(
        graph, nx_k, nx_iterations, nx_random_state
    )

    node_trace = px_create_node_trace(graph)
    edge_traces = px_create_edge_traces(graph)

    fig = px_create_network_fig(
        edge_traces,
        node_trace,
        xaxes_range,
        yaxes_range,
        show_axes,
    )

    fig = px_add_names_to_fig_nodes(fig, graph, n_labels, is_article=False)

    radial_diagram_ = RadialDiagram()
    radial_diagram_.plot_ = fig
    radial_diagram_.graph_ = graph
    radial_diagram_.series_ = series.copy()
    radial_diagram_.item_name_ = name
    radial_diagram_.prompt_ = prompt

    return radial_diagram_
