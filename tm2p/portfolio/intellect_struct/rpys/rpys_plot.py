"""
RPYSPlot
===============================================================================

.. raw:: html

    <iframe src="../_generated/px.portfolio.intellect_struct.rpys.rpys_plot.html"
    height="800px" width="100%" frameBorder="0"></iframe>


Smoke tests:
    >>> from tm2p.portfolio.intellect_struct.rpys import RPYSPlot  # type: ignore
    >>> plot = (
    ...     RPYSPlot()
    ...     #
    ...     .using_rpys_peaks(3)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/system-dynamics-wos/")
    ...     .where_record_years_range(None, 2025)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     .run()
    ... )
    >>> plot.write_html("docsrc/_generated/px.portfolio.intellect_struct.rpys.rpys_plot.html")


"""

import plotly.graph_objects as go  # type: ignore

from tm2p._intern import ParamsMixin
from tm2p.portfolio.intellect_struct.rpys.metr import Metrics


class RPYSPlot(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        df = Metrics().update(**self.params.__dict__).run()

        peaks = df.reset_index()
        peaks = peaks.sort_values(
            by=["PEAK", "MEDIAN", "YEAR"],
            ascending=[False, False, False],
        )
        peaks = peaks.head(self.params.rpys_peaks)

        n_gcr_max = df["N_GCR"].max() * 1.1
        y_mean_max = df["MEDIAN"].abs().max() * 1.1

        fig = go.Figure()

        fig.add_trace(
            go.Bar(
                x=df.index,
                y=df["N_GCR"],
                name="Number of cited references",
                opacity=0.4,
                marker_color="lightgrey",
                marker_line_color="darkslategray",
                marker_line_width=0.6,
            )
        )

        fig.add_trace(
            go.Scatter(
                x=peaks["YEAR"],
                y=peaks["MEDIAN"],
                mode="markers",
                name="Peaks",
                marker=dict(
                    size=16,
                    color="white",
                    line=dict(color="darkslategray", width=1.5),
                    symbol="circle",
                ),
                yaxis="y2",
                showlegend=True,
            )
        )

        fig.add_trace(
            go.Scatter(
                x=df.index,
                y=df["MEDIAN"],
                fill=None,
                mode="lines+markers",
                name="Median",
                marker=dict(size=8, color="darkslategray"),
                line=dict(color="darkslategray", width=1.5),
                yaxis="y2",
            )
        )

        fig.update_layout(
            paper_bgcolor="white",
            plot_bgcolor="white",
            title="Reference Spectroscopy",
            bargap=0.6,
            legend=dict(
                traceorder="reversed",
                x=0.01,
                y=0.99,
                xanchor="left",
                yanchor="top",
            ),
            yaxis=dict(
                title="Cited References",
                linecolor="lightgrey",
                linewidth=2,
                gridcolor="lightgray",
                griddash="dot",
                rangemode="tozero",
                fixedrange=False,
                range=[-n_gcr_max, n_gcr_max],
                tickvals=[i for i in range(0, int(n_gcr_max) + 10, 10)],
            ),
            yaxis2=dict(
                title="5-year median deviation",
                overlaying="y",
                side="right",
                showgrid=False,
                linecolor="lightgray",
                linewidth=2,
                zeroline=False,
                anchor="x",
                fixedrange=False,
                range=[-y_mean_max, y_mean_max],
            ),
        )

        fig.update_xaxes(
            linecolor="gray",
            linewidth=4,
            gridcolor="lightgray",
            griddash="dot",
            title="Reference publication year",
            tickangle=270,
            dtick=1,
        )

        fig.add_shape(
            type="line",
            x0=df.index.min(),
            x1=df.index.max(),
            y0=0,
            y1=0,
            yref="y2",
            xref="x",
            line=dict(color="darkslategray", width=1, dash="dash"),
        )

        for _, row in peaks.iterrows():
            fig.add_annotation(
                x=row["YEAR"],
                y=row["MEDIAN"],
                text=str(int(row["YEAR"])),
                yref="y2",
                showarrow=False,
                textangle=-90,
                xanchor="center",
                yanchor="bottom",
                font=dict(size=12, color="darkslategray", weight="bold"),
                yshift=14,
            )

        return fig
