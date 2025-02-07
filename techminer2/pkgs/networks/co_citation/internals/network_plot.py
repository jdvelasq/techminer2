# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Network Plot
===============================================================================

## >>> from techminer2.pkgs.co_citation_network import NetworkPlot
## >>> plot = (
## ...     NetworkPlot()
## ...     .set_analysis_params(
## ...         unit_of_analysis="cited_sources", # "cited_sources", 
## ...                                           # "cited_references",
## ...                                           # "cited_authors"
## ...     .having_terms_in_top(30)
## ...     .having_citation_threshold(0)
## ...     .having_terms_in(None)
## ...     #
## ...     # CLUSTERING:
## ...     .using_clustering_algorithm_or_dict("louvain")
## ...     #
## ...     #
## ...     # NETWORK:
## ...     .using_spring_layout_k(None)
## ...     .using_spring_layout_iterations(30)
## ...     .using_spring_layout_seed(0)
## ...     #
## ...     .using_edge_colors(["#7793a5"])
## ...     .using_edge_width_range(0.8, 3.0)
## ...     .using_node_size_range(30, 70)
## ...     .using_textfont_opacity_range(0.35, 1.00)
## ...     .using_textfont_size_range(10, 20)
## ...     #
## ...     .using_xaxes_range(None, None)
## ...     .using_yaxes_range(None, None)
## ...     .using_axes_visible(False)
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
## >>> plot.write_html("sphinx/_static/co_citation_network/network_plot.html")

.. raw:: html

    <iframe src="../_static/co_citation_network/network_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

"""
from .....internals.mixins import InputFunctionsMixin
from .....internals.nx import (
    internal__assign_constant_to_edge_colors,
    internal__assign_edge_widths_based_on_weight,
    internal__assign_node_colors_based_on_group_attribute,
    internal__assign_node_sizes_based_on_citations,
    internal__assign_text_positions_based_on_quadrants,
    internal__assign_textfont_opacity_based_on_citations,
    internal__assign_textfont_sizes_based_on_citations,
    internal__cluster_nx_graph,
    internal__compute_spring_layout_positions,
    internal__plot_nx_graph,
)
from .create_nx_graph import internal__create_nx_graph


class NetworkPlot(
    InputFunctionsMixin,
):
    """:meta private:"""

    def build(self):

        nx_graph = internal__create_nx_graph(self.params)

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

        nx_graph = internal__assign_node_colors_based_on_group_attribute(nx_graph)

        nx_graph = internal__assign_node_sizes_based_on_citations(
            nx_graph,
            node_size_range,
        )
        nx_graph = internal__assign_textfont_sizes_based_on_citations(
            nx_graph, textfont_size_range
        )
        nx_graph = internal__assign_textfont_opacity_based_on_citations(
            nx_graph, textfont_opacity_range
        )

        #
        # Sets the edge attributes
        nx_graph = internal__assign_edge_widths_based_on_weight(
            nx_graph, edge_width_range
        )
        nx_graph = internal__assign_text_positions_based_on_quadrants(nx_graph)
        nx_graph = internal__assign_constant_to_edge_colors(nx_graph, edge_color)

        return internal__plot_nx_graph(
            #
            # FUNCTION PARAMS:
            nx_graph=nx_graph,
            #
            # NETWORK PARAMS:
            xaxes_range=xaxes_range,
            yaxes_range=yaxes_range,
            show_axes=show_axes,
        )
