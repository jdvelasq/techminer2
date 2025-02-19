# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Column Plot
===============================================================================

>>> from techminer2.database.metrics.performance import ColumnPlot
>>> plot = (
...     ColumnPlot()
...     #
...     # FIELD:
...     .with_field("author_keywords")
...     #
...     # TERMS:
...     .having_terms_in_top(10)
...     .having_terms_ordered_by("OCC")
...     .having_term_occurrences_between(None, None)
...     .having_term_citations_between(None, None)
...     .having_terms_in(None)
...     #
...     # PLOT:
...     .using_title_text("Ranking Plot")
...     .using_xaxes_title_text("Author Keywords")
...     .using_yaxes_title_text("OCC")
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     #
...     .build()
... )
>>> # plot.write_html("sphinx/_generated/database/metrics/performance/column_plot.html")

.. raw:: html

    <iframe src="../../../_generated/database/metrics/performance/column_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>



"""
from ...._internals.params_mixin import ParamsMixin
from ...._internals.plots.internal__column_plot import internal__column_plot
from .data_frame import DataFrame


class ColumnPlot(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):

        data_frame = DataFrame().update(**self.params.__dict__).build()

        if self.params.title_text is None:
            self.using_title_text("Column Plot")

        if self.params.xaxes_title_text is None:
            self.using_xaxes_title_text(
                self.params.field.replace("_", " ").upper() + " RANK"
            )

        if self.params.yaxes_title_text is None:
            self.using_yaxes_title_text(
                self.params.terms_order_by.replace("_", " ").upper()
            )

        fig = internal__column_plot(params=self.params, data_frame=data_frame)

        return fig
