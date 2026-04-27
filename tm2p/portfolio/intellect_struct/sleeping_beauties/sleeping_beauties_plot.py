"""
SleepingBeautiesPlot
===============================================================================

.. raw:: html

    <iframe src="../_generated/px.portfolio.intellect_struct.sleeping_beauties.sleeping_beauties_plot.html"
    height="800px" width="100%" frameBorder="0"></iframe>


Smoke tests:
    >>> from tm2p.portfolio.intellect_struct.sleeping_beauties import SleepingBeautiesPlot  # type: ignore
    >>> plot = (
    ...     SleepingBeautiesPlot()
    ...     #
    ...     .using_top_n_sleeping_beauties(10)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/system-dynamics-wos/")
    ...     .where_record_years_range(None, 2025)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     .run()
    ... )
    >>> plot.write_html("docsrc/_generated/px.portfolio.intellect_struct.sleeping_beauties.sleeping_beauties_plot.html")


"""

import pandas as pd  # type: ignore
import plotly.graph_objects as go  # type: ignore

from tm2p._intern import ParamsMixin

from .metr import Metrics
from .trajectories import Trajectories


class SleepingBeautiesPlot(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        # --- data ---
        metrics = Metrics().update(**self.params.__dict__).run()
        trajectory = Trajectories().update(**self.params.__dict__).run()

        top = metrics.head(self.params.top_n_sleeping_beauties)

        # --- color scale: darker = higher BC ---
        bc_min = top["BC"].min()
        bc_max = top["BC"].max()

        def bc_to_color(bc):
            t = (bc - bc_min) / (bc_max - bc_min) if bc_max > bc_min else 1.0
            # interpolate from lightsteelblue (low) to darkslategray (high)
            r = int(176 - t * (176 - 47))
            g = int(196 - t * (196 - 79))
            b = int(222 - t * (222 - 79))
            return f"rgb({r},{g},{b})"

        fig = go.Figure()

        for i, (_, row) in enumerate(top.iterrows()):
            doc_id = row["DOC"]
            pub_year = row["PUB_YEAR"]
            awakening_year = row["AWAKENING_YEAR"]
            bc = row["BC"]

            # --- slice trajectory from publication year ---
            traj = trajectory.loc[doc_id, pub_year:]
            cumulative = traj.cumsum()

            # --- normalize 0-1 ---
            c_max = cumulative.max()
            if c_max == 0:
                continue
            cumulative_norm = cumulative / c_max
            zero_year = pub_year - 1
            cumulative_norm = pd.concat(
                [
                    pd.Series({zero_year: 0.0}),
                    cumulative_norm,
                ]
            )

            color = bc_to_color(bc)

            # --- short label: "Author, Year" ---
            parts = doc_id.split(", ")
            label = f"{parts[0]}, {parts[1]}"

            # --- trajectory line ---
            fig.add_trace(
                go.Scatter(
                    x=cumulative_norm.index.tolist(),
                    y=cumulative_norm.values.tolist(),
                    mode="lines",
                    name=label,
                    line=dict(color=color, width=1.5),
                    showlegend=False,
                )
            )

            # --- dot at awakening year ---
            if awakening_year in cumulative_norm.index:
                fig.add_trace(
                    go.Scatter(
                        x=[awakening_year],
                        y=[cumulative_norm[awakening_year]],
                        mode="markers",
                        marker=dict(
                            size=8,
                            color=color,
                            line=dict(color="white", width=1),
                        ),
                        showlegend=False,
                    )
                )

            # --- label at end of line ---
            last_year = cumulative_norm.index[-1]
            last_val = cumulative_norm.iloc[-1]
            fig.add_annotation(
                x=last_year,
                y=last_val,
                text=f"<b>{label}</b>",
                showarrow=False,
                xanchor="left",
                yanchor="middle",
                xshift=6,
                yshift=i * -12,
                font=dict(size=9, color=color),
            )

        fig.update_layout(
            paper_bgcolor="white",
            plot_bgcolor="white",
            title="Sleeping Beauties — Cumulative Citation Trajectories",
        )

        fig.update_xaxes(
            linecolor="gray",
            linewidth=2,
            gridcolor="lightgray",
            griddash="dot",
            title="Year",
            dtick=1,
            tickangle=270,
            range=[trajectory.columns.min() - 1, trajectory.columns.max() + 3],
        )

        fig.update_yaxes(
            linecolor="gray",
            linewidth=2,
            gridcolor="lightgray",
            griddash="dot",
            title="Normalized cumulative citations",
            range=[0, 1.05],
        )

        return fig
