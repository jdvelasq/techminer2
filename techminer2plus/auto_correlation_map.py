# flake8: noqa
"""
.. _auto_correlation_map:

Auto-correlation Map
===============================================================================

Creates an Auto-correlation Map.


>>> root_dir = "data/regtech/"

>>> file_name = "sphinx/_static/auto_correlation_map.html"

>>> import techminer2plus
>>> auto_corr_matrix = techminer2plus.auto_correlation_matrix(
...     rows_and_columns='authors',
...     occ_range=(2, None),
...     root_dir=root_dir,
... )

>>> corr_map =  techminer2plus.auto_correlation_map(
...     auto_corr_matrix,
...     color="#1f77b4", # tab:blue
... )
>>> corr_map
AutoCorrMap(rows-and-columns='authors')

>>> corr_map.fig_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/auto_correlation_map.html" height="600px" width="100%" frameBorder="0"></iframe>





# pylint: disable=line-too-long
"""
import textwrap
from dataclasses import dataclass

import pandas as pd
import plotly.graph_objs as go

from ._network_lib import (
    nx_compute_spring_layout,
    nx_create_graph_from_matrix_list,
    nx_set_edge_properties_for_corr_maps,
    px_add_names_to_fig_nodes,
    px_create_edge_traces,
    px_create_network_fig,
    px_create_node_trace,
)
from .list_cells_in_matrix import list_cells_in_matrix


@dataclass
class AutoCorrMap:
    """Auto-correlation map.

    :meta private:
    """

    fig_: go.Figure
    df_: pd.DataFrame
    rows_and_columns_: str

    def __repr__(self):
        text = "AutoCorrMap("
        text += f"rows-and-columns='{self.rows_and_columns_}'"
        text += ")"
        text = textwrap.fill(text, width=75, subsequent_indent="    ")
        return text


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def auto_correlation_map(
    auto_corr_matrix,
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
    """Auto-correlation Map."""

    matrix_list = list_cells_in_matrix(auto_corr_matrix)

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

    return AutoCorrMap(
        fig_=fig,
        df_=matrix_list.df_,
        rows_and_columns_=auto_corr_matrix.rows_and_columns_,
    )
