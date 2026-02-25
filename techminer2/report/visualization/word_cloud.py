"""
Word Cloud
===============================================================================


Smoke tests:
    >>> from techminer2 import CorpusField, ItemsOrderBy
    >>> from techminer2.report.visualization import WordCloud
    >>> plot = (
    ...     WordCloud()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(CorpusField.AUTH_KEY_NORM)
    ...     #
    ...     # TERMS:
    ...     .having_items_in_top(80)
    ...     .having_items_ordered_by(ItemsOrderBy.OCC)
    ...     #
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     # PLOT:
    ...     .using_plot_width(400)
    ...     .using_plot_height(400)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/fintech/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     #
    ...     .run()
    ... )
    >>> type(plot).__name__
    'Image'
    >>> plot.save("tmp/database.metrics.performance.word_cloud.png")


"""

from techminer2._internals import ParamsMixin
from techminer2._internals.plots.word_cloud import word_cloud
from techminer2.analyze._internals.performance.performance_metrics import (
    PerformanceMetrics,
)


class WordCloud(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        df = PerformanceMetrics().update(**self.params.__dict__).run()
        fig = word_cloud(params=self.params, dataframe=df)

        return fig


#
