# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Network Map Plot
===============================================================================

Creates an Auto-correlation Map.

>>> # grey colors: https://www.w3schools.com/colors/colors_shades.asp
>>> from techminer2.packages.correlation.auto import NetworkMapPlot
>>> plot = (
...     NetworkMapPlot()
...     #
...     #
...     # FIELD:
...     .with_field("authors")
...     .having_terms_in_top(None)
...     .having_terms_ordered_by("OCC")
...     .having_term_occurrences_between(2, None)
...     .having_term_citations_between(None, None)
...     .having_terms_in(None)
...     #
...     # CORRELATION:
...     .with_correlation_method("pearson")
...     #
...     # NETWORK:
...     .using_spring_layout_k(None)
...     .using_spring_layout_iterations(30)
...     .using_spring_layout_seed(0)
...     #
...     .using_edge_colors(["#7793a5", "#7793a5", "#7793a5", "#7793a5"])
...     .using_edge_similarity_threshold(0)
...     .using_edge_top_n(None)
...     .using_edge_widths([2, 2, 4, 6])
...     #
...     .using_node_colors(["#7793a5"])
...     .using_node_size_range(30, 70)
...     #
...     .using_textfont_opacity_range(0.35, 1.00)
...     .using_textfont_size_range(10, 20)
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
>>> # plot.write_html("sphinx/_generated/pkgs/correlation/auto/network_map_plot.html")

.. raw:: html

    <iframe src="../../_generated/pkgs/correlation/auto/network_map_plot.html"
    height="800px" width="100%" frameBorder="0"></iframe>


"""
import pandas as pd  # type: ignore
from sklearn.metrics.pairwise import cosine_similarity  # type: ignore

from ...._internals.mixins import ParamsMixin
from .._internals.internal__correlation_map import internal__correlation_map
from .matrix_data_frame import MatrixDataFrame


class NetworkMapPlot(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        data_frame = MatrixDataFrame().update(**self.params.__dict__).run()

        data_frame = pd.DataFrame(
            cosine_similarity(data_frame),
            index=data_frame.index,
            columns=data_frame.columns,
        )

        return internal__correlation_map(self.params, data_frame)
