# flake8: noqa
# pylint: disable=import-outside-toplevel
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Ranking Plot
===============================================================================

>>> from techminer2.visualize.basic_plots.ranking_plot import RankingPlot
>>> plot = (
...     RankingPlot()
...     .set_analysis_params(
...         metric="OCC",
...     #
...     ).set_item_params(
...         field="author_keywords",
...         top_n=20,
...         occ_range=(None, None),
...         gc_range=(None, None),
...         custom_terms=None,
...     #
...     ).set_plot_params(
...         line_width=1.5,
...         marker_size=7,
...         textfont_size=10,
...         title_text="Ranking Plot",
...         xaxes_label="Author Keywords",
...         yaxes_label="OCC",
...         yshift=4,
...     #
...     ).set_database_params(
...         root_dir="example/", 
...         database="main",
...         year_filter=(None, None),
...         cited_by_filter=(None, None),
...     #
...     ).build()
... )
>>> plot.write_html("sphinx/_generated/visualize/basic_plots/ranking_plot.html")

.. raw:: html

    <iframe src="../../_generated/visualize/basic_plots/ranking_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>


"""


from ...analyze.metrics.performance_metrics_dataframe import performance_metrics_frame
from ...internals.params.database_params import DatabaseParams, DatabaseParamsMixin
from ...internals.params.item_params import ItemParams, ItemParamsMixin
from ...internals.plots.ranking_plot_mixin import RankingPlotMixin, RankingPlotParams
from .internals.analysis_params import AnalysisParams, AnalysisParamsMixin


class RankingPlot(
    AnalysisParamsMixin,
    DatabaseParamsMixin,
    ItemParamsMixin,
    RankingPlotMixin,
):
    """:meta private:"""

    def __init__(self):
        self.analysis_params = AnalysisParams()
        self.database_params = DatabaseParams()
        self.item_params = ItemParams()
        self.plot_params = RankingPlotParams()

    def _set_default_labels(self):

        self.plot_params.xaxes_label = (
            self.item_params.field.title().replace("_", " ")
            if self.plot_params.xaxes_label is None
            else self.plot_params.xaxes_label
        )

        self.plot_params.yaxes_label = (
            self.analysis_params.metric.replace("_", " ")
            if self.plot_params.yaxes_label is None
            else self.plot_params.yaxes_label
        )

    def build(self):

        self._set_default_labels()

        dataframe = performance_metrics_frame(
            metric=self.analysis_params.metric,
            **self.item_params.__dict__,
            **self.database_params.__dict__,
        )

        fig = self.build_ranking_plot(
            dataframe,
            y_col=self.analysis_params.metric,
        )

        return fig
