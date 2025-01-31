# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""

## >>> from techminer2.coupling_network._core.docs.node_density_plot import _node_density_plot
## >>> plot = _node_density_plot(
## ...     #
## ...     # ARTICLE PARAMS:
## ...     top_n=20, 
## ...     citations_threshold=0,
## ...     #
## ...     # NETWORK PARAMS:
## ...     algorithm_or_dict="louvain",
## ...     #
## ...     # NETWORK:
## ...     .using_spring_layout_k(None)
## ...     .using_spring_layout_iterations(30)
## ...     .using_spring_layout_seed(0)

## ...     #
## ...     # DENSITY VISUALIZATION:
## ...     bandwidth=0.1,
## ...     colorscale="Aggrnyl",
## ...     opacity=0.6,
## ...     #
## ...     # DATABASE:
## ...     .where_directory_is("example/")
## ...     .where_database_is("main")
## ...     .where_record_years_between(None, None)
## ...     .where_record_citations_between(None, None)
## ...     .where_records_match(None)
## ...     #
## ...     .build()
## ... )
## >>> # plot.write_html("sphinx/_static/coupling_network/_core/docs/node_density_plot.html")

.. raw:: html

    <iframe src="../../_static/coupling_network/_core/docs/node_density_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

                                             
"""
from .....internals.nx.internal__assign_textfont_sizes_to_nodes_by_citations import (
    internal__assign_textfont_sizes_to_nodes_by_citations,
)
from .....internals.nx.internal__cluster_graph import internal__cluster_graph
from .....internals.nx.internal__compute_spring_layout_positions import (
    internal__compute_spring_layout_positions,
)
from .....internals.nx.internal__create_network_density_plot import (
    internal__create_network_density_plot,
)
from .internals.create_coupling_nx_graph import _create_coupling_nx_graph


def _node_density_plot(
    #
    # ARTICLE PARAMS:
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

    nx_graph = _create_coupling_nx_graph(
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

    nx_graph = internal__cluster_graph(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
        #
        # NETWORK CLUSTERING:
        algorithm_or_dict=algorithm_or_dict,
    )

    nx_graph = internal__compute_spring_layout_positions(
        nx_graph=nx_graph,
        k=nx_k,
        iterations=nx_iterations,
        seed=nx_random_state,
    )

    nx_graph = internal__assign_textfont_sizes_to_nodes_by_citations(
        nx_graph, textfont_size_range
    )

    return internal__create_network_density_plot(
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
