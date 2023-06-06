# flake8: noqa
"""
Network Viewer --- ChatGPT
===============================================================================





Example: 
-------------------------------------------------------------------------------

>>> root_dir = "data/regtech/"
>>> from techminer2 import vantagepoint
>>> co_occ_matrix = vantagepoint.analyze.co_occ_matrix(
...    columns='author_keywords',
...    col_occ_range=(2, None),
...    root_dir=root_dir,
... )
>>> normalized_co_occ_matrix = vantagepoint.analyze.association_index(
...     co_occ_matrix, "association"
... )
>>> graph = vantagepoint.analyze.cluster_column(
...    normalized_co_occ_matrix,
...    community_clustering='louvain',
... )
>>> fig = vantagepoint.analyze.network_viewer(
...     graph,
...     n_labels=15,
...     node_size_min=8,
...     node_size_max=45,
...     textfont_size_min=8,
...     textfont_size_max=20,
... )
>>> file_name = "sphinx/_static/vantagepoint__network_viewer.html"
>>> fig.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../_static/vantagepoint__network_viewer.html"
    height="600px" width="100%" frameBorder="0"></iframe>



# pylint: disable=line-too-long
"""

from ... import network_utils


# pylint: disable=too-many-arguments
def network_viewer(
    graph,
    n_labels=None,
    nx_k=0.5,
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

    graph = network_utils.compute_spring_layout(
        graph, nx_k, nx_iterations, random_state
    )

    if node_size_max is not None and node_size_min is not None:
        graph = network_utils.compute_prop_sizes(
            graph, "node_size", node_size_min, node_size_max
        )

    if textfont_size_max is not None and textfont_size_min is not None:
        graph = network_utils.compute_prop_sizes(
            graph, "textfont_size", textfont_size_min, textfont_size_max
        )

    node_trace = network_utils.create_node_trace(graph)
    # text_trace = network_utils.create_text_trace(graph)
    edge_traces = network_utils.create_edge_traces(graph)

    fig = network_utils.create_network_graph(
        edge_traces=edge_traces,
        node_trace=node_trace,
        # text_trace=text_trace,
        xaxes_range=xaxes_range,
        yaxes_range=yaxes_range,
        show_axes=show_axes,
    )

    fig = network_utils.add_names_to_fig_nodes(fig, graph, n_labels)

    return fig
