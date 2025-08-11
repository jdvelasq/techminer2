# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""

## >>> from techminer2.coupling_network._core.others.node_degree_plot import _node_degree_plot
## >>> plot = _node_degree_plot(
## ...     unit_of_analysis='authors', # authors, countries, organizations, sources
## ...     #
## ...     # COLUMN PARAMS:
## ...     top_n=20,
## ...     citations_threshold=0,
## ...     occurrence_threshold=2,
## ...     custom_terms=None,
## ...     #
## ...     # DEGREE PLOT:
## ...     textfont_size=10,
## ...     marker_size=7,
## ...     line_color="black",
## ...     line_width=1.5,
## ...     yshift=4,
## ...     #
## ...     # DATABASE:
## ...     .where_root_directory_is("examples/fintech/")
## ...     .where_database_is("main")
## ...     .where_record_years_range_is(None, None)
## ...     .where_record_citations_range_is(None, None)
## ...     .where_records_match(None)
## ...     #
## ...     .run()
## ... )
## >>> plot.write_html("docs_source/__static/coupling_network/_core/others.node_degree_plot.html")

.. raw:: html

    <iframe src="../../_static/coupling_network/_core/others.node_degree_plot.html"
    height="600px" width="100%" frameBorder="0"></iframe>

"""
from techminer2._internals.mixins import ParamsMixin
from techminer2._internals.nx import (
    internal__assign_degree_to_nodes,
    internal__collect_node_degrees,
    internal__create_node_degree_plot,
    internal__create_node_degrees_data_frame,
)
from techminer2.packages.networks.coupling._internals.from_others.create_nx_graph import (
    internal__create_nx_graph,
)


class InternalNodeDegreePlot(
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
        data_frame = internal__create_node_degrees_data_frame(node_degrees)
        plot = internal__create_node_degree_plot(self.params, data_frame)

        return plot
