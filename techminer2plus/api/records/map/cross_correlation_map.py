# flake8: noqa
"""
.. _cross_correlation_map:

Cross-correlation Map
===============================================================================

Creates an Cross-correlation Map.



>>> root_dir = "data/regtech/"

>>> file_name = "sphinx/_static/cross_correlation_map.html"

>>> import techminer2plus
>>> cross_corr_matrix = techminer2plus.cross_correlation_matrix(
...     rows_and_columns='authors', 
...     cross_with='countries',
...     top_n=10,
...     root_dir=root_dir,
... )
>>> corr_map = techminer2plus.cross_correlation_map(
...     cross_corr_matrix,
...     color="#1f77b4", # tab:blue
... )
>>> corr_map
CrossCorrMap(rows-and-columns='authors'cross-wtih='countries')

>>> corr_map.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/cross_correlation_map.html" height="600px" width="100%" frameBorder="0"></iframe>

    




# pylint: disable=line-too-long
"""
import textwrap
from dataclasses import dataclass

import pandas as pd
import plotly.graph_objs as go

from ....network_lib import (
    nx_compute_spring_layout,
    nx_create_graph_from_matrix_list,
    nx_set_edge_properties_for_corr_maps,
    px_add_names_to_fig_nodes,
    px_create_edge_traces,
    px_create_network_fig,
    px_create_node_trace,
)
from ..matrix.co_occurrence_matrix.list_cells_in_matrix import (
    list_cells_in_matrix,
)


@dataclass
class CrossCorrMap:
    """Auto-correlation map.

    :meta private:
    """

    plot_: go.Figure
    table_: pd.DataFrame
    rows_and_columns_: str
    cross_with_: str

    def __repr__(self):
        text = "CrossCorrMap("
        text += f"rows-and-columns='{self.rows_and_columns_}'"
        text += f"cross-wtih='{self.cross_with_}'"
        text += ")"
        text = textwrap.fill(text, width=75, subsequent_indent="    ")
        return text


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def cross_correlation_map(
    cross_corr_matrix,
    #
    # Map params:
    n_labels=None,
    color="#8da4b4",
    nx_k=None,
    nx_iterations=10,
    nx_random_state=0,
    node_size_min=30,
    node_size_max=70,
    textfont_size_min=10,
    textfont_size_max=20,
    xaxes_range=None,
    yaxes_range=None,
    show_axes=False,
):
    """Correlation map."""

    matrix_list = list_cells_in_matrix(cross_corr_matrix)

    graph = nx_create_graph_from_matrix_list(
        matrix_list,
        node_size_min,
        node_size_max,
        textfont_size_min,
        textfont_size_max,
    )

    for node in graph.nodes():
        graph.nodes[node]["color"] = color

    graph = nx_set_edge_properties_for_corr_maps(graph, color)

    graph = nx_compute_spring_layout(
        graph, nx_k, nx_iterations, nx_random_state
    )

    node_trace = px_create_node_trace(graph)
    # text_trace = network_utils.create_text_trace(graph)
    edge_traces = px_create_edge_traces(graph)

    fig = px_create_network_fig(
        edge_traces,
        node_trace,
        # text_trace,
        xaxes_range,
        yaxes_range,
        show_axes,
    )

    fig = px_add_names_to_fig_nodes(fig, graph, n_labels, is_article=False)

    return CrossCorrMap(
        plot_=fig,
        table_=matrix_list.df_,
        rows_and_columns_=cross_corr_matrix.rows_and_columns_,
        cross_with_=cross_corr_matrix.cross_with_,
    )
