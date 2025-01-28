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
...     #
...     .where_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     #
...     .build()
... )
>>> plot.write_html("sphinx/_generated/database/metrics/trend_metrics/trend_metrics_plot.html")

.. raw:: html

    <iframe src="../../../_generated/database/metrics/trend_metrics/trend_metrics_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>



"""
from ....internals.mixins.input_functions import InputFunctionsMixin
from ....internals.mixins.ranking_plot import RankingPlotMixin
from .data_frame import DataFrame


class RankingPlot(
    InputFunctionsMixin,
    RankingPlotMixin,
):
    """:meta private:"""

    def build(self):

        data_frame = DataFrame().update_params(**self.params.__dict__)
        data_frame = data_frame.build()
        data_frame["Rank"] = range(1, len(data_frame) + 1)

        self.order_terms_by("OCC")

        if self.params.title_text is None:
            self.using_title_text("Trend Metrics")

        if self.params.xaxes_title_text is None:
            self.using_xaxes_title_text(
                self.params.source_field.replace("_", " ").upper()
            )

        if self.params.yaxes_title_text is None:
            self.using_yaxes_title_text(
                self.params.terms_order_by.replace("_", " ").upper()
            )

        fig = self.build_ranking_plot(data_frame=data_frame)

        return fig
