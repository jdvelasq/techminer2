# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Bar Plot
===============================================================================


Example:
    >>> from techminer2.database.metrics.performance import BarPlot
    >>> plot = (
    ...     BarPlot()
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
    ...     .using_title_text("Bar Plot")
    ...     .using_xaxes_title_text("Author Keywords")
    ...     .using_yaxes_title_text("OCC")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("example/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     #
    ...     .run()
    ... )
    >>> plot.write_html("docs_source/_generated/px.database.metrics.performance.bar_plot.html")

.. raw:: html

    <iframe src="../_generated/px.database.metrics.performance.bar_plot.html"
    height="600px" width="100%" frameBorder="0"></iframe>

"""
from ...._internals.params_mixin import ParamsMixin
from ...._internals.plots.internal__bar_plot import internal__bar_plot
from .data_frame import DataFrame


class BarPlot(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        data_frame = DataFrame().update(**self.params.__dict__).run()

        if self.params.title_text is None:
            self.using_title_text("Bar Plot")

        if self.params.xaxes_title_text is None:
            self.using_xaxes_title_text(
                self.params.terms_order_by.replace("_", " ").upper()
            )

        if self.params.yaxes_title_text is None:
            self.using_yaxes_title_text(self.params.field.replace("_", " ").upper())

        fig = internal__bar_plot(params=self.params, data_frame=data_frame)

        return fig
