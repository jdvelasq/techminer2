"""
Radial Diagram
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/tlab__word_associations_radial_diagram.html"

>>> from techminer2 import tlab__word_associations_radial_diagram
>>> tlab__word_associations_radial_diagram(
...     criterion='words',
...     topic="regtech",
...     topic_min_occ=4,
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../../../../_static/tlab__word_associations_radial_diagram.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
import networkx as nx

from ._get_network_graph_plot import network_graph_plot
from .vantagepoint__co_occ_matrix_list import vantagepoint__co_occ_matrix_list


def tlab__word_associations_radial_diagram(
    criterion,
    topic,
    topics_length=None,
    topic_min_occ=None,
    topic_min_citations=None,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Creates a radial diagram of term associations from a co-occurrence matrix."""

    matrix_list = vantagepoint__co_occ_matrix_list(
        criterion=criterion,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_min_citations=topic_min_citations,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    matrix_list = matrix_list[
        matrix_list["row"].map(lambda x: " ".join(x.split()[:-1]) == topic)
    ]

    if topics_length is not None:
        matrix_list = matrix_list.head(topics_length)

    # create a empty network
    graph = nx.Graph()

    # add nodes
    nodes = [
        (node, dict(size=occ, group=0))
        for node, occ in zip(matrix_list["column"], matrix_list["OCC"])
    ]
    graph.add_nodes_from(nodes)

    # add network edges
    edges = []
    for _, row in matrix_list.iterrows():
        if row[0] != row[1]:
            edges.append((row[0], row[1], row[2]))
    graph.add_weighted_edges_from(edges)

    # create a network plot
    fig = network_graph_plot(
        graph,
        nx_k=0.5,
        nx_iterations=10,
        delta=1.0,
    )

    return fig
