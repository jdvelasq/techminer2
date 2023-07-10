# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
RPYS Chart(Reference Publication Year Spectroscopy)
===============================================================================


>>> import techminer2plus as tm2p
>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/rpys.html"
>>> tm2p.rpys_chart(root_dir=root_dir).write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/rpys_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
import os.path

import pandas as pd
import plotly.graph_objects as go

from .rpys_table import rpys_table


def rpys_chart(
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """Reference Publication Year Spectroscopy."""

    indicator = rpys_table(root_dir=root_dir)

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=indicator.index,
            y=indicator["Num References"],
            fill="tozeroy",
            name="Num References",
            opacity=0.3,
            marker_color="lightgrey",  # darkslategray
        )
    )
    fig.add_trace(
        go.Scatter(
            x=indicator.index,
            y=indicator["Median"],
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
