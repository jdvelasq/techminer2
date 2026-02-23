"""
Column Plot
===============================================================================

Smoke tests:
    >>> from techminer2 import CorpusField, ItemsOrderBy
    >>> from techminer2.report.visualization import ColumnPlot
    >>> plot = (
    ...     ColumnPlot()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(CorpusField.AUTH_KEY_NORM)
    ...     #
    ...     # TERMS:
    ...     .having_items_in_top(10)
    ...     .having_items_ordered_by(ItemsOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     # PLOT:
    ...     .using_title_text("Ranking Plot")
    ...     .using_xaxes_title_text("Author Keywords")
    ...     .using_yaxes_title_text("OCC")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/data/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     #
    ...     .run()
    ... )
    >>> type(plot).__name__
    'Figure'
    >>> plot.write_html("tmp/px.database.metrics.performance.column_plot.html")


"""

from techminer2._internals import ParamsMixin
from techminer2._internals.plots.column_plot import column_plot
from techminer2.report.visualization.dataframe import DataFrame


class ColumnPlot(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        df = DataFrame().update(**self.params.__dict__).run()
        fig = column_plot(params=self.params, dataframe=df)

        return fig


#
