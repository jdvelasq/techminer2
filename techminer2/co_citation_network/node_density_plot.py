# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Node Density Plot
===============================================================================


>>> from techminer2.co_citation_network import node_density_plot
>>> plot = node_density_plot(
...     unit_of_analysis="cited_sources", # "cited_sources", 
...                                       # "cited_references",
...                                       # "cited_authors"
...     #
...     # COLUMN PARAMS:
...     top_n=30, 
...     citations_threshold=None,
...     custom_terms=None,
...     #
...     # NETWORK PARAMS:
...     algorithm_or_dict="louvain",
...     #
...     # LAYOUT:
...     nx_k=None,
...     nx_iterations=30,
...     nx_random_state=0,
...     #
...     # DENSITY VISUALIZATION:
...     bandwidth=0.1,
...     colorscale="Aggrnyl",
...     opacity=0.6,
...     textfont_size_range=(8, 12),
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> # plot.write_html("sphinx/_static/co_citation_network/node_density_plot.html")

.. raw:: html

    <iframe src="../_static/co_citation_network/node_density_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

"""
from .._core.nx.nx_assign_textfont_sizes_to_nodes_based_on_occurrences import nx_assign_textfont_sizes_to_nodes_based_on_occurrences
from .._core.nx.nx_cluster_graph import nx_cluster_graph
from .._core.nx.nx_compute_spring_layout_positions import nx_compute_spring_layout_positions
from .._core.nx.nx_density_plot import nx_density_plot
from ._create_co_citation_nx_graph import _create_co_citation_nx_graph


def node_density_plot(
    unit_of_analysis,
    #
    # COLUMN PARAMS:
    top_n=None,
    citations_threshold=None,
    custom_terms=None,
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
    # AXES:
    # xaxes_range=None,
    # yaxes_range=None,
    # show_axes=False,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """:meta private:"""

    nx_graph = _create_co_citation_nx_graph(
        #
        # FUNCTION PARAMS:
        unit_of_analysis=unit_of_analysis,
        #
        # COLUMN PARAMS:
        top_n=top_n,
        citations_threshold=citations_threshold,
        custom_terms=custom_terms,
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

    nx_graph = nx_assign_textfont_sizes_to_nodes_based_on_occurrences(nx_graph, textfont_size_range)

    return nx_density_plot(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
        #
        # NETWORK PARAMS:
        bandwidth=bandwidth,
        colorscale=colorscale,
        opacity=opacity,
        # xaxes_range=xaxes_range,
        # yaxes_range=yaxes_range,
        # show_axes=show_axes,
    )
