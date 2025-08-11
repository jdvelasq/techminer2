# flake8: noqa
# pylint: disable=import-outside-toplevel
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Ranking Plot
===============================================================================


Example:
    >>> from techminer2.database.metrics.performance import RankingPlot
    >>> plot = (
    ...     RankingPlot()
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
    ...     .using_line_color("black")
    ...     .using_line_width(1.5)
    ...     .using_marker_size(7)
    ...     .using_textfont_size(10)
    ...     .using_title_text("Ranking Plot")
    ...     .using_xaxes_title_text("Author Keywords")
    ...     .using_yaxes_title_text("OCC")
    ...     .using_yshift(4)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("examples/fintech/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     #
    ...     .run()
    ... )
    >>> plot.write_html("docs_source/_generated/px.database.metrics.performance.ranking_plot.html")

.. raw:: html

    <iframe src="../_generated/px.database.metrics.performance.ranking_plot.html"
    height="600px" width="100%" frameBorder="0"></iframe>


"""
from techminer2._internals.params_mixin import ParamsMixin
from techminer2._internals.plots.internal__ranking_plot import internal__ranking_plot
from techminer2.database.metrics.performance.data_frame import DataFrame


class RankingPlot(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        data_frame = DataFrame().update(**self.params.__dict__).run()

        data_frame["Rank"] = range(1, len(data_frame) + 1)

        if self.params.title_text is None:
            self.using_title_text("Ranking Plot")

        if self.params.xaxes_title_text is None:
            self.using_xaxes_title_text(
                self.params.field.replace("_", " ").upper() + " RANK"
            )

        if self.params.yaxes_title_text is None:
            self.using_yaxes_title_text(
                self.params.terms_order_by.replace("_", " ").upper()
            )

        fig = internal__ranking_plot(params=self.params, data_frame=data_frame)

        return fig


#
