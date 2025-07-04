# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=import-outside-toplevel
"""
Bar Chart
===============================================================================


Example:
    >>> from techminer2.database.metrics.trending_terms.user import BarChart

    >>> # Create, configure, and run the plotter
    >>> plotter = (
    ...     BarChart()
    ...     #
    ...     # FIELD:
    ...     .with_field("raw_author_keywords")
    ...     .having_terms_in_top(20)
    ...     .having_terms_ordered_by("OCC")
    ...     .having_term_occurrences_between(None, None)
    ...     .having_term_citations_between(None, None)
    ...     .having_terms_in(None)
    ...     #
    ...     # TIME WINDOW:
    ...     .with_time_window(2)
    ...     #
    ...     # CHART PARAMS:
    ...     .using_xaxes_title_text(None)
    ...     .using_yaxes_title_text(None)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("example/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     .where_records_match(None)
    ... )
    >>> plot = plotter.run()
    >>> plot.write_html("docs_source/_generated/px.database.metrics.trending_terms.user.html")

.. raw:: html

    <iframe src="../_generated/px.database.metrics.trending_terms.user.html"
    height="600px" width="100%" frameBorder="0"></iframe>


"""
import plotly.express as px  # type: ignore

from ....._internals.mixins import ParamsMixin
from .data_frame import DataFrame


class BarChart(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def internal__compute_data_frame(self):

        data_frame = DataFrame().update(**self.params.__dict__).run()

        # extracts the name of column starting with 'between'
        between = [_ for _ in data_frame.columns if _.startswith("between")][0]
        before = [_ for _ in data_frame.columns if _.startswith("before")][0]

        fig_data = data_frame[["OCC", before, between]].copy()
        fig_data[self.params.field] = fig_data.index
        fig_data = fig_data.reset_index(drop=True)

        fig_data = fig_data.melt(
            id_vars=self.params.field,
            value_vars=[before, between],
        )

        fig_data = fig_data.rename(
            columns={
                self.params.field: self.params.field.replace("_", " ").title(),
                "variable": "Period",
                "value": "Num Documents",
            }
        )

        self.before = before
        self.between = between
        self.data_frame = fig_data

    # -------------------------------------------------------------------------
    def internal__make_fig(self):

        #
        # Extracs only the performance metrics data frame
        fig = px.bar(
            self.data_frame,
            x="Num Documents",
            y=self.params.field.replace("_", " ").title(),
            color="Period",
            orientation="h",
            color_discrete_map={
                self.before: "#7793a5",
                self.between: "#465c6b",
            },
        )
        fig.update_layout(
            paper_bgcolor="white",
            plot_bgcolor="white",
        )
        fig.update_yaxes(
            linecolor="gray",
            linewidth=2,
            autorange="reversed",
            title=self.params.yaxes_title_text,
        )
        fig.update_xaxes(
            linecolor="gray",
            linewidth=2,
            gridcolor="gray",
            griddash="dot",
            title=self.params.xaxes_title_text,
        )

        self.fig = fig

    # -------------------------------------------------------------------------
    def run(self):
        self.internal__compute_data_frame()
        self.internal__make_fig()
        return self.fig


# =============================================================================
