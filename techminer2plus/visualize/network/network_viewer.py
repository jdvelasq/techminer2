# flake8: noqa
"""
(NEW) Network Viewer
===============================================================================





>>> root_dir = "data/regtech/"
>>> import techminer2plus
>>> co_occ_matrix = techminer2plus.system.analyze.co_occ_matrix(
...    columns='author_keywords',
...    col_occ_range=(2, None),
...    root_dir=root_dir,
... )
>>> normalized_co_occ_matrix = techminer2plus.system.analyze.association_index(
...     co_occ_matrix, "association"
... )
>>> graph = techminer2plus.system.analyze.cluster_column(
...    normalized_co_occ_matrix,
...    community_clustering='louvain',
... )
>>> fig = techminer2plus.system.analyze.network_viewer(
...     graph,
...     n_labels=15,
...     node_size_min=8,
...     node_size_max=45,
...     textfont_size_min=8,
...     textfont_size_max=20,
... )
>>> file_name = "sphinx/_static/techminer2plus__network_viewer.html"
>>> fig.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../_static/techminer2plus__network_viewer.html"
    height="600px" width="100%" frameBorder="0"></iframe>



# pylint: disable=line-too-long
"""

from ...network import (
    nx_compute_node_property_from_occ,
    nx_compute_spring_layout,
    px_add_names_to_fig_nodes,
    px_create_edge_traces,
    px_create_network_fig,
    px_create_node_trace,
)


# pylint: disable=too-many-arguments
def network_viewer(
    graph,
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

    graph = nx_compute_spring_layout(graph, nx_k, nx_iterations, random_state)

    if node_size_max is not None and node_size_min is not None:
        graph = nx_compute_node_property_from_occ(
            graph, "node_size", node_size_min, node_size_max
        )

    if textfont_size_max is not None and textfont_size_min is not None:
        graph = nx_compute_node_property_from_occ(
            graph, "textfont_size", textfont_size_min, textfont_size_max
        )

    node_trace = px_create_node_trace(graph)
    edge_traces = px_create_edge_traces(graph)

    fig = px_create_network_fig(
        edge_traces=edge_traces,
        node_trace=node_trace,
        xaxes_range=xaxes_range,
        yaxes_range=yaxes_range,
        show_axes=show_axes,
    )

    fig = px_add_names_to_fig_nodes(fig, graph, n_labels, is_article)

    return fig