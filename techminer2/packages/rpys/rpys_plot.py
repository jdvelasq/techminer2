# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
RPYS (Reference Publication Year Spectroscopy) Plot
===============================================================================

>>> from techminer2.packages.rpys import RPYSPlot
>>> plot = (
...     RPYSPlot()
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     .run()
... )
>>> plot.write_html("docs_src/_generated/px.packages.rpys.rpys_plot.html")

.. raw:: html

    <iframe src="../_generated/px.packages.rpys.rpys_plot.html"
    height="800px" width="100%" frameBorder="0"></iframe>


"""
import plotly.graph_objects as go

from ..._internals.mixins import ParamsMixin
from .rpys_frame import RPYSDataFrame


class RPYSPlot(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        data_frame = RPYSDataFrame().update(**self.params.__dict__).run()

        fig = go.Figure()
        fig.add_trace(
            go.Scatter(
                x=data_frame.index,
                y=data_frame["Num References"],
                fill="tozeroy",
                name="Num References",
                opacity=0.3,
                marker_color="lightgrey",  # darkslategray
            )
        )
        fig.add_trace(
            go.Scatter(
                x=data_frame.index,
                y=data_frame["Median"],
                fill="tozeroy",
                name="Median",
                opacity=0.8,
                marker_color="darkslategray",
            )
        )
        fig.update_layout(
            paper_bgcolor="white",
            plot_bgcolor="white",
            title="Reference Spectroscopy",
        )

        fig.update_traces(
            marker=dict(
                size=6,
                line=dict(color="darkslategray", width=2),
            ),
        )
        fig.update_xaxes(
            linecolor="gray",
            linewidth=2,
            gridcolor="lightgray",
            griddash="dot",
        )
        fig.update_yaxes(
            linecolor="gray",
            linewidth=2,
            gridcolor="lightgray",
            griddash="dot",
            title="Cited References",
        )

        return fig
