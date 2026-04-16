"""
WordCloud
===============================================================================

.. image:: ../_generated/px.portfolio.performance_metrics.item_metrics.word_cloud.png
    :width: 800px
    :align: center

Smoke tests:
    >>> from tm2p.enum import Field, ItemOrderBy
    >>> from tm2p.portfolio.performance_metrics.item_metrics import WordCloud
    >>> plot = (
    ...     WordCloud()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.AUTHKW_NORM)
    ...     #
    ...     # TERMS:
    ...     .having_items_in_top(80)
    ...     .having_items_ordered_by(ItemOrderBy.OCC)
    ...     #
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     # PLOT:
    ...     .using_plot_width(2400)
    ...     .using_plot_height(2400)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     #
    ...     .run()
    ... )
    >>> type(plot).__name__
    'Image'
    >>> plot.save("docsrc/_generated/px.portfolio.performance_metrics.item_metrics.word_cloud.png")


"""

from tm2p._intern import ParamsMixin
from tm2p._intern.plots.basic.word_cloud import word_cloud

from .metrics import Metrics


class WordCloud(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        df = Metrics().update(**self.params.__dict__).run()
        fig = word_cloud(params=self.params, dataframe=df)

        return fig


#
