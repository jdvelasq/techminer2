# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Ranking Plot
===============================================================================


>>> from techminer2.database.metrics.trend import RankingPlot
>>> plot = (
...     RankingPlot()
...     #
...     .using_title_text("Trend Metrics Plot")
...     .using_xaxes_title_text("Years")
...     .using_yaxes_title_text("OCC")
...     #
...     .using_line_width(1.5)
...     .using_marker_size(7)
...     .using_textfont_size(10)
...     .using_yshift(4)
...     #
...     .where_root_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_range_is(None, None)
...     .where_record_citations_range_is(None, None)
...     #
...     .run()
... )
>>> # plot.write_html("sphinx/_generated/database/metrics/trend/trend_metrics_plot.html")

.. raw:: html

    <iframe src="../../../_generated/database/metrics/trend/trend_metrics_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>



"""
from ...._internals.params_mixin import ParamsMixin
from ...._internals.plots.internal__ranking_plot import internal__ranking_plot
from .data_frame import DataFrame


class RankingPlot(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        data_frame = DataFrame().update(**self.params.__dict__).run()

        data_frame["Rank"] = range(1, len(data_frame) + 1)

        self.having_terms_ordered_by("OCC")

        if self.params.title_text is None:
            self.using_title_text("Trend Metrics")

        if self.params.xaxes_title_text is None:
            self.using_xaxes_title_text(self.params.field.replace("_", " ").upper())

        if self.params.yaxes_title_text is None:
            self.using_yaxes_title_text(
                self.params.terms_order_by.replace("_", " ").upper()
            )

        fig = internal__ranking_plot(params=self.params, data_frame=data_frame)

        return fig
