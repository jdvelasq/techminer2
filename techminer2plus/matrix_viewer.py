# flake8: noqa
# pylint: disable=line-too-long
"""
.. _matrix_viewer:

Matrix Viewer
===============================================================================



* Preparation

>>> import techminer2plus as tm2p
>>> root_dir = "data/regtech/"

* Object oriented interface

>>> (
...     tm2p.records(root_dir=root_dir)
...     .co_occurrence_matrix(
...         columns='author_keywords',
...         rows='authors',
...         col_top_n=10,
...         row_top_n=10,
...     )
...     .matrix_viewer()
...     .write_html("sphinx/_static/matrix_viewer_0.html")
... )

.. raw:: html

    <iframe src="../_static/matrix_viewer_0.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> (
...     tm2p.records(root_dir=root_dir)
...     .co_occurrence_matrix(
...         columns='author_keywords',
...         col_top_n=10,
...     )
...     .matrix_viewer()
...     .write_html("sphinx/_static/matrix_viewer_1.html")
... )

.. raw:: html

    <iframe src="../_static/matrix_viewer_1.html" height="600px" width="100%" frameBorder="0"></iframe>

* Functional interface

>>> co_occ_matrix = (
...     tm2p.records(root_dir=root_dir)
...     .co_occurrence_matrix(
...         columns='author_keywords',
...         rows='authors',
...         col_top_n=10,
...         row_top_n=10,
...     )
... )
>>> matrix_viewer(co_occ_matrix).write_html("sphinx/_static/matrix_viewer_2.html")

.. raw:: html

    <iframe src="../_static/matrix_viewer_2.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> co_occ_matrix = (
...     tm2p.records(root_dir=root_dir)
...     .co_occurrence_matrix(
...         columns='author_keywords',
...         col_top_n=10,
...     )
... )
>>> matrix_viewer(co_occ_matrix).write_html("sphinx/_static/matrix_viewer_3.html")

.. raw:: html

    <iframe src="../_static/matrix_viewer_3.html" height="600px" width="100%" frameBorder="0"></iframe>



"""
from ._network_lib import (
    nx_compute_spring_layout,
    nx_create_graph_from_matrix,
    px_add_names_to_fig_nodes,
    px_create_edge_traces,
    px_create_network_fig,
    px_create_node_trace,
)


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

    return fig
