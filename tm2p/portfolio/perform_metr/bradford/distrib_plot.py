"""
DistributionPlot
===============================================================================

.. raw:: html

    <iframe src="../_generated/px.portfolio.perform_metr.bradford.distribution_plot.html"
    height="600px" width="100%" frameBorder="0"></iframe>


Smoke tests:
    >>> from tm2p.portfolio.perform_metr.bradford import DistributionPlot  # type: ignore
    >>> (
    ...     DistributionPlot()
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... ).write_html("docsrc/_generated/px.portfolio.perform_metr.bradford.distribution_plot.html")



"""

import numpy as np  # type: ignore
import plotly.express as px  # type: ignore

from tm2p._intern import ParamsMixin
from tm2p.portfolio.perform_metr.bradford.zone_table import ZoneTable


class DistributionPlot(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        zones = ZoneTable().update(**self.params.__dict__).run()
        zones = zones.head(150).loc[zones["N_DOCS"] >= 2].copy()

        fig = px.line(
            zones,
            x="RANK",
            y="N_DOCS",
            title="Bradford Distribution of Sources",
            markers=True,
            hover_data=[zones.index, "N_DOCS"],
            log_x=True,
        )

        fig.update_traces(
            marker=dict(size=5, line=dict(color="darkslategray", width=1)),
            marker_color="rgb(171,171,171)",
            line=dict(color="darkslategray"),
        )

        fig.update_layout(
            paper_bgcolor="white",
            plot_bgcolor="white",
            xaxis_showticklabels=True,
            # margin=dict(b=320),
        )

        fig.update_yaxes(
            linecolor="gray",
            linewidth=2,
            gridcolor="lightgray",
            griddash="dot",
            title="Number of Documents",
        )

        fig.update_xaxes(
            linecolor="gray",
            linewidth=2,
            gridcolor="lightgray",
            griddash="dot",
            tickangle=0,
            title="Source Rank (log scale)",
            tickvals=[1, 2, 5, 10, 20, 50, 100, 150],
            ticktext=["1", "2", "5", "10", "20", "50", "100", "150"],
            range=[0, np.log10(zones["RANK"].max())],
        )

        core = zones.loc[zones["ZONE"] == 1, "RANK"].max()

        fig.add_shape(
            type="rect",
            x0=1,
            y0=0,
            x1=core,
            y1=zones["N_DOCS"].max(),
            line=dict(color="lightgrey", width=2),
            fillcolor="lightgrey",
            opacity=0.2,
            layer="below",
        )

        fig.add_vline(
            x=core,
            line_dash="dash",
            line_color="gray",
        )

        top_core = zones.loc[zones["ZONE"] == 1].head(10)

        for idx, (_, row) in enumerate(top_core.iterrows()):
            fig.add_annotation(
                x=np.log10(row["RANK"]),
                y=row["N_DOCS"],
                text=row.name,
                showarrow=True,
                arrowhead=2,
                ax=45 if idx < 5 else -25,
                ay=-25 if idx < 5 else 25 + 5 * (idx - 5),
                xanchor="left" if idx < 5 else "right",
                yanchor="bottom" if idx < 5 else "top",
                font=dict(size=11),
                bgcolor="rgba(255,255,255,0.75)",
                bordercolor="lightgray",
                borderwidth=1,
                borderpad=4,
            )

        fig.add_annotation(
            x=0.05,
            y=0.44,
            xref="paper",
            yref="paper",
            text="Bradford core<br>Zone 1",
            showarrow=False,
            font=dict(size=14),
        )

        # fig.data = fig.data[::-1]

        return fig
