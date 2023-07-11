# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Lotka's Law Chart
===============================================================================


>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/lotka_law_chart.html"
>>> import techminer2 as tm2
>>> tm2.lotka_law_chart(
...     root_dir=root_dir,
...     ).write_html(file_name)

.. raw:: html

    <iframe src="../../../../../../_static/lotka_law_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
import plotly.graph_objects as go

from .lotka_law_table import lotka_law_table


def lotka_law_chart(
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """Lotka's Law"""

    indicators = lotka_law_table(
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=indicators["Documents Written"],
            y=indicators["Proportion of Authors"],
            fill="tozeroy",
            name="Real",
            opacity=0.5,
            marker_color="darkslategray",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=indicators["Documents Written"],
            y=indicators["Prop Theoretical Authors"],
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
