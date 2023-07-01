# flake8: noqa
"""
.. _matrix_viewer:

Matrix Viewer
===============================================================================



>>> root_dir = "data/regtech/"

>>> file_name = "sphinx/_static/matrix_viewer_0.html"

>>> import techminer2plus 
>>> cooc_matrix = techminer2plus.co_occurrence_matrix(
...     columns='author_keywords',
...     rows='authors',
...     col_occ_range=(2, None),
...     row_occ_range=(2, None),
...     root_dir=root_dir,
... )


>>> chart = techminer2plus.matrix_viewer(
...     cooc_matrix, 
...     n_labels=15,
...     node_size_min=12,
...     node_size_max=70,
...     textfont_size_min=7,
...     textfont_size_max=20,
...     xaxes_range=(-2,2)
... )
>>> chart.fig_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/matrix_viewer_0.html"
    height="600px" width="100%" frameBorder="0"></iframe>





>>> file_name = "sphinx/_static/matrix_viewer_1.html"

>>> cooc_matrix = techminer2plus.co_occurrence_matrix(
...    columns='author_keywords',
...    col_top_n=10,
...    root_dir=root_dir,
... )


>>> chart = techminer2plus.matrix_viewer(
...     cooc_matrix,
...     nx_iterations=5,
...     xaxes_range=(-2,2),
... )
>>> chart.fig_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/matrix_viewer_1.html"
    height="600px" width="100%" frameBorder="0"></iframe>

    





# pylint: disable=line-too-long
"""
from dataclasses import dataclass

import networkx as nx
import pandas as pd
import plotly.graph_objs as go

from .....network_lib import (
    nx_compute_spring_layout,
    nx_create_graph_from_matrix,
    px_add_names_to_fig_nodes,
    px_create_edge_traces,
    px_create_network_fig,
    px_create_node_trace,
)
from .list_cells_in_matrix import list_cells_in_matrix


@dataclass
class MatrixViewer:
    """Matrix viewer."""

    nx_graph_: nx.Graph
    fig_: go.Figure
    df_: pd.DataFrame


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def matrix_viewer(
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
    """Makes cluster map from a ocurrence flooding matrix."""

    graph = nx_create_graph_from_matrix(
        cooc_matrix,
        node_size_min,
        node_size_max,
        textfont_size_min,
        textfont_size_max,
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

    return MatrixViewer(
        fig_=fig,
        nx_graph_=graph,
        df_=list_cells_in_matrix(cooc_matrix).df_,
    )
