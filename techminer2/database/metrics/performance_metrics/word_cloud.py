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

>>> from techminer2.database.metrics.performance_metrics import WordCloud
>>> plot = (
...     WordCloud()
...     #
...     .with_source_field("raw_document_title_nouns_and_phrases")
...     .select_top_n_terms(80)
...     .order_terms_by("OCC")
...     .having_term_occurrences_between(None, None)
...     .having_term_citations_between(None, None)
...     .having_terms_in(None)
...     #
...     .using_plot_width(400)
...     .using_plot_height(400)
...     #
...     .where_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     #
...     .build()
... )
>>> plot.save("sphinx/images/database/metrics/performance_metrics/word_cloud.png")

.. image:: /images/database/metrics/performance_metrics/word_cloud.png
    :width: 900px
    :align: center

"""

from ....internals.mixins.input_functions import InputFunctionsMixin
from ....internals.mixins.word_cloud import WordCloudMixin
from .data_frame import DataFrame


class WordCloud(
    InputFunctionsMixin,
    WordCloudMixin,
):
    """:meta private:"""

    def build(self):

        data_frame = DataFrame().update_params(**self.params.__dict__).build()
        fig = self.build_word_cloud(data_frame)

        return fig
