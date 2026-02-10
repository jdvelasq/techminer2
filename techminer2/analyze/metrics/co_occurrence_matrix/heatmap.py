# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Heatmap
===============================================================================


Example:
    >>> from techminer2.packages.co_occurrence_matrix import Heatmap
    >>> plot = (
    ...     Heatmap()
    ...     #
    ...     # COLUMNS:
    ...     .with_field("author_keywords")
    ...     .having_terms_in_top(10)
    ...     .having_terms_ordered_by("OCC")
    ...     .having_term_occurrences_between(2, None)
    ...     .having_term_citations_between(None, None)
    ...     .having_terms_in(None)
    ...     #
    ...     # ROWS:
    ...     .with_other_field(None)
    ...     .having_other_terms_in_top(None)
    ...     .having_other_terms_ordered_by(None)
    ...     .having_other_term_occurrences_between(None, None)
    ...     .having_other_term_citations_between(None, None)
    ...     .having_other_terms_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_term_counters(True)
    ...     #
    ...     # PLOT:
    ...     .using_title_text(None)
    ...     .using_colormap("Blues")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("examples/small/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> plot.write_html("docs_source/_generated/px.packages.co_occurrence_matrix.heatmap.html")

.. raw:: html

    <iframe src="../_generated/px.packages.co_occurrence_matrix.heatmap.html"
    height="800px" width="100%" frameBorder="0"></iframe>



"""
from techminer2._internals import ParamsMixin
from techminer2._internals.plots.internal__heatmap import internal__heatmap
from techminer2.analyze.metrics.co_occurrence_matrix.matrix_data_frame import (
    MatrixDataFrame,
)


class Heatmap(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        data_frame = MatrixDataFrame().update(**self.params.__dict__).run()
        fig = internal__heatmap(self.params, data_frame)
        return fig
