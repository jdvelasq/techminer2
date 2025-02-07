# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Network Density Plot
===============================================================================

## >>> from techminer2.pkgs.networks.coupling.articles import NodeDensityPlot
## >>> plot = (
## ...     NodeDensityPlot()
## ...     #
## ...     # UNIT OF ANALYSIS:
## ...     .having_terms_in_top(20)
## ...     .having_citation_threshold(0)
## ...     #
## ...     # CLUSTERING:
## ...     .using_clustering_algorithm_or_dict("louvain")
## ...     #
## ...     # NETWORK:
## ...     .using_spring_layout_k(None)
## ...     .using_spring_layout_iterations(30)
## ...     .using_spring_layout_seed(0)
## ...     #
## ...     # DENSITY:
## ...     .using_kernel_bandwidth(0.1)
## ...     .using_colormap("Aggrnyl")
## ...     .using_contour_opacity(0.6)
## ...     .using_textfont_size_range(10, 20)
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
## >>> # plot.write_html("sphinx/_generated/pkgs/networks/coupling/articles/node_density_plot.html")

.. raw:: html

    <iframe src="../../_generated/pkgs/networks/coupling/articles/node_density_plot.html" 
    height="800px" width="100%" frameBorder="0"></iframe>

                                             
"""
from .....internals.mixins import InputFunctionsMixin
from .....internals.nx import (
    internal__assign_textfont_sizes_based_on_citations,
    internal__cluster_nx_graph,
    internal__compute_spring_layout_positions,
    internal__create_network_density_plot,
)
from ..internals.from_articles.create_nx_graph import internal__create_nx_graph


class NodeDensityPlot(
    InputFunctionsMixin,
):
    """:meta private:"""

    def build(self):
        pass


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

    nx_graph = internal__create_nx_graph(
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

    nx_graph = internal__cluster_nx_graph(
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

    nx_graph = internal__assign_textfont_sizes_based_on_citations(
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
