# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""

## >>> from techminer2.coupling_network._core.others.node_density_plot import _node_density_plot
## >>> plot = _node_density_plot(
## ...     unit_of_analysis='authors', # authors, countries, organizations, sources
## ...     #
## ...     # COLUMN PARAMS:
## ...     top_n=20, 
## ...     citations_threshold=0,
## ...     occurrence_threshold=2,
## ...     custom_terms=None,
## ...     #
## ...     # NETWORK PARAMS:
## ...     algorithm_or_dict="louvain",
## ...     ).set_nx_params(
## ...         nx_k=None,
## ...         nx_iterations=30,
## ...         nx_random_state=0,
## ...     #
## ...     # DENSITY VISUALIZATION:
## ...     bandwidth=0.1,
## ...     colorscale="Aggrnyl",
## ...     opacity=0.6,
## ...     #
## ...     # DATABASE:
## ...     .where_root_directory_is("example/")
## ...     .where_database_is("main")
## ...     .where_record_years_range_is(None, None)
## ...     .where_record_citattions_range_is(None, None)
## ...     .where_records_match(None)
## ...     #
## ...     .build()
## ... )
## >>> # plot.write_html("sphinx/_static/coupling_network/_core/others/node_density_plot.html")

.. raw:: html

    <iframe src="../../_static/coupling_network/_core/others/node_density_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

                                             
"""
from ......_internals.mixins import ParamsMixin
from ......_internals.nx import (
    internal__assign_textfont_sizes_based_on_occurrences,
    internal__cluster_nx_graph,
    internal__compute_spring_layout_positions,
    internal__create_network_density_plot,
)
from .create_nx_graph import internal__create_nx_graph


class InternalNodeDensityPlot(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):

        nx_graph = internal__create_nx_graph(params=self.params)

        nx_graph = internal__create_nx_graph(self.params)
        nx_graph = internal__cluster_nx_graph(self.params, nx_graph)
        nx_graph = internal__compute_spring_layout_positions(self.params, nx_graph)
        nx_graph = internal__assign_textfont_sizes_based_on_occurrences(
            self.params, nx_graph
        )

        return internal__create_network_density_plot(self.params, nx_graph)
