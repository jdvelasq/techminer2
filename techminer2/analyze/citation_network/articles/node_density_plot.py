# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Node density plot for articles.

"""
from ....internals.nx.nx_assign_textfont_sizes_to_nodes_by_citations import (
    nx_assign_textfont_sizes_to_nodes_by_citations,
)
from ....internals.nx.nx_cluster_graph import nx_cluster_graph
from ....internals.nx.nx_compute_spring_layout_positions import (
    nx_compute_spring_layout_positions,
)
from ....internals.nx.nx_density_plot import nx_density_plot
from .internals.create_citation_nx_graph import _create_citation_nx_graph


def _node_density_plot(
    #
    # COLUMN PARAMS:
    top_n=None,
    citations_threshold=0,
    #
    # NETWORK PARAMS:
    algorithm_or_dict="louvain",
    #
    # LAYOUT:
    nx_k=None,
    nx_iterations=30,
    nx_random_state=0,
    #
    # DENSITY VISUALIZATION:
    bandwidth="silverman",
    colorscale="Aggrnyl",
    opacity=0.6,
    textfont_size_range=(10, 20),
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """:meta private:"""

    nx_graph = _create_citation_nx_graph(
        #
        # COLUMN PARAMS:
        top_n=top_n,
        citations_threshold=citations_threshold,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    nx_graph = nx_cluster_graph(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
        #
        # NETWORK CLUSTERING:
        algorithm_or_dict=algorithm_or_dict,
    )

    nx_graph = nx_compute_spring_layout_positions(
        nx_graph=nx_graph,
        k=nx_k,
        iterations=nx_iterations,
        seed=nx_random_state,
    )

    nx_graph = nx_assign_textfont_sizes_to_nodes_by_citations(
        nx_graph, textfont_size_range
    )

    return nx_density_plot(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
        #
        # NETWORK PARAMS:
        bandwidth=bandwidth,
        colorscale=colorscale,
        opacity=opacity,
    )
