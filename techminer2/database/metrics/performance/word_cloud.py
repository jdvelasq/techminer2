# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Word Cloud
===============================================================================


Example:
    >>> from techminer2.database.metrics.performance import WordCloud
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
    ...     .where_root_directory_is("examples/fintech/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     #
    ...     .run()
    ... )
    >>> plot.save("docs_source/_generated/database.metrics.performance.word_cloud.png")

.. image:: /_generarted/database.metrics.performance.word_cloud.png
    :width: 900px
    :align: center

"""

from ...._internals.params_mixin import ParamsMixin
from ...._internals.plots.internal__word_cloud import internal__word_cloud
from .data_frame import DataFrame


class WordCloud(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        data_frame = DataFrame().update(**self.params.__dict__).run()
        fig = internal__word_cloud(params=self.params, data_frame=data_frame)

        return fig


#
