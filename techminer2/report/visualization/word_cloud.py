"""
Word Cloud
===============================================================================


Smoke tests:
    >>> from techminer2.analyze.metrics.performance import WordCloud
    >>> plot = (
    ...     WordCloud()
    ...     #
    ...     # FIELD:
    ...     .with_field("raw_document_title_nouns_and_phrases")
    ...     #
    ...     # TERMS:
    ...     .having_terms_in_top(80)
    ...     .having_terms_ordered_by("OCC")
    ...     #
    ...     .having_term_occurrences_between(None, None)
    ...     .having_term_citations_between(None, None)
    ...     .having_terms_in(None)
    ...     #
    ...     # PLOT:
    ...     .using_plot_width(400)
    ...     .using_plot_height(400)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("examples/tests/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     #
    ...     .run()
    ... )
    >>> plot.save("docs_source/_generated/database.metrics.performance.word_cloud.png")

.. image:: /_generarted/database.metrics.performance.word_cloud.png
    :width: 900px
    :align: center

"""

from techminer2._internals import ParamsMixin
from techminer2._internals.plots.word_cloud import word_cloud
from techminer2.report.visualization.dataframe import DataFrame


class WordCloud(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        data_frame = DataFrame().update(**self.params.__dict__).run()
        fig = word_cloud(params=self.params, dataframe=data_frame)

        return fig


#
