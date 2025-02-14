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

>>> from techminer2.pkgs.networks.citation.countries import NetworkPlot
>>> plot = (
...     NetworkPlot()
...     #
...     # UNIT OF ANALYSIS:
...     .having_terms_in_top(30)
...     .having_citation_threshold(0)
...     .having_occurrence_threshold(2)
...     .having_terms_in(None)
...     #
...     # CLUSTERING:
...     .using_clustering_algorithm_or_dict("louvain")
...     #
...     # NETWORK:
...     .using_spring_layout_k(None)
...     .using_spring_layout_iterations(30)
...     .using_spring_layout_seed(0)
...     #
...     .using_edge_colors(["#7793a5"])
...     .using_edge_width_range(0.8, 3.0)
...     .using_node_size_range(30, 70)
...     .using_textfont_opacity_range(0.35, 1.00)
...     .using_textfont_size_range(10, 20)
...     #
...     .using_xaxes_range(None, None)
...     .using_yaxes_range(None, None)
...     .using_axes_visible(False)
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
>>> # plot.write_html("sphinx/_generated/pkgs/networks/citation/countries/network_plot.html")

.. raw:: html

    <iframe src="../../_generated/pkgs/networks/citation/countries/network_plot.html" 
    height="800px" width="100%" frameBorder="0"></iframe>


"""

from .....internals.mixins import ParamsMixin
from ..internals.from_others.network_plot import NetworkPlot as OtherNetworkPlot


class NetworkPlot(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):
        return (
            OtherNetworkPlot()
            .update(**self.params.__dict__)
            .unit_of_analysis("countries")
            .build()
        )
