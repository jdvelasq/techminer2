# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""Node density plot."""
from techminer2._internals import ParamsMixin
from techminer2._internals.nx import (
    internal__assign_textfont_sizes_based_on_occurrences,
    internal__cluster_nx_graph,
    internal__compute_spring_layout_positions,
    internal__create_network_density_plot,
)
from techminer2.networks.citation._internals.from_others.create_nx_graph import (
    internal__create_nx_graph,
)


class NodeDensityPlot(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        nx_graph = internal__create_nx_graph(self.params)
        nx_graph = internal__cluster_nx_graph(self.params, nx_graph)
        nx_graph = internal__compute_spring_layout_positions(self.params, nx_graph)
        nx_graph = internal__assign_textfont_sizes_based_on_occurrences(
            self.params, nx_graph
        )

        return internal__create_network_density_plot(self.params, nx_graph)
