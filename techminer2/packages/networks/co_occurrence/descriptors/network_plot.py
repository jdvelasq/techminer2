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

>>> from techminer2.packages.networks.co_occurrence.descriptors import NetworkPlot
>>> plot = (
...     NetworkPlot()
...     #
...     # FIELD:
...     .having_terms_in_top(20)
...     .having_terms_ordered_by("OCC")
...     .having_term_occurrences_between(None, None)
...     .having_term_citations_between(None, None)
...     .having_terms_in(None)
...     #
...     # COUNTERS:
...     .using_term_counters(True)
...     #
...     # NETWORK:
...     .using_clustering_algorithm_or_dict("louvain")
...     .using_association_index("association")
...     #
...     # PLOT:
...     .using_spring_layout_k(None)
...     .using_spring_layout_iterations(30)
...     .using_spring_layout_seed(0)
...     #
...     .using_node_size_range(30, 70)
...     .using_textfont_size_range(10, 20)
...     .using_textfont_opacity_range(0.35, 1.00)
...     .using_edge_colors(["#7793a5"])
...     .using_edge_width_range(0.8, 3.0)
...     #
...     .using_xaxes_range(None, None)
...     .using_yaxes_range(None, None)
...     .using_axes_visible(False)
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
>>> # plot.write_html("docs_src/_generated/packages/networks/co_occurrence/descriptors/network_plot.html")

.. raw:: html

    <iframe src="../../_generated/packages/networks/co_occurrence/descriptors/network_plot.html"
    height="800px" width="100%" frameBorder="0"></iframe>



"""
from ....._internals.mixins import ParamsMixin
from ..user.network_plot import NetworkPlot as UserNetworkPlot


class NetworkPlot(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            UserNetworkPlot()
            .update(**self.params.__dict__)
            .with_field("descriptors")
            .run()
        )
