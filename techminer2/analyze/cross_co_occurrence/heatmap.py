# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Heatmap (MIGRATED)
===============================================================================

## >>> from techminer2.analyze.cross_co_occurrence import CrossCoOccurrenceHeatmap
## >>> plot = (
## ...     CrossCoOccurrenceHeatmap()
## ...     .set_columns_params(
## ...         field="author_keywords",
## ...         top_n=10,
## ...         occ_range=(None, None),
## ...         gc_range=(None, None),
## ...         custom_terms=None,
## ...     #
## ...     ).set_rows_params(
## ...         field=None,
## ...         top_n=None,
## ...         occ_range=(None, None),
## ...         gc_range=(None, None),
## ...         custom_terms=None,
## ...     #
## ...     ).set_plot_params(
## ...         title_text=None,
## ...         colormap="Blues",
## ...     #
## ...     ).set_database_params(
## ...         root_dir="example/", 
## ...         database="main",
## ...         year_filter=(None, None),
## ...         cited_by_filter=(None, None),
## ...     #
## ...     ).build()
## ... )
## >>> plot.write_html("sphinx/_generated/analyze/cross_co_occurrence/heatmap.html")

.. raw:: html

    <iframe src="../../_generated/analyze/cross_co_occurrence/heatmap.html" 
    height="800px" width="100%" frameBorder="0"></iframe>



"""
from ...internals.params.columns_and_rows_params import ColumnsAndRowsParamsMixin
from ...internals.params.item_params import ItemParams
from ...internals.plots.heatmap_mixin import HeatmapMixin, HeatmapParams
from ...internals.set_params_mixin.set_database_filters_mixin import (
    DatabaseFilters,
    SetDatabaseFiltersMixin,
)
from .internals.output_params import OutputParams, OutputParamsMixin
from .matrix import CrossCoOccurrenceMatrix


class CrossCoOccurrenceHeatmap(
    ColumnsAndRowsParamsMixin,
    SetDatabaseFiltersMixin,
    HeatmapMixin,
    OutputParamsMixin,
):
    """:meta private:"""

    def __init__(self):
        self.plot_params = HeatmapParams()
        self.columns_params = ItemParams()
        self.database_params = DatabaseFilters()
        self.rows_params = ItemParams()
        self.output_params = OutputParams()

    def build(self):

        dataframe = (
            CrossCoOccurrenceMatrix()
            .set_columns_params(**self.columns_params.__dict__)
            .set_rows_params(**self.rows_params.__dict__)
            .set_output_params(**self.output_params.__dict__)
            .set_database_params(**self.database_params.__dict__)
            .build()
        )

        fig = self.build_heatmap(dataframe)

        return fig
