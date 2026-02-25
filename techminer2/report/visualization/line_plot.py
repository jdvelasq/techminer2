"""
Line Plot
===============================================================================

Smoke tests:
    >>> from techminer2 import CorpusField, ItemsOrderBy
    >>> from techminer2.report.visualization import LinePlot
    >>> plot = (
    ...     LinePlot()
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
    ...     .using_title_text("Line Plot")
    ...     .using_xaxes_title_text("Author Keywords")
    ...     .using_yaxes_title_text("OCC")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/fintech/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     #
    ...     .run()
    ... )
    >>> type(plot).__name__
    'Figure'
    >>> plot.write_html("tmp/px.database.metrics.performance.line_plot.html")



"""

from techminer2._internals import ParamsMixin
from techminer2._internals.plots.line_plot import line_plot
from techminer2.analyze._internals.performance.performance_metrics import (
    PerformanceMetrics,
)


class LinePlot(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        df = PerformanceMetrics().update(**self.params.__dict__).run()
        fig = line_plot(params=self.params, df=df)

        return fig


#
