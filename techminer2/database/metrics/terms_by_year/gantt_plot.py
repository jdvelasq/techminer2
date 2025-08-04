# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Gantt Plot
===============================================================================


Example:
    >>> from techminer2.database.metrics.terms_by_year import GanttPlot
    >>> plotter = (
    ...     GanttPlot()
    ...     #
    ...     # FIELD:
    ...     .with_field("raw_author_keywords")
    ...     .having_terms_in_top(20)
    ...     .having_terms_ordered_by("OCC")
    ...     .having_term_occurrences_between(None, None)
    ...     .having_term_citations_between(None, None)
    ...     .having_terms_in(None)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("examples/fintech/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     .where_records_match(None)
    ... )
    >>> plot = plotter.run()
    >>> plot.write_html("docs_source/_generated/px.database.metrics.terms_by_year.gantt_plot.html")

.. raw:: html

    <iframe src="../_generated/px.database.metrics.terms_by_year.gantt_plot.html"
    height="600px" width="100%" frameBorder="0"></iframe>



"""
import plotly.express as px  # type: ignore

from ...._internals.params_mixin import ParamsMixin
from .data_frame import DataFrame as TermsByYearMetricsDataFrame

COLOR = "#465c6b"
TEXTLEN = 40


class GanttPlot(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def internal__compute_data_frame(self):
        data_frame = TermsByYearMetricsDataFrame().update(**self.params.__dict__).run()

        data_frame["RANKING"] = range(1, len(data_frame) + 1)
        data_frame = data_frame.melt(
            value_name="OCC",
            var_name="column",
            ignore_index=False,
            id_vars=["RANKING"],
        )

        data_frame = data_frame[data_frame.OCC > 0]
        data_frame = data_frame.sort_values(by=["RANKING"], ascending=True)
        data_frame = data_frame.drop(columns=["RANKING"])

        data_frame = data_frame.rename(columns={"column": "Year"})
        data_frame = data_frame.reset_index()

        self.data_frame = data_frame

    # -------------------------------------------------------------------------
    def internal__create_gantt_diagram(self):

        data_frame = self.data_frame.copy()

        fig = px.scatter(
            data_frame,
            x="Year",
            y=self.params.field,
            size="OCC",
            hover_data=data_frame.columns.to_list(),
            color=self.params.field,
        )
        fig.update_layout(
            paper_bgcolor="white",
            plot_bgcolor="white",
            showlegend=False,
            xaxis_title=None,
            yaxis_title=self.params.field.replace("_", " ").upper(),
        )
        fig.update_traces(
            marker={
                "line": {"color": "white", "width": 0.5},
                "opacity": 1.0,
            },
            marker_color=COLOR,
            mode="lines+markers",
            line={"width": 2, "color": COLOR},
        )
        fig.update_xaxes(
            linecolor="white",
            linewidth=1,
            gridcolor="gray",
            griddash="dot",
            tickangle=270,
            dtick=1.0,
        )
        fig.update_yaxes(
            linecolor="white",
            linewidth=1,
            gridcolor="gray",
            griddash="dot",
        )

        self.fig = fig

    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""

        self.internal__compute_data_frame()
        self.internal__create_gantt_diagram()

        return self.fig
