# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Node Degree Plot
===============================================================================


Example:
    >>> from techminer2.packages.networks.citation.documents import NodeDegreePlot
    >>> plot = (
    ...     NodeDegreePlot()
    ...     #
    ...     # UNIT OF ANALYSIS:
    ...     .having_terms_in_top(30)
    ...     .using_citation_threshold(0)
    ...     #
    ...     # PLOT:
    ...     .using_textfont_size(10)
    ...     .using_marker_size(7)
    ...     .using_line_color("black")
    ...     .using_line_width(1.5)
    ...     .using_yshift(4)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("examples/fintech/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> plot.write_html("docs_source/_generated/px.packages.networks.citation.documents.node_degree_plot.html")

.. raw:: html

    <iframe src="../_generated/px.packages.networks.citation.documents.node_degree_plot.html"
    height="800px" width="100%" frameBorder="0"></iframe>

"""
from techminer2._internals.mixins import ParamsMixin
from techminer2._internals.nx import (
    internal__assign_degree_to_nodes,
    internal__collect_node_degrees,
    internal__create_node_degree_plot,
    internal__create_node_degrees_data_frame,
)
from techminer2.networks.citation._internals.from_documents.create_nx_graph import (
    internal__create_nx_graph,
)


class NodeDegreePlot(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        nx_graph = internal__create_nx_graph(self.params)
        nx_graph = internal__assign_degree_to_nodes(nx_graph)
        node_degrees = internal__collect_node_degrees(nx_graph)
        data_frame = internal__create_node_degrees_data_frame(node_degrees)
        plot = internal__create_node_degree_plot(self.params, data_frame)

        return plot
