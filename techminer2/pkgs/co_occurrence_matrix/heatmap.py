# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Heatmap
===============================================================================

>>> from techminer2.analyze.cross_co_occurrence import CrossCoOccurrenceHeatmap
>>> plot = (
...     Heatmap()
...     #
...     # COLUMNS:
...     .wiht_field("author_keywords")
...     #
...     .having_terms_in_top(10)
...     .having_terms_ordered_by("OCC")
...     .having_term_occurrences_between(2, None)
...     .having_term_citations_between(None, None)
...     .having_terms_in(None)
...     #
...     # ROWWS:
...     .wiht_other_field("None")
...     #
...     .having_other_terms_in_top(10)
...     .having_other_terms_ordered_by("OCC")
...     .having_other_term_occurrences_between(2, None)
...     .having_other_term_citations_between(None, None)
...     .having_other_terms_in(None)
...     #
...     # COUNTERS:
...     .using_term_counters(True)
...     #
...     # PLOT:
...     .using_title_text(None)
...     .using_colormap("Blues")
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     .where_records_match(None)
...     #
...     .build()
... )
>>> plot.write_html("sphinx/_generated/co_occurrence_matrix//heatmap.html")

.. raw:: html

    <iframe src="../../_generated/co_occurrence_matrix/heatmap.html" 
    height="800px" width="100%" frameBorder="0"></iframe>



"""
from ...internals import DatabaseFilters, SetDatabaseFiltersMixin
from ...internals.params.columns_and_rows_params import ColumnsAndRowsParamsMixin
from ...internals.params.item_params import ItemParams
from ...internals.plots.internal__heatmap import HeatmapMixin, HeatmapParams
from .internals.output_params import OutputParams, OutputParamsMixin
from .matrix_data_frame import CrossCoOccurrenceMatrix


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
