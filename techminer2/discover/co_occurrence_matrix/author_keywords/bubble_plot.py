"""
Bubble Plot
===============================================================================


Smoke tests:
    >>> from techminer2 import CorpusField, ItemsOrderBy
    >>> from techminer2.packages.co_occurrence_matrix import BubblePlot
    >>> plot = (
    ...     BubblePlot()
    ...     #
    ...     # COLUMNS:
    ...     .with_field(CorpusField.AUTH_KEY_TOK)
    ...     .having_items_in_top(10)
    ...     .having_items_ordered_by("OCC")
    ...     .having_item_occurrences_between(2, None)
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
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> plot.write_html("docsrc/_generated/px.packages.co_occurrence_matrix.bubble_plot.html")

.. raw:: html

    <iframe src="../_generated/px.packages.co_occurrence_matrix.bubble_plot.html"
    height="800px" width="100%" frameBorder="0"></iframe>

"""

from techminer2._internals import ParamsMixin
from techminer2._internals.plots.bubble_chart import bubble_chart
from techminer2.discover.occurrence_matrix._internals.matrix_list import MatrixList


class BubblePlot(
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
