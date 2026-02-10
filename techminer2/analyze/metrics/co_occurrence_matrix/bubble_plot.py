# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-few-public-methods
"""
Bubble Plot
===============================================================================


Example:
    >>> from techminer2.packages.co_occurrence_matrix import BubblePlot
    >>> plot = (
    ...     BubblePlot()
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
    >>> plot.write_html("docs_source/_generated/px.packages.co_occurrence_matrix.bubble_plot.html")

.. raw:: html

    <iframe src="../_generated/px.packages.co_occurrence_matrix.bubble_plot.html"
    height="800px" width="100%" frameBorder="0"></iframe>

"""
from techminer2._internals import ParamsMixin
from techminer2._internals.plots.internal__bubble_plot import internal__bubble_plot
from techminer2.analyze.metrics.co_occurrence_matrix.data_frame import DataFrame


class BubblePlot(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        data_frame = DataFrame().update(**self.params.__dict__).run()

        fig = internal__bubble_plot(
            self.params,
            x_name="rows",
            y_name="columns",
            size_col="OCC",
            data_frame=data_frame,
        )

        return fig
