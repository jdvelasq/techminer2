"""
DistributionPlot
===============================================================================

.. raw:: html

    <iframe src="../_generated/px.portfolio.perform_metr.lotka.distrib_plot.html"
    height="600px" width="100%" frameBorder="0"></iframe>


Smoke tests:
    >>> from tm2p.portfolio.perform_metr.lotka import DistributionPlot  # type: ignore
    >>> fig = (
    ...     DistributionPlot()
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...      #
    ...      .run()
    ... )
    >>> assert type(fig).__name__ == 'Figure'
    >>> fig.write_html("docsrc/_generated/px.portfolio.perform_metr.lotka.distrib_plot.html")

    

"""

import plotly.graph_objects as go  # type: ignore

from tm2p._intern import ParamsMixin
from tm2p.portfolio.perform_metr.zipf.lotka.metr import Metrics


class DistributionPlot(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""

        df = Metrics().update(**self.params.__dict__).run()

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                x=df["N_DOCS"],
                y=df["PROP_AUTH_THEO"],
                mode="lines+markers",
                name="Theoretical",
                line=dict(width=2),
                marker=dict(
                    size=8,
                    color="gray",
                ),
                opacity=0.8,
            )
        )

        fig.add_trace(
            go.Scatter(
                x=df["N_DOCS"],
                y=df["PROP_AUTH_OBS"],
                mode="lines+markers",
                name="Observed",
                line=dict(width=3),
                marker=dict(
                    size=8,
                    color="darkslategray",
                ),
            )
        )

        fig.update_layout(
            paper_bgcolor="white",
            plot_bgcolor="white",
            title="Log-Log Author Productivity Distribution (Lotka’s Law)",
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1.0,
            ),
        )

        tickvals_x = [1, 2, 3, 4, 5] + list(range(10, df["N_DOCS"].max(), 10))
        ticktext_x = [str(x) for x in tickvals_x]

        fig.update_xaxes(
            linecolor="gray",
            linewidth=2,
            gridcolor="lightgray",
            griddash="dot",
            title="Number of Documents per Author",
            tick0=1,
            type="log",
            tickvals=tickvals_x,
            ticktext=ticktext_x,
        )

        tickvals_y = [
            0.00001,
            0.0001,
            0.001,
            0.002,
            0.003,
            0.004,
            0.005,
            0.01,
            0.02,
            0.03,
            0.04,
            0.05,
            0.1,
            0.2,
            0.3,
            0.4,
            0.5,
            0.8,
            1.0,
        ]

        ticktext_y = [str(x) for x in tickvals_y]

        fig.update_yaxes(
            linecolor="gray",
            linewidth=2,
            gridcolor="lightgray",
            griddash="dot",
            title="Proportion of Authors",
            type="log",
            tickvals=tickvals_y,
            ticktext=ticktext_y,
        )

        return fig
