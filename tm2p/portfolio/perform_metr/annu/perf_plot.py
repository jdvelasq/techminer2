"""
PerformancePlot
===============================================================================

.. raw:: html

    <iframe src="../_generated/px.portfolio.perform_metr.annu.performance_plot.html"
    height="600px" width="100%" frameBorder="0"></iframe>


Smoke tests:

    >>> from tm2p.portfolio.perform_metr.annu import PerformancePlot
    >>> fig = (
    ...     PerformancePlot()
    ...     #
    ...     .using_line_width(1.5)
    ...     .using_marker_size(7)
    ...     .using_uniform_textfont_size(10)
    ...     .using_yshift(4)
    ...     #
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> assert type(fig).__name__ == 'Figure'
    >>> fig.write_html("docsrc/_generated/px.portfolio.perform_metr.annu.performance_plot.html")



"""

import plotly.graph_objects as go  # type: ignore

from tm2p._intern import ParamsMixin
from tm2p.portfolio.perform_metr.annu.metr import Metrics

MEAN_GCS_PER_YEAR = "MEAN_GCS_PER_YEAR"
OCC = "OCC"


class PerformancePlot(
    ParamsMixin,
):
    """:meta private:"""

    def _create_figure(self):
        return go.Figure()

    def _compute_metrics(self):
        return Metrics().update(**self.params.__dict__).run()

    def _plot_annual_publications(self, fig, df):
        fig.add_trace(
            go.Bar(
                x=df.index,
                y=df[OCC],  # type: ignore
                name="Annual Publications",
                opacity=0.7,
                marker_color="lightgrey",
                marker_line_color="darkslategray",
                marker_line_width=0.6,
            )
        )

    def _plot_avg_citations_per_year(self, fig, df):
        fig.add_trace(
            go.Scatter(
                x=df.index,
                y=df[MEAN_GCS_PER_YEAR],  # type: ignore
                name="Mean Global Citations per Year",
                mode="markers+lines",
                marker=dict(
                    size=self.params.marker_size,
                    color="gray",
                    line=dict(color="darkslategray", width=1.5),
                    symbol="circle",
                ),
                yaxis="y2",
            ),
        )

    def _update_layout(self, fig):
        fig.update_layout(
            paper_bgcolor="white",
            plot_bgcolor="white",
            title="Annual Performance Metrics",
            bargap=0.6,
            legend=dict(
                traceorder="reversed",
                x=0.5,
                y=0.99,
                xanchor="center",
                yanchor="top",
            ),
            yaxis=dict(
                title="Annual Publications",
                linecolor="lightgrey",
                linewidth=2,
                gridcolor="lightgray",
                griddash="dot",
                rangemode="tozero",
                fixedrange=False,
            ),
            yaxis2=dict(
                title="Avg. Global Citations per Year",
                overlaying="y",
                side="right",
                showgrid=False,
                linecolor="lightgray",
                linewidth=2,
                zeroline=False,
                anchor="x",
                fixedrange=False,
            ),
        )

    def _update_x_axis(self, fig):
        fig.update_xaxes(
            linecolor="gray",
            linewidth=4,
            gridcolor="lightgray",
            griddash="dot",
            title="Year",
            tickangle=270,
            dtick=1,
        )

    def run(self):

        df = self._compute_metrics()

        fig = self._create_figure()

        year_max = df.index.max()
        year_max_right = year_max + 0.5
        year_max_left = year_max - 2.5

        fig.add_vrect(
            x0=year_max_left,
            x1=year_max_right,
            fillcolor="lightyellow",
            opacity=0.3,
            line_width=0,
            annotation_text="Incomplete citation window",
            annotation_position="top left",
            annotation_font_size=9,
        )

        self._plot_annual_publications(fig, df)
        self._plot_avg_citations_per_year(fig, df)
        self._update_layout(fig)
        self._update_x_axis(fig)

        return fig
