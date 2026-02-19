# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Bar Chart
===============================================================================


Smoke tests:
    >>> # Create, configure, and run the plotter
    >>> from techminer2.analyze.metrics.trending_terms_by_year.user import BarChart
    >>> (
    ...     BarChart()
    ...     #
    ...     # FIELD:
    ...     .with_field("author_keywords_raw")
    ...     .having_terms_per_year(5)
    ...     .having_terms_in(None)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("examples/tests/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... ).write_html("docs_source/_generated/px.database.metrics.ternding_terms_by_year.user.bar_chart.html")

.. raw:: html

    <iframe src="../_generated/px.database.metrics.ternding_terms_by_year.user.bar_chart.html"
    height="600px" width="100%" frameBorder="0"></iframe>


"""
import plotly.graph_objects as go  # type: ignore

from techminer2._internals import ParamsMixin
from techminer2.analyze.metrics.trending_terms_by_year.usr.data_frame import DataFrame


class BarChart(
    ParamsMixin,
):
    """:meta private:"""

    # ---------------------------------------------------------------------------
    def run(self):

        words_by_year = (
            DataFrame()
            .update(**self.params.__dict__)
            .update(terms_order_by="OCC")
            .run()
        )

        fig = go.Figure(
            go.Bar(
                x=words_by_year.width,
                y=words_by_year.index,
                base=words_by_year.year_q1,
                width=words_by_year.height,
                orientation="h",
                marker_color="lightslategrey",
            ),
        )
        fig.update_layout(
            paper_bgcolor="white",
            plot_bgcolor="white",
        )
        fig.update_yaxes(
            linecolor="gray",
            linewidth=1,
            gridcolor="lightgray",
            griddash="dot",
        )
        fig.update_xaxes(
            linecolor="gray",
            linewidth=1,
            gridcolor="lightgray",
            griddash="dot",
            tickangle=270,
            dtick=1.0,
        )

        return fig


#
