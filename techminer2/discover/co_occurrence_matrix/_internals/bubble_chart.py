"""
Smoke tests:
    >>> from techminer2 import CorpusField, ItemsOrderBy
    >>> from techminer2.discover.co_occurrence_matrix._internals import BubbleChart
    >>> fig = (
    ...     BubbleChart()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(CorpusField.AUTHKW_TOK)
    ...     .having_items_in_top(10)
    ...     .having_items_ordered_by(ItemsOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
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
    >>> fig.write_html("docsrc/_generated/px.discover.co_occurrence_matrix._internals.bubble_chart.html")


"""

from techminer2._internals import ParamsMixin
from techminer2._internals.plots.bubble_chart import bubble_chart

from .matrix_list import MatrixList


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
