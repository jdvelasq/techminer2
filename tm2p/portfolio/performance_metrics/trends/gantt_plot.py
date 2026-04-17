"""
Gantt Plot
===============================================================================

.. raw:: html

    <iframe src="../_generated/px.portfolio.performance_metrics.trends.gantt_plot.html"
    height="600px" width="100%" frameBorder="0"></iframe>

Smoke tests:
    >>> from tm2p.enum import AnalysisUnit, UnitOrderBy
    >>> from tm2p.portfolio.performance_metrics.trends import GanttPlot
    >>> fig = (
    ...     GanttPlot()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.KW)
    ...     #
    ...     .having_top_n_units(20)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> fig.write_html("docsrc/_generated/px.portfolio.performance_metrics.trends.gantt_plot.html")

"""

import plotly.express as px  # type: ignore

from tm2p._intern import ParamsMixin

COLOR = "#465c6b"
TEXTLEN = 40


class GanttPlot(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def internal__compute_data_frame(self):

        from .trends import Trends

        data_frame = Trends().update(**self.params.__dict__).run()

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

        data_frame = data_frame.rename(columns={"column": "YEAR"})
        data_frame = data_frame.reset_index()

        self.data_frame = data_frame

    # -------------------------------------------------------------------------
    def internal__create_gantt_diagram(self):

        data_frame = self.data_frame.copy()

        fig = px.scatter(
            data_frame,
            x="YEAR",
            y=self.params.analysis_unit.value,
            size="OCC",
            hover_data=data_frame.columns.to_list(),
            color=self.params.analysis_unit.value,
        )
        fig.update_layout(
            paper_bgcolor="white",
            plot_bgcolor="white",
            showlegend=False,
            xaxis_title=None,
            yaxis_title=self.params.analysis_unit.value,
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


#
