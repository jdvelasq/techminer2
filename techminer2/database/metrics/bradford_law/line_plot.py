# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Line Plot
===============================================================================


Example:
    >>> from techminer2.database.metrics.bradford_law import LinePlot

    >>> plotter = (
    ...     LinePlot()
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("example/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ... )
    >>> plot = plotter.run()
    >>> plot.write_html("docs_source/_generated/px.database.metrics.bradford_law.line_plot.html")

.. raw:: html

    <iframe src="../_generated/px.database.metrics.bradford_law.line_plot.html"
    height="600px" width="100%" frameBorder="0"></iframe>


"""
import plotly.express as px  # type: ignore

from ...._internals.params_mixin import ParamsMixin
from .zones import ZonesDataFrame


class LinePlot(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""

        zones = ZonesDataFrame().update(**self.params.__dict__).run()

        fig = px.line(
            zones,
            x="no",
            y="OCC",
            title="Source Clustering through Bradford's Law",
            markers=True,
            hover_data=[zones.index, "OCC"],
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
            xaxis_title=None,
            xaxis_showticklabels=False,
        )
        fig.update_yaxes(
            linecolor="gray",
            linewidth=2,
            gridcolor="lightgray",
            griddash="dot",
        )
        fig.update_xaxes(
            linecolor="gray",
            linewidth=2,
            gridcolor="lightgray",
            griddash="dot",
            tickangle=270,
        )

        core = len(zones.loc[zones.zone == 1])

        fig.add_shape(
            type="rect",
            x0=1,
            y0=0,
            x1=core,
            y1=zones.OCC.max(),
            line=dict(
                color="lightgrey",
                width=2,
            ),
            fillcolor="lightgrey",
            opacity=0.2,
        )

        fig.data = fig.data[::-1]

        return fig
