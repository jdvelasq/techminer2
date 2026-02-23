"""
Ranking Plot
===============================================================================

Smoke tests:
    >>> from techminer2.analyze.metrics.records_by_year import RankingPlot
    >>> plotter = (
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
    ...     .where_root_directory("tests/data/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ... )
    >>> plot = plotter.run()
    >>> plot.write_html("docs_source/_generated/px.database.metrics.trend.trend_metrics_plot.html")

.. raw:: html

    <iframe src="../_generated/px.database.metrics.trend.trend_metrics_plot.html"
    height="600px" width="100%" frameBorder="0"></iframe>



"""

from techminer2._internals import ParamsMixin
from techminer2._internals.plots.ranking_plot import ranking_plot
from techminer2.analyze.metrics.records_by_year.data_frame import DataFrame


class RankingPlot(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        data_frame = DataFrame().update(**self.params.__dict__).run()

        data_frame["Rank"] = range(1, len(data_frame) + 1)

        self.having_items_ordered_by("OCC")

        if self.params.title_text is None:
            self.using_title_text("Trend Metrics")

        if self.params.xaxes_title_text is None:
            self.using_xaxes_title_text(self.params.field.replace("_", " ").upper())

        if self.params.yaxes_title_text is None:
            self.using_yaxes_title_text(
                self.params.items_order_by.replace("_", " ").upper()
            )

        fig = ranking_plot(params=self.params, dataframe=data_frame)

        return fig


#
