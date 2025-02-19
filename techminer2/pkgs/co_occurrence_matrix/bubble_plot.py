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

>>> from techminer2.pkgs.co_occurrence_matrix import BubblePlot
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
...     .where_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     .where_records_match(None)
...     #
...     .build()
... )
>>> # plot.write_html("sphinx/_generated/pkgs/co_occurrence_matrix/bubble_plot.html")

.. raw:: html

    <iframe src="../../_generated/pkgs/co_occurrence_matrix/bubble_plot.html" 
    height="800px" width="100%" frameBorder="0"></iframe>

"""
from ..._internals.mixins import ParamsMixin
from ..._internals.plots.internal__bubble_plot import internal__bubble_plot
from .data_frame import DataFrame


class BubblePlot(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):

        data_frame = DataFrame().update(**self.params.__dict__).build()

        fig = internal__bubble_plot(
            self.params,
            x_name="rows",
            y_name="columns",
            size_col="OCC",
            data_frame=data_frame,
        )

        return fig
