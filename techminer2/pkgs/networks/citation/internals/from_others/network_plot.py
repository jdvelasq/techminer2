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

## >>> # Test code for:
## >>> #     source_title
## >>> #     authors
## >>> #     organizations
## >>> #     countries
## >>> from techminer2.pkgs.networks.citation.internals.others import NetworkPlot
## >>> plot = (
## ...     NetworkPlot()
## ...     #
## ...     # UNIT OF ANALYSIS:
## ...     .unit_of_analysis('source_title')
## ...     .having_terms_in_top(30)
## ...     .having_citation_threshold(0)
## ...     .having_occurrence_threshold(2)
## ...     .having_terms_in(None)
## ...     #
## ...     # NETWORK CLUSTERING:
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
## >>> # plot.write_html("sphinx/_generated/pkgs/networks/citation/internals/others/network_map_plot.html")

.. raw:: html

    <iframe src="../../_generated/pkgs/correlation/auto/network_map_plot.html" 
    height="800px" width="100%" frameBorder="0"></iframe>


"""
from ......internals.mixins import InputFunctionsMixin
from ......internals.nx import (
    internal__assign_constant_to_edge_colors,
    internal__assign_edge_widths_based_on_weight,
    internal__assign_node_colors_based_on_group_attribute,
    internal__assign_node_sizes_based_on_occurrences,
    internal__assign_text_positions_based_on_quadrants,
    internal__assign_textfont_opacity_based_on_occurrences,
    internal__assign_textfont_sizes_based_on_occurrences,
    internal__cluster_nx_graph,
    internal__compute_spring_layout_positions,
    internal__plot_nx_graph,
)
from .create_nx_graph import internal__create_nx_graph

UNIT_OF_ANALYSIS = "abbr_source_title"


class NetworkPlot(
    InputFunctionsMixin,
):
    """:meta private:"""

    def build(self):

        nx_graph = internal__create_nx_graph(self.params)
        nx_graph = internal__cluster_nx_graph(self.params, nx_graph)
        nx_graph = internal__compute_spring_layout_positions(self.params, nx_graph)
        nx_graph = internal__assign_node_colors_based_on_group_attribute(nx_graph)
        nx_graph = internal__assign_node_sizes_based_on_occurrences(
            self.params, nx_graph
        )
        nx_graph = internal__assign_textfont_sizes_based_on_occurrences(
            self.params, nx_graph
        )
        nx_graph = internal__assign_textfont_opacity_based_on_occurrences(
            self.params, nx_graph
        )

        #
        # Sets the edge attributes
        nx_graph = internal__assign_edge_widths_based_on_weight(self.params, nx_graph)
        nx_graph = internal__assign_text_positions_based_on_quadrants(nx_graph)
        nx_graph = internal__assign_constant_to_edge_colors(self.params, nx_graph)

        return internal__plot_nx_graph(self.params, nx_graph)
