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
## ...     .where_directory_is("example/")
## ...     .where_database_is("main")
## ...     .where_record_years_between(None, None)
## ...     .where_record_citations_between(None, None)
## ...     .where_records_match(None)
## ...     #
## ...     .build()
## ... )
## >>> # plot.write_html("sphinx/_static/coupling_network/_core/others/node_degree_plot.html")

.. raw:: html

    <iframe src="../../_static/coupling_network/_core/others/node_degree_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

"""
from ......internals.mixins import InputFunctionsMixin
from ......internals.nx import (
    internal__assign_degree_to_nodes,
    internal__collect_node_degrees,
    internal__create_node_degree_plot,
    internal__create_node_degrees_data_frame,
)
from .create_nx_graph import internal__create_nx_graph


class InternalNodeDegreePlot(
    InputFunctionsMixin,
):
    """:meta private:"""

    def build(self):

        nx_graph = internal__create_nx_graph(self.params)
        nx_graph = internal__assign_degree_to_nodes(nx_graph)
        node_degrees = internal__collect_node_degrees(nx_graph)
        data_frame = internal__create_node_degrees_data_frame(node_degrees)
        plot = internal__create_node_degree_plot(self.params, data_frame)

        return plot
