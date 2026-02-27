"""
Bubble Plot
===============================================================================

.. raw:: html

    <iframe src="../_generated/px.discover.occurrence_matrix.authkw_x_org.bubble_chart.html"
    height="800px" width="100%" frameBorder="0"></iframe>

Smoke tests:
    >>> from techminer2 import ItemsOrderBy
    >>> from techminer2.discover.occurrence_matrix.authkw_x_org import BubbleChart
    >>> fig = (
    ...     BubbleChart()
    ...     #
    ...     # COLUMNS:
    ...     .having_column_items_in_top(10)
    ...     .having_column_items_ordered_by(ItemsOrderBy.OCC)
    ...     .having_column_item_occurrences_between(None, None)
    ...     .having_column_item_citations_between(None, None)
    ...     .having_column_items_in(None)
    ...     #
    ...     # ROWS:
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
    >>> fig.write_html("docsrc/_generated/px.discover.occurrence_matrix.authkw_x_org.bubble_chart.html")


"""

from techminer2 import CorpusField
from techminer2._internals import ParamsMixin

from .._internals import BubbleChart as BaseBubbleChart


class BubbleChart(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        return (
            BaseBubbleChart()
            .with_params(self.params)
            .with_column_field(CorpusField.AUTHKW_NORM)
            .with_index_field(CorpusField.ORG)
            .run()
        )
