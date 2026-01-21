# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Line Plot
===============================================================================


Example:
    >>> from techminer2.metrics.lotka_law import LinePlot

    >>> plotter = (
    ...     LinePlot()
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("examples/fintech/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ... )
    >>> plot = plotter.run()
    >>> plot.write_html("docs_source/_generated/px.database.metrics.lotka_law.line_plot.html")

.. raw:: html

    <iframe src="../_generated/px.database.metrics.lotka_law.line_plot.html"
    height="600px" width="100%" frameBorder="0"></iframe>


"""
import plotly.graph_objects as go  # type: ignore

from techminer2._internals.params_mixin import ParamsMixin
from techminer2.lotka.data_frame import DataFrame


class LinePlot(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""

        data_frame = DataFrame().update(**self.params.__dict__).run()

        fig = go.Figure()
        fig.add_trace(
            go.Scatter(
                x=data_frame["Documents Written"],
                y=data_frame["Proportion of Authors"],
                fill="tozeroy",
                name="Real",
                opacity=0.5,
                marker_color="darkslategray",
            )
        )
        fig.add_trace(
            go.Scatter(
                x=data_frame["Documents Written"],
                y=data_frame["Prop Theoretical Authors"],
                fill="tozeroy",
                name="Theoretical",
                opacity=0.5,
                marker_color="lightgrey",
            )
        )
        fig.update_layout(
            paper_bgcolor="white",
            plot_bgcolor="white",
            title="Author Productivity through Lotka's Law",
        )

        fig.update_traces(
            marker=dict(
                size=7,
                line=dict(color="darkslategray", width=2),
            ),
        )
        fig.update_xaxes(
            linecolor="gray",
            linewidth=2,
            gridcolor="lightgray",
            griddash="dot",
            title="Documents Written",
        )
        fig.update_yaxes(
            linecolor="gray",
            linewidth=2,
            gridcolor="lightgray",
            griddash="dot",
            title="Proportion of Authors",
        )

        return fig


#
