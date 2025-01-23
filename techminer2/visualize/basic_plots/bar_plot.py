# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Bar Plot (MIGRATED)
===============================================================================

## >>> from techminer2.visualize.basic_plots.bar_plot import BarPlot
## >>> plot = (
## ...     BarPlot()
## ...     .with_source_field("author_keywords")
## ...     .select_top_n_terms(10)
## ...     .order_terms_by("OCC")
## ...     .having_term_occurrences_between(None, None)
## ...     .having_term_citations_between(None, None)
## ...     .having_terms_in(None)
## ...     #
## ...     .using_bar_color("blue")
## ...     #
## ...     .where_directory_is("example/")
## ...     .where_database_is("main")
## ...     .where_record_years_between(None, None)
## ...     .where_record_citations_between(None, None)
## ...     #
## ...     ).build()



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
## ...         xaxes_title_text=None,
## ...         yaxes_title_text=None,
## ...     #
## ...     ).set_database_params(
## ...         root_dir="example/", 
## ...         database="main",
## ...         year_filter=(None, None),
## ...         cited_by_filter=(None, None),
## ...     #
## ...     ).build()
## ... )
## >>> plot.write_html("sphinx/_generated/visualize/basic_plots/bar_plot.html")

.. raw:: html

    <iframe src="../../_generated/visualize/basic_plots/bar_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>


"""
from ...database.metrics.performance_metrics.data_frame import performance_metrics_frame
from ...internals.params.item_params import ItemParams, ItemParamsMixin
from ...internals.plots.bar_plot_mixin import BarPlotMixin, BarPlotParams
from ...internals.set_params_mixin.set_database_filters_mixin import (
    DatabaseFilters,
    SetDatabaseFiltersMixin,
)
from .internals.analysis_params import AnalysisParams, AnalysisParamsMixin
from .internals.basic_plot import BasicPlotMixin


class BarPlot(
    AnalysisParamsMixin,
    BarPlotMixin,
    BasicPlotMixin,
    SetDatabaseFiltersMixin,
    ItemParamsMixin,
):
    """:meta private:"""

    def __init__(self):
        self.analysis_params = AnalysisParams()
        self.plot_params = BarPlotParams()
        self.database_params = DatabaseFilters()
        self.item_params = ItemParams()

    def build(self):

        dataframe = performance_metrics_frame(
            metric=self.analysis_params.metric,
            **self.item_params.__dict__,
            **self.database_params.__dict__,
        )

        self.set_default_title_texts(
            default_title_text="",
            default_xaxes_title_text=self.analysis_params.metric.replace(
                "_", " "
            ).upper(),
            default_yaxes_title_text=self.item_params.field.replace("_", " ").upper(),
        )

        fig = self.build_bar_plot(
            dataframe,
            x_col=self.analysis_params.metric,
        )

        return fig
