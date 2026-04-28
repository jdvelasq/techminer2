"""
Gantt Plot
===============================================================================

.. raw:: html

    <iframe src="../_generated/px.portfolio.emerg.emerg.gantt_plot.html"
    height="600px" width="100%" frameBorder="0"></iframe>

Smoke tests:
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.portfolio.emerg.emerg import GanttPlot  # type: ignore
    >>> fig = (
    ...     GanttPlot()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.KW)
    ...     #
    ...     # EMERGENCE:
    ...     .using_emergence_baseline_periods(3)
    ...     .using_emergence_recent_periods(3)
    ...     .using_emergence_novelty_threshold(0.15)
    ...     .using_emergence_min_total_records(7)
    ...     .using_emergence_min_active_periods(3)
    ...     .using_emergence_ratio_threshold(0.5)
    ...     #
    ...     .having_top_n_units(20)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> fig.write_html("docsrc/_generated/px.portfolio.emerg.emerg.gantt_plot.html")

"""

import plotly.express as px  # type: ignore

from tm2p._intern import ParamsMixin
from tm2p.enum import UnitOrderBy

from .metr import Metrics

COLOR = "#465c6b"
TEXTLEN = 40


class GanttPlot(
    ParamsMixin,
):
    """:meta private:"""

    def _compute_emergence_metrics(self):
        return Metrics().update(**self.params.__dict__).run()

    def _compute_trends(self, metrics):

        from ...perform_metr.trend import Trends

        df = (
            Trends()
            .update(**self.params.__dict__)
            #
            .having_top_n_units(None)
            .having_units_ordered_by(UnitOrderBy.OCC)
            .having_unit_occurrence_between(None, None)
            .having_unit_global_citation_between(None, None)
            .having_units_in(None)
            .run()
        )
        df = df[df.index.isin(metrics.index)]
        df = df.loc[metrics.index, :]
        df = df.head(self.params.top_n_units)

        return df

    # -------------------------------------------------------------------------
    def _prepare_data(self, trends):

        df = trends.copy()

        df["RANKING"] = range(1, len(df) + 1)
        df = df.melt(
            value_name="OCC",
            var_name="column",
            ignore_index=False,
            id_vars=["RANKING"],
        )

        df = df[df.OCC > 0]
        df = df.sort_values(by=["RANKING"], ascending=True)
        df = df.drop(columns=["RANKING"])

        df = df.rename(columns={"column": "YEAR"})
        df = df.reset_index()

        return df

    # -------------------------------------------------------------------------
    def _create_gantt_diagram(self, df):

        df = df.copy()

        fig = px.scatter(
            df,
            x="YEAR",
            y=self.params.analysis_unit.value,
            size="OCC",
            hover_data=df.columns.to_list(),
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

        return fig

    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""

        metrics = self._compute_emergence_metrics()
        trends = self._compute_trends(metrics)
        df = self._prepare_data(trends)
        fig = self._create_gantt_diagram(df)

        return fig


#
