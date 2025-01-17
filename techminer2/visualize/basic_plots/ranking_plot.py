# flake8: noqa
# pylint: disable=import-outside-toplevel
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Ranking Plot (MIGRATED)
===============================================================================

## >>> from techminer2.visualize.basic_plots.ranking_plot import RankingPlot
## >>> plot = (
## ...     RankingPlot()
## ...     .set_analysis_params(
## ...         metric="OCC",
## ...     #
## ...     ).set_item_params(
## ...         field="author_keywords",
## ...         top_n=20,
## ...         occ_range=(None, None),
## ...         gc_range=(None, None),
## ...         custom_terms=None,
## ...     #
## ...     ).set_plot_params(
## ...         line_width=1.5,
## ...         marker_size=7,
## ...         textfont_size=10,
## ...         title_text="Ranking Plot",
## ...         xaxes_title_text="Author Keywords",
## ...         yaxes_title_text="OCC",
## ...         yshift=4,
## ...     #
## ...     ).set_database_params(
## ...         root_dir="example/", 
## ...         database="main",
## ...         year_filter=(None, None),
## ...         cited_by_filter=(None, None),
## ...     #
## ...     ).build()
## ... )
## >>> plot.write_html("sphinx/_generated/visualize/basic_plots/ranking_plot.html")

.. raw:: html

    <iframe src="../../_generated/visualize/basic_plots/ranking_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>


"""
from ...analyze.metrics.performance_metrics_dataframe import performance_metrics_frame
from ...internals.params.item_params import ItemParams, ItemParamsMixin
from ...internals.plots.ranking_plot_mixin import RankingPlotMixin, RankingPlotParams
from ...internals.set_params_mixin.set_database_filters_mixin import (
    DatabaseFilters,
    SetDatabaseFiltersMixin,
)
from .internals.analysis_params import AnalysisParams, AnalysisParamsMixin
from .internals.basic_plot import BasicPlotMixin


class RankingPlot(
    AnalysisParamsMixin,
    BasicPlotMixin,
    SetDatabaseFiltersMixin,
    ItemParamsMixin,
    RankingPlotMixin,
):
    """:meta private:"""

    def __init__(self):
        self.analysis_params = AnalysisParams()
        self.database_params = DatabaseFilters()
        self.item_params = ItemParams()
        self.plot_params = RankingPlotParams()

    def build(self):

        dataframe = performance_metrics_frame(
            metric=self.analysis_params.metric,
            **self.item_params.__dict__,
            **self.database_params.__dict__,
        )

        dataframe["Rank"] = range(1, len(dataframe) + 1)

        self.set_default_title_texts(
            default_title_text="",
            default_xaxes_title_text=self.item_params.field.replace("_", " ").upper(),
            default_yaxes_title_text=self.analysis_params.metric.replace(
                "_", " "
            ).upper(),
        )

        fig = self.build_ranking_plot(
            dataframe,
            y_col=self.analysis_params.metric,
        )

        return fig
