# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Word Cloud (MIGRATED)
===============================================================================

## >>> from techminer2.visualize.basic_plots.word_cloud import WordCloud
## >>> plot = (
## ...     WordCloud()
## ...     .set_analysis_params(
## ...         metric="OCC",
## ...     #
## ...     ).set_item_params(
## ...         field="title_nlp_phrases",
## ...         top_n=80,
## ...         occ_range=(None, None),
## ...         gc_range=(None, None),
## ...         custom_terms=None,
## ...     #
## ...     ).set_plot_params(
## ...         width=400, 
## ...         height=400,
## ...     #
## ...     ).set_database_params(
## ...         root_dir="example/", 
## ...         database="main",
## ...         year_filter=(None, None),
## ...         cited_by_filter=(None, None),
## ...     #
## ...     ).build()
## ... )
## >>> plot.save("sphinx/images/visualize/basic_plots/word_cloud.png")

.. image:: /images/visualize/basic_plots/word_cloud.png
    :width: 900px
    :align: center

"""

from ...analyze.metrics.performance_metrics_dataframe import performance_metrics_frame
from ...internals.params.item_params import ItemParams, ItemParamsMixin
from ...internals.plots.word_cloud_mixin import WordCloudMixin, WordCloudParams
from ...internals.set_params_mixin.set_database_filters_mixin import (
    DatabaseFilters,
    SetDatabaseFiltersMixin,
)
from .internals.analysis_params import AnalysisParams, AnalysisParamsMixin


class WordCloud(
    AnalysisParamsMixin,
    WordCloudMixin,
    SetDatabaseFiltersMixin,
    ItemParamsMixin,
):
    """:meta private:"""

    def __init__(self):
        self.analysis_params = AnalysisParams()
        self.database_params = DatabaseFilters()
        self.item_params = ItemParams()
        self.plot_params = WordCloudParams()

    def build(self, metric: str = "OCC"):

        dataframe = performance_metrics_frame(
            metric=metric,
            **self.item_params.__dict__,
            **self.database_params.__dict__,
        )

        fig = self.build_word_cloud(
            dataframe,
            values_col=self.analysis_params.metric,
        )

        return fig
