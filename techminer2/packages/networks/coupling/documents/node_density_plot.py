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


Example:
    >>> from techminer2.packages.networks.coupling.documents import NodeDensityPlot
    >>> plot = (
    ...     NodeDensityPlot()
    ...     #
    ...     # UNIT OF ANALYSIS:
    ...     .having_terms_in_top(20)
    ...     .having_citation_threshold(0)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering_algorithm_or_dict("louvain")
    ...     #
    ...     # NETWORK:
    ...     .using_spring_layout_k(None)
    ...     .using_spring_layout_iterations(30)
    ...     .using_spring_layout_seed(0)
    ...     #
    ...     # DENSITY:
    ...     .using_kernel_bandwidth(0.1)
    ...     .using_colormap("Aggrnyl")
    ...     .using_contour_opacity(0.6)
    ...     .using_textfont_size_range(10, 20)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("example/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> plot.write_html("docs_source/_generated/px.packages.networks.coupling.documents.node_density_plot.html")

.. raw:: html

    <iframe src="../_generated/px.packages.networks.coupling.documents.node_density_plot.html"
    height="800px" width="100%" frameBorder="0"></iframe>


"""
from ....._internals.mixins import ParamsMixin
from ....._internals.nx import (
    internal__assign_textfont_sizes_based_on_citations,
    internal__cluster_nx_graph,
    internal__compute_spring_layout_positions,
    internal__create_network_density_plot,
)
from .._internals.from_documents.create_nx_graph import internal__create_nx_graph


class NodeDensityPlot(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        nx_graph = internal__create_nx_graph(self.params)
        nx_graph = internal__cluster_nx_graph(self.params, nx_graph)
        nx_graph = internal__compute_spring_layout_positions(self.params, nx_graph)
        nx_graph = internal__assign_textfont_sizes_based_on_citations(
            self.params, nx_graph
        )

        return internal__create_network_density_plot(self.params, nx_graph)
