# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Pie Plot (MIGRATED)
===============================================================================


## >>> from techminer2.visualize.basic_plots.pie_plot import PiePlot
## >>> plot = (
## ...     PiePlot()
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
## ...         title_text="Most Frequent Author Keywords",
## ...         hole=0.4,
## ...     #
## ...     ).set_database_params(
## ...         root_dir="example/", 
## ...         database="main",
## ...         year_filter=(None, None),
## ...         cited_by_filter=(None, None),
## ...     #
## ...     ).build()
## ... )
## >>> plot.write_html("sphinx/_generated/visualize/basic_plots/pie_plot.html")

.. raw:: html

    <iframe src="../../_generated/visualize/basic_plots/pie_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>


"""
from ...database.metrics.performance_metrics.data_frame import performance_metrics_frame
from ...internals.params.item_params import ItemParams, ItemParamsMixin
from ...internals.plots.pie_plot_mixin import PiePlotMixin, PiePlotParams
from ...internals.set_params_mixin.set_database_filters_mixin import (
    DatabaseFilters,
    SetDatabaseFiltersMixin,
)
from .internals.analysis_params import AnalysisParams, AnalysisParamsMixin
from .internals.basic_plot import BasicPlotMixin


class PiePlot(
    AnalysisParamsMixin,
    BasicPlotMixin,
    PiePlotMixin,
    SetDatabaseFiltersMixin,
    ItemParamsMixin,
):
    """:meta private:"""

    def __init__(self):
        self.analysis_params = AnalysisParams()
        self.database_params = DatabaseFilters()
        self.item_params = ItemParams()
        self.plot_params = PiePlotParams()

    def build(self):

        dataframe = performance_metrics_frame(
            metric=self.analysis_params.metric,
            **self.item_params.__dict__,
            **self.database_params.__dict__,
        )

        fig = self.build_pie_plot(
            dataframe,
            values_col=self.analysis_params.metric,
        )

        return fig
