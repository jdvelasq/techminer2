# flake8: noqa
"""
Radial Diagram
===============================================================================

A radial diagram is a visualization technique that displays the associations
between a term and other terms in a co-occurrence matrix. The radial diagram
is a network graph in which the nodes are the terms and the edges are the
co-occurrence between the terms. The radial diagram is a useful tool for
identifying the most relevant terms associated with a given term.


>>> ROOT_DIR = "data/regtech/"
>>> file_name = "sphinx/_static/analyze/associations/radial_diagram.html"

>>> import techminer2plus 
>>> chart = techminer2plus.analyze.associations.radial_diagram(
...     root_dir=ROOT_DIR,
...     item="REGTECH",
...     columns='author_keywords',
...     col_occ_range=(3, None),
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
Name: REGTECH 28:329, dtype: int64

# pylint: disable=line-too-long
"""
import networkx as nx

from ...classes import RadialDiagram
from ...network import (
    nx_compute_node_property_from_occ,
    nx_compute_spring_layout,
    nx_create_node_occ_property_from_node_name,
    px_add_names_to_fig_nodes,
    px_create_edge_traces,
    px_create_network_fig,
    px_create_node_trace,
)
from ..matrix import co_occurrence_matrix


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def radial_diagram(
    item,
    obj=None,
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
    #
    # Co-occ matrix params:
    columns=None,
    rows=None,
    #
    # Columns item filters:
    col_top_n=None,
    col_occ_range=None,
    col_gc_range=None,
    col_custom_items=None,
    #
    # Rows item filters :
    row_top_n=None,
    row_occ_range=None,
    row_gc_range=None,
    row_custom_items=None,
    #
    # Database params:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Plots a radial diagram."""

    def compute_obj(obj):
        if obj is not None:
            return obj
        return co_occurrence_matrix(
            columns=columns,
            rows=rows,
            #
            # Columns item filters:
            col_top_n=col_top_n,
            col_occ_range=col_occ_range,
            col_gc_range=col_gc_range,
            col_custom_items=col_custom_items,
            #
            # Rows item filters :
            row_top_n=row_top_n,
            row_occ_range=row_occ_range,
            row_gc_range=row_gc_range,
            row_custom_items=row_custom_items,
            #
            # Database params:
            root_dir=root_dir,
            database=database,
            year_filter=year_filter,
            cited_by_filter=cited_by_filter,
            **filters,
        )

    def extract_item_position_and_name(candidate_items, item):
        """Obtains the positions of topics in a list."""

        org_candidate_items = candidate_items[:]
        candidate_items = [col.split(" ")[:-1] for col in candidate_items]
        candidate_items = [" ".join(col) for col in candidate_items]
        pos = candidate_items.index(item)
        name = org_candidate_items[pos]
        return pos, name

    def extract_item_column_from_coc_matrix(obj, pos, name):
        matrix = obj.matrix_.copy()
        series = matrix.iloc[:, pos]
        series = series.drop(labels=[name], axis=0, errors="ignore")
        series = series[series > 0]
        series.index.name = obj.rows_
        return series

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
    obj = compute_obj(obj)
    pos, name = extract_item_position_and_name(obj.matrix_.columns, item)
    series = extract_item_column_from_coc_matrix(obj, pos, name)

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

    return radial_diagram_
