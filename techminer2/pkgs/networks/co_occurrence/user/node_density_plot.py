# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Node Density Plot
===============================================================================


>>> from techminer2.pkgs.networks.co_occurrence.user import NodeDensityPlot
>>> plot = (
...     NodeDensityPlot()
...     #
...     # FIELD:
...     .with_field("author_keywords")
...     .having_terms_in_top(20)
...     .having_terms_ordered_by("OCC")
...     .having_term_occurrences_between(None, None)
...     .having_term_citations_between(None, None)
...     .having_terms_in(None)
...     #
...     # NETWORK:
...     .using_association_index("association")
...     #
...     #
...     .using_spring_layout_k(None)
...     .using_spring_layout_iterations(30)
...     .using_spring_layout_seed(0)
...     #
...     .using_textfont_size_range(10, 20)
...     .using_kernel_bandwidth(0.1)
...     .using_colormap("Aggrnyl")
...     .using_contour_opacity(0.6)
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     .where_records_match(None)
...     #
...     .build()
... )
>>> plot.write_html("sphinx/_generated/pkgs/networks/co_occurrence/user/node_density_plot.html")

.. raw:: html

    <iframe src="../../_generated/pkgs/networks/co_occurrence/user/node_density_plot.html" 
    height="800px" width="100%" frameBorder="0"></iframe>



"""

from ....._internals.mixins import ParamsMixin
from ....._internals.nx import (
    internal__assign_textfont_sizes_based_on_occurrences,
    internal__cluster_nx_graph,
    internal__compute_spring_layout_positions,
    internal__create_network_density_plot,
)
from .._internals.create_nx_graph import internal__create_nx_graph


class NodeDensityPlot(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):
        """:meta private:"""

        nx_graph = internal__create_nx_graph(self.params)
        nx_graph = internal__cluster_nx_graph(self.params, nx_graph)
        nx_graph = internal__compute_spring_layout_positions(self.params, nx_graph)
        nx_graph = internal__assign_textfont_sizes_based_on_occurrences(
            self.params, nx_graph
        )

        return internal__create_network_density_plot(self.params, nx_graph)
