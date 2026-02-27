"""
Bubble Plot
===============================================================================

.. raw:: html

    <iframe src="../_generated/px.discover.occurrence_matrix._internals.bubble_chart.html"
    height="800px" width="100%" frameBorder="0"></iframe>

Smoke tests:
    >>> from techminer2 import CorpusField, ItemsOrderBy
    >>> from techminer2.discover.occurrence_matrix._internals import BubbleChart
    >>> fig = (
    ...     BubbleChart()
    ...     #
    ...     # COLUMNS:
    ...     .with_column_field(CorpusField.AUTHKW_TOK)
    ...     .having_column_items_in_top(10)
    ...     .having_column_items_ordered_by(ItemsOrderBy.OCC)
    ...     .having_column_item_occurrences_between(None, None)
    ...     .having_column_item_citations_between(None, None)
    ...     .having_column_items_in(None)
    ...     #
    ...     # ROWS:
    ...     .with_index_field(CorpusField.AUTH_NORM)
    ...     .having_index_items_in_top(15)
    ...     .having_index_items_ordered_by(ItemsOrderBy.OCC)
    ...     .having_index_item_occurrences_between(0, None)
    ...     .having_index_item_citations_between(None, None)
    ...     .having_index_items_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_item_counters(True)
    ...     #
    ...     # PLOT:
    ...     .using_title_text(None)
    ...     .using_colormap("Blues")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/fintech/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> type(fig).__name__
    'Figure'
    >>> fig.write_html("docsrc/_generated/px.discover.occurrence_matrix._internals.bubble_chart.html")


"""

from techminer2._internals import ParamsMixin
from techminer2._internals.plots.bubble_chart import bubble_chart
from techminer2.discover.occurrence_matrix._internals.matrix_list import MatrixList


class BubbleChart(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        data_frame = MatrixList().update(**self.params.__dict__).run()

        fig = bubble_chart(
            self.params,
            x_name="rows",
            y_name="columns",
            size_col="OCC",
            dataframe=data_frame,
        )

        return fig
