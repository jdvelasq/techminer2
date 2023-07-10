# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _bradford_law_chart:

Bradford's Law Chart
===============================================================================



>>> import techminer2plus as tm2p
>>> root_dir = "data/regtech/"

>>> tm2p.bradford_law_chart(
...     root_dir=root_dir,
... ).write_html("sphinx/_static/bradford_law_chart.html")

.. raw:: html

    <iframe src="../_static/bradford_law_chart.html" height="600px" width="100%" frameBorder="0"></iframe>


"""


import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from .bradford_law_sources_by_zone import bradford_law_sources_by_zone


def bradford_law_chart(
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """Bradfor's Law"""

    indicators = bradford_law_sources_by_zone(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    fig = px.line(
        indicators,
        x="no",
        y="OCC",
        title="Source Clustering through Bradford's Law",
        markers=True,
        hover_data=[indicators.index, "OCC"],
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

    core = len(indicators.loc[indicators.zone == 1])

    fig.add_shape(
        type="rect",
        x0=1,
        y0=0,
        x1=core,
        y1=indicators.OCC.max(),
        line=dict(
            color="lightgrey",
            width=2,
        ),
        fillcolor="lightgrey",
        opacity=0.2,
    )

    fig.data = fig.data[::-1]

    return fig
