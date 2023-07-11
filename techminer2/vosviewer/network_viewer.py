# flake8: noqa
# pylint: disable=line-too-long
"""
Network Viewer
===============================================================================

* Preparation

>>> import techminer2 as tm2
>>> root_dir = "data/regtech/"

* Object oriented interface

>>> fig = (
...     tm2p.records(root_dir=root_dir)
...     .co_occurrence_matrix(
...         columns='author_keywords',
...         col_top_n=20,
...     )
...     .network_create(
...         algorithm_or_estimator="louvain"
...     )
...     .network_viewer()
... )
>>> fig.write_html("sphinx/_static/network_viewer_0.html")

.. raw:: html

    <iframe src="../../_static/network_viewer_0.html" height="600px" width="100%" frameBorder="0"></iframe>


* Functional interface

>>> cooc_matrix = tm2p.co_occurrence_matrix(
...    columns='author_keywords',
...    col_top_n=20,
...    root_dir=root_dir,
... )
>>> network = tm2p.network_create(
...     cooc_matrix,
...     algorithm_or_estimator='louvain',
... )
>>> fig = network_viewer(network)
>>> fig.write_html("sphinx/_static/network_viewer_1.html")

.. raw:: html

    <iframe src="../../_static/network_viewer_1.html" height="600px" width="100%" frameBorder="0"></iframe>

"""

from .._network_lib import (
    nx_compute_node_property_from_occ,
    nx_compute_spring_layout,
    px_add_names_to_fig_nodes,
    px_create_edge_traces,
    px_create_network_fig,
    px_create_node_trace,
)


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def network_viewer(
    network,
    n_labels=None,
    is_article=False,
    nx_k=0.1,
    nx_iterations=10,
    random_state=0,
    node_size_min=None,
    node_size_max=None,
    textfont_size_min=None,
    textfont_size_max=None,
    xaxes_range=None,
    yaxes_range=None,
    show_axes=False,
):
    """Plots a network"""

    nx_graph = network.nx_graph
    nx_graph = nx_compute_spring_layout(
        nx_graph, nx_k, nx_iterations, random_state
    )

    if node_size_max is not None and node_size_min is not None:
        nx_graph = nx_compute_node_property_from_occ(
            nx_graph, "node_size", node_size_min, node_size_max
        )

    if textfont_size_max is not None and textfont_size_min is not None:
        nx_graph = nx_compute_node_property_from_occ(
            nx_graph, "textfont_size", textfont_size_min, textfont_size_max
        )

    node_trace = px_create_node_trace(nx_graph)
    edge_traces = px_create_edge_traces(nx_graph)

    fig = px_create_network_fig(
        edge_traces=edge_traces,
        node_trace=node_trace,
        xaxes_range=xaxes_range,
        yaxes_range=yaxes_range,
        show_axes=show_axes,
    )

    fig = px_add_names_to_fig_nodes(fig, nx_graph, n_labels, is_article)

    return fig
